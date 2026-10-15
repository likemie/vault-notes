from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import vault_lint as lint


class DuplicateYamlKeyTests(unittest.TestCase):
    def parse(self, frontmatter):
        issues = []
        result = lint.parse_yaml_fm(frontmatter, ROOT / "sources/Example.md", issues)
        return result, issues

    def test_top_level_duplicate_reports_both_file_line_numbers(self):
        result, issues = self.parse('title: First\nsummary: Text\ntitle: Second')
        self.assertEqual({}, result)
        self.assertEqual([("ERROR", "YAML_DUPLICATE_KEY", 4)], [(i.severity, i.code, i.line) for i in issues])
        self.assertIn("first declared on line 2", issues[0].message)

    def test_nested_flow_quoted_and_aliased_keys_are_checked(self):
        for fm in ('metadata:\n  year: 2025\n  year: 2026',
                   'metadata: {year: 2025, year: 2026}',
                   'title: First\n"title": Second',
                   '"tit\\u006ce": First\ntitle: Second',
                   '? &key title\n: First\n? *key\n: Second',
                   'items:\n  - {year: 2025, year: 2026}'):
            with self.subTest(fm=fm):
                self.assertEqual(["YAML_DUPLICATE_KEY"], [i.code for i in self.parse(fm)[1]])

    def test_equal_keys_in_distinct_mappings_are_valid(self):
        _, issues = self.parse('first: {year: 2025}\nsecond: {year: 2026}\nitems: [{name: A}, {name: B}]')
        self.assertEqual([], issues)

    def test_comments_block_scalars_and_body_do_not_count_as_keys(self):
        data, issues = self.parse('title: First\n# title: Second\nsummary: |\n  title: Third\n  title: Fourth')
        self.assertEqual([], issues)
        self.assertIn('title: Fourth', data['summary'])

    def test_merge_defaults_can_be_overridden_without_false_duplicates(self):
        data, issues = self.parse('defaults: &defaults {year: 2025}\nmetadata:\n  <<: *defaults\n  year: 2026')
        self.assertEqual([], issues)
        self.assertEqual(2026, data['metadata']['year'])

    def test_explicit_duplicate_after_merge_still_fails(self):
        _, issues = self.parse('defaults: &defaults {year: 2025}\nmetadata:\n  <<: *defaults\n  year: 2026\n  year: 2027')
        self.assertEqual(["YAML_DUPLICATE_KEY"], [i.code for i in issues])

    def test_reused_nested_merge_does_not_recheck_expanded_keys(self):
        data, issues = self.parse('defaults: &base {year: 2025}\nfirst: {<<: &override {<<: *base, year: 2026}}\nsecond: *override')
        self.assertEqual([], issues)
        self.assertEqual(2026, data['second']['year'])

    def test_invalid_yaml_still_reports_parse_error(self):
        self.assertEqual(["YAML_PARSE"], [i.code for i in self.parse('title: [broken')[1]])

    def test_cli_returns_failure_and_json_location(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "duplicate.md"
            path.write_text('---\ncitation: First\ncitation: Second\n---\nBody\n')
            result = subprocess.run([sys.executable, '-B', str(ROOT / 'scripts/vault_lint.py'), '--path', str(path), '--json'], cwd=ROOT, capture_output=True, text=True)
            self.assertEqual(1, result.returncode, result.stderr)
            duplicates = [i for i in json.loads(result.stdout) if i['code'] == 'YAML_DUPLICATE_KEY']
            self.assertEqual([3], [i['line'] for i in duplicates])


if __name__ == '__main__':
    unittest.main()
