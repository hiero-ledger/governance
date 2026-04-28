## What is DCO?

DCO (Developer Certificate of Origin) is a lightweight way for contributors to certify that they have the right to submit their code to an open-source project. It is widely used as a simpler alternative to a formal Contributor License Agreement (CLA).

## Why is DCO Important

Developer Certificate of Origin (DCO) is important because it establishes a clear paper trail for every contribution to a project. It serves as a lightweight alternative to a formal Contributor License Agreement (CLA) while providing critical protections for both maintainers and users. 

Available soon: LFDT Architect team is working on an offical DCO documentation with the legal team.

## How DCO GitHub Action Works and What is DCO-2

DCO2 is a GitHub App that enforces the Developer Certificate of Origin (DCO) on Pull Requests.
It aims to be a drop-in replacement for dcoapp/app.

More information on DCO2 can be found [here](https://github.com/cncf/dco2).

## How do I Add/Fix DCO

To comply with a DCO requirement, every commit message must include a "sign-off" line:

- **Format**: Signed-off-by: Your Name <your.email@example.com>
- **Git Command**: You can automate this by adding the -s flag to your commit command: git commit -s -m "Your message".

If a check fails because you forgot to sign off, you can fix it by amending your commit history:

1. Amend the last commit: git commit --amend --no-edit -s
2. Force push: git push --force-with-lease
3. For multiple commits: Use an interactive rebase (git rebase -i) to add the sign-off to previous commits.
