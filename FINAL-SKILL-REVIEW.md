# Final skill maintenance review

This record contains successive reviews. Earlier dates, counts and versions describe their original snapshots. See the [current collection review](#current-collection-review) for the latest pass. The [README catalog](README.md#available-skills) owns current package versions.

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

## Production Operations addition

On 2026-11-10 the collection added [Production Operations](production-operations/SKILL.md) as its 22nd package. It owns hosted backend planning, pipeline and infrastructure configuration, authorized deployment, runtime verification and recovery. PentaPRO retains specification, Software Delivery retains dependent application implementation, and Git Delivery retains Git publication. The package ships five conditional provider guides, two adaptable templates, worked examples and [offline evaluation scenarios](production-operations/evals/scenarios.md). Its [source notes](production-operations/references/sources.md) record original synthesis and linked primary references. The earlier validation records refer to their own snapshots.

Local validation passed all 22 skill metadata checks, the collection catalog/license/link validator and all 68 offline helper tests. Skills CLI 1.7.6 installed only the new package into a disposable Codex project, where its 18 files matched the source byte for byte.

Two independent same-model forward scenarios exercised planning and safety decisions without cloud access. A Cloud Run runner context mismatch and partial backfill prompted explicit cross-project federation and job execution reconciliation guidance. A Cloudflare staging binding to production data and a Durable Object rename prompted exact lifecycle and rollback rules and checks of the prior revision's bindings. These runs exercised responses to fictional inputs. They supplied no live deployment, provider login, MCP connection, recovery or comparative model evidence.

### Integration follow-up

The adoption path and capability table now route hosted work to Production Operations. The [evaluation runner](SKILL-EVALUATION.md#score-the-outputs) registers a synthetic target mismatch and partial migration fixture. The follow-up verified fixture and owner paths. The new runner case has no model trial result yet.

The existing [GitHub validation workflow](.github/workflows/validate.yml) discovers root skill packages through the collection validator. A disposable Git snapshot passed, and separate controls rejected a missing AWS guide and a mismatched README version for Production Operations. All 22 packages, 768 local links and anchors, and 68 offline tests passed in the follow-up. Hosted CI and live cloud deployment were outside these checks.


## 22-package closing review

Date: 2026-11-10. Reviewed the local collection over `648fe9c`, preserving the pending Production Operations addition and integration changes. This was a maintainer self-review. Read all 22 entrypoints, checked their requested outcomes, authority, failure handling and evidence requirements, and traced selected security, Android, MCP, delivery and operations references. Checked the catalog, routing, project template, provenance, installation instructions and validation workflow. Supporting references received risk-directed inspection, not exhaustive re-execution of every example.

| Packages | Assessment |
| --- | --- |
| PentaPRO; Software Delivery; Agent Instructions | Keep the separation of accepted contracts, proposals, implementation authority and observed evidence. Existing SDD records remain canonical; ordinary scoped work does not need a new specification framework. |
| Technical Research; Diagnose Defect | Keep primary-source applicability, bounded experiments, controls and cause uncertainty. A plausible explanation is not a reproduced cause. |
| HTTP API; MCP Server | Keep tenant/resource authorization, compatibility, uncertain outcomes and durable idempotency. Protocol revision and actual SDK/client support remain separate checks. |
| Behavior Testing; Android Unit Testing; Android Integration Testing; Android UI Testing | Keep independent expectations, actual failure boundaries, deterministic scheduling and the distinction between mocked, host, device and live-service evidence. |
| Android Module Structure; Android Data Layer; Android Error Handling; Android DI Koin; Android Background | Keep version-aware examples, cancellation, account-bound commits, migration preservation, component ownership and effective startup/release checks. |
| UI Design; Peer Review; Cybersecurity | Keep observable interaction/accessibility contracts, substantiated findings, threat/control evidence, actual independence and scoped verdicts. No additional instruction defect was established in the inspected paths. |
| Git Delivery; PR Quiz; Production Operations | Keep publication and deployment scoped to actual authorization, exact revision/target verification and recovery. The quiz remains an educational aid. Provider access and real deployment remain environment-specific. |

Rechecked the [Agent Skills specification](https://agentskills.io/specification), [AGP built-in Kotlin](https://developer.android.com/build/migrate-to-built-in-kotlin), [Koin verification](https://insert-koin.io/docs/reference/koin-test/verify/), [Compose v2 testing](https://developer.android.com/develop/ui/compose/testing/migrate-v2), and [MCP revision changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog). No new third-party skill implementation was incorporated. Existing notices and runtime package versions remain unchanged.

### Corrections to the collection gate

- The anchor validator previously counted headings inside fenced code. A link could therefore pass without a rendered heading, and an example could shift duplicate-heading numbering. Link and heading checks now share the same fenced-example filtering.
- Optional host metadata was not checked by the automated collection gate. It now checks YAML mapping shape and duplicate keys, supported UI fields, owner invocation in the default prompt, packaged icon paths, color syntax and boolean invocation policy. Files remain optional; this does not claim full host-schema or runtime-discovery validation.
- Added 12 offline validator regression/control tests. Six negative cases failed under the old gate because invalid fixtures were accepted; all now pass with the correction. The tests also cover valid collections, real duplicate headings, ignored targets, catalog drift and valid host metadata.
- Updated README validation scope and test descriptions. The existing GitHub Actions job already discovers `scripts/tests`, so it executes the new tests without a workflow edit. No cloud credentials or model calls are needed.

### Observed verification and readiness

All 22 installed skill-creator metadata checks passed. The collection gate passed catalog, license, installation, local-link/anchor and optional host-metadata checks. All 80 offline tests passed: 15 collection/evaluator tests, 26 UI helper tests, 12 PR publisher tests and 27 Node workflow scenarios. Whitespace checks passed. Local runtimes remain Python 3.12.6 and Node.js 26.10.0; hosted CI declares Python 3.12 and Node.js 24.

The collection is ready for use with its documented prerequisites and project-specific verification; no substantiated blocker remains in the inspected scope. This does not establish universal correctness, security certification, or best-in-class performance across models. This closing pass did not rerun model comparisons, live deployments, Android devices, browser/assistive sessions, installation trials or hosted CI. Their earlier evidence retains its original scope. Changes remain local; no commit, push or deployment was performed.

## Pilot readiness review

2026-11-11. Reviewed the 22 entrypoints in the working collection over `9405717` for discovery, responsibilities, authority, operational failure handling and evidence. Followed relevant templates and procedures, including risk-directed inspection of Android version and runtime assumptions, protected API/MCP effects, Git scopes, review independence, OpenSpec status, and production promotion. The [adoption plan](docs/ANTHROPIC-ADOPTION-PLAN.md) records rationale and the [pilot guide](README.md#start-a-pilot) is the project entry point.

| Package | Review and disposition |
| --- | --- |
| Software Delivery | Added OpenSpec and prototype adoption examples. The forward test exercised actual scenario, task and handler evidence. |
| PentaPRO | Added OpenSpec ownership and revision-aware resumption example. Synchronized PROCESS template and catalog. |
| Agent Instructions | Added scoped runner and external grader controls to the evaluation method. Kept evaluation conditional on significant instruction changes. |
| Behavior Testing | Retained test authoring scope, independent expected results and failure sensitivity. Receipt controls exercise those principles. |
| Peer Review | Retained read-only review and substantiated findings. Added a clean comparison fixture to the collection suite. |
| Cybersecurity | Retained threat/control ownership, scoped access and evaluation of the actual enforcement boundary. The runner enforces mount exclusion outside skill instructions. |
| Production Operations | Retained exact target, served revision and recovery boundaries after two offline forward tests. Added the stale-green fixture. |
| Diagnose Defect | Retained failing versus working comparison and authorization for fixes and probes. |
| HTTP API | Retained tenant-scoped retry, compatibility, transaction and external destination controls. |
| MCP Server | Retained revision-specific lifecycle, caller authorization and downstream effect checks. |
| Technical Research | Retained primary evidence, bounded experiments and explicit uncertainty. |
| Git Delivery | Retained staged versus working-tree evidence and explicit publication scope. |
| UI Design | Retained conditional platform procedures and separation of visual, interaction and usability evidence. |
| Android Module Structure | Retained effective Gradle mode, module ownership and supported build/release variants. |
| Android Data Layer | Retained atomic writes, migration and session-bound storage behavior. |
| Android Error Handling | Retained typed failure classification, cancellation and bounded retry behavior. |
| Android DI Koin | Retained runtime argument and qualifier checks beyond graph inspection. |
| Android Background Work | Retained idempotency, WorkManager state and account-at-commit protections. |
| Android Unit Testing | Retained deterministic scheduling, cleanup and observable assertions. |
| Android Integration Testing | Retained actual migration, transport and application construction boundaries. |
| Android UI Testing | Retained native runtime, synchronization, selectors and platform evidence. |
| PR Quiz | Retained opt-in discovery boundary, safe publication and educational grading scope. |

All 22 packages passed the skill-creator validator and the collection catalog, license, link and installation checks. All 83 offline tests passed (18 collection/evaluator, 26 UI helper, 12 PR publisher and 27 Node grader scenarios). The installation comparison matched 144 files. The [pilot evidence](evals/RESULTS.md#anthropic-adoption-pilot-preparation) records the OpenSpec, isolation, grader and operations checks and their coverage. Review of entrypoints and selected references supports adoption for a scoped pilot. It does not establish exhaustive platform behavior, universal discovery, or superior model performance.


## Collection readiness verification

2026-11-11. Reviewed all 22 entrypoints in the candidate over `640d5ed`, their task boundaries and supporting resources, the installation and routing guides, project template, helper scripts, evaluation fixtures, notices and validation workflow. Rechecked version-sensitive instructions against the owning sources for the [Agent Skills format](https://agentskills.io/specification), [Android Gradle and Kotlin](https://developer.android.com/build/migrate-to-built-in-kotlin), [Compose test environments](https://developer.android.com/develop/ui/compose/testing/migrate-v2), [OpenSpec schema](https://openspec.dev/docs/schemas/spec-driven), [MCP revisions](https://modelcontextprotocol.io/specification/2026-07-28/changelog) and [GitHub CLI publishing](https://cli.github.com/manual/gh_pr_edit).

| Change | Reason and evidence |
| --- | --- |
| Software Delivery 1.4.0 and Android Module Structure 1.3.0 | The Castas retrospective showed a source/behavior mismatch and different device visibility in the agent sandbox and host. Porting now links a pinned source, the accepted rule and a comparison through the target entry point. Android setup now checks boot, device identity and a minimal user-visible assertion on uncertain runners. |
| PR Quiz 1.3.0 | The old publisher compared body text alone. A new head could receive questions drafted for an older diff. The supported invocation supplies the target repository and reviewed SHA. The helper pins the resolved PR URL and checks the head and body around the edit. Regression tests and an independent subprocess trial with a fake `gh` covered a matching revision, a stale draft, drift before the edit, and drift after submission. The last case reported the submitted edit and required inspection. GitHub does not provide an atomic compare-and-edit through this helper. |
| Evaluation runner | The candidate snapshot formerly copied whole directories, including ignored local files. It now follows the Git distribution inventory and refuses symlinks in selected package paths. The regression exercises changed tracked content, new files, deleted files, and an ignored control. |
| Documentation and validation | The adoption plan's relative links resolve after its move, and the prior root URL redirects readers. The README includes a first-task example and links the tutorial and case study as dated editions. Git attributes mark the PDFs as binary. A staged validation in a disposable checkout reproduced the original PDF whitespace failure and passed after the attribute was added. |

All 22 entrypoints passed the skill-creator validator. The collection gate found no issues across 135 Markdown files, 818 local link/anchor checks, 22 catalog versions, package licenses and optional host metadata. All 87 offline tests passed: 20 collection and evaluation tests, 26 UI helper tests, 14 quiz publisher tests, and 27 grader scenarios. The OpenSpec 1.16.0 fixture confirmed valid artifacts with unfinished work and detected a missing scenario. The Bubblewrap probe denied grader/sibling file access and confirmed private scratch writes.

Both the manual installation and Skills CLI 1.7.6 with `--copy` installed all 22 packages in disposable projects. All 144 installed package files matched the source. Collection-level guides, scripts and fixtures stayed outside the project installation. Codex CLI 0.160.0 reported all 22 project skills enabled through the local `skills/list` call. The [MCP fixture](evals/check_mcp_sdk.py) also passed in-process with Python SDK 2.2.0 for legacy sessions, modern direct calls, SDK discovery, replay after response loss, caller-bound handles, and version/header errors.

The candidate supports local adoption using the documented tools and prerequisites. Hosted CI, production providers, live GitHub grading, consuming Android builds, and quality comparisons across models and other hosts require their own evidence.

## Current collection review

2026-11-13. Reviewed all 22 installable entrypoints and their supporting assets and references relevant to the reviewed changes, using `2500753` as the starting revision. Checked canonical record ownership, task selection, permission boundaries, reproducible evidence, source currency, standalone installation and developer onboarding. This maintenance pass included targeted independent review, executed controls and a matched synthetic GPT-6.1 Sol pilot. The [evaluation record](evals/RESULTS.md#matched-gpt-61-sol-pilot) describes outcomes and limits.

| Package | Review disposition |
| --- | --- |
| PentaPRO | Resolve authority and output format before writing. Preserve local and external record identity, link verification to the tested revision, and distinguish priority, obligation and confirmation. |
| Software Delivery | Document OpenSpec defaults, version-specific skill invocation, strict post-archive validation, and a project-native SDD example. Preserve direct and exploratory paths. |
| Behavior Testing | Add focused examples for test boundary, denied side effects, input selection, fault sensitivity and intermittent failures. Preserve the existing test-first scope. |
| Diagnose Defect | Add reliable-reproducer prerequisites, bisection handling for unclassifiable revisions, and controlled input reduction. |
| Technical Research | Verify applicable versions and dependency provenance, examine counterevidence, and bound benchmark conclusions. |
| HTTP API | Add conditional guidance for throttling, shared cache isolation, atomic write preconditions and consumer migration. Retain the existing idempotency and SSRF procedure. |
| MCP Server | Make token audience and downstream credential separation operational and link both supported authorization revisions. Test denied requests at the actual downstream boundary. |
| Peer Review | Add a caller/installed API check and an example of a substitute hiding a protection failure. Retain evidence-based review and valid zero-finding outcomes. |
| Cybersecurity | Make detection and accountability visible in threat coverage, update MCP source links, and include the version-qualified Android encrypted storage option. |
| UI Design | Add a rendered accessibility journey spanning automated and manual checks, and make Android companion instructions optional when installed alone. |
| Production Operations | Connect an applicable error-budget policy to a promotion decision and add incident recovery and follow-up evidence to the existing record. |
| Git Delivery | Respect project commit/signature policy and stop publication on credentials present anywhere in the outgoing range. |
| Agent Instructions | Distinguish explicit use from discovery and place generated-code execution and scoring in separate environments. |
| Android Module Structure | Describe effective built-in Kotlin configuration, conditional reference stacks, and Room 2/3 conventions. |
| Android Data Layer | Preserve existing clients and serialization policy, give Room 2/3 setup alternatives, and test actual data boundaries and migration. |
| Android Error Handling | Preserve cancellation, keep deadline ownership explicit, and carry server retry hints where the operation requires them. |
| Android DI Koin | Use compile-time checks where supported and exercise runtime parameters, module selection and platform startup where needed. |
| Android Background | Document current runtime coordinates, expedited quotas, foreground requirements and startup ownership. |
| Android Unit Testing | Clarify test scheduler scope and keep fixtures and cancellation checks deterministic. |
| Android Integration Testing | Describe version-matched Room tests, DataStore test-scope cleanup and optional process isolation. |
| Android UI Testing | Preserve resolved Compose factory/scheduler choices and use supported automated accessibility checks with device evidence when required. |
| PR Quiz | Reviewed the explicitly requested educational workflow, eligibility, revision binding, and the limits of its informational status. The current code and offline grader behavior meet that scope. |

The [routing guide](SKILL-ROUTING.md), [project template](AGENTS-template.md), [maintenance procedure](SKILL-EVALUATION.md) and [Portuguese development guide](docs/guia-consolidado-desenvolvimento-com-agentes.pdf) share the same project-owned contract and verification workflow. The earlier [Castas case study](docs/relatorio-retrospectiva-castas-android.pdf) remains a dated record of that project.

The revised 112-page guide preserves the existing labs and adds OpenSpec 2.0 setup and troubleshooting, project-native SDD, vibe coding and prototype promotion, platform-specific verification, and a comparative pilot exercise. All nine extracted OpenSpec deltas validated and archived with simulated task completion, and all eight consolidated capability specs passed strict validation. The CLI lab passed six subprocess checks and rejected a deliberate negative-value regression. The current PDF's 22 catalog versions, page count, 165 internal destinations and 51 bookmarks were checked. The pages were rendered for inspection.

The Android review exercised five groups of JVM behavior with the extracted Kotlin Result, repository and fake snippets and the real coroutine library. Room, Compose and platform instructions were checked against primary sources. Builds of the updated variants against consuming Android dependencies and device behavior remain project checks. Hosted CI, live GitHub grading and production deployment were outside this local collection validation.

The closing run passed all 22 entrypoint validations and 99 offline checks: 32 collection/evaluator tests, 26 UI helper tests, 14 PR quiz publisher tests, and 27 quiz workflow scenarios. The case manifest and the standalone link and catalog checks passed. Local installation and discovery passed for the supported Codex workflow. Use the [installation guide](README.md#installation-and-activation) to adopt the collection and the [pilot procedure](SKILL-EVALUATION.md#reproduce-the-synthetic-codex-trials) to measure it on representative project work.
