# Steps for creating new repos in [hiero-ledger](https://github.com/hiero-ledger)

## Role Definitions

- **Repository Creation Agent (Community Architect) (CA)** 
  - The person responsible for transferring the repository
  - Must have ability to create a repository in the organization.
- **Repository Creation Approval Agent - Technical Steering Committee (TSC)**
  - The party responsible for approving PRs throughout the transfer process
  - Must have approval authority on the [Hiero-Ledger/governance][governance] repository and on the target repository

## 1. Before Creating a New Repo

- Review our [Project Criteria guidelines](https://github.com/hiero-ledger/hiero/blob/main/project-criteria.md).
  These guidelines will ensure that the project:
  - Is able to adapt to [Hiero's mission](https://github.com/hiero-ledger/hiero/blob/main/project-criteria.md#hieros-mission-and-technical-charter).
  - Participants understand the basis of Open Source collaboration.
  - Has an [adequate license](https://lf-decentralized-trust.github.io/governance/governing-documents/allowed-third-party-licenses/#approved-licenses-for-allowlist).
  - Is willing to promote participation and growth alongside other projects in the organization.
  - Review [LFDT's TAC requirements](https://lf-decentralized-trust.github.io/governance/governing-documents/) to maintain overall project status.
   
## 2. Project Proposal or Request of Repo Addition to an Existing Project

- New project proposals or request for adding a new repository to an existing project must be reviewed and approved by the TSC.
- These requests need to be created as [GitHub issues in the tsc repo](https://github.com/hiero-ledger/tsc/issues) and labeled as ["project proposal"](https://github.com/hiero-ledger/tsc/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22project%20proposal%22)

## 3. Project or Repo approval process

- **All project proposals need to be presented to the TSC prior to requesting a vote.**
- 50% TSC approval vote is required for both project proposals and new repo additions (as defined in chapter 4 of the [technical charter](https://github.com/hiero-ledger/governance/blob/main/hiero-technical-charter.md).
- This can be done in 2 ways:
  - Add your GitHub Issue to the agenda in the next TSC meeting.
  - After presenting your project, a vote can happen during the TSC meeting itself which is a recorded meeting.
  - Optionally, an asyn vote can happen using [GitVote](https://github.com/cncf/gitvote) to collect votes from the TSC members outside the meeting and after having presented the proposal:
    - Create your GitHub Issue
    - Make sure the **tsc** team is tagged in the reviewers
    - Comment **/vote-tscprojectproposal** to start the vote
    - Refer to the [GitVote configuration file](https://github.com/hiero-ledger/tsc/blob/main/.gitvote.yml) to review the profile parameters.
  - Address any issues/concerns brought up by the TSC team to obtain approval.
   
## 4. After Project Approval

Reach out to the CA to help create the repo CLA

- Create a PR to add the new repo in the [governance config file](https://github.com/hiero-ledger/governance/blob/main/config.yaml) [Example](https://github.com/hiero-ledger/governance/pull/346)
- Follow the PR comments for any corrections needed to be done in your change.
- Tag [**@hiero-ledger/lf-staff**](https://github.com/orgs/hiero-ledger/teams/lf-staff) in your GitHub issue if you need help with creating the PR to add the new repository

## 5. After Project Creation

- Committers and Maintainers are responsible for the content of the repository and compliance with the [Project Criteria guidelines](https://github.com/hiero-ledger/hiero/blob/main/project-criteria.md).
- Committers and Maintainers are responsible for updating any documentation in [hiero-docs](https://github.com/hiero-ledger/hiero-docs) and [hiero-website](https://github.com/hiero-ledger/hiero-website)
- Committers and Maintainers are responsible for promoting collaboration and diversity in their new repo.
