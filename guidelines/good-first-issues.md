# 🐣 Good First Issue Guidelines

This guide explains what qualifies as a “Good First Issue” and how to create one for new contributors.
All our good first issues are labeled with the `good first issue` label.
An overview of all open good first issues can be found [here](https://github.com/issues?q=is%3Aopen+is%3Aissue+org%3Ahiero-ledger+archived%3Afalse+label%3A%22good+first+issue%22+).

## What is a Good First Issue?

A Good First Issue is a task that is suitable for newcomers to the project. It should be:

- **Well-defined**: The issue should have a clear goal and scope.
- **Manageable**: The task should be small enough to be completed in a reasonable amount of time (typically a few hours).
- **Educational**: The issue should help the newcomer learn about the project and its codebase.
- **Non-critical**: The issue should not involve critical functionality or complex dependencies.
- **Documented**: The issue should include all necessary information, such as links to relevant documentation, code examples, and any prerequisites.

Examples of Good First Issues:

- Documentation updates (typos, broken links, clarifying setup steps).
- Adding or improving tests for small, isolated components.
- Code style or linting improvements.
- Simple bug fixes with clear reproduction steps.
- Small feature enhancements (e.g., adding a config flag, improving log messages).

## How to Create a Good First Issue

When creating a Good First Issue, the best is to follow our template:

```markdown
## 🆕🐥 First Timers Only

This issue is reserved for people who have never contributed to [Hiero](https://hiero.org) or any open source project in general.
We know that creating a pull request (PR) is a major barrier for new contributors.
The goal of this issue and all other issues labeled by [**'good first issue'**](https://github.com/issues?q=is%3Aopen+is%3Aissue+org%3Ahiero-ledger+archived%3Afalse+label%3A%22good+first+issue%22+) is to help you make your first contribution to Hiero.

## 👾 Description of the issue

AT THIS SECTION YOU NEED TO DESCRIBE THE ISSUE IN A WAY THAT IS UNDERSTANDABLE TO NEW CONTRIBUTORS.
YOU MUST NOT ASSUME THAT SUCH CONTRIBUTORS HAVE ANY KNOWLEDGE ABOUT THE CODEBASE OR HIERO.
IT IS HELPFUL TO ADD LINKS TO THE RELEVANT DOCUMENTATION AND/OR CODE SECTIONS.

## 💡 Solution

AT THIS SECTION YOU NEED TO DESCRIBE THE STEPS NEEDED TO SOLVE THE ISSUE.
PLEASE BREAK DOWN THE STEPS AS MUCH AS POSSIBLE AND MAKE SURE THAT THEY ARE EASY TO FOLLOW.
IF POSSIBLE, ADD LINKS TO THE RELEVANT DOCUMENTATION AND/OR CODE SECTIONS.

### 👩‍💻 Implementation

AT THIS SECTION YOU NEED TO DESCRIBE THE TECHNICAL STEPS NEEDED TO SOLVE THE ISSUE.
PLEASE BREAK DOWN THE STEPS AS MUCH AS POSSIBLE AND MAKE SURE THAT THEY ARE EASY TO FOLLOW.
IF POSSIBLE, ADD LINKS TO THE RELEVANT DOCUMENTATION AND/OR CODE.

## 📋 Step by step guide to do a contribution

If you have never contributed to an open source project at GitHub, the following step-by-step guide will introduce you to the workflow.
More information and concrete samples for shell commands for each step can be found in our [CONTRIBUTING.md](https://github.com/hiero-ledger/.github/blob/main/CONTRIBUTING.md) file.
A more detailed general documentation of the GitHub PR workflow can be found [here](https://github.com/firstcontributions/first-contributions/blob/master/README.md).

- [ ] **Claim this issue:** Comment below that you are interested in working on the issue
- [ ] **Wait for assignment:** A community member with the given rights will add you as an assignee of the issue
- [ ] **Fork the repository:** You can do that in GitHub (by simply clicking the 'fork' button).
- [ ] **Check out the forked repository**
- [ ] **Create a feature branch** for the issue. We do not have a hard naming definition for branches but it is best practice to prefix the branch name with the issue id.
- [ ] **Solve the issue** in your branch.
- [ ] **Commit your changes:** Here, it is needed to add `sign-off` information to the commit to accept the "Developer Certificate of Origin" (https://developercertificate.org).
  Next to that every commit must be [verified](https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification).
  We do not have a hard definition for commit messages but it is best practice to use the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
  More details can be found in our [CONTRIBUTING.md](https://github.com/hiero-ledger/.github/blob/main/CONTRIBUTING.md)
- [ ] **Start a Pull Request (PR)**: When creating a pull request the name of the PR must follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification.
  A GitHub Action will automatically check that the PR name is following the specification and will block the merge if that is not the case.
  Next to that, the `sign-off` information and the verification of all commits will be checked automatically.
- [ ] **Check GitHub Actions:** Several GitHub Actions will be triggered automatically for each PR.
  If a GitHub Action fails and you do not understand the cause of that error do not hesitate to add a comment to the PR and ask the Hiero developer community for support.
- [ ] **Wait for reviews:** Members of the Hiero developer community will review your PR.
  If a reviewer finds any missing pieces or a problem, he or she will start a discussion with you and describe the next steps for solving the problem.
- [ ] **You did it 🎉:** We will merge the fix in the develop branch. Thanks for being part of the Hiero community as an open-source contributor ❤️

## 🎉 Contribute to Hacktoberfest

At the time of the [Hacktoberfest](https://hacktoberfest.digitalocean.com) event we try to mark all PRs that solve any good first issue with the `hacktoberfest-accepted` label.
If you want to solve this issue as part of Hacktoberfest, and we missed to add the label, just add a comment to the issue or PR, and we will add it.

## 🤔 Additional Information

If you have any questions about the topic of this issue, just ask us directly in this issue by adding a comment.
Next to that we want to invite you to join our community at our [Discord](https://discord.gg/kEnnmB9A) server or join our [public community calls](https://zoom-lfx.platform.linuxfoundation.org/meetings/hiero?view=week).
A general manual about open-source contributions can be found [here](https://github.com/firstcontributions/first-contributions/blob/master/README.md).
```

Once you created the issue, please make sure to add the `good first issue candidate` label to it.
Please do not add the `good first issue` label directly, as we want to review all issues before adding that label.

## Reviewing Good First Issues Candidates

All candidates for good first issues can be found [here](https://github.com/issues?q=is%3Aopen%20is%3Aissue%20org%3Ahiero-ledger%20archived%3Afalse%20label%3A%22good%20first%20issue%20candidate%22).

The review process for good first issues candidates is as follows:

1. **Verify Issue Completeness:** Ensure the issue contains a clear description, expected outcome, relevant links, and any necessary context or prerequisites.
2. **Check Scope and Complexity:** Confirm that the issue is well-defined, manageable, educational, non-critical, and documented, as outlined above.
3. **Assess Suitability for Newcomers:** Make sure the issue does not require deep project knowledge or access to sensitive resources.
4. **Provide Feedback:** If the issue is missing information or does not meet the criteria, leave a comment with suggestions for improvement.
5. **Label Appropriately:** Once the issue meets all requirements, remove the `good first issue candidate` label and add the `good first issue` label.
6. **Encourage Discussion:** Invite the original author and other contributors to ask questions or clarify details as needed.

By following these steps, maintainers help ensure that good first issues are welcoming and accessible to new contributors.
