# Skill ownership and integration

Choose the primary owner from the requested outcome and mode, not from an Android keyword alone. Load relevant platform references inside that owner. Use an implementation/test helper only for its narrower task; do not run two interviews, create competing canonical documents or report two verdicts for the same assessment. A request may contain several different tasks, each with its own owner and existing authorization.

Ordinary backend, CLI or other implementation can proceed under the project's instructions without invoking a skill from this collection. The owners compose according to the requested work and the project’s established workflow. A security defect found during peer review can be reported there; it does not automatically start a second audit. An implementation helper must apply relevant security controls without requiring a full security assessment for every edit.

## Choose the depth of the workflow

Select the owner by outcome. Select the specification depth, agent authority and verification separately. The [change contract guide](software-delivery/references/change-contracts.md) defines when to proceed directly, explore in isolation, or establish a material change contract before implementation.

| Request | Route |
| --- | --- |
| Correct copy on one screen without changing meaning or behavior | Apply the local edit and check the affected rendering or content. Use UI Design if the change calls for an interaction or design decision. |
| Try two interaction patterns with synthetic data | UI Design for a visual concept. Technical Research for a bounded feasibility experiment. Capture what the experiment establishes before deciding whether to maintain its output. |
| Add image sharing across an app, API and storage | Use PentaPRO when drafting the requirements. Use Software Delivery to coordinate authorized implementation after the contract establishes permissions, failure behavior and checks. Use specialist guidance at the actual boundaries. |
| Remove one authorization condition | Trace allowed and denied behavior and establish the intended policy before changing it. Use Cybersecurity when threat assessment or hardening is the requested outcome. A short diff can need strong evidence. |

Use an existing issue, specification, schema or contract to record decisions at its owning location. In a combined request, draft and review the scope the user or policy requires before coding. If implementation reveals a material conflict, pause only dependent work and resolve it with the appropriate owner. Keep the actual code, canonical artifacts, tests and evidence aligned through the handoff.

## Generic owners

| Requested result | Primary owner | Boundary |
| --- | --- | --- |
| Requirements, architecture proposal, verification plan or review of specification artifacts | [PentaPRO](penta-pro/SKILL.md) | Five pillars, including their coherence and implementation readiness |
| Screen/flow/visual/accessibility design or critique; authorized UI implementation | [UI Design](ui-design/SKILL.md) | Maintain one cumulative UI contract when documentation is in scope. Load native Android procedures conditionally. |
| Read-only source/PR/test-effectiveness assessment or re-review | [Peer Review](peer-review/SKILL.md) | Evidence-backed findings; test-authoring is a different implementation task |
| Threat modeling, security audit, authorized hardening or security gate | [Cybersecurity](cybersec/SKILL.md) | One threat/control/evidence record, native Android controls loaded conditionally |
| Ambiguous defect, intermittent failure, or performance regression | [Diagnose Defect](diagnose-defect/SKILL.md) | Reproduction, cause evidence, and verification of an authorized fix |
| Tests as the primary deliverable or requested test-first implementation outside native Android | [Behavior Testing](behavior-testing/SKILL.md) | Executed behavioral checks in the existing runner |
| Concrete HTTP API server changes | [HTTP API](http-api/SKILL.md) | Handler and integration implementation against the caller contract |
| Concrete MCP server changes | [MCP Server](mcp-server/SKILL.md) | Protocol capabilities, transport, and actual downstream behavior |

The closure round adds four portable owners, bringing the collection to **21**. See [all upstream dispositions](COLLECTION-REVIEW.md).

- [Software Delivery](software-delivery/SKILL.md) — Coordinate dependent implementation tasks or increments and verify their integrated result.

- [Technical Research](technical-research/SKILL.md) — Resolve technical uncertainty with traceable evidence.

- [Git Delivery](git-delivery/SKILL.md) — Review, commit and publish the authorized Git snapshot.

- [Agent Instructions](agent-instructions/SKILL.md) — Maintain portable software-development agent guidance.

