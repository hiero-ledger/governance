# What is StepSecurity?

[StepSecurity](https://www.stepsecurity.io) is a supply chain security platform that detects, prevents, and responds to attacks across the three main surfaces where modern software development is vulnerable:
CI/CD pipelines, code repositories, and developer machines.

In Hiero, we use its core product — **Harden-Runner** — which runs as a lightweight agent on every GitHub Actions workflow job and monitors everything that happens at runtime.
Functionalities in Hiero:

- **CI/CD pipelines:** Monitors all network calls, file writes, and process executions during every workflow run.
- **Code repositories:** Blocks compromised npm packages and enforces security best practices via pull requests.
- **Developer machines:** Inventories AI agents, IDE extensions, and local packages to catch threats early.

## How Harden-Runner works

[Harden-Runner](https://docs.stepsecurity.io/harden-runner) uses [eBPF](https://ebpf.io) (a Linux kernel technology) to observe every event at the OS level on GitHub Actions runners.
It does not require root access or custom runners — it installs in seconds inside any workflow step.

eBPF lets Harden-Runner intercept and correlate every outbound network call, file write, and process execution back to the exact workflow step that triggered it — without modifying your build scripts or tools.

Once installed, it can operate in two modes:

1. **Audit mode:** Passively logs all activity. Used when first adding StepSecurity to a workflow to learn its expected behavior and generate an allowed list. 
2. **Block mode:** Enforces a strict allowlist. Any network call or file access outside the expected set is blocked and an alert is generated. This is the hardened production state.

## Why StepSecurity is mandatory for all Hiero projects

Hiero is an open-source distributed ledger technology under the Linux Foundation Decentralized Trust.
Our repositories are public, accept contributions from anyone, and run automated workflows on every pull request and push.
This is exactly the attack surface that supply chain attackers target.

Concrete reasons:

- **Any contributor can trigger CI**: Every pull request — including from first-time or external contributors — triggers GitHub Actions. Without runtime monitoring, a malicious commit or compromised dependency runs freely.
- **Third-party actions can be hijacked**: GitHub Actions you use (e.g. `tj-actions/changed-files`) can be silently compromised. StepSecurity detected exactly this [CVE-2025-30066](https://nvd.nist.gov/vuln/detail/cve-2025-30066) in real time before most teams noticed.
- **Secrets can leave silently**: CI jobs have access to repository secrets and tokens. Without network egress monitoring, a compromised step can exfiltrate credentials to an external server without any visible trace.
- **Every repo shares the org's trust**: A compromised workflow in any one repo can be used to pivot — accessing org-level tokens, tagging releases, or poisoning artifact registries used by other projects.
- 
