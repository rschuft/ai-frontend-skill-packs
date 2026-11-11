# Injection prevention, contextual output handling, validation and untrusted content diagnostic and remediation playbook

## Context and boundaries

Identify the trust boundary between untrusted data and interpreters, template engines, database queries and outgoing requests. Relevant ASVS 5.0.0 chapters: V1, V2. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. Map every untrusted input to its sink and execution context, including HTML, URL, SQL, shell, templating and CSV.
2. Use framework autoescaping, contextual encoders and maintained sanitizers; validate URL scheme and host when appropriate.
3. Use server-side parameter binding for queries and safe structured APIs; avoid string-built commands and unsafe evaluation.
4. Test known safe fixtures and maliciously structured input in a local or approved test environment; capture results without exposing secrets.

## Common mistakes

- Do not use HTML escaping for JavaScript, URL or SQL contexts.
- Sanitization alone is not an authorization check.
- CSP helps reduce impact but is not a replacement for safe sinks.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
