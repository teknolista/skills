---
name: android-integration-testing
description: Author, run or debug non-UI native Android boundary tests for Room, Ktor clients, DataStore, DI and WorkManager. Use for integration-test implementation; use peer-review for independent evidence assessment and cybersec for security audits.
metadata:
  version: "1.2.1"
---

# Android Integration Testing

Before editing, inspect the actual project, toolchain, contracts and authorized scope. Implement a coherent change, run the relevant available checks, and distinguish executed evidence from pending work. Cross-package references are optional navigation: if a companion is unavailable, use the project-owned contract rather than inventing that companion's contents.

Reuse the project's existing types and selected libraries; sample Result, route, DI and test definitions are conditional patterns, not authority for a stack migration. For a material handoff, carry the target snapshot/variant, governing behavior, actual checks and remaining gap. Implementation completion, independent review and release acceptance remain separate.

Choose the smallest test environment that exercises the real boundary. Use [unit tests](../android-unit-testing/SKILL.md) for isolated behavior and [UI tests](../android-ui-testing/SKILL.md) when rendering/input/navigation are part of the claim. Multiple real classes alone do not require a device or a server.

## Test location and dependencies

Use Kotlin/JVM or Android `src/test` for supported host tests; use `src/androidTest` with AndroidJUnitRunner for real Android storage/framework behavior. Preserve the project's supported JUnit engine. Typical fixtures include Room testing, Ktor MockEngine or a local MockWebServer, AndroidX test core, WorkManager testing, and coroutine test utilities. Align versions with production libraries.

MockEngine simulates the HTTP client engine without sockets. A loopback server exercises actual HTTP transport and can test disconnects/headers/timing; a controlled real service environment is needed for deployment/auth/backend-contract claims. Select the boundary deliberately and avoid external network dependence in ordinary deterministic suites.

## Repository and HTTP contracts

Reuse the production client configuration with an injected test engine; otherwise the test may miss serialization/auth/default URL bugs. Match method, host/path, query, headers, and body. Make unexpected requests fail immediately. Test response decoding and typed statuses, malformed success payloads, empty-body success, timeout/connectivity classification, and cancellation.

Exercise concurrent token refresh, rejected refresh, retry bounds, allowed hosts, idempotency of writes, and logout/session races when relevant. Do not use real credentials or enable sensitive body logging. Test base-URL path prefixes and encoded route arguments to catch incorrect string concatenation.

For offline-first repositories, collect the real storage stream, refresh, and observe committed changes. Verify a failed network refresh preserves cached data, a failed local write is reported, partial transactions roll back, and pending user edits survive refresh. Separate the refresh error from the observable cache.

## Room and migrations

An in-memory Room database still uses SQLite and is an integration boundary. Construct it per test using application/test Context and the production database/DAOs; close it after each test. Use suspend operations/Flow and controlled scheduling rather than enabling main-thread queries to conceal production violations.

Test constraints, transactions, conflict policy, observable invalidation, and actual DAO queries with representative data. Test migrations from supported historical schemas with `MigrationTestHelper` and committed schema exports; verify both schema validity and preserved/transformed rows. Configure the matching schema asset location for the installed Room plugin/helper version. Do not treat a fresh in-memory database as migration evidence or silently enable destructive fallback.

## DataStore and lifecycle

Create one DataStore per unique test file, owned by a cancellable scope. Cancel/join the owning scope before deleting/reopening the same file. Use unique temporary paths and close resources to avoid multiple active instances per file. Test updates, persistence after a controlled reopen, corruption/migration policy, and multi-process behavior only if supported and used.

For saved-state behavior, distinguish ViewModel initialization from real SavedStateRegistry save/restore. Activity recreation is useful but not a process-kill test. Use the appropriate Android owner/harness and describe the exact restoration boundary exercised.

## DI and workers

Verify required Koin definitions/qualifiers using the installed verification API, then exercise startup and important Android constructors under a realistic owner. Reset isolated/global container state between tests. A graph check cannot establish that every platform service is configured correctly.

Use WorkManager's test facilities to construct workers with the production factory, control constraints/delays, and inspect state/output. Test durable enqueue policy and idempotent reruns as well as `doWork` return values. See [background work](../android-background/SKILL.md) for lifecycle and retry rules.

## Run and report

Run affected host/device tasks with the actual variant, capture failures at the owning boundary, and repeat only after changes or new unresolved concerns. Release-specific DI/shrinking/network configuration needs an appropriate release check. Report fixture, device/API where applicable, scenarios, command results, and remaining live-service/platform limits. Do not equate simulated transport with production connectivity or a passing structural check with executable behavior.

Sources: [Room testing](https://developer.android.com/training/data-storage/room/testing-db), [migration testing](https://developer.android.com/training/data-storage/room/migrating-db-versions), [Ktor MockEngine](https://ktor.io/docs/client-testing.html).

## Negative security scenarios

When applicable, use controlled fixtures to test a wrong account/tenant ID, stale credential refresh after logout, unsafe URI/redirect, forbidden component entry, corrupted/restored storage and rejected TLS validation. Exercise release-effective network/manifest settings; mocks that always approve authentication cannot establish access control. Test backup/reopen failures without enabling destructive migration or plaintext credential fallback.

Keep fixtures independent of test order and ensure failures cannot reach a production endpoint. Check the configured base URL and account before executing writes, not merely whether the UI is running locally. Report which trust boundary the test truly crossed.

Prove that a negative fixture reaches its intended boundary. For authorization, use an existing resource that its owner can access, then a valid different identity; a missing resource or an earlier malformed-input rejection can leave authorization untested. For TLS, use a reachable controlled endpoint and the production trust configuration; a DNS failure or a MockEngine-thrown exception does not verify certificate rejection. Pair the denied case with legitimate behavior and inspect prohibited side effects, not only an error status.
