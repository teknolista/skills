# ✨ AI Agent Skills

My personal collection of reusable skills for developers building software with AI coding agents. PENTA-PRO turns intent into an actionable specification; Code Review checks implementation against requirements and concrete evidence; Cybersec assesses security risks and controls across software, DevOps, and IT systems. UI/UX turns requirements into screen and interaction specifications for web and Android, with authorized implementation and verification. Each skill can be used independently.

All skill instructions and generated artifacts are in English. Conversation can use the user's preferred language.

## Contents

- [✨ AI Agent Skills](#-ai-agent-skills)
  - [Contents](#contents)
  - [Available skills](#available-skills)
  - [Installation and activation](#installation-and-activation)
  - [Agent and model compatibility](#agent-and-model-compatibility)
    - [Native skill locations](#native-skill-locations)
    - [Required capabilities](#required-capabilities)
    - [Model selection and validation](#model-selection-and-validation)
  - [PENTA-PRO](#penta-pro)
    - [The five pillars](#the-five-pillars)
    - [Example requests](#example-requests)
    - [Output and working boundaries](#output-and-working-boundaries)
    - [Resources](#resources)
  - [Code Review](#code-review)
    - [Example requests](#example-requests-1)
    - [Findings, verdicts, and boundaries](#findings-verdicts-and-boundaries)
    - [Test effectiveness](#test-effectiveness)
    - [Independent review and models](#independent-review-and-models)
    - [Hosted review environments](#hosted-review-environments)
    - [Resources](#resources-1)
  - [Cybersec](#cybersec)
    - [Modes and limits](#modes-and-limits)
    - [Example requests](#example-requests-2)
    - [Coverage and findings](#coverage-and-findings)
    - [Resources](#resources-2)
  - [UI/UX](#uiux)
    - [Examples and output](#examples-and-output)
    - [UI/UX resources](#uiux-resources)
  - [Project AGENTS.md template](#project-agentsmd-template)
  - [Repository structure](#repository-structure)
  - [Maintenance and new skills](#maintenance-and-new-skills)
    - [Validation and improvement](#validation-and-improvement)
    - [Adding a new skill](#adding-a-new-skill)
  - [License and attribution](#license-and-attribution)

## Available skills

| Skill | Version | Purpose |
| --- | --- | --- |
| [PENTA-PRO](#penta-pro) | 2.4.1 | Explore, create, resume, update, or review software specifications across PRODUCT, PROOF, PROJECT, PRODUCTION, and PROCESS. |
| [Code Review](#code-review) | 1.5.1 | Review backend, frontend, Android, and test code for substantiated defects and meaningful regression protection. |
| [Cybersec](#cybersec) | 1.3.1 | Model threats, assess security controls, and verify authorized hardening across web/API, desktop/mobile, DevOps, cloud, and IT projects. |
| [UI/UX](#uiux) | 1.1.1 | Specify, refine, review, and implement web and Android screens; maintain cumulative `docs/ui-ux.md`. |

## Installation and activation

Copy the complete directory of each desired skill into the skills location supported by your agent. Preserve its internal relative paths. For a Codex project, the installed entrypoints are:

```text
your-project/.agents/skills/penta-pro/SKILL.md
your-project/.agents/skills/code-review/SKILL.md
your-project/.agents/skills/cybersec/SKILL.md
your-project/.agents/skills/ui-ux/SKILL.md
```

A skill stored in this repository is not automatically installed into other projects. Codex discovers repository skills from `.agents/skills/`; if a copied skill does not appear, restart the session. Other hosts use their own discovery locations and invocation syntax. See [agent and model compatibility](#agent-and-model-compatibility) for documented locations, capabilities, and integration limits.

The skills support automatic selection for matching tasks. In Codex, mention `$penta-pro`, `$code-review`, `$cybersec`, or `$ui-ux` to select one explicitly. Their `agents/openai.yaml` files provide optional display metadata and default prompts; they do not select a model. Select models through the host's controls or authorized orchestration.

The packages use Markdown instructions, references, and templates. No skill requires another skill, a plugin, paid service, API key, external connector, or bundled script runtime. Actual work still requires relevant project access and whatever tools its requested checks need. Saving a specification or report requires a writable destination. Installing a skill does not supply those capabilities or authorize additional actions.

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
| PENTA-PRO creation/update | User intent, relevant existing context, package assets, and a writable requested destination | Ask only consequential missing questions; retain proposals and blockers. If writing is unavailable, return the draft and disclose that it was not saved. |
| PENTA-PRO review | The actual specification and relevant authoritative context | Report missing material rather than treating an absent document as ready. |
| UI/UX specification and implementation | Relevant requirements/design context and a writable target project; source/toolchain for implementation, browser or Android environment for runtime checks | Save a partial specification and mark pending decisions/checks; never claim rendered, device, accessibility or user validation without evidence. |
| Code inspection | Actual selected source/snapshot, relevant requirements/contracts, and applicable references | Report material missing coverage; do not infer a clean review from a description alone. |
| Cybersec assessment | Authorized target/snapshot, relevant security requirements, applicable domain references, and evidence of the controls being claimed | Separate source/configuration from deployed/runtime evidence; mark inaccessible areas and avoid security or compliance guarantees. |
| Executed verification | The project's actual tools and isolated data/environment | Label unexecuted checks and distinguish static conclusions from runtime evidence. |
| Independent review | A separate reviewer/session with actual source access | Disclose self-review or prepare a factual handoff; do not claim independence from a model label. |

Git, shell execution, browsers, Android SDKs, credentials, connectors, and additional agents are not supplied by installing a skill. Git is useful for comparisons, but an explicitly selected source snapshot can be reviewed without it. The skills can be used independently. Cybersec live testing and remediation require actual target/action authorization; capability does not imply permission.

Managed review services may load only instruction text. See [Hosted review environments](#hosted-review-environments) for supporting-file and execution limits.

### Model selection and validation

The skills include concrete behavior traces, failure examples, and evidence checks to reduce reliance on unstated engineering knowledge. For larger tasks, retain the target snapshot, reviewed and pending areas, evidence, unresolved questions, and next action. Reopen relevant source after context loss or a changed snapshot. Validate representative tasks on each intended model and host before relying on its results.

The workflows have no hard-coded model, reasoning setting, vendor tool name, or mandatory orchestration mechanism. `agents/openai.yaml` in these packages contains display metadata and a default prompt; it does not select a model. Hosts may offer their own model overrides. Use those controls deliberately rather than adding a vendor-specific override to the portable core.

Choose a currently available model with sufficient reasoning, domain competence, context capacity, and reliable tool use for the task. Escalate difficult requirements or review risks when evidence warrants it. The documented [OpenAI model options](https://learn.chatgpt.com/docs/models) include the repository's example implementation/review pairing; availability and suitability depend on the host/account and observed results. A model name is not a quality gate.

After changing host, model, or significant instructions, run the relevant [PENTA-PRO cases](penta-pro/evals/scenarios.md), [code-review cases](code-review/evals/scenarios.md), [cybersec cases](cybersec/evals/scenarios.md), and [UI/UX cases](ui-ux/evals/scenarios.md). Check correct activation, preserved user decisions, meaningful defects versus false positives, honest evidence/coverage, and unintended edits. Compare matched tasks before claiming better accuracy, cost, or latency. Official format support does not establish a cross-vendor performance benchmark.

## PENTA-PRO

**Version:** 2.4.1 · **Entrypoint:** [penta-pro/SKILL.md](penta-pro/SKILL.md)

Use PENTA-PRO when defining a product, specifying a substantial feature, maintaining an existing PENTA-PRO document, or checking whether the next increment is ready for development. It uses existing project information and asks about consequential gaps. Ordinary coding tasks and small, clear specification updates do not restart a full interview.

An exploration-only request stays in the conversation until the user asks to capture the findings. For a material change, PENTA-PRO compares the proposal with the current requirements and behavior, identifies compatibility commitments, and traces their effects across the pillars. Applicable project rules and amendments are linked from PROCESS.

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

Creation saves all five initial drafts before pausing for answers. Later rounds update the affected records, with stable IDs and links to their authoritative definitions. PROCESS records an `In progress` state for material updates across files and a `Consistent` state after reconciliation. Resumption inspects actual contents and completes any interrupted update. Proposed changes retain their baseline, compatibility commitments, and separate status until settled.

The skill distinguishes confirmed information, proposals, and pending decisions. Routine decisions made within explicit delegation are attributed to the agent and can be settled for readiness without being presented as user requirements or document acceptance. When the user is unavailable, retain consequential blockers and complete independent specification work. If saving is unavailable, return an explicitly unsaved draft.

PENTA-PRO drafts from accessible evidence and delegated choices with provenance. It identifies unresolved research, baselines, legal applicability, approvals, and test evidence. The interview targets consequential missing decisions. All five pillars remain, with coverage recorded as included, linked, pending, deferred, or not applicable. Larger specifications can link feature details, increment plans, and contracts from their owning pillar. The skill loads specialized forms and examples as needed.

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

## Code Review

**Version:** 1.5.1 · **Entrypoint:** [code-review/SKILL.md](code-review/SKILL.md)

Use Code Review for backend services, frontend applications, Android software, and the effectiveness of their tests. It supports local edits, selected files or snippets, pull requests, commit comparisons, independent second opinions, and re-review after fixes. Reports separate substantiated defects, verification gaps, optional improvements, and remaining release requirements.

### Example requests

```text
Use $code-review to review all my uncommitted changes, including new files.
Use $code-review to review this branch against origin/main, including the local edits.
Use $code-review to review the selected PR against the requirements and checks in docs/product.md and docs/proof.md.
Use $code-review to review the changed tests for assertions that would miss the regressions they claim to detect.
Use $code-review to review the Android release changes, focusing on lifecycle and data migration.
Use $code-review to re-review the fixes for CR-001 and CR-002 on the current revision.
Use $code-review to prepare a handoff for an independent reviewer in another session.
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

The reviewer follows consequential behavior from its contract through entry points, guards, effects, and consumers. Concrete inputs and event order help investigate authorization, races, retries, and stale asynchronous results. Existing protections and unknown premises are checked before retaining a finding.

### Test effectiveness

Code Review examines the tests relied on for changed behavior, including their discovery, fixtures, real subject, assertions, and completion. It asks which realistic wrong behavior would still pass.

- Inspect tautologies, unused matchers, swallowed failures, unawaited assertions, and conditional or empty-case verification.
- Check whether mocks replace the behavior under review and whether shared fixtures, mock history, or automatic retries hide a failure.
- Derive expected results from the contract. Review skips, focus filters, weakened assertions, and regenerated snapshots against any authorized requirement change.
- Inspect helpers and framework semantics before judging a smoke test, snapshot, interaction check, or type assertion.

The verification guidance incorporates lessons from Hollowtest. Its CLI is optional and must support the actual language and runner. Static diagnostics and scores are review evidence to investigate. Mutation probes use a disposable copy and a passing baseline, then distinguish meaningful assertion failures from equivalent mutations, compilation errors, timeouts, and incorrect test selection. The [verification guide](code-review/references/verification.md) contains the detailed checks and execution boundaries.

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
| [Entrypoint](code-review/SKILL.md) | Scope, routing, evidence requirements, independence, and follow-up. |
| [Review method](code-review/references/review-method.md) | Target selection, trusted policy, confidence, severity, coverage, and verdicts. |
| [Backend](code-review/references/backend.md) | APIs, authorization, data, concurrency, failure recovery, and operations. |
| [Frontend](code-review/references/frontend.md) | UI state, contracts, accessibility, browser boundaries, and performance. |
| [Android](code-review/references/android.md) | Lifecycle, coroutines, Flow, Compose/Views, platform security, and release variants. |
| [Android/KMP test effectiveness](code-review/references/android-testing.md) | Coroutine schedulers, Flow, Compose synchronization, restoration and target coverage. |
| [Verification](code-review/references/verification.md) | Test effectiveness, assertion execution, false-positive checks, isolated mutation probes, and evidence reporting. |
| [Independent review](code-review/references/independent-review.md) | Fresh context, model selection, review lenses, and feedback loops. |
| [Report template](code-review/assets/review-report-template.md) | Optional structure for substantial or saved reviews. |
| [Handoff template](code-review/assets/review-handoff-template.md) | Factual packet for another reviewer or model. |
| [Source research](code-review/references/sources.md) | Original sources, official guidance, and synthesis decisions. |
| [Evaluation scenarios](code-review/evals/scenarios.md) | Calibration, scope, policy, host behavior, and validation records. |
| [OpenAI metadata](code-review/agents/openai.yaml) | Optional Codex display metadata and example invocation. |

Android/KMP guidance also examines typed-result fallback/decoding semantics, dependency lifetimes and shared-platform boundaries. Test review distinguishes scheduler/clock ownership, conflated Flow states, device execution and actual OS restoration.

Load the review method and applicable references. Source research and evaluation cases are maintainer resources, not required context for every review. The package is an original synthesis, not an installer or runtime wrapper around upstream skills.

## Cybersec

**Version:** 1.3.1 · **Entrypoint:** [cybersec/SKILL.md](cybersec/SKILL.md)

Use Cybersec for explicit security assessments, threat modeling, secure implementation, hardening, and security readiness checks. It covers web/frontends, backend/APIs, desktop/native applications, Android/iOS, CI/CD, supply chains, cloud/IaC/containers, enterprise IT, and AI/agentic systems when present. It selects the relevant surfaces instead of running every checklist for every project.

### Modes and limits

Threat modeling produces assets, trust boundaries, credible abuse cases, controls, and planned verification. Repository audits inspect the current snapshot unless a narrower target is specified; they preserve reviewed files. Secure-build/hardening mode implements only security work already authorized and verifies affected controls. Readiness mode evaluates the requested gate, including detection, containment, recovery, and risk ownership.

No model or skill can predict every attack or establish invulnerability. Cybersec identifies supported vulnerabilities, credible threats, control gaps, and residual/unassessed risk. Source configuration, deployed controls, and runtime evidence are separate. Framework alignment or passing scans does not establish certification, compliance, or full release approval.

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
| [Threat coverage and verification](cybersec/references/threat-coverage.md) | Traceable coverage, combined attack paths, negative/positive checks, and reassessment triggers. |
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

## UI/UX

**Version:** 1.1.1 · **Entrypoint:** [ui-ux/SKILL.md](ui-ux/SKILL.md)

Use UI/UX to discover, specify, refine, review, or implement screens and multi-screen journeys. A shared method covers task completion, hierarchy, content, components, states, accessibility and evidence; conditional references handle web and native Android (Compose/Views). Other platforms use the common method and actual official framework guidance with explicit coverage limits.

### Examples and output

```text
Use $ui-ux to interview me about this Android app's onboarding and home screens and save the specification to docs/ui-ux.md.
Use $ui-ux to add the offline editing flow to the existing screen specification, preserving accepted decisions.
Use $ui-ux to review this web checkout's keyboard interaction, errors and responsive layout; record findings in docs/ui-ux.md.
Use $ui-ux to implement UI-S03 using the project's existing components, verify the affected flow and update docs/ui-ux.md.
```

Feedback guidance chooses field, form, transient, persistent, content-area or decision surfaces by task consequence, retaining usable content and truthful recovery. Compose guidance covers component contracts, state ownership, previews and shared/platform resources without imposing MVI or a DI library.

The default output is the target project's cumulative **`docs/ui-ux.md`**, with a screen index, shared visual/interaction rules, flows, per-screen contracts, decision status, acceptance scenarios, verification evidence and a resume pointer. It is saved during partial interviews and updated across iterations. Additional mockups or assets are optional linked evidence. A request to specify screens produces documentation; implementation follows the user's requested scope.

When PENTA-PRO files exist, this UI document supplements their five pillars and links canonical requirements, checks, architecture and process records. Existing design systems remain authoritative for their owned tokens/components. The skill has no mandatory dependency on the other skills, BMAD, OpenSpec, Figma, a browser plugin, image generation or a paid service. Runtime checks require available project tools; HTML concepts do not prove Android behavior. Research observations, proposals, accepted decisions and executed checks remain distinct. No production usability or cross-model efficiency benchmark is claimed.

### UI/UX resources

| Resource | Purpose |
| --- | --- |
| [Entrypoint](ui-ux/SKILL.md) | Modes, routing, scope and working loop. |
| [Design method](ui-ux/references/design-method.md) | Discovery, task/flow coverage, screen contracts, content and recovery. |
| [Visual system](ui-ux/references/visual-system.md) | Tokens, identity, typography, graphic assets, charts and motion. |
| [Web](ui-ux/references/web.md) | Browser layout, navigation, semantics and checks. |
| [Android](ui-ux/references/android.md) | Compose/Views, adaptive layout, state, Back, insets and native checks. |
| [Feedback and state coverage](ui-ux/references/feedback-states.md) | Error surfaces, partial failures, refresh/pagination, control variants and stress states. |
| [Validation](ui-ux/references/validation.md) | Rendered inspection, interaction tests, usability and evidence limits. |
| [Document maintenance](ui-ux/references/document-maintenance.md) | Cumulative updates, stable IDs, ownership and resumption. |
| [Output template](ui-ux/assets/ui-ux-template.md) | Adaptable single-file screen and flow specification. |
| [Worked example](ui-ux/references/worked-example.md) | Two-screen Android specification with explicit pending decisions. |
| [Source research](ui-ux/references/sources.md) | Repository coverage, pinned sources, adaptations and research limits. |
| [Evaluation scenarios](ui-ux/evals/scenarios.md) | Realistic cases and validation record. |
| [OpenAI metadata](ui-ux/agents/openai.yaml) | Optional host presentation and invocation prompt. |

## Project AGENTS.md template

[AGENTS-template.md](AGENTS-template.md) is a reusable working guide for AI agents, separate from the skills. Copy it to a target project's root as `AGENTS.md`, fill in the project facts, navigation, actual commands, and decision authority, and remove or mark inapplicable entries. Preserve an existing project's guidance rather than replacing it blindly.

The template supplies general rules for scoped work, implementation, validation, test-effectiveness review, security, collaboration, and handoff. It does not prescribe a stack, folder layout, model, skill dependency, or test framework. Its artifact-language default is English, with exceptions for required identifiers, literal data, and localization. Keep detailed specifications and runbooks in their own authoritative documents and link them from the project guide.

## Repository structure

Each skill lives directly under this repository's root and follows the [Agent Skills specification](https://agentskills.io/specification). There is no additional nested `skills/` directory. Shared usage documentation and licensing live at the root.

```text
skills/
├── README.md
├── LICENSE
├── THIRD-PARTY-NOTICES.md
├── AGENTS-template.md
├── docs/research/              # Maintainer source assessments
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
├── code-review/
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
└── ui-ux/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── evals/
    └── references/
```

`SKILL.md` contains required metadata and runtime instructions. Optional `agents/` files adapt host presentation; `assets/` holds output templates; `references/` holds conditional detail; `evals/` holds maintenance cases and validation records. Create only the directories a skill needs.

The [PL Coding bundle assessment](docs/research/pl-coding-bundle.md) records the Android/KMP lessons incorporated across all four skills, provenance limits and concrete reasons some upstream prescriptions were excluded.

## Maintenance and new skills

Authoring was checked against [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills) and [Anthropic's best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) on 2026-10-25. These are maintainer references, not runtime dependencies. Recheck relevant guidance when changing packaging, discovery, or model support; evaluate upstream changes deliberately rather than importing them automatically.

### Validation and improvement

Use each skill's evaluation cases before expanding its instructions. Compare matched tasks with and without the skill on the models and hosts actually used. Check activation, preserved decisions, invented facts, unnecessary questions, substantiated defects, false positives, material misses, coverage honesty, and unintended actions. Record actual time and usage when available, and retest after relevant model or instruction changes.

The final maintenance pass clarifies staged versus working-file review, version-dependent API evidence, safe test execution, checked versus effective security values, and UI review/implementation boundaries. PENTA-PRO also reconciles companion screen specifications without changing its five-file output. These safeguards support consistent execution; they do not establish reliability on every model.

Keep active versions in `SKILL.md`, this README, and any versioned output template aligned. When behavior changes, reconcile descriptions, UI metadata, templates, references, and evaluation cases. Validate local links and anchors from each file's location. Retain historical research dates and trial versions with their original scope; a package update does not rerun or broaden earlier evidence.

Each skill's evaluation file records its actual audits/trials and limitations. Shorter documents and structural checks do not prove better task performance. No cross-model accuracy, cost, or efficiency benchmark is claimed. Prefer focused corrections supported by observed failures over universal rules for isolated cases.

### Adding a new skill

1. Create a root-level directory whose name matches the skill's `name`, using lowercase letters and hyphens.
2. Add `SKILL.md` with a clear description, focused instructions, and only the supporting resources the workflow needs.
3. Add an entry to [Available skills](#available-skills) and a dedicated section in this README covering purpose, example requests, output/boundaries, and resource links. Keep shared installation and maintenance guidance in their common sections.
4. Keep README and LICENSE files at repository root. Preserve applicable third-party notices where needed, validate metadata and internal links, and run meaningful evaluation cases before claiming improvements.

## License and attribution

The repository and its skills are distributed under the single root [MIT License](LICENSE). Skill directories do not contain duplicate LICENSE or README files.

When copying or redistributing individual skills, retain the repository-level license notice and applicable third-party notices with the distributed material.

The source research for [PENTA-PRO](penta-pro/references/sources.md), [Code Review](code-review/references/sources.md), [Cybersec](cybersec/references/sources.md), and [UI/UX](ui-ux/references/sources.md) records their inputs and adaptation decisions. [Third-party notices](THIRD-PARTY-NOTICES.md) preserve upstream attribution; the repository license does not relicense external articles. Attribution does not imply affiliation, endorsement, or a runtime dependency.
