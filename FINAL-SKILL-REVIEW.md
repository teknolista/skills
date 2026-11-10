# Final skill maintenance review

This record contains successive reviews. Earlier dates, counts and versions describe their original snapshots. See the [final adoption review](#final-adoption-review) for the latest pass; the [README catalog](README.md#available-skills) owns current package versions.

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

The previous [model trial results](evals/RESULTS.md) retain their original snapshots and limitations. The wording changes received source and contract review. Consuming Android builds, browser and assistive sessions, production security checks and the complete MCP client matrix remain project-specific verification.

No substantiated blocker remains in the inspected maintenance scope after these corrections. This supports using the collection with actual project checks; it does not establish exhaustive correctness, universal model efficacy or security certification. Changes remain local, with no commit, push or deployment performed.

## Distribution review

The maintenance snapshot was subsequently published as `bbd941da590e84c4594cd45d49e3aab9fd0d852e`. The [hosted validation run](https://github.com/teknolista/skills/actions/runs/42731202186) passed for that commit. This run is evidence for the published snapshot. The distribution corrections below were checked locally.

The README now uses one version catalog. The README, project template, routing guide and UI evaluation cases describe the same documentation scope and task ownership as the entrypoints. The seven synthetic case definitions still resolve to their intended fixtures and owners. The earlier trial count, routing observations and input-token figures were checked against the retained run summaries. The original trial scope and limitations remain in the [trial record](evals/RESULTS.md).

The local source comparison found matching material in five references embedded in UI Design and Cybersecurity, in addition to the nine standalone imports already recorded. The maintainer subsequently confirmed MIT redistribution permission for all imported material. All 21 packages declare MIT and carry a matching license notice with source attribution. See the [affected paths and provenance](THIRD-PARTY-NOTICES.md#pl-coding-android-and-pr-quiz-skills).

The local review passed collection and skill metadata validation, checked the four UI metadata files, and passed all 64 offline helper tests and the in-process MCP SDK smoke test. The current validator requires MIT metadata and the canonical notice in every package. After the license update, Skills CLI `1.7.6` installed all 21 packages from a local source into a disposable Codex project. Every installed file matched its source bytes, including all 21 license notices.

## Adaptive specification and delivery review

Reviewed on 2026-11-10 against `a910ca37f86ef48b6cb0a09b9569933249534346` and the supplied analyses. The collection already separated requirements, implementation, testing, review and release authority. It already supported persistent specifications, external change records, work without a formal SDD framework and isolated experiments. The gap was how to decide among these modes and how to handle a transition when implementation exposes a consequential ambiguity or an experiment becomes maintained software.

- [Software Delivery 1.2.0](software-delivery/SKILL.md) keeps its dependent-task trigger. Its [change contract guide](software-delivery/references/change-contracts.md) addresses readiness, escalation, experiment adoption, authoritative generation sources and reconciliation of implementation with the agreed contract.
- [PentaPRO 2.7.0](penta-pro/SKILL.md) distinguishes readiness for an increment from a requirement to specify the entire selected scope before coding. The PROCESS template and document maintenance guidance make the handoff reconstructible from the saved artifacts and recognize governed schemas, policies and checks.
- The [README](README.md#choose-a-workflow), [routing guide](SKILL-ROUTING.md#choose-the-depth-of-the-workflow) and [project template](AGENTS-template.md#skill-selection-and-coordination) expose the same decisions for direct edits, exploration and specified work. Existing domain skills continue to own their checks. The [evaluation procedure](SKILL-EVALUATION.md#score-the-outputs) includes cases for the new boundaries.

The review adopted the analyses' separation of agent authority, specification depth and verification. Numeric autonomy levels and a fixed risk score would not establish authority or cover cases where one consequence determines the workflow. Persistent contracts fit maintained behavior. Spec-as-source applies where the project already has a governing input and regeneration process. Automatic pipeline autonomy and universal code generation remain outside the demonstrated scope. [Berkeley position paper and overview](https://rdi.berkeley.edu/blog/auto-software-dev/) · [Böckeler's SDD taxonomy](https://martinfowler.com/articles/exploring-gen-ai/sdd-3-tools.html) · [NCSC guidance on oversight](https://www.ncsc.gov.uk/blogs/the-vibe-coding-spectrum-approach-to-ai-assisted-software-development)

The evidence favors testing specific practices. Practitioner reports describe selective use and additional review costs. The ESEM study analyzed mainly ticket references and did not evaluate adoption of SDD tools. Google's bug-detection gain concerns its contract-guided test generator on the studied tasks. The earlier local token observations compare skill snapshots on matched fixtures, with HTTP API as the localized implementation owner. They do not isolate the effect of adopting SDD. [Practitioner study](https://arxiv.org/abs/2608.25202v4) · [ESEM study](https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.ESEM.2026.84) · [Google test generation study](https://research.google/pubs/grounding-ai-agents-in-contracts-an-empirical-evaluation-of-spec-driven-test-generation/) · [Local trial record](evals/RESULTS.md)

All 21 skill packages passed metadata validation. The collection validator checked local links, catalog versions and standalone notices. All 64 offline helper tests passed. The [adaptive workflow trial record](evals/RESULTS.md#adaptive-workflow-checks-2026-11-10) reports the exercised boundaries and remaining limits separately.

## Collection and installation verification

Reviewed on 2026-11-10 on the working snapshot over `a910ca3`. Read all 21 entrypoints against their intended tasks, routing, authority, and evidence requirements. Traced selected supporting contracts and executable paths, including Android version-sensitive guidance, MCP protocol revision handling, the UI gallery, and PR quiz publication and grading. The README now distinguishes [root maintenance directories](README.md#repository-structure) from packaged resources.

- [UI Design 1.5.7](ui-design/SKILL.md) rejects malformed comment forms that the build-time parser and Chromium can interpret differently. A synthetic fragment passed the old builder and executed its script in Chromium. The new builder rejects that fragment without replacing the previous export. A separate Chromium control confirmed that the generated hash policy blocks the unexpected script while still running the bundled viewer. The regular gallery also opened the requested state, theme and width from a deep link. The helper remains intended for reviewed local inputs.
- [PR Quiz 1.2.3](pr-quiz/SKILL.md) checks the current token and sender eligibility before answer comments can change a status or result comment. The former handler wrote state for some ineligible submissions, including malformed ones. Offline regressions cover authors, outsiders, malformed answers, and missing quiz metadata. PR lifecycle events still report missing or malformed quizzes, and eligible reviewers can still grade the current revision.
- Skills CLI 1.7.6 installed all 21 packages from a disposable copy of the working snapshot using `--copy`. The installed files matched their source bytes, including licenses and nested resources. Root `evals/` and `scripts/` stayed outside the target project.

Collection validation, all skill entrypoint checks, four host metadata checks, nine evaluation case definitions and whitespace validation passed. The 68 offline tests include 3 runner lifecycle tests, 26 UI helper tests, 12 PR publisher tests and 27 grader scenarios. The MCP Python SDK 2.2.0 in-process smoke test passed for the legacy and modern paths in the fixture. The browser and API doubles cover the stated reproductions. Live GitHub workflow execution, consuming Android builds and device tests, production services, and additional model comparisons were outside this pass.

## Final adoption review

Reviewed again on 2026-11-10 against the working collection over `a910ca3`. Read all 21 entrypoints and checked their task boundaries against routing, installation guidance, project instructions and the existing assessment. Supporting procedures and executable paths received targeted inspection, including specification ownership and readiness, Android storage/session boundaries, version-sensitive build/test/DI guidance, MCP revision handling, UI gallery output, PR publication/grading and evaluation-process cleanup. This is a maintainer self-review. It is not an independent approval or an exhaustive audit of every reference and platform combination.

No additional substantiated skill-instruction defect was found in this pass. Preserve the current instructions and versions instead of expanding them without a demonstrated need. The README now supplies a first-task adoption path, describes actual coverage and project-specific verification, and gives the complete offline maintenance commands and prerequisites. Its installation wording now accounts for symbolic links and explicit `--copy`, as documented by the [Skills CLI](https://github.com/vercel-labs/skills/blob/main/docs/commands.md#installation-methods). Root maintenance directories remain outside installed skill packages.

Rechecked primary documentation for the [Agent Skills format](https://agentskills.io/specification), [AGP built-in Kotlin](https://developer.android.com/build/migrate-to-built-in-kotlin), [Koin verification](https://insert-koin.io/docs/reference/koin-test/verify/), [Compose v2 test environments](https://developer.android.com/develop/ui/compose/testing/migrate-v2), and [MCP revision changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog). The inspected guidance still requires matching a consuming project's actual versions. Historical source and evaluation records retain their original evidence; this review does not turn them into new trials.

Fresh local verification passed all 21 skill metadata checks, collection metadata/catalog/license/link validation, and all 68 offline tests (3 evaluator lifecycle, 26 UI helper, 12 PR publisher and 27 grader scenarios). The local runtimes were Python 3.12.6 and Node.js 26.10.0; hosted CI declares Python 3.12 and Node.js 24. The exact reproduction commands are in [README validation](README.md#validation-and-improvement). Whitespace checks passed. The root MIT notice and standalone notices remain aligned, using the maintainer's recorded redistribution authorization.

No blocking finding remains in the inspected collection scope. The collection is usable with the documented prerequisites and project checks. Universal correctness, security certification, effectiveness on every model and readiness of every generated application are not established. This pass did not repeat model comparisons, browser/device sessions, the MCP SDK smoke test, installation trials or hosted CI; their earlier results remain scoped to their recorded snapshots. Publication of the pending changes is a separate step; this pass created no commit or push.
