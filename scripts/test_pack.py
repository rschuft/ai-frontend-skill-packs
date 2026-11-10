#!/usr/bin/env python3
"""Focused offline tests for installation safety, coexistence and audit gating."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from install import install
from check_wcag_audit import check, CAT

ROOT = Path(__file__).resolve().parent.parent


class CombinedPackTests(unittest.TestCase):
    def quiet(self, *args, **kwargs):
        with contextlib.redirect_stdout(io.StringIO()):
            return install(*args, **kwargs)

    def test_both_hosts_dry_run_without_side_effects(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            self.assertEqual(self.quiet(p, 'both', 'both', dry_run=True), 56)
            self.assertFalse((p/'.claude').exists())
            self.assertFalse((p/'.agents').exists())

    def test_both_hosts_install_repeat_and_retain_unrelated_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            old = p/'.claude/skills/unrelated'
            old.mkdir(parents=True)
            (old/'SKILL.md').write_text('unchanged', encoding='utf-8')
            self.assertEqual(self.quiet(p,'both','both'),56)
            self.assertEqual(self.quiet(p,'both','both'),56)
            self.assertEqual((old/'SKILL.md').read_text(encoding='utf-8'),'unchanged')
            self.assertTrue((p/'.agents/skills/ux-diagnose/references/principles.json').is_file())
            self.assertTrue((p/'.claude/skills/wcag21-diagnose/references/criteria.json').is_file())

    def test_family_filter_installs_only_one_family(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            self.assertEqual(self.quiet(p,'claude','wcag21'),14)
            self.assertTrue((p/'.claude/skills/wcag21-diagnose/SKILL.md').exists())
            self.assertFalse((p/'.claude/skills/ux-diagnose').exists())
            self.assertEqual(self.quiet(p,'claude','ux-laws'),14)
            self.assertTrue((p/'.claude/skills/ux-diagnose/SKILL.md').exists())

    def test_refuse_conflict_without_mutating_other_skills(self):
        with tempfile.TemporaryDirectory() as tmp:
            p = Path(tmp)
            conflict = p/'.claude/skills/wcag21-review'
            conflict.mkdir(parents=True)
            (conflict/'SKILL.md').write_text('my custom skill', encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'Existing different skill'):
                self.quiet(p,'claude','both')
            self.assertFalse((p/'.claude/skills/ux-build').exists())
            self.assertEqual((conflict/'SKILL.md').read_text(encoding='utf-8'),'my custom skill')
            self.assertEqual(self.quiet(p,'claude','both',replace=True),28)
            self.assertIn('wcag21-review',(conflict/'SKILL.md').read_text(encoding='utf-8'))

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
        self.assertEqual(len(CAT),78)
        report=json.loads((ROOT/'evaluation/wcag21/sample-audit.json').read_text(encoding='utf-8'))
        result=check(report)
        self.assertEqual(result['expected_criteria'],50)
        self.assertFalse(result['ready_for_independent_human_conformance_review'])
        self.assertFalse(result['conformance_certified'])
        self.assertEqual(result['status_counts']['not_tested'],49)

    def test_report_missing_criteria_rejected(self):
        report=json.loads((ROOT/'evaluation/wcag21/sample-audit.json').read_text(encoding='utf-8'))
        report['criteria']=report['criteria'][:-1]
        self.assertTrue(check(report)['errors'])


if __name__ == '__main__':
    unittest.main()
