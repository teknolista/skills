# Vector Relay upstream release notes

## 2.4.1 · Pinned release

Retries are deduplicated by request ID in a single process. The key is shared across tenants. Restart loses the in-memory record.

## 2.6.0 · Later release

Adds optional tenant-scoped deduplication when a trusted tenant identity is configured. Storage and restart guarantees depend on the selected adapter. Upgrade instructions require verifying existing key compatibility before migration.
