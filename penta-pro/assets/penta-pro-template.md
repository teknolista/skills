# PENTA-PRO: Software Specification Template

**PRODUCT · PROJECT · PROOF · PROCESS · PRODUCTION**

Describe the product, solution, evidence, working method, and operation across its lifecycle, with implementation detail for the next useful increment. Keep detailed supporting material in linked project documents.

**Contents:** [Document state](#document-metadata-and-resume-state) · [PRODUCT](#1-product) · [PROJECT](#2-project) · [PROOF](#3-proof) · [PROCESS](#4-process) · [PRODUCTION](#5-production)

| Pillar | Guiding question | Primary responsibility |
| --- | --- | --- |
| PRODUCT | What should we achieve, for whom, and why? | User needs, behavior, business rules, and quality expectations. |
| PROJECT | What solution will we deliver, within which constraints? | Delivery commitments, resources, risks, and solution design. |
| PROOF | What evidence will show that the solution works and is useful? | Verification, validation, traceability, and acceptance evidence. |
| PROCESS | How will people and agents carry out the work? | Workflow, responsibilities, context, and execution boundaries. |
| PRODUCTION | How will people install, use, operate, and recover the software? | Environments, releases, monitoring, maintenance, and recovery. |

PROJECT includes both delivery planning and the technical blueprint. PROOF means evidence-based confidence, not mathematical proof. PRODUCTION applies to deployed services, installed applications, command-line tools, and distributed libraries.

**How to use this template**

- Replace `[FILL IN]` with supported project content or an explicit gap. Remove drafting instructions, sample rows, and unused forms from the deliverable. Keep the coverage decisions.
- Check links from the final document's location. Replace links to authoring resources with the relevant project artifact or remove them after incorporating the needed details.
- Identify consequential statements as requirements, constraints, decisions, or assumptions, and record their confirmation status: `Confirmed`, `Proposed`, or `Pending`. Examples and placeholders are not approved requirements.
- Resolve blocking uncertainty for the next deliverable. Record other open questions with an owner and a point by which they must be answered. Do not invent missing targets, tools, or approvals.
- Specify the first usable increment and high-risk behavior in detail; refine later work as evidence emerges. A prototype or technical experiment may resolve uncertainty before implementation.
- Keep each fact in one authoritative location. Use stable IDs and links rather than repeating requirements across pillars.
- Keep artifacts in clear English. Define supported user-interface languages separately under PRODUCT.
- Screen every pillar and relevant software or domain concern. Use a concise answer, a maintained link, or an explicit reason for a gap, deferral, or non-applicability. A small project can still have high safety, privacy, or financial consequences.
- Choose depth by consequence and stage. A low-risk internal increment may need only concise answers and links; a consequential system needs explicit contracts, threat and failure analysis, recovery evidence, and specialist review. Stop expanding a section when more detail would not change the next decision, check, or operating action.
- A useful minimum for any increment is: intended outcome and evidence, selected scope and exclusions, observable behavior and acceptance criteria, material design and dependency decisions, planned checks, execution authority, and how the result will be released, operated, or removed. Add conditional detail where consequences require it.
- Preserve existing project conventions for identifiers, artifacts, statuses, and authority. The prefixes and state vocabulary below are defaults for clarity, not a reason to rename an established register.
- Automatically fill supported facts and delegated choices with provenance. Label inferences and recommendations; ask about consequential missing decisions. Never invent research, numerical baselines, legal applicability, resources, or execution evidence.

## Document metadata and resume state

| Field | Value |
| --- | --- |
| Template version | 1.7.1 |
| Product name and one-sentence purpose | [FILL IN] |
| Document owner and decision-makers | [FILL IN] |
| Specification version, updated date, and document status | [FILL IN: Draft / Reviewed / Accepted / Superseded] |
| Target release or increment | [FILL IN] |
| Change context and baseline | [FILL IN: new software, evolution, replacement, or investigation; existing revision when relevant] |
| Repository and authoritative specification location | [FILL IN] |
| Supported platforms and distribution channel | [FILL IN] |
| License and ownership constraints | [FILL IN] |
| Related feature specifications, decisions, and runbooks | [FILL IN] |
| Applicable software profiles and domain concerns | [FILL IN: combine relevant types and overlays] |
| Current specification focus | [FILL IN: discovery / feasibility / implementation / operation; descriptive, not an approval] |
| Next increment readiness | Not assessed |
| Readiness scope, assessor, basis, and date | [FILL IN after assessment] |
| Pending question references | [FILL IN: PROJECT question IDs; identify blockers] |
| Last completed focus | [FILL IN] |
| Next action | [FILL IN] |

`Confirmed` means supported by cited project evidence or a decision made by the responsible person or an agent within explicit delegation. Identify the decision-maker and source of authority; an agent choice is not a user requirement or document acceptance. `Proposed` means a recommendation awaiting a decision. `Pending` means missing, disputed, or unresolved information; link it to an open question in PROJECT. Keep verification results separate: a confirmed requirement can still be unverified.

Assess next-increment readiness as `Not assessed`, `Blocked`, or `Ready for the next increment` against the conditions in PROCESS, with reasons and unresolved question references. Document and readiness statuses describe specification state; they do not authorize implementation, spending, external actions, merge, or release. Record actual authority, its source, and scope under PROCESS.

`Not applicable` means irrelevant for a stated reason. `Unknown` means evidence is missing; `Undecided` means a choice is outstanding; `Disputed` means sources conflict. These are reasons for `Pending`, not evidence of non-applicability. `Deferred` means relevant but scheduled for later, with an owner and trigger; it cannot hide a blocker for the selected increment. An assumption can be authorized for planning while its truth remains unverified.

### Specification at a glance

- **Problem, audience, and evidence:** [FILL IN: link PRODUCT sources; distinguish hypothesis from observation].
- **Product bet and principles:** [FILL IN: vision, why now, differentiation, and decision heuristics].
- **Expected outcome and guardrails:** [FILL IN: objective/measure references].
- **Selected increment and exclusions:** [FILL IN: requirement/non-goal references; retain future scope].
- **Solution direction and constraints:** [FILL IN: decision references, alternatives, and trade-offs].
- **Principal risks, unresolved decisions, and next action:** [FILL IN: canonical IDs and affected work].
- **Decision or approval requested:** [FILL IN: what the reader must decide; do not infer authority].

Keep this a short linked summary, not a second specification.

Where readers have different responsibilities, give each audience a short route from the summary to the records they need to review and the decision or feedback expected. Use the gate records in PROCESS for actual approvals.

### Coverage and authoritative artifacts

| Pillar / concern | Disposition | Detail or canonical artifact / revision | Owner | Reason / resolution trigger |
| --- | --- | --- | --- | --- |
| [FILL IN: all five pillars, then material conditional concerns] | Included / Linked / Pending / Deferred / Not applicable | [FILL IN] | [FILL IN] | [FILL IN] |

Record the source of truth for contracts, designs, decisions, test plans, and runbooks. `Included` means the specification covers the concern directly. Use `Linked` when the artifact is accessible, current enough for the decision, and contains the needed detail. Use `Pending` for unresolved applicability or material gaps, including inaccessible or contradictory links, and reference the PROJECT question. For `Deferred`, state when the work returns and who owns it. For `Not applicable`, state the basis for excluding it.

When inline detail becomes hard to navigate or has an independent review or update cycle, use this index or a filtered view to link feature specifications, increment plans, and contracts by stable ID. Record their owner, revision, status, and related requirement or evidence IDs where useful. Keep the shared outcomes, scope, requirements, and cross-feature decisions findable from the main specification. Generate machine-readable views only for a real consumer, with a defined synchronization rule.

### Glossary and revision history

Define ambiguous domain terms, acronyms, units, and overloaded roles once. Preserve stable IDs when editing; retire or supersede records explicitly rather than reassigning IDs. Existing project identifiers take precedence over the illustrative prefixes used here.

| Term | Meaning / boundary | Authoritative reference |
| --- | --- | --- |
| [FILL IN] | [FILL IN] | [FILL IN] |

| Version / date / author | Material change and reason | Affected IDs / artifacts | Decision or acceptance reference |
| --- | --- | --- | --- |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN: none if not accepted] |

