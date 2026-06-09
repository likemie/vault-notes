# Schema：论文集／编著（Edited Volume）

触发标识：用户标注「(Ed.)」、编著、论文集，或明确说明材料属于 edited volume。

---

## 核心原则

- 论文集 overview 是整本书的结构入口，使用 `wiki/templates/template-argument-edited-volume.md`。
- 论文集章节是主要可引用单元，使用 `wiki/templates/template-argument.md`。
- 章节 Argument 的 citation 字段按章节作者、章节年份和章节标题填写。
- overview source 与章节 source 都放在 `books/<book-folder>/`，不放 `sources/`。
- Concept / Theory / Method / Fact / Person 条目不写 YAML `sources` 和正文 `## 来源`；来源性陈述通过 Argument 链接进入 `related_arguments`。
- 图片、表格、新建条目提及规则和脚本运行规则按 `vault-schema.md` 执行；基础索引统一运行 `.venv/bin/python3 scripts/vault_index.py`。

---

## 文件夹结构

```text
books/
  <book-folder>/
    <book-folder>.md
    Preface.pdf
    Ch3_ChapterAuthor_Year.pdf
    Ch3_ChapterAuthor_Year.md

wiki/arguments/books/<book-folder>/
  Argument_<book-folder>.md
  Argument_ChapterAuthor_Year_关键词.md
```

`<book-folder>` 使用 `Editor_Year_Publisher`。

---

## Overview 处理流程

1. 读取 `vault-schema.md` 和 `schema/schema-edited-volume.md`。
2. 建立 `books/<book-folder>/`。
3. 读取前言、导论或编者说明。
4. 读取 `wiki/index.json` 判断候选条目是否已存在。
5. 更新已有条目或按模板新建条目。
6. 使用 `wiki/templates/template-argument-edited-volume.md` 新建或更新 overview Argument。
7. 使用 `source_record.py edited-volume-overview` 创建 overview source 记录：

```bash
.venv/bin/python3 scripts/source_record.py edited-volume-overview \
  --book-folder <book-folder> \
  --record-name <book-folder> \
  --file books/<book-folder>/Preface.pdf \
  --citation "Editor, E. E. (Ed.). (Year). Book title. Publisher."
```

没有前言 PDF 时省略 `--file`。

8. 在 `## 来源` 列出 overview source wikilink。
9. 执行 `vault-schema.md` 的脚本运行规则，即运行 `.venv/bin/python3 scripts/vault_index.py`。

---

## 章节处理流程

1. 读取 `vault-schema.md` 和 `schema/schema-edited-volume.md`。
2. 确认章节所属 `<book-folder>`。
3. 读取 overview source 记录，确认归属。
4. 根据章节 PDF 或章节文本判断章节编号、标题和作者。
5. 读取 `wiki/index.json` 判断候选条目是否已存在。
6. 更新已有条目或按模板新建条目。
7. 使用 `source_record.py book-chapter` 创建章节 source 记录：

```bash
.venv/bin/python3 scripts/source_record.py book-chapter \
  --book-folder <book-folder> \
  --record-name Ch3_ChapterAuthor_Year \
  --file books/<book-folder>/Ch3_ChapterAuthor_Year.pdf \
  --citation "ChapterAuthor, A. A. (Year). Chapter title. In Editor, E. E. (Ed.), Book title (pp. xx–xx). Publisher." \
  --part-of "[[<book-folder>]]"
```

8. 使用 `wiki/templates/template-argument.md` 新建章节 Argument：
   - 文件名：`Argument_ChapterAuthor_Year_关键词.md`
   - `subtype: book-chapter`
   - `publication_type: book-chapter`
   - `book_title` 写论文集标题
   - `part_of` 指向 overview source
   - citation 字段以章节作者和章节年份为准
9. 更新 overview Argument 的「各章概览」，加入章节 Argument 链接和核心贡献。
10. 在 `## 来源` 列出章节 source wikilink。
11. 执行 `vault-schema.md` 的脚本运行规则，即运行 `.venv/bin/python3 scripts/vault_index.py`。
