from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import citation_linker as cl  # noqa: E402

LI = {"argument": "Argument_Li_2012_Cambridge"}
HATTIE = {"argument": "Argument_Hattie_2017_SLM"}
KAL = {"argument": "Argument_Kalmendal_2025_PsyArXiv"}
ZHENG = {"argument": "Argument_Zheng_2023_ShanghaiSanlian"}
LOOKUP = {
    "Li (2012)": LI, "Li, 2012": LI,
    "Hattie (2017)": HATTIE, "Hattie, 2017": HATTIE,
    "Kalmendal et al. (2025)": KAL, "Kalmendal et al., 2025": KAL,
    "郑雅君 (2023)": ZHENG, "郑雅君, 2023": ZHENG,
}


def link(body: str, path: Path | None = None) -> str:
    stats = {"linked_parenthetical": 0, "linked_narrative": 0, "fixed_display": 0}
    return cl.link_text("---\ntitle: X\n---\n" + body, LOOKUP, stats, [], path)[len("---\ntitle: X\n---\n"):]


class NarrativeAfterChineseTests(unittest.TestCase):
    def test_author_after_chinese_prose(self) -> None:
        self.assertEqual(link("共同构成 Li (2012) 全书"), "共同构成 [[Argument_Li_2012_Cambridge|Li (2012)]] 全书")

    def test_fullwidth_and_no_space(self) -> None:
        self.assertEqual(link("是 Li（2012）提出"), "是 [[Argument_Li_2012_Cambridge|Li (2012)]]提出")
        self.assertEqual(link("回应Hattie(2017)的"), "回应[[Argument_Hattie_2017_SLM|Hattie (2017)]]的")

    def test_chinese_author(self) -> None:
        self.assertEqual(link("在郑雅君（2023）的框架中"), "在[[Argument_Zheng_2023_ShanghaiSanlian|郑雅君 (2023)]]的框架中")

    def test_given_name_kept_outside_link(self) -> None:
        self.assertEqual(link("**Robert Li（2012）** 指出"), "**Robert [[Argument_Li_2012_Cambridge|Li (2012)]]** 指出")

    def test_coauthor_is_not_first_author(self) -> None:
        for text in ["Yamamoto and Li (2012)两种", "Yamamoto 与 Li (2012)研究", "Scott Bolton 与 John Hattie（2017）系统"]:
            self.assertEqual(link(text), text)

    def test_parenthetical_in_fullwidth_parens(self) -> None:
        self.assertEqual(
            link("卡尔门达尔等（Kalmendal et al., 2025）审计"),
            "卡尔门达尔等（[[Argument_Kalmendal_2025_PsyArXiv|Kalmendal et al., 2025]]）审计",
        )


class ProtectedRegionTests(unittest.TestCase):
    def test_every_occurrence_linked(self) -> None:
        self.assertEqual(link("Li (2012) 与 Li (2012)").count("[[Argument_Li"), 2)

    def test_heading_and_sources_untouched(self) -> None:
        body = "## 在 Li (2012) 中的应用\n\n正文 Li (2012)\n\n## 来源\n\n- Li (2012)\n"
        out = link(body)
        self.assertIn("## 在 Li (2012) 中的应用", out)
        self.assertIn("正文 [[Argument_Li_2012_Cambridge|Li (2012)]]", out)
        self.assertTrue(out.endswith("## 来源\n\n- Li (2012)\n"))

    def test_self_citation_skipped(self) -> None:
        text = "这是 Li (2012) 的核心案例"
        self.assertEqual(link(text, Path("wiki/arguments/Argument_Li_2012_Cambridge.md")), text)

    def test_table_pipe_escaped(self) -> None:
        self.assertEqual(link("| a | Li (2012) |"), "| a | [[Argument_Li_2012_Cambridge\\|Li (2012)]] |")

    def test_inline_code_with_wikilink_survives(self) -> None:
        text = "即 `[[Engineered Evidence]]`，见 Li (2012)"
        self.assertEqual(link(text), "即 `[[Engineered Evidence]]`，见 [[Argument_Li_2012_Cambridge|Li (2012)]]")


if __name__ == "__main__":
    unittest.main()