Link existing version history where sufficient; record semantic changes and supersession, not every wording edit.

### Identifiers and status vocabulary

Use stable identifiers for records that are referenced, reconciled, or checked. Reuse existing project prefixes; those below are defaults, not a required scheme.

| Prefix | Typical record | Authoritative home |
| --- | --- | --- |
| `DISC`, `OBJ`, `MET` | Discovery finding, objective, measure | PRODUCT |
| `REQ`, `AC`, `FEAT`, `NG` | Requirement, acceptance criterion, feature, non-goal | PRODUCT |
| `ASM`, `OPEN`, `RISK`, `DEC`, `DEP` | Assumption, open question, risk, decision, dependency | PROJECT |
| `CHECK`, `VAL`, `EVID` | Planned check, validation activity, execution evidence | PROOF |
| `TASK`, `REL`, `RB` | Task, release, runbook | PROCESS for tasks, PRODUCTION for releases and runbooks |

These status vocabularies are distinct and may coexist:

| Dimension | Values | Meaning |
| --- | --- | --- |
| Document | Draft / Reviewed / Accepted / Superseded | State of the specification itself. |
| Statement confirmation | Confirmed / Proposed / Pending | Basis for believing a requirement or decision. |
| Record lifecycle | Active / Deferred / Superseded / Retired | Whether a record still governs current work. |
| Verification | Pass / Fail / Unverified | Result for a stated revision and procedure. |
| Readiness | Not assessed / Blocked / Ready for the next increment | Whether the selected increment is sufficiently specified to proceed once authorized. |
| Decision | Proposed / Accepted / Superseded / Rejected | Authority and current applicability of a choice. |
| Availability | Project-defined stage and cohort | Who can use a feature or release, for example pilot, generally available, or deprecated. Record actual authority separately in PROCESS. |

Do not collapse these into a single `done` or `approved`. A confirmed requirement can be unverified; an accepted decision can later be superseded; readiness does not grant implementation, spending, merge, or release authority. Never reuse a retired identifier. When confidence changes a decision, record its basis (measured, observed, expert judgment, or assumption) and whether it is a one-way or two-way door; reversible low-consequence choices can be delegated, while irreversible or high-consequence choices need explicit authority.

A **material** statement or change is one that could alter scope, behavior, acceptance, design, authority, cost, or operations. A **blocking** condition prevents the selected increment from proceeding or the specification from being accepted; routine choices within delegated authority are neither.

## 1. PRODUCT

Define the intended value and observable behavior. Technical implementation choices belong in PROJECT; evidence that behavior is achieved belongs in PROOF.

### Strategy, principles, and stopping criteria

Record the product bet before listing features. Keep this concise and conditional; an internal tool may need one sentence, while a commercial product may need a business case.

- **Vision and strategic intent:** What future state should this product create, in one or two sentences, and over what horizon?
- **Why now and why this:** Which change, evidence, or constraint makes this worth doing now, and why is this solution direction credible?
- **Principles and decision heuristics:** Which three to seven rules should resolve recurring trade-offs? Examples include “no silent data loss,” “offline-first,” “reversible changes by default,” or “human review before irreversible actions.” A principle is a guide for delegated choices, not a new requirement.
- **Business and stakeholder alignment:** Link relevant organizational objectives, funding, contractual commitments, or portfolio priorities where they exist. Do not invent an OKR, business case, or market claim.
- **Alternatives and differentiation:** Compare build, buy, reuse, extend the current process, and do nothing when credible. State why users would choose this option and what would make that advantage temporary or weak. Market size, pricing, and competitive research are conditional, not universal.
- **Success and stopping criteria:** Define what would count as product success, what evidence would invalidate the core hypothesis, and what result should cause the team to stop, narrow, or change direction. These are product decisions, distinct from technical failure handling.

