#!/usr/bin/env python3
"""Vote required status check for hiero-ledger/governance.

Compares the ``config.yaml`` team membership between a pull request's
merge-base and its head.  When members or maintainers of an existing team are
added or removed, the pull request must carry a passed GitVote before it can be
merged.  The result is published as the commit status ``Vote required`` on the
pull request head, which is meant to be a required status check on ``main``.

Decision table
--------------
no membership change               -> success
``vote-exempt`` label by maintain+ -> success (GitHub maintainers, TSC, LF staff workaround)
GitVote passed, same role changes  -> success
GitVote passed, role changes moved -> failure (re-run the vote)
GitVote open                       -> pending
GitVote failed / none / cancelled  -> failure

Only data files from the pull request are read (``config.yaml``), parsed with
``yaml.safe_load``.  No code from the pull request is executed.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass, field
from datetime import datetime, timezone

import yaml

API = "https://api.github.com"
STATUS_CONTEXT = "Vote required"
EXEMPT_LABEL = "vote-exempt"
GITVOTE_LOGIN = "git-vote[bot]"
SUMMARY_MARKER = "<!-- vote-required-summary -->"
EXEMPT_ROLES = {"admin", "maintain"}
ROLE_FIELDS = ("maintainers", "members")

# --------------------------------------------------------------------------- #
# GitHub REST helpers
# --------------------------------------------------------------------------- #


class GitHub:
    def __init__(self, repo: str, token: str) -> None:
        self.repo = repo
        self.token = token

    def _request(self, method: str, path: str, body: dict | None = None):
        url = path if path.startswith("http") else f"{API}{path}"
        data = json.dumps(body).encode() if body is not None else None
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("Accept", "application/vnd.github+json")
        req.add_header("X-GitHub-Api-Version", "2022-11-28")
        if self.token:
            req.add_header("Authorization", f"Bearer {self.token}")
        if data is not None:
            req.add_header("Content-Type", "application/json")
        with urllib.request.urlopen(req, timeout=30) as resp:
            payload = resp.read()
            link = resp.headers.get("Link", "")
        return (json.loads(payload) if payload else None), link

    def get(self, path: str):
        return self._request("GET", path)[0]

    def paginate(self, path: str) -> list:
        sep = "&" if "?" in path else "?"
        url = f"{API}{path}{sep}per_page=100"
        items: list = []
        while url:
            page, link = self._request("GET", url)
            items.extend(page)
            match = re.search(r'<([^>]+)>;\s*rel="next"', link)
            url = match.group(1) if match else None
        return items

    def post(self, path: str, body: dict):
        return self._request("POST", path, body)[0]

    # Convenience wrappers ------------------------------------------------- #
    def pull(self, number: int) -> dict:
        return self.get(f"/repos/{self.repo}/pulls/{number}")

    def comments(self, number: int) -> list:
        return self.paginate(f"/repos/{self.repo}/issues/{number}/comments")

    def labels(self, number: int) -> set[str]:
        return {l["name"] for l in self.paginate(f"/repos/{self.repo}/issues/{number}/labels")}

    def timeline(self, number: int) -> list:
        return self.paginate(f"/repos/{self.repo}/issues/{number}/timeline")

    def role_name(self, user: str) -> str:
        try:
            return self.get(f"/repos/{self.repo}/collaborators/{user}/permission").get("role_name", "")
        except urllib.error.HTTPError:
            return ""

    def set_status(self, sha: str, state: str, description: str, target_url: str | None) -> None:
        body = {"state": state, "context": STATUS_CONTEXT, "description": description[:140]}
        if target_url:
            body["target_url"] = target_url
        self.post(f"/repos/{self.repo}/statuses/{sha}", body)

    def comment(self, number: int, body: str) -> None:
        self.post(f"/repos/{self.repo}/issues/{number}/comments", {"body": body})


# --------------------------------------------------------------------------- #
# config.yaml membership diff
# --------------------------------------------------------------------------- #


def load_teams(path: str) -> dict[str, dict[str, set[str]]]:
    with open(path, encoding="utf-8") as fh:
        data = yaml.safe_load(fh) or {}
    teams: dict[str, dict[str, set[str]]] = {}
    for team in data.get("teams") or []:
        if not isinstance(team, dict) or "name" not in team:
            continue
        teams[str(team["name"])] = {
            role: {str(u) for u in (team.get(role) or [])} for role in ROLE_FIELDS
        }
    return teams


@dataclass
class Diff:
    changes: list[tuple[str, str, str, str]] = field(default_factory=list)  # (sign, team, role, user)
    added_teams: list[str] = field(default_factory=list)
    removed_teams: list[str] = field(default_factory=list)

    @property
    def requires_vote(self) -> bool:
        return bool(self.changes)

    @property
    def teams(self) -> list[str]:
        return sorted({team for _, team, _, _ in self.changes})

    def canonical(self) -> str:
        lines = [f"{sign} {team} {role}: {user}" for sign, team, role, user in sorted(self.changes)]
        return "\n".join(lines)


def membership_diff(base: dict, head: dict) -> Diff:
    diff = Diff()
    for name in sorted(set(base) | set(head)):
        if name not in base:
            diff.added_teams.append(name)
            continue
        if name not in head:
            diff.removed_teams.append(name)
            continue
        for role in ROLE_FIELDS:
            for user in sorted(head[name][role] - base[name][role]):
                diff.changes.append(("+", name, role, user))
            for user in sorted(base[name][role] - head[name][role]):
                diff.changes.append(("-", name, role, user))
    return diff


# --------------------------------------------------------------------------- #
# GitVote state, exemption label, and voted snapshot
# --------------------------------------------------------------------------- #


def parse_time(value: str) -> datetime:
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(timezone.utc)


@dataclass
class VoteState:
    state: str = "none"  # none | open | passed | failed | cancelled
    created_at: datetime | None = None
    closed_at: datetime | None = None


def gitvote_state(comments: list) -> VoteState:
    vote = VoteState()
    for c in sorted(comments, key=lambda c: c["created_at"]):
        if c.get("user", {}).get("login") != GITVOTE_LOGIN:
            continue
        body = c.get("body") or ""
        when = parse_time(c["created_at"])
        if body.startswith("## Vote created"):
            vote = VoteState("open", when, None)
        elif body.startswith("## Vote cancelled"):
            vote = VoteState("cancelled", vote.created_at, when)
        elif body.startswith("## Vote closed"):
            passed = "The vote **passed**" in body and "did not pass" not in body
            vote = VoteState("passed" if passed else "failed", vote.created_at, when)
    return vote


def exemption(gh: GitHub, number: int, labels: set[str], dry_run: bool) -> tuple[bool, str]:
    """Return (exempt, actor).  The label only counts when its last applier
    holds the ``maintain`` or ``admin`` role on this repository."""
    if EXEMPT_LABEL not in labels:
        return False, ""
    actor = ""
    for event in gh.timeline(number):
        if event.get("event") == "labeled" and event.get("label", {}).get("name") == EXEMPT_LABEL:
            actor = (event.get("actor") or {}).get("login", "")
    if not actor:
        return False, ""
    role = gh.role_name(actor)
    return role in EXEMPT_ROLES, f"{actor} ({role or 'unknown'})"


def summary_body(diff: Diff, head_sha: str) -> str:
    lines = [SUMMARY_MARKER, "### Role changes under vote", ""]
    lines.append("This pull request changes team membership in `config.yaml`. "
                 "Per [roles-and-groups.md](https://github.com/hiero-ledger/governance/blob/main/roles/roles-and-groups.md#voting) "
                 "a passed GitVote is required before it can be merged. The vote covers exactly these changes:")
    lines += ["", "```diff", diff.canonical(), "```", ""]
    if diff.added_teams or diff.removed_teams:
        lines.append("Structural changes not covered by this check (handled by the TSC project process): "
                     + ", ".join([f"new team `{t}`" for t in diff.added_teams]
                                 + [f"removed team `{t}`" for t in diff.removed_teams]) + ".")
        lines.append("")
    lines.append(f"<sub>Recorded for head `{head_sha[:7]}`. If the role changes above change after the vote closes, "
                 f"the `{STATUS_CONTEXT}` check fails until the vote is re-run.</sub>")
    return "\n".join(lines)


def recorded_snapshot(body: str) -> str:
    match = re.search(r"```diff\n(.*?)\n```", body, re.S)
    return match.group(1).strip() if match else ""


def summary_comments(comments: list) -> list:
    return sorted((c for c in comments if SUMMARY_MARKER in (c.get("body") or "")),
                  key=lambda c: c["created_at"])


def profile_hint(gh: GitHub, teams: list[str]) -> str:
    """Best-effort hint for the GitVote profile that matches the changed team."""
    try:
        content = gh.get("/repos/hiero-ledger/.github/contents/.gitvote.yml")
        import base64
        profiles = set((yaml.safe_load(base64.b64decode(content["content"])) or {}).get("profiles") or {})
    except Exception:  # noqa: BLE001 - hint only
        profiles = set()
    for team in teams:
        project = re.sub(r"-(junior-committers|committers|maintainers)$", "", team)
        parts = project.split("-")
        camel = parts[0] + "".join(p.capitalize() for p in parts[1:]) + "Maintainers"
        if camel in profiles:
            return f"/vote-{camel}"
    return "/vote-<profile> (see .gitvote.yml)"


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", required=True, help="owner/name of the governance repository")
    ap.add_argument("--pr", required=True, type=int)
    ap.add_argument("--base-config", required=True, help="config.yaml at the merge-base")
    ap.add_argument("--head-config", required=True, help="config.yaml at the PR head")
    ap.add_argument("--run-url", default=os.environ.get("RUN_URL"))
    ap.add_argument("--dry-run", action="store_true", help="print the decision, do not write to GitHub")
    args = ap.parse_args()

    gh = GitHub(args.repo, os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN") or "")
    pr = gh.pull(args.pr)
    head_sha = pr["head"]["sha"]

    base_teams, head_teams = load_teams(args.base_config), load_teams(args.head_config)
    if not base_teams or not head_teams:
        # An empty team list means the file could not be read properly; never
        # report success on that basis.
        msg = "Could not read teams from config.yaml at merge-base or head; check the workflow logs."
        print(f"error: {msg}", file=sys.stderr)
        if not args.dry_run:
            gh.set_status(head_sha, "error", msg, args.run_url)
        return 1

    diff = membership_diff(base_teams, head_teams)
    print(f"PR #{args.pr} head {head_sha[:7]}: {len(diff.changes)} membership change(s), "
          f"{len(diff.added_teams)} new team(s), {len(diff.removed_teams)} removed team(s)")
    if diff.changes:
        print(diff.canonical())

    state, description = "success", "No team membership changes in config.yaml; no vote required."

    if diff.requires_vote:
        comments = gh.comments(args.pr)
        labels = gh.labels(args.pr)
        vote = gitvote_state(comments)
        exempt, actor = exemption(gh, args.pr, labels, args.dry_run)
        print(f"gitvote: {vote.state}; exempt: {exempt} {actor}")

        # Keep the voted snapshot on the PR so voters (and this check) know what the vote covers.
        existing = summary_comments(comments)
        if not existing or recorded_snapshot(existing[-1]["body"]) != diff.canonical():
            if args.dry_run:
                print("would post role-change summary comment")
            else:
                gh.comment(args.pr, summary_body(diff, head_sha))

        if exempt:
            state, description = "success", f"Exempt from vote: label {EXEMPT_LABEL} applied by {actor}."
        elif vote.state == "passed":
            before_close = [c for c in existing if parse_time(c["created_at"]) <= vote.closed_at]
            if before_close and recorded_snapshot(before_close[-1]["body"]) != diff.canonical():
                state, description = "failure", "Role changes differ from the voted ones; re-run the vote or let a GitHub maintainer apply vote-exempt."
            else:
                state, description = "success", f"GitVote passed on {vote.closed_at:%Y-%m-%d}; role changes match the voted snapshot."
        elif vote.state == "open":
            state, description = "pending", f"GitVote in progress for {len(diff.changes)} role change(s); waiting for the result."
        elif vote.state == "failed":
            state, description = "failure", "GitVote did not pass. GitHub maintainers or the TSC may apply vote-exempt if the written rule says otherwise."
        else:
            hint = profile_hint(gh, diff.teams)
            state, description = "failure", f"Vote required for {len(diff.changes)} role change(s): comment {hint}, or GitHub maintainers apply vote-exempt."

    print(f"status: {state} - {description}")
    if args.dry_run:
        return 0
    gh.set_status(head_sha, state, description, args.run_url)
    return 0


if __name__ == "__main__":
    sys.exit(main())
