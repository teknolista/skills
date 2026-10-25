# PENTA-PRO: Software Specification Template

**PRODUCT · PROJECT · PROOF · PROCESS · PRODUCTION**

Describe the product, solution, evidence, working method, and operation for the next useful increment. Keep detailed supporting material in linked project documents.

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

- Replace `[FILL IN]` with project facts. Mark conditional sections `Not applicable` with a reason. Remove irrelevant prompts from a completed specification.
- Identify consequential statements as requirements, constraints, decisions, or assumptions, and record their confirmation status: `Confirmed`, `Proposed`, or `Pending`. Examples and placeholders are not approved requirements.
- Resolve blocking uncertainty for the next deliverable. Record other open questions with an owner and a point by which they must be answered. Do not invent missing targets, tools, or approvals.
- Specify the first usable increment and high-risk behavior in detail; refine later work as evidence emerges. A prototype or technical experiment may resolve uncertainty before implementation.
- Keep each fact in one authoritative location. Use stable IDs and links rather than repeating requirements across pillars.
- Keep artifacts in clear English. Define supported user-interface languages separately under PRODUCT.

## Document metadata and resume state

| Field | Value |
| --- | --- |
| Template version | 1.3.0 |
| Product name and one-sentence purpose | [FILL IN] |
| Document owner and decision-makers | [FILL IN] |
| Specification version, updated date, and document status | [FILL IN: Draft / Reviewed / Accepted / Superseded] |
| Target release or increment | [FILL IN] |
| Repository and authoritative specification location | [FILL IN] |
| Supported platforms and distribution channel | [FILL IN] |
| License and ownership constraints | [FILL IN] |
| Related feature specifications, decisions, and runbooks | [FILL IN] |
| Next increment readiness | Not assessed |
| Readiness basis and assessment date | [FILL IN after assessment] |
| Pending question references | [FILL IN: PROJECT question IDs; identify blockers] |
| Last completed focus | [FILL IN] |
| Next action | [FILL IN] |

`Confirmed` means supported by cited project evidence or a decision made by the responsible person or an agent within explicit delegation. Identify the decision-maker and source of authority; an agent choice is not a user requirement or document acceptance. `Proposed` means a recommendation awaiting a decision. `Pending` means missing, disputed, or unresolved information; link it to an open question in PROJECT. Keep verification results separate: a confirmed requirement can still be unverified.

Assess next-increment readiness as `Not assessed`, `Blocked`, or `Ready for the next increment` against the conditions in PROCESS, with reasons and unresolved question references. Document and readiness statuses describe specification state; they do not authorize implementation, spending, external actions, merge, or release. Record actual authority, its source, and scope under PROCESS.

## 1. PRODUCT

Define the intended value and observable behavior. Technical implementation choices belong in PROJECT; evidence that behavior is achieved belongs in PROOF.

### Problem, users, and outcomes

- **Problem and current alternatives:** What difficulty exists, and what evidence supports it?
- **Users and stakeholders:** Who uses, buys, administers, supports, or is affected by the software?
- **User journeys:** What tasks should users complete, in which real-world conditions?
- **Value and success measures:** Define the intended outcome, current baseline if known, target, measurement method, and evaluation window. Label untested beliefs as hypotheses.
- **Product boundaries:** Identify included capabilities, explicit non-goals, and unacceptable outcomes even if the software technically works. PROJECT selects which requirements belong in the current release.

### Domain, data, and access

- Define domain terms, actors, conceptual entities, relationships, and business rules using stable identifiers where useful.
- Describe business invariants: conditions that must remain true across operations, including failure and concurrency.
- Specify permissions by role, action, and resource ownership. Include administrative and cross-tenant behavior when applicable.
- Identify data owners, sensitivity, sources, allowed purposes, retention, deletion, export, and applicable obligations. Record the responsible decision-maker for unresolved obligations.
- Describe entity lifecycles, allowed transitions, prerequisites, and visible effects. Add a state diagram when it clarifies complex behavior.

### Requirements and quality targets

Record functional and quality requirements in one register. Use `Must`, `Should`, `Could`, and `Won't in this release` deliberately; priority does not replace acceptance criteria.

| ID | Requirement and reason | Source / owner | Priority | Confirmation status | Feature / acceptance reference |
| --- | --- | --- | --- | --- | --- |
| REQ-001 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

For quality requirement IDs already listed in the register, use the table below to supply measurement details rather than duplicate their definitions. Consider performance, reliability, security, accessibility, usability, compatibility, localization, and resource use.

