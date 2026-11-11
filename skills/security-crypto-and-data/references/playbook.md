# Cryptography, transport security, data protection and privacy boundaries diagnostic and remediation playbook

## Context and boundaries

Trace data sensitivity and location before suggesting controls; browser code and keys are inherently observable to users. Relevant ASVS 5.0.0 chapters: V11, V12, V14. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. Classify sensitive fields, where they travel, storage lifetime, access and logging paths.
2. Use vetted TLS and cryptographic libraries; select established algorithms with appropriate key custody and rotation.
3. Minimize data delivered to clients; consider caching, browser persistence, URLs, error reports, and telemetry.
4. Verify protected transport, appropriate access and retention in a controlled environment; never dump real keys or user data.

## Common mistakes

- Client-side encryption does not solve authorization if the browser receives the decryption secret.
- Hashing is not reversible encryption.
- Do not invent or implement bespoke crypto algorithms.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
