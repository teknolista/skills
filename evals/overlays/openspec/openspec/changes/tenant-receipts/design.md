## Context

The test fixture invokes the existing handler directly and stores receipts and jobs in memory. The caller identity is already supplied by the handler's principal argument.

## Decisions

Scope the lookup by the authenticated tenant and request ID. Retain the payload and receipt to distinguish exact retries from conflicts. Preserve existing input and identity rejection behavior. Verify job effects as well as responses.

## Risks / Trade-offs

The fixture exercises sequential calls only. A persistent or concurrent deployment would need transaction and failure-path checks at its storage boundary.
