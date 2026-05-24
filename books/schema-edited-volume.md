# Schema：论文集／编著（Edited Volume）

触发标识：用户标注「(Ed.)」、编著、论文集，或明确说明材料来自 edited volume。

---

## 核心原则

- 论文集按「整本书 overview」和「单章」分别处理。
- 每章作为独立来源处理，每次只处理用户当前提供的一章或前言。
- 处理前言时建立整本论文集的 overview 与整体 Argument。
- 处理章节时建立该章 source 记录与章节 Argument，并更新 overview 的「已处理章节」。
- 不追踪未处理章节，只记录已经处理的章节。
- `related_*` 与 `sources` 不要求 AI 手动维护，由脚本根据正文 wikilink 与 `## 来源` 自动同步。
- 处理后统一运行索引、自动链接和关系同步脚本。

---

## 文件夹结构

```text
books/
  Author(Ed.)_Year_Publisher/
    Author(Ed.)_Year_Publisher_overview.md
    Ch3_ChapterAuthor_Year.pdf
    Ch3_ChapterAuthor_Year.md
    Ch7_ChapterAuthor_Year.pdf
    Ch7_ChapterAuthor_Year.md

wiki/arguments/books/<book-folder>/
  Argument_Editor_Year_Publisher.md
  Argument_ChapterAuthor_Year_Keyword.md
```

说明：

- `books/<book-folder>/` 保存前言、章节 PDF、章节 source 记录与 overview。
- `wiki/arguments/books/<book-folder>/` 保存整本论文集 Argument 和各章 Argument。
- `<book-folder>` 使用英文文件夹名，例如 `Apple(Ed.)_2019_Routledge`。

---

## overview.md 结构

```markdown
---
title: Author(Ed.)_Year_Publisher
summary: ""
type: source
subtype: edited-volume-overview
citation: "编者 (Ed.). (Year). 书名. 出版社."
book_title: ""
editors: []
publisher: ""
extracted_to: ["[[Argument_Editor_Year_Publisher]]"]
processed_date: YYYY-MM-DD
status: processed
---

# Author(Ed.)_Year_Publisher

![[Preface_FileName.pdf]]

## Citation

编者 (Ed.). (Year). *书名*. 出版社.

---

## Extracted to

- [[Argument_Editor_Year_Publisher]]

---

## 已处理章节

- [[Argument_ChapterAuthor_Year_Keyword]] — 章节标题及核心贡献简述
```

---

## 每章 source 记录结构

```markdown
---
title: ChX_ChapterAuthor_Year
summary: ""
type: source
subtype: book-chapter
citation: "章节作者. (Year). 章节标题. In 编者 (Ed.), 书名 (pp. XX–XX). 出版社."
book_title: ""
chapter_title: ""
chapter_number: ""
part_of: "[[Author(Ed.)_Year_Publisher]]"
extracted_to: ["[[Argument_ChapterAuthor_Year_Keyword]]"]
processed_date: YYYY-MM-DD
status: processed
---

# ChX_ChapterAuthor_Year

![[ChX_ChapterAuthor_Year.pdf]]

## Citation

章节作者. (Year). 章节标题. In 编者 (Ed.), *书名* (pp. XX–XX). 出版社.

---

## Extracted to

- [[Argument_ChapterAuthor_Year_Keyword]]

---

## Part of

- [[Author(Ed.)_Year_Publisher]]
```

---

## 处理前言流程

当用户提供论文集前言或整本书导论时：

1. 读取 `vault-schema.md`。
2. 读取 `books/schema-edited-volume.md`。
3. 在 `books/` 下建立论文集文件夹：

```text
books/Author(Ed.)_Year_Publisher/
```

4. 读取 `wiki/index.json`，判断可提取条目是否已存在。
5. 按 `vault-schema.md` 普通流程处理前言内容，提取 Concept / Theory / Method / Person / Fact / Argument。
6. 新建或更新整本论文集 Argument：

```text
wiki/arguments/books/<book-folder>/Argument_Editor_Year_Publisher.md
```

7. 新建 overview：

```text
books/<book-folder>/Author(Ed.)_Year_Publisher_overview.md
```

8. overview 的 `extracted_to` 至少包含整体 Argument。
9. 维护正文 `## 来源` 章节中的 source wikilink；不手动维护 `related_*`。
10. 运行：

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

11. 处理完成后停止。

---

## 处理后续章节流程

当用户提供论文集某一章时：

1. 读取 `vault-schema.md`。
2. 读取 `books/schema-edited-volume.md`。
3. 根据文件名、用户说明或 citation 识别所属论文集。
4. 读取对应 overview，确认归属：

```text
books/<book-folder>/Author(Ed.)_Year_Publisher_overview.md
```

5. 判断章节编号、章节标题、章节作者、页码范围。
6. 读取 `wiki/index.json`，扫描当前章节可提取条目。
7. 将候选分为：
   - 待更新条目
   - 待新建条目
8. 按 `vault-schema.md` 更新或新建条目。
9. 新建该章 source 记录：

```text
books/<book-folder>/ChX_ChapterAuthor_Year.md
```

10. 新建该章 Argument：

```text
wiki/arguments/books/<book-folder>/Argument_ChapterAuthor_Year_Keyword.md
```

章节 Argument 使用 `wiki/templates/template-argument.md`，frontmatter 至少填写：

```yaml
subtype: book-chapter
publication_type: book
book_title: ""
part_of: "[[Author(Ed.)_Year_Publisher]]"
```

11. 用 `str_replace` 更新 overview 的「已处理章节」列表，加入该章 Argument 链接。
12. 维护正文 wikilink 和 `## 来源`；不手动维护 `related_*`。
13. 运行：

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

14. 处理完成后停止。

---

## 整合论文集 Argument

当用户要求整合整本论文集 Argument 时：

1. 读取整体 Argument 与 overview 的「已处理章节」。
2. 读取 `wiki/templates/template-argument-edited-volume.md`。
3. 整合：
   - 编者论点
   - 全书共同问题
   - 章节组织逻辑
   - 理论框架
   - 各章之间的关系
   - 全书贡献与局限
4. 用 `str_replace` 更新整体 Argument。
5. 保留「各章概览」或章节列表，作为逐章处理记录。
6. 运行：

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

---

## 注意事项

- 每次只处理用户当前提供的前言或章节。
- 不追踪未处理章节。
- 章节 source 记录放在 `books/<book-folder>/`，不放 `sources/`。
- 章节 Argument 放在 `wiki/arguments/books/<book-folder>/`。
- `extracted_to` 必须用数组格式，元素为带引号的 wikilink。
- `part_of` 必须使用带引号的 wikilink。
- `related_*` 由 `wiki_relations.py` 自动维护，AI 不手动填写。
- `sources` 由 `## 来源` 章节同步，AI 只需维护正文来源列表。
