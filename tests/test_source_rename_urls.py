from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
import source_record as source
import vault_lint as lint


class PublishedSourceRenameTests(unittest.TestCase):
    old_url = 'https://img.mylikemie.icu/sources/Old_2024_EP/Old_2024_EP.pdf'
    old_text = f'---\ncitation: "Author (2024). Title."\nextracted_to: []\nprocessed_date: 2026-01-01\n---\n\n# Old_2024_EP\n\n![[Old_2024_EP.pdf]]\n\n<iframe src="{old_url}"></iframe>\n'

    def render(self, preserve):
        return source.update_source_record_text(
            self.old_text, new_name='Old_2024_EducPsych', citation='Author (2024). Title.',
            pdf_filename='Old_2024_EducPsych.pdf', processed_date=None,
            pdf_path=ROOT / 'sources/Old_2024_EducPsych/Old_2024_EducPsych.pdf',
            preserve_remote_url=preserve,
        )

    def test_rename_preserves_published_url_and_changes_local_embed(self):
        text = self.render(True)
        self.assertIn(self.old_url, text)
        self.assertIn('![[Old_2024_EducPsych.pdf]]', text)
        self.assertIn('# Old_2024_EducPsych\n', text)
        self.assertIn('processed_date: 2026-01-01', text)

    def test_default_still_generates_url_from_new_path(self):
        text = self.render(False)
        self.assertNotIn(self.old_url, text)
        self.assertIn('https://img.mylikemie.icu/sources/Old_2024_EducPsych/Old_2024_EducPsych.pdf', text)

    def test_later_citation_refresh_keeps_migrated_published_url(self):
        text = source.update_source_record_text(
            self.render(True), new_name='Old_2024_EducPsych', citation='Author (2024). Updated title.',
            pdf_filename='Old_2024_EducPsych.pdf', processed_date=None,
            pdf_path=ROOT / 'sources/Old_2024_EducPsych/Old_2024_EducPsych.pdf',
        )
        self.assertIn(self.old_url, text)
        self.assertIn('Updated title.', text)

    def test_preservation_refuses_missing_published_url(self):
        with self.assertRaises(ValueError):
            source.update_source_record_text('---\ncitation: Test\n---\n', new_name='New', citation='Test', pdf_filename='New.pdf', processed_date=None, pdf_path=ROOT / 'sources/New.pdf', preserve_remote_url=True)

    def test_lint_allows_explicit_published_url_after_local_rename(self):
        issues = []
        lint.check_source_record(ROOT / 'sources/Old_2024_EducPsych/Old_2024_EducPsych.md', self.render(True), issues)
        self.assertNotIn('SOURCE_PDF_NAS_URL_MISSING', [i.code for i in issues])

    def test_lint_still_rejects_missing_or_wrong_host_iframe(self):
        for body in ('', '<iframe src="https://wrong.example/Old.pdf"></iframe>'):
            text = '---\ncitation: "Author (2024). Title."\nextracted_to: []\nprocessed_date: 2026-01-01\n---\n\n# New\n\n![[New.pdf]]\n' + body
            issues = []
            lint.check_source_record(ROOT / 'sources/New.md', text, issues)
            self.assertIn('SOURCE_PDF_NAS_URL_MISSING', [i.code for i in issues])


if __name__ == '__main__':
    unittest.main()
