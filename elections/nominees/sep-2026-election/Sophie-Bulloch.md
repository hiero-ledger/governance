# Nomination for Hiero TSC Maintainer seat

### Candidate

Sophie Calderon Bulloch - [exploreriii](https://github.com/exploreriii)

### Qualifications

**Ecosystem breadth — SDKs, developer experience, and applications.**

I am a long-standing maintainer of
[hiero-sdk-python](https://github.com/hiero-ledger/hiero-sdk-python) and the
[Hiero website](https://github.com/hiero-ledger/hiero-website). I am also a committer on the
[sdk-collaboration-hub](https://github.com/hiero-ledger/sdk-collaboration-hub), and a member of
the org-wide `github-maintainers` team that operates hiero-ledger's GitHub infrastructure. I am also a contributor-facing member of the `good-first-issue-support` team, helping to lead its governance operations. 

Beyond
hiero-ledger I prototype in Hiero Hackers the application layer the charter names in its scope. For instance, 
[hiero-x402](https://github.com/hiero-hackers/hiero-x402) (per-request agentic payments in HBAR/USDC
with cryptographically checked settlement) and
[hiero-payment-requests](https://github.com/hiero-hackers/hiero-payment-requests), and I co-build
project CI tooling such as [sdk-automations](https://github.com/hiero-hackers/sdk-automations), a
GitHub App for repository-owned governance automation. I also work to improve data and transparency for governance at Hiero having co-built [Hiero Hackers Analytics](https://github.com/hiero-hackers/analytics).

**Governance practice — building the contributor pipeline.** Within Hiero governance I designed
and operate the contributor ladder the charter asks the TSC to oversee: I helped to create a triage rung
for junior committers ([#447](https://github.com/hiero-ledger/governance/pull/447)), founded the
good-first-issue support group ([#457](https://github.com/hiero-ledger/governance/pull/457),
[#461](https://github.com/hiero-ledger/governance/pull/461)) which now spans multiple sub-projects
([#465](https://github.com/hiero-ledger/governance/pull/465),
[#470](https://github.com/hiero-ledger/governance/pull/470)), and have advanced **15+ contributors**
into triage, committer, and maintainer roles — including hiero-sdk-python's current co-maintainer
([#420](https://github.com/hiero-ledger/governance/pull/420),
[#489](https://github.com/hiero-ledger/governance/pull/489)). I also do
stewardship culling: auditing and removing inactive permission holders org-wide that may help tighten security at Hiero
([#517](https://github.com/hiero-ledger/governance/pull/517),
[#657](https://github.com/hiero-ledger/governance/pull/657)). To ground this work in evidence I
built the open [Hiero analytics dashboard](https://hiero-hackers.github.io/analytics/)
([source](https://github.com/hiero-hackers/analytics)), which measures organisation activity and
contributor diversity across hiero-ledger and is reproducible by anyone.


**Engineering depth — building and maintaining a production SDK.** As a long-standing maintainer of
[hiero-sdk-python](https://github.com/hiero-ledger/hiero-sdk-python) I work on the layer where
the protocol meets developers such as: cryptographic signing, protobuf serialization, the transaction
and query lifecycle, and network retry semantics. Regarding the underlying protocol layer, I have also built
early-stage independent verification tooling:
[hiero-streams-rs](https://github.com/hiero-hackers/hiero-streams-rs) (Rust — parses and
cryptographically verifies record stream files, both the v6 and HIP-1056 eras) and
[hiero-block-verifier-js](https://github.com/hiero-hackers/hiero-block-verifier-js) (pure
TypeScript, HIP-1056/1200 block proofs). I work across Python, Rust, and TypeScript. I also have extensive CI/CD experience at Hiero Ledger, creating the contributor-facing automation pipeline and helping to lead efforts to improve SSF scores and CodeQL use at Hiero Ledger. Such experience allowed the creation of a Linux Foundation mentorship which seeks to provide plug-in, configurable, contributor-facing automations for Hiero Ledger to use.

**By the numbers — hiero-ledger, since the project's commencement in 2024** (public GitHub data, reproducible via the analytics dashboard):

- **1,250+ pull requests reviewed** across hiero-ledger
- **263 good-first-issues created** to bring new contributors in
- **146 pull requests merged across 9 hiero-ledger repositories**
- **15+ contributors advanced to committers and maintainers** through roles of infrastructure I helped design

### Statement

I am committing the bandwidth this seat requires: the TSC's meetings, votes, and evaluation work
would sit alongside the maintainer duties I already carry out daily, and my track record shows I
sustain that kind of steady work day in and day out.

What I would bring is a voice to the layer where most of Hiero's future contributors arrive —
SDKs, developer experience, and onboarding — backed by hands-on experience of independently
verifying the network's outputs and of growing Hiero's contributor base and application layer.

On neutrality: I am not employed by any organisation related to Hiero Ledger or Hiero Hackers therefore can focus on the needs brought to the TSC. I have received some sponsorship to attend a handful of community events. My work deliberately spans sub-projects: a Python SDK, triage in the other SDKs, the website, org-wide
GitHub operations, governance tooling, and verification libraries spanning three languages that complement the ecosystem. I would help to
represent the ecosystem layer of Hiero as a whole, not any single sub-project, and I have no
interest in outcomes that favour one repository over the health of the project.
