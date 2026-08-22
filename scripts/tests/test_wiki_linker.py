import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "scripts"))

import wiki_linker  # noqa: E402


class PersonPrefixRegistryTests(unittest.TestCase):
    def setUp(self) -> None:
        entries = [
            wiki_linker.Entry(
                title="Alec Peterson",
                path="wiki/persons/uk/Alec Peterson.md",
                aliases=("Peterson, A. D. C.",),
                type="person",
            ),
            wiki_linker.Entry(
                title="Amelia Peterson",
                path="wiki/persons/us/Amelia Peterson.md",
                aliases=("Peterson, A.",),
                type="person",
            ),
            wiki_linker.Entry(
                title="Thomas Kuhn",
                path="wiki/persons/us/Thomas Kuhn.md",
                aliases=("Kuhn",),
                type="person",
            ),
            wiki_linker.Entry(
                title="Deanna Kuhn",
                path="wiki/persons/us/Deanna Kuhn.md",
                aliases=("Kuhn, D.",),
                type="person",
            ),
        ]
        self.terms, _, _ = wiki_linker.make_terms(entries)
        self.registry = wiki_linker.build_person_prefix_registry(self.terms)

    def link(self, text: str, already_linked: set[str] | None = None) -> tuple[str, int]:
        return wiki_linker.link_plain_text(
            text,
            self.terms,
            current_title="Current Page",
            already_linked=already_linked or set(),
            person_prefix_registry=self.registry,
        )

    def test_registry_records_cross_person_prefixes(self) -> None:
        pairs = {
            (item.shorter.text, item.shorter.target, item.longer.text, item.longer.target)
            for item in self.registry.conflicts
        }
        self.assertIn(
            ("Peterson, A.", "Amelia Peterson", "Peterson, A. D. C.", "Alec Peterson"),
            pairs,
        )
        self.assertIn(("Kuhn", "Thomas Kuhn", "Kuhn, D.", "Deanna Kuhn"), pairs)

    def test_longer_person_is_linked_when_first_seen(self) -> None:
        linked, count = self.link("Peterson, A. D. C.")
        self.assertEqual(linked, "[[Alec Peterson|Peterson, A. D. C.]]")
        self.assertEqual(count, 1)

    def test_longer_person_is_preserved_instead_of_falling_back(self) -> None:
        linked, count = self.link("Peterson, A. D. C.", {"Alec Peterson"})
        self.assertEqual(linked, "Peterson, A. D. C.")
        self.assertNotIn("Amelia Peterson", linked)
        self.assertEqual(count, 0)

    def test_shorter_person_still_links_when_it_is_the_complete_text(self) -> None:
        linked, count = self.link("Peterson, A.")
        self.assertEqual(linked, "[[Amelia Peterson|Peterson, A.]]")
        self.assertEqual(count, 1)

    def test_second_prefix_family_is_protected(self) -> None:
        linked, count = self.link("Kuhn, D.", {"Deanna Kuhn"})
        self.assertEqual(linked, "Kuhn, D.")
        self.assertNotIn("Thomas Kuhn", linked)
        self.assertEqual(count, 0)


if __name__ == "__main__":
    unittest.main()
