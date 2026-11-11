## Why

Request IDs may collide across tenants. Sharing a receipt across tenants can suppress a job and expose another tenant's receipt.

## What Changes

- Scope request IDs to the authenticated tenant.
- Reject conflicting payloads for the same tenant and request ID.

## Capabilities

### New Capabilities

### Modified Capabilities

- `receipts`: Tenant-scoped retries and conflict handling.

## Impact

The in-memory receipt store and existing HTTP handler change. The handler signature and ordinary success response remain compatible.
