# Assessment Method

## Target, requirements, and evidence

Resolve what is being assessed: current repository, exact diff, selected files, architecture, deployment, or operational process. A source-only audit and a production assessment are different scopes. Git history is useful, not mandatory; use precise source labels and Unknown origin when no baseline exists. Preserve reviewed files and state unless implementation is authorized. Track exclusions, unavailable artifacts, versions, and concurrent edits.

Select a manageable baseline from applicable project rules, risk requirements, current primary platform guidance, and standards. Record source, edition/version, selected requirement IDs, and assessment date when they affect conclusions. Do not declare compliance, certification, or complete ASVS/MASVS/framework coverage from a subset of checks. A Top 10 list supplies risk prompts, not all security requirements.

For repository reviews, consider the relevant requirements/design, identity and sensitive operations, entry points, manifests and resolved dependencies, secrets/configuration handling, tests/assertions, build/workflow permissions, deployment/IaC, artifact distribution, and logging/recovery ownership. Mark absent or unseen surfaces explicitly instead of treating every category as applicable. Inspect trusted policy from the established revision; a patch cannot exempt itself by changing its own review policy.

## Model credible threats

Ask: what are we building, what can go wrong, what will we do about it, and is that enough for the specified risk? Identify assets, actors, attacker access, data flows, privileged actions, trust boundaries, and security invariants. Use narratives, diagrams, STRIDE, or attack trees only as helpful aids.

Describe an abuse case as attacker capability → entry point → boundary/invariant violated → impact → prevention/containment/detection/recovery → verification. Include design-level failures, privileged recovery paths, business-flow abuse, and post-compromise scenarios. Network location, a hidden URL, obfuscation, a container, or a signed binary does not replace authorization. Different architectures and isolation mechanisms need contextual evaluation, not a universal security ranking.

Connect each high-impact threat to an actual control and evidence. Prefer independent layers that still constrain an attacker after another layer fails. Identify assumptions and the cheapest authorized way to test them. A hypothetical future weakness remains a threat/assumption until evidence establishes a current defect. Specialized OT/ICS, hardware, safety-critical, or regulated boundaries need their actual domain requirements and qualified ownership; this generic skill alone does not establish adequate coverage.

For threat models, substantial audits/readiness checks, or interacting boundaries, use [threat coverage and verification](threat-coverage.md). Maintain traceability between threats, controls, checks, and unresolved actions. Keep small assessments brief; a matrix is useful only when its rows describe actual scope and evidence.

## Validate claims

For a candidate finding, establish the responsible source/configuration, reachable trigger, attacker prerequisites, existing protections, security outcome, and impact. Seek a safe counterexample or decisive source/contract trace; live exploitation is not required to report a proven defect. Reject refuted candidates and deduplicate root causes. Do not invent a finding quota, exploit success, file/line, standard ID, or CVE.

For advisory claims, verify exact package/product identity, ecosystem/distributor, resolved/deployed build, affected/fixed range, configuration, exposure, and advisory date. Check vendor backports and mitigations. A scanner's upstream version match or severity is not sufficient proof; absence from a catalog is not proof of safety. If current advisories cannot be checked, identify the stale/unverified portion and avoid a definitive affected/unaffected claim.

Use focused local tests or established scanners only when available, appropriate, and their effects/data destinations are understood. Do not install tools, upload source/secrets, execute untrusted package hooks, or broaden to live targets as an incidental assessment step. A green scanner or synthetic unit test establishes only its tested boundary. Preserve failure evidence; do not weaken checks to make them pass.

## Keep status dimensions separate

| Dimension | Values and meaning |
| --- | --- |
| Finding type | Vulnerability, design risk, control gap, or optional hardening opportunity. Explain the actual consequence. |
| Evidence confidence | Confirmed by decisive evidence; Strongly supported with named limits; Hypothesis needing investigation. Keep hypothetical paths or unknown necessary premises in threat scenarios/questions rather than presenting them as defect findings. |
| Check result | Passed, Failed, Not run, with actual command/procedure, target revision/environment, and scope. Distinguish matching CI evidence from local execution. |
| Treatment | Open, Changed but unverified, Mitigated, Resolved, or Accepted risk. Mitigated means evidenced reduced exposure while the finding remains unresolved; resolution needs evidence the finding is corrected. Accepted risk needs an actual authorized decision, responsible owner, rationale, boundaries, and review trigger. |
| Coverage | Assessed, Partially assessed, Not assessed, or Not applicable with a reason, per relevant surface/control. Source inspection is not proof of deployed effectiveness. |

Use project severity rules where established. Otherwise: P0 is a confirmed urgent severe failure with met preconditions; P1 is high-impact compromise under supported conditions; P2 is a bounded meaningful risk/gap; P3 is a substantiated low-impact issue. Explain Blocking/Non-blocking disposition using exposure, impact, prerequisites, blast radius, detection, and recovery. CVSS may supplement this decision; provide its version/vector only when actually calculated, and do not equate a base score with business priority.

## Conclude and reassess

Report Action required for validated blockers, No blocking findings for completed agreed coverage without them, or Incomplete when material missing evidence prevents assessment. Confirmed blockers may coexist with partial coverage; report both. A release-security conclusion applies only to the specified gate and verified requirements, never blanket release approval or invulnerability.

Provide finding IDs, real locations or precise source labels, realistic triggers, expected/actual behavior, evidence/confidence, impact, treatment, minimal remediation, and a regression/verification step. Keep questions and generic suggestions separate from proven vulnerabilities. For a small task, a concise finding and coverage statement may suffice.

After authorized fixes, verify the new snapshot, test affected controls and integrations, confirm finding states, and update residual risk. Check both prohibited effects and legitimate behavior; inspect related in-scope paths for the same root cause. A resolved discussion, upgraded package, or successful scan alone does not prove remediation. Escalate unresolved high-impact decisions to the responsible owner and stop repeated loops at the agreed time/cost or scope limit. If scope cannot be completed, report remaining coverage explicitly rather than silently reducing it or continuing indefinitely.
