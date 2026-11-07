---
name: android-error-handling
description: Implement or debug typed results and expected domain, HTTP and storage error mapping in native Android Kotlin code. Use for concrete error-handling changes; use peer-review for read-only assessment and ui-design for user-facing error interaction design.
metadata:
  version: "1.2.3"
---

# Android Error Handling

## Start with the target project

1. Identify the owning module, active variant, observable contract, and requested change. Reuse its stack and types. Adapt examples only after checking the resolved APIs and existing call sites. If a linked companion is unavailable, use the project contract.
2. Before executing a build or test, inspect the chosen task and hooks for network calls, credentials, publishing, or shared writes. Use isolated fixtures by default for checks with external effects. Confirm the authorized target before any shared-system check.
3. Run the smallest relevant check that exercises the changed boundary. Record the snapshot, variant, command, result, and any untested device or service behavior. A successful implementation check is separate from review and release acceptance.

Use native Android/JVM APIs and the project's selected library versions. Domain error types remain plain Kotlin. Expected failures have typed outcomes; programming defects should remain visible. Preserve coroutine cancellation. See [data ownership](../android-data-layer/SKILL.md) and [UI error rendering](../ui-design/references/android/presentation-mvi.md).

## Typed outcomes in the domain module

Use one consistent result abstraction; do not accidentally mix it with `kotlin.Result`. `AppError` avoids the name collision between the error bound and the nested `Result.Error` class.

```kotlin
interface AppError

sealed interface Result<out D, out E : AppError> {
    data class Success<out D>(val data: D) : Result<D, Nothing>
    data class Error<out E : AppError>(val error: E) : Result<Nothing, E>
}

typealias EmptyResult<E> = Result<Unit, E>

inline fun <T, E : AppError, R> Result<T, E>.map(transform: (T) -> R): Result<R, E> =
    when (this) {
        is Result.Success -> Result.Success(transform(data))
        is Result.Error -> this
    }

inline fun <T, E : AppError> Result<T, E>.onSuccess(action: (T) -> Unit): Result<T, E> =
    apply { if (this is Result.Success) action(data) }

inline fun <T, E : AppError> Result<T, E>.onFailure(action: (E) -> Unit): Result<T, E> =
    apply { if (this is Result.Error) action(error) }

fun <T, E : AppError> Result<T, E>.asEmptyResult(): EmptyResult<E> = map { }

sealed interface DataError : AppError {
    enum class Network : DataError {
        BAD_REQUEST, UNAUTHORIZED, FORBIDDEN, NOT_FOUND, REQUEST_TIMEOUT,
        CONFLICT, PAYLOAD_TOO_LARGE, TOO_MANY_REQUESTS, SERVER_ERROR,
        SERVICE_UNAVAILABLE, NAME_RESOLUTION_FAILED, CONNECTION_FAILED, TLS_FAILURE,
        SERIALIZATION, UNKNOWN
    }
    enum class Local : DataError { DISK_FULL, NOT_FOUND, UNKNOWN }
}
```

Define feature errors beside the owning domain contract, for example `enum class EmailError : AppError { INVALID }`. Choose fail-fast or accumulated validation errors according to the form contract; a single `Result.Error` may contain a structured collection when users need all field errors together.

`onSuccess` and `onFailure` observe an outcome and return the **original result**. They do not recover from errors, replace values, or propagate the result of another operation. Use explicit branching or a deliberately implemented `flatMap`/recovery operation for those behaviors.

## HTTP boundary in the data module

Configure Ktor with `expectSuccess = false` when handling status codes yourself. Do not combine this policy with a validator that throws on the same statuses without adapting the handler. Place both request execution and body decoding inside the protected boundary.

