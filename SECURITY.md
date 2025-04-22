# Hiero, an LF Decentralized Trust Project Security Policy

## About this document

This document defines how security vulnerability reporting is handled in Hiero, an LF Decentralized Trust Project. The approach aligns with the [LF Decentralized Trust Security Policy](https://lf-decentralized-trust.github.io/governance/governing-documents/SECURITY-POLICY). Please review that document to understand the basis of the security reporting for Hiero.

This vulnerability policy borrows heavily from the recommendations of the OpenSSF Vulnerability Disclosure working group. For up-to-date information on the latest recommendations related to vulnerability disclosures, please visit the [GitHub of that working group](https://github.com/ossf).

If you are already familiar with the security policies of Hiero, and ready to report a vulnerability, please jump to [Report Intakes](#report-intakes).

## Outline

This document has the following sections:

- [About this document](#about-this-document)
- [Outline](#outline)
- [What Is a Vulnerability Disclosure Policy?](#what-is-a-vulnerability-disclosure-policy)
- [Security Team](#security-team)
- [Report Intakes](#report-intakes)
- [Embargo List](#embargo-list)
- [GitHub Security Advisories](#github-security-advisories)
- [Private Patch Deployment Infrastructure](#private-patch-deployment-infrastructure)

## What Is a Vulnerability Disclosure Policy?

No piece of software is perfect. All software (at least, all software of a certain size and complexity) has bugs. In open source development, members of the community or the public find bugs and report them to the project. A vulnerability disclosure policy explains how this process functions from the perspective of the project.

This vulnerability disclosure policy explains the rules and guidelines for Hiero. It is intended to act as both a reference for outsiders–including both bug reporters and those looking for information on the project’s security practices–as well as a set of rules that maintainers and contributors have agreed to follow.

## Security Team

The current Hiero security team is:

| Name                     | Email ID               | Discord ID | Area/Specialty            |
|--------------------------|------------------------|------------|---------------------------|
| Hart Mongomery (LFDT)    | <>                     | <>         | Temp Security Advisor     |
| Jessica Gonzalez (LFDT)  | <>                     | <>         | Community Architect       |
| Alex Popowycz            | <>                     | <>         | Security Advisor          |
| Roger Barker             | <>                     | <>         | Project Maintainer        |
| Richard Bair             | <>                     | <>         | Project Maintainer        |
| Nathan Klick             | <>                     | <>         | Security Advisor          |

The security team for Hiero must include at least three project Maintainers that agree to carry out the following duties and responsibilities. Members are added and removed from the team via approved Pull Requests to this repository. For additional background into the role of the security team, see the [People Infrastructure](https://lf-decentralized-trust.github.io/governance/governing-documents/SECURITY-POLICY#people-infrastructure) section of the LF Decentralized Trust Security Policy.

## Report Intakes

We're very thankful for security researchers and users who report vulnerabilities to the Hedera community. For information on our bug bounty process or to make a
report please visit our [Hedera bug bounty program](https://hedera.com/bounty).

## Embargo List

Hiero maintains a private embargo list. If you wish to be added to the embargo list, please email the LF Decentralized Trust Foundation security mailing list, including the project name (Hiero) and reason for being added to the embargo list. Requests will be assessed by the Hiero security team in conjunction with the appropriate LF Decentralized Trust Staff, and a decision will be made to accommodate or not the request.

For more information about the embargo list, please see the Embargo List section of the LF Decentralized Trust Security Policy.

## GitHub Security Advisories

Hiero uses GitHub Security Advisories to manage the public disclosure of security vulnerabilities.

## Private Patch Deployment Infrastructure

In creating patches and new releases that address security vulnerabilities, Hiero uses the private development features of GitHub for security vulnerabilities. GitHub has extensive documentation about these features.

