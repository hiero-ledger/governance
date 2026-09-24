# Advancement Qualifications

This document defines what a Contributor should demonstrate to be nominated as a Junior Committer, Committer, or Maintainer.

This document makes **dimensions** of eligibility explicit while leaving each project to calibrate on thresholds.

## Why this document exists

The responsibilities of Junior Committers, Committers and Maintainers [Roles and Groups](./roles-and-groups.md) have various pillars that extend beyond making pull requests, for example: triaging issues, reviewing pull requests, stewarding the project. 

The goal of this document is to increase transparency and provide a clearer, actionable path towards qualifying as a team member in repositories at Hiero Ledger.

## Contribution categories

Five categories are counted. Most are visible natively on GitHub in any repository, and all are available to perform by any developer in the community.

| Category | What counts | Permissions needed | Where it is visible |
| --- | --- | --- | --- |
| **Authoring** | Merged pull requests, weighted by the difficulty of the linked issue | None | PR list, filtered by author |
| **Reviewing** | Pull request reviews containing substantive findings, questions, or signing or workflow compliance | None | PR list, filtered by reviewer |
| **Issue authorship** | Well-formed bug reports, proposals, and follow-ups opened by the Contributor | None | Issue list, filtered by author |
| **Community support** | Answering questions and unblocking other contributors, in GitHub Discussions, issue threads, or community channels, and taking part in community meetings | None | Discussions and issue timelines; community meeting minutes |
| **Triage** | Reproducing reported issues, identifying duplicates, routing an issue to the right project, and judging whether an issue is still relevant | None to do it in a comment; **Triage** role to apply the label, close, assign, or mark a duplicate | Issue timeline and LFDT discord |

**All are activities open to every developer. At Hiero Ledger we do not consider developers need to wait for approval to be able to perform these duties**

Anyone can fork a repository, create an issue, open a pull request and review other issues and pull requests and share on discord.

Triage is the one category where the GitHub permission and the underlying skill differ.
The judgement that triage consists of is open to anyone, and a Contributor demonstrates it by writing it in a comment. Only applying that label or closing the issue requires Triage permissions. No category therefore requires a role in order to build a record in it.

Community meetings are held at a fixed time that will not suit every timezone.
Attendance strengthens a nomination, but community activity can also be supported by being an active member on discord and responding to questions inside issue and pull requests.

Community members will have different level of skills and experience. At Hiero Ledger we request community members to operate within their circle of competence. For instance, a beginner programmer can provide fruitful reviews such as: pointing to the correct documents to achieve GPG key signing or helping to debug why a workflow has failed. They may open up issues around missing examples or unclear documentation. More advanced developers may concentrate on verifying the robustness of the code and create deeper architectural issues.

Similarly, this document recognises that community members have different levels of availability, thus emphasises sustained contributions and the skills demonstrated over longer periods of time.


## Baseline qualifications by role

Each table states the baseline that applies across the organisation.
`[project-defined]` marks a threshold each project sets for itself.

### Junior Committer

The Junior Committer role is intended to be lightweight to obtain and is the first stepping stone to qualify to become a committer.

| Category | Baseline |
| --- | --- |
| Presence | Active in most weeks across a period of at least **[project-defined, suggested: 6-10 weeks]** |
| Authoring | At least **[project-defined, suggested: 5]** merged pull requests reaching at least **[project-defined, suggested: beginner]** difficulty level |
| Reviewing | At least **[project-defined, suggested: 6]** compliance reviews checking: the change does what its linked issue describes, tests are present, examples run, commits are signed and at least **[project-defined, suggested: 3]** technical reviews at the **[project-defined, suggested: beginner]** difficulty level |
| Triage | Has triaged **[project-defined, suggested: 6]** issues informally, for example by identifying duplicates, asking for reproduction steps, or proposing a difficulty label in a comment |
| Issue authorship | At least **[project-defined, suggested: 2]** issues opened that were accepted as valid |
| Community support | Has helped at least **[project-defined, suggested: 3]** other contributors, for example by answering a question in a Discussion or attending a community call |
| Responsiveness | Follows contribution guidelines and code of conduct, responds to review feedback on their own pull requests within a reasonable period and does not routinely abandon work in progress |