```kotlin
import io.ktor.client.call.NoTransformationFoundException
import io.ktor.client.call.body
import io.ktor.client.network.sockets.ConnectTimeoutException
import io.ktor.client.plugins.HttpRequestTimeoutException
import io.ktor.client.statement.HttpResponse
import io.ktor.serialization.ContentConvertException
import kotlinx.coroutines.CancellationException
import kotlinx.serialization.SerializationException
import java.io.IOException
import java.net.ConnectException
import java.net.SocketTimeoutException
import java.net.UnknownHostException
import java.nio.channels.UnresolvedAddressException
import javax.net.ssl.SSLException

suspend inline fun <reified T : Any> safeCall(
    execute: () -> HttpResponse
): Result<T, DataError.Network> = try {
    responseToResult<T>(execute())
} catch (e: CancellationException) {
    throw e
} catch (e: UnknownHostException) {
    Result.Error(DataError.Network.NAME_RESOLUTION_FAILED)
} catch (e: UnresolvedAddressException) {
    Result.Error(DataError.Network.NAME_RESOLUTION_FAILED)
} catch (e: HttpRequestTimeoutException) {
    Result.Error(DataError.Network.REQUEST_TIMEOUT)
} catch (e: ConnectTimeoutException) {
    Result.Error(DataError.Network.REQUEST_TIMEOUT)
} catch (e: SocketTimeoutException) {
    Result.Error(DataError.Network.REQUEST_TIMEOUT)
} catch (e: ConnectException) {
    Result.Error(DataError.Network.CONNECTION_FAILED)
} catch (e: SerializationException) {
    Result.Error(DataError.Network.SERIALIZATION)
} catch (e: ContentConvertException) {
    Result.Error(DataError.Network.SERIALIZATION)
} catch (e: NoTransformationFoundException) {
    Result.Error(DataError.Network.SERIALIZATION)
} catch (e: SSLException) {
    Result.Error(DataError.Network.TLS_FAILURE)
} catch (e: IOException) {
    Result.Error(DataError.Network.CONNECTION_FAILED)
}

suspend inline fun <reified T : Any> responseToResult(
    response: HttpResponse
): Result<T, DataError.Network> = when (response.status.value) {
    in 200..299 -> {
        if (T::class == Unit::class) {
            @Suppress("UNCHECKED_CAST")
            Result.Success(Unit as T)
        } else {
            Result.Success(response.body<T>())
        }
    }
    400 -> Result.Error(DataError.Network.BAD_REQUEST)
    401 -> Result.Error(DataError.Network.UNAUTHORIZED)
    403 -> Result.Error(DataError.Network.FORBIDDEN)
    404 -> Result.Error(DataError.Network.NOT_FOUND)
    408 -> Result.Error(DataError.Network.REQUEST_TIMEOUT)
    409 -> Result.Error(DataError.Network.CONFLICT)
    413 -> Result.Error(DataError.Network.PAYLOAD_TOO_LARGE)
    429 -> Result.Error(DataError.Network.TOO_MANY_REQUESTS)
    503 -> Result.Error(DataError.Network.SERVICE_UNAVAILABLE)
    in 500..599 -> Result.Error(DataError.Network.SERVER_ERROR)
    else -> Result.Error(DataError.Network.UNKNOWN)
}
```

This is an Android Ktor/OkHttp example, not a promise that all engines and versions expose identical exception classes. Confirm the installed API when adapting imports. Handle additional **known** transport exceptions at this boundary; avoid a catch-all that turns programmer errors into successful control flow. DNS failure does not prove that the entire device is offline; use an appropriately worded message. Do not expose raw exceptions, backend bodies, stack traces, or credentials to users.

Use standard Ktor request functions rather than overloads named `get`/`post` that can resolve ambiguously. Configure a trusted HTTPS base URL once with Ktor's URL builder; define whether routes are relative to its path prefix. Avoid string concatenation and `contains(BASE_URL)` checks. Test leading/trailing slashes, path parameters, queries, and any permitted absolute URLs. Apply the approved origin and credential policy to the final request and each redirect hop. In a controlled fixture, inspect destination and headers after a cross-origin redirect. Reject an invalid TLS certificate without weakening trust checks.

```kotlin
import io.ktor.client.request.get

// A data-source method; client is injected and base URL configuration is shared.
suspend fun loadNotes(client: io.ktor.client.HttpClient): Result<List<NoteDto>, DataError.Network> =
    safeCall { client.get("notes") }
// Import io.ktor.client.request.get. NoteDto is the feature's @Serializable DTO.
```

For a bodyless endpoint request `safeCall<Unit> { ... }`; do not attempt to decode an empty body as a DTO. For authenticated calls, distinguish an expired session from connectivity failure and stop refresh loops after a rejected refresh.

## Storage and UI mapping

Catch storage-specific exceptions in the data layer, rethrow cancellation, and map the actual driver's known failures. `android.database.sqlite.SQLiteFullException` applies to the Android framework driver; a different SQLite driver can expose different exceptions. Do not classify every database failure as disk-full, nor catch arbitrary defects as storage errors.

Map each user-visible domain error to localized text in its presentation owner. Reuse existing conventions such as `R.string.*`, `UiText` or a shared presentation module when present. Internal retry signals need no user-facing string. Keep logs useful and redacted; do not use unconditional `printStackTrace()` as production logging.

## Verify

Exercise status mapping, DNS/connection/timeout failures, malformed success JSON, bodyless success, cancellation, rejected refresh, and unknown statuses. Assert the observable result; ensure cancellation is thrown rather than wrapped. See [integration testing](../android-integration-testing/SKILL.md).

Sources: [Ktor response validation](https://ktor.io/docs/client-response-validation.html), [Android coroutine practices](https://developer.android.com/kotlin/coroutines/coroutines-best-practices).

A bodyless success needs its own supported response contract. An HTTP 202 response acknowledges acceptance for processing. Verify the final operation state through the documented completion path before showing a completed result.

## Failure classification and retry contract

TLS trust/hostname failures are security/configuration failures, not evidence that the device is offline. Do not bypass trust checks or retry them indefinitely. Keep retry policy with the operation. If it honors Retry-After on 429 or 503, preserve the needed response metadata before mapping to an enum, bound the delay, and handle absent or invalid values. Check for retries in every layer so a worker, repository, and HTTP client do not multiply each other’s attempts. A POST timeout can have an unknown server outcome: use a supported status/idempotency contract before resubmitting. Do not parse arbitrary server text into actionable HTML or display it as a trusted localized error.

The sample helper models small buffered responses; streaming responses need lifetime/cleanup and cancellation handling appropriate to their body channel. Do not return a Response stream after closing its client/request scope. Preserve original cancellation rather than converting it into UNKNOWN.
