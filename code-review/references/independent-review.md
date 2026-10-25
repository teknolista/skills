# Independent and Multi-Model Review

## Establish independence

Use a reviewer that did not implement the change, with fresh task context. The implementer may prepare a factual packet, but its summary and test claims are inputs to verify. Give the reviewer access to the actual source and contracts, not just an explanation of why the author believes the patch is correct.

Use the available orchestration mechanism within its permission and cost limits. Do not create user-visible chats, send messages to other chats, or select a different model without the host's required user authorization. When no independent execution is available, prepare a portable handoff for a separate session. A self-review can proceed when allowed, but must be labeled and cannot silently satisfy a required independent-review gate.

If this session is already the independently assigned reviewer, perform the review directly. Do not recursively create reviewers. Multiple independent lenses are useful for high-risk or mixed-domain changes when justified and allowed; they are not a required ceremony for every patch.

## Handoff packet

Use the handoff template linked directly from `SKILL.md` as an output aid. Include:

- Exact target and source access: repository, base/head or local snapshot, relevant files, and exclusions. A SHA alone does not transfer uncommitted files.
- User outcome, scope, accepted constraints, requirement and invariant IDs, and authoritative contract locations.
- Relevant repository conventions, runtime/framework versions, platform support, and known operational context.
- Review-policy source/revision and execution capabilities, including whether linked references and local checks are available.
- Available verification evidence, labeled as executed, CI-reported, or an unverified author claim.
- Review focus, output format, independence requirement, allowed checks, time/cost limits, and escalation point.

Omit the implementer's internal reasoning and full conversation. Accepted design rationale and relevant decisions remain useful context. Avoid anchoring prompts such as asking the reviewer to confirm a suspected bug or reassuring it that another model already approved. For a re-review, previous findings are intentionally supplied so fixes can be verified; still inspect affected paths independently.

## Select a model deliberately

Keep model selection outside the portable skill. An example arrangement is `gpt-6.1-sol` implementing and `gpt-6-astra` reviewing, when both are available in the user's environment. Preserve an explicit model choice; do not silently substitute a model or claim that metadata switched it.

The arrangement is a practical candidate, not an established guarantee that one model is always the best reviewer. A fresh session of the same capable model can still be independent of the implementation session. Different models can diversify some failure modes while sharing others. Repository access, domain competence, a clear packet, and verification matter more than assigning authority based on a model name.

Distinguish a custom skill from a host's built-in review command. Codex documents `review_model` for built-in reviews and separate controls for detached review delivery. Those settings do not by themselves establish which model/context executes an ordinary `$code-review` skill request. Verify the actual reviewer session; see [Codex review documentation](https://learn.chatgpt.com/docs/code-review?surface=app). Changing host configuration requires the user's authorization.

For model/process changes, compare the same representative review cases and track validated defects found, false positives, material misses, review time, and cost. Escalate difficult authentication/data integrity, concurrency, platform, or architectural decisions to a suitably capable reviewer. Keep the lightest arrangement that meets the project's evidence and risk requirements. Do not claim measured superiority without such a comparison.

## Synthesize multiple reviewers

Give each specialist the relevant raw material and scope before exposing it to other reviewers' conclusions. Then a coordinator validates candidates against source and contract evidence, including test-gap claims. Majority agreement is not proof; minority findings are not discarded by vote.

Normalize locations, verify reachable triggers, reject refuted candidates, record unresolved material gaps, and deduplicate by root cause. Assign severity after contextual validation. If a review lens fails, show the missing coverage rather than treating an empty output as a pass. Report a clean review only for completed agreed coverage.

## Close the loop

The implementing agent evaluates each finding and either fixes it within authorization or explains a concrete refutation/accepted trade-off. Do not blindly implement reviewer suggestions. Clarify a blocking ambiguity while continuing unrelated authorized work when safe.

Re-review the resulting snapshot. Mark findings `Resolved`, `Still present`, `Refuted`, or `Accepted risk` with supporting evidence and the responsible decision-maker for accepted risk. Repeat affected checks and inspect for new defects introduced by the fix. Use a stated limit or escalate a persistent disagreement instead of looping indefinitely. A review verdict never substitutes for required CI, human approval, integration checks, or deployment authority.

Read relevant replies and previous automatic findings before closing the loop. Check each claim against the latest source; a dismissed thread is not proof that behavior changed. Update the existing finding's status when possible rather than reporting the same unresolved root cause as a new issue. Keep proposed comments as drafts until publication is authorized, and verify the current repository, revision, file, and lines before posting.
