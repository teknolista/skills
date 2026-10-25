# Independent Code Review Handoff

Use this packet to request a fresh review. Replace placeholders; do not send the implementer's full conversation or hidden reasoning.

- **Goal:** [User outcome and intended behavior]
- **Review target:** [PR / exact base and head / local snapshot / explicit file set]
- **Source access:** [Repository or workspace and how the reviewer obtains the actual content, including uncommitted files]
- **Scope and exclusions:** [Included work and limits]
- **Requirements and invariants:** [Authoritative text or accessible paths/IDs; note any missing specification]
- **Accepted design and constraints:** [Relevant decisions, platform versions, compatibility, and operational needs]
- **Repository guidance:** [Applicable conventions and actual validation commands]
- **Review policy and depth:** [Trusted policy source/revision, scoped rules, and agreed depth]
- **Verification evidence:** [Checks, artifact/revision, results, and whether independently observed or author-reported]
- **Review focus:** [Backend / frontend / Android / mixed surfaces and specific risk areas]
- **Execution boundaries:** [Accessible references, inspection-only or executable checks, disposable environments, time/cost limits, and restricted side effects]
- **Reviewer/model:** [Explicit selection if provided; confirm availability through the host]
- **Previous findings:** [Only for a re-review, including disputed claims and evidence]
- **Output:** [Requested report contract or the bundled report template]

Review independently using the actual source, caller/consumer context, requirements, and tests. Stay within the agreed target. Validate reachable triggers and consequences, separate defects from questions, and report verification limitations. Do not edit the reviewed source or post a remote review unless separately authorized. If you already are the assigned reviewer, review directly rather than delegating again. Return a clear verdict and coverage statement; an empty finding list is valid when supported by completed review.
