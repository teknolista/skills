---
name: android-unit-testing
description: Author, run or debug isolated Kotlin/JVM and Android logic tests using fakes and deterministic coroutine scheduling. Use for test implementation tasks; use peer-review to assess test effectiveness without changing source and ui-design for screen acceptance design.
metadata:
  version: "1.2.1"
---

# Android Unit Testing

Before editing, inspect the actual project, toolchain, contracts and authorized scope. Implement a coherent change, run the relevant available checks, and distinguish executed evidence from pending work. Cross-package references are optional navigation: if a companion is unavailable, use the project-owned contract rather than inventing that companion's contents.

Reuse the project's existing types and selected libraries; sample Result, route, DI and test definitions are conditional patterns, not authority for a stack migration. For a material handoff, carry the target snapshot/variant, governing behavior, actual checks and remaining gap. Implementation completion, independent review and release acceptance remain separate.

Test the public contract and observable behavior. Before writing tests, enumerate plausible ways the behavior could fail: inputs, boundaries, collaborator errors, ordering, cancellation, and restoration. Spend coverage on distinct failure modes, not duplicated assertions. Use the [case catalogue](references/test-cases.md) when the unit handles text, arithmetic, time, or complex state.

## Boundaries and stack

An isolated test can wire multiple real classes when collaborators are pure and cheap. Fake network/storage/time boundaries; do not fake a pure validator merely because it is another class. Real Room/SQLite, files, sockets, and Android lifecycle integration belong in [integration testing](../android-integration-testing/SKILL.md). Ktor MockEngine does not perform real network I/O; tests using it may exercise client integration without a server.

Use `src/test` for JVM-hosted tests and `src/androidTest` when real Android framework/device behavior is needed. A pure framework helper can still be a small unit tested on a device. Robolectric is an optional supported JVM tool when suitable; it is not evidence of identical device behavior. Test critical platform behavior on Android.

Preserve the project's test framework: JUnit5 requires Jupiter dependencies and `useJUnitPlatform()` for host tasks; JUnit4 remains valid and Android instrumented runner support differs. Use AssertK or the established assertion library, Turbine for Flow emissions, and `kotlinx-coroutines-test` for virtual time. Do not move device tests onto Jupiter without a supported runner integration.

## Coroutine scheduling

Use one shared `TestCoroutineScheduler` for a test's dispatchers. Prefer `StandardTestDispatcher` when testing ordering, suspension, or races; use `UnconfinedTestDispatcher` deliberately for eager collectors or simple cases. Eager entry is not production scheduling and does not guarantee all suspend work completes immediately.

```kotlin
@OptIn(ExperimentalCoroutinesApi::class)
class NoteListViewModelTest {
    private val dispatcher = StandardTestDispatcher()

    @BeforeEach
    fun setUp() { Dispatchers.setMain(dispatcher) }

    @AfterEach
    fun tearDown() { Dispatchers.resetMain() }

    @Test
    fun `refresh failure preserves existing notes`() = runTest {
        val repo = FakeNoteRepository(initialNotes = listOf(Note("n1", "Saved")))
        val vm = NoteListViewModel(repo)
        try {
            runCurrent() // Starts the repository observation under test.
            repo.refreshResult = Result.Error(DataError.Network.REQUEST_TIMEOUT)
            vm.onAction(NoteListAction.OnRefreshClick)
            advanceUntilIdle()
            assertThat(vm.state.value.notes.map { it.id }).containsExactly("n1")
            assertThat(vm.state.value.isRefreshing).isFalse()
            assertThat(vm.state.value.error).isNotNull()
        } finally {
            vm.viewModelScope.cancel()
        }
    }
}
```

This example assumes the repository/VM contracts described by the data and presentation skills. Use the [complete controllable fake](references/notes-fake.md) rather than inventing its constructor or refresh behavior. Imports include JUnit Jupiter annotations, coroutine test APIs, `kotlinx.coroutines.Dispatchers`, `kotlinx.coroutines.cancel`, and `androidx.lifecycle.viewModelScope`; use the project's assertion imports. Reset global Main even after assertion failure and cancel ViewModel jobs or clear the owning `ViewModelStore` at teardown. `runTest` uses the replaced Main scheduler; do not create unrelated schedulers inside the fake.

