#!/usr/bin/env python3
"""Fast, stdlib-only contract tests for the application security skill family."""
import contextlib
import copy
import io
import json
import tempfile
import unittest
from pathlib import Path

from install import install
from resolve_security_target import resolve
from check_security_audit import check, CATALOG

ROOT = Path(__file__).resolve().parent.parent


class SecurityPackTests(unittest.TestCase):
    def sample(self):
        return json.loads((ROOT / 'evaluation/security/sample-audit.json').read_text(encoding='utf-8'))

    def test_complete_asvs_500_index(self):
        self.assertEqual(len(CATALOG), 345)
        self.assertEqual({n: sum(x['level'] <= n for x in CATALOG.values()) for n in (1, 2, 3)},
                         {1: 70, 2: 253, 3: 345})
        self.assertIn('v5.0.0-1.2.5', CATALOG)
        self.assertNotIn('v4.0.3-1.2.5', CATALOG)

    def test_default_policy_is_planning_only(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual((resolve(Path(d))['level'], resolve(Path(d))['source']), (2, 'default'))
            self.assertIn('fallback', resolve(Path(d))['note'])

    def test_project_policy_and_explicit_task_precedence(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            (p / '.frontend-security.json').write_text(json.dumps({'standard': 'OWASP ASVS', 'level': 1}), encoding='utf-8')
            self.assertEqual((resolve(p)['level'], resolve(p)['source']), (1, 'project-policy'))
            self.assertEqual((resolve(p, task_level=3)['level'], resolve(p, task_level=3)['source']), (3, 'explicit-task'))

    def test_invalid_policy_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            for invalid in [{'level': True}, {'version': '4.0.3'}, {'level': 4}, {'foo': 'bar'}, ['not an object']]:
                (p / '.frontend-security.json').write_text(json.dumps(invalid), encoding='utf-8')
                with self.subTest(policy=invalid), self.assertRaises(ValueError):
                    resolve(p)
            (p / '.frontend-security.json').write_text('{', encoding='utf-8')
            with self.assertRaises(ValueError):
                resolve(p)

    def test_unsupported_task_baseline_fails_closed(self):
        with tempfile.TemporaryDirectory() as d:
            for kwargs in ({'task_version': '6.0.0'}, {'task_standard': 'NIST CSF'}, {'task_level': 0}, {'task_level': True}):
                with self.subTest(kwargs=kwargs), self.assertRaises(ValueError):
                    resolve(Path(d), **kwargs)

    def test_security_target_routing_fixtures(self):
        cases = json.loads((ROOT / 'evaluation/security/target_routing_cases.json').read_text(encoding='utf-8'))['cases']
        for c in cases:
            with self.subTest(case=c['id']), tempfile.TemporaryDirectory() as d:
                p = Path(d)
                if c['project_policy']:
                    (p / '.frontend-security.json').write_text(json.dumps(c['project_policy']), encoding='utf-8')
                task = c['task']
                result = resolve(p, task_standard=task.get('standard'), task_version=task.get('version'), task_level=task.get('level'))
                self.assertEqual((result['level'], result['source']), (c['expected_level'], c['source']))

    def test_sample_audit_ledger_is_valid_but_entirely_untested(self):
        result = check(self.sample())
        self.assertFalse(result['errors'])
        self.assertEqual(result['expected_requirements'], 70)
        self.assertEqual(result['recorded_requirements'], 70)
        self.assertEqual(result['status_counts']['not_tested'], 70)
        self.assertTrue(result['ledger_valid'])
        self.assertFalse(result['assessment_coverage_complete'])
        self.assertFalse(result['evidence_verified'])
        self.assertFalse(result['security_certified'])

    def test_missing_and_duplicate_requirements_rejected(self):
        r = self.sample()
        r['requirements'].pop()
        self.assertTrue(any('missing' in x for x in check(r)['errors']))
        r = self.sample()
        r['requirements'].append(copy.deepcopy(r['requirements'][0]))
        self.assertTrue(any('duplicate' in x for x in check(r)['errors']))

    def test_false_pass_and_not_applicable_are_rejected(self):
        for status in ('pass', 'fail', 'not_applicable'):
            r = self.sample()
            r['requirements'][0]['status'] = status
            self.assertTrue(check(r)['errors'], status)

    def test_verified_fields_are_never_misrepresented_as_certification(self):
        r = self.sample()
        for row in r['requirements']:
            row.update({'status': 'pass', 'evidence': ['synthetic test trace'], 'methods': ['fixture contract test']})
        result = check(r)
        self.assertTrue(result['assessment_coverage_complete'])
        self.assertTrue(result['all_recorded_findings_favorable'])
        self.assertFalse(result['evidence_verified'])
        self.assertFalse(result['security_certified'])

    def test_wrong_version_and_out_of_level_requirements_rejected(self):
        r = self.sample()
        r['version'] = '4.0.3'
        self.assertTrue(any('version' in x for x in check(r)['errors']))
        r = self.sample()
        high = next(k for k, v in CATALOG.items() if v['level'] == 3)
        r['requirements'][0]['id'] = high
        self.assertTrue(any('beyond selected' in x for x in check(r)['errors']))
        r = self.sample()
        r['requirements'][0]['id'] = 'v5.0.1-1.2.5'
        self.assertTrue(any('unknown' in x for x in check(r)['errors']))

    def test_security_family_install_and_reference_copy(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d)
            with contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(install(p, 'both', 'security'), 28)
                self.assertEqual(install(p, 'both', 'security'), 28)
            self.assertTrue((p / '.claude/skills/security-diagnose/references/asvs/5.0.0/index.json').is_file())
            self.assertTrue((p / '.agents/skills/security-authorization/references/playbook.md').is_file())
            self.assertFalse((p / '.agents/skills/design-build').exists())

    def test_new_evaluation_cases_cover_every_security_skill(self):
        m = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
        names = {s['name'] for s in m['skills'] if s['pack'] == 'security'}
        cases = json.loads((ROOT / 'evaluation/security/invocation_cases.json').read_text(encoding='utf-8'))
        self.assertEqual(len(names), 14)
        self.assertEqual({c['expected_skill'] for c in cases['positive']}, names)
        self.assertGreaterEqual(len(cases['negative']), 5)

    def test_security_index_and_references_are_identical(self):
        original = (ROOT / 'knowledge/security/asvs/5.0.0/index.json').read_bytes()
        installed = (ROOT / 'skills/security-diagnose/references/asvs/5.0.0/index.json').read_bytes()
        self.assertEqual(original, installed)


if __name__ == '__main__':
    unittest.main()