Scope boundaries, users, journeys, and measurable outcomes belong under the next heading. Project selection of the current release belongs in PROJECT.

### Problem, users, and outcomes

- **Problem and current alternatives:** What difficulty exists, and what evidence supports it?
- **Users and stakeholders:** Who uses, buys, administers, supports, or is affected by the software?
- **User journeys:** What tasks should users complete, in which real-world conditions?
- **Value and success measures:** Define the intended outcome, current baseline if known, target, measurement method, and evaluation window. Label untested beliefs as hypotheses.
- **Product boundaries:** Identify included capabilities, explicit non-goals, and unacceptable outcomes even if the software technically works. PROJECT selects which requirements belong in the current release.

### Discovery evidence and user context

| Evidence / hypothesis ID | Finding or belief and affected segment | Source, method, date, and scope | Limitations / contradictory evidence | Related objective / validation plan |
| --- | --- | --- | --- | --- |
| DISC-001 | [FILL IN] | [FILL IN: actual research or explicitly untested hypothesis] | [FILL IN] | [FILL IN] |

For each segment that changes requirements, describe its task, current workaround, frequency/severity of the problem, capabilities, accessibility needs, environment, devices, connectivity, and barriers to adoption. Distinguish user, buyer, administrator, operator, and affected non-user. Personas are optional; do not invent biographies, interviews, or sample sizes.

Explain why this problem matters now and the credible alternatives, including reuse, purchase, or leaving the current process unchanged. Record commercial viability, pricing, procurement, or adoption constraints only when relevant. Compare current and intended journeys and identify how evidence could invalidate the proposed direction.

### Outcomes and measurement

| Objective / measure ID and kind | Definition, population, and unit | Baseline / source and proposed or confirmed target | Window / evaluation owner | Data source / instrumentation | Guardrail and decision trigger |
| --- | --- | --- | --- | --- | --- |
| OBJ-001 / MET-001; user, business, or technical | [FILL IN: formula and denominator if relevant] | [FILL IN: unknown is allowed] | [FILL IN] | [FILL IN: measured locally, manually, or by justified telemetry] | [FILL IN] |

Distinguish leading indicators, eventual outcomes, and guardrails. An operational health metric does not by itself demonstrate user value. Define comparison/baseline, observation window, sample limitations, and what result leads to continue, change, or stop. If a baseline is missing, plan its collection; do not fabricate a target or percentage improvement.

For each required analytics event, specify trigger, schema/version, minimal properties, owner, deduplication, allowed purposes, access, retention, and applicable consent/opt-out behavior. Link the implementation contract in PROJECT and collection checks in PROOF. Do not require network telemetry for local or privacy-constrained products.

### Domain, data, and access

- Define domain terms, actors, conceptual entities, relationships, and business rules using stable identifiers where useful.
- Describe business invariants: conditions that must remain true across operations, including failure and concurrency.
- Specify permissions by role, action, and resource ownership. Include administrative and cross-tenant behavior when applicable.
- Identify data owners, sensitivity, sources, allowed purposes, retention, deletion, export, and applicable obligations. Record the responsible decision-maker for unresolved obligations.
- Describe entity lifecycles, allowed transitions, prerequisites, and visible effects. Add a state diagram when it clarifies complex behavior.

### Privacy, obligations, and inclusive use

- Map relevant data categories to purpose, owner, storage/residency, cross-border transfer limits where applicable, recipients, permitted access, retention, deletion/export, backup treatment, and any consent or permission withdrawal behavior. Link the detailed data contract in PROJECT.
- Record each applicable contractual, legal, licensing, accessibility, safety, or industry obligation with source/version, jurisdiction or scope, responsible reviewer, affected requirements, and required evidence. Applicability and interpretation must be established by the responsible authority; a populated template does not establish compliance.
- Specify accessibility targets and affected journeys, assistive technologies, keyboard/focus behavior, non-visual alternatives, readable content, time limits, cognitive load, and verification method where relevant. Record the chosen standard and version if one applies; do not assume one universal target.
- For localized products, define locales, translation/content ownership, formats, time zones, units/currencies, pluralization, right-to-left behavior, and fallback. Separate document language from product language.
- Identify material misuse, abuse, fraud, physical or social harm, and affected groups. Specify prevention, human review, explanation, appeal, or safe failure where the consequence warrants it. Link threats and hazards to PROJECT and PROOF.
- Where the product can materially affect workers, non-users, communities, or the environment, assess who bears the impact and under what conditions. Consider unequal outcomes, changes to work and fallback access, and resource or energy use. Translate material impacts into requirements, verification scenarios, and an accountable response using the relevant profile.

### Requirements and quality targets

Record functional and quality requirements in one register. Use `Must`, `Should`, `Could`, and `Won't in this release` deliberately; priority does not replace acceptance criteria.

| ID / kind | Requirement and reason | Source / parent objective or requirement / owner | Priority / increment | Confirmation / lifecycle | Feature / acceptance / proof reference |
| --- | --- | --- | --- | --- | --- |
| REQ-001; functional / quality / constraint | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

Keep each requirement independently interpretable and verifiable. Check that it is atomic, unambiguous, necessary, feasible, and consistent with other requirements. Express behavior in observable terms. If an external obligation or an existing platform fixes part of the implementation, record it as a constraint with its source. Link consequential dependencies, conflicts, and derived requirements to their origins and rationale. Distinguish permanent non-goals from scope deferred to a later increment, and give both IDs when other records need to reference them.

When prioritization or sequencing is contested, record the method and rationale used (for example MoSCoW, cost of delay, value/effort/risk/confidence, or an explicit stakeholder decision). Priority is not the same as release scope, and a high-priority item can still be deferred.

