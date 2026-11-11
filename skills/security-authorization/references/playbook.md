# Authorization, object access, tenant isolation and server-enforced permissions diagnostic and remediation playbook

## Context and boundaries

Determine the actual resource/action/actor boundary rather than treating disabled buttons or hidden routes as permission checks. Relevant ASVS 5.0.0 chapters: V8, V2. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. Trace actor, resource owner, tenant, operation and authorization decision at each API entry point.
2. Verify object-level and function-level checks execute server-side for every read and mutation; deny by default.
3. Review list filters, export links, background jobs, cached data and direct ID substitution for cross-tenant access.
4. Test allowed and denied actors across two separate tenants, including stale sessions and direct requests; record only authorized test identities.

## Common mistakes

- Client-side route guards are UX, not authorization.
- A successful HTTP request is not proof of intended entitlement.
- Do not access unapproved tenants or accounts during verification.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
