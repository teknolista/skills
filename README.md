# ✨ AI Agent Skills

My personal collection of reusable skills for developers building software with AI coding agents. PentaPRO turns intent into an actionable specification; Peer Review checks implementation against requirements and concrete evidence; Cybersecurity assesses security risks and controls across software, DevOps, and IT systems. UI Design turns requirements into screen and interaction specifications for web and Android, with authorized implementation and verification. Four generic skills own specification, UI work, peer review and security. Optional native Android implementation/test helpers and a generic PR quiz complement them; see [skill ownership](SKILL-ROUTING.md). Each skill can be used independently.

All skill instructions and generated artifacts are in English. Conversation can use the user's preferred language.

> [!IMPORTANT]
> These skills are still in development. They are based on my personal experience developing my own applications and may need adjustments for other projects, teams, models, and workflows.
>
> Everyone is welcome to use, improve, and adapt them. The [MIT License](LICENSE) covers repository-original work, subject to its notice requirements. Imported material retains its source terms; see [third-party notices](THIRD-PARTY-NOTICES.md).
>
> Feedback from actual use, constructive criticism, and suggestions are very welcome through [GitHub Issues](https://github.com/teknolista/skills/issues).

## Contents

- [✨ AI Agent Skills](#-ai-agent-skills)
  - [Contents](#contents)
  - [Available skills](#available-skills)
  - [Installation and activation](#installation-and-activation)
    - [Install with the skills CLI](#install-with-the-skills-cli)
    - [Manual installation](#manual-installation)
    - [Activation](#activation)
  - [Agent and model compatibility](#agent-and-model-compatibility)
    - [Native skill locations](#native-skill-locations)
    - [Required capabilities](#required-capabilities)
    - [Model selection and validation](#model-selection-and-validation)
  - [PentaPRO](#pentapro)
    - [The five pillars](#the-five-pillars)
    - [Example requests](#example-requests)
    - [Output and working boundaries](#output-and-working-boundaries)
    - [Resources](#resources)
  - [Peer Review](#peer-review)
    - [Example requests](#example-requests-1)
    - [Findings, verdicts, and boundaries](#findings-verdicts-and-boundaries)
    - [Test effectiveness](#test-effectiveness)
    - [Independent review and models](#independent-review-and-models)
    - [Hosted review environments](#hosted-review-environments)
    - [Resources](#resources-1)
  - [Cybersecurity](#cybersecurity)
    - [Modes and limits](#modes-and-limits)
    - [Example requests](#example-requests-2)
    - [Coverage and findings](#coverage-and-findings)
    - [Resources](#resources-2)
  - [UI Design](#ui-design)
    - [Examples and output](#examples-and-output)
    - [UI Design resources](#ui-design-resources)
  - [Native Android implementation and testing](#native-android-implementation-and-testing)
  - [PR Quiz](#pr-quiz)
  - [Project AGENTS.md template](#project-agentsmd-template)
  - [Repository structure](#repository-structure)
  - [Maintenance and new skills](#maintenance-and-new-skills)
    - [Validation and improvement](#validation-and-improvement)
    - [Adding a new skill](#adding-a-new-skill)
  - [License and attribution](#license-and-attribution)

## Available skills

| Skill | Version | Purpose |
| --- | --- | --- |
| [PentaPRO](#pentapro) | 2.5.4 | Explore, create, resume, update, or review software specifications across PRODUCT, PROOF, PROJECT, PRODUCTION, and PROCESS. |
| [Peer Review](#peer-review) | 1.9.0 | Review backend, frontend, Android, and test code for substantiated defects and meaningful regression protection. |
| [Cybersecurity](#cybersecurity) | 1.5.2 | Model threats, assess security controls, and verify authorized hardening across web/API, desktop/mobile, DevOps, cloud, and IT projects. |
| [UI Design](#ui-design) | 1.5.2 | Specify, refine, review, and implement web and Android screens; maintain cumulative `docs/ui-design.md`. |
| [Android modules](android-module-structure/SKILL.md) | 1.2.2 | Implement native Gradle/module configuration; specification belongs to PentaPRO. |
| [Android data](android-data-layer/SKILL.md) | 1.2.2 | Implement repositories, Ktor/OkHttp, Room, DataStore and sync. |
| [Android errors](android-error-handling/SKILL.md) | 1.2.1 | Implement typed domain/HTTP/storage error handling. |
| [Android Koin](android-di-koin/SKILL.md) | 1.2.1 | Implement dependency bindings and Android lifetimes. |
| [Android background](android-background/SKILL.md) | 1.2.1 | Implement durable WorkManager jobs and retries. |
| [Android unit testing](android-unit-testing/SKILL.md) | 1.2.1 | Author/run/debug isolated logic tests. |
| [Android integration testing](android-integration-testing/SKILL.md) | 1.2.2 | Author/run/debug non-UI integration tests. |
| [Android UI testing](android-ui-testing/SKILL.md) | 1.2.1 | Author/run/debug native device/emulator Compose tests. |
| [PR Quiz](pr-quiz/SKILL.md) | 1.2.1 | Explicitly requested PR decision-comprehension aid, separate from review approval. |

The [routing and consolidation map](SKILL-ROUTING.md) records all 14 source skills. Four Android UI skills are internal UI Design procedures; Android security is a Cybersecurity reference. Those five overlapping names are deliberately not separate installable skills.

## Installation and activation

### Install with the skills CLI

Install [Node.js 22.20 or later](https://github.com/vercel-labs/skills#install-a-skill), with npm/npx available, and run the command from the project where you want to use the skills. The CLI downloads the published GitHub contents; local unpublished changes in this repository are not included.

Choose which skills to install for Codex:

```bash
npx skills@latest add teknolista/skills -a codex
```

Install all available skills for Codex without selection prompts:

```bash
npx skills@latest add teknolista/skills --skill '*' -a codex -y
```

Install only one skill, or inspect the available skills without installing:

```bash
npx skills@latest add teknolista/skills --skill ui-design -a codex
npx skills@latest add teknolista/skills --list
```

Available skill names are `penta-pro`, `peer-review`, `cybersec`, `ui-design`, `android-module-structure`, `android-data-layer`, `android-error-handling`, `android-di-koin`, `android-background`, `android-unit-testing`, `android-integration-testing`, `android-ui-testing`, and `pr-quiz`. Replace `codex` with another [supported agent identifier](https://github.com/vercel-labs/skills/blob/main/docs/agents.md), such as `claude-code` or `cursor`. Keep the quotes around `'*'` so the shell passes it to the CLI.

Installation defaults to the current project. Add `-g` for user-level installation across projects:

```bash
npx skills@latest add teknolista/skills --skill '*' -a codex -g -y
```

Use `npx skills@latest check` to check for updates and `npx skills@latest update` to update installed skills. See the [official CLI reference](https://github.com/vercel-labs/skills/blob/main/docs/commands.md) for installation options and update scopes.

### Manual installation

Copy the complete directory of each desired skill into the skills location supported by your agent. Preserve its internal relative paths. For a Codex project, the installed entrypoints are:

```text
your-project/.agents/skills/penta-pro/SKILL.md
your-project/.agents/skills/peer-review/SKILL.md
your-project/.agents/skills/cybersec/SKILL.md
your-project/.agents/skills/ui-design/SKILL.md
your-project/.agents/skills/android-module-structure/SKILL.md
your-project/.agents/skills/android-data-layer/SKILL.md
your-project/.agents/skills/android-error-handling/SKILL.md
your-project/.agents/skills/android-di-koin/SKILL.md
your-project/.agents/skills/android-background/SKILL.md
your-project/.agents/skills/android-unit-testing/SKILL.md
your-project/.agents/skills/android-integration-testing/SKILL.md
your-project/.agents/skills/android-ui-testing/SKILL.md
your-project/.agents/skills/pr-quiz/SKILL.md
```

A skill stored in this repository is not automatically installed into other projects. Codex discovers repository skills from `.agents/skills/`; if a copied skill does not appear, restart the session. Other hosts use their own discovery locations and invocation syntax. See [agent and model compatibility](#agent-and-model-compatibility) for documented locations, capabilities, and integration limits.

### Activation

The skills support automatic selection for matching tasks. In Codex, mention `$penta-pro`, `$peer-review`, `$cybersec`, or `$ui-design` to select one explicitly. Their `agents/openai.yaml` files provide optional display metadata and default prompts; they do not select a model. Select models through the host's controls or authorized orchestration. Native helpers use their listed names, for example `$android-data-layer`; `pr-quiz` runs only for a requested comprehension quiz or quiz setup, never merely after PR creation.

The core instructions use Markdown and optional references/templates. Cross-package links are optional navigation; no generic owner requires an Android helper for other platforms. The optional prototype helper uses Python. Publishing a requested PR quiz requires Python, gh and actual GitHub access; its optional grader uses GitHub Actions. Installing a package does not install these tools or activate a remote workflow. Actual work still requires relevant project access and whatever tools its requested checks need. Saving a specification or report requires a writable destination. Installing a skill does not supply those capabilities or authorize additional actions.

## Agent and model compatibility

Official host documentation checked on 2026-10-25. These packages use the Agent Skills format: Markdown instructions, relative references/assets, and optional OpenAI UI metadata. Native format support, execution access, and measured task quality are separate claims.

### Native skill locations

Copy the complete skill directory, retaining its internal paths. Use the location supported by the actual host and execution environment; installing locally does not install into every cloud agent.

| Host | Documented project locations | Documented user locations | Official guidance |
| --- | --- | --- | --- |
| Codex | `.agents/skills/<name>/` | `~/.agents/skills/<name>/` | [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` | [Extend Claude with skills](https://code.claude.com/docs/en/skills) |
| Gemini CLI | `.gemini/skills/<name>/` or `.agents/skills/<name>/` | `~/.gemini/skills/<name>/` or `~/.agents/skills/<name>/` | [Agent skills](https://geminicli.com/docs/cli/skills/) |
| GitHub Copilot | `.github/skills/<name>/`, `.claude/skills/<name>/`, or `.agents/skills/<name>/` | `~/.copilot/skills/<name>/` or `~/.agents/skills/<name>/` | [Create agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| Cursor | `.agents/skills/<name>/` or `.cursor/skills/<name>/` | `~/.agents/skills/<name>/` or `~/.cursor/skills/<name>/` | [Agent Skills](https://cursor.com/docs/skills) |

Invocation and consent differ by host. For example, Codex documents `$name`, Claude Code and Cursor support `/name`, and Gemini CLI exposes skill discovery/activation controls. Confirm discovery using the host's skill list or explicit invocation. Avoid installing duplicate copies with the same name just to cover several paths.

### Required capabilities

| Task | Necessary access | If unavailable |
| --- | --- | --- |
| PentaPRO creation/update | User intent, relevant existing context, package assets, and a writable requested destination | Ask only consequential missing questions; retain proposals and blockers. If writing is unavailable, return the draft and disclose that it was not saved. |
| PentaPRO review | The actual specification and relevant authoritative context | Report missing material rather than treating an absent document as ready. |
| UI Design specification and implementation | Relevant requirements/design context and a writable target project; source/toolchain for implementation, browser or Android environment for runtime checks | Save a partial specification and mark pending decisions/checks; never claim rendered, device, accessibility or user validation without evidence. |
| Code inspection | Actual selected source/snapshot, relevant requirements/contracts, and applicable references | Report material missing coverage; do not infer a clean review from a description alone. |
| Cybersecurity assessment | Authorized target/snapshot, relevant security requirements, applicable domain references, and evidence of the controls being claimed | Separate source/configuration from deployed/runtime evidence; mark inaccessible areas and avoid security or compliance guarantees. |
| Executed verification | The project's actual tools and isolated data/environment | Label unexecuted checks and distinguish static conclusions from runtime evidence. |
| Independent review | A separate reviewer/session with actual source access | Disclose self-review or prepare a factual handoff; do not claim independence from a model label. |

Git, shell execution, browsers, Android SDKs, credentials, connectors, and additional agents are not supplied by installing a skill. Git is useful for comparisons, but an explicitly selected source snapshot can be reviewed without it. The skills can be used independently. Cybersecurity live testing and remediation require actual target/action authorization; capability does not imply permission.

Managed review services may load only instruction text. See [Hosted review environments](#hosted-review-environments) for supporting-file and execution limits.

### Model selection and validation

The skills include concrete behavior traces, failure examples, and evidence checks to reduce reliance on unstated engineering knowledge. For larger tasks, retain the target snapshot, reviewed and pending areas, evidence, unresolved questions, and next action. Reopen relevant source after context loss or a changed snapshot. Validate representative tasks on each intended model and host before relying on its results.

The workflows have no hard-coded model, reasoning setting, vendor tool name, or mandatory orchestration mechanism. `agents/openai.yaml` in these packages contains display metadata and a default prompt; it does not select a model. Hosts may offer their own model overrides. Use those controls deliberately rather than adding a vendor-specific override to the portable core.

Choose a currently available model with sufficient reasoning, domain competence, context capacity, and reliable tool use for the task. Escalate difficult requirements or review risks when evidence warrants it. The documented [OpenAI model options](https://learn.chatgpt.com/docs/models) include the repository's example implementation/review pairing; availability and suitability depend on the host/account and observed results. A model name is not a quality gate.

After changing host, model, or significant instructions, run the relevant [PentaPRO cases](penta-pro/evals/scenarios.md), [Peer Review cases](peer-review/evals/scenarios.md), [Cybersecurity cases](cybersec/evals/scenarios.md), and [UI Design cases](ui-design/evals/scenarios.md). Check correct activation, preserved user decisions, meaningful defects versus false positives, honest evidence/coverage, and unintended edits. Compare matched tasks before claiming better accuracy, cost, or latency. Official format support does not establish a cross-vendor performance benchmark.

## PentaPRO

**Version:** 2.5.4 · **Entrypoint:** [penta-pro/SKILL.md](penta-pro/SKILL.md)

Use PentaPRO when defining a product, specifying a substantial feature, maintaining an existing PentaPRO document, or checking whether the next increment is ready for development. It uses existing project information and asks about consequential gaps. Ordinary coding tasks and small, clear specification updates do not restart a full interview.

An exploration-only request stays in the conversation until the user asks to capture the findings. For a material change, PentaPRO compares the proposal with the current requirements and behavior, identifies compatibility commitments, and traces their effects across the pillars. Applicable project rules and amendments are linked from PROCESS.

### The five pillars

| Pillar | Focus |
| --- | --- |
| PRODUCT | Users, value, journeys, business rules, permissions, scope, and observable acceptance criteria. |
| PROOF | Verification methods, concrete examples, failure cases, and acceptance evidence. |
| PROJECT | Delivery constraints, resources, dependencies, risks, architecture, data, and contracts. |
| PRODUCTION | Installation, environments, updates, migration, support, monitoring, and recovery. |
| PROCESS | Tasks, responsibilities, execution authority, review, integration, and escalation. |

The preferred order for interview deepening and document presentation is PRODUCT → PROOF → PROJECT → PRODUCTION → PROCESS. Establish behavior and evidence needs before designing the solution, then detail its operation and execution plan. Gather consequential operational, budget, and platform constraints early. Refine PROOF after design and operational decisions, and maintain PROCESS authority and resume state throughout. Reconcile affected pillars as decisions change; the order does not impose sequential development phases.

The template connects product strategy and stopping criteria to discovery evidence, outcomes, requirements, contracts, verification, and post-release learning. It includes a consolidated identifier and status model, increment readiness, decision and uncertainty records, privacy and accessibility considerations, delivery dependencies, documentation, launch and support readiness, and operational recovery evidence. Conditional profiles cover services, installed/offline apps, CLI tools, infrastructure, libraries, data/scientific workloads, AI features, embedded systems, interactive media, and commercial launch. For Android/KMP projects, an [additional overlay](penta-pro/references/android-kmp.md) details cross-platform contracts, test boundaries, state retention, dependency lifetimes and release evidence within the five pillar files. Combine profiles for hybrid products; they are not an exhaustive taxonomy.

Discovery resolves ambiguous domain terms with examples and counterexamples, compares material alternatives, and records the authority behind decisions. Binding principles become verifiable requirements. The selected increment includes a useful outcome and a check that can demonstrate it before later features exist. Detailed patterns address uncertain completion, retries, concurrent actions, access changes during queued work, and migration coexistence.

### Example requests

```text
Use $penta-pro to explore options for offline editing before we write the specification.
Use $penta-pro to interview me and create a specification for this project.
Use $penta-pro to resume the interview from docs/process.md.
Use $penta-pro to update the specification with these new requirements: ...
Use $penta-pro to review whether the first increment is ready for development.
```

### Output and working boundaries

By default, a first specification uses five files in the project's `docs/` directory. Each file owns its pillar and links related records in the others. One integrated interview populates the set, and the initial draft records pending decisions so the interview can resume.

- `docs/product.md` covers users, scope, requirements, and acceptance criteria.
- `docs/proof.md` covers planned checks, traceability, and actual evidence.
- `docs/project.md` covers design, constraints, contracts, and decisions.
- `docs/production.md` covers distribution, operation, and recovery.
- `docs/process.md` covers the workflow, shared status, coverage, revision history, and next interview action.

Existing single-file specifications and explicitly requested locations remain supported. Migration is performed when requested.

When the project already assigns normative requirements or implementation tasks to an existing change/specification system, PentaPRO keeps the five pillars as global context and navigation. It links the authoritative records instead of copying complete requirements or maintaining another task list. [Integration guidance](penta-pro/references/document-maintenance.md#existing-change-and-specification-workflows) distinguishes the current baseline, an accepted/proposed change, verification and actual deployment without imposing another framework.

Creation saves all five initial drafts before pausing for answers. Later rounds update the affected records, with stable IDs and links to their authoritative definitions. PROCESS records an `In progress` state for material updates across files and a `Consistent` state after reconciliation. Resumption inspects actual contents and completes any interrupted update. Proposed changes retain their baseline, compatibility commitments, and separate status until settled.

The skill distinguishes confirmed information, proposals, and pending decisions. Routine decisions made within explicit delegation are attributed to the agent and can be settled for readiness without being presented as user requirements or document acceptance. When the user is unavailable, retain consequential blockers and complete independent specification work. If saving is unavailable, return an explicitly unsaved draft.

PentaPRO drafts from accessible evidence and delegated choices with provenance. It identifies unresolved research, baselines, legal applicability, approvals, and test evidence. The interview targets consequential missing decisions. All five pillars remain, with coverage recorded as included, linked, pending, deferred, or not applicable. Larger specifications can link feature details, increment plans, and contracts from their owning pillar. The skill loads specialized forms and examples as needed.

Critical product rules should have concrete input/output examples independent of the implementation. PROOF identifies realistic regressions that planned assertions must detect and checks that reported execution actually exercises them. Planned checks remain `Unverified` until executed. Specification readiness, document acceptance, implementation verification, and release acceptance are separate states. Creating or updating a specification does not itself authorize implementation or release; existing authorization remains valid.

A sufficiently specified increment can be ready for implementation while its future software tests remain unverified. An unresolved product decision blocks the work that depends on it. Acceptance records the responsible person's actual decision, scope, revision, and conditions. Exploration and review preserve their next action in the conversation unless specification writing is authorized.

The workflow is model-neutral. Use a host that can load the complete skill folder and relevant project context. Disclose missing capabilities rather than inventing answers or verification results. Package compatibility does not establish identical quality across models.

### Resources

| Resource | Purpose |
| --- | --- |
| [Entrypoint](penta-pro/SKILL.md) | Scope, interview workflow, document maintenance, readiness, and handoff. |
| [Template index](penta-pro/assets/penta-pro-template.md) | Authoring guidance and links to the five pillar templates. |
| [Document maintenance](penta-pro/references/document-maintenance.md) | Canonical ownership, coordinated updates, resumption, and migration. |
| [Focused discovery](penta-pro/references/discovery.md) | Conditional techniques for unclear intent, dependent questions, alternatives, and consequential missing information. |
| [Software profiles](penta-pro/references/software-profiles.md) | Coverage prompts for software types and cross-cutting concerns, including accessibility, privacy, and impacts on people and the environment. |
| [Specification patterns](penta-pro/references/specification-patterns.md) | Conditional forms for data, interfaces, decisions, threats, evidence, and runbooks. |
| [Worked example](penta-pro/references/worked-example.md) | Fictional example of linked requirements and planned evidence, with explicit uncertainty. |
| [Analyst review assessment](penta-pro/references/analyst-review-assessment.md) | Assessment of the supplied reviews, adopted improvements, and recommendations adapted or not adopted. |
| [Source notes](penta-pro/references/sources.md) | Discovery, proposal, project-rule, and operational research, with inspected revisions and adaptation decisions. |
| [Evaluation scenarios](penta-pro/evals/scenarios.md) | Discovery, interview, update, delegation, and scope cases, with validation records. |
| [OpenAI metadata](penta-pro/agents/openai.yaml) | Optional Codex display metadata and example invocation. |

For creation, read the template index and five pillar templates. For updates and reviews, consult relevant sections for structural gaps or readiness. Screen profiles for new specifications or material scope changes and read detailed patterns as needed. Source notes, the analyst assessment, and evaluation cases are maintainer resources.

## Peer Review

**Version:** 1.9.0 · **Entrypoint:** [peer-review/SKILL.md](peer-review/SKILL.md)

Use Peer Review for backend services, frontend applications, Android software, and the effectiveness of their tests. It supports local edits, selected files or snippets, pull requests, commit comparisons, independent second opinions, and re-review after fixes. Reports separate substantiated defects, verification gaps, optional improvements, and remaining release requirements.

### Example requests

```text
Use $peer-review to review all my uncommitted changes, including new files.
Use $peer-review to review this branch against origin/main, including the local edits.
Use $peer-review to review the selected PR against the requirements and checks in docs/product.md and docs/proof.md.
Use $peer-review to review the changed tests for assertions that would miss the regressions they claim to detect.
Use $peer-review to review the Android release changes, focusing on lifecycle and data migration.
Use $peer-review to re-review the fixes for CR-001 and CR-002 on the current revision.
Use $peer-review to prepare a handoff for an independent reviewer in another session.
```

`origin/main` is an example; use the actual intended base. A committed comparison and the current worktree are different scopes. With no named target, the skill starts with uncommitted work, including staged, unstaged, and relevant untracked files, and identifies comparisons that need clarification.

An explicitly selected file or source snippet can be reviewed without Git or an earlier version. The reviewer assesses current behavior and reports origin as `Unknown` when history is unavailable; it does not invent a regression claim or source location.

### Findings, verdicts, and boundaries

Findings include a real location or precise snippet label, reachable trigger, expected/actual behavior, impact, evidence, confidence, correction direction, and regression check. Severity uses P0–P3 with an explicit blocking disposition. Expected results come from authoritative product rules and examples, independently of the implementation and its tests. Zero findings is valid; there is no finding quota.

The report gives coverage, evidence, limitations, and one verdict:

- `Changes requested`: validated blocking findings remain.
- `No blocking findings`: the agreed review is complete without validated blockers.
- `Incomplete`: material context or coverage is missing.

The review preserves the selected source and Git state. Fixes, remote comments or approvals, merging, and releasing follow actual user authorization and project gates. Reports and filled handoffs belong to the reviewed project or requested output location, not the reusable skill folder. Existing `REVIEW.md` guidance is optional; the skill does not create or change project policy automatically.

The reviewer follows consequential behavior from its contract through entry points, guards, effects, and consumers. Concrete inputs and event order help investigate authorization, races, retries, and stale asynchronous results. Existing protections and unknown premises are checked before retaining a finding. Cross-file change maps and guided summaries are reconciled with the full in-scope diff. For related PRs, the skill checks shared behavior and distinguishes branch evidence from the actual integration state. [Conditional coordination guidance](peer-review/references/independent-review.md#coordinate-related-changes) covers owners, dependencies, review capacity and workflow evaluation without imposing queue limits or authorizing Git integration.

The [automated-check layer](peer-review/references/verification.md#establish-automated-check-evidence) separates formatting/static/build checks, security/secret scans and behavioral tests from semantic review. Evidence must match the snapshot; required gates retain their consequences. Migrations, authentication/configuration, dependencies and weakened test/CI protection trigger deeper tracing. Test retirement or replacement is assessed against the affected contract and remaining protection. For known escaped defects, the [learning loop](peer-review/references/verification.md#learn-from-escaped-defects) connects the root cause to a meaningful regression check and proportionate process improvement under the existing authorization.

### Test effectiveness

Peer Review examines the tests relied on for changed behavior, including their discovery, fixtures, real subject, assertions, and completion. It asks which realistic wrong behavior would still pass.

- Inspect tautologies, unused matchers, swallowed failures, unawaited assertions, and conditional or empty-case verification.
- Check whether mocks replace the behavior under review and whether shared fixtures, mock history, or automatic retries hide a failure.
- Derive expected results from the contract. Review skips, focus filters, weakened assertions, and regenerated snapshots against any authorized requirement change.
- Inspect helpers and framework semantics before judging a smoke test, snapshot, interaction check, or type assertion.

The verification guidance incorporates lessons from Hollowtest. Its CLI is optional and must support the actual language and runner. Static diagnostics and scores are review evidence to investigate. Mutation probes use a disposable copy and a passing baseline, then distinguish meaningful assertion failures from equivalent mutations, compilation errors, timeouts, and incorrect test selection. The [verification guide](peer-review/references/verification.md) contains the detailed checks and execution boundaries.

### Independent review and models

A practical workflow is:

```text
Implementer -> project checks -> fresh reviewer -> validated findings
           <- focused fixes  <-                  |
           -> relevant checks -> re-review ------+
```

The reviewer receives requirements, actual source/snapshot access, contracts, and check evidence. It does not need the implementer's full conversation. A fresh session of the same capable model can provide independence; a different model may add diversity.

For example, use `gpt-6.1-sol` for implementation and `gpt-6-astra` for review when available in the host. Select the reviewer through model/session controls or authorized orchestration; installing this package does not select or change a model. Evaluate the arrangement on validated defects, material misses, false positives, time, and cost. No model-pair benchmark is claimed.

### Hosted review environments

Confirm how a managed reviewer receives instructions. Including only the body of `SKILL.md` does not transfer supporting references or execution capabilities. Claude's [managed Code Review customization](https://code.claude.com/docs/en/code-review-customize) can include skill text through its review policy but does not load supporting files. This differs from a local Claude Code session loading the complete directory. Supply needed guidance through that service's supported configuration and qualify coverage when references or execution are unavailable.

### Resources

| Resource | Purpose |
| --- | --- |
| [Entrypoint](peer-review/SKILL.md) | Scope, routing, evidence requirements, independence, and follow-up. |
| [Review method](peer-review/references/review-method.md) | Target selection, trusted policy, confidence, severity, coverage, and verdicts. |
| [Backend](peer-review/references/backend.md) | APIs, authorization, data, concurrency, failure recovery, and operations. |
| [Frontend](peer-review/references/frontend.md) | UI state, contracts, accessibility, browser boundaries, and performance. |
| [Android](peer-review/references/android.md) | Lifecycle, coroutines, Flow, Compose/Views, platform security, and release variants. |
| [Android/KMP test effectiveness](peer-review/references/android-testing.md) | Coroutine schedulers, Flow, Compose synchronization, restoration and target coverage. |
| [Verification](peer-review/references/verification.md) | Test effectiveness, assertion execution, false-positive checks, isolated mutation probes, model correspondence, performance claims, and evidence reporting. |
| [Independent review](peer-review/references/independent-review.md) | Fresh context, model selection, review lenses, and feedback loops. |
| [Report template](peer-review/assets/review-report-template.md) | Optional structure for substantial or saved reviews. |
| [Handoff template](peer-review/assets/review-handoff-template.md) | Factual packet for another reviewer or model. |
| [Source research](peer-review/references/sources.md) | Original sources, official guidance, and synthesis decisions. |
| [Evaluation scenarios](peer-review/evals/scenarios.md) | Calibration, scope, policy, host behavior, and validation records. |
| [OpenAI metadata](peer-review/agents/openai.yaml) | Optional Codex display metadata and example invocation. |

Android/KMP guidance also examines typed-result fallback/decoding semantics, dependency lifetimes and shared-platform boundaries. Test review distinguishes scheduler/clock ownership, conflated Flow states, device execution and actual OS restoration.

Load the review method and applicable references. Source research and evaluation cases are maintainer resources, not required context for every review. The package is an original synthesis, not an installer or runtime wrapper around upstream skills.

## Cybersecurity

**Version:** 1.5.2 · **Entrypoint:** [cybersec/SKILL.md](cybersec/SKILL.md)

Use Cybersecurity for explicit security assessments, threat modeling, secure implementation, hardening, and security readiness checks. It covers web/frontends, backend/APIs, desktop/native applications, Android/iOS, CI/CD, supply chains, cloud/IaC/containers, enterprise IT, and AI/agentic systems when present. It selects the relevant surfaces instead of running every checklist for every project.

### Modes and limits

Threat modeling produces assets, trust boundaries, credible abuse cases, controls, and planned verification. Repository audits inspect the current snapshot unless a narrower target is specified; they preserve reviewed files. Secure-build/hardening mode implements only security work already authorized and verifies affected controls. Readiness mode evaluates the requested gate, including detection, containment, recovery, and risk ownership.

No model or skill can predict every attack or establish invulnerability. Cybersecurity identifies supported vulnerabilities, credible threats, control gaps, and residual/unassessed risk. Source configuration, deployed controls, and runtime evidence are separate. Framework alignment or passing scans does not establish certification, compliance, or full release approval.

Live scans, exploitation, fuzzing, credential tests, shared-system testing, production changes, and external data transfers require authorization covering the specific actions, targets, methods, environment, and limits. Existing valid authorization is reused. An audit does not itself authorize fixes, installations, deployment, or secret/IAM changes.

### Example requests

```text
Use $cybersec to assess this repository's security controls and report findings and unreviewed areas. Keep the source unchanged.
Use $cybersec to threat-model the architecture in docs/project.md, including abuse cases and verification plans.
Use $cybersec to map this project's relevant threats to controls, tests, and gaps, including cross-component attack chains. Save the assessment to docs/security-assessment.md.
Use $cybersec to review this desktop app's IPC, local-file access, installer, and update boundaries.
Use $cybersec to review the Android and iOS release configuration and API trust boundaries.
Use $cybersec to assess CI/CD, dependencies, IaC, cloud IAM, and container isolation without live scans.
Use $cybersec to review IT identity, endpoint, network, and recovery policies; distinguish policy from operational evidence.
Use $cybersec to implement the approved fixes for SEC-001 and SEC-002 in this local test environment, then verify them.
Use $cybersec to re-assess the requested release-security gate and write docs/security-assessment.md.
```

### Coverage and findings

Substantial reports include the selected target/snapshot, relevant baseline/versions, credible threats, evidence-backed findings, and control coverage. Each relevant area is marked Assessed, Partially assessed, Not assessed, or Not applicable with a reason. Findings distinguish impact-based priority from confidence, test results, and treatment state; a changed but unverified fix is not a resolved vulnerability. Hypotheses remain investigation items rather than confirmed defects.

The coverage map connects material threats to controls, verification evidence, residual gaps, and responsible next actions. It considers attacks that combine weaknesses across components and tests whether fixes block unauthorized effects while preserving legitimate behavior. Reassess affected coverage after meaningful system or threat changes. Narrow reviews stay concise; the skill does not impose a full matrix on every change, assign an invented security score, or start continuous monitoring.

Mobile guidance also covers packaged configuration versus privileged secrets, credential storage/backups, HTTP logging, trusted destinations and refresh/logout races across actual platform implementations.

Concrete traces connect attacker-controlled input, the protected resource and rule, actual enforcement, effects, and counterevidence. Mechanism checks include queued work and caches after permission changes, concurrent one-use actions, resource limits before allocation, native length arithmetic, password hashing, token lifecycle, and cryptographic library use. Authorization checks pair an existing protected resource and an allowed actor with the prohibited case, then inspect data and side effects after denial.

The assessment can conclude `Action required`, `No blocking findings` within completed agreed coverage, or `Incomplete` when material evidence is missing. Zero findings is valid. Reports and filled templates belong in the target project or requested location; report files are written only when requested or required by the calling workflow. Without project artifacts, the output is a plan or scoped threat model rather than a fabricated audit.

The skill was informed by Silva97's [Bem-vindo ao ciberapocalipse](https://www.tabnews.com.br/Silva97/bem-vindo-ao-ciberapocalipse) and accessible related material, with technical guidance checked against primary NIST, OWASP, and platform sources. Opinionated article claims are not treated as standards. See [source notes](cybersec/references/sources.md) for access limits and [third-party notices](THIRD-PARTY-NOTICES.md) for attribution.

### Resources

| Resource | Purpose |
| --- | --- |
| [Entrypoint](cybersec/SKILL.md) | Modes, authority, target scope, routing, and working loop. |
| [Assessment method](cybersec/references/assessment-method.md) | Threat reasoning, repository baseline, evidence, severity/status, coverage, and conclusions. |
| [Threat coverage and verification](cybersec/references/threat-coverage.md) | Traceable coverage, combined attack paths, negative/positive checks, structural guarantees, security-model limits, and reassessment triggers. |
| [Web and API](cybersec/references/web-api.md) | Browser/service trust, authorization, business logic, inputs, and data. |
| [Credential and cryptographic controls](cybersec/references/web-api.md#credentials-and-cryptographic-controls) | Passwords, security tokens, encryption, and key handling across relevant platforms. |
| [Desktop and native](cybersec/references/desktop-native.md) | IPC/bridges, file access, privileged helpers, distribution, updates, and native boundaries. |
| [Mobile](cybersec/references/mobile.md) | Android/iOS release, platform, storage, network, and inter-app boundaries. |
| [DevOps and supply chain](cybersec/references/devops-supply-chain.md) | Dependencies, CI/build/artifact trust, cloud, IaC, containers, and Kubernetes. |
| [IT operations](cybersec/references/it-operations.md) | Assets, enterprise identities, endpoints, networks, incident readiness, and recovery. |
| [AI and agentic systems](cybersec/references/ai-agentic.md) | Prompt/tool boundaries, retrieval/memory isolation, unsafe output, and action scope. |
| [Assessment template](cybersec/assets/security-assessment-template.md) | Adaptable threat/control/finding/evidence report. |
| [Source notes](cybersec/references/sources.md) | Article attribution, primary sources, adaptation decisions, and unavailable readings. |
| [Evaluation scenarios](cybersec/evals/scenarios.md) | Discovery, platform/CI/IT risks, guard controls, authorization, evidence, and validation records. |
| [OpenAI metadata](cybersec/agents/openai.yaml) | Optional host display metadata and invocation prompt; no model selection. |

## UI Design

**Version:** 1.5.2 · **Entrypoint:** [ui-design/SKILL.md](ui-design/SKILL.md)

Use UI Design to discover, specify, refine, review, or implement screens and multi-screen journeys. A shared method covers task completion, hierarchy, content, components, states, accessibility and evidence; conditional references handle web and native Android (Compose/Views). Other platforms use the common method and actual official framework guidance with explicit coverage limits.

### Examples and output

```text
Use $ui-design to interview me about this Android app's onboarding and home screens and save the specification to docs/ui-design.md.
Use $ui-design to add the offline editing flow to the existing screen specification, preserving accepted decisions.
Use $ui-design to review this web checkout's keyboard interaction, errors and responsive layout; record findings in docs/ui-design.md.
Use $ui-design to implement UI-S03 using the project's existing components, verify the affected flow and update docs/ui-design.md.
Use $ui-design to compare two visual directions for the same search screen and create an optional offline state gallery, keeping docs/ui-design.md authoritative.
```

Feedback guidance chooses field, form, transient, persistent, content-area or decision surfaces by task consequence, retaining usable content and truthful recovery. Compose guidance covers component contracts, state ownership, previews and shared/platform resources without imposing MVI or a DI library.

The default output is the target project's cumulative **`docs/ui-design.md`**, with a screen index, shared visual/interaction rules, flows, per-screen contracts, decision status, acceptance scenarios, verification evidence and a resume pointer. It is saved during partial interviews and updated across iterations. Additional mockups or assets are optional linked evidence. A request to specify screens produces documentation; implementation follows the user's requested scope.

When PentaPRO files exist, this UI document supplements their five pillars and links canonical requirements, checks, architecture and process records. Existing design systems remain authoritative for their owned tokens/components. The skill has no mandatory dependency on the other skills, BMAD, OpenSpec, Figma, a browser plugin, image generation or a paid service. Runtime checks require available project tools; HTML concepts do not prove Android behavior. Research observations, proposals, accepted decisions and executed checks remain distinct. No production usability or cross-model efficiency benchmark is claimed.

An optional standard-library Python helper checks explicitly declared token contrast pairs and builds local HTML state galleries from editable sources. These concepts support named screen/state/theme/window links and token-derived specimens without remote font/icon services or automatic publication. Existing project formats, native previews and browser tooling remain valid alternatives. See the [prototype workflow](ui-design/references/prototyping.md); calculated pairs and HTML concepts do not establish accessibility conformance or native runtime correctness.

### UI Design resources

| Resource | Purpose |
| --- | --- |
| [Entrypoint](ui-design/SKILL.md) | Modes, routing, scope and working loop. |
| [Design method](ui-design/references/design-method.md) | Discovery, task/flow coverage, screen contracts, content and recovery. |
| [Visual system](ui-design/references/visual-system.md) | Tokens, identity, typography, graphic assets, charts and motion. |
| [Web](ui-design/references/web.md) | Browser layout, navigation, semantics and checks. |
| [Android](ui-design/references/android.md) | Compose/Views and conditional implementation procedures for components, presentation, architecture and navigation. |
| [Feedback and state coverage](ui-design/references/feedback-states.md) | Error surfaces, partial failures, refresh/pagination, control variants and stress states. |
| [Validation](ui-design/references/validation.md) | Rendered inspection, reproducible journeys, durable outcomes, usability and evidence limits. |
| [Document maintenance](ui-design/references/document-maintenance.md) | Cumulative updates, stable IDs, ownership and resumption. |
| [Output template](ui-design/assets/ui-design-template.md) | Adaptable single-file screen and flow specification. |
| [Prototype workflow](ui-design/references/prototyping.md) | Optional token checks, local state galleries, direction comparison and reproducible review. |
| [Prototype tools](ui-design/scripts/prototype_tools.py) | Original local checker/builder; no external runtime packages required. |
| [Prototype starter](ui-design/assets/prototype/manifest.json) | Synthetic editable gallery inputs, not a production design system. |
| [Design consolidation](ui-design/references/design-consolidation.md) | File-by-file transfer and exclusions from the retired local design skill. |
| [Worked example](ui-design/references/worked-example.md) | Two-screen Android specification with explicit pending decisions. |
| [Source research](ui-design/references/sources.md) | Repository coverage, pinned sources, adaptations and research limits. |
| [Evaluation scenarios](ui-design/evals/scenarios.md) | Realistic cases and validation record. |
| [OpenAI metadata](ui-design/agents/openai.yaml) | Optional host presentation and invocation prompt. |

## Native Android implementation and testing

These helpers implement concrete native Kotlin/JVM/Android changes. They do not create another specification or assessment workflow. Design and implement Android screens through UI Design's conditional Compose/presentation/navigation references; assess Android security through Cybersecurity's Android controls. Review source and test effectiveness through Peer Review. [Ownership and every source destination](SKILL-ROUTING.md) explain the boundaries.

| Helper | Example request | Main supporting resources |
| --- | --- | --- |
| [android-module-structure](android-module-structure/SKILL.md) | Add the approved notes data module using the existing Gradle conventions. | [Build logic](android-module-structure/references/build-logic.md), [execution](android-module-structure/references/execution.md), [maintenance cases](android-module-structure/evals/scenarios.md) |
| [android-data-layer](android-data-layer/SKILL.md) | Implement atomic refresh while retaining cached notes after failure. | Repository/storage/transport procedures and typed-domain examples in the entrypoint |
| [android-error-handling](android-error-handling/SKILL.md) | Implement cancellation-preserving HTTP error mapping with TLS failures distinguished. | Typed Result and Ktor boundary examples in the entrypoint |
| [android-di-koin](android-di-koin/SKILL.md) | Wire the existing repository and destination ViewModel with the correct owner. | Binding, startup and lifetime procedures in the entrypoint |
| [android-background](android-background/SKILL.md) | Implement an account-scoped idempotent synchronization worker. | WorkManager retry/initialization and Koin procedures in the entrypoint |
| [android-unit-testing](android-unit-testing/SKILL.md) | Write a deterministic test for a delayed refresh cancelled during logout. | [Case catalogue](android-unit-testing/references/test-cases.md), [Notes fake](android-unit-testing/references/notes-fake.md) |
| [android-integration-testing](android-integration-testing/SKILL.md) | Write the Room migration/data-preservation test for this schema update. | Native boundary, storage and transport test procedures in the entrypoint |
| [android-ui-testing](android-ui-testing/SKILL.md) | Write a device test for the retry button and retained content. | Native host, selectors, scheduling and cleanup procedures in the entrypoint |

Implementation results are source/configuration changes and proportionate executed checks, with missing SDK/device/service evidence disclosed. Existing stacks, versions, supported behavior and user authorization govern the work. These packages do not add iOS/Desktop targets, start a UI redesign or run independent audits merely because code is Android-specific. Cross-package links help when companions are installed; each helper retains essential local instructions and uses project-owned contracts otherwise.

## PR Quiz

[pr-quiz](pr-quiz/SKILL.md) creates an explicitly requested decision-comprehension quiz for a specific GitHub PR. It is generic across platforms and separate from Peer Review: passing questions does not establish defect freedom, security or independent approval. Creating a PR alone never activates it.

Example: `Use $pr-quiz to draft a quiz about the caching and retry decisions in PR 123.` Drafting stays local; publishing requires the requested PR-edit scope. The [Python helper](pr-quiz/scripts/publish_quiz.py) previews with `--dry-run` without GitHub access, then can preserve surrounding PR text while publishing through `gh` when authorized. Resolve its installed path in the target repository.

The [optional workflow asset](pr-quiz/assets/pr-quiz.yml) grades through trusted GitHub metadata events, without running PR-head code. It is not installed as an active workflow here. Authors are ineligible by default; passes bind to quiz ID and head SHA. Adapt reviewer/team policy, reviewed action pinning, token permissions and actual repository rules before enabling it. Merge queues/custom policies need their own integration checks. The answer key is public encoding, so this is not a security or tamper-proof approval boundary. Test setup in a controlled repository before relying on a required status.

Offline maintainer checks: `PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s pr-quiz/scripts/tests -v` and `node pr-quiz/scripts/tests/workflow.cjs`. They exercise rendering/body preservation and the actual embedded grader with API doubles; they do not validate a live GitHub deployment or branch rule.

## Project AGENTS.md template

[AGENTS-template.md](AGENTS-template.md) is a reusable working guide for AI agents, separate from the skills. Copy it to a target project's root as `AGENTS.md`, fill in the project facts, navigation, actual commands, and decision authority, and remove or mark inapplicable entries. Preserve an existing project's guidance rather than replacing it blindly.

The template supplies general rules for scoped work, implementation, validation, test-effectiveness review, security, collaboration, and handoff. It routes work to `penta-pro`, `ui-design`, `peer-review`, and `cybersec`, identifies the five pillar documents plus the cumulative UI specification, and explains ownership, resumption and evidence states. Optional Android implementation/test helpers and PR Quiz have separate task boundaries in the routing table. Fill in actual skill locations and commands; copying the template does not install the packages or require all four on every task. It leaves the stack, source layout, model and test framework to the project. Its artifact-language default is English, with exceptions for required identifiers, literal data, and localization. Keep detailed specifications and runbooks in their own authoritative documents and link them from the project guide.

## Repository structure

Each skill lives directly under this repository's root and follows the [Agent Skills specification](https://agentskills.io/specification). There is no additional nested `skills/` directory. Shared usage documentation and licensing live at the root.

```text
skills/
├── README.md
├── LICENSE
├── THIRD-PARTY-NOTICES.md
├── AGENTS-template.md
├── SKILL-ROUTING.md
├── android-module-structure/
├── android-data-layer/
├── android-error-handling/
├── android-di-koin/
├── android-background/
├── android-unit-testing/
├── android-integration-testing/
├── android-ui-testing/
├── pr-quiz/
├── penta-pro/
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/
│   │   ├── penta-pro-template.md
│   │   ├── product.md
│   │   ├── proof.md
│   │   ├── project.md
│   │   ├── production.md
│   │   └── process.md
│   ├── evals/
│   └── references/
├── peer-review/
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/
│   ├── evals/
│   └── references/
├── cybersec/
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/
│   ├── evals/
│   └── references/
└── ui-design/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── evals/
    ├── references/
    └── scripts/
```

`SKILL.md` contains required metadata and runtime instructions. Optional `agents/` files adapt host presentation; `assets/` holds output templates; `references/` holds conditional detail; `evals/` holds maintenance cases and validation records; `scripts/` holds optional executable helpers and their focused tests. Create only the directories a skill needs.

## Maintenance and new skills

Authoring was checked against [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills) and [Anthropic's best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) on 2026-10-25. These are maintainer references, not runtime dependencies. Recheck relevant guidance when changing packaging, discovery, or model support; evaluate upstream changes deliberately rather than importing them automatically.

### Validation and improvement

The pstack-informed update adds caller-facing contract sketches and verification recipes to PentaPRO, safety-premise and measurement checks to Peer Review, model/enforcement distinctions to Cybersecurity, and instance-aware journey evidence to UI Design. These additions are conditional; the skills keep their existing output contracts and introduce no pstack dependency. [Research attribution and limits](THIRD-PARTY-NOTICES.md#cursor-pstack-research) identify the pinned source and adaptations.

Use each skill's evaluation cases before expanding its instructions. Compare matched tasks with and without the skill on the models and hosts actually used. Check activation, preserved decisions, invented facts, unnecessary questions, substantiated defects, false positives, material misses, coverage honesty, and unintended actions. Record actual time and usage when available, and retest after relevant model or instruction changes.

The collection review on 2026-11-06 strengthened handoffs across all 13 skills, retained project-owned contracts and made sample stacks conditional. Android corrections clarify Koin worker parameters, periodic-work termination, account-scoped commit races, pure StateFlow updates and version-sensitive build/test configuration. The optional PR quiz now separates reflected text from bot control markers, rejects ambiguous blocks/keys, renders question text literally and pins its action dependency to an official release commit with narrower permissions. Its grading remains an educational aid. Existing guidance covers safe test execution, staged versus working-file review, type/model limits, design fidelity and companion-document ownership. See the [validation scope and maintenance record](SKILL-ROUTING.md#validation-scope) for actual results and remaining limits; these checks do not establish reliability on every model.

The closing audit additionally corrected external specification/task ownership, effective built-in Kotlin mode, literal-query and update/cascade semantics, final-write account isolation, conditional Android UI examples and strict JSON input handling in both helpers. Regression checks and a bounded PentaPRO forward trial are recorded in [the closure audit](SKILL-ROUTING.md#closing-audit-after-sdd-and-layered-review-integration--2026-11-06). These changes clarify concrete decisions and failure modes without adding mandatory stages or another framework dependency.

Keep active versions in `SKILL.md`, this README, and any versioned output template aligned. When behavior changes, reconcile descriptions, UI metadata, templates, references, and evaluation cases. Validate local links and anchors from each file's location. Retain historical research dates and trial versions with their original scope; a package update does not rerun or broaden earlier evidence.

Where present, evaluation files and executable tests record the package's actual cases, audits/trials and limitations. A package without a recorded trial has no implied behavioral evaluation. Shorter documents and structural checks do not prove better task performance. No cross-model accuracy, cost, or efficiency benchmark is claimed. Prefer focused corrections supported by observed failures over universal rules for isolated cases.

### Adding a new skill

1. Create a root-level directory whose name matches the skill's `name`, using lowercase letters and hyphens.
2. Add `SKILL.md` with a clear description, focused instructions, and only the supporting resources the workflow needs.
3. Add an entry to [Available skills](#available-skills) and a dedicated section in this README covering purpose, example requests, output/boundaries, and resource links. Keep shared installation and maintenance guidance in their common sections.
4. Keep README and LICENSE files at repository root. Preserve applicable third-party notices where needed, validate metadata and internal links, and run meaningful evaluation cases before claiming improvements.

## License and attribution

Repository-original work uses the root [MIT License](LICENSE). The Android/PR-quiz source material is attributed to Philipp Lackner and PL Coding; no bundle-specific redistribution license was supplied or established, and the repository license does not relicense it. See [third-party notices](THIRD-PARTY-NOTICES.md#pl-coding-android-and-pr-quiz-skills) for provenance and limits. Skill directories do not contain duplicate LICENSE or README files.

When copying or redistributing individual skills, retain the repository-level license notice and applicable third-party notices with the distributed material.

The source research for [PentaPRO](penta-pro/references/sources.md), [Peer Review](peer-review/references/sources.md), [Cybersecurity](cybersec/references/sources.md), and [UI Design](ui-design/references/sources.md) records their inputs and adaptation decisions. [Third-party notices](THIRD-PARTY-NOTICES.md) preserve upstream attribution; the repository license does not relicense external articles. Attribution does not imply affiliation, endorsement, or a runtime dependency.
