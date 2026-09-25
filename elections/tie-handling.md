# Handling of ties in elections

If, in any election under 3.h.iii to 3.h.vi [of the charter](https://github.com/hiero-ledger/governance/blob/main/hiero-technical-charter.md),
two or more candidates receive an equal number of votes and the number of seats still to be filled is lower than
the number of such candidates, those seats shall be allocated among the tied candidates only, as set out below.
All other seats are allocated as normal and are unaffected.

## Related Parties

The limit in 3.h.vii.1 of the charter is applied before any of the steps below.
A candidate whose election would exceed the number of TSC Members permitted from one group of Related Parties
is not eligible for the seat in question and takes no part in the runoff or the draw.

## Withdrawal

Any tied candidate may withdraw before the tie is resolved.
If withdrawals leave no more candidates than open seats, the remaining candidates are elected and no further step is required.

## Runoff

The TSC shall hold a runoff among the tied candidates, open to the same Selecting Group as the original election,
lasting no fewer than seven (7) and no more than fourteen (14) calendar days.
At most one runoff shall be held per election.

## Lot

If the runoff does not resolve the tie, the seats shall be allocated by random lot among the remaining tied candidates.
The method shall be published before the draw, shall be reproducible from publicly available data by any Collaborator,
and the draw shall take place in a meeting open to the public.

### Announcement

The TSC shall publish an announcement no less than 48 hours before the announced draw, containing:

- the tied candidates, in fixed order (alphabetical by GitHub login, case-insensitive), numbered from `0`
- the number of seats to be allocated
- the source of randomness chosen by the TSC, and the value to be used from it
  (for Option A the chain hash and round number, for Option B the timestamp)
- the rule by which the randomness is mapped onto the candidate list

The value to be used does not exist at the time of publication and cannot be predicted by anyone, including
the TSC. Neither the candidate list, its order, the number of seats, the source, nor the announced value may
be changed after publication. If any of them has to change, the announcement is void and a new one must be
published for a later point in time.

This ordering is what makes the draw trustworthy. The source cannot be manipulated into producing a chosen
name, but the mapping from the random value onto a name can be — by anyone who gets to choose the candidate
order after seeing the value. Publishing the order first removes that possibility.

### Choosing the source of randomness

Two sources are described below. Both satisfy the requirement that the value be unknowable at the time of
the announcement and reproducible from public data afterwards. They differ in their guarantees and in what
they signal, and the trade-off is a governance question rather than a technical one.

**The TSC shall decide, by vote, which source applies — and record that decision in this document — before
the first tie is resolved under these rules.** Deciding once a tie exists would mean choosing a method while
the candidates are already known, which is exactly what the announcement rules are meant to prevent.

Whichever source is chosen, everything in "Announcement", "Rule", "Multiple seats" and "Vacancy during
resolution" applies unchanged.

| | Option A — drand | Option B — Hedera block hash |
| --- | --- | --- |
| Built as a randomness beacon | yes | no; it is a hash over block contents |
| Unpredictability guarantee | threshold BLS; no single operator can bias the value | none in the cryptographic sense; whoever influences which transactions enter a record file can grind the hash at low cost |
| Operated by | League of Entropy (Cloudflare, Protocol Labs, EPFL and others) | Hedera consensus nodes, run by Hedera Council members |
| Conflict of interest | none with respect to this Project | Council members employ people who stand for TSC seats |
| Commitment is to | a round number, known exactly in advance | a point in time; the block number is only known afterwards |
| Uses our own ecosystem | no | yes |

A third possibility is to combine both, so that the result is at least as strong as the better of the two:
as long as either value is unpredictable, the combination is. This keeps the cryptographic guarantee of
drand while drawing on the Project's own network.

```
seed = sha256(drand_randomness_hex + hedera_block_hash_hex_without_0x)
winner_index = int(seed, 16) mod len(candidates)
```

If the TSC chooses this, the announcement names both the drand round and the Hedera timestamp, and the
verification rules of both options apply.

### Option A — drand

[drand](https://drand.love) is a public randomness beacon operated by the League of Entropy. The
[drand public HTTP API](https://docs.drand.love/developer/http-api/) is used to retrieve the random value.
The URL is made up of three parts:

```
https://api.drand.sh/<chain-hash>/public/<round>
                     ^^^^^^^^^^^^        ^^^^^^^
                     network we use      round for the given draw
```

Chain hash `52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971` identifies the drand `quicknet`
network. It is stable and shall be used for all our elections.

`quicknet` produces a new round every 3 seconds since the genesis of the network
(2023-08-23 15:09:27 UTC, or `1692803367` as a Unix timestamp). Both values are published by the network itself:

```bash
curl -s https://api.drand.sh/52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971/info
```

The round covering a given point in time follows from those two values:

```python
round = (target_unix - 1692803367) // 3 + 1
```

The `// 3` divides the elapsed seconds by the period; the `+ 1` accounts for drand numbering its rounds from 1
rather than 0. Converting in either direction:

```bash
# Date → round
python3 -c "
from datetime import datetime, timezone
t = datetime(2026,10,15,16,0,0,tzinfo=timezone.utc).timestamp()
print(int((t - 1692803367)//3 + 1))"

# Round → date
python3 -c "
from datetime import datetime, timezone
print(datetime.fromtimestamp(1692803367 + (33092212-1)*3, timezone.utc))"
```

The random value is the `randomness` field of the API response, a hexadecimal string.

**Multiple seats.** The next seat is drawn from the following round of the same beacon — `round + 1`, then
`round + 2`, and so on.

**Verification.** The result shall be confirmed against at least two independent drand endpoints
(`api.drand.sh`, `api2.drand.sh`, `api3.drand.sh`, `drand.cloudflare.com`). The published `randomness` is the
SHA-256 hash of the round `signature` and can be verified against the drand group public key with a drand
client, which proves the value was produced by the beacon and not by a relay.

### Option B — Hedera block hash

Hedera groups transactions into record files, which are numbered as blocks; each has a SHA-384 hash that is
published through any [mirror node](https://docs.hedera.com/hedera/sdks-and-apis/rest-api/blocks). Because the
block number for a future point in time cannot be known exactly in advance, the announcement commits to a
timestamp instead: **the first block whose consensus timestamp is at or after the announced time.**

```bash
# 2026-10-15T16:00:00Z = 1792080000
curl -s "https://mainnet-public.mirrornode.hedera.com/api/v1/blocks?timestamp=gte:1792080000&order=asc&limit=1"
```

The response contains `number`, `timestamp.from` and `timestamp.to`, `previous_hash` and `hash`. The random
value is `hash` with its `0x` prefix removed — 96 hexadecimal characters.

```bash
curl -s "https://mainnet-public.mirrornode.hedera.com/api/v1/blocks?timestamp=gte:1792080000&order=asc&limit=1" \
  | python3 -c "
import json,sys
b = json.load(sys.stdin)['blocks'][0]
print('block', b['number'], '-> index', int(b['hash'][2:],16) % 3)"
```

The query is deterministic and can be run against any mirror node. The block number in the result makes the
draw unambiguously citable afterwards.

**Multiple seats.** The next seat is drawn from the immediately following block — the one whose `previous_hash`
is the hash just used — so that no further timestamp has to be announced.

**Verification.** The result shall be confirmed against at least two independent mirror nodes. Each returned
block shall be checked to be the earliest one at or after the announced timestamp, and its `previous_hash`
shall match the `hash` of the preceding block.

**Known limitation.** A block hash is a hash over the contents of a record file, not a purpose-built beacon.
A party able to influence which transactions enter a record file — by submitting, withholding or timing them —
can grind the hash at low cost. The announcement rules limit but do not remove this. The TSC accepts this
limitation if it chooses this option.

### Rule

With the candidates numbered from `0` in the published order, and `random_value` the hexadecimal value
obtained from the chosen source:

```
winner_index = int(random_value, 16) mod len(candidates)
```

### Multiple seats

Where more than one seat is to be allocated among the tied candidates, the procedure is repeated. The winner is
removed from the list, the remaining candidates keep their relative order, and the next seat is drawn from the
next value of the same source, as described for that option. All values to be used shall be named in the
announcement.

### Failure

If the announced value cannot be retrieved, or if independent endpoints return different values for it, the
draw is postponed and a new announcement is published under the rules above. The source of randomness shall
not be changed in order to resolve a pending draw.

### Example

A complete announcement for a single seat among three tied candidates, using Option A:

```
Tie between three candidates for one seat. The seat will be allocated by public lot.

Candidates, in fixed order (alphabetical by GitHub login, case-insensitive):
  0 = alice-dev
  1 = bob-ops
  2 = carol-py

Randomness source: drand quicknet
Chain hash: 52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971
Round: 33092212 — 2026-10-15T16:00:00Z
Rule: winner_index = int(randomness, 16) mod 3

Published: 2026-10-08T12:00:00Z

The draw will be recomputed live in the public TSC call on 2026-10-15 at 16:15 UTC.
```

The same announcement using Option B:

```
Randomness source: Hedera mainnet, first block with consensus timestamp >= 1792080000
                   (2026-10-15T16:00:00Z), via any mirror node
Rule: winner_index = int(block hash without 0x, 16) mod 3
```

After the announced time has passed, anyone can reproduce the result:

```bash
# Option A
curl -s https://api.drand.sh/52db9ba70e0cc0f6eaf7803dd07447a1f5477735fd3f661792ba94600c84e971/public/33092212 \
  | python3 -c "import json,sys; print(int(json.load(sys.stdin)['randomness'],16) % 3)"

# Option B
curl -s "https://mainnet-public.mirrornode.hedera.com/api/v1/blocks?timestamp=gte:1792080000&order=asc&limit=1" \
  | python3 -c "import json,sys; print(int(json.load(sys.stdin)['blocks'][0]['hash'][2:],16) % 3)"
```

## Vacancy during resolution

A seat that remains unfilled while a tie is being resolved shall not be counted toward the total number of
TSC Members for the purposes of quorum under 4.b of the charter.
The term of a seat filled under this document runs from the date the tie is resolved.