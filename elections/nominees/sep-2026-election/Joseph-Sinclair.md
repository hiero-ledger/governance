# Nomination for Hiero TSC Maintainer seat

### Candidate

Joseph Sinclair - [jsync-swirlds](https://github.com/jsync-swirlds)

### Qualifications

**A proven maintainer with depth across the core network stack.**

Hiero's governance records list Joseph as a
[Hiero Block Node Maintainer](https://github.com/hiero-ledger/governance/blob/main/config.yaml#L138-L145),
as well as a committer on both
[Hiero Consensus Node](https://github.com/hiero-ledger/governance/blob/main/config.yaml#L164-L205)
and [Hiero Improvement Proposals](https://github.com/hiero-ledger/governance/blob/main/config.yaml#L575-L615).
That combination reflects the role he already plays in practice: connecting protocol design,
consensus-node behavior, block-stream production, and the Block Node systems that consume and
serve those streams.

Joseph's public contribution record is sustained and substantial. GitHub attributes at least
**159 merged pull requests** to him across Hiero: **95** in
[hiero-block-node](https://github.com/hiero-ledger/hiero-block-node/pulls?q=is%3Apr+author%3Ajsync-swirlds+is%3Amerged),
**53** in
[hiero-consensus-node](https://github.com/hiero-ledger/hiero-consensus-node/pulls?q=is%3Apr+author%3Ajsync-swirlds+is%3Amerged),
and **11** in
[hiero-improvement-proposals](https://github.com/hiero-ledger/hiero-improvement-proposals/pulls?q=is%3Apr+author%3Ajsync-swirlds+is%3Amerged).
Those contributions span 2023 through the present and show consistent delivery rather than a
short burst of activity.

**Block streams and operational reliability.**

Joseph has helped turn Block Node from an architectural proposal into an operable distributed
system. Representative work includes creating a simpler
[stream subscriber plugin](https://github.com/hiero-ledger/hiero-block-node/pull/1058) that moves
cleanly between historical and live blocks; reducing
[out-of-memory risk under high load](https://github.com/hiero-ledger/hiero-block-node/pull/1543);
documenting the sequencing and responsibilities for the
[record-stream to block-stream cutover](https://github.com/hiero-ledger/hiero-block-node/pull/2193);
adding detection, recovery, tests, and metrics for
[stalled publishers](https://github.com/hiero-ledger/hiero-block-node/pull/2665); and connecting
[live roster and address-book data](https://github.com/hiero-ledger/hiero-block-node/pull/3289)
to publisher discovery and end-of-stream handling. This is the kind of work a TSC needs to
understand: protocol semantics, failure modes, deployment transitions, observability, and the
operational consequences of design decisions.

His earlier Consensus Node work shows the same breadth. He helped establish the modular
[Schedule Service](https://github.com/hiero-ledger/hiero-consensus-node/pull/7664), extended
pre-handle behavior for
[optional keys and hollow accounts](https://github.com/hiero-ledger/hiero-consensus-node/pull/6542),
and has continued working at the boundary between Consensus Node and Block Node, including the
[skip and resend protocol](https://github.com/hiero-ledger/hiero-consensus-node/pull/18133) for
block delivery. He understands both sides of one of Hiero's most important architectural
transitions.

**Protocol design and cross-project judgment.**

Joseph is an author or co-author of seven HIPs:
[HIP-1037, Protocol Buffer API Specification](https://github.com/hiero-ledger/hiero-improvement-proposals/blob/main/HIP/hip-1037.md),
[HIP-1046, gRPC-Web proxy endpoints](https://github.com/hiero-ledger/hiero-improvement-proposals/blob/main/HIP/hip-1046.md),
[HIP-1081, Block Node](https://github.com/hiero-ledger/hiero-improvement-proposals/blob/main/HIP/hip-1081.md),
[HIP-1137, Block Node discoverability](https://github.com/hiero-ledger/hiero-improvement-proposals/blob/main/HIP/hip-1137.md),
[HIP-1299, dynamic address-book refinements](https://github.com/hiero-ledger/hiero-improvement-proposals/blob/main/HIP/hip-1299.md),
[HIP-1313, high-volume entity creation](https://github.com/hiero-ledger/hiero-improvement-proposals/blob/main/HIP/hip-1313.md),
and [HIP-1398, TSS Ceremony](https://github.com/hiero-ledger/hiero-improvement-proposals/blob/main/HIP/hip-1398.md).
Six of these have already reached Accepted, Approved, or Final status. He has also participated in
working groups for five other HIPs. The topics range from API specification and service discovery
to network operations, throttling, address books, and cryptographic ceremony design. That range
demonstrates advanced professional experience and the ability to reason beyond a single repository.

**He already shows up for TSC work.**

The published minutes name Joseph as a guest at **nine TSC meetings from October through December
2025** (from [October 14](https://github.com/hiero-ledger/tsc/blob/main/minutes/2025-10-14.md)
through [December 16](https://github.com/hiero-ledger/tsc/blob/main/minutes/2025-12-16.md)) and at
**ten more meetings in 2026**. He does more than attend: he explained
[HIP-1313](https://github.com/hiero-ledger/governance/wiki/TSCCall20260106), presented
[HIP-1137](https://github.com/hiero-ledger/governance/wiki/TSCCall20260203) and
[HIP-1398](https://github.com/hiero-ledger/governance/wiki/TSCCall20260303), and contributed to the
TSC's technical review of
[state-proof design](https://github.com/hiero-ledger/governance/wiki/TSCCall20260428). This record
is direct evidence of both available bandwidth and a willingness to do the substantive preparation
the role requires.

### Commitments

By commenting `I approve this nomination`, Joseph confirms the commitments required by section
2.ix.b of the [TSC Charter](https://github.com/hiero-ledger/governance/blob/main/hiero-technical-charter.md):

- **Bandwidth.** He has the available bandwidth to attend TSC meetings, review proposals, vote,
  and follow through on work arising from the committee.
- **Professional experience.** His record as a Block Node Maintainer, Consensus Node and HIP
  committer, HIP author, and cross-project engineer demonstrates advanced professional experience
  in the scope of Hiero.
- **Neutrality.** He will evaluate proposals on their technical merit and their effect on Hiero as
  a whole, disclose relevant conflicts, and balance the interests of any employer or sub-project
  against the long-term success of the Project.

### Nominator's Statement

I know Joseph as both a colleague and a friend. He consistently shows up to Hiero TSC meetings,
comes prepared, and is reliable about following work through. His public record matches my own
experience of him: he combines deep technical knowledge with careful operational judgment and a
willingness to engage constructively across teams. I believe he will serve Hiero well and help guide
its future in an open, technically rigorous, and project-first way.
