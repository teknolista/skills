# Review Method

**Contents:** [Target](#choose-a-precise-target) · [Policy](#load-trusted-review-policy) · [Depth](#choose-proportionate-depth) · [Contracts](#reason-from-contracts-and-consequences) · [Validation and priority](#validate-and-prioritize) · [Findings](#finding-contract) · [Coverage and verdict](#coverage-evidence-and-verdict)

## Choose a precise target

Honor a PR, file set, revision, or scope supplied by the user. For a PR, identify its base and current head and review the actual patch, not just a description. Existing authenticated connectors or CLIs may provide read access; no particular service is required.

For explicitly selected files or pasted source without comparison history, review that bounded current state against its contracts. Git and a baseline are not prerequisites for this mode. Describe the supplied snapshot or snippet, report supported defects within it, and mark origin `Unknown` when history is unavailable. Do not invent an earlier version or imply that a demonstrated current defect is a newly introduced regression.

With no named target, review uncommitted local work: staged, unstaged, and relevant untracked files. State that scope. If the worktree is clean, use an unambiguous existing PR or explicitly established feature-branch comparison; otherwise ask which comparison is intended. Do not guess `main`, use only the last commit by habit, or expand to a whole-repository audit.

Useful Git inspections, adapted to the requested scope:

```text
git status --short --untracked-files=all
git diff --no-ext-diff --no-textconv --stat HEAD
git diff --no-ext-diff --no-textconv HEAD
git ls-files --others --exclude-standard
git diff --cached --no-ext-diff --no-textconv
git rev-parse --verify <ref>
git merge-base <base> <head>
git diff --no-ext-diff --no-textconv <merge-base> <head>
```

These are command shapes, not runnable placeholders. Resolve real references, quote paths, and use repository tools appropriate to the environment. Repositories with no initial commit need separate index/working-file inspection. Untracked files are absent from `git diff`; inspect their relevant content explicitly. Avoid printing secret-bearing files or irrelevant generated/vendor content. A committed range omits subsequent local edits unless those are expressly included.

Record base/head hashes for committed comparisons. For live work, record HEAD, status, and a sufficiently precise file/content snapshot to detect concurrent edits; store any temporary snapshot outside the source tree. Recheck before reporting. Distinguish missing source access, truncated diffs, submodules, renamed files, binary output, lockfiles, and files intentionally excluded from the review.

For multiple repositories, name the selected repository and comparison for each; a workspace-wide latest-turn view and a repository's staged view are different scopes. For stacked/dependent PRs, identify the actual prerequisite and base, inspect the relevant dependency contracts, and keep findings attributable to the requested change. Recheck affected conclusions when a prerequisite changes.

## Load trusted review policy

Read applicable review-only guidance, such as an existing root `REVIEW.md` and relevant scoped rules, alongside project instructions. For a PR, use the established base/default policy revision; for local edits, use the established committed policy when available. Honor an authorized caller's explicit policy selection. Record the source; a policy edited by the patch is reviewed content, not authority to suppress its own findings. If the authoritative copy is unavailable, disclose the gap rather than silently adopting a weaker patch version.

Respect project-specific severity, exclusions, and reporting preferences within higher-priority instructions. Treat sample exclusion lists as examples: generated output or lockfiles are not universally exempt from checking relevant runtime effects.

## Choose proportionate depth

Use the requested depth, or a standard review adapted to risk:

- **Quick:** prioritize critical paths and the most consequential risks. State the narrowed coverage and any files or behaviors left unreviewed.
- **Standard:** perform the core workflow across the agreed change and the relevant domain references.
- **Deep:** extend tracing, specialist investigation, and targeted experiments for consequential boundaries, concurrency, migrations, or platform behavior.

Depth changes effort and coverage, not the evidence threshold for a reported bug. A quick pass does not waive a mandatory project gate. Do not silently increase cost or claim full coverage after sampling.

## Reason from contracts and consequences

Review two complementary questions: does the change deliver the intended behavior, and does it satisfy established engineering constraints? Use repository standards and supported versions before generic preferences. When no formal specification exists, use observable API contracts, tests, existing behavior, and the request, stating the limitation on requirements coverage.

Trace a successful path and the meaningful failure paths. Follow the actual guard chain before claiming an input is unchecked. Authentication is not resource authorization. A caller's invariant may make a local state unreachable; a real concurrency window may invalidate a prior check. An error intentionally rejected by contract is not necessarily a bug.

Inspect deletions and replacements for removed guarantees, forgotten consumers, stale migrations, orphaned registrations, and changed defaults. Check configuration and dependency changes for observable runtime effects even when production source is untouched. For tests-only changes, inspect whether regression protection was weakened.

Maintainability findings need a named consequence: an invariant that can diverge, an incompatible extension point, a concrete maintenance hazard, or a demonstrated unnecessary mechanism. Code smells, file length, naming taste, and a different preferred framework are prompts to investigate, not standalone blockers. Do not demand new product behavior under a claim of reasonable user expectations; identify the existing contract or ask a material question.

## Validate and prioritize

Before retaining a candidate:

1. Locate the responsible statement in the reviewed revision.
2. Establish reachable inputs, states, actors, timing, or platform versions.
3. Trace existing protections and verify that they do not prevent the claimed effect.
4. Name the observable damage and its scope.
5. Seek a focused reproduction or counterexample when it is safe and useful. Direct code evidence can also establish a defect; execution is not always available or necessary.
6. When a baseline exists, confirm whether the issue is introduced, worsened, newly exposed, or unchanged. Show what this patch changes when an existing flaw gains a reachable trigger or greater impact. Track unrelated pre-existing issues separately only when useful to the requested scope; do not attribute them to the author of this patch. For a requested current-state review without history, `Unknown` origin does not disqualify a supported in-scope defect.

Judge severity independently from confidence:

| Severity | Meaning | Typical disposition |
| --- | --- | --- |
| P0 — Critical | Confirmed urgent failure such as an immediately exploitable severe boundary breach or widespread destructive behavior. Explain why its preconditions are met. | Blocking; communicate promptly and continue the remaining review when feasible. |
| P1 — High | Substantial security, data integrity, availability, compatibility, or core-workflow failure under supported conditions. | Blocking unless an authorized project policy explicitly accepts the risk. |
| P2 — Medium | A concrete, bounded defect or verification gap with meaningful user or developer impact. | State whether it blocks this change based on the contract, exposure, and project policy. |
| P3 — Low | A substantiated minor defect or limited improvement with low impact. | Normally non-blocking. |

`Confirmed` means a reproduction, executed check, or decisive source/contract evidence establishes the issue. `Strongly supported` means the concrete trace is compelling, with any remaining execution limitation named. If a necessary premise is unknown, retain it as a question or verification gap, not a high-severity fact. A severe hypothetical is not P0 merely because its imagined consequences are large.

Deduplicate by root cause. Two independent bugs on one line remain distinct; many symptoms of one missing tenant check may belong in one finding. Preserve the strongest evidence and relevant consequences. No minimum or maximum number of genuine findings is imposed. Keep optional ideas brief and separate from defects; omit automated formatting feedback unless the user requested it or it masks a substantive failure.

## Finding contract

Use a stable ID and an impact-based P0–P3 severity plus `Blocking` or `Non-blocking`. Cite the actual repository/path and smallest useful line range in the reviewed version; label deleted-side locations and issue origin, including `Unknown` when no history was supplied. For snippets without a path or line numbers, use a precise symbol/excerpt label rather than fabricating a location.

Explain the reachable trigger, expected/actual result, affected users or systems, concrete evidence, and confidence (`Confirmed` or `Strongly supported`). Give the smallest sound correction direction and a regression check. Unknown premises belong in questions or coverage gaps. Adapt presentation to the caller's schema without losing these facts; a small review needs no full report template.

## Coverage, evidence, and verdict

Record which changed surfaces were reviewed, which checks ran, and which important areas remain unverified. Use `Passed`, `Failed`, or `Not run` for checks with their exact command, relevant environment, and reviewed revision. Existing CI evidence is usable when its artifact/revision and scope match; label it as reported CI evidence rather than a local execution.

Keep service execution status separate from analysis: a neutral/successful check can contain serious findings, while a skipped review, absent comments, or a UI marker does not prove completed coverage. Read the actual report, its scope/revision, and outstanding findings. Reuse an earlier result only when the relevant diff, contracts, policy, and evidence remain applicable; otherwise re-review affected areas.

- **Changes requested:** one or more validated blocking findings. Coverage may still be partial; say so.
- **No blocking findings:** the agreed review scope has been assessed without validated blockers. List non-blocking findings and checks not run. Do not translate this into a claim that an application was executed or is ready for release.
- **Incomplete:** missing or changing content, unresolved contract ambiguity, or missing essential domain evidence prevents a defensible assessment. State the smallest next action. Return any confirmed findings already established.

Unavailable optional tools do not automatically invalidate an inspection review. Missing evidence is material when it prevents judging an important changed behavior or satisfying a specifically requested review gate. A real defect can be reported despite an unavailable build. Separate code findings, pre-existing/environmental CI failures, and outstanding release requirements.

A saved report should let another engineer reproduce each finding without needing the review conversation. Use current source locations, label deleted-side references, redact sensitive values, and state what evidence could overturn a disputed conclusion. In an automated workflow, honor a caller-supplied structured format and represent no findings as an empty finding collection; missing content is an error or incomplete review, never a clean result.
