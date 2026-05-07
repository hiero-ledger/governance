# GitHub Token Request Guidelines

To automate some processes, users might require a token to access GitHub's API.
While personal tokens are **NOT** provided to users, access to a service account with the needed permissions could be issued instead. 
Follow these steps to request token permissions.

**Do not discuss token or account secrets in public**

More information on GitHub's REST API can be found in the [GitHub Docs](https://docs.github.com/en/rest?).

## Submit Your Request

- Start a new discussion in your organization using the "Token Requests" template or using [this link](https://github.com/orgs/hiero-ledger/discussions/new?category=token-requests).
  1. What type of token is being requested? (Classic or Fine-grained)
  2. How long are the permissions needed for? (Avoid long lived tokens requests unless there is a proper justification)
  3. What repositories are being accessed by the token? (Avoid "All" when possible)
  4. What permissions are needed by the token and why? (Refer to GitHub Docs to understand token permissions)
