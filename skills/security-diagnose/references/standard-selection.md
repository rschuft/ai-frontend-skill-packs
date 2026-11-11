# Application security baseline selection

## Decision order

1. Use the explicit application/contract security baseline and level when known.
2. Otherwise honor a consuming project's `.frontend-security.json` (or unequivocal `AGENTS.md` policy). Resolve conflicting requirements explicitly before claiming completion.
3. Otherwise use **OWASP ASVS 5.0.0 Level 2 as a review-planning fallback**, not a guarantee the application needs Level 2 or that all controls apply. Level 1 is a subset; Level 3 is for higher-assurance scenarios. Record application boundary and risk context.

```json
{ "standard": "OWASP ASVS", "version": "5.0.0", "level": 2 }
```

ASVS scope includes the relevant service, identity provider, endpoints, deployment, and data paths. **Do not classify an uninspected backend control as a pass** based on frontend source, a passing SAST scan, or an inaccessible network. Record `not_tested` or `needs_manual_verification`. Mark `not_applicable` only with a rationale tied to architecture and a reviewable exception.

For machine-readable completeness, resolve policy with `scripts/resolve_security_target.py` and assess `evaluation/security/sample-audit.json` using `scripts/check_security_audit.py`. These helpers ship in the distribution repository, not automatically in an installed skill folder; each diagnostic skill includes its copy of the catalog and selection guidance.

**Authority:** Requirement identifiers are pinned to [ASVS 5.0.0](https://github.com/OWASP/ASVS/tree/v5.0.0_release/5.0). The bundled index omits requirement wording, so read upstream requirements when evaluating their meaning. OWASP WSTG 4.2 describes testing techniques; OWASP Top 10:2025 is risk awareness. NIST SSDF 1.1 adds secure-development process guidance and NIST CSF 2.0 optional governance context; neither is a substitute for ASVS. SSDF 1.2 is draft-only as of the catalog snapshot.

Security tools are separate evidence producers, not agent attestations. Untrusted inputs, active testing and destructive/external systems require explicit authorization. Redact secrets and personal data in report artifacts. No collection of automated scans certifies an application as secure.
