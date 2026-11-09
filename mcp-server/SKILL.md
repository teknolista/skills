---
name: mcp-server
description: Implement or change a Model Context Protocol server, its exposed capabilities, or its client-facing transport and authorization behavior. Use for concrete MCP server work. General HTTP implementation, requirements discovery, and independent security review have separate workflows.
license: MIT
metadata:
  version: "1.0.0"
---

# Implement an MCP server

1. Identify the client tasks, supported protocol revision, SDK version, client capabilities, transport, and deployment trust boundary. Verify SDK support and the matching [MCP specification](https://modelcontextprotocol.io/specification/) before selecting protocol details. Preserve existing compatibility. List what each caller is entitled to read or change and which downstream operation performs each effect.
2. Expose the smallest useful set of capabilities. Make names, descriptions, schemas, scope, limits, and result shapes precise enough for a client to select and call them. Distinguish protocol errors from operation failures using the selected revision. Return bounded results, actionable errors, and pagination when applicable. Keep credentials and internal traces out of results. Treat tool annotations and descriptions as client guidance.
3. Use SDK transport and request handling where supported. Keep stdio protocol output separate from diagnostics. For HTTP, apply the selected revision's transport and authorization requirements. Validate the caller and authorize the resource, action, and destination at the effect boundary. For remote or proxied servers, verify audience and token handling, origin/network controls, and redirect or outbound fetch constraints where applicable. Keep inbound credentials separate from downstream credentials. For local launch, scope process identity, filesystem and network access to the task.
4. Treat arguments and downstream content as untrusted. Reuse service-layer business rules. Bound expensive calls and retries. Define cancellation and repeat-call semantics for operations with side effects, including what happens when a client loses the response. Use actual application authorization or policy for sensitive effects. An annotation or client confirmation UI cannot enforce server permissions.
5. Test with a protocol client and an isolated downstream fixture. Exercise the selected lifecycle, discovery, normal invocation, schema failures, operation failures, and unsupported capabilities as relevant. Use a permitted control and an out-of-scope caller/resource, and inspect the downstream record for forbidden effects. Include lost response/retry, cancellation, or result truncation when the contract promises behavior there. For multiple supported client or transport combinations, record the tested matrix.

For a stateful HTTP server with authentication, validate credentials on every protected request, including stream resumption. Bind session state to the authenticated principal. Test replay of a valid session identifier by a different caller and without credentials. Verify rejection before any data or downstream effect. Follow the selected revision's transport rules for origin validation and local binding. [MCP transport](https://modelcontextprotocol.io/specification/2025-11-25/basic/transports) and [session security guidance](https://modelcontextprotocol.io/docs/2025-11-25/tutorials/security/security_best_practices) for revision 2025-11-25.

Execute only authorized operations in isolated fixtures. Inspect dependencies and local launch configuration before running an external server.

Return the exposed contract, compatibility and authorization decisions, verification by client/transport/revision, and remaining limitations. A successful call from one client establishes only the exercised path.
