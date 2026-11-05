# PL Coding Skills Bundle assessment

Research date: 2026-11-05. Local source supplied by the user: `/home/dever/workspace/PL Coding Skills Bundle`. The directory label identifies the supplied bundle, not independently verified authorship or a public release. No license, README, upstream URL or version manifest was found. Instructions below are an independently written synthesis of general engineering lessons; no source code, templates, CSS, JavaScript, token dataset or substantial instruction passages were redistributed into these skills. Source remains unchanged.

## Scope and provenance

Inventoried 39 files and examined all 20 skill entrypoints, comparing the overlapping Android/KMP pairs and their platform-specific differences. Examined the design references, viewer/build assets and PR-quiz tooling for relevant behavior/dependencies; this is a skill-maintenance assessment, not a complete security audit of the bundle or a guarantee of its snippets. Missing references such as android-background, android-integration-testing, kmp-ui-testing, kotlin-mutation-testing and figma-to-android-vector were not supplied and were not treated as installed capabilities.

Snapshot SHA-256: `b10a08b19c03a9a331ea190f07e65f7da24575e894b835e9433aa333137509d5`. Computation: for every regular file sorted by absolute path, hash relative UTF-8 path, NUL, file bytes, NUL in order. Entrypoint digests below are first 12 hex characters of each SKILL.md SHA-256; they identify inspected inputs, not a signature of authenticity.

| Entrypoint | Digest | Useful lesson and destination |
| --- | --- | --- |
| android-compose-components | 2137999addc4 | Narrow component contracts, accessible primitives, resource/theme reuse and meaningful previews → UI/UX and Code Review. |
| android-data-layer | 5f75db45347e | Data authority, DTO/storage boundaries and cache behavior → PENTA-PRO and Code Review; logging/token assumptions → Cybersec. |
| android-di-koin | 983066b83f1e | Composition roots and object lifetimes → PENTA-PRO and Code Review; no mandatory Koin. |
| android-error-handling | 4272b11abcae | Expected errors versus cancellation, response decoding and user-facing mapping → PENTA-PRO, Code Review and UI/UX. |
| android-module-structure | 06341d72191c | Dependency ownership and reuse → PENTA-PRO and Code Review; generated-client secret handling → Cybersec. |
| android-navigation | 2fd39ef235eb | Minimal route arguments and feature integration → UI/UX and Code Review; argument trust → Cybersec. |
| android-presentation-mvi | f65c6f381458 | Integration/rendering separation, state/effect lifetimes and restoration → all relevant planning/UI/review surfaces; no universal MVI/Channel rule. |
| android-ui-testing | 83c6848929a9 | Meaningful UI outcomes, runtime boundaries, semantic targets and synchronization → Code Review and UI/UX. |
| android-unit-testing | 9bbd59d7c22c | Contract-derived failure vectors, controlled collaborators/time and observable outcomes → Code Review and PROOF; adapt overly broad completeness claims. |
| design | 496c529e08a6 | Screen/state inventory, feedback-surface choice, realistic stress content and reviewable variants → UI/UX; keep docs/ui-ux.md canonical. |
| kmp-compose-architecture | 753597bbe6ea | Shared/platform boundaries, keyed effects and deferred state reads → UI/UX and Code Review; reject automatic Stable annotation and all-state-in-ViewModel rules. |
| kmp-compose-components | 8bbb5a5455bd | Shared resources/preview compatibility and target-specific verification → UI/UX and Code Review. |
| kmp-data-layer | ad24a1888434 | Engine/storage adapters and per-target persistence → PENTA-PRO, Code Review and Cybersec. |
| kmp-di-koin | bf42e4adaa21 | Platform initialization ownership and duplicate-start/lifetime risks → PENTA-PRO and Code Review. |
| kmp-error-handling | ba802caac78f | Engine-specific exceptions, cancellation and platform-aware decoding → Code Review; accurate error meaning → UI/UX. |
| kmp-module-structure | eb2e504290ad | Source-set/plugin/test-compilation compatibility → PENTA-PRO and Code Review; packaged BuildKonfig values → Cybersec. |
| kmp-navigation | 31eab3eedfb2 | Platform entry/Back/deep-link adapters → PENTA-PRO, UI/UX and Code Review; no unverified all-platform equivalence. |
| kmp-presentation-mvi | fd2075da7f4a | Shared API availability versus actual termination/restoration guarantees → PENTA-PRO, UI/UX and Code Review. |
| kmp-unit-testing | e1802d396eef | Shared contract tests versus platform actual coverage and native-capable test dependencies → PROOF and Code Review. |
| pr-quiz | da58b5f21111 | Explain state authority, retries, wiring/lifetimes and tradeoffs in handoffs → PENTA-PRO/Code Review. Quiz publication, workflow installation and merge-status changes excluded. |

