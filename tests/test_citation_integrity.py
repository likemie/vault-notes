from __future__ import annotations

import contextlib
import io
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import citation_index as index
import citation_linker as linker
import vault_lint as lint


class CitationIntegrityTests(unittest.TestCase):
    path = ROOT / "wiki/arguments/journal-articles/Test/Argument_Test.md"

    def metadata_issues(self, citation: str, extra: str = "") -> list[lint.Issue]:
        text = ('---\ntitle: Argument_Test\ntype: argument\n'
                'authors: ["Author, A."]\nyear: 2025\n'
                'citation_aliases: ["Author, 2025", "Author (2025)"]\n'
                + citation + extra + '---\n')
        issues = []
        lint.check_frontmatter(self.path, text, {}, issues)
        return issues

    def test_missing_null_and_blank_full_citations_fail_lint(self):
        for field in ('', 'citation:\n', 'citation: ""\n', 'citation: "   "\n'):
            with self.subTest(field=field):
                found = [i for i in self.metadata_issues(field) if i.code == "ARGUMENT_FULL_CITATION_MISSING"]
                self.assertEqual(["ERROR"], [i.severity for i in found])

    def test_complete_citation_passes(self):
        self.assertNotIn("ARGUMENT_FULL_CITATION_MISSING", [i.code for i in self.metadata_issues('citation: "Author (2025). Title."\n')])

    def test_inherited_chapter_and_overview_allow_empty_citation(self):
        for extra in ('subtype: monograph\npublication_type: book-chapter\npart_of: "[[Argument_Book]]"\n',
                      'subtype: textbook\npublication_type: book-chapter\npart_of: "[[Argument_Book]]"\n',
                      'subtype: edited-volume-overview\n'):
            with self.subTest(extra=extra):
                self.assertNotIn("ARGUMENT_FULL_CITATION_MISSING", [i.code for i in self.metadata_issues('citation: ""\n', extra)])

    def test_independent_edited_volume_chapter_requires_citation(self):
        issues = self.metadata_issues('citation: ""\n', 'subtype: edited-volume\npublication_type: book-chapter\npart_of: "[[Argument_Book]]"\n')
        self.assertIn("ARGUMENT_FULL_CITATION_MISSING", [i.code for i in issues])

    def test_index_check_rejects_empty_citation(self):
        item = index.ArgumentCitation(self.path, "Argument_Test", ["Author, A."], "2025", "", "", "", "en", ["Author, 2025"], ["Author, 2025"])
        with contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(1, index.check([item]))
            item.citation = "Author (2025). Title."
            self.assertEqual(0, index.check([item]))

    def test_plain_text_source_is_flagged_even_in_draft(self):
        for status in ("draft", "active"):
            issues = []
            lint.check_sources_section(self.path, "---\ntype: argument\n---\n## 来源\n\n- Author_2025\n", {"type": "argument", "status": status}, issues)
            self.assertIn("ARGUMENT_SOURCE_SECTION_EMPTY", [i.code for i in issues])


class TwoAuthorCitationTests(unittest.TestCase):
    target = {"Argument_Test": {"aliases": ["Hofer & Pintrich, 1997", "Hofer & Pintrich (1997)"]}}
    lookup = {key: {"argument": "Argument_Test"} for key in ("Hofer & Pintrich, 1997", "Hofer & Pintrich (1997)")}

    def test_lint_and_fix_preserve_valid_forms(self):
        for display in ("Hofer and Pintrich (1997, p. 12)", "(Hofer & Pintrich, 1997, p. 12)", "Hofer & Pintrich, 1997"):
            body = f"[[Argument_Test|{display}]]"
            issues = []
            lint.check_citation_links(ROOT / "wiki/concepts/Example.md", body, {"type": "concept"}, self.target, issues)
            self.assertEqual([], [i for i in issues if i.code in {"CITATION_ENGLISH_AND", "CITATION_LINK_TARGET_MISMATCH"}])
            self.assertEqual((body, 0), lint.fix_body_spans(body, self.target))

    def test_fix_wrong_forms_in_raw_and_linked_citations_is_idempotent(self):
        for before, after in (("Hofer & Pintrich (1997)", "Hofer and Pintrich (1997)"),
                              ("(Hofer and Pintrich, 1997)", "(Hofer & Pintrich, 1997)")):
            for linked in (False, True):
                raw = f"[[Argument_Test|{before}]]" if linked else before
                expected = f"[[Argument_Test|{after}]]" if linked else after
                fixed, count = lint.fix_body_spans(raw, self.target)
                self.assertEqual(expected, fixed)
                self.assertEqual(1, count)
                self.assertEqual((expected, 0), lint.fix_body_spans(fixed, self.target))

    def test_narrative_linker_uses_and_and_preserves_locator(self):
        for raw in ("Hofer and Pintrich (1997, p. 12)", "Hofer & Pintrich (1997, p. 12)"):
            actual = linker.link_narrative(raw, self.lookup, {"linked_narrative": 0}, [])
            self.assertEqual("[[Argument_Test|Hofer and Pintrich (1997, p. 12)]]", actual)

    def test_linked_author_narrative_uses_and(self):
        actual = linker.link_wikilink_narrative("[[Hofer|Hofer & Pintrich]] (1997)", self.lookup, {"linked_narrative": 0}, [])
        self.assertEqual("[[Argument_Test|Hofer and Pintrich (1997)]]", actual)

    def test_parenthetical_linker_uses_ampersand(self):
        actual = linker.link_parenthetical_group("Hofer and Pintrich, 1997", self.lookup, {"linked_parenthetical": 0}, [], "(", ")")
        self.assertIn("[[Argument_Test|Hofer & Pintrich, 1997]]", actual)

    def test_conjunction_does_not_split_names_ending_in_and(self):
        for author in ("Brand Smith", "Bertrand Russell"):
            display = f"{author} (1997)"
            self.assertEqual(display, lint.fix_english_author_and(display))
            self.assertEqual(author, linker.normalize_display_author(author, narrative=True))
            self.assertEqual(display, linker.normalize_citation_alias(display))

    def test_chinese_and_code_examples_unchanged(self):
        for body in ("林德布拉德和波普凯维茨 (2004)", "`Hofer & Pintrich (1997)`", "```\nHofer & Pintrich (1997)\n```", "## 来源\n\nHofer & Pintrich (1997)\n"):
            self.assertEqual((body, 0), lint.fix_body_spans(body, self.target))


if __name__ == "__main__":
    unittest.main()
