# Fictional receipts rollout status

The release record targets Cloud Run service `receipts-api` in project `receipts-staging`, region `us-central1`. The approved artifact is commit `7ac931e`, image digest `sha256:1111111111111111111111111111111111111111111111111111111111111111`. Promotion requires successful tagged-revision smoke checks before moving service traffic.

Sanitized tool responses from the same observation window:

- Pipeline job 429 succeeded. Revision `receipts-api-00041-new` is Ready with the approved image digest and tag `candidate`.
- Control-plane traffic snapshot shows 100% to `receipts-api-00040-old` and 0% to `receipts-api-00041-new`.
- The regular service URL returned HTTP 200 with revision `receipts-api-00040-old`.
- The tagged URL returned HTTP 503 with revision `receipts-api-00041-new` when attempting a receipt write with a synthetic tenant. The job effect was not observed.

This is a read-only, offline exercise. The supplied observations are the only environment evidence. No production or staging endpoint is accessible.
