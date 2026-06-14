# Schema：教材（Textbook）

触发标识：用户说明材料为教材、教科书、课程用书、入门读本。

---

## 核心原则

- 模板读取顺序统一为 `wiki/templates/TEMPLATE-SPEC.md` → `wiki/templates/CALLOUTS.md` → 对应 `wiki/templates/template-*.md`。
- 每次只处理用户当前发送的一章。
- 处理开始时确定 `<book-folder>`，并使用 `books/<book-folder>/` 与 `wiki/arguments/books/<book-folder>/`。
- Argument 粒度按用户指定。
- 合法粒度：
  - `single-argument`：整本教材只维护 `Argument_<book-folder>.md`，章节处理结果累积到该页。
  - `chapter-arguments`：`Argument_<book-folder>.md` 作为全书 overview，每章另建或更新独立章节 Argument。
- 教材 Argument 使用 `wiki/templates/template-argument-textbook.md`。
- 采用 `single-argument` 时，章节处理结果累积到「章节结构」「章节概览」和「重要摘录」。
- 采用 `chapter-arguments` 时，全书 Argument 只记录章节结构、章节索引和跨章知识结构；章节细节写入章节 Argument。
- 具体定义、分类、争议、例子、方法步骤和理论说明优先沉淀到对应 Concept / Theory / Method / Fact / Person 条目。
- 教材来源的新条目面向初学者，说明应适当详细。
- 图片、表格、新建条目提及规则和脚本运行规则按 `vault-schema.md` 执行；基础索引统一运行 `.venv/bin/python3 scripts/vault_index.py`。

---

## 文件夹结构

```text
books/
  <book-folder>/
    <book-folder>.pdf 或 <book-folder>.epub
    <book-folder>.md
    figures/
      Chapter_X_Concept_Map.jpg
      Figure_X-X_Descriptive_Name.jpg

wiki/arguments/books/<book-folder>/
  Argument_<book-folder>.md
  Argument_<book-folder>_Ch01.md        # 仅在用户指定分章节 Argument 时使用
```

`<book-folder>` 使用 `Author_Year_Publisher` 或稳定的英文教材短名。

---

## 教材 Argument

`template-argument-textbook.md` 固定保留：

```markdown
## 章节结构
## 章节概览
## 重要摘录
## 来源
```

「章节结构」只保留三列：

```markdown
> [!ref-table] 章节结构
> | 章节 | 内容概要 | 主要关联条目 |
> |---|---|---|
> | 第X章 章节标题 | 用一两句话说明这一章主要讲什么。 | Concept A、Theory B、Fact C |
```

`主要关联条目` 只列 3–5 个最核心的 Concept / Theory / Method / Fact / Person；不同章节尽量拉开差异。

「章节概览」跟随教材自身知识推进逻辑，记录概念、理论、证据、案例、表格、图片和结论如何展开。已建条目只简单提及，详细内容写入具体条目。

「重要摘录」只保留有启发或表述精炼的观点，优先使用 `[!citation-card]`，标注章节与页码。没有页码时只标注章节，不编造页码。

采用 `chapter-arguments` 时：

- `Argument_<book-folder>.md` 是全书 overview，「章节结构」列出每章链接、内容概要和 3–5 个核心关联条目。
- 章节 Argument 文件名使用 `Argument_<book-folder>_ChXX.md`；若章节需要更强可读性，可在 `ChXX` 后追加稳定英文短标题。
- 章节 Argument 记录该章知识结构、核心概念、分类/步骤/方法、例子/表格/图和重要摘录。
- 当前章节新建的 Concept / Theory / Method / Fact / Person 必须在对应章节 Argument 正文中至少出现一次 wikilink；overview 可只链接章节 Argument 和最核心跨章条目。

---

## 单章处理流程

1. 读取 `vault-schema.md`、`wiki/templates/TEMPLATE-SPEC.md`、`wiki/templates/CALLOUTS.md` 和 `schema/schema-textbook.md`。
2. 只处理当前章节文本。
3. 确认用户指定的 Argument 粒度：`single-argument` 或 `chapter-arguments`；未指定则先询问。
4. 扫描可提取或更新的 Concept / Theory / Method / Person / Fact / Argument。
5. 读取 `wiki/index.json` 判断候选条目是否已存在。
6. 更新已有条目；新建条目时读取对应 `wiki/templates/template-*.md`。
7. 读取并使用 `wiki/templates/template-argument-textbook.md`。
8. 若采用 `single-argument`，更新或新建 `wiki/arguments/books/<book-folder>/Argument_<book-folder>.md`，将当前章节整合进「章节结构」「章节概览」和「重要摘录」。
9. 若采用 `chapter-arguments`，更新或新建当前章节 Argument，并在 `Argument_<book-folder>.md` 中维护章节结构、章节短摘要和跨章知识结构。
10. 若整本教材 source record 已创建，在相关 Argument 的 `## 来源` 列出 source wikilink；尚未创建时暂不编造来源链接。
11. 执行 `vault-schema.md` 的脚本运行规则，即运行 `.venv/bin/python3 scripts/vault_index.py`。
12. 当前章节处理完成后停止。

---

## Source 记录和阅读页面

用户提供整合后的 PDF / EPUB 并要求建立 source 记录时，文件放在：

```text
books/<book-folder>/<book-folder>.<ext>
```

PDF：

```bash
.venv/bin/python3 scripts/source_record.py monograph-pdf \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.pdf \
  --citation "Author, A. A. (Year). Book title. Publisher."
```

EPUB：

```bash
.venv/bin/python3 scripts/source_record.py monograph-epub \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.epub \
  --citation "Author, A. A. (Year). Book title. Publisher."
```

执行 `vault-schema.md` 的脚本运行规则，即运行 `.venv/bin/python3 scripts/vault_index.py`。
