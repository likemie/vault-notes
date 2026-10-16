from __future__ import annotations

import contextlib
import io
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import check_vault as checks


class ChangeSelectionTests(unittest.TestCase):
    def test_clean_checkout_checks_committed_changes_including_unicode_rename(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)

            def git(*args):
                return subprocess.check_output(["git", *args], cwd=root, stderr=subprocess.DEVNULL).decode().strip()

            git("init")
            git("config", "user.email", "test@example.invalid")
            git("config", "user.name", "Test")
            (root / "wiki").mkdir()
            (root / "output").mkdir()
            (root / "wiki/Old.md").write_text("old\n")
            (root / "wiki/Deleted.md").write_text("delete\n")
            git("add", ".")
            git("commit", "-m", "base")
            base = git("rev-parse", "HEAD")
            git("mv", "wiki/Old.md", "wiki/Håkansson note.md")
            (root / "wiki/Deleted.md").unlink()
            (root / "wiki/New.md").write_text("new\n")
            (root / "output/Draft.md").write_text("draft\n")
            git("add", "-A")
            git("commit", "-m", "change")
            self.assertEqual("", git("status", "--porcelain"))
            with patch.object(checks, "ROOT", root):
                self.assertEqual(["wiki/Håkansson note.md", "wiki/New.md"], checks.changed_markdown(base))
                self.assertEqual([], checks.changed_markdown(None))
                self.assertEqual(["wiki/Håkansson note.md", "wiki/New.md"], checks.changed_markdown("0" * 40))
                (root / "wiki/Untracked.md").write_text("new\n")
                (root / "wiki/New.md").write_text("modified\n")
                self.assertEqual(["wiki/New.md", "wiki/Untracked.md"], checks.changed_markdown(None))


class ValidationFailureTests(unittest.TestCase):
    def test_failure_stops_remaining_checks(self):
        with patch.object(checks, "changed_markdown", return_value=[]), \
             patch.object(checks.subprocess, "run", return_value=subprocess.CompletedProcess([], 1)) as run, \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(1, checks.run_checks())
            self.assertEqual(1, run.call_count)

    def test_selected_paths_are_passed_to_lint_without_shell_splitting(self):
        paths = ["wiki/concepts/Two words.md", "sources/Håkansson.md"]
        with patch.object(checks, "changed_markdown", return_value=paths), \
             patch.object(checks.subprocess, "run", return_value=subprocess.CompletedProcess([], 0)) as run, \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(0, checks.run_checks("base"))
            self.assertEqual(5, run.call_count)
            self.assertEqual([sys.executable, "-B", "scripts/vault_lint.py", "--path", paths[0], "--path", paths[1]], run.call_args.args[0])


if __name__ == "__main__":
    unittest.main()
