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

## Worked example with OpenSpec

A receipt endpoint is approved to scope request IDs to the authenticated tenant. The published capability defines replay. The accepted OpenSpec change adds independent tenant receipts and conflict handling. Locate the actual root, version, schema and active change. Under the default schema, read the proposal for scope, the spec delta for behavior, design for technical decisions and tasks for the implementation checklist. In a MODIFIED requirement, preserve existing scenarios that the change still supports. Inspect the complete replacement block, including cases outside the immediate fix. [Default schema](https://openspec.dev/docs/schemas/spec-driven)

Before changing the handler, use the installed CLI to inspect artifact and task status. For OpenSpec 1.16.0, examples are `openspec status --change tenant-receipts --json`, `openspec instructions apply --change tenant-receipts --json` and `openspec validate tenant-receipts --strict`. Use equivalent commands when the project uses a different version or schema. Valid artifacts establish the state of the change record. The project's accepted decision establishes intent and the implementation request establishes authority.

| Scenario in the governing delta | Check through the existing entry point |
| --- | --- |
| Two tenants use the same ID | Submit under both authenticated identities. Observe two receipts and two independent jobs. |
| Exact replay | Repeat the same tenant, ID and payload. Observe the original receipt and no additional job. |
| Conflicting replay | Change the payload for that tenant and ID. Observe the contract's conflict response and unchanged job and receipt state. |

Run relevant tests before and after the change when the baseline can reproduce the defect. Update the canonical tasks for work actually completed. Link the scenario, command, observed result, tested commit or working-tree snapshot, and limits in the project's existing verification record or the handoff when no such record exists. A test with sequential in-memory calls leaves durable and concurrent behavior unverified. The optional [OpenSpec verification skill](https://openspec.dev/docs/skills#openspec-verify-change) can supplement the comparison with the plan. If the work resumes after a revision changes, reopen the active change and diff, and rerun checks affected by the new revision. Archive when requested or required by the project's workflow after reconciliation.

## Worked example of adopting a prototype

An isolated upload prototype demonstrated that users can retry a failed submission. Record what it demonstrated with synthetic data. When asked to make it part of the maintained application, inspect the real entry point, account permissions, file limits, dependency changes and the prototype's stubbed storage. Reuse the interaction where it fits the application. Replace the stub through the owning adapter and establish the accepted behavior for failed and repeated submissions in the existing ticket or change record. Exercise successful upload, denied access and retry on the maintained implementation. Record the observed result there. Use OpenSpec if the project's workflow or user selects it for this change.
