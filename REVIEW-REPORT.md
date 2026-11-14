# Skill Review Report

This historical report records recommendations against earlier package revisions. The maintenance review tracks subsequent changes and verification. [Final skill maintenance review](FINAL-SKILL-REVIEW.md)

## Project Overview

This repository contains **22 skills** for assisting developers in building high-quality software with AI coding agents. The skills cover the full software development lifecycle: specification (PentaPRO), implementation (HTTP API, MCP, Android), testing (unit, integration, UI), review (Peer Review, Cybersecurity), delivery (Git Delivery, Software Delivery, Production Operations), and guidance (Agent Instructions, PR Quiz).

The collection was last reviewed and closed on 2026-11-06, with all 21 skill packages passing structural validation and executable checks. This report identifies improvement opportunities to ensure these skills remain the most effective tools for helping developers build high-quality, secure software.

---

## 1. Overarching Improvements

### 1.1 Spec-Driven Development (SDD) Integration Enhancement
The project mentions the option to incorporate SDD with OpenSpec, but several skills could better integrate SDD patterns:

- **PentaPRO** (`penta-pro/SKILL.md`): While version 2.8.0 is comprehensive, add explicit SDD workflow markers and OpenSpec change integration patterns. Document how PentaPRO specifications interface with OpenSpec change scenarios, including the "accepted change" vs. "proposed change" distinction seen in evaluation cases.

- **HTTP API** (`http-api/SKILL.md`): Strengthen OpenAPI 3.1 integration patterns. Add explicit guidance on how API changes should be documented through PentaPRO before implementation, and how regression tests should be generated from spec changes.

- **Software Delivery** (`software-delivery/SKILL.md`): Add explicit SDD change contract guidance. Reference how accepted OpenSpec changes should flow through the software delivery workflow, including task list updates and verification sequences.

- **All skills**: Add a consistent "SDD compatibility" note where relevant, indicating whether and how the skill integrates with specification-driven development workflows.

### 1.2 Executable Check Expansion
Several skills have verification sections but could benefit from more systematic executable check patterns:

- **Peer Review** (`peer-review/SKILL.md`): Expand the "Examine evidence" workflow to include systematic mutation testing probes and automated assertion effectiveness checks. Reference the [verification guide](peer-review/references/verification.md) more explicitly for test effectiveness patterns.

- **Cybersecurity** (`cybersec/SKILL.md`): Add systematic scan integration guidance that distinguishes between "evidence of controls observed in source" vs. "deployed/runtime evidence." Include guidance on when to use static vs. dynamic analysis.

- **Behavior Testing** (`behavior-testing/SKILL.md`): Add patterns for regression test generation from spec changes and explicit baseline comparison checks.

- **HTTP API** (`http-api/SKILL.md`): Add explicit receipt verification patterns (as seen in evaluation check_receipts.py) for write effects and idempotency key reuse.

### 1.3 Evidence-First Methodology
Several skills could more explicitly distinguish between evidence and assumptions:

- **Diagnose Defect** (`diagnose-defect/SKILL.md`): Add explicit "hypothesis vs. evidence" framing for all conclusions. Include a pattern for labeling findings as "confirmed," "hypothesis," or "inconclusive" with required evidence.

- **All skills**: Add a standard "Evidence statement" section or footnote pattern that requires contributors to distinguish observed behavior from inferred causes. This is particularly important for AI-assisted development where model hallucinations can masquerade as code defects.

### 1.4 Model-Agnostic Design Explicitness
The skills already note model neutrality, but could be more explicit about when human judgment is required:

- **Agent Instructions** (`agent-instructions/SKILL.md`): Add a "Model limitation acknowledgment" section that explicitly states which tasks require model-specific capabilities and where human review is mandatory.

- **All skills**: Add a standard "Model dependency" field in metadata that rates the skill's reliance on model reasoning capacity (e.g., "low: pattern-matching", "medium: contract adherence", "high: creative problem-solving").

### 1.5 Cross-Skill Consistency
Improve terminology and pattern consistency across related skills:

- **Terminology alignment**: Ensure "contract," "specification," "spec," "change," and "agreement" are used consistently across PentaPRO, HTTP API, Software Delivery, and Peer Review.

