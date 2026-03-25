# Artifact Namespace Guidelines

Hiero defines namespace conventions for publishing artifacts to ensure consistency across projects and to prevent conflicts where multiple projects attempt to publish to the same namespace.
This document provides an overview of the namespace rules that all Hiero projects must follow.

To describe namespaces in a language-independent way, we use the [Package URL (purl) specification](https://github.com/package-url/purl-spec).
A purl follows the format `pkg:type/namespace/name@version` and allows us to reference packages and namespaces across different ecosystems in a standardized manner.

## General Namespace Rules

- All Hiero projects must publish artifacts under a Hiero-owned namespace as listed in the [Reserved Namespaces](#reserved-namespaces) section below.
- Artifact names should always be prefixed with `hiero-` to clearly identify them as part of the Hiero ecosystem.
- Projects may create sub-namespaces (e.g., `org.hiero.did` for DID-related artifacts), but the top-level namespace must always be a reserved Hiero namespace.
- No two projects should publish artifacts to the same namespace. If a namespace conflict arises, coordinate with the TSC to resolve it.

## Reserved Namespaces

The following table lists all namespaces reserved by Hiero, expressed as [purl](https://github.com/package-url/purl-spec) strings.
Since we are reserving namespaces (not individual packages), the `name` and `version` components are omitted.
Some ecosystems (like Cargo/crates.io) do not support namespaces natively.
In those cases, the namespace is enforced by naming convention only (i.e., all artifact names must start with `hiero-`).

| purl | Ecosystem | Description |
| :--- | :--- | :--- |
| `pkg:maven/org.hiero` | Java / Maven | Primary namespace for all Java artifacts |
| `pkg:npm/%40hiero-ledger` | JavaScript / npm | Primary namespace for all npm packages (`@hiero-ledger` scope) |
| `pkg:npm/%40hiero-did-sdk` | JavaScript / npm | Namespace for DID-related npm packages (`@hiero-did-sdk` scope) |
| `pkg:golang/github.com/hiero-ledger` | Go | Primary namespace for all Go modules |
| `pkg:swift/github.com/hiero-ledger` | Swift / SwiftPM | Primary namespace for all Swift packages |

Ecosystems without native namespace support:

| Ecosystem | Naming Convention | Example |
| :--- | :--- | :--- |
| Rust / Cargo | All crates must use the `hiero-` prefix | `hiero-sdk` |
| Python / PyPI | All packages must use the `hiero-` prefix | `hiero-sdk-python` |

## Example

Using the purl format, a concrete Java artifact would be expressed as:

```
pkg:maven/org.hiero/hiero-sdk@1.0.0
```

This translates to the following Maven coordinates:

```xml
<groupId>org.hiero</groupId>
<artifactId>hiero-sdk</artifactId>
<version>1.0.0</version>
```

In this example:

- `maven` is the purl type identifying the ecosystem.
- `org.hiero` is the reserved namespace.
- `hiero-sdk` is the artifact name, prefixed with `hiero-` as required.
- `1.0.0` is the version.

## Sub-Namespaces

Projects that cover a specific domain may use a sub-namespace to organize their artifacts.
For example, all DID-related artifacts could be published under `org.hiero.did` (purl: `pkg:maven/org.hiero.did`).
Sub-namespaces must always remain under a reserved Hiero namespace.

## Published Artifacts

The following tables list all artifacts currently published by Hiero projects or reserved for near-future publication, expressed as [purl](https://github.com/package-url/purl-spec) strings.

### npm (`@hiero-ledger`)

| purl | Repository |
| :--- | :--- |
| `pkg:npm/%40hiero-ledger/sdk` | [hiero-sdk-js](https://github.com/hiero-ledger/hiero-sdk-js) |
| `pkg:npm/%40hiero-ledger/hiero-cli` | [hiero-cli](https://github.com/hiero-ledger/hiero-cli) |
| `pkg:npm/%40hiero-ledger/hiero-contracts` | [hiero-contracts](https://github.com/hiero-ledger/hiero-contracts) |
| `pkg:npm/%40hiero-ledger/cryptography` | [hiero-sdk-js](https://github.com/hiero-ledger/hiero-sdk-js) |
| `pkg:npm/%40hiero-ledger/proto` | [hiero-sdk-js](https://github.com/hiero-ledger/hiero-sdk-js) |
| `pkg:npm/%40hiero-ledger/solo` | [solo](https://github.com/hiero-ledger/solo) |

### npm (`@hiero-did-sdk`)

| purl | Repository |
| :--- | :--- |
| `pkg:npm/%40hiero-did-sdk/crypto` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/core` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/cache` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/client` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/messages` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/zstd` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/verifier-internal` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/resolver` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/lifecycle` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/signer-internal` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/publisher-internal` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/anoncreds` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |
| `pkg:npm/%40hiero-did-sdk/hcs` | [hiero-did-sdk-js](https://github.com/hiero-ledger/hiero-did-sdk-js) |

### Rust / Cargo

| purl | Repository |
| :--- | :--- |
| `pkg:cargo/hiero-sdk` | [hiero-sdk-rust](https://github.com/hiero-ledger/hiero-sdk-rust) |
| `pkg:cargo/hiero-sdk-proto` | [hiero-sdk-rust](https://github.com/hiero-ledger/hiero-sdk-rust) |

### Python / PyPI

| purl | Repository |
| :--- | :--- |
| `pkg:pypi/hiero-sdk-python` | [hiero-sdk-python](https://github.com/hiero-ledger/hiero-sdk-python) |
| `pkg:pypi/hiero-did-sdk-python` | [hiero-did-sdk-python](https://github.com/hiero-ledger/hiero-did-sdk-python) |

### Java / Maven

| purl | Repository |
| :--- | :--- |
| `pkg:maven/org.hiero/hiero-enterprise-java` | [hiero-enterprise-java](https://github.com/hiero-ledger/hiero-enterprise-java) |
