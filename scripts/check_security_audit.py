#!/usr/bin/env python3
"""Validate ASVS report *structure*, coverage and presence of test evidence.

This tool does not execute security tests, verify evidence truth, or certify security.
"""
import argparse
import json
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CATALOG = {r['id']: r for r in json.loads((ROOT / 'knowledge/security/asvs/5.0.0/index.json').read_text(encoding='utf-8'))['requirements']}
STATUSES = ('pass', 'fail', 'not_applicable', 'not_tested', 'needs_manual_verification')


def check(report):
    errors = []

    def require(ok, message):
        if not ok:
            errors.append(message)

    if not isinstance(report, dict):
        return {'errors': ['Report must be a JSON object'], 'evidence_verified': False, 'security_certified': False}
    require(report.get('standard') == 'OWASP ASVS', 'standard must equal OWASP ASVS')
    require(report.get('version') == '5.0.0', 'version must equal stable 5.0.0')
    level = report.get('level')
    require(type(level) is int and level in (1, 2, 3), 'level must be integer 1, 2, or 3')
    expected = {k for k, x in CATALOG.items() if type(level) is int and level in (1, 2, 3) and x['level'] <= level}

    scope = report.get('scope')
    require(isinstance(scope, dict), 'scope must be an object')
    scope = scope if isinstance(scope, dict) else {}
    require(isinstance(scope.get('application'), str) and bool(scope.get('application', '').strip()),
            'scope.application requires nonempty name')
    require(isinstance(scope.get('assessment_date'), str) and bool(scope.get('assessment_date', '').strip()),
            'scope.assessment_date is required')
    require(isinstance(scope.get('components'), list) and bool(scope.get('components')) and
            all(isinstance(x, str) and x.strip() for x in scope.get('components', [])),
            'scope.components must list at least one named component')
    require(isinstance(scope.get('trust_boundaries'), list) and bool(scope.get('trust_boundaries')) and
            all(isinstance(x, str) and x.strip() for x in scope.get('trust_boundaries', [])),
            'scope.trust_boundaries must be a nonempty list of boundaries')

    records = report.get('requirements')
    require(isinstance(records, list), 'requirements must be a list')
    records = records if isinstance(records, list) else []
    outcomes = {}
    for i, item in enumerate(records):
        if not isinstance(item, dict):
            errors.append(f'requirements[{i}] must be an object')
            continue
        rid = item.get('id')
        if not isinstance(rid, str) or rid not in CATALOG:
            errors.append(f'requirements[{i}] invalid or unknown ASVS 5.0.0 ID {rid!r}')
            continue
        if rid in outcomes:
            errors.append(f'duplicate requirement {rid}')
            continue
        outcomes[rid] = item
        require(rid in expected, f'{rid} beyond selected L{level}')
        status = item.get('status')
        require(status in STATUSES, f'{rid} invalid status {status!r}')
        evidence = item.get('evidence', [])
        require(isinstance(evidence, list) and all(isinstance(x, str) and x.strip() for x in evidence),
                f'{rid} evidence must be a list of nonempty strings')
        if status in ('pass', 'fail'):
            require(isinstance(evidence, list) and bool(evidence), f'{rid} {status} requires concrete evidence references')
            methods = item.get('methods', [])
            require(isinstance(methods, list) and bool(methods) and all(isinstance(x, str) and x.strip() for x in methods),
                    f'{rid} {status} requires at least one test or inspection method')
        if status == 'not_applicable':
            reason = item.get('rationale')
            require(isinstance(reason, str) and len(reason.strip()) >= 15,
                    f'{rid} N/A requires an architecture-specific rationale')
            require(isinstance(evidence, list) and bool(evidence), f'{rid} N/A requires supporting evidence')
    missing = expected - outcomes.keys()
    if missing:
        errors.append(f'{len(missing)} selected ASVS requirements missing from ledger')
    counts = Counter(i.get('status') for i in outcomes.values())
    complete = (not errors and bool(expected) and all(outcomes[k]['status'] in ('pass', 'fail', 'not_applicable') for k in expected))
    favorable = (complete and all(outcomes[k]['status'] in ('pass', 'not_applicable') for k in expected))
    return {
        'standard': report.get('standard'), 'version': report.get('version'), 'level': level,
        'expected_requirements': len(expected), 'recorded_requirements': len(outcomes),
        'status_counts': {s: counts.get(s, 0) for s in STATUSES},
        'ledger_valid': not errors, 'assessment_coverage_complete': complete,
        'all_recorded_findings_favorable': favorable,
        'evidence_verified': False, 'security_certified': False,
        'note': 'Only structural coverage and evidence presence checked. No live testing or independent security assurance.',
        'errors': errors
    }


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('audit', type=Path)
    p.add_argument('--json', action='store_true')
    args = p.parse_args()
    try:
        report = json.loads(args.audit.read_text(encoding='utf-8'))
    except (OSError, json.JSONDecodeError) as exc:
        p.error(str(exc))
    result = check(report)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print('ASVS security coverage:', result.get('recorded_requirements'), '/', result.get('expected_requirements'),
              '; errors:', len(result['errors']))
        for err in result['errors']:
            print('INVALID:', err)
        print('Evidence not independently verified; security is not certified.')
    return 2 if result['errors'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
