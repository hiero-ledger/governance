# Hiero technical governance

[![CII Best Practices](https://bestpractices.coreinfrastructure.org/projects/10697/badge)](https://bestpractices.coreinfrastructure.org/projects/10697)

This repository contains all governance documents of the Hiero project:

- The [elections](elections) folder contains information and rules about the elections of the Hiero **Technical Steering Committee** (TSC).
- The `config.yaml` file that is used to configure all GitHub repositories of the organisation.
  https://clowarden.io is used as tool to manage the GitHub resources and the change list for all Hiero repos can be found [here](https://clowarden.io/audit/?organization=LFDT-Hiero).
- The [roles-and-groups.md](roles-and-groups.md) file contains the rules for the roles and groups of the Hiero project.

## Creating PRs in the Governance Repository

There are five templates available for creating PRs. The best way to choose between them is with URL switching.

| Template Name            | URL Switch                                                                                                               | Description                                          |
|--------------------------|--------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------|
| Organization Default     | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?quick_pull=1`                                     | Default template for PRs in Hiero-Ledger             |
| Custom Properties Update | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?template=custom_properties_update_pr_template.md` | Use when modifying custom properties file            |
| Create New Repository    | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?template=new_repository_pr_template.md`           | Use when creating a new repository                   |
| Create New Team          | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?template=new_team_pr_template.md`                 | Use when creating a new team                         |
| Vote Required            | `https://github.com/hiero-ledger/governance/compare/main...<my-branch>?template=vote_pr_template.md`                     | Use when adding new members or changing member roles |

## Contribute

- To contribute, please refer to the **[Hiero-Ledger's contribution guidelines](https://github.com/hiero-ledger/.github/blob/main/CONTRIBUTING.md)**

## Help/Community

- Join our [community discussions](https://discord.lfdecentralizedtrust.org/) on discord.

## About Users and Maintainers

- Users and Maintainers guidelies are located in **[Hiero-Ledger's roles and groups guidelines](https://github.com/hiero-ledger/governance/blob/main/roles-and-groups.md#maintainers).**

## License

- Hiero's source code is available under the **Apache License, Version 2.0 (Apache-2.0)**