For races, control a fake with deferred responses or gates: start request A, start B, finish B, then finish A; assert the agreed stale-result policy. For deadlines, move virtual time to just before/at/after the threshold. `advanceTimeBy` can require `runCurrent()` to execute work scheduled exactly at the new time. Do not use real sleeps or arbitrary multi-second advances as synchronization.

## Flow, state, and effects

Use Turbine `test { ... }` for observable emissions, with a collector active before triggering the action. `StateFlow` conflates equal/rapid updates: do not assume every intermediate loading value is observable. If a loading state is part of the contract, suspend the fake response and assert while it is pending; otherwise assert the final state.

For lazily shared/stateIn flows, keep an active collector in `backgroundScope` using the test scheduler. Cancel collectors at the end. Test best-effort ViewModel effects with an outcome only the ViewModel can decide, such as an async operation result; ordinary click-driven navigation belongs to UI callbacks. Prefer acknowledged state for effects requiring reliable delivery and test acknowledgement, duplicate consumption, and lifecycle re-entry.

## Fakes and fixtures

Prefer working in-memory fakes for repository/service contracts. Expose configured outcomes and controllable completion, not only a boolean that can represent one error. Mirror cancellation and expected error semantics. Keep mocks for cases where an observable fake is impractical; avoid asserting incidental call order instead of behavior.

A shared `:core:testing` JVM/Android test-fixtures module can own reusable fakes and clock utilities. Test-only dependencies must not leak into production. Keep mutable fake state per test, and use real pure collaborators where useful. Clock injection should distinguish wall time from monotonic elapsed time.

## Saved state and scope

Construct a real `SavedStateHandle(mapOf("noteId" to "n1"))` to test initialization and required-key validation. Test updates to the handle and restoration from captured values. This verifies the ViewModel contract, not the OS save/restore path; use Android lifecycle/restoration tests for that path. Do not mock the handle or promise persistence after force-stop.

## Coverage and completion

Cover meaningful success/failure distinctions, including error mappings that produce different behavior. Parameterized tests are useful for one contract across many inputs; retain input-specific failure diagnostics. Do not call two tests redundant merely because one production change could break both: independent contracts may legitimately share implementation.

Stop when the scoped behavior and relevant risks have meaningful coverage; document uncovered boundaries. Mutation testing is optional when explicitly requested, uses a compatible available tool, and can reveal weak assertions. Surviving mutants require investigation, not automatic production API changes, and a perfect score is not proof of exhaustive correctness.

When coverage reporting is needed, use Android/JVM JaCoCo or a compatible Kover setup without adding other targets. Report the actual variant, exclusions, and line/branch limits; coverage percentage alone does not establish useful assertions.

Run affected tests using the module's actual task: for example `:feature:notes:presentation:testDebugUnitTest` for an Android debug variant, or `:core:domain:test` for a Kotlin/JVM module. Run device tests separately. Report commands, results, and limits accurately.

Sources: [coroutine testing](https://developer.android.com/kotlin/coroutines/test), [Flow testing](https://developer.android.com/kotlin/flow/test).

## Parallelism, fakes and failure assertions

Dispatchers.setMain changes global process state. Do not run tests that replace Main concurrently without isolation; use the test engine's supported serialization/resource-lock configuration or separate processes. Reuse one scheduler for all dispatchers under test, but create independent fixture state per test. If a fake completes immediately, it may conceal the loading, cancellation or interleaving behavior you intended to test: add controllable suspension before asserting that behavior.

Use the same domain interface in the fake and production owner. Test each error that changes observable behavior; use tables for equivalent mappings. Include cancellation identity and stale-account/stale-request rejection when relevant. A passing test against a fake that silently reports every write as success does not exercise storage failure.
