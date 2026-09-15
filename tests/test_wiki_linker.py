from __future__ import annotations

import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import wiki_linker as linker


def ordered_terms(*terms: linker.Term) -> list[linker.Term]:
    return sorted(terms, key=lambda term: len(term.text), reverse=True)


class TermMatcherTests(unittest.TestCase):
    def test_trie_matches_reference_semantics_and_order(self) -> None:
        terms = ordered_terms(
            linker.Term("教育研究", "Education Research", True, "concept"),
            linker.Term("教育", "Education", True, "concept"),
            linker.Term("Research", "Research", False, "concept"),
            linker.Term("US", "United States", True, "fact"),
        )
        matcher = linker.TermMatcher(terms)
        text = "教育研究 research RESEARCH US us"

        for start in range(len(text)):
            expected = [term for term in terms if linker.match_term_at(text, start, term.text)]
            self.assertEqual(expected, matcher.matches_at(text, start))

    def test_longest_cjk_match_is_preserved(self) -> None:
        terms = ordered_terms(
            linker.Term("教育研究", "Education Research", True, "concept"),
            linker.Term("教育", "Education", True, "concept"),
            linker.Term("研究", "Research", True, "concept"),
        )
        result, additions = linker.link_plain_text(
            "教育研究",
            terms,
            "Current Page",
            set(),
            term_matcher=linker.TermMatcher(terms),
        )

        self.assertEqual("[[Education Research|教育研究]]", result)
        self.assertEqual(1, additions)

    def test_person_prefix_does_not_capture_known_longer_name(self) -> None:
        terms = ordered_terms(
            linker.Term("Peterson, A. D. C.", "Longer Person", True, "person"),
            linker.Term("Peterson, A.", "Shorter Person", True, "person"),
        )
        registry = linker.build_person_prefix_registry(terms)
        result, additions = linker.link_plain_text(
            "Peterson, A. D. C.",
            terms,
            "Current Page",
            {"Longer Person"},
            term_matcher=linker.TermMatcher(terms),
            person_prefix_registry=registry,
        )

        self.assertEqual("Peterson, A. D. C.", result)
        self.assertEqual(0, additions)


class MarkdownProtectionTests(unittest.TestCase):
    def setUp(self) -> None:
        self.terms = ordered_terms(linker.Term("教育研究", "Education Research", True, "concept"))
        self.matcher = linker.TermMatcher(self.terms)

    def test_protected_spans_remain_unchanged(self) -> None:
        text = "# 教育研究\n正文教育研究。`教育研究`。[[Existing|教育研究]]\n"
        result, additions = linker.link_section(
            text,
            self.terms,
            "Current Page",
            set(),
            term_matcher=self.matcher,
        )

        self.assertEqual(
            "# 教育研究\n正文[[Education Research|教育研究]]。`教育研究`。[[Existing|教育研究]]\n",
            result,
        )
        self.assertEqual(1, additions)

    def test_table_alias_pipe_is_escaped(self) -> None:
        result, additions = linker.link_table_row(
            "| 术语 | 教育研究 |\n",
            self.terms,
            "Current Page",
            set(),
            self.matcher,
        )

        self.assertEqual("| 术语 | [[Education Research\\|教育研究]] |\n", result)
        self.assertEqual(1, additions)


if __name__ == "__main__":
    unittest.main()
