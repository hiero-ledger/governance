# Asynchronous Voting Using GitVote

[GitVote](https://github.com/cncf/gitvote) is a GitHub application that allows holding a vote on issues and pull requests.
More background information and how GitVote can be configured, can be found in the original GitVote documentation site. 

# How to Configure GitVote?

GitVote allows for a great flexibility of options to perform a vote. As described in the original GitVote page documentation, GitVote uses a configuration file [.gitvote.yml](https://github.com/hiero-ledger/.github/blob/main/.gitvote.yml) at a root level in our .github repo which contains an arrange of options for maintainer teams to vote on issues and pull requests.
Each repo in GitHub's hiero-ledger organization inherits this configuration file if there is no local .gitvote.yml file at the root of said repo.

Project maintainers can either create a local .gitvote.yml file in the root of their repo with the desired configuration that allows them to conform to their voting process or they can request changes to the main [.gitvote.yml](https://github.com/hiero-ledger/.github/blob/main/.gitvote.yml) file by opening a pull request against this file. 

# When and How to Cast an Asynchronous Vote

Anyone can trigger a vote via issues and pull request comments. Detailed information on how the comments trigger votes can be found in the original [GitVote usage documentation](https://github.com/cncf/gitvote?tab=readme-ov-file#usage).

The supported profiles to cast a vote using **"/vote-[profileName]"** via comments can be found under the [profile section](https://github.com/hiero-ledger/.github/blob/main/.gitvote.yml#L46) of the main .gitvote.yml configuration file. If the repo in question has a local .gitvote.yml file, the profile section in that file describes the different types of votes that can be performed. 

Depending on the profile called, GitVote will post a comment on the issue or pull request where it was invoked to the team/teams invited to participate in the vote. Votes from users outside those teams won't count towards the total of the vote.

It is up to project maintainers to decide when to run an asynchronous vote using GitVote vs calling for a vote on a project meeting. Similarly, the TSC can decide to run an asynchronous vote in cases where a meeting does not have enough quorum for example. The important aspect, is to keep all votes recorded and registered for later reference.

# Recommendations

It is strongly recommended that anyone invoking GitVote in an issue or pull request proactively notify participants, such as by announcing it during public meetings or posting a heads up in relevant Discord channels, to ensure adequate awareness and participation.

# GitVote Usage Example

https://github.com/hiero-ledger/governance/pull/475
