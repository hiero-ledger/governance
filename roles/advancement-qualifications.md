# Advancement Qualifications

This document defines the pillars a Contributor should demonstrate to be nominated as a Junior Committer, Committer, or Maintainer.
The pillars, and what counts in each, apply across Hiero.
The thresholds, such as how many merged pull requests, are set by each project and published in its MAINTAINERS.md.

## Principles

- Every counted activity is open to any developer. No role or approval is needed to start.
- Thresholds are a floor for consideration, not an entitlement.
- Sustained contribution over months outweighs a burst of activity.
- Depth in one area can substitute for breadth, where the role will be exercised in that area.
- Roles are held, not banked. The inactivity and removal rules in [Roles and Groups](./roles-and-groups.md) apply.

## Contribution categories

| Category | What counts | Permissions needed | Where to check |
| --- | --- | --- | --- |
| **Authoring** | Merged pull requests | None | PR list, filtered by author; Hiero Analytics |
| **Reviewing** | Pull request reviews containing substantive findings, questions, or signing or workflow compliance | None | PR list, filtered by reviewer; Hiero Analytics |
| **Issue authorship** | Well-formed bug reports, proposals, and follow-ups opened by the Contributor | None | Issue list, filtered by author; Hiero Analytics |
| **Community support** | Answering questions and unblocking other contributors, in GitHub Discussions, issue threads, or community channels, and taking part in community meetings | None | Discussions and issue timelines; community meeting minutes; Hiero Analytics |
| **Triage** | Reproducing reported issues, identifying duplicates, routing an issue to the right project, and judging whether an issue is still relevant | None to do it in a comment; **Triage** role to apply the label, close, assign, or mark a duplicate | Issue timeline and LFDT discord; Hiero Analytics |

Authoring counts merged pull requests, not opened ones, unless a project says otherwise.

## Pillars by role

Each table lists what is counted for the role.
The project sets the threshold for every row.

### Junior Committer

The role is lightweight by design, and the barrier is kept low.

| Pillar | What is counted |
| --- | --- |
| Presence | Weeks of regular activity |
| Authoring | Merged pull requests |
| Reviewing | Reviews that raised a finding or question, or confirmed the change matches its issue and its tests pass |
| Triage and issues | Issues triaged in a comment, or opened and accepted as valid |

Also weighed: helping other contributors; responding to review on their own pull requests; following the contribution guidelines and code of conduct.

### Committer

A Committer merges the work of others, so reviewing carries the most weight.

| Pillar | What is counted |
| --- | --- |
| Standing | Junior Committer on the project, except under the exceptional nominations described below |
| Presence | Months of sustained activity |
| Authoring | Merged pull requests |
| Reviewing | Technical reviews, including some that found a defect, regression, or missing test before merge |
| Triage | Issues triaged |
| Issues | Issues opened that someone else completed |
| Breadth | Areas of the codebase contributed to, or depth in one area where merge rights will be exercised |

Also weighed: helping other contributors; handling scope and risk well, for example splitting an oversized pull request or raising a design question before implementation.

### Maintainer

For a Maintainer, the bar is depth and judgement, not volume.

| Pillar | What is counted |
| --- | --- |
| Standing | Months held as a Committer on the project |
| Technical mastery | Merged changes to core or cross-cutting components, and the ability to explain the architecture of parts they did not write |
| Design leadership | Design proposals, architectural decisions, or substantial refactors adopted by the project |
| Reviewing | Final-stage reviews, including some that blocked or redirected a change |
| Stewardship | Project-health contributions, such as OpenSSF Scorecard or Best Practices Badge work, a security report, contributor documentation, or leading a community meeting |
| Mentorship | Contributors helped toward a role, by reviewing their work consistently or creating issues at the right level for them |

Also weighed: handling of public API evolution and breaking changes; diagnosing hard defects; regular community meeting participation; being the person other Committers route hard questions to.

## Setting thresholds

Each project sets a threshold for every row above and publishes them in its MAINTAINERS.md, using the [advancement template](../templates/maintainers-advancement.md).
The template carries example values to adjust, not defaults to inherit.
A completed table for a fictional mid-sized repository is shown in the [FAQ](./committer-and-maintainer-faq.md#what-does-a-published-threshold-table-look-like).
A project publishes its thresholds before nominating under this framework.
Until it does, the guidance in [Roles and Groups](./roles-and-groups.md) applies on its own.
A project that labels issue difficulty may add a difficulty floor to any row.

## Nominating

The nominating Committer or Maintainer fills the evidence section of the [vote PR template](../.github/PULL_REQUEST_TEMPLATE/vote_pr_template.md).
Evidence must include at least one analytics reference and a link for each item cited.

## Exceptional nominations

A project may need to add a Junior Committer, Committer, or Maintainer who does not meet its published thresholds.
Examples include a sole Maintainer stepping down, a security or release need, or a project being bootstrapped or transferred.
The procedure and the alternative evidence to weigh in these cases will be defined in a separate pull request.
Until then, such a nomination states in its pull request why the published thresholds do not apply, and the vote proceeds under [Roles and Groups](./roles-and-groups.md).
