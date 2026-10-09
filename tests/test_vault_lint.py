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
        "book_subtype": "monograph",
    },
    "Argument_Book_Ch11": {
        "title": "Argument_Book_Ch11",
        "type": "argument",
        "path": "wiki/arguments/books/Book/Argument_Book_Ch11.md",
        "book_subtype": "monograph",
    },
    "Argument_Book_Ch12": {
        "title": "Argument_Book_Ch12",
        "type": "argument",
        "path": "wiki/arguments/books/Book/Argument_Book_Ch12.md",
        "book_subtype": "monograph",
    },
    "Argument_Other_Book": {
        "title": "Argument_Other_Book",
        "type": "argument",
        "path": "wiki/arguments/books/Other/Argument_Other_Book.md",
        "book_subtype": "monograph",
    },
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

    def test_nested_callout_does_not_end_parent_index(self) -> None:
        issues = self.lint(
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            "> - [[Argument_Book_Ch11|Author (2025, Ch. 11)]] — 第一项。\n"
            "> > [!axis] 补充讨论\n"
            "> > 正文。\n"
            "> - [[Argument_Book_Ch12|Author (2025, Ch. 12)]] — 第二项。\n"
        )

        self.assertEqual(["RELATED_RESEARCH_DUPLICATE_BOOK"], [issue.code for issue in issues])

    def test_same_book_outside_related_research_index_is_ignored(self) -> None:
        issues = self.lint(
            "## 其他\n\n"
            "> [!evidence-grid-a] 证据索引\n"
            "> - [[Argument_Book_Ch11|Author (2025, Ch. 11)]] — 第一项。\n"
            "> - [[Argument_Book_Ch12|Author (2025, Ch. 12)]] — 第二项。\n"
        )

        self.assertEqual([], issues)

    def test_edited_volume_chapters_remain_independent_entries(self) -> None:
        issues = self.lint(
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            "> - [[Argument_Volume_Ch01|Author A (2025)]] — 第一章。\n"
            "> - [[Argument_Volume_Ch02|Author B (2025)]] — 第二章。\n"
        )

        self.assertEqual([], issues)


class RelatedResearchEntryLengthTests(unittest.TestCase):
    def lint(self, entry: str) -> list[lint.Issue]:
        issues: list[lint.Issue] = []
        text = (
            "## 相关研究\n\n"
            "> [!evidence-grid-a] 相关研究索引\n"
            f"> - {entry}\n"
        )
        lint.check_related_research_entry_length(
            ROOT / "wiki" / "concepts" / "Example.md",
            text,
            issues,
        )
        return issues

    def test_exactly_150_visible_characters_is_allowed(self) -> None:
        issues = self.lint("中" * 150)

        self.assertEqual([], issues)

    def test_151_visible_characters_warns(self) -> None:
        issues = self.lint("中" * 151)

        self.assertEqual(["RELATED_RESEARCH_ENTRY_TOO_LONG"], [issue.code for issue in issues])
        self.assertIn("151", issues[0].message)

    def test_wikilink_target_and_markdown_marks_are_not_visible(self) -> None:
        visible = lint.markdown_visible_text(
            "**[[Argument_A_Very_Long_Internal_Target|Author (2025)]]** — 结论。"
        )

        self.assertEqual("Author (2025) — 结论。", visible)


class AxisCalloutTests(unittest.TestCase):
    def lint(self, body: str) -> list[lint.Issue]:
        issues: list[lint.Issue] = []
        lint.check_axis_callouts(
            ROOT / "wiki" / "concepts" / "Example.md",
            body,
            issues,
        )
        return issues

    def test_bad_nested_blank_separator_is_an_error(self) -> None:
        body = (
            "> [!debates] 学术争议\n"
            ">\n"
            "> > [!axis] 第一项\n"
            "> > 正文。\n"
            "> >\n"
            "> > [!axis] 第二项\n"
            "> > 正文。\n"
        )

        issues = self.lint(body)

        self.assertEqual(["AXIS_SIBLING_SEPARATOR"], [issue.code for issue in issues])
        self.assertEqual(5, issues[0].line)

    def test_single_outer_quote_separator_is_valid(self) -> None:
        body = (
            "> [!debates] 学术争议\n"
            ">\n"
            "> > [!axis] 第一项\n"
            "> > 正文。\n"
            ">\n"
            "> > [!axis] 第二项\n"
            "> > 正文。\n"
        )

        self.assertEqual([], self.lint(body))

    def test_axis_at_wrong_quote_depth_is_an_error(self) -> None:
        issues = self.lint("> [!axis] 错误层级\n")

        self.assertEqual(["AXIS_NESTING"], [issue.code for issue in issues])

    def test_fenced_example_is_ignored(self) -> None:
        body = "```markdown\n> >\n> > [!axis] 示例\n```\n"

        self.assertEqual([], self.lint(body))

    def test_fix_changes_only_the_bad_separator(self) -> None:
        body = (
            "> [!debates] 学术争议\n"
            ">\n"
            "> > [!axis] 第一项\n"
            "> > 正文。\n"
            "> >\n"
            "> > [!axis] 第二项\n"
        )

        fixed, count = lint.fix_axis_callouts(body)

        self.assertEqual(1, count)
        self.assertEqual(
            body.replace("> >\n> > [!axis] 第二项", ">\n> > [!axis] 第二项"),
            fixed,
        )

    def test_fix_normalizes_axis_quote_depth(self) -> None:
        body = (
            "> [!debates] 学术争议\n"
            ">\n"
            "> > > [!axis] 多缩进一层\n"
            "> > 正文。\n"
        )

        fixed, count = lint.fix_axis_callouts(body)

        self.assertEqual(1, count)
        self.assertEqual(body.replace("> > > [!axis]", "> > [!axis]"), fixed)

    def test_fix_rescans_separator_after_normalizing_depth(self) -> None:
        body = (
            "> [!debates] 学术争议\n"
            ">\n"
            "> > [!axis] 第一项\n"
            "> > 正文。\n"
            "> >\n"
            "> > > [!axis] 第二项\n"
            "> > 正文。\n"
        )

        fixed, count = lint.fix_axis_callouts(body)
        issues = self.lint(fixed)

        self.assertEqual(2, count)
        self.assertEqual([], issues)
        self.assertIn(">\n> > [!axis] 第二项", fixed)

if __name__ == "__main__":
    unittest.main()