For quality requirement IDs already listed in the register, use the table below to supply measurement details rather than duplicate their definitions. Consider functional suitability, performance, reliability, security, privacy, accessibility, usability, compatibility, localization, maintainability, portability, interoperability, operability, supportability, safety, sustainability, and resource use. These are screening prompts, not automatic requirements. An established taxonomy such as ISO/IEC 25010 may be used as a checklist when it helps, but no standard is mandatory by default.

| ID | Attribute / user journey | Target and applicable baseline or basis | Workload, platform, and measurement window | Proof reference |
| --- | --- | --- | --- | --- |
| [Existing quality requirement ID] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

For performance, specify the percentile, dataset size, concurrency or request rate, network conditions, and acceptable error rate where relevant. Avoid unexplained numbers such as a universal response-time or coverage target.

### Feature specification — repeat for each coherent feature

For linked feature specifications, point readers to their canonical records through the coverage index above.

- **Feature ID and title:** `[FILL IN]`.
- **Purpose and requirement references:** `[FILL IN]`.
- **Actors and permissions:** `[FILL IN]`.
- **Preconditions, inputs, and postconditions:** `[FILL IN]`.
- **Main journey:** Describe the steps and observable outcomes.
- **Alternative and failure journeys:** Include invalid input, denied access, unavailable dependencies, cancellation, partial completion, and recovery where applicable.
- **Business rules and state transitions:** Reference the domain definitions; describe feature-specific rules here.
- **Interface behavior:** Specify screens or commands, navigation, inputs, outputs, validation, and relevant responsive or accessibility behavior.
- **UI states, when applicable:** Initial, loading, empty, populated, submitting, success, error, denied, stale or offline, and retry. Specify only meaningful states; optimistic updates require defined failure behavior.
- **Content and design:** Link the approved design system. Include labels, error messages, and accessibility names when exact wording matters. Mark draft copy explicitly.
- **Navigation and interaction:** For relevant interfaces, map entry/exit, deep links, back/undo, focus, interruption/resume, unsaved work, and responsive behavior. For content-driven products, define content sources, publishing/review, translation, ownership, and expiry.
- **First use and activation:** Where relevant, define the initial state, permissions or setup, onboarding or guidance, and the first observable useful result. Do not assume a returning, expert user.
- **Feature lifecycle and availability:** Record the relevant lifecycle state and the planned or actual availability separately. Include cohort, flags, or entitlements where they change who can use the feature.
- **Acceptance criteria:** Assign IDs such as `AC-001`. Describe observable outcomes using Given / When / Then or equally precise statements. Include meaningful negative and boundary cases. For behavior with variable outcomes, define a repeatable evaluation with representative inputs, tolerances or scoring criteria, and a decision rule. Make the criteria usable by someone who did not write the code.
- **Dependencies and unresolved decisions:** `[FILL IN]`.

Use a behavior table when it clarifies complex features; do not repeat simple prose in a second form.

| Situation / AC ID | Input, actor, and prior state | Expected output / effect / next state | Failure, recovery, and irreversible effects | Proof reference |
| --- | --- | --- | --- | --- |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

## 2. PROJECT

Define a feasible delivery commitment and the technical blueprint that supports it. This pillar covers more than scheduling: it connects scope and constraints to solution design.

### Delivery boundaries and resources

- **Current release:** Link the selected requirement IDs and explain the smallest useful outcome.
- **Milestones:** Define deliverables, dependencies, owners, and deadlines; distinguish fixed constraints from estimates.
- **Resources and budget:** Record available people, tools, environments, development costs, agent usage limits, and expected operating costs. Note material knowledge concentration, single-person dependencies, and backup ownership where they threaten delivery.
- **Decision rights:** Identify who owns product priorities, technical decisions, acceptance, and releases.
- **Trade-offs:** State what takes priority when scope, time, cost, maintainability, or quality conflict. Identify constraints that cannot be traded away.
- **Estimation basis:** Record method, range, assumptions, evidence, and uncertainty; distinguish forecasts from commitments. Include procurement, vendor limits, team availability, and licensing constraints when material.

| Dependency ID / deliverable | Provider / accountable owner | Consumer / affected requirement | Needed-by condition / commitment evidence | Fallback and escalation |
| --- | --- | --- | --- | --- |
| DEP-001 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

For consequential third-party dependencies, link the actual service commitments, limits, commercial or renewal constraints, and an exit path for replacing the dependency or exporting its data. Record unavailable commitments as gaps with the affected scope.

### Risks, assumptions, and open decisions

| ID / kind | Statement / source | Impact / affected IDs / blocking condition | Owner | Resolution, validation, or mitigation | Needed by / status |
| --- | --- | --- | --- | --- | --- |
| OPEN-001 / question; ASM-001 / assumption; RISK-001 / risk | [FILL IN: one record per row] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

Separate evidence from assumptions. Use a limited experiment when a consequential assumption can be tested cheaply. Escalate only the work blocked by an unresolved decision.

- For assumptions: record basis, validation/invalidation method, deadline, and who authorized proceeding if consequential; permission does not prove the assumption true.
- For risks: record likelihood and impact with rationale, prevention, detection/trigger, mitigation, residual risk, and acceptance owner. Avoid unsupported numerical precision.
- For questions: distinguish unknown, undecided, and disputed; identify the decision that depends on the answer and its resolver.
- For spikes/experiments: record question, bounded effort, method, success/failure or inconclusive criteria, expected evidence, owner, stopping condition, and decision enabled. Describe the plan without claiming it ran.
- Track intentional technical/specification debt with consequence, owner, reason, and review/repayment trigger. Do not call deferred blocking work complete.

### Solution architecture and technology

- Describe system boundaries, components, responsibilities, trust boundaries, and data flow. Include a diagram when useful.
- Select the simplest architecture that meets the requirements. Explain significant alternatives and trade-offs.
- Record approved runtimes, versions, frameworks, libraries, storage, and external services with rationale. Inventory existing systems, contracts, data, and platform constraints that the solution must reuse or preserve, with their owner and imposed limitation.
- For existing software, distinguish observed behavior, required compatibility, and intended changes. Identify consumers and older data affected by the change. Link representative characterization checks and regression coverage, and record discrepancies between observed behavior and accepted requirements for resolution.
- Document meaningful decisions with status, requirement links, rationale, consequences, and conditions for reconsideration. An accepted decision can later be superseded explicitly.
- Define module boundaries, repository structure, important conventions, and actual reference implementations. Apply patterns where they solve a demonstrated problem.

