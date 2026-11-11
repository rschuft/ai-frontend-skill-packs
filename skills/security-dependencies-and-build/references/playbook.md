# Dependencies, supply chain, build provenance and secure coding workflow diagnostic and remediation playbook

## Context and boundaries

Treat SCA and secure delivery as independent gates; a model claim or a passing build is not a security scan. Relevant ASVS 5.0.0 chapters: V15. Consult the exact version-pinned OWASP ASVS requirement text and related OWASP WSTG 4.2 test methods when needed, within authorized scope.

## Differential diagnosis

- Start from a **reproducible symptom** and a specific affected actor, resource and runtime state.
- Ask whether the relevant control is actually server-enforced, whether client-facing evidence is only suggestive, and whether the observed outcome is consistent with an intended project policy.
- Identify nearby security categories that could explain the same symptom; do not collapse distinct authorization, authentication, input handling or deployment failures into one issue.

## Practical sequence

1. Inventory direct and transitive dependencies, lockfiles, build plugins, externally loaded scripts and deploy artifacts.
2. Use existing maintained SCA, secret scanning, static analysis and signing/provenance where appropriate.
3. Check advisories for affected versions and exploitability, propose lowest-risk supported upgrades, and preserve reproducible builds.
4. Re-run focused build/tests/scans; record tool versions and results, and treat missing scanning as not tested.

## Common mistakes

- Do not claim a vulnerability because a package name looks risky without an advisory or evidence.
- Do not force upgrades that violate supported runtime or API contracts.
- A clean SCA scan is not proof of a secure application.

## Evidence and safe verification

- Identify test target, authorization, environment, component, relevant version-prefixed ASVS requirement IDs, inspection method and date.
- Preserve minimal redacted reproduction and explain the user's or operator's actual security impact.
- Use negative tests on owned fixtures or mocks where possible. Dynamic security tests, scanning and actions against live endpoints require explicit approval.
- Distinguish tested and untested controls. The selected ASVS verification level is cumulative, not an independent severity rating.

## Related workflows

Start with `security-diagnose` if root cause is ambiguous. `security-review` creates a coverage ledger; `security-build` implements controlled fixes; `security-validate` records retest evidence.
