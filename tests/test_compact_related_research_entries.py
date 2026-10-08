from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import vault_lint as lint
from compact_related_research_entries import compact_entry, compact_related_research_entries


class CompactEntryTests(unittest.TestCase):
    def test_keeps_first_complete_sentence(self) -> None:
        entry = "[[Argument_A|Author (2025)]] — " + "甲" * 80 + "。" + "乙" * 100 + "。"

        result = compact_entry(entry)

        self.assertTrue(result.endswith("。"))
        self.assertNotIn("乙", result)
        self.assertLessEqual(len(lint.markdown_visible_text(result)), 150)

    def test_closes_at_natural_clause_boundary(self) -> None:
        entry = "[[Argument_A|Author (2025)]] — " + "甲" * 100 + "，" + "乙" * 100 + "。"

        result = compact_entry(entry)

        self.assertTrue(result.endswith("。"))
        self.assertNotIn("乙", result)
        self.assertLessEqual(len(lint.markdown_visible_text(result)), 150)

    def test_never_splits_wikilink(self) -> None:
        entry = "[[Argument_A|Author (2025)]] — " + "甲" * 120 + "[[Concept|概念]]" + "乙" * 30

        result = compact_entry(entry)

        self.assertEqual(result.count("[["), result.count("]]"))
        self.assertIn("[[Argument_A|Author (2025)]]", result)
        self.assertLessEqual(len(lint.markdown_visible_text(result)), 150)

    def test_document_fix_is_idempotent(self) -> None:
        text = (
            "---\nupdated: 2026-01-01\n---\n"
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            "> - [[Argument_A|Author (2025)]] — " + "甲" * 160 + "。\n"
        )

        once, first_count = compact_related_research_entries(text, updated_date="2026-10-08")
        twice, second_count = compact_related_research_entries(once, updated_date="2026-10-08")

        self.assertEqual(1, first_count)
        self.assertEqual(0, second_count)
        self.assertEqual(once, twice)


if __name__ == "__main__":
    unittest.main()
