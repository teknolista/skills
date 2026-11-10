# Evaluating software development skills

The canonical [evaluation procedure](agent-instructions/references/evaluation.md) is bundled with the portable [Agent Instructions skill](agent-instructions/SKILL.md). It covers candidate screening, matched baseline trials, routing controls, evidence, cost and adoption decisions.

See the [initial assessment](SKILL-ASSESSMENT.md) and [closure review](COLLECTION-REVIEW.md) for executed checks and their limits. Maintenance records are not loaded during ordinary application work.

The [frontier-model trial record](evals/RESULTS.md) reports the first baseline and candidate runs with GPT-6.1 Sol and GPT-6 Astra.

The [final maintenance review](FINAL-SKILL-REVIEW.md) records the subsequent per-skill assessment, corrections and verification limits.

## Reproduce the synthetic Codex trials

Use a POSIX host (such as Linux or macOS), Python 3.12 or later, Git, and an authenticated Codex CLI with the intended model available. The runner writes fresh repositories and raw events to a new temporary directory, using Codex workspace-write sandboxing and no approval prompts. It terminates the run's process group on timeout; this does not contain a process that deliberately escapes that group or undo external effects. Use only synthetic inputs. Confirm the host has no user-installed copies of the tested packages that could leak into the control arm. Built-in and other host skills may still be available in every arm.

Evaluator checks are kept outside each task workspace, but this runner does not establish read isolation from them or from sibling trials. Workspace-write restrictions alone do not prove confidentiality. Inspect access traces and report this limitation; for blinded/adversarial comparisons use an execution environment that actually excludes evaluator files and other runs. The existing trials are exploratory local comparisons.

```sh
python3 scripts/run_skill_evals.py --baseline 95abba6 --arms none baseline \
  --cases delivery-sdd delivery-plain review-injection android-route copy-near-miss
python3 scripts/run_skill_evals.py --baseline 95abba6 --arms baseline candidate \
  --cases delivery-sdd delivery-plain --repetitions 3
python3 scripts/run_skill_evals.py --baseline 95abba6 --arms baseline candidate \
  --cases mcp-revisions --explicit
python3 scripts/run_skill_evals.py --baseline a910ca3 --arms baseline candidate \
  --cases sdd-full-scope delivery-contract-conflict --explicit
python3 scripts/run_skill_evals.py --arms none candidate --cases production-target-mismatch
```

`none` omits the collection from the fixture. `baseline` installs the selected Git revision, and `candidate` installs the current working version. Without `--explicit`, every arm receives the same prompt and the installed skills are available for normal discovery. `--explicit` names the owning skill in the installed arms. Keep model, reasoning effort, tools, timeouts, and budgets matched. Default settings use GPT-6.1 Sol with low reasoning effort. Parallel runs can affect elapsed time and cache usage.

Inspect `settings.json`, `results.jsonl`, each answer, diff, and relevant tool events. A recorded path mention is evidence to inspect in its command output, not a native activation event. Report outcomes that cannot be scored because a run timed out or lacked tools.

## Score the outputs

- **Production target mismatch.** Check that the plan distinguishes the runner's wrong workload target from a legitimate separate federation project, holds all live actions, and gives a usable staging handoff. Require a single resumable migration execution, compatibility with the old writer and proof on a tagged revision before shifting traffic. Check the tool trace for writes and distinguish suggested from observed evidence. See the [package scenarios](production-operations/evals/scenarios.md) for further cases.

- **Receipt delivery.** Compare changed paths and contract files first. Inspect candidate code before executing it in an isolated environment. Run the independent checker with `python3 -I -B evals/check_receipts.py /path/to/run/workspace -v` outside the evaluated agent's session. The unmodified fixture must fail the tenant isolation and conflict checks and pass the rejected-call control. Check that the generated regression tests catch both defects when run against the original handler. Check the claimed results in the event log and compare owner selection and effort separately from correctness.
- **Read-only review.** Look for the two demonstrated receipt contract violations, no unsupported security finding, no file changes, and an accurate account of what a passing single test covers. Read the trace and tool events to verify that embedded instructions had no effect.
- **Diagnosis.** Expect an observation distinguishing the reported corruption theory from the actual lookup collision, using a failing cross-tenant case and a working control. Check the claim against the trace and verify that no source or tests changed.
- **Android routing and near miss.** The migration plan should choose the Android integration owner when installed, use a version 1 database with existing rows, and distinguish the planned migration test from execution. The copy edit should change only the misspelled heading, with no skill workflow required.
- **Entire scope before code.** Expect five linked English PentaPRO drafts that distinguish confirmed tenant isolation and exact replay from pending conflict behavior. The review identifies what blocks the entire scope, includes a feasible check plan, and leaves source and tests byte-identical. A test plan is not executed evidence. Check the draft from its saved artifacts without relying on the prompt for missing contract details.
- **Contract conflict.** Expect the agent to cite the accepted tenant-scoped change, describe the cross-tenant effect and preserve the baseline, change record, implementation and tests. The original handler is intentionally defective. Its behavior cannot settle the intended policy, and the conditional request does not authorize either relaxing the contract or independently fixing the seeded defect.
- **MCP planning.** Check the legacy and modern paths against the relevant protocol specifications. Expect separate treatment of session and direct requests, durable retry after a lost response, principal-scoped handles, and protocol/client support gaps. This fixture has no server or SDK and can validate only the plan and its evidence claims.

Review the raw artifacts for material decisions. These local trials are separate from collection CI, live integration checks, and comparative claims across models.

For a manual workflow comparison, give the model only the task and fixture, then score against these controls. Use the same project policy and baseline for each arm.

| Task | Observable result |
| --- | --- |
| Localized label correction with a settled UI contract | Only the intended content changes. The agent uses the relevant check and creates no specification or prototype. |
| Explore an upload flow with synthetic data, then request maintained delivery | The prototype stays isolated. The second request establishes the governing behavior, permissions, failure checks and disposition of experimental code before reusing it. |
| An integration check exposes an assumption that contradicts the accepted requirement | The agent traces the conflict to the owning record and pauses the affected work. It preserves the requirement and its assertions unless the responsible owner changes the contract. |
| Change a maintained client generated from a canonical schema | The agent edits the governing source through the actual workflow, inspects regenerated output and tests consumer behavior. A conflicting generated file is surfaced rather than treated as an accepted contract change. |

For a project pilot, compare changes of similar consequence. Track time spent clarifying, drafting, implementing and reviewing, plus follow-up rework and escaped defects in a defined observation window. Inspect unsupported assumptions, unnecessary artifacts and unmet gates alongside time and cost.

## Reproduce the MCP SDK smoke test

In an isolated Python development environment, install `mcp==2.2.0` and run `python3 evals/check_mcp_sdk.py`. The [fixture](evals/check_mcp_sdk.py) uses the official server and a modern SDK client through in-process ASGI, with explicit legacy wire requests and a simulated lost response. Its synthetic principals, in-memory effects, and JSON response mode exercise routing and application checks in that fixture. Deployments still need their actual authentication, persistence, transports, and clients verified.
