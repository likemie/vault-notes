from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from merge_related_research_books import merge_duplicate_book_entries


BOOK_INDEX = {
    "Argument_Book_Ch01": {
        "title": "Argument_Book_Ch01",
        "type": "argument",
        "path": "wiki/arguments/books/Book/Argument_Book_Ch01.md",
        "book_subtype": "monograph",
    },
    "Argument_Book_Ch02": {
        "title": "Argument_Book_Ch02",
        "type": "argument",
        "path": "wiki/arguments/books/Book/Argument_Book_Ch02.md",
        "book_subtype": "monograph",
    },
    "Argument_Other": {
        "title": "Argument_Other",
        "type": "argument",
        "path": "wiki/arguments/books/Other/Argument_Other.md",
        "book_subtype": "monograph",
    },
}

EDITED_VOLUME_INDEX = {
    "Argument_Volume_Ch01": {
        "title": "Argument_Volume_Ch01",
        "type": "argument",
        "path": "wiki/arguments/books/Volume/Argument_Volume_Ch01.md",
        "book_subtype": "edited-volume",
    },
    "Argument_Volume_Ch02": {
        "title": "Argument_Volume_Ch02",
        "type": "argument",
        "path": "wiki/arguments/books/Volume/Argument_Volume_Ch02.md",
        "book_subtype": "edited-volume",
    },
}


class MergeRelatedResearchBooksTests(unittest.TestCase):
    def test_merges_same_book_and_preserves_other_entries(self) -> None:
        text = (
            "---\nupdated: 2026-01-01\n---\n"
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            "> - [[Argument_Book_Ch01|Author (2025, Ch. 1)]] — 第一章。\n"
            "> - [[Argument_Other|Other (2024)]] — 另一本书。\n"
            "> - [[Argument_Book_Ch02|Author (2025, Ch. 2)]] — 第二章。\n"
        )

        result, count = merge_duplicate_book_entries(
            text,
            BOOK_INDEX,
            updated_date="2026-10-08",
        )

        self.assertEqual(1, count)
        self.assertIn("updated: 2026-10-08", result)
        self.assertIn(
            "> - [[Argument_Book_Ch01|Author (2025, Ch. 1)]] — 第一章。 "
            "[[Argument_Book_Ch02|Author (2025, Ch. 2)]] — 第二章。",
            result,
        )
        self.assertIn("> - [[Argument_Other|Other (2024)]] — 另一本书。", result)

    def test_description_chapter_links_do_not_trigger_another_merge(self) -> None:
        text = (
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            "> - [[Argument_Book_Ch01|Author (2025)]] — 包括 "
            "[[Argument_Book_Ch02|第二章]]。\n"
        )

        result, count = merge_duplicate_book_entries(text, BOOK_INDEX)

        self.assertEqual(0, count)
        self.assertEqual(text, result)

    def test_fix_is_idempotent(self) -> None:
        text = (
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            "> - [[Argument_Book_Ch01|Author (2025, Ch. 1)]] — 第一章。\n"
            "> - [[Argument_Book_Ch02|Author (2025, Ch. 2)]] — 第二章。\n"
        )

        once, first_count = merge_duplicate_book_entries(text, BOOK_INDEX)
        twice, second_count = merge_duplicate_book_entries(once, BOOK_INDEX)

        self.assertEqual(1, first_count)
        self.assertEqual(0, second_count)
        self.assertEqual(once, twice)

    def test_edited_volume_chapters_are_not_merged(self) -> None:
        text = (
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            "> - [[Argument_Volume_Ch01|Author A (2025)]] — 第一章。\n"
            "> - [[Argument_Volume_Ch02|Author B (2025)]] — 第二章。\n"
        )

        result, count = merge_duplicate_book_entries(text, EDITED_VOLUME_INDEX)

        self.assertEqual(0, count)
        self.assertEqual(text, result)


if __name__ == "__main__":
    unittest.main()
