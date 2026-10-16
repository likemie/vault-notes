from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import vault_index


class ArgumentRatingTests(unittest.TestCase):
    def test_star_and_diamond_boundaries(self):
        cases = {
            0: (0, "☆"), 9: (0, "☆"),
            10: (1, "⭐"), 19: (1, "⭐"),
            20: (2, "⭐⭐"), 29: (2, "⭐⭐"),
            30: (3, "💎"), 39: (3, "💎"),
            40: (4, "💎⭐"), 49: (4, "💎⭐"),
            50: (5, "💎⭐⭐"), 59: (5, "💎⭐⭐"),
            60: (6, "💎💎"), 99: (9, "💎💎💎"),
            100: (10, "💎💎💎⭐"), 300: (30, "💎" * 10),
        }
        for count, expected in cases.items():
            with self.subTest(count=count):
                self.assertEqual(vault_index.argument_stars_for(count), expected)

    def test_generated_fields_include_instruments_and_are_idempotent(self):
        related = "\n".join(f'  - "[[Concept {i}]]"' for i in range(29))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "Argument_Test_2026_Journal.md"
            path.write_text(
                '---\ntype: argument\npublication_type: journal-article\n'
                f'related_concepts:\n{related}\n'
                'related_instruments:\n  - "[[Test Instrument]]"\n'
                'argument_related_count: 999\nargument_related_level: 99\n'
                'argument_related_stars: "old"\n---\n\nBody.\n',
                encoding="utf-8",
            )
            changed, summary = vault_index.update_argument_base_fields(path, False, False)
            self.assertTrue(changed)
            self.assertEqual(summary, (30, "💎"))
            meta = vault_index.parse_frontmatter(path.read_text(encoding="utf-8"))
            self.assertEqual(int(meta["argument_related_count"]), 30)
            self.assertEqual(int(meta["argument_related_level"]), 3)
            self.assertEqual(meta["argument_related_stars"], "💎")
            self.assertFalse(vault_index.update_argument_base_fields(path, False, False)[0])


if __name__ == "__main__":
    unittest.main()
