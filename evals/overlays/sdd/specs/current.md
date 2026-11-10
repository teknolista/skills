# Current receipt handler baseline

`RCPT-1` currently allocates request IDs from one global namespace. A repeat of a known ID returns its existing receipt. The active tenant-receipts change replaces this requirement when implemented and verified.
