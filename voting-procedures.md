# Voting Procedure

This file contains an overview of Hiero's voting procedure using the
automated [GitVote](https://github.com/cncf/gitvote) system.

For project-based exceptions to any of these procedures and how to request an exception, please refer to the
following [Tracker](https://github.com/hiero-ledger/governance/blob/main/project-rules-exceptions.md).

## Before You Start

### Understanding GitVote

GitVote is a GitHub application that automates voting on pull requests. All GitVote commands are typed **in PR comments
**, not in your terminal or command line.

### Am I Eligible to Vote?

You can vote if you are a member of the team associated with the voting profile being used. Check your team membership
in the [Hiero GitHub organization](https://github.com/orgs/hiero-ledger/teams) or ask a maintainer if you're unsure.

### Finding Team Names

GitHub team names follow the pattern `@hiero-ledger/<team-name>`. You can find exact team names in
the [config.yaml file](https://github.com/hiero-ledger/governance/blob/main/config.yaml) or by typing `@hiero-ledger/`
in any GitHub comment to see available teams.

## Quick Reference

**Common Voting Scenarios:**

- **Governance repository changes:** Use `/vote profile=default` → Notify
  `@hiero-ledger/lf-staff @hiero-ledger/tsc @hiero-ledger/github-maintainers`
- **Core project repos (hiero, hiero-website, tsc):** Use `/vote profile=hiero-project-maintainers-vote` → Notify
  `@hiero-ledger/tsc @hiero-ledger/github-maintainers`
- **SDK changes:** Use `/vote profile=hiero-sdk-<language>-maintainers-vote` → Notify
  `@hiero-ledger/hiero-sdk-<language>-maintainers`
- **Consensus Node changes:** Use `/vote profile=hiero-consensus-node-maintainers-vote` → Notify
  `@hiero-ledger/hiero-consensus-node-maintainers`

**Quick Actions:**

- **Check vote status:** Comment `/check-vote`
- **Cancel ongoing vote:** Comment `/cancel-vote`

## What requires a vote

A vote of Hiero maintainers is required in, but not necessarily limited to, the cases listed below:

1. Changes to the membership of a project group (limited to the maintainers of the affected project)
2. Changes to the permissions of a project group (limited to the maintainers of the affected project)
3. Adding or removing a project group
4. Changes to a project's exceptions from the guidelines and procedures defined in the governance repository.

The intent is for maintainers to vote on any change to project membership, roles, and exceptions.

## Choosing the Right Voting Profile

Before initiating a vote, you need to select the appropriate voting profile based on what your change affects:

| **Your Change Affects**                        | **Use Profile**                         | **Notify Teams**                                                            |
|------------------------------------------------|-----------------------------------------|-----------------------------------------------------------------------------|
| Governance repository itself                   | `default`                               | `@hiero-ledger/lf-staff @hiero-ledger/tsc @hiero-ledger/github-maintainers` |
| Core project repos (hiero, hiero-website, tsc) | `hiero-project-maintainers-vote`        | `@hiero-ledger/tsc @hiero-ledger/github-maintainers`                        |
| Consensus Node project                         | `hiero-consensus-node-maintainers-vote` | `@hiero-ledger/hiero-consensus-node-maintainers`                            |
| Mirror Node project                            | `hiero-mirror-node-maintainers-vote`    | `@hiero-ledger/hiero-mirror-node-maintainers`                               |
| Java SDK project                               | `hiero-sdk-java-maintainers-vote`       | `@hiero-ledger/hiero-sdk-java-maintainers`                                  |
| Python SDK project                             | `hiero-sdk-python-maintainers-vote`     | `@hiero-ledger/hiero-sdk-python-maintainers`                                |
| Other SDK projects                             | `hiero-sdk-<language>-maintainers-vote` | `@hiero-ledger/hiero-sdk-<language>-maintainers`                            |
| Documentation                                  | `hiero-docs-maintainers-vote`           | `@hiero-ledger/hiero-docs-maintainers`                                      |
| Security matters                               | `security-maintainers-vote`             | `@hiero-ledger/security-maintainers`                                        |

**Still unsure?** Check the [GitVote Configuration](#gitvote-configuration) section below or ask the maintainers in
the [hiero-general Discord channel](https://discord.com/channels/905194001349627914/1289954446712770600).

## How to initiate a vote

1. Open a PR with the changes you wish to propose (optional templates are available [here]([vote_pr_template.md](.github/PULL_REQUEST_TEMPLATE/))).
2. Add the `maintainer-vote` label to the PR
3. Use the GitVote command to start voting with the appropriate team profile:
   ```
   /vote profile=<team-name>-maintainers-vote
   ```
   This will cause the `git-vote` bot to post a comment with voting instructions. See
   the [Choosing the Right Voting Profile](#choosing-the-right-voting-profile) section for specific profile examples.

4. **Notify the voting team** by adding a comment that @mentions the team:
   ```
   @hiero-ledger/<team-name> please participate in this vote
   ```
   Refer to the [Choosing the Right Voting Profile](#choosing-the-right-voting-profile) table for specific team
   notification examples.

5. Post a link to the PR in the [Hiero maintainers channel](https://discord.com/channels/905194001349627914/1283487103006543952) for additional visibility.

GitVote will automatically:

- Set the voting duration to 2 weeks
- Enable voting for designated maintainer teams
- Track votes and calculate results
- Provide real-time status updates via GitHub checks

**Note:** GitVote does not automatically notify team members. The @mention in step 4 is required to ensure team members
receive GitHub notifications about the vote.

## How to cast votes

Once a vote is initiated, eligible maintainers can vote using GitHub reaction emojis:

- **In Favor:** Add 👍 reaction to the `git-vote` bot comment
- **Against:** Add 👎 reaction to the `git-vote` bot comment
- **Abstain:** Add 👀 reaction to the `git-vote` bot comment

Vote status is automatically tracked and displayed via GitHub checks on the PR.

## Vote monitoring

GitVote provides real-time vote tracking through:

- GitHub status checks showing current vote tally
- Automatic notifications when votes are cast
- Optional periodic status updates
- Vote result announcements (configurable)

Use `/check-vote` command to manually check current vote status.

## Concluding the vote

GitVote automatically concludes votes when:

1. **Vote passes:** At least 51% of **active voters** (those who vote in favor or against) vote in favor before the
   2-week deadline
2. **Vote fails:** The 2-week voting period expires without achieving majority approval

**Note:** The 51% threshold is calculated from active votes only (👍 and 👎), not from total eligible maintainers. Abstain
votes (👀) and non-participants do not count toward the denominator.

The PR status will be automatically updated with the final result.

Maintainers can use `/cancel-vote` to cancel an ongoing vote if needed.

## Vote Calculation

GitVote calculates pass/fail results based on **active votes cast**, not total eligible voters. Abstain votes are
excluded from the pass_threshold calculation.

### Calculation Example

If you have:

- 10 eligible voters defined in the voting profile
- 4 vote "in favor" (👍)
- 2 vote "against" (👎)
- 3 abstain (👀)
- 1 doesn't vote at all

**GitVote calculation:** 4 in favor out of 6 active votes = **66.7%**

- Active votes = in favor + against votes only (4 + 2 = 6)
- Abstain votes and missing votes are excluded from calculation
- With `pass_threshold: 51`, this vote would **pass**

## Merging After Vote Passes

Once a vote passes, the PR becomes eligible for merging. The merging process depends on the repository configuration:

### Manual Merging (Current Standard)
For most repositories, PRs require manual merging after a vote passes:

1. **Vote passes:** GitVote updates the PR status to show the passing result
2. **Manual merge required:** Someone with **write** or **maintain** privileges in that repository can merge the PR
3. **Who can merge:** Repository maintainers, GitHub organization owners, or users with write access to the specific repository
4. **Verification:** Before merging, the person should verify:
    - The vote genuinely passed (check GitVote status and vote tallies)

### Protected Branch Requirements (Future Configuration)
Some repositories may be configured to require a passing vote before allowing merges:

- **Branch protection rules:** Can be set to require GitVote status checks to pass
- **Automatic enforcement:** GitHub will prevent merging until vote requirements are satisfied
- **Override permissions:** Only users with admin privileges can override vote requirements
- **Status integration:** GitVote provides GitHub status checks that integrate with branch protection

### Best Practices for Merging

- **Verify vote legitimacy:** Ensure the vote was conducted properly with appropriate team participation
- **Check vote alignment:** Confirm the final PR state matches what voters reviewed and approved
- **Document decisions:** For significant governance changes, consider adding merge comments explaining the decision

**Note:** The person merging the PR does not need to have participated in the vote, but they must have appropriate repository permissions and should verify the vote was conducted properly.

## Vote participation

### Requirements

Maintainers are required to participate in votes within their area of responsibility. Participation includes:

- Casting a vote (👍, 👎, or 👀 reaction)
- OR posting a comment explaining non-participation

### Inactive Maintainer Policy

If a maintainer does not participate in enough consecutive votes without good reason (i.e. they are out on vacation),
they will be considered "inactive" which may be grounds for removal of maintainer status, consistent with existing
governance policies.

### Team-Based Voting Eligibility

Voting eligibility is determined by team membership as defined
in [config.yaml](https://github.com/hiero-ledger/governance/blob/main/config.yaml):

- `lf-staff`, `tsc`, and `github-maintainers` teams for governance repository votes (default profile)
- `tsc` and `github-maintainers` teams for core project repositories (hiero-project-maintainers-vote)
- Specific project maintainer teams for project-specific changes

## GitVote Configuration

The repository uses voting profiles configured in `.gitvote.yml`:

### Standard Governance Vote Profile

```yaml
default:
  duration: 2w
  pass_threshold: 51
  allowed_voters:
    teams: [ "lf-staff", "tsc", "github-maintainers" ]
  close_on_passing: false
```

### Hiero Project Maintainers Vote Profile

```yaml
hiero-project-maintainers-vote:
  duration: 2w
  pass_threshold: 51
  allowed_voters:
    teams: [ "tsc", "github-maintainers" ]
  close_on_passing: false
```

### Example SDK Team Vote Profile

```yaml
hiero-sdk-java-maintainers-vote:
  duration: 2w
  pass_threshold: 51
  allowed_voters:
    teams: [ "hiero-sdk-java-maintainers" ]
  close_on_passing: false
```

## Troubleshooting

### GitVote Issues

- If `/vote` command doesn't work, verify GitVote app installation and repository access
- If vote counting seems incorrect, use `/check-vote` to verify current status

### Configuration Problems

- Ensure `.gitvote.yml` is properly formatted and committed to main branch
- Verify team names in voting profiles match those in `config.yaml`
- Check that maintainer teams have proper GitHub permissions

### Process Questions

For questions about voting procedures or governance, contact the governance-triage team or create an issue in this
repository.