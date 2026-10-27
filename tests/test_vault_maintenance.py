"""Regression checks for shared maintenance and related-update persistence."""
import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
import related_update as related
import vault_index as index
import vaultlib


class MaintenanceTests(unittest.TestCase):
    def test_generated_fields_keep_anchor_order_and_remove_old_block(self):
        raw = 'type: fact\nsubtype: event\nfact_region:\n  - old\nregion: asia\nsummary: "keep"\n'
        result = vaultlib.upsert_generated_fields(
            raw, {'fact_region'}, ['fact_region: "asia"'],
            stop_after=('region',), after=('subtype',), fallback_after=('type',))
        self.assertEqual(result, 'type: fact\nsubtype: event\nregion: asia\nfact_region: "asia"\nsummary: "keep"\n')

    def test_person_uses_first_subtype_or_nationality_anchor(self):
        result = vaultlib.upsert_generated_fields(
            'type: person\nsubtype: school\nnationality: global\n', set(), ['person_region: "global"'],
            stop_after=('nationality', 'subtype'), fallback_after=('type',))
        self.assertEqual(result.splitlines()[2], 'person_region: "global"')

    def test_dry_run_and_check_never_write(self):
        for dry_run, check in ((True, False), (False, True)):
            with self.subTest(dry_run=dry_run, check=check), patch.object(index, 'write_md') as write:
                self.assertTrue(index.write_base_fields(
                    Path('demo.md'), 'old', 'type: concept\n', 'body',
                    dry_run=dry_run, check=check, update_date=True))
                write.assert_not_called()

    def test_argument_keeps_existing_updated_date(self):
        with patch.object(index, 'write_md') as write:
            index.write_base_fields(Path('demo.md'), 'old', 'type: argument\nupdated: 2000-01-01\n',
                                    'body', dry_run=False, check=False, update_date=False)
            self.assertIn('updated: 2000-01-01', write.call_args.args[1])
        with patch.object(index, 'write_md') as write:
            index.write_base_fields(Path('demo.md'), 'old', 'type: concept\nupdated: 2000-01-01\n',
                                    'body', dry_run=False, check=False, update_date=True)
            self.assertIn('updated: ' + index.datetime.date.today().isoformat(), write.call_args.args[1])

    def test_atomic_failure_preserves_previous_state(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'state.json'
            related.write_json(path, {'status': 'pending'})
            before = path.read_bytes()
            with patch.object(Path, 'replace', side_effect=OSError('replace failed')):
                with self.assertRaises(OSError):
                    related.write_json(path, {'status': 'done'})
            self.assertEqual(path.read_bytes(), before)
            self.assertEqual(related.read_json(path), {'status': 'pending'})

    def test_required_json_never_substitutes_default(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'state.json'
            self.assertEqual(vaultlib.load_json(path, {}), {})
            with self.assertRaises(FileNotFoundError):
                related.read_json(path)
            path.write_text('{bad json', encoding='utf-8')
            with self.assertRaises(ValueError):
                related.read_json(path)

    def test_shared_frontmatter_preserves_body_and_accepts_eof(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'note.md'
            path.write_text('---\ntype: concept\n---\n\nBody\n', encoding='utf-8')
            self.assertEqual(related.read_note(path), ({'type': 'concept'}, '\nBody\n'))
            path.write_text('---\ntype: concept\n---', encoding='utf-8')
            self.assertEqual(related.read_note(path), ({'type': 'concept'}, ''))
            path.write_text('missing frontmatter', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, '缺少 frontmatter'):
                related.read_note(path)

    def test_target_handles_alias_heading_and_block(self):
        for value in ('[[wiki/concepts/Example.md#Heading\\|Alias]]',
                      '[[wiki/concepts/Example.md^block|Alias]]', 'wiki/concepts/Example.md'):
            self.assertEqual(related.target(value), 'wiki/concepts/Example')

    def test_accept_stops_after_one_batch_and_keeps_failure_pending(self):
        for failure in (False, True):
            with self.subTest(failure=failure), tempfile.TemporaryDirectory() as directory:
                job = Path(directory)
                batches = [{'number': 1, 'status': 'pending', 'entries': [{'path': 'A'}]},
                           {'number': 2, 'status': 'pending', 'entries': [{'path': 'B'}]}]
                state = {'batches': batches}
                receipt = job / 'batch-001' / 'result.json'
                related.write_json(receipt, {'items': ['补充']})
                with (patch.object(related, 'vault_lock', contextlib.nullcontext),
                      patch.object(related, 'load_job', return_value=(job, state)),
                      patch.object(related, 'check_argument'),
                      patch.object(related, 'gates', side_effect=ValueError('gate failed') if failure else None) as gate,
                      patch.object(related, 'emit_task') as emit,
                      contextlib.redirect_stdout(io.StringIO())):
                    if failure:
                        with self.assertRaisesRegex(ValueError, 'gate failed'):
                            related.accept_job(SimpleNamespace(job=job))
                        self.assertFalse((job / 'state.json').exists())
                    else:
                        related.accept_job(SimpleNamespace(job=job))
                        self.assertEqual(related.read_json(job / 'state.json')['batches'][0]['status'], 'done')
                    gate.assert_called_once_with()
                    emit.assert_not_called()
                self.assertEqual(batches[0]['status'], 'pending' if failure else 'done')
                self.assertEqual(batches[1]['status'], 'pending')


if __name__ == '__main__':
    unittest.main()
