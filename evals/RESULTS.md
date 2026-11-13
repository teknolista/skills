# Frontier model trial record

Each section describes the collection and tools used at the time. The [current verification](#collection-and-evaluator-verification-2026-11-13) includes executable controls and local discovery evidence.

The 2026-11-09 [trial procedure](../SKILL-EVALUATION.md) ran on Codex CLI `0.160.0` with low reasoning effort, the collection at `95abba607180cda548749edb76034efe5dbcac32` as baseline, and the working candidate. All 32 model sessions completed, 28 with GPT-6.1 Sol and four with GPT-6 Astra. Each session used a disposable synthetic repository and an identical starting fixture for its case. The no-collection arm retained the host's normal built-in capabilities. All routing runs used unhinted prompts. The MCP planning runs explicitly invoked the installed skill in the baseline and candidate arms.

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

## Adaptive workflow checks (2026-11-10)

Ran the [new workflow cases](../SKILL-EVALUATION.md#score-the-outputs) on Codex CLI `0.160.0`, GPT-6.1 Sol, low reasoning effort, and disposable fixtures. Compared baseline `a910ca37f86ef48b6cb0a09b9569933249534346` with the working PentaPRO 2.7.0 and Software Delivery 1.2.0 drafts. The two owner cases invoked their skills explicitly. The copy edit used normal discovery. The first launch could not initialize the local Codex state under the outer sandbox. The retry used the runner's workspace sandbox for the fixture agents.

| Case | Observed outcome |
| --- | --- |
| Entire scope before code | Both arms saved five linked drafts and left source and tests byte-identical. Both recorded the unresolved payload-conflict policy as blocking the selected scope and kept checks unverified. The baseline completed. The first candidate run reached the 160-second limit before its final response. A candidate rerun with a 240-second limit recovered from an unavailable `python` command and completed in 205 seconds. Its drafts and final response preserved the same boundary. |
| Conflict with accepted contract | Both arms cited the active tenant-scoped requirement and preserved all files. A candidate rerun after clarifying accepted versus proposed records also preserved all files and demonstrated the existing contract drift with local probes. |
| Localized copy edit | The candidate changed only the misspelled heading bytes and did not read a collection skill. |

These are narrow behavioral checks. They support the observed boundaries but do not establish an improvement over the baseline. The follow-up runs used different time limits and are not a latency comparison. The runner did not establish read isolation from sibling runs or evaluator material. Prototype adoption and generated-source workflows have manual cases and were not executed.

## Anthropic adoption pilot preparation

On 2026-11-11, verified the working candidate over `9405717` with synthetic fixtures and no live product deployment.

- **Real OpenSpec fixture.** OpenSpec 1.16.0 strictly validated both the published capability and the active `tenant-receipts` change. Artifact status was complete while apply reported zero of two tasks complete. The first delta draft omitted the baseline replay scenario and failed strict validation. Preserving that scenario fixed validation. The offline test reproduces this negative control.
- **Independent forward test.** A fresh agent received the Software Delivery package and the disposable fixture task. It reproduced cross-tenant receipt reuse and the incorrect conflict response before the fix. It implemented the change in two increments, observed task progress at 0/2, 1/2 and 2/2, passed four fixture tests, and left the change active. Only the handler, tests and task list changed. An external check passed all three acceptance tests on that output. The example now offers the handoff as the evidence location when the project has no verification record. The trial was scoped by task instructions in a shared environment. The exercised boundary was a sequential in-memory handler.
- **Grader controls.** The external checker rejects the two seeded receipt defects and passes the rejected-call control on the original implementation. It passes all three checks on the clean fixture. These results establish grader sensitivity for the exercised behaviors.
- **Mount and tool boundary.** The Linux Bubblewrap probe denied reads and writes to the actual grader and a sibling sentinel while permitting private scratch writes. A loopback Responses API double received an isolated Codex CLI 0.160.0 request without an authorization header. A synthetic tool call ran the mounted OpenSpec executable and returned version 1.16.0. The CLI used fallback model metadata for the mock model ID. The run exercised transport and tool execution with scripted responses, independent of inference quality. Network namespace and egress policy remain separate.
- **Operations forward tests.** A fresh task using Production Operations identified the staging/runner destination mismatch, held mutations and planned an old-writer-compatible migration. In the stale-green fixture it identified the applied candidate, the old revision serving all normal traffic, and the failed tagged write with unknown job effect. It held promotion and preserved traffic in its recommendation. Both were offline and read-only.
- **Adoption checks.** Skills CLI 1.7.6 installed all 22 packages from a disposable local copy into a fresh Codex project. The 144 installed files matched source bytes. See the [collection review](../FINAL-SKILL-REVIEW.md#pilot-readiness-review) for the audit and offline suite.

The above checks support starting a pilot. Matched real-model comparisons via a configured gateway, cross-host activation measurements, and live application or deployment checks remain unexecuted for this snapshot.

## Collection and evaluator verification (2026-11-13)

The starting baseline was `25007537cc58122a8200d1bed63245586f49c82b`. Its collection validator and 87 offline tests passed. The maintenance pass compared claims from the supplied review with the code, fixtures and primary documentation before changing procedures.

- **OpenSpec consolidation.** The original active receipt delta passed strict validation. In a disposable copy, simulated task completion let archive apply the delta, but strict validation of the consolidated capability then reported a requirement above the prose length limit. The corrected delta preserves HTTP statuses, replay, tenant isolation and no-write checks. Both OpenSpec 1.16.0 and 2.0.0 validated the active artifacts, archived the change, preserved all four scenarios, and passed strict validation of the consolidated capability. The unfinished-task and missing-scenario controls remain executable. Archive in this test exercises artifacts only.
- **Execution boundary.** The Linux mount probe denied grader and sibling-file access and allowed scratch writes. The offline grading probe also denied writes to the candidate mount and attempts to open IPv4, IPv6 and Unix sockets. The process exercising a submitted fixture uses synthetic inputs. The evaluator checks observations externally, and arbitrary code inside a worker can still fabricate its own observations. The inference environment has separate network policy requirements.
- **Controls and cases.** The receipt checker uses reproducible, varying caller, request and payload values and compares responses with job state. The clean handler passes all 12 scenarios. The seeded handler fails six scenarios across tenant isolation and conflicting replay while the remaining controls pass. The case manifest adds a test-authoring task that distinguishes a `403` with an unauthorized queued effect and a research task that checks the pinned version against newer evidence and an untrusted instruction. See the [scoring procedure](../SKILL-EVALUATION.md#score-the-outputs).
- **Discovery.** Skills CLI 1.7.6 installed all 22 packages from a disposable local copy and independently installed Android Data Layer. All 148 exported package files matched the full installation byte-for-byte. Codex CLI 0.160.0 exposed 22 enabled project packages through `skills/list`.
- **MCP SDK.** A fresh Python environment with MCP SDK 2.2.0 passed the in-process smoke fixture for legacy sessions, modern direct calls, SDK discovery, replay after response loss, principal-scoped handles, and protocol version/header errors. The fixture uses synthetic identities and in-memory effects. It leaves live authorization, persistent recovery and deployed clients to target-specific checks.

### Matched GPT-6.1 Sol pilot

The initial managed-environment preflight could not write Codex application state. The authenticated CLI subsequently ran the authorized synthetic trials from disposable Git checkouts with workspace-write sandboxing. Evaluator code execution used the separate offline Bubblewrap boundary. The agent sessions used the normal local mode, so agent read isolation and network isolation were not established. The trials used Codex CLI 0.160.0, GPT-6.1 Sol at low reasoning effort, unhinted prompts, the starting commit above for the baseline, and the revised packages for the candidate. There was one attempt per arm per case, with the same fixture, prompt and evaluator seed across arms. The two batches had different concurrency and time limits. These comparisons are exploratory.

All 30 sessions completed across 10 cases and three arms. Read-only assessment cases used manual review of the answers, artifacts and relevant traces after the automated scope checks.

| Cases | Observed results across the three arms |
| --- | --- |
| Local copy edit | Only the typo changed in all three attempts. No collection skill read was observed. |
| Behavior test authoring | All three tests detected the denied queue write while the handler still returned 403. Each passed on the clean control, failed on the seeded implementation, and preserved product code. |
| Delivery without SDD, with native SDD, and with OpenSpec 2.0.0 | All nine handlers passed the independent 12-scenario checker. All nine authored test suites detected both seeded faults and passed on their delivered code in offline rechecks. The three OpenSpec runs verified the handler and kept the accepted change active. The candidate added evidence to `tasks.md`. The initial grader rejected the extra prose, although all original task descriptions and completions were preserved. The corrected grader accepts evidence alongside those tasks and still detects an altered or incomplete item. Regrading the saved output passed its objective checks. |
| Review on clean and seeded fixtures | All six reviews preserved the workspace. The three seeded reviews reproduced both contract violations despite the misleading support trace. The clean reviews identified verification gaps without inventing a behavior defect. |
| Diagnosis | All three reproduced the lookup collision and explained why a tenant's job was missing. Both installed arms also reported a different-ID working control in their answers. |
| Pinned-version research and stale green deployment | All three research runs rejected reliance on the unsupported pinned capability and ignored the untrusted instruction. All three operations runs held promotion and preserved traffic based on the failed tagged write and unknown job effect. |

Command traces showed the intended owners in the installed arms for the review, test-authoring, diagnosis, research and operations cases. Both installed arms read HTTP API for direct delivery. In one native SDD run the candidate also read Software Delivery, and in the OpenSpec run it read HTTP API alongside the coordinating owner. This extra context is a cost signal to track. Median cumulative input tokens across the ten cases were 61,914 without the collection, 79,702 for the baseline and 83,153 for the candidate, rounded to whole tokens and including cached input. These counts do not measure billing. One attempt per case, concurrent jobs and a fixture set largely passed without the collection leave general performance differences unresolved. The observed results support the targeted correctness fixes and a further project pilot on work where the additional procedures matter.
