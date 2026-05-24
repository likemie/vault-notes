# Schema：专著（Monograph）— PDF

触发标识：用户标注「专著」或说明材料来自专著 PDF。

---

## 核心原则

- 用户按章节向 AI 提供文本。
- AI 每次只处理用户当前发送的一章。
- 不自动拆分 PDF。
- 不读取整本 PDF。
- 在整本书处理完成前，不创建整本书 source 记录，不创建阅读页面。
- 章节处理结果累积到全书 Argument 的「各章概览」。
- 用户提供整本 PDF 后，再建立书籍 source 记录和阅读页面。
- `related_*` 与 `sources` 不要求 AI 手动维护，由脚本根据正文 wikilink 与 `## 来源` 自动同步。

---

## 文件夹结构

```text
books/
  作者姓_年份_出版社/
    BookName.pdf
    作者姓_年份_出版社.md

wiki/arguments/books/<book-folder>/
  Argument_作者姓_年份_出版社.md
```

说明：

- `BookName.pdf` 在整本书处理完成后再放入。
- `作者姓_年份_出版社.md` 是整本书 source 记录，用户提供完整 PDF 后再创建。
- 全书 Argument 在逐章处理过程中逐步建立和更新。

---

## 单章处理流程

当用户发送某一章文本时：

1. 读取 `vault-schema.md`。
2. 读取 `books/schema-monograph-pdf.md`。
3. 只处理用户当前发送的章节文本。
4. 基于当前章节扫描可提取条目：
   - Concept
   - Theory
   - Method
   - Person
   - Fact
   - Argument
5. 读取 `wiki/index.json` 判断候选条目是否已存在。
6. 将候选分为：
   - 待更新条目
   - 待新建条目
7. 更新已有条目：
   - 读取目标文件。
   - 判断插入位置。
   - 使用 `str_replace` 精确整合。
8. 新建条目：
   - 只读取对应模板。
   - 写入对应正式文件夹。
9. 更新或新建全书 Argument：

```text
wiki/arguments/books/<book-folder>/Argument_作者姓_年份_出版社.md
```

若 Argument 不存在，读取：

```text
wiki/templates/template-argument-monograph.md
```

新建时至少填写：

```yaml
subtype: monograph
publication_type: book
book_title: ""
authors: []
publisher: ""
citation: ""
```

10. 将当前章节内容整合进「各章概览」。
11. 维护正文 wikilink 和 `## 来源`；不手动维护 `related_*`。
12. 运行：

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

13. 当前章节处理完成后停止。

---

## 章节文本分批

如果用户发送的一章过长，可按小节分批处理：

- 每批仍视为同一章的一部分。
- 不要为同一章重复新建 Argument。
- 后续批次应整合到同一章的「各章概览」条目下。
- 同章重复发送时，应判断是补充、修订还是替换。

---

## 整合 Argument

当用户要求整合全书 Argument 时：

1. 读取全书 Argument 中的「各章概览」。
2. 读取 `wiki/templates/template-argument-monograph.md`。
3. 提炼：
   - 全书研究问题
   - 理论框架
   - 核心概念
   - 论证结构
   - 章节推进关系
   - 主要结论
   - 关键证据
   - 局限与批评
4. 用 `str_replace` 在「各章概览」之前写入正式论证结构。
5. 保留「各章概览」作为原始章节记录。
6. 运行：

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

---

## 全书完成后的 source 记录与阅读页面

当用户提供整本 PDF 并要求建立 source 记录或阅读页面时：

1. 将 PDF 放入：

```text
books/作者姓_年份_出版社/BookName.pdf
```

2. 新建：

```text
books/作者姓_年份_出版社/作者姓_年份_出版社.md
```

3. source 记录格式：

```markdown
---
title: 作者姓_年份_出版社
summary: ""
type: source
subtype: monograph-pdf
citation: "作者姓, 名字缩写. (年份). 书名. 出版社."
book_title: ""
authors: []
publisher: ""
book_file: "books/作者姓_年份_出版社/BookName.pdf"
extracted_to: ["[[Argument_作者姓_年份_出版社]]"]
processed_date: YYYY-MM-DD
status: processed
---

# 作者姓_年份_出版社

## Citation

作者姓, 名字缩写. (年份). *书名*. 出版社.

---

## Extracted to

- [[Argument_作者姓_年份_出版社]]

---

## PDF Reader

![[BookName.pdf]]
```

4. 根据已经建立或更新的条目补全 `extracted_to`。
5. 运行：

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

---

## 注意事项

- 每次只处理用户当前提供的章节文本。
- 不自动拆分 PDF。
- 不要求 AI 读取整本 PDF。
- 不要求 Python 读取整本 PDF。
- 所有来源性陈述必须标注页码。
- 如果用户提供的章节文本没有页码，只能记录无页码信息，不得编造页码。
- source 记录和阅读页面只在用户提供整本 PDF 后建立。
- `related_*` 由 `wiki_relations.py` 自动维护，AI 不手动填写。
- `sources` 由 `## 来源` 章节同步，AI 只需维护正文来源列表。
- `extracted_to` 必须使用数组格式，元素为带引号的 wikilink。
