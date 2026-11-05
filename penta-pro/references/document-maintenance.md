# Maintaining the Five-Pillar Specification

Use for creation, updates, resumption, or requested migration to the five-file layout. Paths below are relative to the project's root. Preserve explicitly requested locations and existing authoritative documents.

## Ownership and navigation

| File | Owns |
| --- | --- |
| `docs/product.md` | Product summary, glossary, objectives, requirements, and acceptance criteria. |
| `docs/project.md` | Architecture, contracts, dependencies, risks, assumptions, open questions, and decisions. |
| `docs/proof.md` | Check plans, requirement-to-evidence links, actual results, and outcome evaluation. |
| `docs/process.md` | Shared specification metadata, coverage, identifier conventions, revision history, resume state, tasks, gates, and authority. |
| `docs/production.md` | Environments, distribution, migrations, operations, support, and recovery. |

Keep sibling navigation in each file and link specific records using their stable IDs and valid anchors. Record a fact once and reference its owner. For example, a check in `proof.md` links its acceptance criterion in `product.md` and its contract in `project.md`. Define stable headings or explicit anchors where record-level navigation is needed. Existing external schemas or trackers can remain authoritative.

For a first specification using the default layout, create all five files with supported content and explicit gaps. Small projects can have short pillars. Keep the template index as authoring guidance in the skill package. Remove drafting links and placeholders from the generated project files. Before writing, inspect any existing files at the destinations and resolve ambiguous ownership.

## Coordinated updates and resumption

1. Read `process.md` for current scope, next action, shared status, and any unfinished update. Then inspect the affected pillars and their referenced records. For an existing single-file specification, read its equivalent resume section.
2. Identify the changed canonical records and downstream consequences. A requirement change may affect contracts, verification, tasks, and operating procedures. Update only files whose content or references need to change.
3. Before a material multi-file update, record `In progress` in PROCESS with affected IDs/files and remaining reconciliation. Save changes to the owning records, preserve unrelated edits, and reconcile their references. If concurrent edits are detected, inspect and combine them before writing.
4. Check target files and anchors, cross-file IDs, affected acceptance/check links, evidence applicability, and conflicting statuses. Preserve historical evidence and acceptance scope. Mark changed or unreviewed scope accurately.
5. After successful reconciliation, record the shared revision, change summary, and `Consistent` in PROCESS. Reassess readiness for the affected increment and save the next action. Consistency describes the documents and can coexist with pending questions or unverified software.

File writes may complete only partly. If interrupted, leave a durable record of which files were updated and what remains, and disclose partial saving. Resume by inspecting actual contents before completing the pending update. A partially reconciled set cannot be reported as fully updated or newly accepted. Preserve prior acceptance as history tied to its actual scope and revision.

## Baseline and proposed changes

For a material change to existing software, compare the request with accepted requirements, observed behavior, and related work already in progress. Record the baseline revision or state in PROCESS and link any conflict or overlap that could affect delivery. In PROJECT, summarize the intended additions, modifications, and retirements by canonical PRODUCT ID, with the reason, affected consumers or stored data, and compatibility commitments. Link changes to contracts, planned checks, tasks, and operating procedures in their owning pillars.

Keep a pending proposal separate from active requirements within the same files. Apply settled changes to the owning records, retaining stable IDs where identity remains the same and recording supersessions or retirements. Preserve previous acceptance and evidence with their original scope. If a compatibility commitment is still undecided, record who can resolve it and which work depends on it.

## Existing specifications and migration

An existing `docs/penta-pro.md` or another authoritative layout remains supported. An ordinary update preserves it. Migrate when the user requests the split or authorizes migration of that specification.

For migration, inventory sections, IDs, incoming links, decisions, evidence, and local customizations before moving content. Assign each record to its owning pillar, move shared state to PROCESS, and preserve all material content. Rewrite internal and discoverable incoming links and verify them from the new locations. Record uninspectable external references as migration limitations. Reconcile the five-file set before changing which location is authoritative.

Keep the old path as a short navigation page with forwarding anchors where existing links need them, unless its removal is authorized. It must point to the new canonical files and avoid retaining competing copies of requirements. The normal new-project output remains the five pillar files.
