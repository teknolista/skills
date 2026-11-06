# Skill ownership and Android integration

Choose the primary owner from the requested outcome and mode, not from an Android keyword alone. Load relevant platform references inside that owner. Use an implementation/test helper only for its narrower task; do not run two interviews, create competing canonical documents or report two verdicts for the same assessment. A request may contain several different tasks, each with its own owner and existing authorization.

Ordinary backend, CLI or other implementation can proceed under the project's instructions without invoking a skill from this collection. The four generic owners do not form a mandatory pipeline. A security defect found during peer review can be reported there; it does not automatically start a second audit. An implementation helper must apply relevant security controls without requiring a full security assessment for every edit.

## Generic owners

| Requested result | Primary owner | Boundary |
| --- | --- | --- |
| Requirements, architecture proposal, verification plan or readiness specification | [PentaPRO](penta-pro/SKILL.md) | Five pillars; ordinary coding does not start a new interview |
| Screen/flow/visual/accessibility design or critique; authorized UI implementation | [UI Design](ui-design/SKILL.md) | One cumulative UI contract, native Android procedures loaded conditionally |
| Read-only source/PR/test-effectiveness assessment or re-review | [Peer Review](peer-review/SKILL.md) | Evidence-backed findings; test-authoring is a different implementation task |
| Threat modeling, security audit, authorized hardening or security gate | [Cybersecurity](cybersec/SKILL.md) | One threat/control/evidence record, native Android controls loaded conditionally |

## Every source skill and its destination

Source inventory: the 14 entrypoints in the user-supplied local `android-skills` directory on 2026-11-06. The earlier `design` consolidation remains recorded in UI Design; it is absent from this source inventory. Integration copies the source; it does not delete or install anything in that directory or a user's agent profile.

| Source | Destination | Decision / requested result |
| --- | --- | --- |
| `android-compose-architecture` | [UI Design / Compose architecture](ui-design/references/android/compose-architecture.md) | Consolidated: screen structure, state, performance and input implementation already fall within UI Design |
| `android-compose-components` | [UI Design / components](ui-design/references/android/compose-components.md) | Consolidated: component design/implementation, resources and semantics |
| `android-presentation-mvi` | [UI Design / presentation](ui-design/references/android/presentation-mvi.md) | Consolidated: native screen integration; MVI remains a conditional project choice |
| `android-navigation` | [UI Design / navigation](ui-design/references/android/navigation.md) | Consolidated: flows and native screen/navigation implementation |
| `android-security` | [Cybersecurity / Android controls](cybersec/references/android-controls.md) | Consolidated: security assessment/hardening already has a generic owner |
| `android-module-structure` | [Native module implementation](android-module-structure/SKILL.md) | Retained: concrete Gradle/module changes, not PentaPRO architecture discovery/specification |
| `android-data-layer` | [Native data implementation](android-data-layer/SKILL.md) | Retained: repository, network, database and synchronization code |
| `android-error-handling` | [Native typed errors](android-error-handling/SKILL.md) | Retained: typed-result/transport/storage implementation; UX feedback design stays in UI Design |
| `android-di-koin` | [Native Koin wiring](android-di-koin/SKILL.md) | Retained: dependency graph/lifetime implementation, not screen design or independent assessment |
| `android-background` | [Native background work](android-background/SKILL.md) | Retained: durable job implementation/debugging, not product planning or security audit |
| `android-unit-testing` | [Unit-test authoring](android-unit-testing/SKILL.md) | Retained: write/run/debug isolated tests; effectiveness review stays in Peer Review |
| `android-integration-testing` | [Integration-test authoring](android-integration-testing/SKILL.md) | Retained: write/run/debug non-UI boundary tests |
| `android-ui-testing` | [Native UI-test authoring](android-ui-testing/SKILL.md) | Retained: automate device/emulator tests; visual/interaction critique stays in UI Design |
| `pr-quiz` | [PR decision quiz](pr-quiz/SKILL.md) | Retained, generic: explicitly requested comprehension exercise, not review approval/security evidence |

There are **13 discoverable skills**: four generic owners, eight native Android implementation/test helpers and the generic PR quiz. The five consolidated Android names are not separate SKILL.md entrypoints or forwarding aliases, preventing duplicate discovery. Their material remains in conditional references, with local links redirected to the canonical owner.

## Boundaries in common requests

- “Review this Android PR and its tests” → Peer Review with Android/test references. Do not activate a test-writing workflow or modify source from that review request.
- “Implement retry on this Compose screen” → UI Design with its Android presentation/component procedures; use data/background helpers only for actual subordinate code changes.
- “Write a Room migration test” → Android integration testing. “Are these migration tests meaningful?” → Peer Review.
- “Audit login/deep links/WebView” → Cybersecurity with Android controls, not an additional Android security audit.
- “Plan an Android architecture” → PentaPRO. “Add this approved Gradle module” → Android module structure.
- “Create a PR” alone → no quiz. “Add a comprehension quiz to this PR” → PR Quiz. Drafting, publishing, workflow installation and branch-rule changes retain their distinct authorization scopes.

