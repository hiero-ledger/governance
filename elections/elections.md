# Elections to the Technical Steering Committee

As set forth in the [Hiero Technical Charter](/Hiero%20Technical%20Charter%20Final%209-16-2024.md) in section 3.9.3.2,
this document sets forth the process and timeline for the nominations, qualification, and election of TSC members.

## Seats

The TSC is composed of 9 seats (see section 3.8 of the charter):

- The Leemon Baird seat. This seat is filled by Leemon Baird and is not open for election.
- The Hedera seat. This seat is filled by a delegate selected by Hedera for the first 3 years of the Hiero project.
- Three Maintainer seats. These seats are filled by candidates elected by the maintainers of the Hiero projects.
- One Contributor seat. This seat is filled by a candidate elected by the contributors to the Hiero projects.
- One End User seat. This seat is filled by a candidate elected by "end user developers", which are defined in this
  document.
- Two TSC seats. These seats are filled by candidates elected by the other members of the TSC. After the initial 3-year
  period, this is expanded to 3 seats.

### Leemon Baird Seat

The Leemon Baird seat is held by Leemon Baird himself and is not open for election.

### Hedera Seat

Hedera may select a delegate to represent them on the TSC as they choose. This seat is not open for election until
September 1st, 2027.

### Maintainer Seats

The list of maintainers qualified to vote will be drawn from the maintainers of Hiero GitHub projects, as defined in
the [Governance config.yaml](/config.yaml) file. Only maintainers of "Graduated" projects may vote (the charter is
ambiguous on this point: section 3.8.3 does not mention "graduated" while 3.8.7 does). Each maintainer will be able to
vote once for each available seat with no more than one vote supporting any one candidate.

### Contributor Seat

The list of contributors qualified to vote shall be defined as any individual, identified by their GitHub credentials,
who has created a PR that was subsequently merged into any project (graduated or otherwise) within Hiero within the
calendar year preceding the beginning of the election period, or who held a role within any project within Hiero such as
maintainer or member as defined in the [Governance config.yaml](/config.yaml) file.

### End User Seat

To become eligible to vote in this election, electors shall create a PR modifying
the [end-user-electors.md](/elections/end-user-electors.md) file. The PR shall be reviewed and approved by at least 2
members of the TSC or authorized reviewers selected by the TSC. If a dispute arises regarding the legitimacy of any
elector, any TSC member may call for a vote by the full TSC on the validity of any elector of the End User Seat.

### TSC Seats

Following the election of Maintainer, Contributor, and End User seats, the TSC itself shall elect the remaining TSC
seats.

## Election Periods and Terms

As defined in section 3.9.4 of the charter, TSC members shall fill two-year terms. To help provide continuity on the
TSC, the seats on the TSC shall be divided into two cohorts, with one cohort being elected each year. During the
"startup period" of the Hiero project, only 7 seats are electable (neither the Leemon Baird seat nor the Hedera seat are
electable). Cohort A shall be comprised of 1 Maintainer seat, 1 Contributor seat, and 1 TSC seat. Cohort B shall be
comprised of 2 Maintainer seats, 1 End User seat, and 1 TSC seat. After the startup period when the Hedera seat reverts
to a TSC seat, that seat shall be part of Cohort A.

The initial term for Cohort A shall be measured from September 1st, 2023, and shall therefore be re-elected on September
1st, 2025 and every two years thereafter. The initial term for Cohort B shall be measured from September 1st, 2024, and
shall therefore be re-elected on September 1st, 2026 and every two years thereafter.

As of January 2025, not all seats on Hiero were filled during the initial setup of the project. A special election shall
be opened on March 18th, 2025 and closed by March 31st, 2025 to fill the remaining seats. Nominations shall be open from
February 10th, 2025 until March 10th, 2025. 

## Nominations

All candidates must be nominated. They may be nominated by themselves or another party, but must agree to the
nomination. Each nomination shall be submitted as a PR to the appropriate election folder beneath /elections/nominees.
Each nominee must submit a markdown file formatted as [sample-nomination.md](/elections/nominees/mar-2025-election/sample-nomination.md).

## Voting Procedure

The specific voting procedure for each election shall be defined in the README.md file in the appropriate election
folder.