Because Contributors do not yet hold Triage rights, triage evidence at this stage will usually take the form of comments rather than label or issue status changes.
Projects should treat a well-argued comment identifying a duplicate as equivalent.

### Committer

A Committer merges the work of others.
Eligibility should concentrate on the technical competence of their reviews.

| Category | Baseline |
| --- | --- |
| Standing | Is an existing Junior Committer on the project, holding Triage rights |
| Presence | Sustained activity over **[project-defined, suggested: 3-9 months]**, consistent with the existing guidance in [Roles and Groups](./roles-and-groups.md#adding-a-committer) |
| Authoring | At least **[project-defined, suggested: 20]** merged pull requests reaching at least **[project-defined, suggested: intermediate]** difficulty level across general issues, or **[project-defined, suggested: advanced]** difficulty level within a niche |
| Reviewing | At least **[project-defined, suggested: 20]** insightful technical reviews at the **[project-defined, suggested: intermediate]** difficulty level, of which at least **[project-defined, suggested: 5]** identified a defect, a regression, or a missing test before merge |
| Triage | At least **[project-defined, suggested: 20]** issues triaged, applying labels and opening or closing issues directly under the Triage rights held as a Junior Committer |
| Issue authorship | At least **[project-defined, suggested: 10]** well-documented issues opened at varying difficulty levels that were picked up and completed by someone else |
| Breadth | Contributions across at least **[project-defined, suggested: 3]** areas of the codebase, so that merge rights are not granted over code the Committer has never worked in. A Contributor nominated on the niche route above is assessed on depth within that niche instead, and their merge rights are expected to be exercised there |
| Community support | Has helped at least **[project-defined, suggested: 10]** other contributors, and is a person newer contributors are already comfortable directing a question to |
| Judgement | At least **[project-defined, suggested: 2]** occasions of handling scope and risk appropriately, for example by splitting an oversized pull request, declining an out-of-scope change, or raising a design question before implementation |

The reviewing bar shifts in kind, not only in number.

A Junior Committer is asked for compliance reviews and beginner technical reviews; a Committer is expected to review the substance of a change, since they may be the one merging it.

Whether Committers are encouraged to exercise their merge rights, and related branch protections, is to be declared project-by-project.

### Maintainer

A Maintainer is responsible for a project's direction, health, and reporting.

This is by design the hardest role to obtain, and the longest to reach.
A Maintainer sets technical direction and is the final authority on whether a change is correct, safe, and consistent with where the project is going.
That authority rests on demonstrated technical mastery of the codebase, not on tenure or on volume of contribution.

The bar is high in **depth**, not in throughput.
A Maintainer is not a Committer who has merged more pull requests.
They are a Committer who has shown they can be trusted to decide what the project should become, and to catch what every earlier stage of review missed.

| Category | Baseline |
| --- | --- |
| Standing | Is an existing Committer on the project, and has held that role for at least **[project-defined, suggested: 6-12 months]** |
| Presence | Sustained activity over **[project-defined, suggested: 12-18 months]** in total |
| Technical mastery | Can reasonably explain and defend the architecture of the project as a whole, including the parts they did not write. Has authored at least **[project-defined, suggested: 10]** changes at the **[project-defined, suggested: advanced]** difficulty level that touched core or cross-cutting components, not only self-contained features |
| Design leadership | Has authored or driven at least **[project-defined, suggested: 1]** design proposal, architectural decision, or substantial refactor that the project adopted |
| Reviewing | Has performed **[project-defined, suggested: 40]** final-stage reviews at the **[project-defined, suggested: advanced]** difficulty level, including at least **[project-defined, suggested: 10]** occasions of blocking or redirecting a change on judgement, and has caught at least **[project-defined, suggested: 3]** defects of correctness, security, or compatibility that earlier review stages missed |
| API and compatibility judgement | Has demonstrated sound handling of public API evolution, for example deprecation, versioning, backward compatibility, or the communication of a breaking change |
| Debugging depth | Has diagnosed and resolved at least **[project-defined, suggested: 2]** hard defects, for example a race condition, a serialisation or protocol mismatch, or an incompatibility with another implementation |
| Stewardship | Has made at least **[project-defined, suggested: 5]** broader project health contributions such as regarding: open SSF score, Best Practices Badge, a security report, contributor-facing documentation, and helping to lead its community meeting, integrating with other LFDT projects |
| Mentorship | Has helped at least **[project-defined, suggested: 2]** Contributors meet the minimum qualifications toward a role, for example by reviewing their work consistently and creating issues at the right difficulty for them |
| Community leadership | Takes part in relevant project's community meeting(s) on a regular enough basis, and is willing to represent the project to its users and to the TSC. This is a duty of the role rather than an optional strength |
| Escalation | Is already, in practice, a person other Committers route difficult technical questions to |

Triage and issue authorship are not restated here, because a Maintainer already met those bars as a Committer and repeating them would only measure throughput again.

Authoring and reviewing **are** restated, because what changes at this level is not how much a candidate has done but how deep and how consequential it was.

Depth may substitute for breadth of authorship, as at the Committer level.
A Committer whose own work concentrates in one subsystem, such as a conformance test suite, a protocol layer, or release tooling, may be nominated on that basis.
They must nonetheless satisfy the technical and stewardship mastery row for the project as a whole, since a Maintainer reviews and decides on changes well outside whatever they personally build.

Which specific duties a project expects of its Maintainers, for example release ownership or reporting to the TSC, is to be declared project-by-project thus the required qualifications may be higher than this document describes.

## Nomination evidence

The nominating Committer or Maintainer includes the following in the nomination pull request, alongside the `config.yaml` change described in [Creating a PR](./roles-and-groups.md#creating-a-pr-to-add-or-remove-a-person-for-a-specific-role).

Citing links rather than impressions gives voters something to check, and shows every Contributor reading the pull request what the organisation actually counts.
The same section is built into the repository's [vote pull request template](../.github/PULL_REQUEST_TEMPLATE/vote_pr_template.md), which is where it is filled in.

```markdown
### Nomination: @username for [role] on [project]

**Active since:** [date] — [describe the pattern of activity, not only the total]

**Authoring:** [links to merged PRs]

**Reviewing:** [links to reviews, noting what each one found]

**Triage:** [links to issues triaged]

**Community support:** [links to Discussions or issue threads where they helped someone; meeting minutes]

**Issue authorship:** [links to issues opened]

**Judgement / stewardship:** [links or a short description]

**Why now:** [what the project needs and why this person meets it]
```

## Project calibration

Each project publishes its own thresholds for every `[project-defined]` value in its `MAINTAINERS.md` or `TEAM.md`, and links to that section from its README.
A template for this is available at [templates/team.md](../templates/team.md), which also asks the project to define what its difficulty levels mean.

Projects should set thresholds proportionate to their own volume and level of project difficulty.
A repository receiving several pull requests a week and one receiving several a month cannot share the same numbers, and a smaller project that adopts numbers set for a larger one will find itself unable to grow Committers at all.

The intent is that the framework never becomes the reason a small project or projects that are working on exceptional difficulty of issues cannot develop new Maintainers.

## Safeguards

- **Quality over quantity.** Thresholds are a floor for consideration and should be set appropriately by project maintainers, not an entitlement. A nominator or voter may reasonably argue that a set of contributions does not represent the depth the count implies, and a Contributor who clears every number is not thereby owed the role.
- **Merged, not opened.** Unless a project states otherwise, authoring counts merged pull requests.
- **Roles are held, not banked.** Continued eligibility follows the inactivity and removal criteria already defined for each role in [Roles and Groups](./roles-and-groups.md).
