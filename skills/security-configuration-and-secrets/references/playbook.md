# Secure application configuration, secret custody and operational exposure diagnostic and remediation playbook

## Context and boundaries

Separate public build-time variables from server-side secrets and privileged configuration. Relevant ASVS 5.0.0 chapters: V13. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. Inventory configuration entry points, default values, feature flags and environment-specific overrides.
2. Locate accidental browser-bundle or source-map exposure of sensitive configuration; do not print secret values.
3. Require secrets from a managed provider; check privilege scope, rotation, audit trail and safe fallback behavior.
4. Verify hardened deployment config and negative configuration cases; redact logs and findings.

## Common mistakes

- A variable called SECRET is not secret when embedded into a public JavaScript bundle.
- Do not assume repository scanning covers runtime-injected secrets.
- Never include credentials in tests or evidence artifacts.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