| Decision ID / status | Context / affected requirements | Options and trade-offs | Choice / rationale / consequences | Decision-maker / authority / date | Revisit trigger / supersedes |
| --- | --- | --- | --- | --- | --- |
| DEC-001; Proposed / Accepted / Superseded / Rejected | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

Record the evidence basis for consequential decisions (measured, observed, expert judgment, or assumption) and whether the choice is a one-way or two-way door. Reversible, low-consequence choices can usually be delegated; irreversible or high-consequence choices need explicit authority and stronger review. Decision acceptance records the authorized decision, not acceptance of the entire specification. Link existing architecture decision records instead of duplicating them. Use context, component, deployment, sequence, state, or entity diagrams when they resolve real ambiguity; no diagram notation is mandatory.

Model expected and peak workload, data growth, resource limits, critical bottlenecks, scaling/degradation strategy, and cost drivers where they influence feasibility. State units and assumptions, distinguish measured values from estimates, and link validation in PROOF and operational triggers in PRODUCTION.

### Data design and integration contracts

- Define logical schemas, constraints, identifiers, relationships, and ownership; add physical schema and indexing choices where needed.
- Specify transaction boundaries, consistency requirements, concurrent-update behavior, deduplication, and migration compatibility.
- For each API, event, file format, or external service, identify its owner and authoritative contract. Define schemas, validation, authorization, errors, compatibility, and versioning.
- Specify timeouts, cancellation, retryable failures, retry limits, and duplicate-request handling per operation. Repeated requests must not accidentally repeat irreversible effects.
- Define partial-failure handling and compensation where needed. Distributed transactions, queues, and circuit breakers require a stated reason.
- Identify security threats and map mitigations to relevant requirements and verification checks. Include secret handling, tenant boundaries, and dependency risks where applicable.

Use the [detailed patterns](../references/specification-patterns.md) for data dictionaries, interface contracts, and threat or hazard models when a maintained artifact does not already cover the concern. For instrumentation, link the collection semantics in PRODUCT and operating limits in PRODUCTION. Record any design-specific schema, correlation, redaction, or failure behavior here.

Store details once, link requirement IDs, and flag unavailable vendor guarantees. Use maintainable formats such as OpenAPI, AsyncAPI, schema files, or native headers where appropriate. Verify provider conformance separately.

### Interface and implementation conventions

- For visual interfaces, link the selected visual reference or design system with its approval status: components, tokens, themes, layouts, and accessibility expectations. Mark this not applicable for non-visual products; retain their interface contracts.
- Define project-specific code, dependency, error, logging, and documentation conventions. Distinguish mandatory rules from preferences.
- Explain compatibility constraints and forbidden patterns by their impact. Avoid arbitrary limits that encourage mechanical splitting or unnecessary abstractions.

## 3. PROOF

Specify how the team will verify requirements and validate that the product serves its users. Define the checks before implementation; collect evidence as work proceeds.

### Acceptance and traceability

Keep acceptance criteria beside their feature in PRODUCT. Link each requirement and criterion to a check and its execution evidence here.

| Requirement / criterion | Task or change | Verification method | Result | Evidence and tested revision |
| --- | --- | --- | --- | --- |
| [FILL IN] | [FILL IN] | [FILL IN] | Pass / Fail / Unverified | [FILL IN] |

Evidence identifies the tested commit or artifact, environment, relevant data, command or manual procedure, expected and actual outcome, and execution date. A planned check or an unexecuted test remains `Unverified`.

Trace the value chain: objective/discovery → requirement → acceptance criterion → design/contract and task → check/evidence → outcome evaluation. Reuse the canonical IDs and links. For the selected increment, flag missing or orphan references and report failed, unverified, or stale evidence. Retain historical results with their tested scope. Recheck after changes that affect a result or when the gate requires the exact revision. Where the gate permits prior evidence, document why changed inputs, requirements, or conditions cannot affect the result. Use existing automation for structural checks such as duplicate IDs, missing owners, broken links, or missing verification.

### Verification and validation strategy

- Choose unit, integration, contract, end-to-end, manual, or other checks according to behavior and risk. Define representative fixtures and isolate side effects.
- Use inspection or static analysis for structural constraints and analysis, simulation, or formal methods where they fit the claim or are required. Record assumptions and the limits of each method, including where target hardware or runtime evidence is needed.
- For critical rules, record concrete inputs and expected outputs derived from product requirements, independently of the implementation. Use these examples to check both the software and its tests.
- Test important failures and boundaries: denied access, malformed input, duplicate actions, concurrent updates, dependency failures, and partial completion as applicable.
- For UI changes, inspect relevant flows in the running application, including keyboard use, supported layouts, and error recovery. A successful build alone does not establish usable behavior.
- For critical or hard-to-test logic, add techniques that fit the actual risk — property-based tests, fuzzing, fault injection, or controlled load/chaos exercises — when they offer meaningful additional assurance. Record the technique choice and rationale where the consequence warrants it; advanced techniques are an investment decision, not a standing requirement.
- Define reproducible workload and environment details for performance checks. Validate security controls against the selected threat model and applicable requirements.
- Specify how representative users or a responsible stakeholder will validate the intended outcome. Passing technical tests does not establish product usefulness by itself.
- Identify checks that must recur as the system, dependencies, or usage change, such as performance after growth, accessibility after UI changes, dependency vulnerability review, and recovery drills. Record the cadence, owner, and action when a recurring check fails.
- Document the chosen test-first policy and any coverage targets in one place. Coverage is supporting evidence, not a substitute for meaningful assertions or behavioral checks.
- Use independent review for changes that require it. Provide the reviewer with requirements, the actual diff, relevant context, and evidence; review approval does not replace execution checks.

