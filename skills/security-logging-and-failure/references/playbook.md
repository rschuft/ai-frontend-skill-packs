# Security event logging, audit signals and resilient error handling diagnostic and remediation playbook

## Context and boundaries

Keep user-facing diagnostics separate from internal security telemetry; avoid logging secrets and personal data. Relevant ASVS 5.0.0 chapters: V16. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. Identify authentication, authorization, abuse, transaction and administrative security events.
2. Review safe structured logging, trace context, redaction, integrity, retention and alerting responsibilities.
3. Ensure errors fail safely with useful user recovery but do not expose internal exceptions, keys or implementation details.
4. Test failure modes and alert routing with synthetic events; confirm the owner/operator can investigate the evidence.

## Common mistakes

- Not every exception is an attack and not every 200 status means success.
- Avoid leaking PII or session tokens into monitoring systems.
- Logs alone do not enforce an authorization decision.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
