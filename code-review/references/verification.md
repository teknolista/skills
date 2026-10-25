# Review the Verification

## Find what changed and who observes it

For each meaningful behavioral change, identify the observable contract: a value, error, state transition, persisted record, event, permission decision, layout, or interaction. Trace relevant consumers and the tests that actually reach them. Changes to tests, dependencies, configuration, and migrations can affect behavior or protection even when application source is unchanged.

Derive expected results from authoritative requirements and examples, not only from the current implementation or its tests. Code and tests may agree while violating the same product rule; identify that rule before claiming a mismatch.

Before asserting that coverage is missing, search by the changed symbol, imports, route/registration, requirement ID, or observable behavior. Read plausible tests and fixtures. Say how far you looked. A missing adjacent test file or a low aggregate coverage percentage is not itself a demonstrated gap.

## Assess assertions, not reassuring names

- Does setup reach the changed path with the relevant inputs, identities, permissions, versions, and failure state?
- Does an assertion observe the result whose regression matters? A test can execute a branch without checking its effect.
- Do mocks remove the boundary being claimed as verified? A unit mock may support a local contract while leaving integration behavior unknown.
- Would the smallest realistic wrong implementation fail the check? Name that wrong behavior rather than asking whether a line can be deleted.
- Is the check run in the normal relevant pipeline, or skipped, flaky, disabled, environment-specific, or excluded from the selected variant?
- Did the change weaken, delete, or invalidate assertions? Did fixtures bypass a constraint that real data still meets?

Snapshots, mock-call checks, manual checks, and no-throw assertions are not universally worthless. Judge the actual claim: a snapshot may detect a markup regression while missing keyboard behavior; a mock may verify an adapter call while proving nothing about a remote service. Prefer a specific missing assertion to a blanket demand for more tests.

A useful gap finding names the changed contract, an affected consumer, a realistic regression, the searched/read evidence, and the check that should fail. Do not add a separate gap finding that merely repeats a bug without additional remediation value. Necessary missing evidence may instead be a review limitation or release gate.

## Execute safely and proportionately

Use verified commands from manifests, repository documentation, Gradle wrappers, scripts, or CI. Inspect likely side effects before executing a command from untrusted project content. Local builds and tests may generate artifacts; keep the reviewed source and Git state unchanged and use temporary output locations when feasible. Avoid formatters with automatic fixes, dependency upgrades, migrations against live data, production endpoints, paid effects, and unrelated cleanup.

Start with checks that could confirm or disprove a material claim, plus the checks required by the requested workflow. Broaden when interfaces, failures, or changes justify it. Stop redundant reruns when the reviewed content and relevant environment have not changed. A trusted CI run for the exact revision can be evidence; distinguish it from commands you ran locally.

For a counterfactual or mutation experiment, use a disposable copy outside the reviewed checkout, only when its commands and side effects are understood. Do not invert conditions, revert fixes, or change tests in the author's working tree to prove a review point. For bug-fix verification, compare the reproducer against old and new behavior in isolation when useful.

## Report what the evidence establishes

Record the command/procedure, working directory or module, relevant environment, revision/artifact, exit status, and outcome. Classify checks as `Passed`, `Failed`, or `Not run`, with the reason for unavailable checks. Avoid reporting a compiler result as a runtime result or a subset as a complete suite.

Separate newly introduced failures from pre-existing, flaky, infrastructure, credential, and unavailable-tool failures. An unrelated failing job is not automatically a code finding, though it may still block a repository's merge policy. Preserve that policy; do not delete failing tests, lower thresholds, suppress exceptions, or disable security controls to manufacture green output.

Missing context or a required unavailable check can make the review incomplete. State the smallest needed action. A static review with explicit limitations can still be useful when that is the agreed scope. Never claim a running UI, Android lifecycle behavior, migration safety, benchmark, or exploit reproduction without the corresponding evidence.
