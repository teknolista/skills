# AI and Agentic System Security

Use only when models, retrieval, agents, or generated outputs participate in the assessed system. Map the real principal, data access, and capability behind each model/tool action.

- Treat user uploads, retrieved pages/documents, tool responses, and model outputs crossing trust boundaries as untrusted content. Keep trusted task/policy instructions separate; a document cannot grant itself higher authority by claiming to be a system message.
- Check prompt injection and indirect instructions against consequences: data disclosure, tool misuse, policy bypass, unsafe execution, poisoned memory, and unauthorized external actions. Prompt wording and filters alone cannot enforce application authorization.
- Enforce identity, tenant/resource access, allowed operations/arguments, destinations, and approvals in trusted code. Bind approval to the exact sensitive action and current parameters; model confidence or a previous broad approval must not silently widen it.
- Inspect retrieval indexing/query filters, embeddings/document access, shared caches, conversation state, and persistent memory across users/tenants. Retrieved data and remembered instructions must not bypass the original user's access rights.
- Constrain code execution, filesystem/network access, credentials, tool chaining, callbacks, and third-party agent/service connections. A sandbox needs verified boundaries; an agent message does not itself authorize another agent's actions.
- Validate model output before rendering HTML/Markdown, executing commands/code, querying data, or changing configuration. Trace the actual sink and side effects rather than reporting the presence of a model as a vulnerability.
- Review provenance, model/provider updates, sensitive telemetry/training destinations, retention, and permission for external transmission. Avoid leaking real data in security evaluation prompts or logs.
- Bound cost, steps, concurrent work, retries, and externally visible effects. Test cancellation, replay, partial failure, and human escalation without executing unauthorized real-world actions.

Use synthetic adversarial documents and safe mock tools to test denied actions and data isolation. A successful refusal on one prompt does not establish resistance to all prompt injection; record the tested boundaries and residual exposure.

Primary guidance: [OWASP AI Agent Security](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html), [OWASP prompt injection prevention](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html).
