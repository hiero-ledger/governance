# Advancement Qualifications

This document sets out what a Contributor should demonstrate to be nominated as a Junior Committer, Committer, or Maintainer.
Projects inherit these defaults unless their MAINTAINERS.md overrides a row.

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

## Default thresholds

### Junior Committer

The role is lightweight by design, and the barrier is kept low.

| Category | Default |
| --- | --- |
| Presence | Active in most weeks over the last 8 weeks |
| Authoring | 5 merged pull requests |
| Reviewing | 6 reviews that each raised a finding or question, or confirmed the change matches its issue and its tests pass |
| Triage and issues | 8 issues, in any mix, either triaged in a comment or opened and accepted as valid |

Also weighed: helping other contributors; responding to review on their own pull requests; following the contribution guidelines and code of conduct.

### Committer

A Committer merges the work of others, so reviewing carries the most weight.

| Category | Default |
| --- | --- |
| Standing | Junior Committer on the project. Exceptions will be defined separately |
| Presence | Sustained activity over the last 6 months |
| Authoring | 20 merged pull requests |
| Reviewing | 20 technical reviews, at least 5 of which found a defect, regression, or missing test before merge |
| Triage | 20 issues triaged |
| Issues | 10 issues opened that someone else completed |
| Breadth | Contributions in at least 3 areas of the codebase, or depth in one area where merge rights will be exercised |

Also weighed: helping other contributors; handling scope and risk well, for example splitting an oversized pull request or raising a design question before implementation.

### Maintainer

For a Maintainer, the bar is depth and judgement, not volume.

| Category | Default |
| --- | --- |
| Standing | Committer on the project for at least 6 months |
| Technical mastery | 10 merged changes to core or cross-cutting components, and able to explain the architecture of parts they did not write |
| Design leadership | 1 design proposal, architectural decision, or substantial refactor adopted by the project |
| Reviewing | 40 final-stage reviews, at least 10 of which blocked or redirected a change |
| Stewardship | 5 project-health contributions, such as OpenSSF Scorecard or Best Practices Badge work, a security report, contributor documentation, or leading a community meeting |
| Mentorship | 2 Contributors helped toward a role, by reviewing their work consistently or creating issues at the right level for them |

Also weighed: handling of public API evolution and breaking changes; diagnosing hard defects; regular community meeting participation; being the person other Committers route hard questions to.

## Project overrides

A project may raise, lower, or add rows in its MAINTAINERS.md using the [advancement template](../templates/maintainers-advancement.md).
Rows not listed use the default.
A project that labels issue difficulty may add a difficulty floor.

## Nominating

The nominating Committer or Maintainer fills the evidence section of the [vote PR template](../.github/PULL_REQUEST_TEMPLATE/vote_pr_template.md).
Evidence must include at least one analytics reference and a link for each item cited.
