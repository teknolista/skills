# Mobile Security

Identify Android/iOS, actual release/debug variants, supported OS/SDK versions, entitlements/permissions, backend contracts, and the threat model for a controlled device. Use MASVS for selected controls and MASTG for relevant verification, without treating every resilience measure as mandatory.

- Map exported/inter-app entry points, deep/app/universal links, URI grants, custom schemes, intent handlers, WebViews, JavaScript/native bridges, and local services. Validate sender, arguments, ownership, and navigation at the trusted boundary; an exported entry point alone is not proof of a vulnerability.
- On Android, inspect the merged release manifest, exported components/providers, PendingIntent behavior, runtime permissions, network-security configuration, backups, signing, and debug-only controls. Match conclusions to the supported API levels and build variant.
- On iOS, inspect entitlements, URL/universal-link handling, Keychain access/sharing, app groups/extensions, data protection, ATS exceptions, and provisioning/signing settings relevant to the actual build.
- Trace credentials and sensitive data into preferences/files/databases, backups, notifications, clipboard, screenshots, crash/analytics SDKs, logs, and exports. Check key lifecycle, logout/account-switch cleanup, biometric authorization semantics, and user consent where required.
- Verify TLS trust/hostname handling and actual cleartext endpoints, not only configuration names. Inspect custom trust bypasses and debug overrides leaking into release. Pinning can address specific threats but requires lifecycle/recovery design; its absence is not automatically a defect.
- Remote resource authorization belongs in the trusted backend; hiding UI, obfuscation, device attestation, or root/jailbreak checks do not replace it. Offline resources need their own OS/process/data access policy, not an invented server requirement.
- Check offline sync/conflict behavior, replay, transaction state, delayed client upgrades, cancellation, and background work when they can duplicate privileged effects or leak data. Separate privacy requirements from a generic claim of compliance.
- Review third-party SDK permissions, data destinations, native libraries, distribution integrity, and supported update paths. Judge reverse-engineering resistance against the actual threat, not a universal rule.

Use authorized test devices/emulators and synthetic accounts. Instrumentation can install software and alter device state; repository assessment does not authorize changes to a person's device. State when evidence is static, JVM/unit-only, debug-build-only, or lacks release/device verification.

Primary guidance: [MASVS](https://mas.owasp.org/MASVS/), [MASTG](https://mas.owasp.org/MASTG/).
