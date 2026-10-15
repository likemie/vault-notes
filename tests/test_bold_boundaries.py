from __future__ import annotations

import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import vault_lint as lint


class BoldBoundaryTests(unittest.TestCase):
    def test_reported_reliability_example_adds_only_required_space(self):
        before = '它是信度作为**等值性（reliability as equivalence）**的核心形式之一'
        after = '它是信度作为**等值性（reliability as equivalence）** 的核心形式之一'
        self.assertEqual((after, 1), lint.fix_bold_boundaries(before))
        self.assertEqual((after, 0), lint.fix_bold_boundaries(after))

    def test_opening_quote_and_closing_quote_need_both_boundaries(self):
        self.assertEqual(('这是 **“术语”** 的定义', 2), lint.fix_bold_boundaries('这是**“术语”**的定义'))

    def test_valid_bold_is_unchanged(self):
        for text in ('这是**术语**的定义', '**术语（Term）**。', '这是 **术语（Term）** 的定义', '**标题** 正文', '***嵌套强调***'):
            self.assertEqual((text, 0), lint.fix_bold_boundaries(text))

    def test_wikilink_and_its_display_are_preserved(self):
        text = '采用**[[Reliability|信度]]（reliability）**检验'
        self.assertEqual(('采用 **[[Reliability|信度]]（reliability）** 检验', 2), lint.fix_bold_boundaries(text))

    def test_frontmatter_code_comments_and_escaped_markers_are_unchanged(self):
        for text in ('---\nsummary: "这是**术语（Term）**的定义"\n---\n正文',
                     '`这是**术语（Term）**的定义`',
                     '```markdown\n这是**术语（Term）**的定义\n```',
                     '<!-- 这是**术语（Term）**的定义 -->',
                     '%% 这是**术语（Term）**的定义 %%',
                     r'这是\**术语（Term）\**的定义'):
            self.assertEqual((text, 0), lint.fix_bold_boundaries(text))

    def test_lint_warns_with_vault_file_line_number(self):
        text = '---\ntitle: Example\n---\n\n这是**术语（Term）**的定义\n'
        issues = []
        lint.check_markdown_misc(ROOT / 'wiki/concepts/Example.md', text, issues)
        found = [i for i in issues if i.code == 'BOLD_DELIMITER_BOUNDARY']
        self.assertEqual([('WARN', 5)], [(i.severity, i.line) for i in found])


if __name__ == '__main__':
    unittest.main()
