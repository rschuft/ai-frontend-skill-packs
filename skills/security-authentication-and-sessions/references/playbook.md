# Authentication, sessions, identity tokens, MFA, federated sign-in and logout diagnostic and remediation playbook

## Context and boundaries

Review whether identity is established at the correct boundary and whether sessions are established, rotated, expired and terminated consistently. Relevant ASVS 5.0.0 chapters: V6, V7, V9, V10. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. Trace sign-in, MFA/recovery, token issuance and logout through client, identity provider, and relying-party server.
2. Inspect session-cookie flags and host scope; require server-side enforcement of token validity, audience, expiration and revocation.
3. Prefer established identity libraries and supported OAuth/OIDC flows; avoid long-lived bearer tokens in browser storage without a threat-model justification.
4. Test sign-in, session expiry, concurrent sessions, logout, failed MFA, refresh, and restoration after navigation.

## Common mistakes

- Front-end hiding of a sign-in button is not authentication.
- Do not confuse OAuth authorization tokens with authenticated browser sessions.
- Do not recommend inventing cryptographic protocols or custom token validation.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
