# Threat models, abuse cases, architecture and secure design reviews diagnostic and remediation playbook

## Context and boundaries

Map assets, trust boundaries, actors and assumptions before classifying risk; security design differs from a static checklist. Relevant ASVS 5.0.0 chapters: V2, V15. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. State protected assets, attacker capabilities, entry points, data flows and trusted execution boundaries.
2. Enumerate realistic abuse and failure scenarios, including multi-tenant, administrative and supply-chain misuse.
3. Match mitigations to specific architecture components and ASVS requirements, with explicit residual risk.
4. Verify assumptions using diagrams, interface contracts and focused negative tests, then record unresolved questions.

## Common mistakes

- A threat hypothesis is not a confirmed vulnerability.
- Do not infer server enforcement from frontend code alone.
- A single checklist cannot substitute for architecture-specific threat modeling.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
