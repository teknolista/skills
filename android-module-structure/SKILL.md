---
name: android-module-structure
description: Implement native Android/Kotlin JVM module boundaries, Gradle conventions and build configuration in an existing or authorized project. Use for concrete module/build changes; use penta-pro for requirements, architecture proposals and readiness specifications, and peer-review for read-only code review.
metadata:
  version: "1.2.3"
---

# Native Android Module Structure

Before editing, inspect the actual project, toolchain, contracts and authorized scope. Implement a coherent change, run the relevant available checks, and distinguish executed evidence from pending work. Cross-package references are optional navigation: if a companion is unavailable, use the project-owned contract rather than inventing that companion's contents.

Before running project commands, inspect the relevant build/test scripts, plugins, hooks, configured endpoints and inherited credentials. Choose checks within the authorized scope; use isolated fixtures or test accounts when effects are possible. A task named test, lint or build can still contact shared services or publish artifacts. Reuse existing authorization, but do not treat a validation request as permission for deployment or destructive operations.

Reuse the project's existing types and selected libraries; sample Result, route, DI and test definitions are conditional patterns, not authority for a stack migration. For a material handoff, carry the target snapshot/variant, governing behavior, actual checks and remaining gap. Implementation completion, independent review and release acceptance remain separate.

Build Android applications with `com.android.application`, Android libraries with `com.android.library`, and framework-free modules with `org.jetbrains.kotlin.jvm`. Use Jetpack Compose and AndroidX artifacts. Project/source-set boundaries are Android and JVM: `src/main`, `src/test`, `src/androidTest`, and Android build variants.

## Choose boundaries from ownership

Start with the project's existing structure and complexity. Feature-first layering is useful when features have independent data/presentation responsibilities; small features may share one module. Do not create a module for one trivial helper or require a domain/use-case layer without a real responsibility.

```text
:app                            Application, manifest, navigation/DI composition
:core:domain                    Shared domain contracts and error types
:core:data                      Shared transport/storage policy
:core:presentation              Shared Android UI helpers and resource-backed text
:core:design-system             Jetpack Compose theme, primitives, icons
:core:database                  Shared Room database, entities, DAOs, migrations
:core:testing                   Reusable test fixtures only, when needed
:feature:notes:domain           Feature contracts and models, if a separate module pays off
:feature:notes:data             Data implementations and DTO mapping
:feature:notes:presentation     ViewModels, routes, screens, feature resources
build-logic/                    Included Gradle build, not an application subproject
```

Keep code within the owning feature until multiple consumers justify a shared module. A database owned by one feature may use `:feature:notes:database`; do not duplicate a shared database per feature. Put related schema/migration ownership in the same database module.

| Module | Permitted dependencies in this layout |
|---|---|
| feature presentation | Its domain/API, core domain/presentation/design-system |
| feature data | Its domain/API, core domain/data, owning database |
| feature domain | Core domain and required Kotlin/JVM libraries; no Android UI/data implementation |
| database | Room and schema dependencies; no presentation |
| app | Required feature entrypoints and DI modules; application assembly |
| test fixtures | Test-facing contracts/utilities; never a production dependency |

Avoid direct feature implementation dependencies. Coordinate cross-feature navigation through callbacks assembled in the app; extract a narrow contract for genuinely shared domain interactions. Use Gradle `implementation` by default and `api` only when a dependency is part of a module's public API. Feature entrypoints must be public when the app consumes them; `internal` is module-scoped.

## Build configuration

Use an included `build-logic` build and version catalog for repeated configuration. Keep plugin versions, dependency versions, BOMs, and SDK/JVM choices compatible with the Gradle wrapper and Android Studio. Do not upgrade the entire toolchain as a side effect of adding a feature.

Read [native build-logic examples](references/build-logic.md) when creating conventions, Room/KSP setup, or catalog wiring. It covers included-build catalog access, native application/library conventions, Compose tooling, and registration through precompiled script plugin filenames.

AGP 9+ enables built-in Kotlin by default, but inspect effective `android.builtInKotlin` settings and supported module overrides before changing plugins. When built-in Kotlin is enabled, do not also apply `org.jetbrains.kotlin.android` to that Android module. On a supported opt-out/legacy configuration that still uses the Kotlin Android plugin, retain it until a deliberate migration; the AGP version alone does not prove which mode a module uses. Kotlin/JVM modules still use their own Kotlin plugin. Align the Compose compiler and serialization compiler plugins with the effective Kotlin compiler; inspect AGP's embedded Kotlin compatibility when applicable. Use public `com.android.build.api.dsl` APIs, not Gradle/AGP internals.

