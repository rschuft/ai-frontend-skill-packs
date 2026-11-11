# Browser security, DOM sinks, CSP, cookies, origin separation and third-party scripts diagnostic and remediation playbook

## Context and boundaries

Distinguish browser-enforced mitigations from server-enforced authorization and session integrity. Relevant ASVS 5.0.0 chapters: V3. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. Inspect rendered DOM injection sinks, navigation targets, iframe policies, third-party scripts and storage of sensitive values.
2. Review applicable CSP, cookies, CSRF defense, CORS response rules, frame ancestry and referrer policy.
3. Use restrictive policies grounded in actual resources; avoid breaking required content or relying on wildcard origins.
4. Verify policies and responses in browser developer tools and negative tests from a controlled cross-origin test page.

## Common mistakes

- CORS is not authentication or CSRF prevention by itself.
- Security headers require examination of actual HTTP responses.
- Do not claim complete XSS protection solely from a CSP header.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