## Adaptations and counterexamples

- Preserve the project's architecture, tools and selected targets. Koin/Ktor/Room, Clean Architecture, file naming, module counts, mandatory iOS and fixed SDK/Gradle versions are not universal requirements. An AGP migration condition must not be attributed solely to the Gradle major version.
- The data-layer fallback example invokes local loading inside an onFailure observer whose definition returns the original result. That callback does not replace the failed result. Added a review trace for fallback transformation and ignored cache-write outcomes; no example implementation was imported.
- An Android safe-call example decodes the response after its request try/catch. Decoding exceptions can escape that boundary, and a Unit/empty-body response needs different handling from a JSON payload. Added coverage prompts without prescribing a new Result type.
- BuildConfig/BuildKonfig/local.properties may improve configuration sourcing without making packaged values secret. DataStore alone is not proof of encrypted credential storage. Added threat-based storage, logging, backup, trusted destination and refresh/logout-race checks.
- A List-containing state does not justify Stable/Immutable automatically. Annotation changes the compiler contract and can hide incorrect mutation. Local UI state need not universally move to a ViewModel, and one-shot channels do not guarantee lifecycle/process delivery.
- A test API or rule name alone does not identify the execution environment. Inspect runner/source set, resolved library and actual test/effect contexts. Do not infer that Compose 1.11+ requires arbitrary fixed clock advances in all tests; automatic synchronization and external work have different owners.
- StateFlow conflation makes an uncontrolled assertion of every intermediate loading emission unreliable. A constructed SavedStateHandle verifies value consumption, not an OS process-death cycle. Added controlled-dependency and evidence-level guidance.
- Mutation survival is not proof of a useless test, and several tests are not redundant merely because one bug breaks them all. Keep risk-based examples and the existing isolated-mutation/equivalence safeguards. Avoid universal input catalogues and unbounded “cannot think of another case” completion gates.
- Adopt feedback selection and state/stress coverage without a compulsory three-option interview, separate docs/design tree, external publication, hardcoded aesthetics or copying the HTML viewer. Actual field/form/transient/persistent/content/decision surfaces remain contextual.
- The PR quiz explicitly exposes a base64 answer key, permits authors by default and carries a pass across later commits when its quiz ID remains. It is a comprehension aid, not independent code/security verification. No quiz automation or external mutation was added.

## Executed source probe

Read the supplied design_tools.py before execution. Ran only its `check` subcommand on two synthetic token configurations under `/tmp/pl-bundle-review`, with no changes to the bundle and no publishing/screenshot command:

1. An explicitly requested contrast pair with a missing foreground token was silently omitted: exit 0, 64 pairs checked, 0 failing.
2. An explicit same-color pair with an unknown usage string (`text-typo`) was assigned a zero threshold: exit 0, 66 pairs checked, 0 failing.

The existing valid palette pairs still passed. These bounded counterexamples support the new UI/UX rule to inspect checker pair coverage, unknown categories and skipped evidence; they do not assess the whole tool or prove rendered accessibility. The tool was not bundled or modified.

## Primary verification sources

- [Android stability guidance](https://developer.android.com/develop/ui/compose/performance/stability/fix): annotations assert a contract rather than changing mutability.
- [Android coroutine testing](https://developer.android.com/kotlin/coroutines/test) and [StateFlow](https://kotlinlang.org/api/kotlinx.coroutines/kotlinx-coroutines-core/kotlinx.coroutines.flow/-state-flow/): scheduler control and conflation.
- [Compose synchronization](https://developer.android.com/develop/ui/compose/testing/synchronization): automatic clock advancement, idleness and work outside the Compose clock.
- [Android KMP plugin](https://developer.android.com/kotlin/multiplatform/plugin): actual plugin/migration conditions and test compilations.
- [Ktor logging](https://ktor.io/docs/client-logging.html) and [bearer authentication](https://ktor.io/docs/client-bearer-auth.html): configured redaction/auth behavior; confirm installed-version defaults.
- [Android hardcoded secrets](https://developer.android.com/privacy-and-security/risks/hardcoded-cryptographic-secrets) and [DataStore](https://developer.android.com/topic/libraries/architecture/datastore): inspect actual packaged secrets/storage implementation.

## Package validation limits

The four skills' evaluation files add relevant regression scenarios. Structural validators and author-side source/contract review are distinct from a fresh model trial. No Android/KMP application was compiled, no real device/iOS runner or user study was exercised, and no cross-model accuracy/efficiency improvement is claimed. Versions and references describe the new guidance; historical trial records retain their original version and scope.
