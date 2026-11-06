# Native Android skill evaluation scenarios

Maintainer cases for the whole collection. Run selected cases on the actual model/host with isolated synthetic fixtures before claiming model quality or efficiency. The rows are authored expectations, not a measured pass rate or an application-security certification. Do not expose the expected solution to an independently evaluating agent.

| Skill / task | Required observable result | Failure to catch |
| --- | --- | --- |
| Module structure: add a small feature to an existing AGP project | Uses actual wrapper/catalog/variant; permitted dependencies and complete bindings/resources; affected build checks recorded | Rewrites architecture, invents versions or applies incompatible Kotlin plugins |
| Data: two refreshes and logout before a delayed response | Deliberate serialization/version policy; cache retained on failure; stale session cannot commit | Old data overwrites newer/account data; local-write error discarded |
| Errors: malformed success body, bodyless success, TLS rejection and cancellation | Decoding is inside protected boundary; Unit supported; TLS not treated as offline/retry; cancellation propagates | Trust-all workaround; swallowed cancellation; fake success |
| Koin: open a typed detail destination with SavedStateHandle | Full constructor graph, scoped owner, correct route ID and no shared global handle | Container verification alone misreported as real navigation validation |
| UI Design / presentation: retry fails with previously saved data | Immutable observed content retained; loading/error transitions; no invented event channel; sensitive state excluded | UI clears cache, writes on recomposition, persists credentials |
| UI Design / Compose architecture: search results finish out of order | Current query/session owns result; correct effect lifecycle and main-safe work | Stale result applied; context leak; annotations replace profiling |
| UI Design / components: icon-only delete with disabled and large-font variants | Correct callback, target/name/semantics and native resource owner; actual interaction check | Comment-only stub, duplicate announcement or clickable disabled UI |
| UI Design / navigation: attacker domain containing trusted host text and foreign record ID | Exact parsed URI validation and operation-level authorization; recovery on invalid input | Substring host matching or typed route treated as authorization |
| Background: old account's queued upload after login switch | Reject stale owner, bounded retry, idempotent operation, correct initialization | Uses new token for old outbox; WorkManager initialized twice |
| Unit tests: a suspend failure hidden by an eager fake | Shared scheduler and controllable gate; public behavior assertions; cleanup | Sleeps, unrelated schedulers, immediate fake hides loading race |
| Integration: restore encrypted data without its original key | Safe recovery/reauthentication; migration/data policy preserved; driver boundary disclosed | Plaintext fallback, destructive migration or false full-device claim |
| UI tests: real click/Back/IME and lifecycle-sensitive error | Actual controls, synchronized observable outcome, clear host/device distinction | Calls handler directly or claims TalkBack/process-death proof from a screenshot |
| Cybersecurity / Android: exported component forwards an arbitrary nested intent | Restricted entry, allowlisted operation/caller/data, negative test and release manifest inspection | Forwarded privileged intent or hidden UI treated as enforcement |
| Background: permanent revocation during a periodic schedule | Stops future ineligible work through schedule cancellation/eligibility, preserves committed-effect evidence and uses runtime WorkerParameters | Treats failure of one periodic run as permanent cancellation or shares one run's WorkerParameters |
| Data: session changes between a successful check and a suspended write | Commit is account-bound/serialized with session replacement and cannot become visible in the new account | Adds a pre-write boolean check while retaining a check/use race |
| UI Design / state: concurrent StateFlow updates | Pure update transformation and separately owned external effect | Repeats writes or ID allocation inside a retried update lambda |

## Source review before integration — 2026-11-06

Reviewed all twelve existing native skills and their two supporting references. Added explicit execution guidance and a dedicated Android security skill, targeted trust-boundary/concurrency/release checks, a complete controllable Notes fake and these cross-skill cases. Existing technical patterns and project-stack choices were retained. Version-sensitive security guidance was checked against Android Developers; APIs must still match the consuming project's actual SDK/dependencies.

Structural/link checks and executable extracted Kotlin checks are reported separately in the task handoff. These authored cases are not independent executions on smaller models. A full app build, release artifact inspection, device/assistive session and real backend assessment require a representative consuming project; none is inferred from these documents.

Executed extracted-Kotlin checks during this maintenance: typed-result helpers, repository and Notes fake snippets compiled together with the installed Kotlin compiler and real kotlinx-coroutines-core. Seven existing behavioral scenario groups passed; additional checks confirmed serialized refresh, cancellation releasing the lock, a typed fake failure preserving rows and a controllable fake's cancellation. This is host logic evidence with in-memory collaborators, not compilation against AndroidX/Ktor, Room transaction behavior or a test of TLS validation. No smaller-model behavioral pass rate is asserted.

After integration, UI procedures belong to UI Design and security procedures to Cybersecurity; the table uses those current owners. Final collection maintenance clarified conditional sample stacks, handoffs, Koin runtime parameters, periodic-work termination and account commit boundaries. The new rows are authored regression tasks, not additional executed app/model trials.