### Risk coverage and test data

| Risk / requirement / AC IDs | Failure or boundary to exercise | Method / environment / data | Expected result / check reference | Owner / evidence or gap |
| --- | --- | --- | --- | --- |
| [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

Select checks for material risks, including migration, isolation, concurrency, recovery, accessibility, security, load, or device compatibility as applicable. Define regression selection for changed behavior and contracts, critical always-run checks, environment differences, and how flaky checks are investigated without silently removing a gate.

Specify fixture provenance, realistic volumes/distributions, edge/invalid cases, privacy protection, reproducible generation/seeds when useful, setup/reset/cleanup, and ownership. Prefer synthetic or appropriately de-identified data; record required access without including credentials. Keep unavailable environments and manual-only checks visible. Define defect severity by user impact, triage ownership, and which severity blocks each gate.

### User validation and experiments

| Validation ID / objective or hypothesis | Method / representative participants or stakeholder | Scenario / baseline or comparison / window | Success, failure, guardrails, and limitations | Owner / decision / evidence |
| --- | --- | --- | --- | --- |
| VAL-001 | [FILL IN: planned or actually recruited; distinguish them] | [FILL IN] | [FILL IN] | [FILL IN] |

Choose usability sessions, prototypes, acceptance walkthroughs, pilots, offline evaluation, or controlled experiments as appropriate. Plan how findings change the product decision and how actual participant/data access will be obtained. Do not equate technical test passes with product usefulness or infer causation from an uncontrolled metric change.

### Quality gates and exceptions

Define the checks required for a task, integration, and release, including their commands and owners. Keep one authoritative set of thresholds. Match checks to the risk and retain mandated project checks.

- Required acceptance criteria pass. A failed or unverified required check blocks the affected gate unless an explicitly authorized exception is recorded below.
- Required build, analysis, tests, and review have evidence for the relevant revision.
- Material findings are resolved; changes after verification trigger the affected checks again.
- Documentation, configuration, compatibility, and operational impacts are addressed.
- Any authorized exception records its owner, rationale, impact, mitigation, and expiry or follow-up. Do not weaken checks silently to obtain a pass.

An authorized exception leaves the underlying result `Fail` or `Unverified`. Record the separate gate disposition and revisit trigger. Check that the decision-maker has authority to waive the specific condition. Keep non-waivable obligations and constraints blocking until satisfied or formally changed by the responsible authority. Link gate ownership in PROCESS.

### Post-release validation

For the released revision and cohort, link product measures and operational signals, observation windows, responsible evaluator, acceptable result, and actions for regressions or inconclusive evidence. Define who may pause rollout, disable a feature, roll back, or schedule follow-up. Schedule the outcome review and record whether the original assumptions held, unexpected user behavior, support and cost impact, and the resulting product or specification changes. Record actual deployment, rollback, restoration, and outcome evidence only after execution; include artifact/data scope, timestamp, result, and unresolved gaps.

### Learning and effectiveness

Track product outcomes alongside delivery indicators such as time to an accepted increment, escaped defects, rework, operating cost, and human interruptions. Record baselines and compare similar work. Use findings to improve the specification and workflow; do not treat generated code volume as a success measure.

For material escaped defects or recurring incidents, record the affected requirement/check references, detection stage, supported causal findings, fix, regression coverage, and an owned prevention action. If the cause remains unknown, retain the uncertainty with the investigation or risk decision and follow-up trigger. Record recovery and longer-term corrective work separately.

## 4. PROCESS

Define how people and agents transform agreed work into a reviewed change. PROOF defines the evidence required at each gate; PRODUCTION defines operational actions.

### Development cycle — repeat for each increment

PROCESS governs the entire cycle. Consult relevant material from all five pillars for each task; their document order is not a sequence of execution phases.

Define the project's cycle from selecting an outcome and preparing checks through implementation, review, integration, and authorized release. Identify the required evidence and responsible role at each transition. Recheck affected behavior after fixes or integration, and feed feedback into tracked work and the relevant pillars.

| Stage / handoff | Responsible worker / accountable decision-maker | Input and output artifacts | Gate / evidence reference | Escalation or backup |
| --- | --- | --- | --- | --- |
| [FILL IN: actual workflow, including feedback] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

Use a formal plan when complexity or uncertainty warrants it. Planning-only requests produce investigation and a proposal; they do not authorize implementation. Define any required plan approval explicitly.

### Increment readiness, authority, and completion

Assess these conditions for the selected increment, retaining unresolved items with owners and scope:

- Outcome, users, selected scope, exclusions, and evidence/hypotheses are explicit.
- Behavior, permissions, important failures, quality constraints, and observable acceptance criteria are sufficient for implementation.
- Necessary design, contracts, dependencies, feasibility, privacy/safety concerns, and operational constraints are resolved or covered by explicitly authorized assumptions with validation plans.
- Required checks are feasible; environments, access, representative data, and responsible roles are available when needed. A missing prerequisite for the next work is a blocker; future release evidence may remain planned.
- Blocking questions/conflicts are resolved; deferrals have no hidden dependency in this increment.
- Ownership, handoff, and exception or escalation rules are known. Identify who can authorize execution and record actual authorization separately. An implementer can proceed without guessing consequential product decisions once authorized.

Mark `Blocked` if any unmet condition prevents this increment; record what would unblock it, who owns the resolution, and any project-defined response expectation. Do not label routine choices within delegated authority as blockers, and do not convert a count or percentage of completed sections into readiness.

Before recording specification acceptance, review the selected revision. Check coverage dispositions and canonical links, sources and observable acceptance for scoped requirements, feasible planned checks for scoped `Must` requirements, and measurement details for scoped quality targets. Identify any gaps, their owners, the affected increment or gate, and the needed-by point. Record what the responsible person actually accepted, including scope, revision, date, and conditions. A review can find the document coherent while the increment still has a blocker. Assess its readiness and authorization separately.

| Gate or authority | Responsible assessor / decision-maker | Required basis | Actual state / source / date / scope |
| --- | --- | --- | --- |
| Specification reviewed / accepted | [FILL IN] | Review findings resolved or recorded; actual acceptance by responsible person | [FILL IN: no acceptance inferred] |
| Increment ready | [FILL IN] | Checklist above and material assumption decisions | Not assessed |
| Implementation / spending / external actions authorized | [FILL IN] | Actual request or policy and its limits; separate actions as needed | [FILL IN: existing authorization remains valid] |
| Task done / integration eligible | [FILL IN] | Applicable PROOF checks, review, documentation, and addressed impacts | [FILL IN: not assessed before execution] |
| Release authorized | [FILL IN] | Release evidence, operational readiness, accepted exceptions, actual authority | [FILL IN] |
| Launch or public availability authorized | [FILL IN] | Applicable docs, support, training, communications, pricing/billing, legal terms, analytics, and on-call readiness | [FILL IN or Not applicable] |
| Post-release outcome evaluated | [FILL IN] | Planned observation and actual evidence linked in PROOF | [FILL IN] |

These records do not impose a new approval ceremony. The same person may own several roles; honor authority already granted. Completion of a coding task need not mean deployment, and a ready specification does not mean verified software.

### Task definition

A task is ready when its goal, scope, acceptance criteria, dependencies, necessary contracts, and decision authority are sufficiently clear. A task should deliver a verifiable increment; avoid splitting work solely by technical layer when that prevents usable outcomes.

| Task field | Required information |
| --- | --- |
| Identity and outcome | Task ID, requirement references, user-visible result, and out-of-scope work. |
| Inputs | Relevant source files, specification sections, contracts, and prior decisions. |
| Execution | Owner, dependencies, permitted changes, and relevant environment. |
| Completion | Acceptance references, required checks, review requirements, and handoff location. |

Use these checks as a project-adaptable definition of ready and done, not a universal ceremony:

- **Ready to start:** the outcome and scope are clear; relevant requirements are confirmed; acceptance criteria are observable; dependencies, contracts, environment, and test data are available; blocking decisions are resolved or explicitly out of scope; execution authority is known.
- **Done for this task:** required behavior is implemented; applicable checks pass for the actual revision; acceptance evidence is recorded; review and documentation updates are complete; configuration, migration, compatibility, and operational impacts are handled; handoff is recorded. Done does not automatically mean deployed or launched.
- **Specification accepted is not increment ready.** Acceptance means the document is coherent and its gaps are visible; readiness means the selected increment can proceed without guessing a consequential product decision.

### Agent responsibilities and authority

- Define concrete responsibilities, inputs, outputs, and tool access for implementation, review, and coordination. Use separate roles only when useful.
- Record permitted local edits, external actions, costs, merge authority, and release authority. Do not infer permission to deploy from permission to implement or merge.
- Continue authorized work without repeatedly requesting the same approval. Group non-blocking questions; escalate material scope changes or unresolved high-impact decisions.
- When running work in parallel, record dependencies and ownership, isolate conflicting changes, limit concurrency, and define the integration order.
- Set time, cost, and retry limits for automated runs. Define escalation conditions, cancellation behavior, and how work resumes without duplicating external actions.
- Keep durable task status, decisions, blockers, and evidence in the existing tracker or agreed file. Avoid maintaining contradictory task lists.
- Identify accountable owner, worker, backup/escalation, material-change boundaries, and response expectations when needed. Use human-only or mixed workflows without requiring agents.
- For automated work, specify input/context versions, output/schema expectations, acceptance rubric, consequential human checkpoints, usage budgets, and fallback if a model, tool, or skill is unavailable. Use independent evidence for generated claims. Record useful run/tool/decision traces with redaction and retention; do not require private model reasoning. Where generated or reused code is subject to provenance or licensing constraints, record those constraints with the review they require.
- On interruption or cancellation, save completed work, pending side effects, evidence, ownership, and a safe resume step. Reconcile actual external state before retrying; avoid duplicate actions.

### Context, skills, and change control

- Keep `AGENTS.md` focused on durable instructions and navigation. Store detailed requirements, feature specifications, decisions, and runbooks in their authoritative locations.
- Load the context needed for the current task. Identify source, version, and status when retrieving external or historical material; distinguish reference content from authorized instructions.
- Maintain a small registry only for skills and tools actually selected for the project: source/version, availability, trigger, inputs, outputs, permissions, and fallback if unavailable.
- Define the actual branch, commit, review, and CI conventions. Do not assume a branch name, installed skill, file path, or approval policy.
- When requirements change, assess affected tasks, contracts, tests, and operations; update their references and record the decision.
- At handoff, report changes, verification results, unresolved issues, and the exact next action when one is needed.
- Provide a short onboarding route through the authoritative specification, setup, sample task/check, current decisions, and escalation contact. Link the existing contributor guide when available.
- Define communication channels, decision turnaround, review cadence, and cross-team sync only where coordination needs them. Use the project's actual branch/CI baseline with rationale, not an assumed universal workflow.
- For a material change, identify source/reason, affected objectives and requirements, design/contracts, checks/evidence, schedule/cost, operations, and authority; record accepted/deferred/rejected disposition, update authoritative artifacts, and invalidate stale results. Track unresolved specification debt with owner and resolution trigger.
- When owners disagree or instructions conflict, record the arbiter, decision criteria, and expected resolution point. Pause only the work that depends on the unresolved choice instead of continuing on contradictory assumptions.

## 5. PRODUCTION

Define how the software reaches actual users and remains usable. Adapt this pillar to the distribution model; a local tool may need installation and upgrade instructions without cloud infrastructure.

### Environments, setup, and configuration

Document required runtimes, services, supported platforms, access, and meaningful differences between development, test, staging, and production. Use isolated test data and credentials. Keep important validation and authorization behavior consistent; document any isolated development exceptions.

| Operation | Command or procedure and verification status | Working directory / prerequisites |
| --- | --- | --- |
| Install dependencies | [FILL IN] | [FILL IN] |
| Configure and start locally | [FILL IN] | [FILL IN] |
| Run checks and build | [FILL IN or reference PROOF] | [FILL IN] |
| Apply migrations and prepare test data | [FILL IN or Not applicable] | [FILL IN] |
| Package, install, or deploy | [FILL IN] | [FILL IN] |
| Recover or restore | [FILL IN] | [FILL IN] |

Do not execute placeholder commands. For each configuration value, record its name, type, purpose, validation, environment-specific default, whether it is secret, and how it is supplied. Keep secret values out of the specification and version control.

### Release, update, and recovery

- Identify the release owner, authorized actions, versioned artifact, target environment, prerequisites, and acceptance evidence.
- Record known limitations with affected users, impact, workaround, planned resolution, and whether they block release or public launch.
- Define rollout steps, user communication when needed, post-release checks, and rollback or roll-forward triggers.
- Describe data migration sequencing and compatibility between versions. Record irreversible changes and recovery limits; reverting application code may not restore prior data.
- Before a consequential cutover, plan a rehearsal with representative state, data volume, and failure points. Define reconciliation criteria, the point of no return, and abort or recovery steps that can actually work. Link rehearsal evidence in PROOF before the applicable release gate.
- Define backup scope, retention, access, restoration procedure, maximum acceptable data loss, and maximum recovery time where applicable. Add point-in-time recovery or equivalent granularity when the data and failure modes require it. Verify restoration and link the evidence under PROOF.
- For installed software or libraries, specify packaging, supported upgrades, compatibility, diagnostics, and removal behavior, including treatment of user data.

| Supported version / platform / consumer | Compatibility commitment | Upgrade / migration / coexistence path | Deprecation or end-of-support trigger | Verification reference |
| --- | --- | --- | --- | --- |
| [FILL IN] | [FILL IN: API, ABI, schema, file, device, or runtime as relevant] | [FILL IN] | [FILL IN] | [FILL IN] |

Choose a direct, staged, pilot, canary, flag-based, app-store, package, or other release strategy suited to distribution. Define enable/disable ownership, cohorts, abort signals, user communication, known limitations, and impact on in-progress work. For migrations, specify cut-over, old/new coexistence, validation/reconciliation, downtime if any, and recovery from partial or irreversible steps; do not assume dual writes are required.

Where recovery matters, name recovery time objective (RTO) and recovery point objective (RPO), with scope, rationale, dependencies, and planned exercise. Link the latest actual restoration/rollback evidence, tested revision/data scope, and outstanding gaps in PROOF; mark untested procedures explicitly.

### Launch, documentation, and customer operations

Release authorization asks whether the artifact may be deployed. Launch readiness asks whether real users, support, documentation, and commercial commitments are ready. Use this section conditionally; a local utility may need only installation/removal guidance and a defect-reporting channel.

- Define the launch tier (internal, alpha, beta, early access, general availability) and the evidence required for it. Distinguish launch from technical deployment.
- Identify required documentation and enablement: user, administrator, API, migration, troubleshooting, release notes, in-product help, support macros, and training. Assign ownership, review, localization, and a check that examples work with the released version. For APIs, CLIs, libraries, and platforms, documentation is part of the product.
- Define the support model proportional to actual use: channels, hours, tiers, response or resolution expectations, knowledge base, escalation, and status communication. A written target is not evidence that support is staffed.
- For commercial or multi-user products, cover onboarding/activation, adoption or health signals, renewal and churn reasons, entitlement or billing operations, and the feedback route back into PRODUCT. Do not invent pricing, revenue, or customer commitments.
- Record public announcements, partner or marketplace requirements, and legal or policy notices only where they affect delivery or operation.

### Operation, support, and maintenance

- Define relevant health signals, service-level objectives, capacity assumptions, resource budgets, and cost alerts. Reference the quality targets in PRODUCT.
- Distinguish operational logs from audit records. Specify necessary events and fields, redaction, access, and retention; avoid indiscriminate collection of personal or secret data.
- Assign ownership for alerts, incidents, support, dependency updates, and vulnerability response. Link actionable runbooks and escalation paths.
- Document data locations and access controls, retention/deletion jobs, and operational responsibilities for applicable obligations.
- Define maintenance, deprecation, export, and retirement behavior when relevant. Feed operational findings back into PRODUCT, PROJECT, PROOF, and PROCESS.

| Signal / requirement reference | Indicator, data source, target, and window | Alert / severity / actionable trigger | Owner / response expectation / runbook | Evidence reference |
| --- | --- | --- | --- | --- |
| [FILL IN] | [FILL IN: SLI/SLO where relevant; local diagnostics can suffice] | [FILL IN] | [FILL IN] | [FILL IN] |

Define service-level indicator (SLI) and objective (SLO) formulas, populations, and exclusions when used. Specify sampling, correlation, cardinality/cost controls, and behavior when observability fails. Link thresholds to PRODUCT quality targets, avoiding competing definitions. Define error-budget actions when useful for the service, not as a requirement for all software.

Each actionable runbook identifies symptom/trigger, diagnosis, permissions, safe mitigation, recovery verification, escalation, communication, and follow-up evidence. Incident severity and response expectations should reflect impact and actual support coverage. Record who coordinates an incident and how users/stakeholders are informed; feed causal findings and corrective work into the backlog.

Plan capacity reviews, cost ownership/alerts, dependency inventory, provenance or SBOM where needed, license checks, vulnerability triage, patch targets and response expectations where the project commits to them, emergency fixes, and supported-version policy. Record the usage or cost threshold that triggers scaling or provisioning and the lead time needed to act on it where capacity affects release or readiness. For multi-tenant products, include tenant onboarding/offboarding, isolation checks, export, and deletion. Schedule retention/deletion jobs with failure handling and verification. Connect support and feedback channels to product decisions. Define sunset notice, migration/export, archival/deletion, and disabled integration behavior where applicable.