| ID | Attribute / user journey | Target | Workload, platform, and measurement window | Proof reference |
| --- | --- | --- | --- | --- |
| [Existing quality requirement ID] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

For performance, specify the percentile, dataset size, concurrency or request rate, network conditions, and acceptable error rate where relevant. Avoid unexplained numbers such as a universal response-time or coverage target.

### Feature specification — repeat for each coherent feature

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
- **Acceptance criteria:** Assign IDs such as `AC-001`. Describe observable outcomes using Given / When / Then or equally precise statements. Include meaningful negative and boundary cases.
- **Dependencies and unresolved decisions:** `[FILL IN]`.

## 2. PROJECT

Define a feasible delivery commitment and the technical blueprint that supports it. This pillar covers more than scheduling: it connects scope and constraints to solution design.

### Delivery boundaries and resources

- **Current release:** Link the selected requirement IDs and explain the smallest useful outcome.
- **Milestones:** Define deliverables, dependencies, owners, and deadlines; distinguish fixed constraints from estimates.
- **Resources and budget:** Record available people, tools, environments, development costs, agent usage limits, and expected operating costs.
- **Decision rights:** Identify who owns product priorities, technical decisions, acceptance, and releases.
- **Trade-offs:** State what takes priority when scope, time, cost, maintainability, or quality conflict. Identify constraints that cannot be traded away.

### Risks, assumptions, and open decisions

| ID | Risk, assumption, or question | Impact / affected work | Owner | Resolution or mitigation | Needed by / status |
| --- | --- | --- | --- | --- | --- |
| OPEN-001 | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] | [FILL IN] |

Separate evidence from assumptions. Use a limited experiment when a consequential assumption can be tested cheaply. Escalate only the work blocked by an unresolved decision.

### Solution architecture and technology

- Describe system boundaries, components, responsibilities, trust boundaries, and data flow. Include a diagram when useful.
- Select the simplest architecture that meets the requirements. Explain significant alternatives and trade-offs.
- Record approved runtimes, versions, frameworks, libraries, storage, and external services with rationale. Identify decisions still open and existing technology that must be reused.
- Document meaningful decisions with status, requirement links, rationale, consequences, and conditions for reconsideration. An accepted decision can later be superseded explicitly.
- Define module boundaries, repository structure, important conventions, and actual reference implementations. Apply patterns where they solve a demonstrated problem.

### Data design and integration contracts

- Define logical schemas, constraints, identifiers, relationships, and ownership; add physical schema and indexing choices where needed.
- Specify transaction boundaries, consistency requirements, concurrent-update behavior, deduplication, and migration compatibility.
- For each API, event, file format, or external service, identify its owner and authoritative contract. Define schemas, validation, authorization, errors, compatibility, and versioning.
- Specify timeouts, cancellation, retryable failures, retry limits, and duplicate-request handling per operation. Repeated requests must not accidentally repeat irreversible effects.
- Define partial-failure handling and compensation where needed. Distributed transactions, queues, and circuit breakers require a stated reason.
- Identify security threats and map mitigations to relevant requirements and verification checks. Include secret handling, tenant boundaries, and dependency risks where applicable.

### Interface and implementation conventions

- Link one approved visual reference or design system: components, tokens, themes, layouts, and accessibility expectations.
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

### Verification and validation strategy

- Choose unit, integration, contract, end-to-end, manual, or other checks according to behavior and risk. Define representative fixtures and isolate side effects.
- For critical rules, record concrete inputs and expected outputs derived from product requirements, independently of the implementation. Use these examples to check both the software and its tests.
- Test important failures and boundaries: denied access, malformed input, duplicate actions, concurrent updates, dependency failures, and partial completion as applicable.
- For UI changes, inspect relevant flows in the running application, including keyboard use, supported layouts, and error recovery. A successful build alone does not establish usable behavior.
- Define reproducible workload and environment details for performance checks. Validate security controls against the selected threat model and applicable requirements.
- Specify how representative users or a responsible stakeholder will validate the intended outcome. Passing technical tests does not establish product usefulness by itself.
- Document the chosen test-first policy and any coverage targets in one place. Coverage is supporting evidence, not a substitute for meaningful assertions or behavioral checks.
- Use independent review for changes that require it. Provide the reviewer with requirements, the actual diff, relevant context, and evidence; review approval does not replace execution checks.

### Quality gates and exceptions

Define the checks required for a task, integration, and release, including their commands and owners. Keep one authoritative set of thresholds. Match checks to the risk and retain mandated project checks.

