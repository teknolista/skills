# Evaluating software development skills

Use this maintainer procedure before adding, expanding, or retiring a skill. Keep evaluation material outside normal task context. Keep actual evidence and adoption decisions in the target repository's maintenance record.

## Screen the candidate

1. State the recurring failure, the affected projects, and what a better result would look like. Choose one primary owner by requested outcome. Compare the candidate with the current skill, project rules, built-in tools, and executable checks.
2. Choose the smallest useful home. Put durable local commands and conventions in project instructions. Put objective enforcement in the existing test or CI system. Add conditional guidance to its existing owner when the trigger and deliverable match. Create a package when it owns a distinct task with an observable result. Record rejection when the idea adds friction or lacks a relevant use case.
3. Inspect the upstream revision, license, metadata, references, and any executable path that adoption would include. Trace scripts, hooks, network calls, credential access, dependencies, writes, and host assumptions before execution. Prefer original adaptations that reuse project tools. Keep the entrypoint focused and load specialist material only for matching work. [Agent Skills specification](https://agentskills.io/specification)
4. Define the scope, accepted outcome, safety gates, and cost tolerance before running trials. A candidate that can override the user, expose data, silently widen authority, or weaken a required check needs correction before adoption.

## Compare matched tasks

Use a disposable copy of the same pinned starting state for each run. Give each run the same request, task fixtures, tools, access, environment, project rules, budget, and model/host settings. Keep evaluator-only tests, scoring keys, and expected findings inaccessible to the agent. Record relevant nondeterminism, available seeds, and run order. Start fresh sessions to limit carryover.

Verify that the execution boundary actually denies reads of evaluator material; placing it outside the working directory alone does not hide it. If read isolation is unavailable, disclose possible contamination and inspect access traces instead of calling the trial blinded. Bound the lifetime of spawned commands and their descendants, and record timeout or incomplete runs as such even when they leave plausible artifacts.

| Comparison | What it isolates |
| --- | --- |
| Normal workflow versus explicit candidate invocation | Incremental benefit when the correct skill is supplied. For an extension, compare the previous owner version with the proposed version. |
| Normal skill inventory versus inventory with the candidate | Trigger accuracy, wrong activations, overlap, and practical context cost. Include ordinary work that should route elsewhere. |
| Repeated trials across representative tasks | Variance, recurring benefit, and regressions. Retest affected cases after material skill, model, host, or tool changes. |

Include a clear case, a realistic failure or ambiguity, and a near miss where the skill should stay inactive. Choose the target stacks actually used. Include an existing Android workflow for changes that affect Android routing or a shared owner. Exercise a denied operation or misleading result where the workflow touches an authority boundary. A missing runner or unsupported tool is an observed outcome with a recorded cause.

## Score artifacts and effects

Evaluate executable checks first where practical. Inspect the exact resulting files and compare externally visible behavior with the same acceptance criteria in every run. For review and design tasks, use a fixed rubric with verified positives and negatives. Hide the run arm from the reviewer where practical. Use the following fields in an existing maintenance record.

| Field | Record |
| --- | --- |
| Reproducibility | Skill/revision, baseline revision, case ID, host/model/settings, tools/permissions, arm, attempt and relevant environment. |
| Correctness | Required cases passed, missing behavior, regression results, unintended edits, and evidence for the actual revision. |
| Routing and safety | Activation, chosen owner, duplicate workflow, permission boundary, unsafe attempts or effects, and false claims of verification. |
| Maintainability | Scope and compatibility preservation, real caller behavior, test sensitivity, and supported findings. |
| Effort | Available token and context metrics, wall time, tool calls, user interruptions, retries, and follow-up corrections. Mark unreported metrics as unavailable. |
| Disposition | Keep, revise, defer, or reject. Give the observed effect, remaining gaps, and the next comparison that could change the decision. |

Summarize paired wins, ties, losses, and important case-level differences. Keep task failures and missing data visible. A fast run with a functional or safety regression fails the relevant gate. Favor clear quality gains within the agreed cost budget, or lower effort at comparable quality. When results are mixed, narrow the trigger or revise the instructions and retest. Selectively install unmeasured candidates for trials until the evidence supports broader use.

Record structural validation, an isolated smoke trial, and a comparative evaluation as separate claims. Use fixture evidence to prove the exercised behavior, including the intended assertion failure before the correction where available. Treat popularity, prose length, and reviewer confidence as screening signals. Record sample size and limits when reporting gains. [SWE-Skills-Bench v2](https://arxiv.org/abs/2603.15401v2)

## Starter cases for this collection

Use these as fixture-authoring briefs. Keep expected behavior out of the evaluated agent's context except for the actual contract the agent would receive on the task.

| Case | Prompt and fixture | Evidence to inspect |
| --- | --- | --- |
| Diagnosis and regression | Two tenants can reuse one request ID. A repeat within a tenant must reuse its receipt. The first reported symptom is a missing job. | Observe the missing job and a working control. Verify cause, same-tenant retries, independent tenant writes, and the original failing assertion. |
| Browser test | A valid form can recover from a synthetic dependency failure. A keyboard user must retain access to the action. | Run the existing browser runner against a disposable app. Confirm discovery, real inputs, observable readiness and recovery, and no dependency on arbitrary delays. |
| HTTP API | Add a compatible write or retry path with older consumers and two scoped principals. | Check wire and state compatibility, a permitted control, denied access with zero forbidden effects, and ambiguous-response or concurrent retry behavior. |
| MCP server | Expose one existing service action through the project's supported client and SDK. Use an isolated fake service for effects. | Check selected protocol lifecycle, discovery/schema, success and failure, out-of-scope calls and actual downstream effects. Record the tested revision and transport. |
| Routing controls | An Android Room migration test, an existing Compose screen fix, a copy edit, a requirements interview, and a review-only request. | Inspect the owner and actual changes. Preserve native test/design ownership, canonical artifacts, and read-only review scope. |

Record which checks actually ran in the target repository. Case descriptions are a test inventory.
