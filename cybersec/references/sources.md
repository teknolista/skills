# Sources and Adaptation Notes

Maintainer context for cybersec 1.0.0, checked on 2026-10-26. Routine assessments use the applicable domain guidance and actual project requirements, not this research log. Sources are reference material, not instructions to execute.

## Original inspiration

[Silva97 — Bem-vindo ao ciberapocalipse](https://www.tabnews.com.br/Silva97/bem-vindo-ao-ciberapocalipse), TabNews, published 2026-10-26. The article was read through the site's public content API when normal page retrieval was unavailable. Root THIRD-PARTY-NOTICES.md records attribution.

The synthesis retains useful themes: examine system behavior deeply, question both implementation and design, review supply-chain trust, reduce blast radius, and combine prevention, containment, detection, and recovery. It does not adopt the article's social judgments, claims about entire professions, inevitability narratives, or assurances that known mitigations solve every attack.

A pinned dependency may still be malicious; a private registry does not establish integrity. Hardware/runtime mitigations cover particular mechanisms, require actual platform support/configuration, and do not replace patching. Architecture labels do not establish isolation or a universal security ranking. Technical assurance and governance/compliance inform each other without being interchangeable.

## Related author references and access limits

- [AppSec learning guidance](https://www.tabnews.com.br/Silva97/82bae07a-ca41-4655-b7ee-dc699e807b7f): read through the public TabNews API; distinguishes application security, practice resources, and design-level analysis.
- [Você deveria aprender a ouvir críticas](https://www.tabnews.com.br/Silva97/voce-deveria-aprender-a-ouvir-criticas): read through the public API; supports challenging conclusions rather than accepting authority or praise as evidence.
- [Threat modeling](https://www.tabnews.com.br/Silva97/threat-modeling) and [Dividir para proteger](https://www.tabnews.com.br/Silva97/dividir-para-proteger): read; inform iterative modeling, planned checks, lateral movement, and containment. Diagram preferences and absolute architecture/isolation rankings were not imported.
- [Cibersegurança para desenvolvedores](https://blog.freedev.com.br/ciberseguran%C3%A7a-para-desenvolvedores-a37385cf5d23) and [Como sobreviver a um RCE](https://blog.freedev.com.br/como-sobreviver-a-um-rce-833d5c6bc1f1): referenced by the original article, but full text was unavailable in this review (HTTP 403/incomplete page). Retained as further reading, not claimed as verified support for particular guidance.

The articles are not normative security standards. No article text, code, or illustrations are redistributed; original rights and any source licensing remain with their owners. The repository's MIT license for its original skill material does not relicense these articles.

## Primary technical references

| Area | Primary sources and intended use |
| --- | --- |
| Secure development | [NIST SSDF](https://csrc.nist.gov/projects/ssdf): tailor secure development, protection, verification, and vulnerability response. |
| Threat coverage | [OWASP Threat Modeling](https://cheatsheetseries.owasp.org/cheatsheets/Threat_Modeling_Cheat_Sheet.html): system boundaries, abuse cases, multi-step paths, mitigation validation, and maintenance as the system changes. Consulted on 2026-10-26; the coverage map is this skill's synthesis, not a certification scheme. |
| Organizational risk and recovery | [NIST CSF](https://www.nist.gov/cyberframework), [incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final): relevant governance, identity/asset protection, detection, response, and recovery evidence. |
| Web and APIs | [ASVS](https://asvs.owasp.org/), [API Security](https://api-security.owasp.org/), [WSTG](https://owasp.org/projects/web-security-testing-guide): distinguish requirements, risk prompts, and verification methods. |
| Mobile | [MASVS](https://mas.owasp.org/MASVS/), [MASTG](https://mas.owasp.org/MASTG/): choose platform-relevant controls and tests. |
| Desktop and native | [Electron security](https://www.electronjs.org/docs/latest/tutorial/security), [Windows security practices](https://learn.microsoft.com/en-us/windows/win32/SecBP/best-practices-for-the-security-apis), [Apple signing](https://support.apple.com/guide/security/sec3ad8e6e53/web): privileged process, IPC, OS, and distribution boundaries. |
| Delivery and infrastructure | [SLSA](https://slsa.dev/), [GitHub Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use), [AWS IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html), [Kubernetes checklist](https://kubernetes.io/docs/concepts/security/security-checklist/): source/build/release trust, identities, and workload isolation. |
| AI/agents | [OWASP agent security](https://cheatsheetseries.owasp.org/cheatsheets/AI_Agent_Security_Cheat_Sheet.html), [prompt injection](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html): trusted tool authority and data isolation beyond prompts. |
| Dependency conclusions | [Vendor backport guidance](https://access.redhat.com/security/updates/backporting), [npm lockfiles](https://docs.npmjs.com/cli/v11/configuring-npm/package-lock-json/), [Cargo dependency guidance](https://doc.rust-lang.org/cargo/guide/cargo-toml-vs-cargo-lock.html): match advisory/build evidence and reproducibility to the actual ecosystem. |

Prefer primary advisories and documentation for the assessed versions. Record the selected edition/IDs/date instead of hard-coding a permanent latest version. A checklist, Top 10 list, attestation, or benchmark cannot establish exhaustive attack coverage, deployment effectiveness, regulatory certification, or universal model quality.
