#!/usr/bin/env python3
"""Focused offline tests for installation safety, coexistence and audit gating."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from install import install
from check_wcag_audit import check, CATALOGS
from resolve_wcag_target import resolve

ROOT = Path(__file__).resolve().parent.parent


class CombinedPackTests(unittest.TestCase):
    def quiet(self, *args, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return install(*args, **kwargs)

    def test_version_neutral_wcag_layout_and_resolver_paths(self):
        self.assertEqual(len(list((ROOT/'skills').glob('wcag-*'))), 14)
        self.assertFalse(list((ROOT/'skills').glob('wcag21-*')))
        self.assertFalse((ROOT/'knowledge/wcag21').exists())
        self.assertFalse((ROOT/'evaluation/wcag21').exists())
        for version in ('2.1', '2.2'):
            repo = ROOT / 'knowledge/wcag' / version / 'criteria.json'
            refs = ROOT / 'skills/wcag-diagnose/references' / version / 'criteria.json'
            self.assertEqual(repo.read_bytes(), refs.read_bytes())
        with tempfile.TemporaryDirectory() as td:
            self.assertEqual(resolve(Path(td))['catalog'], 'knowledge/wcag/2.2/criteria.json')
            self.assertEqual(resolve(Path(td), task_standard='WCAG 2.1')['catalog'], 'knowledge/wcag/2.1/criteria.json')
            self.assertEqual(resolve(Path(td), task_standard='WCAG 3.0')['catalog'], 'knowledge/wcag/3.0/draft-guidance.json')

    def test_wcag_csv_catalogs_match_installed_references(self):
        """Published CSV reference copies must be exact and LF-normalized."""
        for name in ('2.1/criteria.csv', '2.2/criteria.csv'):
            source = ROOT / 'knowledge/wcag' / name
            bundled = ROOT / 'skills/wcag-diagnose/references' / name
            with self.subTest(catalog=name):
                data = source.read_bytes()
                self.assertIn(b'\n', data)
                self.assertNotIn(b'\r\n', data)
                self.assertEqual(data, bundled.read_bytes())

    def test_both_hosts_dry_run_without_side_effects(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            self.assertEqual(self.quiet(p, 'both', 'both', dry_run=True), 112)
            self.assertFalse((p/'.claude').exists())
            self.assertFalse((p/'.agents').exists())

    def test_both_hosts_install_repeat_and_retain_unrelated_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            old = p/'.claude/skills/unrelated'
            old.mkdir(parents=True)
            (old/'SKILL.md').write_text('unchanged', encoding='utf-8')
            self.assertEqual(self.quiet(p,'both','both'),112)
            self.assertEqual(self.quiet(p,'both','both'),112)
            self.assertEqual((old/'SKILL.md').read_text(encoding='utf-8'),'unchanged')
            self.assertTrue((p/'.agents/skills/ux-diagnose/references/principles.json').is_file())
            self.assertTrue((p/'.claude/skills/wcag-diagnose/references/2.1/criteria.json').is_file())

    def test_family_filter_installs_only_one_family(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            self.assertEqual(self.quiet(p,'claude','wcag'),14)
            self.assertTrue((p/'.claude/skills/wcag-diagnose/SKILL.md').exists())
            self.assertFalse((p/'.claude/skills/ux-diagnose').exists())
            self.assertEqual(self.quiet(p,'claude','ux-laws'),14)
            self.assertTrue((p/'.claude/skills/ux-diagnose/SKILL.md').exists())

    def test_refuse_conflict_without_mutating_other_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            conflict = p/'.claude/skills/wcag-review'
            conflict.mkdir(parents=True)
            (conflict/'SKILL.md').write_text('my custom skill', encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'Existing different skill'):
                self.quiet(p,'claude','both')
            self.assertFalse((p/'.claude/skills/ux-build').exists())
            self.assertEqual((conflict/'SKILL.md').read_text(encoding='utf-8'),'my custom skill')
            self.assertEqual(self.quiet(p,'claude','both',replace=True),56)
            self.assertIn('wcag-review',(conflict/'SKILL.md').read_text(encoding='utf-8'))

    def test_visual_design_family_filter_and_specialist_references(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            self.assertEqual(self.quiet(p, 'codex', 'visual-design'), 14)
            self.assertTrue((p/'.agents/skills/design-diagnose/references/principles.json').is_file())
            self.assertTrue((p/'.agents/skills/design-color-theory/references/playbook.md').is_file())
            self.assertFalse((p/'.agents/skills/ux-diagnose').exists())
            self.assertFalse((p/'.agents/skills/wcag-review').exists())

    def test_legacy_both_alias_includes_all_families(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            self.assertEqual(self.quiet(p, 'claude', 'both', dry_run=True), 56)
            self.assertEqual(self.quiet(p, 'claude', 'all', dry_run=True), 56)

    def test_visual_design_conflict_refusal_preflight(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            d = p/'.claude/skills/design-color-theory'
            d.mkdir(parents=True)
            (d/'SKILL.md').write_text('local custom version', encoding='utf8')
            with self.assertRaisesRegex(ValueError, 'Existing different skill'):
                self.quiet(p, 'claude', 'all')
            self.assertFalse((p/'.claude/skills/design-build').exists())
            self.assertEqual((d/'SKILL.md').read_text(encoding='utf8'), 'local custom version')

    def test_refuse_symlinked_destination(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            actual = p/'actual'
            actual.mkdir()
            link = p/'.agents'
            try:
                link.symlink_to(actual, target_is_directory=True)
            except (OSError,NotImplementedError):
                self.skipTest('No symlink permission on platform')
            with self.assertRaisesRegex(ValueError,'symlink'):
                self.quiet(p,'codex','ux-laws')
            self.assertEqual(list(actual.iterdir()),[])

    def test_report_structure_cannot_certify(self):
        self.assertEqual(len(CATALOGS['WCAG 2.1']),78)
        self.assertEqual(len(CATALOGS['WCAG 2.2']),86)
        report=json.loads((ROOT/'evaluation/wcag/sample-audit.json').read_text(encoding='utf-8'))
        result=check(report)
        self.assertEqual(result['expected_criteria'],50)
        self.assertFalse(result['ready_for_independent_human_conformance_review'])
        self.assertFalse(result['conformance_certified'])
        self.assertEqual(result['status_counts']['not_tested'],49)

    def test_report_missing_criteria_rejected(self):
        report=json.loads((ROOT/'evaluation/wcag/sample-audit.json').read_text(encoding='utf-8'))
        report['criteria']=report['criteria'][:-1]
        self.assertTrue(check(report)['errors'])


    def test_wcag_22_default_resolution(self):
        with tempfile.TemporaryDirectory() as td:
            r = resolve(Path(td))
            self.assertEqual((r['standard'],r['level'],r['source']), ('WCAG 2.2','AA','default'))
            self.assertTrue(r['conformance_allowed'])

    def test_project_policy_and_task_override(self):
        with tempfile.TemporaryDirectory() as td:
            p = Path(td)
            (p/'.frontend-a11y.json').write_text(json.dumps({'standard':'WCAG 2.1','level':'AAA','wcag3_advisory':True}),encoding='utf-8')
            self.assertEqual((resolve(p)['standard'],resolve(p)['level']), ('WCAG 2.1','AAA'))
            self.assertEqual((resolve(p,task_standard='WCAG 2.2')['standard'], resolve(p,task_standard='WCAG 2.2')['level']), ('WCAG 2.2','AA'))
            self.assertEqual(resolve(p,task_level='A')['level'],'A')

    def test_wcag3_draft_is_research_only(self):
        with tempfile.TemporaryDirectory() as td:
            r=resolve(Path(td),task_standard='WCAG 3.0')
            self.assertEqual(r['mode'],'research_only')
            self.assertFalse(r['conformance_allowed'])
            self.assertIsNone(r['level'])
            with self.assertRaisesRegex(ValueError,'no A/AA/AAA'):
                resolve(Path(td),task_standard='WCAG 3.0',task_level='AA')
            (Path(td)/'.frontend-a11y.json').write_text('{'+'"standard": "WCAG 3.0"'+'}',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'must be WCAG 2.1 or WCAG 2.2'):
                resolve(Path(td))

    def test_wcag_22_aa_sample_and_version_mixing(self):
        report=json.loads((ROOT/'evaluation/wcag/sample-audit-22.json').read_text(encoding='utf-8'))
        result=check(report)
        self.assertEqual(result['expected_criteria'],55)
        self.assertEqual(result['recorded_criteria'],55)
        self.assertEqual(result['status_counts']['not_tested'],55)
        self.assertFalse(result['conformance_certified'])
        self.assertFalse(result['ready_for_independent_human_conformance_review'])
        self.assertEqual(result['errors'],[])
        report['criteria'][0]['id']='4.1.1'  # removed in 2.2
        self.assertTrue(any('does not exist' in e for e in check(report)['errors']))

    def test_wcag_rejects_22_only_criteria(self):
        report=json.loads((ROOT/'evaluation/wcag/sample-audit.json').read_text(encoding='utf-8'))
        report['criteria'][0]['id']='2.5.8'
        self.assertTrue(any('does not exist' in e for e in check(report)['errors']))

    def test_wcag3_cannot_be_conformance_audit(self):
        report=json.loads((ROOT/'evaluation/wcag/sample-audit-22.json').read_text(encoding='utf-8'))
        report['standard']='WCAG 3.0'
        result=check(report)
        self.assertTrue(result['errors'])
        self.assertEqual(result['expected_criteria'],0)
        self.assertFalse(result['ready_for_independent_human_conformance_review'])

    def test_version_routing_evaluation_cases(self):
        cases=json.loads((ROOT/'evaluation/wcag/version_routing_cases.json').read_text(encoding='utf-8'))['cases']
        for case in cases:
            with tempfile.TemporaryDirectory() as td:
                p=Path(td)
                if case['project_policy']:
                    (p/'.frontend-a11y.json').write_text(json.dumps(case['project_policy']),encoding='utf-8')
                task=case.get('task') or {}
                r=resolve(p,task.get('standard'),task.get('level'))
                with self.subTest(case=case['id']):
                    self.assertEqual((r['standard'],r['level'],r['mode']), (case['expected_standard'],case['expected_level'],case['mode']))

    def test_installed_wcag_reference_has_versioned_catalogs(self):
        with tempfile.TemporaryDirectory() as td:
            p=Path(td)
            self.assertEqual(self.quiet(p,'codex','wcag'),14)
            refs=p/'.agents/skills/wcag-diagnose/references'
            self.assertTrue((refs/'2.2/criteria.json').is_file())
            self.assertTrue((refs/'3.0/draft-guidance.json').is_file())
            self.assertTrue((refs/'standard-selection.md').is_file())


if __name__ == '__main__':
    unittest.main()
