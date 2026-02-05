# Adding GitHub accounts to groups in Hiero

In the [hiero-ledger organization](https://github.com/hiero-ledger), maintainers have write access to the [governance repository](https://github.com/hiero-ledger/governance) where user permissions are maintained.
[Maintainers](roles-and-groups.md#maintainers) should submit a PR to the hiero-ledger/governance repo in the `config.yaml` file to update users to the requested permissions.

## Clowarden configuration

The `config.yaml` file is used to configure all GitHub repositories of the organization.
https://clowarden.io is used to manage the GitHub repositories and permission list for all Hiero repos. The Clowarden tool log can be found [here](https://clowarden.io/audit/?organization=LFDT-Hiero).

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

There are multiple teams for each repository. These teams take the format `RepoName-maintainers` and `RepoName-committers`. There may be additional teams added at the discretion of the repository maintainers.
In each team, there are two sections that can be a little misleading: `maintainers` and `members`.
The `maintainers` section defines **not the project maintainers**.
For clowarden the `maintainers` section is needed and must contain at least one person that is already a member of the hiero-ledger GitHub organization.
That is must to create a valid group.
It is best practice to have only one person in the `maintainers` section.
The `members` section contains all the members of the group.
When an individual is nominated to become a Committer or a Maintainer, the PR should add the individual's GitHub username to the `members` section of the respective group. Note the username is case sensitive.

## Approving the new member

After a pull request is created, the maintainer(s) responsible for the team the individual is being added to are required to vote on the request.
Here we use GitVote for those voting.
A documentation of the voting process [can be found here](../rules-and-guidelines/asynchronous-voting.md).
