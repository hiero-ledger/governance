# Roles and Groups

This file contains an overview of our rules for roles and groups

## Definition of general roles

The Hiero project (and the LFDT) defines 3 different types of **roles**: **Contributors**, **Committers**, and **Maintainers**.
Each person who contributes to Hiero must follow our [**Code of Conduct**](https://github.com/hiero-ledger/.github/blob/main/CODE_OF_CONDUCT.md).
Those roles are not assigned globally for the Hiero project but per **project**.
In most cases a project is a single GitHub repository, but it can also be a group of repositories that are related to each other.
A person can have multiple roles in multiple projects.

### Contributors

Any person that does any contribution to the project is a Contributor. A contribution can be anything from opening an issue, to writing code, to writing documentation, etc.

  - If a PR has gone 2 days without approvals or an Issue or Discussion has no activity for 2 days, the owner must reach our to our hiero-general Discord channel.
  - If a PR or discussion has gone stale for 2 weeks, the repo maintainers can close them due to inactivity.
We honor legitimate contributions to the project, and we want to make sure that all contributions are recognized.
A Contributor can be nominated by a Committer or a Maintainer to become a Committer:
  - **Start Contributing**: Submit pull requests, report bugs, improve docs, review code. Show consistency and quality in your contributions
  - **Build Trust and Tack Record**: Active committers will notice your contributions, your understanding and responsiveness.
  - **Get noticed**: Consistency and valuable contributions will create more project involvement and reliability.
  - **Review eligibility**: A minimum number of approved PRs and a reasonable time contributing to the project (3-6 months) is the general acceptable baseline for eligibility. 

### Committers

A Committer has specific rights for the project.

As an example a Committer can assign people to issues, merge PRs, or create branches directly in a repository of the project.
Any Committer or Maintainer of the given project should nominate a Contributor to become a Committer based on the project's needs and following these steps:

- **Define your project's needs**: A repository should have minimum 3 committers to ensure a project's sustainability and resilience. It will also allow for fairness in the votes. Project owners, can choose to have more committers depending on the size of their project.
- **Evaluate your project's performance**: Committers and Maintainers should monitor their project health and velocity and make decisions about whether the project needs more Committers.
- **Verify your project's needs**: Committers or Maintainers should define the number of good contributions that a Contributor must reach to consider a nomination. This is based on the size and complexity of the repo in question.
- **Nominate more resources**: To promote a contributor, a vote should be held in a GitHub PR (by doing a change to the config.yaml file) and by making mention of the basis reached for nominating the Contributor.
- **Approve the nomination**: All Maintainers should vote on that nomination and the vote passes when reaching majority of votes.
- **Make adjustments**: Maintainers should be responsible for removing inactive committers. A committer is considered inactive if there has been no activity for six months and there has been no response when trying to contact them.
As long as a Committer follows our Code of Conduct, makes reasonable contributions to the project,
and is not violating any of our policies, they will keep their Committer role.

A committer can lose the role if:

- Breaks code of conduct
- Shown no activity for 6 months and does not responds when reached
- Keeps making bad decisions (their approvals and contributions are actively affecting the project's performance).

The Maintainers of the project can decide to remove a Committer from the project based on those rules.
Like with the nomination of a Committer, the vote of the maintainers should be held in a GitHub PR (by doing a change to the `config.yaml` file).

### Maintainers

The Maintainers of the project are the people that are responsible for the project.

A Maintainer should drive the project's roadmap/vision and take care of topics like community meetings,
the general structure of the project (fits our best practices, is secure, ...), and so on.

In addition, the Maintainers should report project updates to the Hiero **Technical Steering Committee** (TSC).
A Committer of a project can be nominated to become a Maintainer:

- **Define your project's needs**: A repository should have 1 to 3 maintainers to ensure a project's sustainability and resilience. It is not necesarily a goal for the committer to become a mintainer unless the project's needs require it to have more maintainers.
- **Nominate a maintainer**: To promote a candidate, a vote should be held in a GitHub PR (by doing a change to the config.yaml file) and by making mention of the basis reached for nominating the Maintainer.
- **Approve the nomination**: All Maintainers should vote on that nomination and the vote passes when reaching majority of votes.
- **Make adjustments**: A maintainer is considered inactive if there has been no activity for six months and there has been no response when trying to contact them.

A maintainer can lose the role if:

- Breaks code of conduct
- Are inactive for 6 months and do not responds when reached
- Keeps making bad decisions (their contributions are actively affecting the project's performance).
More on maintainer guidelines, can be found in the [**LFDT site**](https://lf-decentralized-trust.github.io/governance/governing-documents/MAINTAINERS-file.html).

## Definition of groups

Since Hiero contains multiple projects, we need to define GitHub **groups** that are used to manage the access to the GitHub repositories.
The groups are defined in the `config.yaml` file and are used to manage the access to the GitHub repositories that belong to a project.
Contributors do not have any specific rights, and therefore we do not need to define any groups for them.
Committers and Maintainers are defined in groups that are used to manage the access to the GitHub repositories.
For each project we have defined a Committers group and a Maintainers group:

- **`PROJECT-maintainers`**: For each project we have a group that defines the Maintainers of that project.
- **`PROJECT-committers`**: For each project we have a group that defines the Committers of that project.

Next to that you can find some other general groups in the `config.yaml` file:

- **`hiero-automation`**: CI/CD Automation service account for hiero-ledger projects
- **`hiero-mirror-node-automation`**: CI/CD Automation serice account for hiero-ledger mirror node projects
- **`github-maintainers`**: The group is responsible for maintaining our GitHub environment and infrastructure (including GitHub Action runners, ...).
- **`tsc`**: The group that contains all members of the technical steering committee (TSC) as defined [here](https://github.com/hiero-ledger/tsc).
- **`lf-staff`**: The group contains all Linux Foundation and LF Decentralized Trust members that needs (mostly ADMIN) rights on the org.
- **`security-maintainers`**: This group contains members of the security teams who are responsible for monitoring and maintaining security within hiero-ledger projects
- **`prod-security`**: This group contains members of the security teams who are responsible for monitoring and maintaining security within hiero-ledger projects
- **`sec-ops`**: This group contains members of the security teams who are responsible for monitoring and maintaining security within hiero-ledger projects

## Definitions of rights

For each project the following GitHub roles should be defined for the groups that work on the project.
Those GitHub roles defines the rights of the groups on the GitHub repositories of the project.
All roles are based on the [GitHub role defintions](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).

- **`github-maintainers`**: `MAINTAIN`
- **`tsc`**: `MAINTAIN`
- **`PROJECT-maintainers`**: `MAINTAIN`
- **`PROJECT-committers`**: `WRITE`

The GitHub roles are assigned in the `config.yaml`.

## Usage of GitHub CODEOWNERS in combination with our roles, groups, and rights

A project can decide to use GitHub `CODEOWNERS` (see https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
Using `CODEOWNERS` is a best practice.
It should be encouraged in all projects but is not required.
This helps maintainers ensure that the codebase is getting reviewed by the experts on those areas of the code.
Combining the Contributors, Committers, and Maintainers roles with GitHub `CODEOWNERS` is a little bit tricky.
So far, the following definitions are valid:

- The `CODEOWNERS` file defines some specific groups that are **codeowner** of particular files (or folders) of the repository.
- A PR that contains changes on those files needs to be approved by one of those codeowners.
- A `CODEOWNERS` file will not affect the definition of Contributors, Committers, and Maintainers.
- The minimum permission a **codeowner** must have is `write` on a given repository. As such a **codeowner** must be a Committer or Maintainer on the project
  (see **`PROJECT-maintainers`** and **`PROJECT-committers`**) or one of our special groups like **`lf-staff`**.
