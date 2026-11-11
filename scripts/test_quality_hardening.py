#!/usr/bin/env python3
"""Pure, fast contracts for skill portability and future behavioral cases."""
import copy
import json
import tempfile
import unittest
from pathlib import Path
from validate_pack import validate_skill_references, validate_behavior_scenarios

ROOT = Path(__file__).resolve().parent.parent


class QualityHardeningTests(unittest.TestCase):
    @staticmethod
    def fixtures():
        return json.loads((ROOT / 'evaluation/agent_behavior_scenarios.json').read_text(encoding='utf-8'))

    @staticmethod
    def names():
        return {s['name'] for s in json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))['skills']}

    def test_all_behavior_scenarios_have_executable_acceptance_contracts(self):
        validate_behavior_scenarios(self.fixtures(), self.names())

    def test_unknown_skill_rejected(self):
        x = self.fixtures()
        x['cases'][0]['acceptable_primary_skills'] = ['not-a-real-skill']
        with self.assertRaisesRegex(AssertionError, 'invalid acceptable primary skills'):
            validate_behavior_scenarios(x, self.names())

    def test_missing_negative_expectations_rejected(self):
        x = self.fixtures()
        x['cases'][0]['prohibited_claims'] = []
        with self.assertRaisesRegex(AssertionError, 'invalid prohibited_claims'):
            validate_behavior_scenarios(x, self.names())

    def test_duplicate_case_ids_rejected(self):
        x = self.fixtures()
        x['cases'][1]['id'] = x['cases'][0]['id']
        with self.assertRaisesRegex(AssertionError, 'Duplicate'):
            validate_behavior_scenarios(x, self.names())

    def test_sibling_reference_resolves_from_installed_layout(self):
        with tempfile.TemporaryDirectory() as d:
            parent = Path(d)
            f = parent / 'skills/design-build/SKILL.md'
            f.parent.mkdir(parents=True)
            ref = parent / 'skills/design-diagnose/references/principles.json'
            ref.parent.mkdir(parents=True)
            ref.write_text('{}', encoding='utf-8')
            validate_skill_references('Use `../design-diagnose/references/principles.json`.', f)

    def test_missing_sibling_prefix_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / 'skills/design-build/SKILL.md'
            f.parent.mkdir(parents=True)
            with self.assertRaisesRegex(AssertionError, 'unresolved installed-skill reference'):
                validate_skill_references('Use `design-diagnose/references/principles.json`.', f)

    def test_missing_cross_skill_file_rejected(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / 'skills/wcag-review/SKILL.md'
            f.parent.mkdir(parents=True)
            with self.assertRaisesRegex(AssertionError, 'unresolved installed-skill reference'):
                validate_skill_references('Read `../wcag-diagnose/references/absent.json`.', f)

    def test_generic_specialist_reference_is_not_misclassified_as_local(self):
        with tempfile.TemporaryDirectory() as d:
            f = Path(d) / 'skills/security-build/SKILL.md'
            f.parent.mkdir(parents=True)
            validate_skill_references("Read the matched specialist's `references/playbook.md`.", f)


if __name__ == '__main__':
    unittest.main()