- **Handoff patterns**: Standardize the handoff template format across PentaPRO, Software Delivery, and Production Operations. The current templates (penta-pro/assets/penta-pro-template.md, production-operations/assets/deployment-brief.md, etc.) could reference a common base format.

- **Version metadata**: Ensure all skills consistently use the `metadata.version` field and that version bumping follows a predictable schema (major.minor.patch for breaking/feature/minor changes).

---

## 2. Skill-Specific Recommendations

### 2.1 agent-instructions (v1.1.0)
**Strengths**: Strong portable guidance foundation; clear evaluation procedure integration.

**Recommendations**:
- Add explicit guidance on when to create a new skill vs. extending project instructions (AGENTS.md template)
- Include a "migration from upstream" pattern that documents how skills adapted from mattpocock/skills and obra/superpowers maintain or diverge from original intent
- Add guidance on preserving canonical requirement IDs when editing specifications across PentaPRO and Software Delivery
- Include more "before/after" examples showing instruction improvements and their measurable effects

### 2.2 peer-review (v1.10.2)
**Strengths**: Mature review methodology; comprehensive coverage across backend, frontend, Android, and test code.

**Recommendations**:
- Add LLM-generated code specific patterns: hallucination detection, incorrect assumption identification, and synthetic test generation verification
- Include mutation testing probe patterns with concrete examples of "meaningful vs. equivalent mutation" distinction
- Expand the "Challenge candidates" section with AI-assisted review anti-patterns (e.g., accepting model claims without evidence)
- Add guidance on review depth selection for AI-assisted vs. human-written code

### 2.3 cybersec (v1.6.0)
**Strengths**: Comprehensive threat modeling and audit modes; extensive reference routing.

**Recommendations**:
- Add LLM/model security specific section: prompt injection, context leakage, tool use safety, and AI supply chain risks
- Include supply chain security patterns for AI dependencies (model versions, plugin integrity, credential leakage)
- Add "security in AI agent workflows" guidance: how agent skills interact with secrets, how to audit agent-generated code for security regression
- Enhance threat modeling with modern web application patterns (CSP, clickjacking, BOLA, etc.) and mobile-specific threats

### 2.4 diagnose-defect (v1.0.0)
**Strengths**: Clear reproduction-feedback-loop-verification pattern; good distinction between regression and suspected defects.

**Recommendations**:
- Add intermittent failure patterns specific to AI-assisted development (nondeterministic model outputs, environment state changes)
- Include guidance on reproducing defects when only model conversation logs are available (vs. full repository reproduction)
- Add "cause classification" framework: model error vs. code defect vs. environment issue vs. configuration error
- Expand the "reproduction unavailable" section with safe evidence inspection patterns

### 2.5 behavior-testing (v1.1.0)
**Strengths**: Good boundary testing guidance; clear test-first workflow patterns.

**Recommendations**:
- Add browser/test automation anti-patterns: arbitrary sleeps, global network quiet assumptions, and unwaited state
- Include explicit regression test generation patterns from specification changes
- Add guidance on test isolation for AI-assisted development (dependency mocking boundaries)
- Expand the "test-only work" section with patterns for preserving and restoring fixed code

### 2.6 http-api (v1.1.1)
**Strengths**: Comprehensive HTTP implementation guidance; strong OpenAPI/RFC 9110 integration.

**Recommendations**:
- Add OpenAPI 3.1-specific patterns (newest spec version, updated serialization)
- Include API deprecation and migration strategy patterns with backward compatibility guarantees
- Add explicit idempotency key scope guidance (operation+caller+tenant as seen in the evaluation)
- Enhance SSRF prevention with more concrete OWASP cheatsheet integration patterns
- Add receipt verification patterns for write effects and concurrent duplicate handling

### 2.7 mcp-server (v1.1.0)
**Strengths**: Protocol-aware implementation guidance; SDK version verification.

**Recommendations**:
- Add protocol revision compatibility matrix (legacy vs. modern direct calls, as seen in MCP evaluation)
- Include authentication/authorization patterns for protected requests and session handling
- Add guidance on capability deprecation and backward compatibility for MCP servers
- Enhance SDK-specific patterns with modern vs. legacy wire request handling
- Include pattern for durable retry after lost response (observed in MCP evaluation cases)

