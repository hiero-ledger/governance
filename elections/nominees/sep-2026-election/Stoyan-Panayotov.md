# Nomination for Hiero TSC Maintainer seat

### Candidate

Stoyan Panayotov - [stoqnkpL](https://github.com/stoqnkpL)

This is a self-nomination for re-election. I currently serve on the Hiero TSC.

### Qualifications

I have worked in the Hedera/Hiero ecosystem since 2021, focused on the smart contract stack: the EVM inside the consensus node, and the surrounding tooling that developers actually build against - the [JSON-RPC Relay](https://github.com/hiero-ledger/hiero-json-rpc-relay),
[Hiero Local Node](https://github.com/hiero-ledger/hiero-local-node), the mirror node's web3 module, and the SDKs.
I am a committer on [hiero-consensus-node](https://github.com/hiero-ledger/hiero-consensus-node) and [hiero-improvement-proposals](https://github.com/hiero-ledger/hiero-improvement-proposals), and a member of the current TSC.

**Smart contracts and EVM equivalence.** I worked on integrating the Besu EVM into the consensus node and on the smart contract service built on top of it, so that standard Ethereum tooling and contracts work against Hedera without giving up hashgraph consensus. Much of my work since has been closing the remaining gaps between "runs on an EVM chain" and "runs on Hedera" - in the network itself and in the tooling around it.

**Protocol design through the HIP process.** I have authored or co-authored several HIPs, most of them concerned with bridging Hiero-native services and the EVM:

- **[HIP-376](https://hips.hedera.com/hip/hip-376): Support Approve/Allowance/transferFrom standard calls from
  ERC20 and ERC721** (author) - let native Hedera Token Service tokens be used through the standard ERC-20/ERC-721
  approval and allowance interfaces, so existing Ethereum contracts and tooling can work with them unmodified.
- **[HIP-435](https://hips.hedera.com/hip/hip-435): Record Stream V6** (author) - moved the record file definition
  to protobuf and introduced sidecar records, giving the network a general mechanism for externalising extra
  transaction detail without bloating the main record stream. Sidecars are what later traceability work is built on.
- **[HIP-513](https://hips.hedera.com/hip/hip-513): Smart Contract Traceability Extension** (co-author, with
  Mustafa Uzun and Steven Sheehy) - externalised contract state changes, actions and bytecode via sidecars,
  which is what made real contract-level debugging and observability possible on mirror nodes.
- **[HIP-583](https://hips.hedera.com/hip/hip-583): Expand alias support in CryptoCreate & CryptoTransfer
  Transactions** (working group) - removed a major barrier for users and developers coming from Ethereum by
  letting them transact against accounts addressed by EVM alias.
- **[HIP-801](https://hips.hedera.com/hip/hip-801): Add support for `debug_traceTransaction` RPC API**
  (co-author, with Ivan Kavaldzhiev) - brought the standard Ethereum transaction-tracing API to the JSON-RPC Relay
  and mirror node, which is the debugging entry point most contract developers reach for first.
- **[HIP-844](https://hips.hedera.com/hip/hip-844): Handling and externalisation improvements for account nonce
  updates** (author) - defined when an Ethereum transaction signer's nonce is updated and how that update is externalised, resolving cases where consensus nodes and mirror nodes disagreed on an account's nonce.

**Working across sub-projects.** A change to the EVM rarely stays in one repository: it lands in the consensus node, then has to be reflected in the mirror node, the relay, the local node and the SDKs before a developer can use it. Most of what I have done has required getting those teams to agree on a shape, and that cross-repository view is what I try to bring to TSC discussions.

**Tracking the upstream ecosystem.** I follow EIPs, Ethereum network upgrades and Besu releases, assess what they
mean for Hiero, and turn that into concrete proposals and roadmap input rather than a standing list of gaps. That work has fed both the HIPs above and quarterly prioritisation with the technical leads.

### Commitments

As required of nominees by section 2.ix.b of the [TSC Charter](https://github.com/hiero-ledger/governance/blob/main/hiero-technical-charter.md):

- **Bandwidth.** I have the available bandwidth to invest in the TSC, and I commit to it: attending TSC meetings,
  reviewing HIPs and proposals brought to the committee, and taking on the follow-up work that comes out of them.
  I have kept this up during my current term and my circumstances are unchanged.
- **Professional experience.** I have spent my career as a software engineer on distributed systems and
  blockchain protocols, and the last five years specifically on Hiero's consensus and smart contract layers -
  both the protocol design and the implementation.
- **Neutrality.** My background is in one part of the stack, which makes it my responsibility to weigh proposals
  on what they do for Hiero as a whole rather than for the sub-projects I know best. I will keep judging
  proposals on their technical merit and their effect on the project overall, and I will say plainly when a
  decision touches work I am close to.

### Statement

I would be honoured to continue serving on the Hiero TSC. Hiero's value comes from being a genuinely open,
vendor-neutral home for this technology, and the TSC's job is to keep the technical decisions worthy of that.

If re-elected, I want to keep pushing on three things: keeping Hiero's EVM close to upstream Ethereum so the
ecosystem's tooling keeps working here by default; making sure changes are designed across sub-projects rather
than shipped in one repository and patched into the rest; and keeping the HIP process a real technical forum,
where proposals get substantive review and contributors outside the largest teams can get a fair hearing.
