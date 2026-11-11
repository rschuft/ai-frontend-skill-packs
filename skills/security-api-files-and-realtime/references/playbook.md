# API boundaries, file handling, GraphQL, WebSocket and WebRTC risks diagnostic and remediation playbook

## Context and boundaries

Include server-side processing, data exposure and attachment boundaries in scope even when the task is a frontend screen. Relevant ASVS 5.0.0 chapters: V4, V5, V17. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. Identify request schemas, media types, methods, authorization checks, file parsers and realtime channel authentication.
2. Validate request limits and content types on the server; safely handle uploads, file storage paths and downloads.
3. Apply message/field permissions and output filtering to REST, GraphQL and realtime subscriptions.
4. Test legitimate and unauthorized operations, oversized inputs and rejected uploads against owned fixtures or mocks.

## Common mistakes

- Client-side file type hints are not security controls.
- WebSocket handshake success does not establish message-level authorization.
- Do not send test content to production endpoints without explicit permission.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
