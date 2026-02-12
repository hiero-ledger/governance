# Roles and Groups

This file contains an overview of our rules for roles and groups.

For project-based exceptions to any of these rules and how to request an exception, please refer to the following [Tracker](https://github.com/hiero-ledger/governance/blob/main/project-rules-exceptions.md)

## Definition of project roles

The Hiero project (and the LFDT) defines 4 different types of **roles**: **Contributors**, **Junior Committers**, **Committers**, and **Maintainers**.
Each person who contributes to Hiero must follow our [**Code of Conduct**](https://github.com/hiero-ledger/.github/blob/main/CODE_OF_CONDUCT.md).
Those roles are not assigned globally for the Hiero project but per **project**.
In most cases a project is a single GitHub repository, but it can also be a group of repositories that are related to each other.
A person can have multiple roles in multiple projects.

### Contributors

Any person who contributes to a project is a Contributor.
A contribution can be anything from opening an issue, to writing code, to writing documentation, etc.
We honor legitimate contributions to the project, and we want to make sure that all contributions are recognized.
A Contributor can be nominated by a Committer or a Maintainer to become a Junior Committers or Committers based on the project's needs and the quality of their contributions.
The following are some guidelines to help Contributors become active contributors to the project:

  - **Start Contributing**: Submit pull requests, report bugs, improve documentation, review code. Show consistency and quality in your contributions.
  - **Build Trust and Track Record**: Active committers will note your contributions, your general understanding of the project, and responsiveness.
  - **Get noticed**: Consistent and valuable contributions will demonstrate more project involvement and reliability.
  - **Review eligibility**: Quality contributions via Pull Request and a reasonable time contributing to the project (often 3-6 months) is the general acceptable baseline for eligibility. It is up to the project maintainers to determine the number of contributions required for promotion eligibility. This threshold may vary depending on factors such as the project's size and pace of development.

### Junior Committers

A Junior Committer is a community member who works on a regular basis on a project.
Since the Contributor role provides very limited rights on a project, the Junior Committer role bridges the gap between Contributors and Committers.
A Junior Committer is granted GitHub **Triage** rights on the repositories of the project, which allows them to:

- Assign themselves or others to issues
- Add and remove labels on issues
- Mark issues as duplicates
- Close and reopen issues

A Junior Committer will **not** have write access to the repository and their reviews will **not** count toward the required approvals on a pull request.
The Junior Committer role is designed to be **lightweight to obtain** and serves as a stepping stone toward becoming a Committer.
Junior Committers are encouraged to continue contributing and growing their involvement in the project with the goal of eventually being nominated as a Committer.

#### Adding a Junior Committer

A Contributor or Junior Committers can be nominated by any Committer or Maintainer of the project to become a Junior Committer:

- **Eligibility**: A Contributor who has shown regular activity on the project over a period of several weeks (e.g., opening issues, submitting pull requests, participating in discussions or reviews) can be nominated. Given the lightweight nature of this role, the barrier for approval should be kept low.
- **Nomination and voting**: The nomination follows the [Creating a PR](#creating-a-pr-to-add-or-remove-a-person-for-a-specific-role) and [Voting](#voting) processes described below.

#### Removing a Junior Committer

Project maintainers may remove a Junior Committer if:

- The Junior Committer breaks our Code of Conduct.
- The Junior Committer has shown no activity for 1 to 2 months. Maintainers are encouraged to remove inactive Junior Committers promptly to keep the group current and active.
- The Junior Committer is not responsive when contacted by the project maintainers.

The removal of Junior Committers must be decided by a project maintainer vote.
The voting must be held via a GitHub PR (by proposing a change to the `config.yaml` file).

### Committers

A Committer has specific rights for the project.
As an example, a Committer can assign people to issues, merge PRs, or create branches directly in a repository of the project.

#### Adding a Committer

Any Committer or Maintainer of the given project can nominate a Contributor to become a Committer based on the project's needs and following these steps:

- **Define your project's needs**: A repository should have a minimum of Committers to ensure a project's sustainability and resilience.
  The exact number should be determined by the project Maintainers based on the size and pace of the project's development, taking into account the overall activity level and ensuring a fair voting process.
- **Evaluate your project's performance**: Committers and Maintainers should monitor their project health and velocity and make decisions about whether the project needs more Committers.
- **Verify your project's needs**: Committers and Maintainers should define the number of good contributions that a Contributor must reach to consider a nomination.
  This is based on the size and complexity of the project in question.
- **Nomination and voting**: The nomination follows the [Creating a PR](#creating-a-pr-to-add-or-remove-a-person-for-a-specific-role) and [Voting](#voting) processes described below. The PR should describe the basis reached for nominating the Contributor.

As long as a Committer follows our Code of Conduct, makes reasonable contributions to the project, and is not violating any of our policies, they will keep their Committer role.

#### Removing a Committer

Project maintainers may remove a committer if:

- The Commiter breaks our Code of Conduct.
- Shown no activity for 6 months and does not respond when contacted by the project maintainers or LFDT staff.
- Keeps making bad decisions (their approvals and contributions are negatively affecting the project's performance).

Maintainers are responsible for removing inactive committers.
A committer is considered inactive if there has been no activity for six months and there has been no response when trying to contact them.
The removal of committers must be decided by a project maintainer vote. The voting must be held via a GitHub PR (by proposing a change to the `config.yaml` file).

### Maintainers

The Maintainers of the project are the people that are responsible for the project.
A Maintainer should drive the project's roadmap/vision and take care of topics like community meetings,
the general structure of the project (fits our best practices, is secure, ...), and so on.
In addition, the Maintainers should report project updates to the Hiero **Technical Steering Committee** (TSC).
Maintainers are responsible for keeping track of project Issues and Discussions and help pushing inactive conversations.
It is a responsibility of the maintainers to close Issues and Discussions that are considered outdated or stale to the current goals of the project.

#### Adding a Maintainer

A Committer of a project can be nominated to become a Maintainer:

- **Define your project's needs**: A repository should have 1 to 3 maintainers to ensure a project's sustainability and resilience. It is not necesarily a goal for the committer to become a maintainer unless the project's needs require it to have more maintainers.
- **Nomination and voting**: The nomination follows the [Creating a PR](#creating-a-pr-to-add-or-remove-a-person-for-a-specific-role) and [Voting](#voting) processes described below. The PR should describe the basis reached for nominating the Maintainer.

#### Removing a Maintainer

Project maintainers or the TSC may remove a maintainer who:

- Breaks Code of Conduct.
- Is inactive for 6 months and does not respond when contacted.
- Keeps making bad decisions (their contributions are negatively affecting the project's performance).

A maintainer is considered inactive if there has been no activity for six months and there has been no response when trying to contact them.
The removal of maintainers must be decided by a project maintainer vote. The voting must be held via a GitHub PR (by proposing a change to the `config.yaml` file).

### Creating a PR to add or remove a person for a specific role

When a person is nominated to become a Junior Committer, Committer, or Maintainer, a PR should be created against the [`config.yaml`](config.yaml) file.
The file is a configuration for https://clowarden.io that is used as tool to manage all Hiero repos.
The file contains all maintainer, committer, and junior committer groups and their members.
The file follows the defined syntax of clowarden that looks like this:

```yaml
teams:
  - name: PROJECT-maintainers
    maintainers:
      - user1
    members:
      - user2
      - user3
  - name: PROJECT-committers
    maintainers:
      - user1
    members:
      - user5
      - user6
  - name: PROJECT-junior-committers
    maintainers:
      - user1
    members:
      - user8
      - user9
```

As you can see there are three groups defined for a project: `PROJECT-maintainers`, `PROJECT-committers`, and `PROJECT-junior-committers`.
In each group there are two sections that can be a little misleading: `maintainers` and `members`.
The `maintainers` section defines **not the project maintainers**.
For clowarden the `maintainers` section is needed and must contain at least one person that is already a member of the hiero-ledger GitHub organization.
That is must to create a valid group.
It is best practice to have only one person in the `maintainers` section.
The `members` section contains all the members of the group.
When a person is nominated to become a Junior Committer, Committer, or Maintainer, the PR should add the person to the `members` section of the respective group.

#### Example: Adding a New Maintainer

To nominate `alice123` as a new maintainer for the PROJECT, update the `config.yaml` file by adding their GitHub username to the `members` section of the `PROJECT-maintainers` group:

    teams:
      - name: PROJECT-maintainers
        maintainers:
          - user1
        members:
          - user2
          - user3
          - alice123  # New maintainer being added
      - name: PROJECT-committers
        maintainers:
          - user1
        members:
          - user5
          - user6

#### Example: Adding a New Committer

To nominate `bob456` as a new committer for the PROJECT, update the `config.yaml` file by adding their GitHub username to the `members` section of the `PROJECT-committers` group:

    teams:
      - name: PROJECT-maintainers
        maintainers:
          - user1
        members:
          - user2
          - user3
      - name: PROJECT-committers
        maintainers:
          - user1
        members:
          - user5
          - user6
          - bob456  # New committer being added

#### Example: Adding a New Junior Committer

To nominate `carol789` as a new junior committer for the PROJECT, update the `config.yaml` file by adding their GitHub username to the `members` section of the `PROJECT-junior-committers` group:

    teams:
      - name: PROJECT-maintainers
        maintainers:
          - user1
        members:
          - user2
          - user3
      - name: PROJECT-committers
        maintainers:
          - user1
        members:
          - user5
          - user6
      - name: PROJECT-junior-committers
        maintainers:
          - user1
        members:
          - user8
          - user9
          - carol789  # New junior committer being added

### Voting

When it comes to electing and voting for new junior committers, committers, or maintainers, the project should consider the following:

For candidates seeking promotion to Junior Committers, Committers, or Maintainers:
- The candidate needs to show participation in the project by contributing with code, issues, discussions, reviews, etc.
- These contributions need to show proper understanding of the project and quality of the work.
- 3 to 6 months worth of contributions is considered a good minimum for candidates to be selected for a role promotion.
- A Committer or Maintainer will be considered inactive if they shown no activity for 6 months at least, in such case, they could be selected for removal.
- A Committer can maintain their project status independently from their employment.

For Maintainers and Committers voting on new candidates:
- When a candidate is selected for becoming a Junior Committer, Committer, or Maintainer, this proposal needs to be made via PR request against the config.yaml in the governance repo.
- An example of a promotion can be found in the following [PR](https://github.com/hiero-ledger/governance/pull/509).
-  We use the tool [GitVote](https://github.com/cncf/gitvote) for all async votings in Hiero. You can find information about the usage in our [guideline](../rules-and-guidelines/asynchronous-voting.md). We have ready-to-use profiles for all maintainer groups that can be found [in this config file](https://github.com/hiero-ledger/.github/blob/main/.gitvote.yml#L46). The vote starts by adding a comment to the PR. A concrete example for adding a new maintainer to the Rust SDK can be found [here](https://github.com/hiero-ledger/governance/pull/509#issuecomment-3824234728).
- The creator of the PR should notify all maintainers that a vote is now open.
- Maintainers that vote against the candidate's promotion should post a comment in the PR containing the reason.
- All Maintainers are required to participate in a nomination, but may effectively abstain from voting by only posting a comment in the PR.
- Maintainers are required to vote, if a maintainer does not participate in several consecutive votes they will be considered "inactive" which can be grounds for removal of maintainer status.
- A vote passes when more maintainers have voted in favor (+1 / thumbs up in GitVote) than against (-1 / thumbs down in GitVote). Maintainers who abstain or do not vote are not counted. For example, 2 votes in favor and 0 against with 10 abstentions is a passing vote. Once the vote has passed, the PR can be merged and the candidate will be officially part of their new team.
- A vote can be closed early when the outcome can no longer change based on the remaining votes. For example, if a majority of all maintainers have already voted in favor, the vote passes regardless of how the remaining maintainers vote. Conversely, if enough maintainers have voted against that it is impossible for the remaining votes to produce more +1 than -1, the vote fails early.
- If a PR remains inactive for 2 days, it is a responsibility of the PR owner to reach out to the reviewers via Discord, bring it up in Community calls or reach out for help in the [hiero-general Discord channel](https://discord.com/channels/905194001349627914/1289954446712770600).
- If a PR shows no activity for 2 weeks, it will be considered stale and it will be closed with no promotion.
- A Maintainer or Committer can nominate a candidate for removal from the teams if the candidate has not shown any activity for 6 months at least or is not responsive.
- A candidate can also be nominated for removal from the teams if they break code of conduct or has consistently made contributions that are affecting the team.
- The voting process for removing a candiate is the same as the process for promoting a candidate (via PR).

## Definition of groups

Since Hiero contains multiple projects, we define GitHub **groups** that are used to manage the access to the GitHub repositories.
The groups are defined in the `config.yaml` file and are used to manage the access to the GitHub repositories that belong to a project.
Contributors do not have any specific rights, and therefore we do not need to define any groups for them.
Junior Committers, Committers, and Maintainers are defined in groups that are used to manage the access to the GitHub repositories.
For each project we have defined a Junior Committers group, a Committers group, and a Maintainers group:

- **`PROJECT-maintainers`**: For each project we have a group that defines the Maintainers of that project.
- **`PROJECT-committers`**: For each project we have a group that defines the Committers of that project.
- **`PROJECT-junior-committers`**: For each project we have a group that defines the Junior Committers of that project.

There are global groups in the [`config.yaml`](https://github.com/hiero-ledger/governance/blob/main/config.yaml) file as well:

- **`hiero-automation`**: This group contains the CI/CD Automation service accounts for hiero-ledger projects.
- **`github-maintainers`**: This group contains those responsible for maintaining our GitHub environment and infrastructure (including GitHub Action runners, ...).
- **`tsc`**: This group contains all members of the technical steering committee (TSC) as defined [here](https://github.com/hiero-ledger/tsc).
- **`lf-staff`**: This group contains all Linux Foundation and LF Decentralized Trust members who require (mostly ADMIN) rights on the organization.
- **`security-maintainers`**: This group contains members of the security teams who are responsible for monitoring and maintaining security tooling and automated scanners within hiero-ledger projects.
- **`prod-security`**: This group contains members of the security teams who are responsible for reviewing code for security issues, threat modeling and reducing risk within hiero-ledger projects.
- **`sec-ops`**: This group contains members of the security teams who are responsible for responding to security incidents within hiero-ledger projects.

## Definitions of GitHub roles

For each project the following GitHub roles should be defined for the groups that work on the project.
The GitHub roles define the privileges afforded the groups on the GitHub repositories of the project.
All roles are based on the [GitHub role defintions](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).

- **`github-maintainers`**: `MAINTAIN`
- **`tsc`**: `MAINTAIN`
- **`PROJECT-maintainers`**: `MAINTAIN`
- **`PROJECT-committers`**: `WRITE`
- **`PROJECT-junior-committers`**: `TRIAGE`

The GitHub roles are assigned in the [`config.yaml`](https://github.com/hiero-ledger/governance/blob/main/config.yaml).

### Additional Roles for supporting onboarding, contribution and project management

Two additional roles can be defined per project next to committer and maintainer roles to support onboarding and contribution to the Hiero project:

- **`PROJECT-triage-contributor`**: grants triage access (e.g., ability to assign tickets) but not write access to project boards.
  This will allow to assign issues to contributors and help with the triage of issues without granting full write access to the project.
  We believe that this role is essential for onboarding new contributors that will work full time on the project.
  Next to that the role allows managers of companies that are members of the Hiero project to help with the triage of issues without granting full write access to the project.
- **`PROJECT-board-contributor`**: grants write access to project boards (e.g., changing board status and sprint planning).
  Companies that are members of the Hiero project might have project managers working on the project.
  This role allows them to update the project boards without granting full write access to the project.

These roles can be granted based on community sponsorship or through a maintainer vote, depending on the governance process adopted.
As defined today the roles can only be granted to people based on a sponsorship from a company that is a [member of the LF Decentralized Trust](https://www.lfdecentralizedtrust.org/members).
The TSC will review requests in the form of a PR against the https://github.com/hiero-ledger/governance repository for these roles and approve the PR based on the previous criteria.

## Usage of GitHub CODEOWNERS in combination with our roles, groups, and rights

A project can decide to use GitHub [`CODEOWNERS`](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
Using `CODEOWNERS` is a best practice.
Use of `CODEOWNERS` should be encouraged in all projects but is not required.
This helps maintainers ensure that the codebase is getting reviewed by the experts in specific areas of the code.
Combining the Contributors, Committers, and Maintainers roles with GitHub `CODEOWNERS` may require extra care and consideration.
The following definitions help to describe the current effects:

- The `CODEOWNERS` file defines some specific groups that are **codeowner** of particular files (or folders) of the repository.
- A PR that contains changes on those files needs to be approved by one of those codeowners.
- A `CODEOWNERS` file will not affect the definition of Contributors, Committers, and Maintainers.
- The minimum permission a **codeowner** must have is `write` on a given repository. As such a **codeowner** must be a Committer or Maintainer on the project.
    - See [**`PROJECT-maintainers`**](#rights) and [**`PROJECT-committers`**](#rights) or one of our specific groups (for example, [**`lf-staff`**](#rights)) for added detail.
