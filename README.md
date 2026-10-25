# ✨ AI Agent Skills

A collection of reusable skills for developers building software with AI coding agents. PENTA-PRO turns intent into an actionable specification; Code Review checks implementation against requirements and concrete evidence. Each skill can be used independently.

All skill instructions and generated artifacts are in English. Conversation can use the user's preferred language.

## Contents

- [Available skills](#available-skills)
- [Installation and activation](#installation-and-activation)
- [PENTA-PRO](#penta-pro)
- [Code Review](#code-review)
- [Project AGENTS.md template](#project-agentsmd-template)
- [Repository structure](#repository-structure)
- [Maintenance and new skills](#maintenance-and-new-skills)
- [License and attribution](#license-and-attribution)

## Available skills

| Skill | Version | Purpose |
| --- | --- | --- |
| [PENTA-PRO](#penta-pro) | 1.3.0 | Create, resume, update, or review software specifications across PRODUCT, PROJECT, PROOF, PROCESS, and PRODUCTION. |
| [Code Review](#code-review) | 1.3.0 | Review backend, frontend, and Android changes with prioritized findings, concrete evidence, and explicit verification limits. |

## Installation and activation

Copy the complete directory of each desired skill into the skills location supported by your agent. Preserve its internal relative paths. For a Codex project, the installed entrypoints are:

```text
your-project/.agents/skills/penta-pro/SKILL.md
your-project/.agents/skills/code-review/SKILL.md
```

A skill stored in this repository is not automatically installed into other projects. Codex discovers repository skills from `.agents/skills/`; if a copied skill does not appear, restart the session. Other hosts use their own discovery locations and invocation syntax. See [agent and model compatibility](docs/compatibility.md) for documented locations, capabilities, and integration limits.

Both skills support automatic selection for matching tasks. In Codex, mention `$penta-pro` or `$code-review` to select one explicitly. Their `agents/openai.yaml` files provide optional display metadata and default prompts; they do not select a model. Select models through the host's controls or authorized orchestration.

The packages use Markdown instructions, references, and templates. Neither requires the other skill, a plugin, paid service, API key, external connector, or bundled script runtime. Actual work still requires relevant project access and whatever tools its requested checks need. Saving a specification or report requires a writable destination. Installing a skill does not supply those capabilities or authorize additional actions.

## PENTA-PRO

**Version:** 1.3.0 · **Entrypoint:** [penta-pro/SKILL.md](penta-pro/SKILL.md)

Use PENTA-PRO when defining a product, specifying a substantial feature, maintaining an existing PENTA-PRO document, or checking whether the next increment is ready for development. It uses existing project information and asks about consequential gaps. Ordinary coding tasks and small, clear specification updates do not restart a full interview.

### The five pillars

| Pillar | Focus |
| --- | --- |
| PRODUCT | Users, value, journeys, business rules, permissions, scope, and observable acceptance criteria. |
| PROJECT | Delivery constraints, resources, dependencies, risks, architecture, data, and contracts. |
| PROOF | Verification methods, concrete examples, failure cases, and acceptance evidence. |
| PROCESS | Tasks, responsibilities, execution authority, review, integration, and escalation. |
| PRODUCTION | Installation, environments, updates, migration, support, monitoring, and recovery. |

The pillars organize the specification; they are not sequential development phases. Resolve enough detail for the next useful increment and refine later work as evidence emerges.

### Example requests

```text
Use $penta-pro to interview me and create a specification for this project.
Use $penta-pro to resume the interview from docs/penta-pro.md.
Use $penta-pro to update the specification with these new requirements: ...
Use $penta-pro to review whether the first increment is ready for development.
```

### Output and working boundaries

The normal destination is `docs/penta-pro.md` in the target project, unless the user selects another path or an existing specification has an established location. Project answers belong in that document; the shared template stays generic. Preserve completed specifications and reconcile updates deliberately rather than replacing them with a newer blank template.

The skill distinguishes confirmed information, proposals, and pending decisions. Routine decisions made within explicit delegation are attributed to the agent and can be settled for readiness without being presented as user requirements or document acceptance. When the user is unavailable, retain consequential blockers and complete independent specification work. If saving is unavailable, return an explicitly unsaved draft.

Critical product rules should have concrete input/output examples independent of the implementation. Planned checks remain `Unverified` until executed. Specification readiness, document acceptance, implementation verification, and release acceptance are separate states. Creating or updating a specification does not itself authorize implementation or release; existing authorization remains valid.

The workflow is model-neutral. Use a host that can load the complete skill folder and relevant project context. Disclose missing capabilities rather than inventing answers or verification results. Package compatibility does not establish identical quality across models.

### Resources

| Resource | Purpose |
| --- | --- |
| [Entrypoint](penta-pro/SKILL.md) | Scope, interview workflow, document maintenance, readiness, and handoff. |
| [Specification template](penta-pro/assets/penta-pro-template.md) | Reusable five-pillar document structure and field guidance. |
| [Focused discovery](penta-pro/references/discovery.md) | Conditional techniques for unclear intent, dependent questions, alternatives, and consequential missing information. |
| [Source notes](penta-pro/references/sources.md) | Brainstorming research, inspected revisions, exclusions, and adaptation decisions. |
| [Evaluation scenarios](penta-pro/evals/scenarios.md) | Discovery, interview, update, delegation, and scope cases, with validation records. |
| [OpenAI metadata](penta-pro/agents/openai.yaml) | Optional Codex display metadata and example invocation. |

Load the template for creation or structural gaps, and discovery guidance when needed. Source notes and evaluation cases are maintainer resources rather than routine interview context.

## Code Review

**Version:** 1.3.0 · **Entrypoint:** [code-review/SKILL.md](code-review/SKILL.md)

Use Code Review for backend services, frontend applications, and Android software. It supports local edits, selected files or snippets, pull requests, commit comparisons, independent second opinions, and re-review after fixes. Reports separate substantiated defects, verification gaps, optional improvements, and remaining release requirements.

### Example requests

```text
Use $code-review to review all my uncommitted changes, including new files.
Use $code-review to review this branch against origin/main, including the local edits.
Use $code-review to review the selected PR against docs/penta-pro.md.
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

Confirm how a managed reviewer receives instructions. Including only the body of `SKILL.md` does not transfer supporting references or execution capabilities. Claude's managed Code Review can include skill text through its review policy but does not load supporting files. Supply needed guidance through that service's supported configuration and qualify coverage when material resources are unavailable.

### Resources

| Resource | Purpose |
| --- | --- |
| [Entrypoint](code-review/SKILL.md) | Scope, routing, evidence requirements, independence, and follow-up. |
| [Review method](code-review/references/review-method.md) | Target selection, trusted policy, confidence, severity, coverage, and verdicts. |
| [Backend](code-review/references/backend.md) | APIs, authorization, data, concurrency, failure recovery, and operations. |
| [Frontend](code-review/references/frontend.md) | UI state, contracts, accessibility, browser boundaries, and performance. |
| [Android](code-review/references/android.md) | Lifecycle, coroutines, Flow, Compose/Views, platform security, and release variants. |
| [Verification](code-review/references/verification.md) | Assertions, regression protection, safe checks, and evidence reporting. |
| [Independent review](code-review/references/independent-review.md) | Fresh context, model selection, review lenses, and feedback loops. |
| [Report template](code-review/assets/review-report-template.md) | Optional structure for substantial or saved reviews. |
| [Handoff template](code-review/assets/review-handoff-template.md) | Factual packet for another reviewer or model. |
| [Source research](code-review/references/sources.md) | Original sources, official guidance, and synthesis decisions. |
| [Evaluation scenarios](code-review/evals/scenarios.md) | Calibration, scope, policy, host behavior, and validation records. |
| [OpenAI metadata](code-review/agents/openai.yaml) | Optional Codex display metadata and example invocation. |

Load the review method and applicable references. Source research and evaluation cases are maintainer resources, not required context for every review. The package is an original synthesis, not an installer or runtime wrapper around upstream skills.

## Project AGENTS.md template

[AGENTS-template.md](AGENTS-template.md) is a reusable working guide for AI agents, separate from the skills. Copy it to a target project's root as `AGENTS.md`, fill in the project facts, navigation, actual commands, and decision authority, and remove or mark inapplicable entries. Preserve an existing project's guidance rather than replacing it blindly.

The template supplies general rules for scoped work, implementation, validation, security, collaboration, and handoff. It does not prescribe a stack, folder layout, model, skill dependency, or test framework. Its artifact-language default is English, with exceptions for required identifiers, literal data, and localization. Keep detailed specifications and runbooks in their own authoritative documents and link them from the project guide.

## Repository structure

Each skill lives directly under this repository's root and follows the [Agent Skills specification](https://agentskills.io/specification). There is no additional nested `skills/` directory. Shared usage documentation and licensing live at the root.

```text
skills/
├── README.md
├── LICENSE
├── AGENTS-template.md
├── docs/
│   └── compatibility.md
├── penta-pro/
│   ├── SKILL.md
│   ├── agents/
│   ├── assets/
│   ├── evals/
│   └── references/
└── code-review/
    ├── SKILL.md
    ├── agents/
    ├── assets/
    ├── evals/
    └── references/
```

`SKILL.md` contains required metadata and runtime instructions. Optional `agents/` files adapt host presentation; `assets/` holds output templates; `references/` holds conditional detail; `evals/` holds maintenance cases and validation records. Create only the directories a skill needs.

## Maintenance and new skills

Authoring was checked against [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills) and [Anthropic's best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices) on 2026-10-25. These are maintainer references, not runtime dependencies. Recheck relevant guidance when changing packaging, discovery, or model support; evaluate upstream changes deliberately rather than importing them automatically.

### Validation and improvement

Use each skill's evaluation cases before expanding its instructions. Compare matched tasks with and without the skill on the models and hosts actually used. Check activation, preserved decisions, invented facts, unnecessary questions, substantiated defects, false positives, material misses, coverage honesty, and unintended actions. Record actual time and usage when available, and retest after relevant model or instruction changes.

Version 1.3.0 includes separately assigned specification and code-review smoke trials with their limitations recorded in the evaluation files. Shorter documents and structural checks do not prove better task performance. No cross-model accuracy, cost, or efficiency benchmark is claimed. Prefer focused corrections supported by observed failures over universal rules for isolated cases.

### Adding a new skill

1. Create a root-level directory whose name matches the skill's `name`, using lowercase letters and hyphens.
2. Add `SKILL.md` with a clear description, focused instructions, and only the supporting resources the workflow needs.
3. Add an entry to [Available skills](#available-skills) and a dedicated section in this README covering purpose, example requests, output/boundaries, and resource links. Keep shared installation and maintenance guidance in their common sections.
4. Keep README and LICENSE files at repository root. Preserve applicable third-party notices where needed, validate metadata and internal links, and run meaningful evaluation cases before claiming improvements.

## License and attribution

The repository and its skills are distributed under the single root [MIT License](LICENSE). Skill directories do not contain duplicate LICENSE or README files.

When copying or redistributing individual skills, retain the repository-level license notice and applicable third-party notices with the distributed material.

The source research for [PENTA-PRO](penta-pro/references/sources.md) and [Code Review](code-review/references/sources.md) records their inputs and adaptation decisions. Attribution does not imply affiliation, endorsement, or a runtime dependency.
