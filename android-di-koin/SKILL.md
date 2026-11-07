---
name: android-di-koin
description: Implement or debug Koin bindings, Android ViewModel ownership and application/worker dependency wiring. Use for concrete DI code changes; use peer-review for independent inspection and ui-design for screen design.
metadata:
  version: "1.2.2"
---

# Android Dependency Injection with Koin

Before editing, inspect the actual project, toolchain, contracts and authorized scope. Implement a coherent change, run the relevant available checks, and distinguish executed evidence from pending work. Cross-package references are optional navigation: if a companion is unavailable, use the project-owned contract rather than inventing that companion's contents.

Before running project commands, inspect the relevant build/test scripts, plugins, hooks, configured endpoints and inherited credentials. Choose checks within the authorized scope; use isolated fixtures or test accounts when effects are possible. A task named test, lint or build can still contact shared services or publish artifacts. Reuse existing authorization, but do not treat a validation request as permission for deployment or destructive operations.

Reuse the project's existing types and selected libraries; sample Result, route, DI and test definitions are conditional patterns, not authority for a stack migration. For a material handoff, carry the target snapshot/variant, governing behavior, actual checks and remaining gap. Implementation completion, independent review and release acceptance remain separate.

Use the selected Android Koin integration and compatible versions. Keep dependency injection at composition roots and constructors; do not use a service locator inside domain logic. Respect an existing DI stack rather than adding Koin alongside another container without a migration need.

## Dependencies and imports

Use `io.insert-koin:koin-android` for application startup/Context and `io.insert-koin:koin-androidx-compose` for the Android Compose integration. Use the Koin BOM or consistently aligned catalog versions. Add `koin-androidx-workmanager` only for workers. Do not assume an online example's imports match the installed Koin release.

Constructor DSL imports include `org.koin.core.module.dsl.singleOf` and `factoryOf`; `bind` is the declaration DSL, and `viewModelOf`/`koinViewModel` imports must match the selected integration version. Recent releases expose ViewModel DSL through `org.koin.core.module.dsl.viewModelOf` and Compose acquisition through `org.koin.compose.viewmodel.koinViewModel`; older Android integrations expose AndroidX package paths. Verify exported symbols rather than adding another UI platform integration merely to satisfy an import.

## Feature bindings and lifetimes

Create modules for actual bindings, usually one per feature layer. Assemble them in the Android application. Prefer constructor references for ordinary constructors; use lambdas for factory calls, named qualifiers, runtime parameters, and controlled initialization.

```kotlin
val notesDataModule = module {
    singleOf(::OfflineFirstNoteRepository) { bind<NoteRepository>() }
}
val notesPresentationModule = module {
    viewModelOf(::NoteListViewModel)
    viewModelOf(::NoteDetailViewModel)
}
```

A repository constructor's data-source interfaces must also have bindings. Register the native transport engine, configured HttpClient, DAO/database, and DataStore only where needed; use the construction/lifetime policies in [data layer](../android-data-layer/SKILL.md). Prefer a singleton for an owned database/client, a ViewModel definition for a ViewModel, and a factory when a new instance per resolution is intended. Do not turn Activity-scoped state into a singleton by default.

## Application composition

```kotlin
class NotesApplication : Application() {
    override fun onCreate() {
        super.onCreate()
        startKoin {
            androidContext(this@NotesApplication)
            modules(coreDataModule, notesDataModule, notesPresentationModule)
        }
    }
}
```

Declare the application class in `AndroidManifest.xml`. Start Koin once in that process before resolving dependencies; do not restart it on every Activity or screen composition. Account for Android startup providers/workers and extra processes if the app uses them.

Acquire a ViewModel at the Root/destination:

```kotlin
@Composable
fun NoteDetailRoot(viewModel: NoteDetailViewModel = koinViewModel()) {
    // Collect with lifecycle awareness; pass state and callbacks to Screen.
}
```

Use the current navigation entry's `ViewModelStoreOwner`/creation extras so arguments reach `SavedStateHandle`. Declare `SavedStateHandle` as a ViewModel constructor parameter; do not register a global singleton handle or create a fresh handle on every recomposition. A shared graph ViewModel requires an intentional parent owner. Qualifiers/keys distinguish instances within the same owner; parameters are applied on creation, not a command to mutate an existing ViewModel.

Resolve dependencies once at appropriate Compose boundaries. Pass values/callbacks to children rather than a ViewModel or container. Keep an Android Activity Context scoped to the Activity; use application Context for application-lived services. Close resources in their owner, and release scopes without retaining destroyed Android components.

## Workers and verification

Read [background work](../android-background/SKILL.md) for factory ordering, initializer removal, and worker registration. Do not initialize WorkManager twice with competing factories.

Use Koin graph verification supported by the installed version and an application startup test for required bindings, qualifiers, parameterized factories, and saved-state/navigation owners. Verification of definitions alone does not execute every Android constructor. In tests, use isolated containers where possible and close/reset the container so overrides do not leak across tests.

Sources: [Android Koin ViewModels](https://insert-koin.io/docs/reference/koin-android/viewmodel/), [Compose ViewModels](https://insert-koin.io/docs/reference/koin-compose/compose-viewmodel/), [Koin WorkManager](https://insert-koin.io/docs/reference/koin-android/workmanager/).

## Resolve all bindings before calling a feature complete

Walk each constructor from the app composition root: concrete implementation, interface binding, qualifier, runtime parameters and lifetime. A module definition containing only a repository binding is not a complete graph if its data sources are absent. For a destination with SavedStateHandle, exercise resolution under the real navigation entry owner; do not fix it by registering one global handle.

Account-scoped services must not outlive their credentials/data policy. Close/reset owned clients and scopes on session replacement, reject late old-account writes, and never retain Activity/Composable references in singleton definitions. Verify the merged Application/startup configuration in the actual release variant, not only a test container with overrides.
