## MODIFIED Requirements

### Requirement: Receipt retries

For a valid authenticated request, the service SHALL scope a request ID to its authenticated tenant and return HTTP 202 with a receipt. A repeat with the same tenant, request ID and payload SHALL return the original receipt without a new job. Reusing the same tenant and request ID with a different payload SHALL return HTTP 409 with `{"error": "idempotency_conflict"}` without changing the receipt or creating a job. The handler signature and ordinary success response SHALL remain compatible. Missing identity SHALL return HTTP 401 and malformed input SHALL return HTTP 400, with no job created in either case.

#### Scenario: Independent tenants use the same ID

- **WHEN** two authenticated tenants submit valid requests with the same ID
- **THEN** each gets its own receipt and job

#### Scenario: Request ID is replayed

- **WHEN** a tenant repeats the same ID and payload
- **THEN** it receives its original receipt without creating another job

#### Scenario: Conflicting replay

- **WHEN** a tenant repeats the ID with a different payload
- **THEN** it receives the specified conflict response and the original receipt and job remain unchanged

#### Scenario: Rejected calls have no effect

- **WHEN** a request is unauthenticated or malformed
- **THEN** it returns the corresponding error and creates no job