### 2.8 git-delivery (v1.0.0)
**Strengths**: Comprehensive Git operation guidance; strong review-verify-commit-push sequence.

**Recommendations**:
- Add signed commit and GPG verification guidance
- Include merge conflict resolution patterns and when to stop vs. attempt resolution
- Add PR template best practices and when quiz/feedback should be integrated
- Enhance branch protection and workflow integration guidance
- Add guidance on atomic Git operations and when partial commits are appropriate

### 2.9 production-operations (v1.0.0)
**Strengths**: Comprehensive deployment and operations guidance; provider-specific references.

**Recommendations**:
- Add cloud provider hardening guides (beyond basic IAM) for AWS, Azure, GCP, Cloudflare, VPS
- Include observability and monitoring setup patterns (metrics, logs, traces for deployment verification)
- Add rollback and recovery procedure patterns with verified sequences
- Enhance secrets management beyond "never commit credentials" to rotation, auditing, and expiry
- Add cost optimization and resource management patterns for deployment pipelines

### 2.10 penta-pro (v2.8.0)
**Strengths**: Mature five-pillar specification methodology; comprehensive quality bar.

**Recommendations**:
- Add explicit readiness gates and "blocked/ready/assessed" classification with concrete criteria
- Include specification evolution and versioning patterns (how to update specs without losing traceability)
- Add accessibility and internationalization consideration patterns across pillars
- Enhance the quality bar with more concrete anti-pattern examples (especially "status collapsed into done")
- Include more worked examples with full traceability from user intent to five-pillar documents

### 2.11 software-delivery (v1.4.0)
**Strengths**: Coordination of dependent tasks; change contract guidance.

**Recommendations**:
- Add incremental delivery and feature flag patterns with gradual rollout strategies
- Include canary release and blue-green deployment guidance
- Enhance change contract guidance with more concrete OpenSpec worked examples
- Add rollback and recovery procedure patterns with evidence requirements
- Include dependency verification patterns (package publisher, version, source authentication)

### 2.12 technical-research (v1.0.0)
**Strengths**: Technical uncertainty resolution with traceable evidence.

**Recommendations**:
- Add technical spike documentation patterns with explicit success/failure criteria
- Include evaluation-to-production handoff patterns (how spikes become maintained specifications)
- Add patterns for evaluating multiple alternatives with comparison tables and decision records
- Explicit criteria for spike completion vs. abandonment

### 2.13 android-module-structure (v1.3.0)
**Strengths**: Clear module ownership and boundary patterns; Gradle convention guidance.

**Recommendations**:
- Add explicit Kotlin/Java version compatibility and built-in Kotlin migration patterns (already referenced but could be more systematic)
- Include gradual module migration patterns from monolithic to feature-first
- Add build-cache optimization patterns for Gradle configurations
- Enhance supply chain security for native dependencies (transitive dependency verification)

### 2.14 android-data-layer (v1.2.4)
**Strengths**: Comprehensive data layer implementation; offline-first patterns; Room and DataStore guidance.

**Recommendations**:
- Add Room migration pattern examples with destructive vs. non-destructive changes
- Include DataStore encryption options beyond "choose credential protection from threat model"
- Add offline-first conflict resolution patterns beyond "replaceAll must be atomic"
- Enhance network error handling with more transient failure classification

### 2.15 android-error-handling (v1.2.3)
**Strengths**: Typed result abstraction; comprehensive Ktor exception mapping.

**Recommendations**:
- Add more comprehensive error classification patterns (programming vs. operational vs. security failures)
- Include guidance on error reporting to users vs. logging (redaction policies)
- Add error boundary design patterns for Compose UI
- Enhance Ktor exception handling with connection pool and timeout coordination

### 2.16 android-di-koin (v1.2.3)
**Strengths**: Koin binding and lifecycle guidance; ViewModel scoping patterns.

**Recommendations**:
- Add more explicit ViewModel scoping patterns (application vs. activity vs. fragment)
- Include DI container lifecycle management and reset patterns between tests
- Add patterns for testing DI configurations with qualified bindings
- Enhance worker and background integration guidance (Koin + WorkManager coordination)

