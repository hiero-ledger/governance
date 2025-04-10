# Hiero technical governance

This repository contains the `config.yaml` file that is used to configure all GitHub repositories of the organisation.
https://clowarden.io is used as tool to manage the GitHub ressources and the changelist for all Hiero repos can be found [here](https://clowarden.io/audit/?organization=LFDT-Hiero).

## Definition of general roles

In general the Hiero project (and the LFDT) defines 3 different types of roles: **Contributors**, **Committers**, and **Maintainers**.

Independent of the role each person contributes to Hiero must follow our Code of Conduct (https://github.com/hiero-ledger/.github/blob/main/CODE_OF_CONDUCT.md).

Those roles are not assigned globally for the Hiero project but per **Project**.
In most cases a **Project** is a single GitHub repository, but it can also be a group of repositories that are related to each other.
A person can have multiple roles in multiple projects.

In general any person that does any contribution to the project is a **Contributor**.
A contribution can be anything from opening an issue, to writing code, to reviewing code, to writing documentation, etc.
We honor all contributions to the project, and we want to make sure that all contributions are recognized.

If a person is a **Contributor** and has made significant contributions to the project, they can be invited to become a **Committer**.
Any **Committer** or **Maintainer** of the given project can nominate a person to become a **Committer**.
All **Maintainers** should vote on that nomination.
The vote should be held in a GitHub PR (by doing a change to the `config.yaml` file).

A **Committer** has specific rights for the **Project**.
As an example a **Committer** can assign people to issues, merge PRs, or create branches directly in a repository of the **Project**.
A detailed overview of all rights will be given below.

As long as a **Committer** follows our Code of Conduct, makes reasonable contributions to the **Project**,
and is not violating any of our policies, they will keep their **Committer** rights.
If a **Committer** is not making any contributions to the **Project** anymore for a longer periode of time they will lose their **Committer** state.
We need to define a reasonable timeframe for that.
The **Maintainers** of the **Project** can decide to remove a **Committer** from the **Project** based on those rules.
Like with the nomination of a **Committer**, the vote should be held in a GitHub PR (by doing a change to the `config.yaml` file). 

The **Maintainers** of the **Project** are the people that are responsible for the project.
Each **Project** should have 1-3 **Maintainers**.
A **Maintainer** should drive the **Project**'s roadmap/vision and take care of topics like community meetings,
the general structure of the **Project** (fits our best practices, is secure, ...), and so on.
In addition, the **Maintainers** should report **Project** updates to the Hiero **Technical Steering Committee** (TSC).

A **Committer** of a **Project** can be nominated to become a **Maintainer** of that **Project**, and all **Maintainers** should vote on that.
The vote should be held in a GitHub PR (by doing a change to the `config.yaml` file).
It is not the goal that every **Committer** of a **Project** becomes a **Maintainer**.
Having hundreds of **Maintainer** for a single project does not make sense.
As already defined for the **Committer** role, a **Maintainer** can lose the **Maintainer** role if they harm the **Project** in any way.
For a **Maintainer** the contribution to the **Project** should be on a really high level.
Therefore, it is a valid decision to remove a **Maintainer** from the **Project** and give that person the **Committer** role.
Remove a **Maintainer** from the **Project** and give that person the **Contributors** role should only happen in
really extreme cases where the **Maintainer** is harming the **Project** or ignoring the Code of Conduct.

## Definition of groups

Since Hiero contains multiple **Projects**, we need to define GitHub **Groups** that are used to manage the access to the GitHub repositories.
The groups are defined in the `config.yaml` file and are used to manage the access to the GitHub repositories.

**Contributors** do not have any specific rights, and therefore we do not need to define any groups for them.
**Committers** and **Maintainers** are defined in groups that are used to manage the access to the GitHub repositories.
For each project we have defined a **Committers** group and a **Maintainers** group: 

- **`PROJECT-maintainers`**: For each **Project** we have a **Group** that defines the **Maintainers** of that **Project**.
- **`PROJECT-committers`**: For each **Project** we have a **Group** that defines the **Committers** of that **Project**.

Next to that you can find some other general groups in the `config.yaml` file:

- **`hiero-automation`**: TODO
- **`hiero-mirror-node-automation`**: TODO
- **`github-maintainers`**: The group is responsible for maintaining our GitHub environment and infrastructure (including GitHub Action runners, ...).
- **`community`**: A group that contains all people that are currently not part of any other (non-temporary) group.
  We use this temporarly to invite people to the Hiero org.
- **`tsc`**: The group that contains all members of the technical steering committee (TSC) as defined [here](https://github.com/hiero-ledger/tsc).
- **`lf-staff`**: The group contains all Linux Foundation and LF Decentralized Trust members that needs (mostly ADMIN) rights on the org.
- **`security-maintainers`**: TODO
- **`prod-security`**: TODO
- **`sec-ops`**: TODO

## Definitions of GitHub roles

For each **Project** the following GitHub roles should be defined for the **Groups** that work on the **Project**.
All roles are based on the [GitHub role defintions](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).

- **`github-maintainers`**: `MAINTAIN`
- **`tsc`**: `ADMIN`
- **`PROJECT-maintainers`**: `MAINTAIN`
- **`PROJECT-committers`**: `WRITE`

The GitHub roles are assigned in the `config.yaml`.

## Usage of GitHub CODEOWNERS in combination with our roles and groups

A project can decide to use GitHub CODEOWNERS (see https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners).
Using CODEOWNERS is a best practice.
It should be encouraged in all projects (certainly not required).
This helps maintainers ensure that the codebase is getting reviewed by the experts on those areas of the code.

Combining the **Contributors**, **Committers**, and **Maintainers** roles with GitHub CODEOWNERS is a little bit tricky:

- The CODEOWNERS file defines some specific **Groups** that are **Codeowner** of particular files (or folders) of the repository.
- A PR that contains changes on those files needs to be approved by one of those **Codeowners**.
- A CODEOWNERS file will not affect the definition of **Contributors**, **Committers**, and **Maintainers**.
- With that in mind, it makes zero sense that a **Group** in the CODEOWNERS file is not a **Committer**, and **Maintainer** **Group** (see **`PROJECT-maintainers`** and **`PROJECT-committers`**) or one of our special groups like **`lf-staff`**.