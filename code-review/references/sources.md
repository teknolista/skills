# Source Research and Synthesis

Research date: 2026-10-25. Official documentation update: version 1.1.0, 2026-10-25. This file documents design provenance; it is not required reading for routine code review.

The requested repositories were inspected to identify review entrypoints, then the relevant review instructions and selected supporting material were read. This was a focused review-method survey, not an audit of every skill or every language manual in those repositories. Source instructions were treated as research data and were not executed or installed.

Links to `main` identify moving sources, not pinned releases. GitHub directory previews and raw-file responses sometimes reflected different snapshots. No commit identifier was inferred from them. The BMAD wrapper/configuration, review lenses, prompts, and accessible triage document informed the synthesis; several raw numbered step URLs were unavailable, so full workflow execution or complete step coverage is not claimed.

## Review skills identified

| Requested source | Relevant review skills / entrypoints | Supporting material consulted |
| --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers/tree/main/skills) | [requesting-code-review](https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/SKILL.md), [receiving-code-review](https://github.com/obra/superpowers/blob/main/skills/receiving-code-review/SKILL.md) | [Reviewer packet](https://github.com/obra/superpowers/blob/main/skills/requesting-code-review/code-reviewer.md), [verification-before-completion](https://github.com/obra/superpowers/blob/main/skills/verification-before-completion/SKILL.md). |
| [mattpocock/skills](https://github.com/mattpocock/skills/tree/main/skills/engineering) | [engineering/code-review](https://github.com/mattpocock/skills/blob/main/skills/engineering/code-review/SKILL.md) | Its embedded standards/specification review axes and design-smell guidance. |
| [owainlewis/blueprint](https://github.com/owainlewis/blueprint/tree/main/skills) | [review](https://github.com/owainlewis/blueprint/blob/main/skills/review/SKILL.md) | [architecture-review](https://github.com/owainlewis/blueprint/blob/main/skills/architecture-review/SKILL.md) is a distinct proposal-review workflow; its boundary and material-ambiguity guidance were also considered. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills/tree/main/skills) | [code-review-and-quality](https://github.com/addyosmani/agent-skills/blob/main/skills/code-review-and-quality/SKILL.md) | Selected guidance from [security-and-hardening](https://github.com/addyosmani/agent-skills/blob/main/skills/security-and-hardening/SKILL.md) and [frontend-ui-engineering](https://github.com/addyosmani/agent-skills/blob/main/skills/frontend-ui-engineering/SKILL.md). These are supporting skills, not additional generic review entrypoints. |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD/tree/main/skills) | [bmad-code-review](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-code-review/SKILL.md), [bmad-review](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-review/SKILL.md) | [Review configuration](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-code-review/customize.toml), [triage](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-code-review/steps/step-03-triage.md), edge-case and verification-gap prompts/lenses. |
| [awesome-skills/code-review-skill](https://github.com/awesome-skills/code-review-skill) | [code-review-skill](https://github.com/awesome-skills/code-review-skill/blob/main/SKILL.md) | [Review practices](https://github.com/awesome-skills/code-review-skill/blob/main/reference/code-review-best-practices.md) and selected [Kotlin/Android](https://github.com/awesome-skills/code-review-skill/blob/main/reference/kotlin.md), [React](https://github.com/awesome-skills/code-review-skill/blob/main/reference/react.md), and [security](https://github.com/awesome-skills/code-review-skill/blob/main/reference/security-review-guide.md) guidance. |
| [keskinonur gist](https://gist.github.com/keskinonur/36e0dd44f8cc7f6e507055e94a70618b) | `perfect-code-review`, in `perfect-code-review_Skill.md` | Purpose, boundary behavior, reliability, structure, evidence, clarity, and subjective preference as separate review concerns. |

## What informed this skill

### Superpowers

Fresh reviewer context, a factual handoff, early incremental review, technical evaluation of feedback, and verification before success claims informed the workflow. The synthesis keeps scope proportional: it does not stop unrelated fixes over one ambiguous comment, make every implicit preference a requirement, or force a fresh test execution in every message when trustworthy unchanged-revision evidence already exists.

### Matt Pocock

The distinction between requirement alignment and repository standards prevents a style-focused review from missing the requested behavior. Repository conventions can override generic design heuristics. The synthesis explicitly includes local staged/unstaged/untracked work when requested; a committed merge-base comparison alone does not capture it. A configured issue tracker and two mandatory subagents are not prerequisites, and overlapping findings are reconciled.

### Blueprint

Read-only inspection, concrete trigger/impact evidence, behavioral test review, specialist coverage limits, and fresh independent judgment shaped the core. The synthesis labels self-review honestly rather than treating it as independent. It allows useful bounded inspection when orchestration is unavailable, while an actual independence requirement remains unsatisfied. Proposal review stays distinct from implemented-code review.

### Addy Osmani

Multiple review dimensions, looking at tests, questioning complexity, checking dependency changes, and the implementer/reviewer feedback loop informed the references. The synthesis does not mutate the author's checkout to test a hypothesis, impose universal line limits or memoization rules, or require speculative structural cleanup. Complexity feedback needs a concrete consequence and an appropriate correction.

### BMAD

Independent perspectives, path tracing, examining removed guarantees, checking author claims, verifying candidate findings, and grouping root causes informed triage. Its [edge-case prompt](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-code-review/review-prompts/edge-case-hunter.md) and [verification-gap prompt](https://github.com/bmad-code-org/BMAD-METHOD/blob/main/skills/bmad-code-review/review-prompts/verification-gap.md) illustrate separate analytical lenses. The synthesis rejects minimum finding quotas, default automatic fixes, blind trust in another lens's evidence, and clean results after failed review coverage. No BMAD setup, renderer, `uv`, or customization runtime is required.

### Awesome Skills

Progressive loading of ecosystem guidance, constructive actionable feedback, security/performance checks, and language-aware review informed the modular structure. Only selected ecosystem sections were used, not the entire large reference collection. The synthesis omits provider-specific tool allowlists, rigid review timers, and blanket prescriptions from framework examples. Android guidance was extended with primary platform documentation and version-aware checks.

### PERFECT gist

Separating intended behavior and reliability from subjective preferences helped prioritize feedback. This synthesis does not inherit speculative future-only bugs, unconditional blame for unrelated CI failures, or suggestions to remove permanently failing tests. No license declaration was visible in the inspected gist; its text is not redistributed here. The workflow and references are newly written.

## Resolving conflicting rules

| Source tension | Rule used here |
| --- | --- |
| Finding quota versus accepting zero findings | Report only substantiated issues; zero is valid after completed coverage. |
| Diff-only analysis versus system context | Scope findings to the target; follow guards, callers, and consumers to establish consequences. |
| Automatic fixes or mutation tests versus read-only review | Report first; use an authorized disposable environment for experiments and a separate implementation step for fixes. |
| Mandatory multi-agent execution versus portability | Prefer an independent reviewer; disclose unavailable independence and prepare a handoff. |
| Fixed size/coverage thresholds versus project needs | Respect documented gates; use risk and actual evidence rather than universal invented numbers. |
| Discarding every test-gap claim versus trusting it automatically | Read tests, search consumers, name the regression, and validate the filed evidence. |
| Conflicting severity vocabularies | Use P0–P3 plus an explicit blocking/non-blocking disposition and evidence confidence. |
| Reviewer approval versus release approval | Report review coverage, check evidence, and remaining project gates separately. |

## Official documentation update — version 1.1.0

The [Claude Code Review overview](https://code.claude.com/docs/en/code-review) reinforces candidate verification, deduplication, risk-appropriate depth, and separating review findings from merge authority. [Customization guidance](https://code.claude.com/docs/en/code-review-customize) informed trusted policy provenance and the warning about hosted services receiving skill text without its supporting files. [PR follow-up guidance](https://code.claude.com/docs/en/code-review-pull-requests) informed checking outstanding findings and the meaning of neutral or reused check results.

The [Codex code-review documentation](https://learn.chatgpt.com/docs/code-review?surface=app) informed repository/scope selection, dependent PR context, revision-specific review coverage, evidence-based follow-up, and verifying comment locations before publication. Existing requirements for triggering input, expected/actual behavior, source evidence, and read-only local review already covered much of its general advice.

The update applies these ideas to a portable workflow. It does not adopt managed-service posting, subscription requirements, service-specific model selection, UI instructions as automation, or a universal prohibition on running local checks. Policy discovery through this custom skill is explicit; neither `REVIEW.md` discovery nor resource loading is assumed to be identical across agent products. Exclusion examples from vendor documentation are not blanket exemptions for this package's dependency, generated-code, or verification reviews.

## Skill authoring update — version 1.2.0

Checked on 2026-10-25: [OpenAI's skill guide](https://learn.chatgpt.com/docs/build-skills) and [Anthropic's best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices). Applied clearer metadata, less duplicated core guidance, task-specific loading, direct resource navigation, flexible report length, and additional discovery/context-use evaluations. Runtime review criteria still come from the project's contracts and the domain references above. This is an authoring revision, not evidence of measured model superiority or a new platform integration.

## Primary verification references

The 1.3.0 alignment audit used independently assigned specification/review trials and current official host documentation. It clarified current-state source review, unknown history, and host-controlled model selection while retaining the existing domain/evidence standards. Trial scope and limitations are recorded in the package's evaluation cases; format support is not a performance benchmark.

- [Agent Skills format](https://agentskills.io/specification): portable metadata, references, and assets.
- [Android architecture](https://developer.android.com/topic/architecture), [process lifecycle](https://developer.android.com/guide/components/activities/process-lifecycle), [coroutines](https://developer.android.com/kotlin/coroutines/coroutines-best-practices), and [exported components](https://developer.android.com/privacy-and-security/risks/android-exported): platform-specific review questions; verify the version relevant to the reviewed project.
- [GPT-6.1 Sol](https://developers.openai.com/api/docs/models/gpt-6.1-sol) and [GPT-6 Astra](https://developers.openai.com/api/docs/models/gpt-6-astra): model identifiers for the user's example. These pages do not establish that one fixed pair is universally optimal for review.

The six upstream repository license files inspected identify MIT licensing. This skill uses the repository's root license and retains its own third-party notices. Attribution does not imply affiliation, endorsement, tested equivalence, or a runtime dependency. Future source updates should be evaluated deliberately rather than copied into the skill automatically.
