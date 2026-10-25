# Brainstorming Research Notes

Maintainer provenance for version 1.2.0, inspected on 2026-10-25. These notes are not routine interview context. Upstream instructions were analyzed as source material, not executed as project authority. The synthesis uses original wording and bundles no upstream scripts or templates.

## Sources used

| Source and inspected revision | Material inspected | Contribution adapted to PENTA-PRO |
| --- | --- | --- |
| [obra/superpowers](https://github.com/obra/superpowers/tree/2ce8aa15d05bd57213e6f746f953aafb7ded7a8b/skills/brainstorming) | `brainstorming/SKILL.md` and its builder-check prompt | Discover the purpose behind a feature, reflect intent, explore meaningful alternatives, and check whether an implementer needs consequential missing information. |
| [mattpocock/skills](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/engineering/grill-with-docs/SKILL.md) | `grill-with-docs`, `grill-me`, and the [grilling primitive](https://github.com/mattpocock/skills/blob/5beb35b040e3de97e54fa9e386d7e42d15c295c2/skills/productivity/grilling/SKILL.md) they invoke | Ask questions only when their prerequisites are settled; distinguish facts the agent can inspect from decisions requiring the user. The interview primitive sits outside the supplied engineering folder but is an explicit dependency of its interview wrapper. |
| [addyosmani/agent-skills: interview-me](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/interview-me/SKILL.md) | Intent-discovery workflow | Distinguish the desired outcome from a conventional feature request, probe vague quality claims, and consolidate an interpretation the user can correct. |
| [addyosmani/agent-skills: idea-refine](https://github.com/addyosmani/agent-skills/blob/aeac41d4d005999432bb7312f7ff06383a91d59d/skills/idea-refine/SKILL.md) | Divergent/convergent ideation workflow | Compare viable directions, expose consequential assumptions, simplify the first increment, and preserve explicit exclusions. |
| [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD/tree/61e01f82644c4bb533750cfa0d6d61ab61d2cc9b/skills/bmad-brainstorming) | `bmad-brainstorming/SKILL.md`, convergence, in-chat technique selection, and creative-partner references | Separate exploration from selection, change the thinking lens when stuck, and preserve who supplied an idea or decision. |

## Scope exclusions

- [owainlewis/blueprint](https://github.com/owainlewis/blueprint/tree/74210b5f4f07e6a213d2d3950603f55a868c9f4a/skills): the inspected skill inventory has no dedicated brainstorming skill. `requirements` was inspected to classify its scope; requirements, architecture, and planning workflows were not imported into this brainstorming-only synthesis.
- [awesome-skills/code-review-skill](https://github.com/awesome-skills/code-review-skill/tree/4850184dfd7765ea7b3c5c4e9b6cf8e0815ee7cb): the inspected inventory contains a code-review skill, with no brainstorming skill identified.
- [The supplied PERFECT gist](https://gist.github.com/keskinonur/36e0dd44f8cc7f6e507055e94a70618b): its published skill is a code-review workflow, outside this update's scope.

## Deliberate adaptations

Keep questioning proportional to the next increment, with no exhaustive design-tree requirement, idea quota, subjective confidence percentage, or mandatory questionnaire format. Existing PENTA-PRO readiness criteria remain authoritative for this workflow.

Preserve actual user authorization and delegated decisions. Do not import mandatory approval loops, automatic commits, forced skill chaining, external publication, or particular orchestration/tooling. Resolve important uncertainty without turning routine technical choices into user blockers.

Use conditional guidance instead of a new standalone brainstorming phase, browser service, method catalog, or duplicate intent document. The project specification remains the durable record. Source attribution does not imply endorsement, equivalent behavior, or measured performance improvements.
