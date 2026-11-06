---
name: android-data-layer
description: Implement or debug native Android repositories, Ktor/OkHttp clients, Room persistence, DataStore and synchronization. Use for data-layer code changes; use peer-review for independent assessment and cybersec for security audits.
metadata:
  version: "1.2.1"
---

# Android Data Layer

Before editing, inspect the actual project, toolchain, contracts and authorized scope. Implement a coherent change, run the relevant available checks, and distinguish executed evidence from pending work. Cross-package references are optional navigation: if a companion is unavailable, use the project-owned contract rather than inventing that companion's contents.

Reuse the project's existing types and selected libraries; sample Result, route, DI and test definitions are conditional patterns, not authority for a stack migration. For a material handoff, carry the target snapshot/variant, governing behavior, actual checks and remaining gap. Implementation completion, independent review and release acceptance remain separate.

Use Android libraries and standard `src/main`, `src/test`, and `src/androidTest` directories. Domain contracts are Kotlin/JVM code without Android framework dependencies. See [module ownership](../android-module-structure/SKILL.md), [typed errors](../android-error-handling/SKILL.md), and [Koin wiring](../android-di-koin/SKILL.md).

## Ownership and models

- A data source encapsulates a concrete transport or storage mechanism. A repository exposes application data and coordinates sources or policy. A repository may wrap one source; do not add an abstraction merely to satisfy a source-count rule.
- Place contracts consumed by presentation in the domain/API module so presentation does not import concrete data implementations. Adapt this arrangement to an existing architecture instead of splitting every trivial feature into three modules.
- Separate network DTOs and Room entities from domain models when their contracts differ. Keep serialization, database annotations, and transport details out of domain contracts. Use data-layer mapping extensions such as `NoteDto.toNote()` and `NoteEntity.toNote()`.
- Name concrete implementations by their mechanism or policy (`RoomNoteDataSource`, `OfflineFirstNoteRepository`). Follow established project naming when it differs.

## Ktor on Android

Use `io.ktor:ktor-client-okhttp` with the matching Ktor core, auth, content-negotiation, JSON serialization, and optional logging artifacts. Manage versions in the catalog. The Android app needs the `android.permission.INTERNET` manifest permission.

Create and inject one owned client; accept an engine to reuse production configuration with `MockEngine` in tests. Do not create a new client per request. The owner closes clients/engines in tests and explicitly managed scopes. Configure `expectSuccess = false` for the status-based helper in [error handling](../android-error-handling/SKILL.md).

Set bounded connection/request/socket timeouts appropriate to the service. Configure a trusted HTTPS base URL with Ktor `defaultRequest` and URL builders; test path-prefix handling rather than concatenating arbitrary URLs. Use JSON content negotiation for typed bodies. Retry only selected transient failures with bounds and backoff; do not retry non-idempotent writes without a server-supported idempotency contract.

Enable verbose logging only in debug builds and sanitize authorization/cookie headers. Payloads may also contain tokens or personal data: prefer header/status logging, and never assume header redaction makes body logging safe.

## Authentication and DataStore

Use Ktor bearer authentication with injected token storage, bounded refresh, and explicit session invalidation. Serialize concurrent refreshes or use the selected plugin version's coordination; test concurrent 401s, rejected refresh, logout during refresh, and stale responses. Avoid recursion when the refresh call itself receives 401. Restrict token transmission to intended hosts.

DataStore persists small preferences/settings. It does not by itself establish an encrypted credential vault. Choose credential protection from the threat model; Android Keystore protects cryptographic keys, not arbitrary strings. Never describe APK constants or `local.properties` as protection for backend secrets.

Keep **one DataStore instance per file per process**. A top-level Android delegate is a simple native construction:

```kotlin
import android.content.Context
import androidx.datastore.preferences.preferencesDataStore

val Context.sessionDataStore by preferencesDataStore(name = "session")
```

Provide `androidContext().sessionDataStore` as a Koin singleton. Do not also create a second factory instance for that file. For multiple processes, explicitly choose the supported multiprocess API and use it consistently. Keep stored values immutable, handle corruption according to a documented recovery policy, and use transactional updates for related fields.

## Room setup and storage errors

Place a shared database in `:core:database`; use `:feature:<name>:database` only when independent ownership justifies it. Keep entities, DAOs, the database class, exported schemas, and migrations together. Data modules depend on that database module; presentation does not access DAOs directly.

