# Collection closure review

This records the earlier collection closure. See the [distribution review](FINAL-SKILL-REVIEW.md#distribution-review) for the later license and release status.

## Scope and conclusion

Reviewed on 2026-11-09 against the pending previous-round changes and baseline `fd8633a`. The previous round integrated selected techniques, not every upstream entrypoint. This round closes useful workflow gaps and records every source disposition. This is a curated collection of 21 packages, not a literal mirror or a claim of identical behavior. Installing Matt Pocock or Superpowers is unnecessary for these workflows.

Both public Git trees were retrieved in full with no truncation. All 54 entrypoint paths were inventoried and screened. Relevant engineering bodies and selected supporting resources were inspected in detail. Excluded personal/framework packages were screened for fit, not audited as executable products. No upstream scripts, hooks or launchers were run or imported.

## Previous round

Added `diagnose-defect` for unclear failures, `behavior-testing` for cross-stack behavioral checks, `http-api` for actual HTTP server contracts/effects, and `mcp-server` for protocol and downstream boundaries. Extended PentaPRO task slices, Peer Review standards/specification coverage, Cybersecurity MCP trust checks and UI Design browser-fetch reasoning. The [initial assessment](SKILL-ASSESSMENT.md) retains its actual evidence and limits.

## This round

- Added [Software Delivery](software-delivery/SKILL.md) because no owner executed multi-step plans, refactors and resumable task coordination across stacks. Conditional references cover code design, isolation, bounded automation and human-only prerequisites.
- Added [Technical Research](technical-research/SKILL.md) because independent engineering research and technical spikes differ from product interviews and visual prototypes.
- Added [Git Delivery](git-delivery/SKILL.md) because read-only review does not own commits, branch publication or PR preparation. It preserves index selections, checks outgoing history and verifies the remote ID.
- Added [Agent Instructions](agent-instructions/SKILL.md) so portable authoring and evaluation of the factory's instructions do not depend on either external skill pack or a particular host. Moved the evaluation procedure into this package and retained the root navigation page.
- Reconciled the README catalog, complete install list, manual paths, routing and AGENTS template. Clarified that the native helpers' Android/JVM scope does not restrict the whole collection.
- Preserved five-pillar PentaPRO, native Android implementation/test logic, UI prototypes and PR Quiz behavior. No source package was deleted merely for reducing the count.

## Upstream coverage

### mattpocock/skills

Inspected inventory at `4ae2317ddb22b046e26455e4f9c9b3aaaf62212d` — 39 entrypoints.

| Source | Local destination or exclusion | Adaptation / reason |
| --- | --- | --- |
| [ask-matt](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/ask-matt/SKILL.md) | Excluded | Author-specific advice and personal context are not a portable engineering contract. |
| [code-review](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/code-review/SKILL.md) | [peer-review](peer-review/SKILL.md) | Standards and requirements coverage, evidence, independent handoff. |
| [codebase-design](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/codebase-design/SKILL.md) | [software-delivery/references/code-design.md](software-delivery/references/code-design.md) | Cohesive responsibilities, caller contracts, justified boundaries and testability. |
| [diagnosing-bugs](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/diagnosing-bugs/SKILL.md) | [diagnose-defect](diagnose-defect/SKILL.md) | Discriminating reproduction, tracing and controls. |
| [domain-modeling](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/domain-modeling/SKILL.md) | [penta-pro/references/discovery.md](penta-pro/references/discovery.md) | Domain terms and decisions stay in existing canonical records. |
| [grill-with-docs](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/grill-with-docs/SKILL.md) | [penta-pro](penta-pro/SKILL.md) | Focused discovery; deprecated upstream alias needs no local alias. |
| [implement-spec](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/implement-spec/SKILL.md) | [software-delivery](software-delivery/SKILL.md) | Dependency-aware increments, integration and resumption. |
| [implement](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/implement/SKILL.md) | [software-delivery](software-delivery/SKILL.md) | Authorized implementation with actual checks, no implicit commit. |
| [improve-codebase-architecture](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/improve-codebase-architecture/SKILL.md) | [software-delivery/references/code-design.md](software-delivery/references/code-design.md) | Investigate concrete coupling, compare alternatives and preserve contracts. |
| [pr](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/pr/SKILL.md) | [git-delivery](git-delivery/SKILL.md) | Problem, resulting behavior, evidence and recovery in the project PR format. |
| [prototype](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/prototype/SKILL.md) | [technical-research](technical-research/SKILL.md) | Bounded technical spikes; visual concepts already belong to UI Design. |
| [research](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/research/SKILL.md) | [technical-research](technical-research/SKILL.md) | Applicable primary sources, uncertainty and durable findings. |
| [retro](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/retro/SKILL.md) | [software-delivery/references/execution-controls.md](software-delivery/references/execution-controls.md) | Evidence-based process improvements without automatic global edits. |
| [setup-matt-pocock-skills](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/setup-matt-pocock-skills/SKILL.md) | Excluded | Upstream-specific tracker/plugin bootstrap; local catalog and project instructions own setup. |
| [tdd](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/tdd/SKILL.md) | [behavior-testing](behavior-testing/SKILL.md) | Meaningful failure before correction when test-first or regression evidence applies; native Android keeps native helpers. |
| [to-spec](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/to-spec/SKILL.md) | [penta-pro](penta-pro/SKILL.md) | Synthesize known intent without restarting settled discovery or automatically publishing. |
| [to-tickets](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/to-tickets/SKILL.md) | [software-delivery](software-delivery/SKILL.md) | Verifiable slices, prerequisites and compatible migration sequencing. |
| [triage](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/triage/SKILL.md) | [software-delivery](software-delivery/SKILL.md) | Establish requested outcome and evidence before task readiness; no imported tracker state machine or automatic closure. |
| [wayfinder](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/wayfinder/SKILL.md) | [penta-pro](penta-pro/SKILL.md) | Resolve consequential uncertainties incrementally with canonical decisions and resume state. |
| [wizard](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/engineering/wizard/SKILL.md) | [software-delivery/references/execution-controls.md](software-delivery/references/execution-controls.md) | Precise human-only prerequisites and safe reusable setup when warranted; no imported Bash runtime. |
| [chief-of-staff](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/chief-of-staff/SKILL.md) | [software-delivery/references/execution-controls.md](software-delivery/references/execution-controls.md) | Bounded coordination and durable handoffs; exclude personal schedules and mandatory agent orchestration. |
| [claude-handoff](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/claude-handoff/SKILL.md) | [software-delivery/references/execution-controls.md](software-delivery/references/execution-controls.md) | Portable resumption; no Claude subprocess launcher. |
| [loop-me](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/loop-me/SKILL.md) | [penta-pro](penta-pro/SKILL.md) | Software workflow requirements and authority; personal life automation excluded. |
| [setup-ts-deep-modules](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/setup-ts-deep-modules/SKILL.md) | [software-delivery/references/code-design.md](software-delivery/references/code-design.md) | Boundary rationale and project-owned enforcement; no forced TypeScript layout or dependency-cruiser installation. |
| [software-factory](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/software-factory/SKILL.md) | [software-delivery/references/execution-controls.md](software-delivery/references/execution-controls.md) | Run identities, ownership, bounded retries, evidence and actual authority; no infrastructure is provisioned. |
| [writing-beats](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/writing-beats/SKILL.md) | Excluded | Authoring narrative content is outside the requested software-development collection. |
| [writing-fragments](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/writing-fragments/SKILL.md) | Excluded | Personal content-production workflow outside scope. |
| [writing-shape](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/in-progress/writing-shape/SKILL.md) | Excluded | Personal content-production workflow outside scope. |
| [git-guardrails-claude-code](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/git-guardrails-claude-code/SKILL.md) | [git-delivery](git-delivery/SKILL.md) | Explicit Git targets and preservation rules; host-specific hooks are not installed. |
| [migrate-to-shoehorn](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/migrate-to-shoehorn/SKILL.md) | Excluded | A library-specific fixture migration does not justify another global workflow or dependency. |
| [scaffold-exercises](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/scaffold-exercises/SKILL.md) | Excluded | Course-specific exercise generation and CLI outside scope. |
| [setup-pre-commit](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/misc/setup-pre-commit/SKILL.md) | [software-delivery/references/execution-controls.md](software-delivery/references/execution-controls.md) | Project-selected deterministic checks with positive/negative controls; no mandatory Husky/Prettier. |
| [grill-me](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grill-me/SKILL.md) | [penta-pro](penta-pro/SKILL.md) | Deprecated alias absorbed into focused software discovery. |
| [grilling](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/grilling/SKILL.md) | [penta-pro](penta-pro/SKILL.md) | Consequential questions and examples; preserve delegated decisions. |
| [handoff](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/handoff/SKILL.md) | [software-delivery](software-delivery/SKILL.md) | Current contracts, revision, evidence and next action. |
| [teach](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/teach/SKILL.md) | Excluded | General tutoring and course management outside scope; PR Quiz remains optional. |
| [to-questionnaire](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/to-questionnaire/SKILL.md) | [penta-pro/references/discovery.md](penta-pro/references/discovery.md) | Focused missing decisions and known evidence; add asynchronous questionnaire guidance. |
| [wait-what](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/wait-what/SKILL.md) | Excluded | Ordinary clarification does not need a separate installed skill. |
| [writing-for-agents](https://github.com/mattpocock/skills/blob/4ae2317ddb22b046e26455e4f9c9b3aaaf62212d/skills/productivity/writing-for-agents/SKILL.md) | [agent-instructions](agent-instructions/SKILL.md) | Conditional pointers, clear completion criteria, concise reusable instructions. |

### obra/superpowers

Inspected inventory at `22f0b463e7a5e579904dd6211a520321035526f7` — 15 entrypoints.

| Source | Local destination or exclusion | Adaptation / reason |
| --- | --- | --- |
| [brainstorming](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/brainstorming/SKILL.md) | [penta-pro](penta-pro/SKILL.md) | Focused discovery and alternatives, retaining five canonical pillars and existing authority. |
| [diagnosing-superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/diagnosing-superpowers/SKILL.md) | Excluded | Debugs the upstream framework; it is not installed here. |
| [dispatching-parallel-agents](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/dispatching-parallel-agents/SKILL.md) | [software-delivery/references/execution-controls.md](software-delivery/references/execution-controls.md) | Independent tasks and explicit ownership only when delegation is authorized and available. |
| [executing-plans](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/executing-plans/SKILL.md) | [software-delivery](software-delivery/SKILL.md) | Sequential execution with evidence and resumption, no mandatory upstream scripts. |
| [finishing-a-development-branch](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/finishing-a-development-branch/SKILL.md) | [git-delivery](git-delivery/SKILL.md) | Explicit destination and reviewed snapshot; no automatic merge, deletion or deployment. |
| [receiving-code-review](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/receiving-code-review/SKILL.md) | [peer-review](peer-review/SKILL.md) | Evidence-based disposition and scoped re-review, without mandatory external comments. |
| [requesting-code-review](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/requesting-code-review/SKILL.md) | [peer-review](peer-review/SKILL.md) | Factual source-aware handoff and disclosed independence. |
| [subagent-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/subagent-driven-development/SKILL.md) | [software-delivery/references/execution-controls.md](software-delivery/references/execution-controls.md) | Optional delegation, integrated verification, unresolved gates remain unresolved. |
| [systematic-debugging](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/systematic-debugging/SKILL.md) | [diagnose-defect](diagnose-defect/SKILL.md) | Reproduction and cause evidence; incident containment remains distinct. |
| [test-driven-development](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/test-driven-development/SKILL.md) | [behavior-testing](behavior-testing/SKILL.md) | Observed assertions and regression sensitivity, without deleting existing implementation or imposing universal TDD. |
| [using-git-worktrees](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-git-worktrees/SKILL.md) | [software-delivery/references/execution-controls.md](software-delivery/references/execution-controls.md) | Isolation and actual ownership; worktrees do not isolate services or credentials. |
| [using-superpowers](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/using-superpowers/SKILL.md) | Excluded | Always-on bootstrap and mandatory invocation would add context and conflict with narrow ownership. |
| [verification-before-completion](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/verification-before-completion/SKILL.md) | [software-delivery](software-delivery/SKILL.md) | Snapshot-specific completion evidence, also retained inside domain owners; no extra global ritual. |
| [writing-plans](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-plans/SKILL.md) | [software-delivery](software-delivery/SKILL.md) | Actionable task contracts and checks in existing canonical records. |
| [writing-skills](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/skills/writing-skills/SKILL.md) | [agent-instructions](agent-instructions/SKILL.md) | Portable authoring, observable outcomes and matched evaluations; no destructive rewrite or automatic publication. |

## Platform and model boundaries

The common lifecycle covers commercial websites, landing pages, web apps, HTTP/MCP services, mobile and desktop software. Native Android has dedicated implementation/testing procedures. Web has dedicated UI guidance. iOS, Flutter, React Native and desktop work uses the common contracts and the project's actual SDK documentation, runner and platform checks. There is no claim that bundled specialist recipes exist for every framework. OS and game workflows were not added.

Shorter entrypoints, observable steps and conditional detail reduce reliance on unstated expertise. They do not establish smaller-model reliability. Validate the selected model/host on representative tasks before granting unattended operation. Skills supply procedures, not runners, credentials, event subscriptions, merge policy or deployment infrastructure.

## Validation and remaining limits

The final validation below checks the resulting local snapshot. Historical trials in other files retain their original scope. No consuming Castas build, device/assistive-technology session, deployed HTTP/MCP integration or cross-model cost/accuracy benchmark was run for this closure.

- All **21** packages passed the available skill-creator structural validator.
- The repository validator passed **93 Markdown files, 637 local links/anchors, 21 version checks**, complete manual-install coverage and directory/name matching. Its positive control and two negative controls (broken local resource, omitted install entry) behaved as expected in a disposable copy.
- Existing checks passed again: UI helper **24 Python tests**, PR publisher **12 Python tests**, embedded PR grader **25 offline Node scenarios**. No executable Android/UI/quiz implementation was changed.
- Independent review covered all eight native Android entrypoints and PR Quiz, and all four new packages. The separate core-owner review reported no substantiated blocker in inspected methods/templates/runtime references and 24 UI tests passing, then hit a usage limit during its last resource consistency scan. The maintainer completed the resulting link/version/catalog checks; this is not reported as a completed independent full-core review.
- The new-package review caught two concrete issues. The portable evaluation reference no longer links to repository-root maintenance files absent from an installation. Git Delivery now explicitly preserves unrelated staged selections and requires a verified candidate commit or a stop before unsafe separation.
- A same-model independent Git Delivery forward trial in `/tmp/git-delivery-trial-p7ftcxny` created commit `55172f9cb371b87c80368190be620e228936e1de` with only the intended documentation file, pushed to a local bare repository and verified matching remote HEAD. An unrelated untracked file retained its bytes. This was not this repository's commit and was not a GitHub push. Staged mixtures, divergence, hosted hooks and CI were not exercised by that trial.
- `git diff --check` and untracked-text whitespace checks passed. No installation into another project, global setting change, real repository commit/push, merge or deployment occurred.

The collection is ready for use as one maintained toolkit on new projects, subject to each project's real tools and gates. The four new workflows have source review and structural evidence; only Git Delivery received a fresh executed agent trial in this round. No matched baseline comparison or smaller-model benchmark was performed. Full unattended factory operation still requires an explicitly configured runtime, permission boundaries and measured validation on the selected model and target stack.

## Final publication review

The final pass reviewed the 21 skill entrypoints and the pending collection changes. It clarified when UI Design and Software Delivery may save artifacts or update task records. The HTTP workflow now describes caller or tenant scoping, conflicting key reuse, and verification of durable effects. The MCP workflow now checks authentication on protected requests and replay of another caller's session. The evaluation procedure separates the fixtures the agent needs from the evaluator's private tests and expected findings.

The collection validator previously accepted a link to an ignored file because it existed locally. It now checks local targets against the Git file inventory. A disposable copy passed the valid case and rejected an ignored file, a symlink to an ignored file, and missing version metadata. The 21 skill validators and 61 existing regression tests passed. These results cover the repository and its local tools. The new protocol guidance was checked against primary references, with application integration and comparative model performance still unmeasured.
