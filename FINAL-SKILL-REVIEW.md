# Final skill maintenance review

Date: 2026-11-09. Scope: the current working collection of 21 packages, including the preceding maintenance changes on top of `95abba607180cda548749edb76034efe5dbcac32`. This is a maintainer self-review, not an independent approval or a claim of globally optimal skills.

## Assessment

Read every skill entrypoint and traced selected supporting procedures, technical examples, ownership boundaries and evaluation tooling. Checked activation, task scope, SDD and non-SDD contracts, safety, completion evidence and version-sensitive guidance. Supporting materials received targeted inspection; historical source notes, every template field and every platform/library combination were not independently revalidated in this pass.

The collection's division of responsibility is suitable for the stated development workflow. Keep requirements, implementation, tests, independent review, security and publication as distinct outcomes with explicit handoffs. More instructions are useful only when they change a relevant decision; a longer universal checklist would not establish higher quality.

| Package | Disposition and assessed contract |
| --- | --- |
| [PentaPRO](penta-pro/SKILL.md) | Retain. Five pillars, accepted versus proposed changes, stable IDs and external SDD ownership remain coherent. Readiness does not authorize implementation. |
| [Software Delivery](software-delivery/SKILL.md) | Retain. Executes dependent increments using accepted SDD records or ordinary contracts; verifies integrated results and preserves unfinished gates. |
| [Technical Research](technical-research/SKILL.md) | Retain. Primary evidence, version applicability, bounded experiments and honest uncertainty; no automatic production promotion. |
| [Diagnose Defect](diagnose-defect/SKILL.md) | Retain. Reproduction, working control, distinguishing hypotheses and scoped remediation; no unsupported cause claim. |
| [Behavior Testing](behavior-testing/SKILL.md) | Retain. Independent expectations, meaningful red phase when applicable, runtime-specific boundaries and test-only scope. |
| [HTTP API](http-api/SKILL.md) | Clarify outbound security. Preserve compatibility, authorization, durable effect/retry semantics and supported consumer behavior. |
| [MCP Server](mcp-server/SKILL.md) | Retain. Separate protocol revision from SDK support, legacy/modern lifecycle, server enforcement and application idempotency. |
| [Peer Review](peer-review/SKILL.md) | Retain. Source-backed findings, counterevidence, snapshot freshness and distinct verification/independence claims. |
| [Cybersecurity](cybersec/SKILL.md) | Retain. Threat-to-control evidence, actual effect boundaries, allowed/denied controls, residual risk and authorization. |
| [UI Design](ui-design/SKILL.md) | Correct documentation scope. Preserve platform-aware interaction/accessibility checks and distinguish specifications, concepts and runtime evidence. |
| [Git Delivery](git-delivery/SKILL.md) | Retain. Reviewed snapshot, unrelated index preservation, explicit destinations and remote confirmation; no implicit merge/deploy. |
| [Agent Instructions](agent-instructions/SKILL.md) | Strengthen evaluation integrity. Small useful owners, conditional references, verified isolation and honest comparison limits. |
| [Android Module Structure](android-module-structure/SKILL.md) | Retain. Actual AGP/Kotlin mode, compatible conventions, explicit dependencies and release evidence. |
| [Android Data Layer](android-data-layer/SKILL.md) | Retain. Atomic storage, migration and query semantics, account boundaries and uncertain remote outcomes. |
| [Android Error Handling](android-error-handling/SKILL.md) | Retain. Typed expected failures, cancellation propagation, transport-specific mapping and visible programming defects. |
| [Android DI Koin](android-di-koin/SKILL.md) | Retain. Actual API version, owner/lifetime, parameterized resolution and graph-check limits. |
| [Android Background](android-background/SKILL.md) | Retain. Persistent work, bounded retries, stable operation identity, cancellation limits and account-switch enforcement. |
| [Android Unit Testing](android-unit-testing/SKILL.md) | Retain. Shared scheduler, controlled suspension, meaningful assertions and correct restoration limits. |
| [Android Integration Testing](android-integration-testing/SKILL.md) | Retain. Real storage/transport boundaries, historical migrations, negative-test reachability and legitimate controls. |
| [Android UI Testing](android-ui-testing/SKILL.md) | Retain. Installed test APIs, real input, synchronization and device/assistive evidence limits. |
| [PR Quiz](pr-quiz/SKILL.md) | Retain. Explicit educational scope, publication authority and revision-bound informational results; no security/review approval claim. |

## Corrections and evidence

1. **UI scope contradiction, corrected.** The document-maintenance reference said an invocation normally creates a document, while the entrypoint made documentation conditional. A localized UI implementation could therefore acquire an unnecessary specification deliverable. The reference and description now distinguish specification work from localized implementation and read-only review. Existing authoritative contracts still receive scoped updates when affected. Version: `1.5.6`.
2. **Outbound HTTP boundary, clarified.** Added conditional destination/credential enforcement for caller-controlled URLs and redirect hops, bounded response processing and allowed/denied endpoint checks. This puts a relevant implementation constraint in the API owner without requiring a full security audit for ordinary endpoint work. Basis: [OWASP SSRF prevention](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html). Version: `1.1.1`. No live integration or new model-comparison gain is claimed.
3. **Evaluation isolation claims, qualified.** Evaluator files outside a task workspace may remain readable; directory separation is not confidentiality. The portable evaluation procedure now requires checking that boundary or disclosing it. Local trial documentation explicitly records that read isolation was not established. Prior measured results remain unchanged and exploratory. Agent Instructions version: `1.0.1`.
4. **Evaluation process lifetime, fixed.** A synthetic child wrote after `subprocess.run(timeout=...)` had terminated its parent. The runner now starts a POSIX process group and kills that group on timeout or an exception while waiting. A regression test confirms the child started and cannot perform the later write. The same test failed on the former behavior; success and nonzero-exit controls passed. The CI workflow includes these offline tests. Basis: [Python subprocess semantics](https://docs.python.org/3/library/subprocess.html). Process groups are cleanup, not a security sandbox for deliberately detached processes or external effects.

Current official documentation was also consulted for [AGP built-in Kotlin](https://developer.android.com/build/migrate-to-built-in-kotlin), [Koin verification](https://insert-koin.io/docs/reference/koin-test/verify/), [Compose v2 testing](https://developer.android.com/develop/ui/compose/testing/migrate-v2), and [MCP revision changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog). No conflicting rule requiring another change was established in those inspected paths. Consuming projects must still resolve their actual versions.

## Validation and limits

- All 21 packages passed the installed skill-creator `quick_validate.py`.
- Collection metadata, catalog versions and local links/anchors passed `scripts/validate_collection.py`.
- 64 offline checks passed: 3 evaluator lifecycle tests, 24 UI helper tests, 12 PR publisher tests and 25 Node grader scenarios.
- The lifecycle negative control failed for the intended late-write assertion under the old implementation, and passed with the correction.
- Whitespace validation passed. The CI workflow was parsed locally; hosted execution remains pending publication.

The previous [model trial results](evals/RESULTS.md) retain their original snapshots and limitations; the latest wording changes have source/contract review, not a new matched model trial. This pass did not execute consuming Android builds, browser/assistive sessions, production security checks or the complete MCP client matrix. Those remain project-specific evidence, not defects to hide with broader prose. Source-derived package license omissions remain as documented in [third-party notices](THIRD-PARTY-NOTICES.md).

No substantiated blocker remains in the inspected maintenance scope after these corrections. This supports using the collection with actual project checks; it does not establish exhaustive correctness, universal model efficacy or security certification. Changes remain local, with no commit, push or deployment performed.
