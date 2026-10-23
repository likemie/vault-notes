import importlib.util
import sys
import unittest
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "vault_lint", Path(__file__).parents[1] / "scripts/vault_lint.py"
)
lint = importlib.util.module_from_spec(spec)
sys.modules["vault_lint"] = lint
spec.loader.exec_module(lint)

JOURNAL = Path("wiki/arguments/journal-articles/Journal/Argument_Author_2008a.md")
BOOK = Path("wiki/arguments/books/Book/Argument_Author_2008a.md")
ALIASES = {"author, 2008a"}


def self_aliases():
    data = {"type": "argument", "citation_aliases": ["Author, 2008a", "Author (2008a)"]}
    citations = {
        "Argument_Author_2008a": {
            "aliases": ["Author, 2008a", "Author (2008a)"],
            "citation_stem": "Author, 2008",
        },
        "Argument_Book": {
            "aliases": ["Editor, 2009a", "Editor (2009a)"],
            "citation_stem": "Editor, 2009",
        },
    }
    fm = 'part_of: "[[Argument_Book]]"\n'
    return lint.argument_self_parenthetical_aliases(JOURNAL, fm, data, citations)


def apply_self(text, drop_pages):
    def rewrite(group):
        result = lint.self_alias_rewrite(group, ALIASES, drop_pages=drop_pages)
        return None if result is None else result[0]

    updated, _ = lint._replace_parentheticals(text, rewrite)
    return updated


def apply_journal_pages(text):
    updated, _ = lint._replace_parentheticals(
        text, lambda group: "" if lint.is_journal_self_page_group(group) else None
    )
    return updated


class JournalSelfCitationTests(unittest.TestCase):
    def test_self_aliases_keep_year_suffix(self):
        aliases = self_aliases()
        self.assertIn("author, 2008a", aliases)
        self.assertIn("editor, 2009a", aliases)
        self.assertNotIn("author, 2008", aliases)
        self.assertNotIn("editor, 2009", aliases)

    def test_journal_path_requires_journal_article_fields(self):
        journal = {
            "type": "argument",
            "argument_kind": "journal-article",
            "subtype": "journal-article",
            "publication_type": "journal-article",
        }
        book = {"type": "argument", "subtype": "monograph", "publication_type": "book"}
        self.assertTrue(lint.is_journal_argument(JOURNAL, journal))
        self.assertFalse(lint.is_journal_argument(BOOK, journal))
        self.assertFalse(lint.is_journal_argument(JOURNAL, book))

    def test_journal_rewrite_drops_this_article_only(self):
        text = (
            "结论 (Author, 2008a, p. 4)。另见 (Author, 2008b, p. 12) 与 (Nye, 2004, p. 73)。"
            "保留 (Reardon, 2011, pp. 7–8)。无后缀 (Author, 2008, p. 4)。"
        )
        updated = apply_journal_pages(apply_self(text, drop_pages=True))
        self.assertEqual(
            updated,
            "结论。另见 (Author, 2008b, p. 12) 与 (Nye, 2004, p. 73)。"
            "保留 (Reardon, 2011, pp. 7–8)。无后缀 (Author, 2008, p. 4)。",
        )
        self.assertEqual(
            lint.self_alias_rewrite("(Author, 2008a, p. 4)", ALIASES, drop_pages=True),
            ("", "self"),
        )
        self.assertIsNone(lint.self_alias_rewrite("(Author, 2008b, p. 12)", ALIASES, drop_pages=True))
        self.assertIsNone(lint.self_alias_rewrite("(Nye, 2004, p. 73)", ALIASES, drop_pages=True))

    def test_journal_page_locators_drop_and_statistics_stay(self):
        text = "范围（pp. 3–4）。表格（pp. 3–4, Table 1）。显著（p=0.011）。比较 (p<0.05)。"
        self.assertTrue(lint.is_journal_self_page_group("（pp. 3–4）"))
        self.assertTrue(lint.is_journal_self_page_group("（pp. 3–4, Table 1）"))
        self.assertFalse(lint.is_journal_self_page_group("（p=0.011）"))
        self.assertFalse(lint.is_journal_self_page_group("(p<0.05)"))
        self.assertFalse(lint.is_journal_self_page_group("(Reardon, 2011, pp. 7–8)"))
        self.assertEqual(apply_journal_pages(text), "范围。表格。显著（p=0.011）。比较 (p<0.05)。")

    def test_book_self_cite_keeps_pages_and_sibling_citation(self):
        text = "结论 (Author, 2008a, p. 4)。另见 (Author, 2008b, p. 9)。"
        self.assertEqual(
            lint.self_alias_rewrite("(Author, 2008a, p. 4)", ALIASES, drop_pages=False),
            ("(p. 4)", "self"),
        )
        self.assertIsNone(lint.self_alias_rewrite("(Author, 2008b, p. 9)", ALIASES, drop_pages=False))
        self.assertEqual(apply_self(text, drop_pages=False), "结论 (p. 4)。另见 (Author, 2008b, p. 9)。")
        self.assertFalse(lint.is_journal_argument(BOOK, {"type": "argument", "subtype": "monograph", "publication_type": "book"}))


if __name__ == "__main__":
    unittest.main()
