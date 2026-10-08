from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import vault_lint as lint


BOOK_INDEX = {
    "Argument_Book": {
        "title": "Argument_Book",
        "type": "argument",
        "path": "wiki/arguments/books/Book/Argument_Book.md",
    },
    "Argument_Book_Ch11": {
        "title": "Argument_Book_Ch11",
        "type": "argument",
        "path": "wiki/arguments/books/Book/Argument_Book_Ch11.md",
    },
    "Argument_Book_Ch12": {
        "title": "Argument_Book_Ch12",
        "type": "argument",
        "path": "wiki/arguments/books/Book/Argument_Book_Ch12.md",
    },
    "Argument_Other_Book": {
        "title": "Argument_Other_Book",
        "type": "argument",
        "path": "wiki/arguments/books/Other/Argument_Other_Book.md",
    },
}


class RelatedResearchBookTests(unittest.TestCase):
    def lint(self, body: str) -> list[lint.Issue]:
        issues: list[lint.Issue] = []
        lint.check_related_research_duplicate_books(
            ROOT / "wiki" / "concepts" / "Example.md",
            body,
            BOOK_INDEX,
            issues,
        )
        return issues

    def test_different_chapters_of_one_book_warn_on_second_entry(self) -> None:
        issues = self.lint(
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            "> - [[Argument_Book_Ch11|Author (2025, Ch. 11)]] — 第一项。\n"
            "> - [[Argument_Book_Ch12|Author (2025, Ch. 12)]] — 第二项。\n"
        )

        self.assertEqual(["RELATED_RESEARCH_DUPLICATE_BOOK"], [issue.code for issue in issues])
        self.assertEqual(5, issues[0].line)

    def test_chapter_links_inside_one_book_entry_are_allowed(self) -> None:
        issues = self.lint(
            "## 相关研究\n\n"
            "> [!evidence-grid-a] [[Correlational Research|相关研究]]索引\n"
            "> - [[Argument_Book|Author (2025)]] — 包括 "
            "[[Argument_Book_Ch11|Ch. 11]] 与 [[Argument_Book_Ch12|Ch. 12]]。\n"
            "> - [[Argument_Other_Book|Other (2024)]] — 另一项。\n"
        )

        self.assertEqual([], issues)

    def test_nested_stance_links_are_not_top_level_sources(self) -> None:
        issues = self.lint(
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            "> - [[Argument_Book_Ch11|Author (2025, Ch. 11)]] — 第一项。\n"
            "> > - 补充立场。[[Argument_Book_Ch12|(Author, 2025)]]\n"
        )

        self.assertEqual([], issues)

    def test_same_book_outside_related_research_index_is_ignored(self) -> None:
        issues = self.lint(
            "## 其他\n\n"
            "> [!evidence-grid-a] 证据索引\n"
            "> - [[Argument_Book_Ch11|Author (2025, Ch. 11)]] — 第一项。\n"
            "> - [[Argument_Book_Ch12|Author (2025, Ch. 12)]] — 第二项。\n"
        )

        self.assertEqual([], issues)


if __name__ == "__main__":
    unittest.main()
