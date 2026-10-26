# Web, API, and Service Security

Select the changed/exposed surfaces and actual stack. ASVS requirements, API risk lists, and WSTG tests have different purposes; select applicable editions/IDs rather than claiming blanket compliance.

## Identity, business rules, and data

- Trace authentication, token/session validation, expiry, revocation, account recovery, privileged MFA, and identity changes through the actual entry points. A signed token or authenticated actor does not establish resource authorization.
- Enforce remote operations at a trusted server/service boundary. Follow object, property, function, and tenant authorization across reads, writes, bulk actions, exports, background jobs, alternate routes, and caches. Follow effective guards before reporting a missing check.
- Model abuse of legitimate features: invitation/recovery takeover, payment/refund transitions, coupon/credit replay, workflow bypass, account enumeration, sensitive search, and automated consumption. Verify the project's business invariant and realistic attacker prerequisites.
- Check transaction/race windows, idempotency, ordering, and uncertain external outcomes. Authenticate webhook source/payload and constrain replays; IP allowlists or an obscure callback URL alone are not authenticity checks.
- Trace sensitive fields into responses, logs, analytics, URLs, browser storage, shared caches, backups, and downstream APIs. Inspect schema/migration compatibility and data lifecycle controls, including delayed clients.

## Untrusted inputs and browser boundaries

- Follow input into SQL/NoSQL, command arguments, filesystem/archive paths, templates, deserialization, uploads, and URL fetches. Check actual parameterization/encoding/containment; validation at an unrelated layer may not protect the sink.
- For SSRF, assess allowed destinations, DNS resolution/rebinding, redirects, private/link-local/metadata targets, protocol support, and egress policy appropriate to the fetcher. Do not require a denylist when a sound allowlist or constrained service enforces the contract.
- For XSS and client/server rendering, examine context-sensitive output handling, raw HTML/Markdown, URLs, sanitization, hydration, and private values reaching public bundles or caches. CSP is one layer, not a substitute for safe rendering.
- Match cookies, CSRF defenses, CORS, same-origin isolation, postMessage origin checks, OAuth redirects, and session storage to the credential mechanism and supported browser behavior. Do not demand cookie-specific controls for every API.
- Check resource limits and abuse controls for expensive parsing, searches, uploads, decompression, authentication, and automation. Rate limits should reflect the identity/boundary and workload, not an invented universal number.

## Evidence

High-value checks include two identities accessing the same resource, allowed versus denied properties/actions, replayed/reordered requests, malicious content at the final rendering sink, cross-account cache reuse, and recovery after partial effects. Use isolated fixtures or established local services. Record which browser/API/runtime boundaries were actually exercised; a build or scanner alone does not establish end-to-end security.

Primary guidance: [ASVS](https://asvs.owasp.org/), [API Security](https://api-security.owasp.org/), [WSTG](https://owasp.org/projects/web-security-testing-guide).