Use `androidx.room:room-runtime`, the Room compiler through KSP, and `androidx.room`'s Gradle plugin with `schemaDirectory(...)`. Match compiler/runtime/plugin versions and commit exported schemas. Construct a singleton with `Room.databaseBuilder(applicationContext, AppDatabase::class.java, "app.db")`. No generated-constructor abstraction is required. Prefer suspend DAO operations and observable `Flow` queries; do not enable main-thread queries in production.

Catch only known storage failures when a typed result is required. Rethrow `CancellationException` before broader catches. A flow query can also fail during collection: define whether that failure is propagated or materialized as state, rather than silently completing or reporting an empty database.

Choose automatic migrations only for supported schema changes; use manual migrations for transformations and explicit migration specs for ambiguous changes. Test migration paths with exported schemas and representative rows. Do not silently enable destructive migration for user-owned data. Use transactions for multi-table updates and cache replacement; make write conflicts and uniqueness rules explicit.

## Offline-first when required

Use the database as the observable source of truth. Network refresh writes to storage; UI observes storage. Keep refresh failures separate from cached data so a failed refresh does not erase useful content.

```kotlin
import kotlinx.coroutines.sync.Mutex
import kotlinx.coroutines.sync.withLock

// Domain declarations; Note is the domain model.
interface NoteRepository {
    fun observeNotes(): kotlinx.coroutines.flow.Flow<List<Note>>
    suspend fun refresh(): EmptyResult<DataError>
}
interface NoteLocalDataSource {
    fun observeNotes(): kotlinx.coroutines.flow.Flow<List<Note>>
    suspend fun replaceAll(notes: List<Note>): EmptyResult<DataError.Local>
}
interface NoteRemoteDataSource {
    suspend fun fetchNotes(): Result<List<Note>, DataError.Network>
}

class OfflineFirstNoteRepository(
    private val local: NoteLocalDataSource,
    private val remote: NoteRemoteDataSource
) : NoteRepository {
    private val refreshMutex = Mutex()
    override fun observeNotes() = local.observeNotes()

    override suspend fun refresh(): EmptyResult<DataError> = refreshMutex.withLock {
        when (val result = remote.fetchNotes()) {
            is Result.Success -> local.replaceAll(result.data)
            is Result.Error -> result
        }
    }
}
```

`replaceAll` must be atomic if partially replacing cached rows would expose an invalid state. A local-write failure is returned, not discarded inside `onSuccess`. A network error leaves the existing database untouched. This example models a replaceable read cache; do not delete unsynchronized user edits during refresh. Offline writes need an outbox, stable operation IDs, conflict policy, and retry scheduling; use [Android background work](../android-background/SKILL.md) for durable sync.

For a one-shot cache-fallback API, explicitly `return` the local outcome in the failure branch. Calling `local.read()` inside `onFailure` does not change the original error result. Do not present that pattern as offline-first observation.

## Verification

Test DTO mapping, malformed JSON, storage errors, cancellation, atomic refresh, local-write failure, cache retention, refresh races, and relevant migrations with [integration testing](../android-integration-testing/SKILL.md). Use an injected clock for expiration and a controllable transport for deterministic errors.

Sources: [Room migrations](https://developer.android.com/training/data-storage/room/migrating-db-versions), [DataStore](https://developer.android.com/topic/libraries/architecture/datastore), [Ktor testing](https://ktor.io/docs/client-testing.html).

## Concurrent refresh, identity and bounded data

Scope the repository and its local source to one account/tenant. Serialize competing refresh commits or compare request/version identities so a slow response cannot overwrite newer data. For the simple repository example, a single instance serializes refreshes; this is not cross-process synchronization. Before committing, verify that the captured session is still current. Test logout during a request and account switches with pending writes.

Bind queries and writes to the captured account's storage key/database. A session check followed by a suspending write to a shared “current account” store still has a race. Coordinate the check and commit with session replacement at the actual writer boundary, or keep storage strictly account-partitioned and prevent stale results from becoming visible. A Mutex protects only participants using that same lock; logout, another repository instance or another process is not automatically covered. The sample above omits session policy and must not be presented as a complete multi-account implementation.

Validate DTO domain constraints after decoding; well-formed JSON can still contain invalid IDs, amounts or sizes. Bound pagination, response/media sizes and in-memory accumulation. Do not interpolate external strings into SQL or filesystem paths. See [security boundaries](../cybersec/references/android-controls.md) for credential hosts, backups, file sharing and account-scoped caches.