### 2.17 android-background (v1.2.3)
**Strengths**: WorkManager job design; Koin integration guidance.

**Recommendations**:
- Add more explicit WorkManager constraint patterns (network, storage, retry backoff)
- Include foreground service alternatives with permission guidance
- Add idempotent operation design patterns with operation ID deduplication
- Enhance account/session boundary guidance with generation isolation at write boundary

### 2.18 android-unit-testing (v1.2.3)
**Strengths**: Coroutine testing patterns; fake/fixture design guidance.

**Recommendations**:
- Add more explicit coroutine scheduler patterns (StandardTestDispatcher vs. UnconfinedTestDispatcher)
- Include test parameterization strategies for equivalent input/output mappings
- Add mutation testing setup patterns with compatible tools (JakoCoa, Kover)
- Enhance fake/fixture design with out-of-order response and race condition patterns

### 2.19 android-integration-testing (v1.2.4)
**Strengths**: Boundary test guidance; Room, Ktor, DataStore, DI, and Worker testing.

**Recommendations**:
- Add more explicit Room testing patterns with MigrationTestHelper and schema exports
- Include MockEngine limitations and when loopback server is required
- Add negative security testing patterns (wrong account/tenant, stale credentials, unsafe URI/redirect)
- Enhance DI verification in integration tests with qualifier and property resolution

### 2.20 android-ui-testing (v1.2.3)
**Strengths**: Compose UI testing guidance; accessibility and resource patterns.

**Recommendations**:
- Add more explicit accessibility testing patterns (TalkBack, screen readers, semantic assertions)
- Include flaky test mitigation strategies (idling resources, waitUntil, synchronization patterns)
- Add multi-device testing strategies and release behavior verification
- Enhance Compose version migration guidance with v2 factory patterns and dispatchers

### 2.21 pr-quiz (v1.3.0)
**Strengths**: PR decision comprehension quiz generation; grading workflow guidance.

**Recommendations**:
- Add question quality assessment patterns (distractor plausibility, correct answer distinctiveness)
- Include guidance on quiz integration in CI/CD pipelines beyond the optional GitHub Actions workflow
- Add patterns for feedback loop between quiz results and code review recommendations
- Enhance the "optional grading workflow" with more adaptive template patterns

---

## 3. Integration and Consistency Improvements

### 3.1 Specification-Implementation Continuity
Improve the flow from specification to implementation across PentaPRO → Software Delivery → HTTP API → Peer Review:

- Add a standard "specification change ID" that travels through the workflow
- Document how PentaPRO decision IDs map to Software Delivery task IDs
- Reference how HTTP API contract changes should trigger PentaPRO review
- Clarify when Peer Review should check specification conformance vs. code contract conformance

### 3.2 Android Skill Integration
The 14 Android-related skills could better coordinate:

- **Consolidated references**: Android UI Design references (`ui-design/references/android/`) should consistently reference the native implementation procedures from `android-module-structure`
- **Error handling chain**: `android-error-handling` → `android-data-layer` → `android-integration-testing` should have explicit error propagation patterns
- **DI-background-data flow**: `android-di-koin` → `android-background` → `android-data-layer` should have initialization ordering guarantees
- **Test hierarchy**: `android-unit-testing` → `android-integration-testing` → `android-ui-testing` should have clear boundary definitions

### 3.3 Evidence Hierarchy Across Skills
Define a consistent evidence hierarchy:

- **Observed behavior**: What the model/runtime actually did (highest confidence)
- **Test result**: What a test asserted (medium confidence, test-dependent)
- **Model claim**: What the model stated (lowest confidence, model-dependent)
- **Documented contract**: What the specification says (high confidence, source-dependent)

Each skill should explicitly state which evidence class its outputs belong to and what confidence level to assign.

### 3.4 Change Contract Standardization
Standardize change contract patterns across skills that modify behavior:

- **What changed**: Precise description of the behavior change
- **Why changed**: Rationale from specification or requirement
- **What stayed the same**: Backward compatibility guarantees
- **What to verify**: Checklist of regression tests and verification steps
- **Rollback plan**: How to reverse the change if verification fails

This pattern already exists in Software Delivery but should be more systematically applied across HTTP API, PentaPRO, and Android skills.

---

