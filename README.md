# Hiero technical governance

This repository contains the `config.yaml` file that is used to configure all GitHub repositories of the organisation. https://clowarden.io is used as tool to manage the GitHub ressources and the changelist for all Hiero repos can be found [here](https://clowarden.io/audit/?organization=LFDT-Hiero).

## Definition of groups

The `config.yaml` file defines several groups that all have different usecases:

- **`github-maintainers`**: The group is responsible for maintaining our GitHub environment and infrastructure (including GitHub Action runners, ...).
- **`github-committers`**:
- **`community`**: A group that contains all people that are currently not part of any other (non-temporary) group.
  We use this temporarly to invite people to the Hiero org.
- **`tsc`**: The group that contains all members of the technical steering committee (TSC) as defined [here](https://github.com/hiero-ledger/tsc).
- **`lf-staff`**: The group contains all Linux Foundation and LF Decentralized Trust members that needs (mostly ADMIN) rights on the org.
- **`REPO-maintainers`**: For each repository/project we have a group that defines the maintainers of that repository/project.
- **`REPO-committers`**: For each repository/project we have a group that defines the committers of that repository/project.
- **`voting-candidates`**: A temporary group that contains all people that did contributions to [Hashgraph repositories](https://github.com/hashgraph) in the past and
  therefore are allowed to vote on [TAC votings](https://lf-decentralized-trust.github.io/governance/member-info/).

## Definitions of roles

For each project the following roles should be defined for the groups that work on the repository. All roles are based on the [GitHub role defintions](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization).

- **`github-maintainers`**: `MAINTAIN`
- **`tsc`**: `ADMIN`
- **`REPO-maintainers`**: `MAINTAIN`
- **`REPO-committers`**: `WRITE`

### Difference between committers and maintainers

As said we have a `REPO-maintainers` and `REPO-committers` group per project. The idea is that the `REPO-maintainers` group contains 1-3 people that will manage/lead the development of that project. The people in the group have some additional rights next to the people in the `REPO-committers` group. All differences can be found in the [GitHub role defintions](https://docs.github.com/en/organizations/managing-user-access-to-your-organizations-repositories/managing-repository-roles/repository-roles-for-an-organization) but some concrete examples are the management of labels for the repository or the mutation of the project description that is only allowed by people in the `REPO-maintainers` group.

## Creating PRs in the Governance Repository

There are five templates available for creating PRs. The best way to choose between them is with URL switching.

| Template Name            | URL Switch                                                                                                               | Description                                          |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| Organization Default     | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?quick_pull=1`                                     | Default template for PRs in Hiero-Ledger             |
| Custom Properites Update | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?template=custom_properties_update_pr_template.md` | Use when modifying custom properties file            |
| Create New Repository    | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?template=new_repository_pr_template.md`           | Use when creating a new repository                   |
| Create New Team          | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?template=new_team_pr_template.md`                 | Use when creating a new team                         |
| Vote Required            | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?template=vote_pr_template.md`                     | Use when adding new members or changing member roles |
