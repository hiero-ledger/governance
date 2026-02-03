# Adding GitHub accounts to groups in Hiero

In the [hiero-ledger organization](https://github.com/hiero-ledger), maintainers have write access to the [governance repository](https://github.com/hiero-ledger/governance) where user permissions are maintained.
[Maintainers](roles-and-groups.md#maintainers) should submit a PR to the hiero-ledger/governance repo in the `config.yaml` file to update users to the requested permissions.

## Clowarden configuration

The `config.yaml` file is used to configure all GitHub repositories of the organisation.
https://clowarden.io is used as tool to manage the GitHub resources and the change list for all Hiero repos can be found [here](https://clowarden.io/audit/?organization=LFDT-Hiero).

### Add a user to Clowarden configuration

The file `config.yaml` contains groups and their members.
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
      - user4
    members:
      - user5
      - user6
```

As you can see there are multiple groups.
In each group there are two sections that can be a little misleading: `maintainers` and `members`.
The `maintainers` section defines **not the project maintainers**.
For clowarden the `maintainers` section is needed and must contain at least one person that is already a member of the hiero-ledger GitHub organization.
That is must to create a valid group.
It is best practice to have only one person in the `maintainers` section.
The `members` section contains all the members of the group.
When a person is nominated to become a Committer or a Maintainer, the PR should add the person to the `members` section of the respective group.

When you want to add a new member to an existing group, you only need to add the GitHub account name of that member to the file.

## Approving the new member

After a pull request is created, the maintainers responsible for the group the user selected are required to vote on the request.
Here we use GitVote for those voting.
A documentation of the voting process [can be found here](../rules-and-guidelines/asynchronous-voting.md).