## 4. SDD/OpenSpec Integration Recommendations

Since the user specifically mentioned SDD with OpenSpec, here are targeted improvements:

### 4.1 PentaPRO + OpenSpec Workflow
- Add a "OpenSpec change integration" section to PentaPRO that documents how accepted OpenSpec changes are incorporated into the five pillars
- Include pattern for "specification first" vs. "implementation first" SDD workflows
- Document how to handle "design decisions" vs. "requirements" in the OpenSpec context

### 4.2 Software Delivery + OpenSpec
- Add explicit OpenSpec change receipt tracking (as seen in evaluation check_receipts.py)
- Include two-increment implementation pattern for OpenSpec changes
- Document task list update sequencing when OpenSpec changes are applied

### 4.3 HTTP API + OpenSpec
- Add OpenAPI specification version tracking and change acceptance criteria
- Include pattern for how API contract changes flow from specification to implementation to verification
- Document how regression tests are generated from OpenSpec changes

### 4.4 Cross-Skill OpenSpec References
- Add OpenSpec integration notes to relevant skills (Peer Review for spec conformance, Cybersecurity for OpenSpec security considerations)
- Document which skills should be activated when OpenSpec changes are requested
- Include OpenSpec change ID tracking across the workflow

---

## 5. Priority Matrix for Improvements

| Priority | Skill | Impact | Effort |
|----------|-------|--------|--------|
| High | `diagnose-defect` | Critical for AI-assisted debugging | Medium |
| High | `peer-review` | Critical for code quality assurance | Medium |
| High | `http-api` | Critical for API contract integrity | Medium |
| Medium | `penta-pro` | High for specification quality | High |
| Medium | `software-delivery` | High for delivery coordination | Medium |
| Medium | `cybersec` | High for security awareness | Medium |
| Medium | `behavior-testing` | Medium for test effectiveness | Medium |
| Low | `mcp-server` | Low (niche protocol) | Low |
| Low | `pr-quiz` | Low (educational aid) | Low |
| Low | `agent-instructions` | Medium (foundational) | Medium |

---

## 6. Recommended Implementation Roadmap

### Phase 1: Foundational Improvements (1-2 months)
1. Add evidence hierarchy explicitness to all skills
2. Standardize SDD/OpenSpec integration notes across relevant skills
3. Enhance model-agnostic design documentation in agent-instructions
4. Add LLM-specific patterns to peer-review and cybersec

### Phase 2: Skill Enhancements (2-4 months)
1. Expand executable check patterns in behavior-testing, http-api, and peer-review
2. Add Android skill integration consistency (module-structure, data-layer, error-handling)
3. Improve PentaPRO readiness gates and specification evolution patterns
4. Standardize change contract patterns across software-delivery, http-api, and android skills

### Phase 3: Cross-Skill Harmonization (4-6 months)
1. Implement evidence hierarchy across all skill outputs
2. Standardize OpenSpec integration workflows
3. Create cross-skill contribution guidelines
4. Establish periodic skill review cadence (quarterly)

### Phase 4: Evaluation and Validation (6-12 months)
1. Run matched baseline comparisons on improved skills
2. Validate SDD/OpenSpec integration workflows with real projects
3. Measure improvement in developer productivity and software quality
4. Publish updated skill versions with versioned evaluation results

---

## 7. Conclusion

The 22 skills in this collection provide comprehensive coverage of the software development lifecycle with AI coding agents. They already demonstrate strong alignment with established methodologies (PentaPRO, Agent Skills specification, Thoughtworks Technology Radar patterns) and include many best practices.

The recommended improvements focus on:
1. **Explicit evidence demarcation** - distinguishing observed behavior from model claims
2. **SDD/OpenSpec integration** - stronger specification-driven development workflows
3. **Model-agnostic design** - clearer boundaries of model capability vs. human review
4. **Cross-skill consistency** - standardized patterns, terminology, and handoff procedures
5. **Executable verification** - systematic checks and regression test generation
6. **Security by design** - LLM/model-specific security considerations across all skills

Implementing these recommendations will ensure the skills remain effective, efficient tools for helping developers build high-quality, secure software while maintaining compatibility with the Spec-Driven Development framework and OpenSpec specification approach.