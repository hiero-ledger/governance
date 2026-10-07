# Committer and Maintainer FAQ

This document answers frequently asked questions from Hiero maintainers and committers.
The document is based on questions that have been asked in the community.

## How are the responsibilities of a project maintainer defined?

Maintainers have responsibilities that go beyond those of regular contributors or committers:

- Vote and act on governance decisions
  - Maintainers are trusted to cast informed votes on role assignments, project direction, and governance matters.
  - They should maintain deep technical expertise in relevant areas.
    In larger projects, expertise may be scoped to specific subsystems (e.g., consensus module, smart contracts).
- Keep the project organized and moving forward
  - This includes labeling and closing issues, resolving stale discussions, and encouraging active participation.
  - Maintainers should stay engaged in community discussions (e.g., on [Discord](https://discord.gg/pZ2GT6aq), Github discussions, or meetings).
- Monitor and track activity
    - Maintainers should track contributions and raise votes for role changes when warranted.
- Define and document exceptions
  - Exceptions to governance roles or processes must be documented transparently in the relevant repository.

## I'm working on Hiero as part of my daily job. What happens to my project roles if my employment status changes?

Committer and maintainer roles are community roles and are not tied to employment.
If someone leaves an employer, they keep their community roles.
Only access that was granted due to external sponsorship (e.g., **`PROJECT-board-contributor`** role) may be subject to review.

## How do I know when someone deserves to be promoted from the contributor to committer role?
    
Here are some general guidelines that should be considered when determining if someone should be promoted to the committer role:
    
- The candidate shows consistent participation in the project by contributing valuable code, issues, discussion, reviews, etc. for 3-6 months.
- The candidate has a solid understanding of the project including design, architecture, and roadmap.
- The candidate is trusted and reliable enough to be granted `write` permission to the project, including the ability to create branches, open PRs, merge PRs, and write tickets among others.
    
Details can also be found in this [doc](roles-and-groups.md).
The default thresholds for each role are set out in [Advancement Qualifications](advancement-qualifications.md).

## How do I know when someone deserves to be promoted from the committer group to the maintainer group?
    
Here are some general guidelines that should be considered when determining if someone should be promoted to the maintainer role:
    
- The candidate has been a committer for 3-6 months contributing highly valuable code, issues, discussion, reviews, etc.
- The candidate shows a superior level of understanding and knowledge of the project including design, architecture, and roadmap.
- The candidate shows interest in and cares about the management of the project.
- The candidate is highly trusted. Their opinion is taken seriously enough to warrant a vote in future decisions.

The default thresholds for each role are set out in [Advancement Qualifications](advancement-qualifications.md).

## Do I need a role before I can build a record toward one?

No.
Every counted activity is open to any developer, so nobody has to wait for approval to start.
Anyone can fork a repository, open an issue or a pull request, review the work of others and help on Discord.
Triage is the one category where the GitHub permission and the underlying skill differ.
A contributor can show triage judgement in a comment, and only applying a label or closing an issue needs the Triage role.
See [Advancement Qualifications](advancement-qualifications.md) for the categories that are counted.

## I cannot attend the community meetings. Does that count against me?

No.
Meetings are held at a fixed time that will not suit every timezone.
Attendance at any Hiero community call is good to have, but it is not required.
Community activity can also be shown by answering questions on Discord and in issue and pull request threads.
See [Advancement Qualifications](advancement-qualifications.md) for how community support is counted.

## I am new to programming. What reviews count?

Community members are asked to work within their circle of competence.
A beginner can give useful reviews, for example by pointing to the documentation on GPG key signing or by helping to debug why a workflow has failed.
They can also open issues about missing examples or unclear documentation.
More experienced developers may focus on the robustness of the code and raise deeper architectural issues.
The review thresholds are listed in [Advancement Qualifications](advancement-qualifications.md).

## How does a Committer's reviewing differ from a Junior Committer's?

The reviewing bar shifts in kind, not only in number.
A Junior Committer is asked for reviews that raise a finding or question, or that confirm the change matches its issue and its tests pass.
A Committer is expected to review the substance of a change, because they may be the one merging it.
Whether Committers are encouraged to use their merge rights, and the related branch protections, is declared project by project.
See [Advancement Qualifications](advancement-qualifications.md) for the thresholds at each level.

## What makes a Maintainer different from a very active Committer?

The bar for a Maintainer is depth and judgement, not volume.
A Maintainer sets technical direction and is the final authority on whether a change is correct, safe and consistent with where the project is going.
That authority rests on demonstrated mastery of the codebase, not on tenure or on the number of pull requests merged.
Triage and issue authorship are not restated for Maintainers, because they already met those bars as Committers.
Authoring and reviewing are restated, because what changes at this level is how deep and how consequential the work was.
See [Advancement Qualifications](advancement-qualifications.md) for the Maintainer thresholds.

## Can I be nominated on deep work in one subsystem?

Yes.
Depth in one area can substitute for breadth, where the role will be exercised in that area.
A Committer whose work concentrates in one subsystem, such as a conformance test suite, a protocol layer or release tooling, can be nominated on that basis, and is expected to use merge rights there.
A Maintainer nominee must still show an understanding of the project as a whole, because Maintainers decide on changes well outside whatever they build themselves.
See [Advancement Qualifications](advancement-qualifications.md) for the breadth and mastery rows.

## What does good nomination evidence look like?

Good evidence gives voters something to check: at least one analytics reference, and a link for each item cited.
It describes the pattern of activity over time, not only the total.
The example below is illustrative only, for a fictional nominee, and follows the vote pull request template.
See [Advancement Qualifications](advancement-qualifications.md) for what is counted.

```markdown
### Nomination: @example-dev for Committer on Example SDK

**Analytics:** https://hiero-hackers.github.io/analytics/ (contributor view for example-sdk, illustrative)

**Active since:** March 2026, steady weekly activity, with a quieter month in June

**Authoring:** https://github.com/hiero-ledger/example-sdk/pull/123, https://github.com/hiero-ledger/example-sdk/pull/131

**Reviewing:** https://github.com/hiero-ledger/example-sdk/pull/140#pullrequestreview-1001 (found a missing test for the retry path)

**Triage:** https://github.com/hiero-ledger/example-sdk/issues/98 (identified as a duplicate of #64)

**Issue authorship:** https://github.com/hiero-ledger/example-sdk/issues/102 (completed by another contributor)

**Community support:** https://github.com/hiero-ledger/example-sdk/discussions/77 (helped a newcomer set up signing)

**Judgement / stewardship:** https://github.com/hiero-ledger/example-sdk/pull/150 (split an oversized change before review)

**Why now:** The project needs more reviewers for the transaction module, and @example-dev has reviewed there consistently for six months.
```

## How do I know when someone deserves to be added to the `code-owner` group?
    
A person should be considered for the `code-owner` group if they are already a committer or a maintainer and they have the knowledge and experience in that area to provide deep and meaningful reviews.
Typically, people in the code-owner group should be a Subject Matter Expert (SME) in the owned files.
They should be trusted enough to be the sole reviewer of changes in the owned code before those changes are merged into `main`.
    
 A `code-owner` should be considered for removal from the `code-owner` role if one or more of the following items is true:

- The `code-owner` requests to be removed from the group.
- The `code-owner` is inactive for 6 months and does not respond when contacted (see [Hiero guidelines](roles-and-groups.md#maintainers)).
- The `code-owner` makes enough decisions which negatively affect the project's performance (see [Hiero guidelines](roles-and-groups.md#maintainers)).
- The `code-owner` breaks the [Code of Conduct](https://github.com/hiero-ledger/.github/blob/main/CODE_OF_CONDUCT.md).

## How do I know when someone should be moved from the maintainer group to the committer role?
    
As a general rule, a maintainer should be considered for removal from the maintainer role to the committer role if one or more of the following items is true:
    
- The maintainer requests to be removed from the group.
- The maintainer is inactive for 6 months and does not respond when contacted (see [Hiero guidelines](roles-and-groups.md#maintainers)).
- The maintainer makes enough decisions which negatively affect the project's performance (see [Hiero guidelines](roles-and-groups.md#maintainers)).
- The maintainer breaks the [Code of Conduct](https://github.com/hiero-ledger/.github/blob/main/CODE_OF_CONDUCT.md).
    
The project maintainers may also decide to propose removal from the maintainer role and not added to the committer role (i.e. reverted to the contributor role) depending on the severity of the situation.

## How do I know when someone should be removed from the committer group?
    
As a general rule, a committer should be considered for removal from the committer role to if one or more of the following items is true:
    
- The committer requests to be removed from the group.
- The committer is inactive for 6 months and does not respond when contacted (see [Hiero guidelines](roles-and-groups.md#maintainers)).
- The committer makes enough decisions which negatively affect the project's performance (see [Hiero guidelines](roles-and-groups.md#maintainers)).
- The committer breaks the [Code of Conduct](https://github.com/hiero-ledger/.github/blob/main/CODE_OF_CONDUCT.md).

## What is the escalation path when in doubt?
    
Options:
    
- Post your issue to the [hiero-general](https://discord.com/channels/905194001349627914/1289954446712770600) discord channel.
  This is the best first step of escalation.
- Put your issue on the community meeting agenda and attend the next [community meeting](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week&occurrence=1755788400).

## I have a question not answered in this FAQ. Where can I find the answer?
    
Post your question to the [hiero-general](https://discord.com/channels/905194001349627914/1289954446712770600) discord channels.