- Required acceptance criteria pass. A failed or unverified required check blocks the affected gate unless an explicitly authorized exception is recorded below.
- Required build, analysis, tests, and review have evidence for the relevant revision.
- Material findings are resolved; changes after verification trigger the affected checks again.
- Documentation, configuration, compatibility, and operational impacts are addressed.
- Any authorized exception records its owner, rationale, impact, mitigation, and expiry or follow-up. Do not weaken checks silently to obtain a pass.

### Learning and effectiveness

Track product outcomes alongside delivery indicators such as time to an accepted increment, escaped defects, rework, operating cost, and human interruptions. Record baselines and compare similar work. Use findings to improve the specification and workflow; do not treat generated code volume as a success measure.

## 4. PROCESS

Define how people and agents transform agreed work into a reviewed change. PROOF defines the evidence required at each gate; PRODUCTION defines operational actions.

### Development cycle — repeat for each increment

PROCESS governs the entire cycle. Consult relevant material from all five pillars for each task; their document order is not a sequence of execution phases.

Define the project's cycle from selecting an outcome and preparing checks through implementation, review, integration, and authorized release. Identify the required evidence and responsible role at each transition. Recheck affected behavior after fixes or integration, and feed feedback into tracked work and the relevant pillars.

Use a formal plan when complexity or uncertainty warrants it. Planning-only requests produce investigation and a proposal; they do not authorize implementation. Define any required plan approval explicitly.

### Task readiness and completion

A task is ready when its goal, scope, acceptance criteria, dependencies, necessary contracts, and decision authority are sufficiently clear. A task should deliver a verifiable increment; avoid splitting work solely by technical layer when that prevents usable outcomes.

| Task field | Required information |
| --- | --- |
| Identity and outcome | Task ID, requirement references, user-visible result, and out-of-scope work. |
| Inputs | Relevant source files, specification sections, contracts, and prior decisions. |
| Execution | Owner, dependencies, permitted changes, and relevant environment. |
| Completion | Acceptance references, required checks, review requirements, and handoff location. |

### Agent responsibilities and authority

- Define concrete responsibilities, inputs, outputs, and tool access for implementation, review, and coordination. Use separate roles only when useful.
- Record permitted local edits, external actions, costs, merge authority, and release authority. Do not infer permission to deploy from permission to implement or merge.
- Continue authorized work without repeatedly requesting the same approval. Group non-blocking questions; escalate material scope changes or unresolved high-impact decisions.
- When running work in parallel, record dependencies and ownership, isolate conflicting changes, limit concurrency, and define the integration order.
- Set time, cost, and retry limits for automated runs. Define escalation conditions, cancellation behavior, and how work resumes without duplicating external actions.
- Keep durable task status, decisions, blockers, and evidence in the existing tracker or agreed file. Avoid maintaining contradictory task lists.

### Context, skills, and change control

- Keep `AGENTS.md` focused on durable instructions and navigation. Store detailed requirements, feature specifications, decisions, and runbooks in their authoritative locations.
- Load the context needed for the current task. Identify source, version, and status when retrieving external or historical material; distinguish reference content from authorized instructions.
- Maintain a small registry only for skills and tools actually selected for the project: source/version, availability, trigger, inputs, outputs, permissions, and fallback if unavailable.
- Define the actual branch, commit, review, and CI conventions. Do not assume a branch name, installed skill, file path, or approval policy.
- When requirements change, assess affected tasks, contracts, tests, and operations; update their references and record the decision.
- At handoff, report changes, verification results, unresolved issues, and the exact next action when one is needed.

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
- Define rollout steps, user communication when needed, post-release checks, and rollback or roll-forward triggers.
- Describe data migration sequencing and compatibility between versions. Record irreversible changes and recovery limits; reverting application code may not restore prior data.
- Define backup scope, retention, access, restoration procedure, maximum acceptable data loss, and maximum recovery time where applicable. Verify restoration and link the evidence under PROOF.
- For installed software or libraries, specify packaging, supported upgrades, compatibility, diagnostics, and removal behavior, including treatment of user data.

### Operation, support, and maintenance

- Define relevant health signals, service-level objectives, capacity assumptions, resource budgets, and cost alerts. Reference the quality targets in PRODUCT.
- Distinguish operational logs from audit records. Specify necessary events and fields, redaction, access, and retention; avoid indiscriminate collection of personal or secret data.
- Assign ownership for alerts, incidents, support, dependency updates, and vulnerability response. Link actionable runbooks and escalation paths.
- Document data locations and access controls, retention/deletion jobs, and operational responsibilities for applicable obligations.
- Define maintenance, deprecation, export, and retirement behavior when relevant. Feed operational findings back into PRODUCT, PROJECT, PROOF, and PROCESS.
