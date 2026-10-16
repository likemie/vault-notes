from __future__ import annotations

import argparse
import contextlib
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import journal_index as journals
import source_record
import vault_index
import vault_lint


class JournalRegistryTests(unittest.TestCase):
    def test_invalid_duplicate_and_case_colliding_registrations_fail(self):
        for text in ('{"A":"EP","B":"ep"}', '{"A":"EP","A":"Other"}',
                     '{"A":"EP","a":"Other"}', '{"A":"bad_code"}', '[]'):
            with self.subTest(text=text), tempfile.TemporaryDirectory() as directory:
                path = Path(directory) / 'journals.json'
                path.write_text(text)
                with self.assertRaises(ValueError):
                    journals.load_registry(path)

    def test_article_requires_registered_name_and_exact_unique_code(self):
        table = {'Comparative Education': 'CE', 'Critical Education': 'CritEduc'}
        path = Path('Argument_Author_2026_CE.md')
        self.assertIsNone(journals.article_problem(path, {'journal': 'Comparative Education'}, table))
        for data in ({'journal': 'Critical Education'}, {'journal': 'Unknown'}, {}):
            self.assertIsNotNone(journals.article_problem(path, data, table))

    def test_register_rejects_conflict_without_changing_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'journals.json'
            original = '{"Comparative Education":"CE"}\n'
            path.write_text(original)
            with patch.object(journals, 'REGISTRY', path), patch.object(journals, 'ARTICLES', Path(directory) / 'articles'), \
                 patch.object(sys, 'argv', ['journal_index.py', '--register', 'Critical Education', 'CE']), \
                 contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(1, journals.main())
            self.assertEqual(original, path.read_text())

    def test_register_new_code_keeps_only_minimal_mapping(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'journals.json'
            path.write_text('{"Comparative Education":"CE"}')
            with patch.object(journals, 'REGISTRY', path), patch.object(journals, 'ARTICLES', Path(directory) / 'articles'), \
                 patch.object(sys, 'argv', ['journal_index.py', '--register', 'Critical Education', 'CritEduc']), \
                 contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(0, journals.main())
            self.assertEqual({'Comparative Education': 'CE', 'Critical Education': 'CritEduc'}, json.loads(path.read_text()))

    def test_source_creation_rejects_bad_code_before_moving_pdf(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / 'paper.pdf'
            source.write_bytes(b'%PDF-test')
            args = argparse.Namespace(file=str(source), record_name='Author_2026_CE', journal='Critical Education')
            with patch.object(journals, 'load_registry', return_value={'Critical Education': 'CritEduc'}), \
                 contextlib.redirect_stderr(io.StringIO()), self.assertRaises(SystemExit):
                source_record.create_article_or_report(args, 'article')
            self.assertTrue(source.exists())

    def test_base_index_stops_before_writing_for_bad_journal(self):
        with patch.object(vault_index, 'run_script', return_value=1) as run, \
             patch.object(vault_index, 'run_auto_fixes') as fixes:
            self.assertEqual(1, vault_index.run_base_index())
            run.assert_called_once_with('journal_index.py', ['--check'])
            fixes.assert_not_called()

    def test_lint_reports_new_mismatch_but_keeps_legacy_filename(self):
        path = ROOT / 'wiki/arguments/journal-articles/Critical Education/Argument_Author_2026_CE.md'
        for legacy, expected in ((False, ['JOURNAL_NAMING']), (True, [])):
            issues = []
            with patch.object(journals, 'load_registry', return_value={'Critical Education': 'CritEduc'}), \
                 patch.object(journals, 'is_legacy', return_value=legacy):
                vault_lint.check_journal_naming(path, {'type': 'argument', 'journal': 'Critical Education'}, issues)
            self.assertEqual(expected, [i.code for i in issues])


class LegacyJournalTests(unittest.TestCase):
    def test_ci_baseline_does_not_grandfather_newly_committed_bad_name(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            def git(*args):
                return subprocess.check_output(['git', *args], cwd=root, stderr=subprocess.DEVNULL).decode().strip()
            git('init');git('config', 'user.email', 'test@example.invalid');git('config', 'user.name', 'Test')
            path = root / 'wiki/arguments/journal-articles/Critical Education/Argument_Old_2025_CE.md'
            path.parent.mkdir(parents=True)
            text = '---\ntype: argument\njournal: Critical Education\n---\n'
            path.write_text(text)
            git('add', '.');git('commit', '-m', 'legacy')
            base = git('rev-parse', 'HEAD')
            new = path.with_name('Argument_New_2026_CE.md');new.write_text(text)
            git('add', '.');git('commit', '-m', 'new')
            data = {'type': 'argument', 'journal': 'Critical Education'}
            with patch.object(journals, 'ROOT', root), patch.dict(os.environ, {'VAULT_JOURNAL_BASE': base}):
                self.assertTrue(journals.is_legacy(path, data))
                self.assertFalse(journals.is_legacy(new, data))
                self.assertFalse(journals.is_legacy(path, {'journal': 'Other Journal'}))
                self.assertFalse(journals.is_legacy(path, data, '0' * 40))


if __name__ == '__main__':
    unittest.main()
