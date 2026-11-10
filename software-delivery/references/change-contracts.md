# Choose the change contract and checks

Read when the requested change needs explicit specification, its risk or scope changes, an experiment may become maintained software, or the project generates code from a governing source. Apply the project's actual policies and the user's authorized scope. Choose independently how much the agent may do, where intent is recorded, and which checks must pass.

| Work | Minimum useful contract |
| --- | --- |
| Localized edit with clear intent, known callers, low consequence and easy recovery | Use the request and existing contract. Make the scoped edit and run the relevant check. Keep the brief in the existing request or ticket when sufficient. |
| Exploration of a design or technical uncertainty | Name the question, limits, stopping condition and observable result. Run an authorized isolated experiment with synthetic data when useful. Capture the finding and limitations for the next decision. |
| Planned feature, material behavior or boundary change, or work subject to an explicit specification policy | Establish the affected scope, behavior and checks in the authoritative change record before changing that behavior. Reuse a sufficient existing contract. Add a focused specification for the change, or a broader one when the requested scope requires it. |

Judge consequence from actual effects and consumers. A one-line change can weaken access control, alter a public contract, corrupt stored data, or make recovery harder. Sensitive data, irreversible effects, coupled teams or components, unresolved business rules and costly verification are reasons to inspect the contract and strengthen checks. Established review, security and release gates still apply to a short prompt or a small diff.

## Establish readiness before implementation

1. Identify the governing baseline and accepted changes. Derive the draft from the request, project records, examples, known constraints and observed behavior. Cite the origin of material rules and distinguish confirmed intent, delegated decisions, proposals and unknowns. Use existing tickets, specifications, schemas, decision records and checks according to what each actually governs.
2. For the scoped change, establish the outcome and exclusions, consumer contracts, representative success and failure examples, affected constraints, and how to verify them. Include migration, recovery, security, ownership and rollout where they change the design or gates. Use the level of detail that lets an implementer proceed without guessing a consequential decision. Follow project rules for the required format and approval.
3. Ask the accountable person only for unresolved consequential choices outside delegation. Record the answer, scope and dependent work. A combined specification and implementation request can proceed on settled scope under existing authority after applicable readiness gates are met. If the user or project requires the entire selected scope specified before coding, complete that scope and its required review first. Otherwise prepare and verify one coherent increment at a time.
4. Plan checks from the agreed behavior before implementing it. Preserve independent expectations when the same agent edits code and tests. Use controlled counterexamples, representative state and the real affected boundary where appropriate. A schema, test or policy can own a precise part of the contract. Link intent, rationale and constraints those checks cannot express.

## Change course and reconcile

If implementation reveals that the contract is incomplete, contradictory or infeasible, identify the affected records, consumers and checks. Keep the supported baseline, agreed change and observed implementation distinct. Correct implementation drift against the contract. For a justified change to the contract, obtain or use actual decision authority, update the owning record and recheck affected work. Preserve old results with the revisions they exercised. Resume from the reconciled contract and the next pending check.

When moving an experiment into maintained use, decide what to discard, reuse or rebuild. Review any reused source and dependencies, replace temporary data and shortcuts, establish the maintained behavior and operating constraints, and run the applicable integration and acceptance checks. Carry prototype observations only for the conditions they exercised.

When a project governs generated code through a schema, DSL or another source artifact, edit the governing source and regenerate through the established toolchain. Check the resulting diff, consumer compatibility and actual behavior. Treat unexpected generated drift as a discrepancy to resolve with the owner. Follow the project's exception policy for any direct patch. A Markdown brief or a passing test alone does not establish such a generation workflow.