For a deliberate built-in Kotlin migration, also inspect annotation processing and source directories: legacy `org.jetbrains.kotlin.kapt` is incompatible with that mode; use supported KSP or the documented AGP legacy-kapt path when needed. Move custom Kotlin sources through supported Android source APIs rather than assuming the old Kotlin source-set DSL still applies. Do not remove a processor until its generated-code consumers have a verified replacement.

Keep Java and Kotlin bytecode targets aligned, and choose a JDK supported by the selected Gradle/AGP versions. Enable core-library desugaring only for required Java APIs on the supported minSdk. Enable configuration/build caches where supported and fix incompatible custom tasks before treating caching as effective. Prefer provider-backed configuration over environment reads or internal `gradleLocalProperties` helpers.

## Native dependencies and resources

Use AndroidX Compose via its BOM, AndroidX Navigation/Lifecycle/Room/DataStore/WorkManager, and the chosen native Koin and Ktor/OkHttp integrations. These libraries do not require additional platform targets. Domain modules can use coroutines, `java.time` where supported by their runtime consumers, and other Kotlin/JVM libraries without becoming Android modules.

Each Android module owns its `namespace`, `src/main/res`, strings, plurals, and drawables. Share resources through appropriate Android library modules or public UI/accessor APIs. Reference the owning module's `R`; respect non-transitive R classes and resource visibility. Prefix resource names where that prevents collisions.

Use `BuildConfig` only for non-secret build configuration such as an endpoint or public client identifier; explicitly enable generation in modules that need it. Inject environment configuration into services for testability. `local.properties` and CI variables keep values out of source control, but generated APK constants are extractable. Keep server secrets on a server; configure signing credentials outside committed build files. Configure release shrinking/resource shrinking and keep rules according to the app's libraries, then exercise the release build.

The retained stack is used only through Android/JVM artifacts and Android source sets:

| Concern | Native project choice |
|---|---|
| UI and adaptation | AndroidX Jetpack Compose/Material 3 and AndroidX adaptive/window APIs |
| Navigation/lifecycle | AndroidX Navigation and Lifecycle |
| DI | Koin Android integrations |
| HTTP/serialization | Ktor with OkHttp and Kotlin serialization |
| Persistence | Android Room and Preferences/Proto DataStore |
| Images | The project's Android Compose image loader, such as Coil; preserve lifecycle/caching behavior and test loading/error content |
| Logging | Android logging or the established Android logger, with redaction and release policy |
| Durable background work | AndroidX WorkManager |
| Tests | Supported JUnit host/device engines, coroutine-test, Turbine, and the established assertions |

## Add a feature

1. Select the smallest useful module boundaries; add chosen modules to `settings.gradle.kts`.
2. Apply the native conventions and assign a unique namespace where required.
3. Add explicit permitted dependencies, native resources, and the feature API.
4. Register its data/ViewModel bindings through [Koin](../android-di-koin/SKILL.md) and routes through [navigation](../ui-design/references/android/navigation.md).
5. If using Room, configure KSP/schema export and migration coverage in the owning database module.
6. Run affected unit tests, lint, and a representative debug/release assembly. Run relevant device tests; do not report a documented command as an executed result.

Sources: [built-in Kotlin](https://developer.android.com/build/migrate-to-built-in-kotlin), [Gradle convention plugins](https://docs.gradle.org/current/userguide/implementing_gradle_plugins_convention.html).

## Supply chain and release handoff

Pin reproducible tool/dependency inputs and verify their origin before adding a repository or plugin. Avoid dynamic versions, arbitrary executable Gradle snippets from error pages, broad repository fallbacks, or disabling dependency verification to resolve a build. Keep signing credentials outside tracked files and restrict CI access. Inspect the merged release manifest, effective network/backup config and minified output; a clean debug build alone cannot establish release readiness. See [Android security](../cybersec/references/android-controls.md).

Use targeted lint and meaningful host/device checks for affected behavior. For startup or scrolling performance work, capture a baseline and compare profileable/release behavior using supported benchmark tooling and representative devices; do not infer speed from fewer recompositions or more modules. Baseline Profiles and caching are optional measured optimizations, not substitutes for functional checks.

Maintainers evaluating another model/host can use the [cross-skill scenarios](evals/scenarios.md). A structural validator does not establish how well that model implements an Android app.

For concrete Android code/build changes, the [execution guidance](references/execution.md) supplies the inspect/implement/verify/handoff procedure without replacing the generic planning or assessment owners.
