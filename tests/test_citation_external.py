import importlib.util
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).parents[1]
SCRIPTS = ROOT / "scripts"


def load(name: str):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module


external = load("citation_external")
lint = load("vault_lint")


SNIPPET = """---
title: Demo
---

正文 [[Argument_Nye_2004|Nye, 2004]] 已入库。
未入库 (Nye, 2004, p. 73) 与 Li (2012)。
Figure (2019) 不是文献。
（王和李，2020）。
In Smith (2018) 与 The World Bank (2017)。

> [!metax]
> (Hidden, 1999)

## 来源

(Sourceonly, 1998)
"""


class CitationExternalTests(unittest.TestCase):
    def test_comma_key_normalizes_narrative_and_conjunction(self):
        self.assertEqual(external.comma_key("Smith and Jones (2020a)"), "Smith & Jones, 2020a")
        self.assertEqual(external.comma_key("Smith & Jones, 2020"), "Smith & Jones, 2020")

    def test_choose_author_keeps_multiword_name_and_drops_leading_word(self):
        self.assertEqual(external.choose_author("In Smith"), "Smith")
        self.assertEqual(external.choose_author("The World Bank"), "World Bank")
        self.assertEqual(external.choose_author("共同构成 Li"), "Li")
        self.assertEqual(external.choose_author("结论见李明"), "")
        self.assertEqual(external.choose_author("李明"), "李明")
        self.assertEqual(external.choose_author("在卡普与扎米斯卡"), "卡普与扎米斯卡")
        self.assertEqual(external.choose_author("对哈蒂"), "哈蒂")
        self.assertEqual(external.choose_author("第七届"), "")
        self.assertEqual(external.choose_author("同上"), "")
        self.assertEqual(external.choose_author("作者甲和作者乙"), "作者甲和作者乙")

    def test_extract_skips_links_metax_sources_and_labels(self):
        keys = [key for key, _offset in external.first_sightings(SNIPPET)]
        self.assertIn("Nye, 2004", keys)
        self.assertIn("Li, 2012", keys)
        self.assertIn("王和李, 2020", keys)
        self.assertIn("Smith, 2018", keys)
        self.assertIn("World Bank, 2017", keys)
        self.assertNotIn("Figure, 2019", keys)
        self.assertNotIn("Hidden, 1999", keys)
        self.assertNotIn("Sourceonly, 1998", keys)

    def test_suffixes_follow_title_sort_and_lone_letter_stays_unsuffixed(self):
        saved = {
            "Smith, 2020b": {"doi": "", "isbn": "", "title": "Alpha paper", "seen_in": []},
            "Smith, 2020a": {"doi": "", "isbn": "", "title": "Beta paper", "seen_in": []},
        }
        sightings = {
            "Smith, 2020b": ["wiki/a.md"],
            "Smith, 2020a": ["wiki/b.md"],
        }
        rows, generated = external.assemble(saved, sightings, [])
        self.assertEqual(set(rows), {"Smith, 2020a", "Smith, 2020b"})
        alpha = generated["items"]["Smith, 2020a"]
        beta = generated["items"]["Smith, 2020b"]
        self.assertEqual(alpha["identity_keys"], ["Smith, 2020b"])
        self.assertEqual(alpha["title"], "Alpha paper")
        self.assertEqual(beta["identity_keys"], ["Smith, 2020a"])
        self.assertEqual(generated["by_identity"]["Smith, 2020b"], "Smith, 2020a")

        lone_rows, lone = external.assemble(
            {},
            {"Smith, 2020c": ["wiki/a.md"]},
            [],
        )
        self.assertEqual(list(lone_rows), ["Smith, 2020c"])
        self.assertIn("Smith, 2020", lone["items"])
        self.assertNotIn("Smith, 2020c", lone["items"])
        self.assertEqual(lone["items"]["Smith, 2020"]["identity_keys"], ["Smith, 2020c"])
        self.assertEqual(lone["by_identity"]["Smith, 2020c"], "Smith, 2020")

    def test_same_doi_merges_to_one_unsuffixed_work(self):
        saved = {
            "Smith, 2020a": {"doi": "https://doi.org/10.1000/ABC", "isbn": "", "title": "", "seen_in": []},
            "Smith, 2020b": {"doi": "10.1000/abc", "isbn": "", "title": "Readable title", "seen_in": []},
        }
        rows, generated = external.assemble(saved, {"Smith, 2020a": ["wiki/a.md"], "Smith, 2020b": ["wiki/b.md"]}, [])
        self.assertEqual(list(generated["items"]), ["Smith, 2020"])
        entry = generated["items"]["Smith, 2020"]
        self.assertEqual(entry["identity_keys"], ["Smith, 2020a", "Smith, 2020b"])
        self.assertEqual(entry["title"], "Readable title")
        self.assertEqual(rows["Smith, 2020a"]["doi"], "https://doi.org/10.1000/ABC")

    def test_ingest_deletes_matched_identity_and_keeps_empty_sibling(self):
        works = [{
            "base_key": "Smith, 2020",
            "aliases": ["Smith, 2020a", "Smith (2020a)"],
            "doi": "10.1000/vault",
            "isbn": "",
            "citation": "Smith, A. (2020). A long enough paper title. Journal.",
        }]
        saved = {
            "Smith, 2020": {"doi": "", "isbn": "", "title": "", "seen_in": ["wiki/old.md"]},
            "Jones, 2019": {"doi": "10.1000/vault", "isbn": "", "title": "", "seen_in": []},
            "Smith, 2020b": {
                "doi": "",
                "isbn": "",
                "title": "A long enough paper title",
                "seen_in": [],
            },
        }
        sightings = {"Smith, 2020": ["wiki/old.md"], "Smith, 2020b": ["wiki/old.md"]}
        rows, _generated = external.assemble(saved, sightings, works)
        self.assertIn("Smith, 2020", rows)
        self.assertNotIn("Jones, 2019", rows)
        self.assertNotIn("Smith, 2020b", rows)
        self.assertEqual(rows["Smith, 2020"]["doi"], "")

    def test_regen_preserves_filled_fields_and_drops_unseen_empty_stub(self):
        saved = {
            "Smith, 2020": {"doi": "10.1000/keep", "isbn": "", "title": "Keep me", "seen_in": ["wiki/old.md"]},
            "Jones, 2019": {"doi": "", "isbn": "", "title": "", "seen_in": ["wiki/gone.md"]},
        }
        rows, _generated = external.assemble(saved, {"Smith, 2020": ["wiki/new.md"]}, [])
        self.assertEqual(rows["Smith, 2020"]["doi"], "10.1000/keep")
        self.assertEqual(rows["Smith, 2020"]["title"], "Keep me")
        self.assertEqual(rows["Smith, 2020"]["seen_in"], ["wiki/new.md"])
        self.assertNotIn("Jones, 2019", rows)

    def test_unseen_filled_row_is_kept(self):
        saved = {"Smith, 2020": {"doi": "10.1000/keep", "isbn": "", "title": "", "seen_in": ["wiki/old.md"]}}
        rows, _generated = external.assemble(saved, {}, [])
        self.assertEqual(rows["Smith, 2020"]["doi"], "10.1000/keep")
        self.assertEqual(rows["Smith, 2020"]["seen_in"], [])

    def test_lint_identity_is_info_and_full_mode_collapses(self):
        lint._EXTERNAL_IDENTITY_LOOKUP = {
            "Nye, 2004": {"doi": "", "isbn": "", "title": ""},
            "Li, 2012": {"doi": "10.1000/li", "isbn": "", "title": "Has a title"},
        }
        path = lint.WIKI_DIR / "concepts" / "demo.md"
        issues: list = []
        lint.check_external_citation_identity(path, SNIPPET, issues)
        self.assertEqual(len(issues), 1)
        self.assertEqual(issues[0].severity, "INFO")
        self.assertEqual(issues[0].code, "EXTERNAL_CITATION_IDENTITY")
        self.assertIn("Nye, 2004", issues[0].message)
        collapsed = lint.collapse_external_identity_issues(issues + issues)
        self.assertEqual(len(collapsed), 1)
        self.assertIn("2 处", collapsed[0].message)
        self.assertEqual(collapsed[0].severity, "INFO")


if __name__ == "__main__":
    unittest.main()
