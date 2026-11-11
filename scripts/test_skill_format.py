#!/usr/bin/env python3
"""Small, isolated regression tests for portable skill frontmatter and layout."""
import json
import unittest
from pathlib import Path
from validate_pack import validate_skill_markdown

ROOT = Path(__file__).resolve().parent.parent


class SkillFormatTests(unittest.TestCase):
    def test_all_skills_follow_the_contract(self):
        manifest = json.loads((ROOT / 'manifest.json').read_text(encoding='utf-8'))
        expected = {item['name']: item['description'] for item in manifest['skills']}
        self.assertEqual(len(expected), 56)
        for name, description in sorted(expected.items()):
            path = ROOT / 'skills' / name / 'SKILL.md'
            with self.subTest(skill=name):
                self.assertEqual(validate_skill_markdown(path.read_text(encoding='utf-8'), name), description)

    def test_unquoted_colon_is_rejected(self):
        content = self.sample().replace('description: "', 'description: ').replace('"\n---', '\n---')
        with self.assertRaisesRegex(AssertionError, 'double-quoted'):
            validate_skill_markdown(content, 'ux-review')

    def test_missing_procedure_is_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'Scope and one Procedure'):
            validate_skill_markdown(self.sample().replace('## Procedure', '## Workflow'), 'ux-review')

    def test_wrong_name_is_rejected(self):
        with self.assertRaisesRegex(AssertionError, 'match directory'):
            validate_skill_markdown(self.sample(), 'design-review')

    def test_invalid_json_quoted_description_is_rejected(self):
        s = self.sample().replace('description: "', 'description: "invalid \\q ')
        with self.assertRaisesRegex(AssertionError, 'invalid quoted description'):
            validate_skill_markdown(s, 'ux-review')

    @staticmethod
    def sample():
        return ('---\nname: ux-review\ndescription: "Review a complex frontend workflow: '
                'capture evidence and identify practical improvements."\n---\n\n'
                '# Review UX\n\n## Scope\n\nSpecific task and bounds.\n\n'
                '## Procedure\n\n1. Observe the actual workflow before suggesting repairs.\n'
                '2. Record findings and verify their evidence.\n\n'
                'Findings distinguish direct observations from hypotheses and unknown states.\n'
                'Preserve user intent and route implementation through the appropriate workflow.\n')


if __name__ == '__main__':
    unittest.main()
