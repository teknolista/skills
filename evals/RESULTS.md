# Frontier-model trial record, 2026-11-09

The [trial procedure](../SKILL-EVALUATION.md) ran on Codex CLI `0.160.0` with low reasoning effort, the collection at `95abba607180cda548749edb76034efe5dbcac32` as baseline, and the working candidate. All 32 model sessions completed, 28 with GPT-6.1 Sol and four with GPT-6 Astra. Each session used a disposable synthetic repository and an identical starting fixture for its case. The no-collection arm retained the host's normal built-in capabilities. All routing runs used unhinted prompts. The MCP planning runs explicitly invoked the installed skill in the baseline and candidate arms.

## Localized HTTP change

| Model and workflow | Baseline skill reads | Candidate skill reads | Baseline input tokens | Candidate input tokens |
| --- | --- | --- | ---: | ---: |
| Sol, accepted SDD change | 3, 3, 3 | 2, 1, 1 | 113,689 | 70,633 |
| Sol, existing contract without SDD | 3, 2, 3 | 1, 1, 1 | 97,797 | 70,747 |
| Astra, accepted SDD change | 3 | 1 | 99,670 | 72,530 |

Sol token counts are medians of three attempts per installed arm. Astra counts are from one attempt per arm. Counts are cumulative input tokens reported by the CLI, including cached input. Skill reads were observed in command traces. Neither count measures billing. Sol wall times were mixed, with a median of 45.82 versus 44.18 seconds with SDD and 44.00 versus 45.97 seconds without SDD. The two Sol runs without the collection took 64,894 and 62,208 input tokens and also satisfied the fixture.

All 16 implementation outputs passed three independent acceptance tests. Their generated regressions failed on both seeded defects when rerun against the original handler and passed on the resulting implementation. Each output changed only `receipts.py` and `test_receipts.py`. The SDD change and prior baseline remained intact. The fixture exercised sequential in-memory effects.

Keep the narrower Software Delivery and Behavior Testing triggers. HTTP API covered the localized change and its tests in every candidate run. The candidate sometimes still loaded Software Delivery in the SDD case. This comparison measures a combined change to the routing descriptions and HTTP contract guidance. It does not isolate the effect of each line.

## Scope and planning controls

- **Read-only review.** All three Sol arms independently reproduced both seeded contract violations and preserved the workspace after reading the misleading support trace. The installed Peer Review runs additionally recorded their reviewed snapshot and evidence limits.
- **Android plan and copy edit.** Both installed Sol arms selected Android integration testing for the Room migration and kept execution pending because the fixture lacks a build and SDK. All three copy-edit arms changed only the typo bytes. No collection skill read was observed for that edit.
- **Diagnosis.** Both Sol versions reproduced the lookup collision with a discriminating control and preserved source. The proposed prompt wording about treating the reported cause as a hypothesis produced no observed advantage in this case. Keep the existing Diagnose Defect instructions and retain the regression case.
- **MCP.** The baseline Sol and Astra plans preserved legacy behavior and identified sound application retry and authorization checks, but left the modern lifecycle unresolved in the offline fixture. The candidate plans used the local revision reference to distinguish legacy initialization from a valid modern direct call, include `server/discover` and version/header errors, and retain the SDK compatibility gate. The Astra run used the final reference including the cache-scope guidance. The Sol run used the preceding reference without that additional cache paragraph. These planning trials exercised no deployed server.

## MCP SDK smoke test

The [MCP fixture](check_mcp_sdk.py) passed with the official Python SDK `2.2.0`. One in-process Streamable HTTP endpoint served the legacy initialization, session and tool list, a modern direct call, and discovery by the official modern SDK client. A client-side failure discarded the response after the fixture wrote. Retrying with a new protocol ID and the same application key returned the original receipt, including through the legacy path. A second synthetic principal could create an independent receipt but could not read the first principal's handle. Header mismatch and unsupported version returned their expected errors without new effects. Tool listing exposed the modern cache fields. The test covers synthetic caller isolation and an in-memory effect. OAuth, persistent recovery, SSE and production clients require their own integration checks. [SDK release](https://pypi.org/project/mcp/2.2.0/) · [Protocol changes](https://modelcontextprotocol.io/specification/2026-07-28/changelog)

## Structural checks

Local validation passed all 21 packages, the helper suites (24 UI and 12 PR publisher Python tests), and 25 offline grader scenarios. A positive control and seven targeted invalid frontmatter variants exercised the new validator. The validation workflow was parsed locally. GitHub-hosted execution and project-specific Android, security, and deployment checks remain outside this record.

## Final-review qualification (2026-11-09)

The trials above kept evaluator checks outside task workspaces, but did not establish that the host denied reads of those files or sibling runs. Treat them as exploratory local comparisons, not blinded or adversarially isolated evaluations. The later runner timeout correction is covered by offline process-lifetime tests; it does not retroactively change these recorded runs or their measured outcomes.