## Every Android source skill and its destination

Source inventory: the 14 entrypoints in the user-supplied local `android-skills` directory on 2026-11-06. The project attributes the Android and PR-quiz source skills to Philipp Lackner and [PL Coding's Claude Code Skills page](https://www.pl-coding.com/claude-skills); see [third-party notices](THIRD-PARTY-NOTICES.md#pl-coding-android-and-pr-quiz-skills) for attribution and license limits. The earlier `design` consolidation remains recorded in UI Design; it is absent from this source inventory. Integration copies and adapts the source; it does not delete or install anything in that directory or a user's agent profile.

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

The Android integration stage brought the collection to **13 discoverable skills**. With the four engineering packages above, that research stage reached **17**. The five consolidated Android names are not separate SKILL.md entrypoints or forwarding aliases, preventing duplicate discovery. Their material remains in conditional references, with local links redirected to the canonical owner.

## Boundaries in common requests

- “Review the requirements, design and handoff in these five pillar files” → PentaPRO. “Review the implementation against those requirements” → Peer Review.
- “Specify an API migration and its recovery plan” → PentaPRO with the service/API profiles. “Review whether old clients survive the migration” → Peer Review with the backend reference. “Assess cross-tenant access in the API” → Cybersecurity with web/API controls.
- “Design and implement the approved browser form” → UI Design with the web reference. The backend behavior stays with the project's existing contract and implementation workflow.
- “Review this Android PR and its tests” → Peer Review with Android/test references. Do not activate a test-writing workflow or modify source from that review request.
- “Implement retry on this Compose screen” → UI Design with its Android presentation/component procedures; use data/background helpers only for actual subordinate code changes.
- “Write a Room migration test” → Android integration testing. “Are these migration tests meaningful?” → Peer Review.
- “Audit login/deep links/WebView” → Cybersecurity with Android controls, not an additional Android security audit.
- “Plan an Android architecture” → PentaPRO. “Add this approved Gradle module” → Android module structure.
- “Find why this Android sync sometimes drops writes” → Diagnose Defect while the cause is unclear. Use the native data helper for the concrete fix when applicable.
- “Add a browser regression for retry after a failed save” → Behavior Testing. A native Compose interaction test uses the native Android UI test owner.
- “Implement this HTTP write endpoint and its regression checks” → HTTP API. “Expose the action as an MCP tool” → MCP Server. An implementation that touches both uses the actual transport and owning service contract at each boundary. Coordinate through Software Delivery when dependent tasks or increments need a shared execution plan.
- “Create a PR” alone → no quiz. “Add a comprehension quiz to this PR” → PR Quiz. Drafting, publishing, workflow installation and branch-rule changes retain their distinct authorization scopes.

Cross-package links are optional navigation within this collection. A separately installed helper uses its own core instructions and project-owned contracts; it must not claim to have loaded an absent companion. Install related packages when desired, and preserve each package's internal references. Generic owners do not require the Android helper packages for non-Android work.

## Carry context between tasks

For a material handoff, carry the requested outcome/mode and existing authority, target repository and snapshot/variant, canonical requirement/contract IDs, decisions versus proposals, changed files, actual checks and remaining gaps. Reopen the affected source if it changed. Keep this in the existing task record or conversation; no new handoff document is required.

For example, “implement retry, then review the change” has an implementation step followed by read-only review of the resulting snapshot. Reuse the screen/data contract; do not restart a product interview. A review finding does not itself authorize unrelated fixes. If the same issue appears in a security and code review, reference the shared root cause and reconcile evidence instead of counting it as two defects or averaging verdicts. Distinct requested assessments may retain their own scoped conclusions.

When contracts disagree, identify the actual conflicting records and status/authority. A mock, test, later file timestamp or confident model statement cannot silently overrule an accepted requirement. Settle routine delegated implementation choices directly; leave only work depending on an unresolved consequential decision pending. Preserve earlier evidence with its tested revision rather than relabeling it as evidence for the new one.

Project-selected specification and tracking tools retain their canonical records. The five PentaPRO pillars may index external requirement/task artifacts instead of duplicating them; the UI contract links the governing behavior rather than defining a competing business policy. A proposed change, an implemented branch and the deployed baseline are distinct states even when they share a capability ID.

## Validation scope

The [skill evaluation procedure](SKILL-EVALUATION.md) defines candidate screening, paired runs, evidence and adoption decisions. The [assessment](SKILL-ASSESSMENT.md#validation-record) records the initial new-skill trial.

For a model or host comparison, pin the skill revision, fixture and starting state. Use the same task, available tools, permissions and budget for the baseline and skill-assisted runs. Supply both matching and non-matching requests, including a case with a missing reference or a misleading tool result. Keep expected outcomes separate from reviewer inputs. Score the selected owner, observable output, preserved files, actual effects and accuracy of evidence claims. Record runs and failures by model/host, and keep structural checks separate from these results.

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

### Closing audit after SDD and layered-review integration — 2026-11-06

Reviewed all 13 current entrypoints and their supporting resources by area, preserving the earlier attribution, Peer Review 1.9.0 and tutorial work. Seven packages received justified corrections; the other six required no further behavioral change. Updated versions and manual-installation coverage are synchronized in README.

Concrete corrections: PentaPRO indexes project-selected canonical requirement/change/task artifacts instead of creating competing copies; native build guidance respects effective built-in Kotlin opt-outs; DAO guidance distinguishes literal LIKE matching and SQLite REPLACE cascades from ordinary updates; integration tests exercise these actual boundaries. Android UI examples preserve the selected DI/presentation/module choices. Security guidance requires account/generation isolation at the final write boundary, not just a prior session check. UI tooling and the PR publisher reject duplicate JSON declarations; UI tooling also reports oversized numeric input cleanly and distinguishes an old retained export from a new successful build.

Executed closure checks: all 13 skill validators, README/template version alignment, repository-local Markdown links/anchors, YAML parsing and `git diff --check` passed. The UI helper passed 22 Python tests; the PR publisher passed 10 Python tests; the actual embedded workflow passed 19 offline scenarios. New ambiguous-JSON/numeric regressions failed before their fixes and passed afterward. Compiled Kotlin/SQLite checks reproduced wildcard and REPLACE counterexamples, passed seven literal-query cases, and retained seven orchestration groups plus four concurrency/fake checks with real coroutines.

A fresh PentaPRO forward trial updated only five pillar files in a disposable project, retained canonical OpenSpec records and honest readiness/evidence states, and preserved the other seven files by SHA-256 comparison. Its package evaluation file records the actual scope. This adds one bounded workflow observation, not evidence of smaller-model quality or automatic activation across hosts. No consuming Android app/build, generated Room DAO, device/assistive-technology run, deployed service or live GitHub permission test was performed.

### Final maintenance pass — 2026-11-07

Reviewed all 13 entrypoints and the pending changes. The Android helpers put project, contract, and verification decisions before examples. The generic skills sharpen the traces for durable writes, uncertain outcomes, review evidence, delayed UI results, and authorization at the actual tool effect.

The offline PR Quiz review reproduced stale checkbox and comment submissions and a hidden key pointing to a removed option. The grader now checks the event head or comment revision token, rejects invalid visible option/key combinations, and confirms the current revision before writing a new pass. Bare comment commands from the earlier template need the current token. The prototype checker now resolves long alias chains iteratively and bounds recursive fragment expansion.

All 13 packages passed structural validation. The UI helper passed 24 Python tests, the PR publisher passed 12 Python tests, and the actual embedded grader passed 25 offline scenarios with GitHub API doubles. In a disposable project, a separate PentaPRO trial produced five linked drafts, preserved all three existing files, and recorded blocked readiness for a proposed inventory API retry contract. The Peer Review trial and PentaPRO trial used the same model as this maintenance pass. Smaller models, consuming Android apps, and a hosted GitHub workflow were outside these checks.
