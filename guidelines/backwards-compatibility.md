# Backwards Compatibility Guideline

This document provides information about the handling of backward compatibility within projects at Hiero.

The content of this document is based on an independent third party researched how other leading blockchain networks
manage breaking changes and backwards compatibility.
The independent 3rd party concluded the following:

* None of the leading blockchain or DLT networks have a definitive public policy with
  respect to breaking changes and backwards compatibility.
* None have stated that breaking changes cannot happen. All networks
  communicate an intent to prioritize backwards compatibility and propose that
  major changes and deprecations will be communicated clearly and in advance.

In summary, all examined networks:

* Strive to balance technological advancement with maintaining stability and minimizing disruption to existing
  applications and services.
* Employ various communication channels, including release notes, blog posts, and developer forums, to inform
  stakeholders of changes.
* Utilize governance mechanisms involving validators and/or token holders to approve major protocol changes.
* Provide migration guides and support during significant updates or SDK deprecations to facilitate smooth transitions
  for developers.

Hiero intends to follow the same principles as described in more detail in this document.

## Backwards compatibility and breaking changes

The development of software involves ongoing agility and the need to adapt to changing technologies and evolving user
demands.
The adoption of new features and improved capabilities often leads to critical decisions including how to maximize the
opportunities offered by these changes against potential user impact.

As much as is possible, Hiero projects are committed to maintaining backwards compatibility to ensure a reliable
experience for users and developers.
Below is an outline of the approach towards backwards compatibility, the process for introducing breaking changes when
necessary, and the communication and deprecation timelines required to maintain transparency and stability within the
Hiero ecosystem.

Hiero encompasses a large number of projects at different stages of development, the principles outlined below may not
immediately apply to every Hiero project, but will apply to the following projects:

* Hiero Consensus Node
* Hiero Block Node
* Hiero JSON RPC Relay
* Hiero Mirror Node
* Most Hiero SDKs (Go, JavaScript, Rust, Java, CPP, Swift)

Other Hiero projects may choose how to handle backwards compatibility as their maturity increases.
The best practice here is to provide information about backwards compatibility at least when the project has a semantic
version number of 1.X or bigger.

### Ensuring Backwards Compatibility

* All changes must be evaluated for their impact on existing / known users and applications.
* Deprecation of features must be accompanied by clear documentation and migration paths.
* Consider every public API as potentially accessible to any community member.
* Feature enhancements and bug fixes other than those that address critical defects or security vulnerabilities should
  be implemented in a way that does not break existing functionality.
  For example and not limited to:
    * Adding new methods when a return type must be changed
    * Adding parameters to methods with default values is acceptable if behaviour isn’t changed when parameters aren’t
    supplied
* APIs and data structures should follow versioning best practices to avoid disruption, for example:
    * Changes to return data structures should be additive, not subtractive
    * New API parameters should be defaulted without changes to behaviour if not provided
* Changes to response codes (in remote connections) are considered breaking changes

## Breaking Changes Process

The process below will be followed when a breaking change is planned, except in exceptional circumstances such as issues
affecting the security of the network.

Security is the number one concern for public ledgers, a critical security fix necessitating a breaking change may
result in compressed or immediate deprecation timelines and may require more restrictive communications of the issue and
related remediation in order to avoid exploitation of the security concern prior to the deployment of the fix.

### Proposal and Review

A detailed proposal outlining the breaking change must be submitted for review by internal stakeholders and technical 
leads.
The proposal must include justification, potential impact, short and medium term workarounds, and alternatives 
considered.
Open source maintainer stakeholders and technical leads must review, provide feedback and approve the proposal.

### Hiero Technical Steering Committee (TSC) Approval

* A formal meeting with the Hiero Technical Steering Committee (TSC) must be scheduled.
* The TSC will review the proposed breaking change and assess its necessity and impact.
* Approval from the TSC is required before proceeding with the implementation.

### Deprecation and Communication Plan

* A structured deprecation plan must be established, adhering to best practices.
* The deprecation timeline should provide users with adequate time to migrate.
* Clear documentation, including migration guides and upgrade instructions, must be published.
* Communication should include:
    * Deprecation or Breaking Changes announced in `README.md` at the root of each project.
    * Deprecated API should be annotated / tagged / labeled in code if the programming language allows to do so.
    * Deprecated API should contain code documentation with a clear alternative / favored public API
    * Updates in release notes.
    * Announcements in official Hiero community channels.
    * Notifications in relevant technical documentation.

### Implementation and Monitoring

* The breaking change should be implemented with feature flags, if possible, to allow gradual adoption.
* While making the decisions, the TSC should look at adoption rates and identify potential issues, if applicable to the
  project.
* Feedback from the community should be actively collected and addressed.

### Hiero SDKs

Hiero SDKs will adhere to Semantic Versioning ([https://semver.org](https://semver.org/)) whereby an SDK version is 
identified as `MAJOR.MINOR.PATCH`.

* `MAJOR` version is incremented when an incompatible API change is made, subject to deprecation timelines.
* `MINOR` version is incremented when functionality is added in a backward compatible manner.
* `PATCH` version is incremented for backward compatible bug fixes.

Additional labels for pre-release and build metadata are available as extensions to the `MAJOR.MINOR.PATCH` format.
For example, a convention is prefixing with `v` like `v1.0.0`.

Upgrades to a `MINOR` or `PATCH` version should be seamless for application developers.

Upgrades to a `MAJOR` version may entail some rework by application developers.

In the event of a `MAJOR` version update of the SDKs
* the previous version will benefit from functionality enhancements for a minimum period of 6 months.
* the previous version will be maintained for major bugs and critical security fixes for a minimum period of 1 year.

### Deprecation Timelines

* **Initial Announcement:** At least 3 months before enforcement, announce the deprecation and provide migration
  guidelines.
* **Active Support:** Continue supporting the deprecated feature for at least 6 months while encouraging migration.
  A longer period may be considered depending on the severity of the deprecation.
* **Final Removal:** The feature is removed only after the communicated timeline has elapsed and sufficient migration
  support has been provided.

## Exceptions

#### EVM

Hiero inherits its EVM from the Ethereum community.
Should a breaking change be included in a particular release of the EVM, this breaking change will most likely carry
over to Hiero.

#### Emergency/Security issues

If a defect is found on the network that puts either the network or the users' security at risk, then in that unlikely
scenario, Hiero will upgrade the network with the fix as soon as practical.
These scenarios are expected to be very rare.

#### Other

Hiero depends on 3rd party dependencies (e.g. post quantum cryptography).
It is not possible to foresee whether changes imposed on Hiero by 3rd parties would affect backwards compatibility. 
