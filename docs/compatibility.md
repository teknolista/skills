# Agent and Model Compatibility

Official host documentation checked on 2026-10-25. These packages use the Agent Skills format: Markdown instructions, relative references/assets, and optional OpenAI UI metadata. Native format support, execution access, and measured task quality are separate claims.

## Native skill locations

Copy the complete skill directory, retaining its internal paths. Use the location supported by the actual host and execution environment; installing locally does not install into every cloud agent.

| Host | Documented project locations | Documented user locations | Official guidance |
| --- | --- | --- | --- |
| Codex | `.agents/skills/<name>/` | `~/.agents/skills/<name>/` | [Build skills](https://learn.chatgpt.com/docs/build-skills) |
| Claude Code | `.claude/skills/<name>/` | `~/.claude/skills/<name>/` | [Extend Claude with skills](https://code.claude.com/docs/en/skills) |
| Gemini CLI | `.gemini/skills/<name>/` or `.agents/skills/<name>/` | `~/.gemini/skills/<name>/` or `~/.agents/skills/<name>/` | [Agent skills](https://geminicli.com/docs/cli/skills/) |
| GitHub Copilot | `.github/skills/<name>/`, `.claude/skills/<name>/`, or `.agents/skills/<name>/` | `~/.copilot/skills/<name>/` or `~/.agents/skills/<name>/` | [Create agent skills](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-cloud-agent/add-skills) |
| Cursor | `.agents/skills/<name>/` or `.cursor/skills/<name>/` | `~/.agents/skills/<name>/` or `~/.cursor/skills/<name>/` | [Agent Skills](https://cursor.com/docs/skills) |

Invocation and consent differ by host. For example, Codex documents `$name`, Claude Code and Cursor support `/name`, and Gemini CLI exposes skill discovery/activation controls. Confirm discovery using the host's skill list or explicit invocation. Avoid installing duplicate copies with the same name just to cover several paths.

## Required capabilities

| Task | Necessary access | If unavailable |
| --- | --- | --- |
| PENTA-PRO creation/update | User intent, relevant existing context, package assets, and a writable requested destination | Ask only consequential missing questions; retain proposals and blockers. If writing is unavailable, return the draft and disclose that it was not saved. |
| PENTA-PRO review | The actual specification and relevant authoritative context | Report missing material rather than treating an absent document as ready. |
| Code inspection | Actual selected source/snapshot, relevant requirements/contracts, and applicable references | Report material missing coverage; do not infer a clean review from a description alone. |
| Executed verification | The project's actual tools and isolated data/environment | Label unexecuted checks and distinguish static conclusions from runtime evidence. |
| Independent review | A separate reviewer/session with actual source access | Disclose self-review or prepare a factual handoff; do not claim independence from a model label. |

Git, shell execution, browsers, Android SDKs, credentials, connectors, and additional agents are not supplied by installing a skill. Git is useful for comparisons, but an explicitly selected source snapshot can be reviewed without it. Neither package requires the other.

Some managed review services load only instruction text. Claude's [managed Code Review customization](https://code.claude.com/docs/en/code-review-customize) can include a skill body without its supporting files. This is a different integration from a local Claude Code session loading the complete directory. Supply the required guidance through the service's supported configuration, and qualify coverage when references or execution are unavailable.

## Model selection and validation

The workflows have no hard-coded model, reasoning setting, vendor tool name, or mandatory orchestration mechanism. `agents/openai.yaml` in these packages contains display metadata and a default prompt; it does not select a model. Hosts may offer their own model overrides. Use those controls deliberately rather than adding a vendor-specific override to the portable core.

Choose a currently available model with sufficient reasoning, domain competence, context capacity, and reliable tool use for the task. Escalate difficult requirements or review risks when evidence warrants it. The documented [OpenAI model options](https://learn.chatgpt.com/docs/models) include the repository's example implementation/review pairing; availability and suitability depend on the host/account and observed results. A model name is not a quality gate.

After changing host, model, or significant instructions, run the relevant [PENTA-PRO cases](../penta-pro/evals/scenarios.md) and [code-review cases](../code-review/evals/scenarios.md). Check correct activation, preserved user decisions, meaningful defects versus false positives, honest evidence/coverage, and unintended edits. Compare matched tasks before claiming better accuracy, cost, or latency. Official format support does not establish a cross-vendor performance benchmark.
