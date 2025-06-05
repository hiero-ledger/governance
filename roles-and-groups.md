# Roles and Groups

This file contains an overview of our rules for roles and groups.

For project-based exceptions to any of these rules and how to request an exception, please refer to the following [Tracker](https://github.com/hiero-ledger/governance/blob/main/project-rules-exceptions.md)

## Definition of general roles

The Hiero project (and the LFDT) defines 3 different types of **roles**: **Contributors**, **Committers**, and **Maintainers**.
Each person who contributes to Hiero must follow our [**Code of Conduct**](https://github.com/hiero-ledger/.github/blob/main/CODE_OF_CONDUCT.md).
Those roles are not assigned globally for the Hiero project but per **project**.
In most cases a project is a single GitHub repository, but it can also be a group of repositories that are related to each other.
A person can have multiple roles in multiple projects.

### Contributors

Any person who contributes to a project is a Contributor. A contribution can be anything from opening an issue, to writing code, to writing documentation, etc.

  - If a pull request has not received an approval within 2 business days or a discussion has no activity for more than 2 business days, we suggest to reach out to the Maintainers via our [hiero-general Discord channel](https://discord.lfdecentralizedtrust.org/).
  - If a pull request or discussion has gone stale for more than 2 weeks, the repo maintainers may close them due to inactivity.

We honor legitimate contributions to the project, and we want to make sure that all contributions are recognized.

A Contributor can be nominated by a Committer or a Maintainer to become a Committer:

  - **Start Contributing**: Submit pull requests, report bugs, improve documentation, review code. Show consistency and quality in your contributions.
  - **Build Trust and Track Record**: Active committers will note your contributions, your general understanding of the project, and responsiveness.
  - **Get noticed**: Consistent and valuable contributions will demonstrate more project involvement and reliability.
  - **Review eligibility**: Quality contributions via Pull Request and a reasonable time contributing to the project (often 3-6 months) is the general acceptable baseline for eligibility. It is up to the project maintainers to determine the number of contributions required for promotion eligibility. This threshold may vary depending on factors such as the project's size and pace of development.

### Committers

A Committer has specific rights for the project.

As an example, a Committer can assign people to issues, merge PRs, or create branches directly in a repository of the project.
Any Committer or Maintainer of the given project can nominate a Contributor to become a Committer based on the project's needs and following these steps:

- **Define your project's needs**: A repository should have a minimum of Committers to ensure a project's sustainability and resilience. The exact number should be determined by the project Maintainers based on the size and pace of the project's development, taking into account the overall activity level and ensuring a fair voting process.
- **Evaluate your project's performance**: Committers and Maintainers should monitor their project health and velocity and make decisions about whether the project needs more Committers.
- **Verify your project's needs**: Committers and Maintainers should define the number of good contributions that a Contributor must reach to consider a nomination. This is based on the size and complexity of the project in question.
- **Nominate new committers**: To promote a contributor, a vote should be held in a GitHub PR (by proposing a change to the config.yaml file) and by describing the basis reached for nominating the Contributor. The template [vote_pr_template.md](https://github.com/hiero-ledger/governance/blob/main/.github/PULL_REQUEST_TEMPLATE/vote_pr_template.md) should be used to creating a nomination.
- **Approve the nomination**: All Maintainers should vote on that nomination and the vote passes when a majority of maintainers vote to proceed. The voting procedure is explained in the same template [vote_pr_template.md](https://github.com/hiero-ledger/governance/blob/main/.github/PULL_REQUEST_TEMPLATE/vote_pr_template.md).
- **Make adjustments**: Maintainers are responsible for removing inactive committers. A committer is considered inactive if there has been no activity for six months and there has been no response when trying to contact them.
As long as a Committer follows our Code of Conduct, makes reasonable contributions to the project,
and is not violating any of our policies, they will keep their Committer role.

Project maintainers may remove a committer if:

- The Commiter breaks our Code of Conduct.
- Shown no activity for 6 months and does not respond when contacted by the project maintainers or LFDT staff.
- Keeps making bad decisions (their approvals and contributions are negatively affecting the project's performance).

The addition or removal of committers must be decided by a project maintainer vote. The voting must be held via a GitHub PR (by proposing a change to the `config.yaml` file).

### Maintainers

The Maintainers of the project are the people that are responsible for the project.

A Maintainer should drive the project's roadmap/vision and take care of topics like community meetings,
the general structure of the project (fits our best practices, is secure, ...), and so on.

In addition, the Maintainers should report project updates to the Hiero **Technical Steering Committee** (TSC).
A Committer of a project can be nominated to become a Maintainer:

- **Define your project's needs**: A repository should have 1 to 3 maintainers to ensure a project's sustainability and resilience. It is not necesarily a goal for the committer to become a maintainer unless the project's needs require it to have more maintainers.
- **Nominate a maintainer**: To promote a candidate, a vote should be held in a GitHub PR (by proposing a change to the config.yaml file) and by making mention of the basis reached for nominating the Maintainer. The template [vote_pr_template.md](https://github.com/hiero-ledger/governance/blob/main/.github/PULL_REQUEST_TEMPLATE/vote_pr_template.md) should be used to creating a nomination.
- **Approve the nomination**: All maintainers should vote on that nomination and the vote passes when a majority of maintainers vote to proceed. The voting procedure is explained in the same template [vote_pr_template.md](https://github.com/hiero-ledger/governance/blob/main/.github/PULL_REQUEST_TEMPLATE/vote_pr_template.md).
- **Make adjustments**: A maintainer is considered inactive if there has been no activity for six months and there has been no response when trying to contact them.

Maintainers are responsible for keeping track of project Issues and Discussions and help pushing inactive conversations. It is a responsibility of the maintainers to close Issues and Discussions that are considered outdated or stale to the current goals of the project.

Project maintainers or the TSC may remove a maintainer who:

- Breaks Code of Conduct.
- Is inactive for 6 months and does not respond when contacted.
- Keeps making bad decisions (their contributions are negatively affecting the project's performance).

More on maintainer guidelines can be found on the [**LFDT TAC site**](https://lf-decentralized-trust.github.io/governance/governing-documents/MAINTAINERS-file.html).

### Role Changes

Changes in role require a maintainer vote. Voting procedures can be found [here](https://github.com/hiero-ledger/governance/blob/main/voting-procedures.md). When it comes to electing and voting for new committers or new maintainers, the project should consider the following:

For candidates seeking promotion to Committers or Maintainers:
- The candidate needs to show participation in the project by contributing with code, issues, discussions, reviews, etc.
- These contributions need to show proper understanding of the project and quality of the work.
- 3 to 6 months worth of contributions is considered a good minimum for candidates to be selected for a role promotion.
- A Committer or Maintainer will be considered inactive if they shown no activity for 6 months at least, in such case, they could be selected for removal.
- A Committer can maintain their project status independently from their employment.

For Maintainers and Committers voting on new candidates:
- When a candidate is selected for becoming a Committer or a Maintainer, this proposal needs to be made via PR request against the config.yaml in the governance repo in accordance with the [voting procedures](https://github.com/hiero-ledger/governance/blob/main/voting-procedures.md).
- An example of a promotion can be found in the following [PR](https://github.com/hiero-ledger/governance/pull/176).
- If a PR remains inactive for 2 days, it is a responsibility of the PR owner to reach out to the reviewers via Discord, bring it up in Community calls or reach out for help in the [hiero-general Discord channel](https://discord.com/channels/905194001349627914/1289954446712770600).
- A Maintainer or Committer can nominate a candidate for removal from the teams if the candidate has not shown any activity for 6 months at least or is not responsive.
- A candidate can also be nominated for removal from the teams if they break code of conduct or has consistently made contributions that are affecting the team.
- The voting process for removing a candiate is the same as the process for promoting a candidate (via PR).

## Definition of groups

Since Hiero contains multiple projects, we define GitHub **groups** that are used to manage the access to the GitHub repositories.
The groups are defined in the `config.yaml` file and are used to manage the access to the GitHub repositories that belong to a project.
Contributors do not have any specific rights, and therefore we do not need to define any groups for them.
Committers and Maintainers are defined in groups that are used to manage the access to the GitHub repositories.
For each project we have defined a Committers group and a Maintainers group:

- **`PROJECT-maintainers`**: For each project we have a group that defines the Maintainers of that project.
- **`PROJECT-committers`**: For each project we have a group that defines the Committers of that project.

There are global groups in the [`config.yaml`](https://github.com/hiero-ledger/governance/blob/main/config.yaml) file as well:

- **`hiero-automation`**: This group contains the CI/CD Automation service accounts for hiero-ledger projects.
- **`github-maintainers`**: This group contains those responsible for maintaining our GitHub environment and infrastructure (including GitHub Action runners, ...).
- **`tsc`**: This group contains all members of the technical steering committee (TSC) as defined [here](https://github.com/hiero-ledger/tsc).
- **`lf-staff`**: This group contains all Linux Foundation and LF Decentralized Trust members who require (mostly ADMIN) rights on the organization.
- **`security-maintainers`**: This group contains members of the security teams who are responsible for monitoring and maintaining security tooling and automated scanners within hiero-ledger projects.
- **`prod-security`**: This group contains members of the security teams who are responsible for reviewing code for security issues, threat modeling and reducing risk within hiero-ledger projects.
- **`sec-ops`**: This group contains members of the security teams who are responsible for responding to security incidents within hiero-ledger projects.

## Definitions of roles

For each project the following GitHub roles should be defined for the groups that work on the project.
The GitHub roles define the privileges afforded the groups on the GitHub repositories of the project.
All roles are based on the [GitHub role defintions](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).

- **`github-maintainers`**: `MAINTAIN`
- **`tsc`**: `MAINTAIN`
- **`PROJECT-maintainers`**: `MAINTAIN`
- **`PROJECT-committers`**: `WRITE`

The GitHub roles are assigned in the [`config.yaml`](https://github.com/hiero-ledger/governance/blob/main/config.yaml).

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
