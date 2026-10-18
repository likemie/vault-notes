"""Regression tests; fixtures never touch the real vault."""
import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import link_exceptions as ex
import wiki_linker as linker


class LinkExceptionsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.note = 'wiki/arguments/Example.md'
        self.target = 'wiki/concepts/Research Hypothesis.md'
        self.other = 'wiki/concepts/Evidence.md'
        self.entries = [linker.Entry('Research Hypothesis', self.target, ('假设',), 'concept'),
                        linker.Entry('Evidence', self.other, ('证据',), 'concept'),
                        linker.Entry('Example', self.note, (), 'argument')]
        for entry in self.entries:
            path = self.root / entry.path
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('---\ntype: ' + entry.type + '\n---\n', encoding='utf-8')
        self.registry = self.root / 'scripts/link_exceptions.json'
        self.registry.parent.mkdir()
        self.patch = patch.multiple(linker, ROOT=self.root, WIKI_DIR=self.root / 'wiki',
                                    LINK_EXCEPTIONS=self.registry, INDEX_JSON=self.root / 'wiki/index.json')
        self.patch.start(); self.addCleanup(self.patch.stop)
        linker.INDEX_JSON.write_text(json.dumps([
            dict(title=e.title, path=e.path, aliases=e.aliases, type=e.type) for e in self.entries]))

    def record(self, sentence='这一假设需要证据。'):
        return {'sentence': sentence, 'target': self.target}

    def sync(self, body, records, dry_run=False):
        path = self.root / self.note
        path.write_text('---\ntype: argument\n---\n' + body)
        terms, by_title, path_to_title = linker.make_terms(self.entries)
        linker.sync_file(path, terms, linker.TermMatcher(terms), None, {}, by_title,
                         path_to_title, {}, linker.build_person_prefix_registry(terms),
                         dry_run, exclusions=records)
        return linker.split_frontmatter(path.read_text())[1]

    def test_only_one_sentence_target_and_first_valid_mention(self):
        body = '这一[[Research Hypothesis|假设]]需要证据。研究假设涉及证据。\n'
        result = self.sync(body, [self.record()])
        self.assertIn('这一假设需要[[Evidence|证据]]。', result)
        # Use a separate standalone occurrence for the original boundary rule.
        result = self.sync('这一假设需要证据。\n假设需要检验。\n', [self.record()])
        self.assertIn('这一假设需要[[Evidence|证据]]。', result)
        self.assertIn('[[Research Hypothesis|假设]]需要检验。', result)

    def test_removed_link_does_not_change_identity(self):
        plain = '这一假设需要证据。'
        linked = '这一[[Research Hypothesis|假设]]需要[[Evidence|证据]]。'
        self.assertEqual([s for s, _, _ in ex.sentences(plain)],
                         [s for s, _, _ in ex.sentences(linked)])
        result = self.sync(linked, [self.record()])
        self.assertEqual(result, self.sync(result, [self.record()]))

    def test_registration_removes_only_existing_mislink_and_deduplicates(self):
        path = self.root / self.note
        path.write_text('---\ntype: argument\n---\n这一[[Research Hypothesis|假设]]需要证据。\n')
        with contextlib.redirect_stdout(io.StringIO()):
            linker.register_exclusion(self.note, self.record()['sentence'], self.target)
            linker.register_exclusion(self.note, self.record()['sentence'], self.target)
        self.assertIn('这一假设需要证据。', path.read_text())
        self.assertEqual(ex.load(self.registry), {self.note: [self.record()]})

    def test_prune_deleted_edited_missing_targets_and_dry_run(self):
        path = self.root / self.note
        path.write_text('---\ntype: argument\n---\n这一假设需要证据。\n')
        data = {self.note: [self.record(), self.record('已经删除的句子。')]}
        ex.save(self.registry, data)
        _, active = ex.clean(self.root, self.registry, dry_run=True)
        self.assertEqual(active, {self.note: [self.record()]})
        self.assertEqual(ex.load(self.registry), data)
        ex.clean(self.root, self.registry)
        path.write_text('---\ntype: argument\n---\n这一猜测需要证据。\n')
        self.assertEqual(ex.prune(self.root, ex.load(self.registry)), {})
        path.unlink()
        self.assertEqual(ex.prune(self.root, data), {})
        path.write_text('这一假设需要证据。')
        (self.root / self.target).unlink()
        self.assertEqual(ex.prune(self.root, data), {})

    def test_read_failure_never_rewrites_registry(self):
        data = {self.note: [self.record()]}
        ex.save(self.registry, data)
        original_read = Path.read_text
        def fail(path, *args, **kwargs):
            if path == self.root / self.note: raise PermissionError('unreadable')
            return original_read(path, *args, **kwargs)
        with patch.object(Path, 'read_text', fail), self.assertRaises(PermissionError):
            ex.clean(self.root, self.registry)
        self.assertEqual(ex.load(self.registry), data)

    def test_duplicate_sentence_and_bad_registration_rejected(self):
        path = self.root / self.note
        path.write_text('这一假设需要证据。\n这一假设需要证据。')
        with self.assertRaises(ValueError):
            linker.register_exclusion(self.note, self.record()['sentence'], self.target)
        with self.assertRaises(ValueError):
            ex.mask(path.read_text(), [self.record()], self.entries, linker.valid_boundary)
        with self.assertRaises(ValueError):
            linker.register_exclusion(self.note, self.record()['sentence'], self.note)

    def test_table_and_callout(self):
        for body in ('> 这一[[Research Hypothesis|假设]]需要证据。\n',
                     '| 这一[[Research Hypothesis\\|假设]]需要证据。 | 其他 |\n'):
            result = self.sync(body, [self.record()])
            self.assertNotIn('Research Hypothesis', result)
            self.assertIn('假设', result)
        body = '| 假设需要检验。 | 证据 |\n'
        result = self.sync(body, [self.record('假设需要检验。')])
        self.assertIn('| 假设需要检验。 |', result)
        self.assertIn('[[Evidence\\|证据]]', result)

    def test_code_protected_and_no_record_preserves_normal_behavior(self):
        body = '```text\n这一假设需要证据。\n```\n'
        masked, replacements = ex.mask(body, [self.record()], self.entries, linker.valid_boundary)
        self.assertEqual(masked, body)
        self.assertEqual(replacements, {})
        result = self.sync('假设需要检验。\n', [])
        self.assertIn('[[Research Hypothesis|假设]]', result)

    def test_incremental_registry_only_change_and_sync_dry_run(self):
        path = self.root / self.note
        original = '---\ntype: argument\n---\n这一[[Research Hypothesis|假设]]需要证据。\n'
        path.write_text(original)
        ex.save(self.registry, {self.note: [self.record()]})
        with patch.object(linker, 'select_link_files', return_value=[]), \
             patch.object(linker, 'git_files_at_ref', return_value={}), \
             patch.object(linker, 'load_source_entries', return_value=[]), \
             contextlib.redirect_stdout(io.StringIO()):
            linker.run_sync([], True, False, False, False, wiki_only=True)
            self.assertEqual(path.read_text(), original)
            linker.run_sync([], False, False, False, False, wiki_only=True)
        self.assertNotIn('Research Hypothesis', path.read_text())

    def test_invalid_registry_fails_instead_of_resetting(self):
        self.registry.write_text('{"wiki/a.md":[],"wiki/a.md":[]}')
        with self.assertRaises(ValueError): ex.load(self.registry)
        self.registry.write_text('{"../outside.md":[]}')
        with self.assertRaises(ValueError): ex.load(self.registry)


if __name__ == '__main__':
    unittest.main()