Cross-package links are optional navigation within this collection. A separately installed helper uses its own core instructions and project-owned contracts; it must not claim to have loaded an absent companion. Install related packages when desired, and preserve each package's internal references. Generic owners do not require the Android helper packages for non-Android work.

## Carry context between tasks

For a material handoff, carry the requested outcome/mode and existing authority, target repository and snapshot/variant, canonical requirement/contract IDs, decisions versus proposals, changed files, actual checks and remaining gaps. Reopen the affected source if it changed. Keep this in the existing task record or conversation; no new handoff document is required.

For example, “implement retry, then review the change” has an implementation step followed by read-only review of the resulting snapshot. Reuse the screen/data contract; do not restart a product interview. A review finding does not itself authorize unrelated fixes. If the same issue appears in a security and code review, reference the shared root cause and reconcile evidence instead of counting it as two defects or averaging verdicts. Distinct requested assessments may retain their own scoped conclusions.

When contracts disagree, identify the actual conflicting records and status/authority. A mock, test, later file timestamp or confident model statement cannot silently overrule an accepted requirement. Settle routine delegated implementation choices directly; leave only work depending on an unresolved consequential decision pending. Preserve earlier evidence with its tested revision rather than relabeling it as evidence for the new one.

## Validation scope

Inspect descriptions and entrypoint boundaries against the cases above whenever adding a skill. Structural checks can establish unique names, linked resources and absence of retired entrypoints, but cannot guarantee identical automatic routing across models/hosts. Run representative tasks on the actual intended host/model before claiming reliable activation or comparative quality. The PR quiz helper/workflow has offline behavioral tests; its template is not installed as an active repository workflow by this integration.

Executed integration checks on 2026-11-06: all 13 discoverable packages passed skill-creator validation; local Markdown links/anchors, retired-name absence and README versions were checked. The existing UI prototype helper retained its 20 passing regression tests. The PR publisher passed 8 local regressions, and its actual embedded workflow script passed 9 offline GitHub-API-double scenarios (valid/wrong/duplicate answers, author/outsider rejection, stale/current commit passes and malformed/missing metadata). These are not live GitHub permission, merge-rule or fork-workflow tests. No cross-model activation benchmark or consuming Android app build was executed for this integration.

### Final collection review — 2026-11-06

Reviewed the 13 entrypoints, their ownership contracts, relevant runtime references/examples, output templates, metadata and executable helpers. All entrypoints now preserve canonical contracts and scoped handoff evidence; examples cannot mandate a stack migration. Existing generic platform coverage is retained, while native helpers introduce no KMP targets or workflow. Ordinary implementation and narrow assessments do not trigger a mandatory pipeline.

Concrete corrections: Koin runtime WorkerParameters versus container dependencies; stopped versus cancelled work and future periodic runs; account-partitioned commits versus a stale pre-write session check; pure StateFlow update transformations; built-in Kotlin migration/default targets; version-supported Compose test input configuration; and negative fixtures that actually reach authorization/TLS enforcement. Their primary sources are linked at the relevant procedure.

The PR workflow had a reproduced reflection bug: an editable explanation could insert a pass marker into the bot's failure report, and the earlier substring cache would accept it later. A regression failed before correction. Explanations now render as literal text and only a structured result prefix can supply a cached pass. Ambiguous quiz blocks/keys are rejected, author exclusion is explicit, questions cannot introduce active Markdown/mentions, and the optional action uses an official full-commit pin and narrower token permissions. This does not turn an editable educational quiz into a trusted approval gate.

Executed checks for the resulting collection:

- All **13** packages passed `skill-creator/scripts/quick_validate.py`; names, README versions, UI metadata, consolidated-entrypoint absence and inactive workflow placement were checked.
- **77 Markdown files / 498 local links and anchors** passed the local resource check. The 21 files in the original local import source retained their recorded hashes.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s ui-design/scripts/tests -v`: **20 passed**.
- `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pr-quiz/scripts/tests -v`: **9 passed**.
- `node pr-quiz/scripts/tests/workflow.cjs`: **19 passed**, executing the actual embedded handler with offline API doubles on local Node 26.10.0. Includes checkbox-event freshness, structured/stale pass caches, author/reviewer eligibility and explanation reflection; no GitHub calls.
- Re-extracted the current typed-result, repository and Notes fake snippets and compiled them with the installed Kotlin compiler and real coroutine library: **7 behavioral groups plus 4 concurrency/fake conditions passed**. This verifies host orchestration, not AndroidX/Ktor imports, database transactions or TLS behavior.
- `git diff --check` and a separate whitespace/final-newline check of untracked text files passed; dedicated README sections and the versioned PentaPRO output template match the current entrypoints.

This was a maintainer review with local regression checks, not a new independent cross-model evaluation. No consuming application, device/assistive-technology session, deployed backend or live GitHub workflow/merge-rule test was run. The pinned action's actual hosted runtime/permissions still need validation when adopted. Existing browser/model trials retain their original scope and are not relabeled as fresh evidence for this review. No claim of exhaustive correctness, certification or identical routing on smaller models follows from these results.
