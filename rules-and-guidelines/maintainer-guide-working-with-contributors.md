# Hiero Maintainer Guide: Working with Contributors

> A practical handbook for maintainers across the [`hiero-ledger`](https://github.com/hiero-ledger) repositories on how to welcome new contributors,
set healthy boundaries, and protect the project from low-effort or AI-generated noise — without losing the open spirit that makes open source work.

This guide is **for Hiero maintainers**.
It is a companion to each repository's `CONTRIBUTING.md`, which is written for contributors.
If you are a contributor looking for how to get involved, please start with the [Hiero organization README](https://github.com/hiero-ledger) and the `CONTRIBUTING.md`
in the repository you want to contribute to.

This document operates under the authority of the [Hiero Project Charter](../hiero-technical-charter.md) and complements the existing Hiero governance documents
It follows the open-source norms of [LF Decentralized Trust (LFDT)](https://www.lfdecentralizedtrust.org/).

## Why This Guide Exists

Hiero depends on a social contract between maintainers and contributors.
Contributions are made in good faith, and experienced maintainers help with review, mentorship, and integration.
As an LFDT project, Hiero is committed to open governance and vendor-neutral collaboration, and that openness is one of our strongest assets.

Generative AI has changed the balance of this contract.
Several of our 28+ Hiero repositories now receive a growing number of contributions that:

- Were created without understanding the project, its roadmap, or its community.
- Solve problems that were never raised by users, contributors, or the TSC.
- Are produced by AI tools and submitted without meaningful human review.
- Bundle large structural changes into a single PR without prior discussion in TSC, community calls, or HIPs.

This pattern is often called **AI slop**.
It is rarely malicious — most contributors mean well — but the cumulative effect on Hiero maintainer time and morale is severe.
Maintainers across LFDT and other Linux Foundation projects have reported the review burden tipping into "demoralizing" territory.

This guide gives Hiero maintainers a shared playbook so you do not have to invent a response every time.
It applies to every repository in the `hiero-ledger` organization.

## Core Principles

When in doubt, return to these:

- **Assume good intent first.** Most over-eager contributors are not bad actors.
  They are new, excited, or unfamiliar with open source norms. A short pointer to our guidelines is often enough.
- **Protect your time and energy.** You cannot mentor everyone. Triage ruthlessly, mentor selectively.
- **Be kind, be clear, be brief.** Friendly tone, unambiguous message, no long essays.
- **Refer, do not repeat.** Always link to written guidelines (this guide, the repo's `CONTRIBUTING.md`) or good-first-issue labels rather than re-explaining in every PR.
- **Quality over quantity.** Throughput of merged PRs is not a measure of Hiero's health.
- **Issues are cheap, PRs are expensive.** Encourage discussion in our [community Discord](https://discord.gg/kEnnmB9A) or at the next
  [Hiero community call](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week) before code.

## Triage: The First 5 Minutes

When a new PR or issue arrives from an unfamiliar contributor, the following checklist will help you to decide how to respond:

1. **Is this linked to an existing, accepted issue?** If not, the PR is a proposal, not a fix. Treat accordingly.
2. **Is the contributor known?** Check their history in the `hiero-ledger` org and on GitHub more broadly. Have they been seen in TSC or community calls? In Discord?
3. **Does the scope match a single, focused change?** Or does it touch many unrelated areas?
4. **Does the description show understanding of the project?** Or does it read as generic AI-generated boilerplate?
5. **Is the change aligned with the current roadmap?** Substantial changes should follow the [Hiero Improvement Proposal (HIP)](https://github.com/hiero-ledger/hiero-improvement-proposals) process.
  If not aligned, even a perfect implementation should not be merged now.
6. **DCO check.** All commits must be signed off under the [Developer Certificate of Origin](https://developercertificate.org/).
  If they are not, that is the first thing to fix — regardless of everything else.

Based on this, pick a response from [Section 6](#6-response-templates).

## Red Flags

These are signals — not proofs — that a contribution is low-effort or AI-generated. Several flags together warrant the structured response in Section 5.

**Pattern flags:**

- The contributor opened the issue and the PR themselves within minutes, with no community discussion in between.
- Multiple large PRs from the same contributor in a short time window, each touching different parts of the codebase.
- The contributor has a thin or recently-inflated GitHub history.
- PRs across multiple unrelated Hiero repos with similar structure or wording — or the same pattern across other LFDT projects.
- The contributor has never appeared in Discord, community calls, or TSC meetings.

**Content flags:**

- PR descriptions with generic structure ("Description / Problem / Solution / Testing") but vague substance.
- Claims like "I conducted a white-box security review" or "I refactored the entire error handling" without prior issue or community discussion.
- Adding heavyweight features (distributed tracing, full exception hierarchies, framework refactors) without any user demand or HIP.
- Conversion of a library into a "standalone application" or similar architectural rewrite.
- Code that compiles but does not match existing patterns, naming conventions, or test style of the affected Hiero repo.
- Tests that exist but do not actually verify the new behavior.

**Communication flags:**

- Responses to review comments arrive instantly and address the wording rather than the substance.
- Pushback that ignores the maintainer's point and repeats the original argument.
- The contributor cannot explain a specific technical decision in their own PR.

## The Escalation Ladder

Use this in order. Move down only if the previous step does not change the behavior. The tone stays friendly throughout — only the consequences change.

### Step 1 — Welcome and Redirect (always start here)

Friendly comment pointing the contributor at the repo's `CONTRIBUTING.md`, the Hiero org overview, good-first-issues, Discord, and community meetings.
Close or convert the PR to draft if scope is wrong. See template **T1**.

### Step 2 — Set Clear Expectations

If the contributor returns with more out-of-scope PRs, respond once more with clear, specific guidance:
which issues are appropriate, what PR limit applies, what discussion must happen first (community call, HIP, or `needs-discussion` issue). See template **T2**.

### Step 3 — Pause Contributions

If behavior does not change after Step 2, close open PRs from this contributor with a final message stating that further submissions on out-of-scope topics will be closed
without review until they engage with the Hiero community first. See template **T3**.

### Step 4 — Hard Stop

Apply GitHub's [interaction limits](https://docs.github.com/en/communities/moderating-comments-and-conversations/limiting-interactions-in-your-repository) at the user or repository level.
Document the decision in the maintainer Discord channel and notify the TSC via the [`hiero-ledger/tsc`](https://github.com/hiero-ledger/tsc) repo. For organization-wide patterns,
escalate to the TSC for a coordinated response.

> Stay friendly and factual at every step. We are an LFDT project — our public behavior is part of Hiero's reputation.

## Response Templates

Copy, adapt, post. Replace `{placeholders}` before sending. Keep your own voice; do not paste verbatim if it feels robotic.

### T1 — Welcome and Redirect (out-of-scope PR or self-created issue)

> Thanks for your interest in Hiero and for taking the time to open this!
>
> Before we look at the code itself, a quick note on how contributions work here:
> changes of this size and scope need to be discussed with the community first, so we can align them with the roadmap and with what other maintainers and users are working on.
> The issue linked here was opened by you alongside the PR, so it has not yet been discussed by the community.
>
> The best way to get started with Hiero is:
>
> 1. Browse our [issue explorer at hiero.org/issues](https://hiero.org/issues) — it groups open issues by skill level (**Good First Issue**, **Beginner**, **Intermediate**, **Advanced**) across all `hiero-ledger` repos, so you can find something that matches your experience.
> 2. Join the [Hiero community](https://github.com/hiero-ledger) — say hi on our [Discord](https://discord.gg/kEnnmB9A), and join the next community call from our [public calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week).
> 3. For larger ideas, open a [GitHub Discussion]({discussions-link}) or an issue first — not a PR. For features that change Hiero's behavior at the protocol or API level, the right path is a [HIP](https://github.com/hiero-ledger/hiero-improvement-proposals).
>
> I'll close this PR for now. That is not a rejection of you — it is how we keep the project healthy. Once you have spent some time in the community and understand where Hiero is heading, you are very welcome to revisit this idea. Looking forward to working with you!

### T2 — Set Clear Expectations (repeat behavior)

> Thanks for the follow-up PRs. I want to be transparent with you about where we are:
>
> The changes you are proposing (e.g. {short list}) are substantial and were not requested by users, maintainers, or the TSC roadmap. Even if the code itself is fine, we cannot merge architectural changes that have not been discussed.
>
> Please:
>
> - Pause new PRs for now.
> - Pick **one** task from our [issue explorer](https://hiero.org/issues) — start at the **Good First Issue** or **Beginner** level and work through it end-to-end.
> - Join the next Hiero community call ([calendar here](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week)) or drop into our [Discord](https://discord.gg/kEnnmB9A).
>
> This is the path that has worked for every long-term Hiero contributor. I am happy to mentor you through it — but I cannot mentor four parallel large PRs. Let's start small.

### T3 — Pause Contributions (no change after T2)

> I'm closing this PR along with the others currently open from you.
>
> We have asked twice to slow down and engage with the Hiero community before submitting large changes. That has not happened, and continuing to review PRs that are not aligned with the project costs the maintainer team time we don't have.
>
> Further PRs on out-of-scope topics will be closed without review until you have:
>
> - Participated in at least one Hiero community call or TSC meeting, or
> - Successfully completed one issue from our [issue explorer](https://hiero.org/issues) at the **Good First Issue** or **Beginner** level.
>
> This is not personal and the door is not shut. We just need the order of operations to be right. Thanks for understanding.

### T4 — AI-Generated Content Suspected

> Thanks for the PR. Before we go further: parts of this change (description, commit messages, code patterns) suggest significant AI assistance. That is allowed in Hiero, but only under our policy:
>
> - You, as the human author, take full responsibility for the contribution and have signed off under the [DCO](https://developercertificate.org/).
> - You have reviewed every change line by line and can explain and defend it.
> - The work solves a real problem from our issue tracker, not one invented by the tool.
>
> Could you confirm this, and could you walk us through {specific technical decision in the PR}? If you can, great — let's continue. If not, please withdraw the PR and start with a task from our [issue explorer](https://hiero.org/issues) instead.

**Maintainer note:** If a PR is clearly AI-generated spam — no meaningful engagement, no understanding of the codebase, possibly part of a pattern — apply the `spam` label per the [Good First Issue Guidelines](https://github.com/hiero-ledger/governance/blob/main/rules-and-guidelines/good-first-issues.md). Multiple spam-labeled PRs from one contributor are grounds for org-wide interaction limits and Hacktoberfest exclusion.

### T5 — Self-Created Issue Without Community Demand

> Thanks for the suggestion! Just to set expectations: this issue was opened by you and has not yet been raised by users, maintainers, or the TSC. We keep issues open in Hiero as long as they reflect real demand or align with the roadmap.
>
> I'll leave it open for {2–4 weeks} so the community can weigh in. If there is no interest in that time, we'll close it. In the meantime, please do not open a PR for it — we want the discussion to happen first. If this is a substantial change to Hiero's behavior, the right place to propose it is a [HIP](https://github.com/hiero-ledger/hiero-improvement-proposals).

### T6 — Closing a Stale or Speculative Issue

> Closing this as there has been no community interest and it is not on the current Hiero roadmap. This is not a judgement on the idea — it just means there is no one to maintain it right now. Feel free to reopen if circumstances change or if it picks up traction in a discussion or at a community call.

## Repository Hygiene

Every repository in `hiero-ledger` should have the following in place. The org-wide configuration already enforces some of these — but the rest is up to each repo's maintainers. Open an issue in your repo if any are missing.

**Required files:**

- `CONTRIBUTING.md` — how to contribute, link to this guide.
- `CODE_OF_CONDUCT.md` — the [LFDT Code of Conduct](https://lfdecentralizedtrust.org/code-of-conduct).
- `SECURITY.md` — pointing to Hiero's security reporting process. Never report security issues in public.
- `.github/PULL_REQUEST_TEMPLATE.md` — requires linked issue, scope description, human-author confirmation, and DCO sign-off reminder.
- `.github/ISSUE_TEMPLATE/` — at least a bug report, a feature request, and a question template.

**Required labels:**

The Hiero [Good First Issue Guidelines](https://github.com/hiero-ledger/governance/blob/main/rules-and-guidelines/good-first-issues.md) define the org-wide standard labels for newcomer-friendly work:

- `good first issue candidate` — issues that may become a good first issue but need more description first.
- `good first issue` — reviewed and ready, ideal for first-time contributors.
- `non-code` — issues that can be solved without coding (e.g. documentation).
- `spam` — irrelevant, low-quality, or AI-generated PRs/issues. Multiple spam labels per contributor lead to Hacktoberfest exclusion and may trigger interaction limits.
- `hacktoberfest-accepted` — applied to PRs that count toward Hacktoberfest.

In addition, the [hiero.org issue explorer](https://hiero.org/issues) groups issues by skill level. To make your repo discoverable there, also use:

- `skill: good first issue` (or `good first issue`)
- `skill: beginner` (or `beginner`)
- `skill: intermediate` (or `intermediate`)
- `skill: advanced` (or `advanced`)

For this maintainer workflow, we additionally recommend:

- `help wanted` — issues the team would welcome help on.
- `needs discussion` — for proposals that must be discussed before any PR.
- `community-needs-review` — for PRs or issues that should be picked up in the next shared review slot.
- `out of scope` — for issues we will not pursue.
- `ai-assisted` — optional, for transparency on PRs that disclose AI use.

**Repository settings:**

- DCO check enforced on all commits (org-wide).
- Require linked issues for PRs where possible.
- Require at least one maintainer review before merge.
- Restrict who can trigger CI on PRs from first-time contributors.
- Consider enabling interaction limits during incidents.

**Documented policies in `CONTRIBUTING.md`:**

- PR scope: one logical change per PR.
- No more than {2} open PRs per contributor at a time, unless agreed otherwise.
- Large changes require a prior discussion or an issue with the `needs-discussion` label. Protocol- or API-level changes require a HIP.
- AI-assisted contributions are welcome but must be disclosed, and the human author is fully responsible.
- All commits must be DCO-signed.

## Handling Specific Situations

**Contributor opens issue and PR simultaneously.**
Treat the issue as a proposal, not as community-validated demand. Apply T1.

**Contributor pushes back on review with AI-style replies.**
Ask a specific technical question that requires understanding of the codebase. If the answer does not address it, apply T2 or T3.

**Contributor's PR is technically fine but unwanted.**
"Good code, wrong project state" is a valid reason to close. Use T1 and be explicit: this is about timing and scope, not quality.

**Multiple maintainers disagree on how to respond.**
Discuss in the maintainer Discord channel or the next TSC call before replying. A unified response is better than a fast one.

**Contributor is well-known and respected in Hiero.**
The same rules apply, but tone can be more informal. Long-standing contributors should still link to issues and stay in scope — leading by example matters, especially in an LFDT project that other communities watch.

**You suspect coordinated or automated abuse.**
Do not engage publicly. Bring it to the TSC immediately and consider org-wide interaction limits across `hiero-ledger`.

**The PR touches another Hiero repo's responsibility.**
Loop in maintainers of that repo via Discord or a cross-repo issue before merging. Avoid surprises across the `hiero-ledger` org.

**It's October (Hacktoberfest).**
Expect a noticeable spike in PRs — many from first-time contributors. Be extra welcoming for genuine attempts (this is often someone's first ever PR), and don't hesitate to apply the `spam` label to obviously AI-generated submissions per the [Good First Issue Guidelines](https://github.com/hiero-ledger/governance/blob/main/rules-and-guidelines/good-first-issues.md#hacktoberfest). When merging valid PRs, remember to add `hacktoberfest-accepted` so the contribution counts.

## Self-Care for Maintainers

This part is not optional.

- **You are allowed to not respond immediately.** A PR sitting for a few days is fine. Consider adding a `community-needs-review` label and scheduling one fixed slot per week to walk through everything that has accumulated. This works even better as a shared session — with your co-maintainers in the same Hiero repo, or across repositories with maintainers from other `hiero-ledger` projects. Most of these decisions are not deeply technical; they are about scope, roadmap fit, and community process, so a second pair of eyes from a neighboring Hiero project is often just as useful as a domain expert. If you are unsure how to handle a specific case, you can always reach out to the TSC or to the TSC Chair (Hendrik Ebbers) directly — that is what we are here for.
- **You are allowed to close PRs — but always with a message.** Closing is not rejecting the person, but a silent close feels exactly like rejection. Just as we expect contributors to communicate with us (linked issues, clear descriptions, responses to review), they can expect the same from us. A short, friendly note explaining *why* you are closing — and pointing to what would be welcome instead — is the minimum. Templates T1, T3, and T6 are there for exactly this.
- **You are allowed to say "not now."** Roadmap alignment is a legitimate reason in Hiero. The HIP process exists precisely so big ideas can wait for the right moment.
- **You are not obligated to mentor everyone.** Pick the contributors who engage with the community.
- **Talk to other maintainers.** This guide exists because we share these problems across the `hiero-ledger` org.

If you are feeling the review burden tipping into "demoralizing" territory, raise it in the maintainer Discord channel or with the TSC early. We adjust the policies, not the people.

## Escalation Paths Inside Hiero

When this guide is not enough:

- **First stop:** your repo's co-maintainers, via Discord or a private channel.
- **Cross-repo questions:** the `#hiero-maintainers` Discord channel.
- **Governance, policy, or repeated abuse:** the [Hiero TSC](https://github.com/hiero-ledger/tsc). Open an issue in the TSC repo or raise it at the next TSC call (see the [Hiero public calendar](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week)).
- **Code of Conduct violations:** follow the LFDT process — do not handle these on your own.
- **Security issues:** never public. Use the `SECURITY.md` reporting path of the affected repo.
