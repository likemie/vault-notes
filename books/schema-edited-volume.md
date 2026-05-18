# Schema：论文集／编著（Edited Volume）

**触发标识：** 用户标注「(Ed.)」

---

## 文件夹结构

```
books/
  Author(Ed.)_Year_Publisher/
    Author(Ed.)_Year_Publisher_overview.md         ← 前言提取内容，列出已处理章节（永久保留）
    Ch3_ChapterAuthor_Year.pdf                     ← 该章 PDF
    Ch3_ChapterAuthor_Year.md                      ← 该章 sources 记录（与 PDF 同名）
    Ch7_ChapterAuthor_Year.pdf
    Ch7_ChapterAuthor_Year.md
```

论文集每章独立处理，各自有：
- `books/Author(Ed.)_Year_Publisher/ChX_ChapterAuthor_Year.md` + `.pdf` ← 该章 sources 记录与 PDF
- `wiki/arguments/books/Argument_ChapterAuthor_Year_关键词.md` ← 该章论证框架（使用 template-argument.md，subtype 可用 `book-chapter`）
- `wiki/arguments/books/Argument_Editor_Year_Publisher.md` ← 整本论文集框架（使用 template-argument-edited-volume.md）

---

## overview.md 结构

```markdown
---
citation: "编者 (Ed.). (Year). 书名. 出版社."
extracted_to: ["[[Argument_Editor_Year_Publisher]]", "[[Argument_ChapterAuthor_Year_关键词]]"]
processed_date: YYYY-MM-DD
---

# Author(Ed.)_Year_Publisher

![[前言PDF文件名.pdf]]

## 已处理章节
- [[Argument_ChapterAuthor_Year_关键词]] — 章节标题及核心贡献简述
- [[Argument_ChapterAuthor2_Year_关键词]] — 章节标题及核心贡献简述
```

## 每章 sources 记录结构

```markdown
---
citation: "章节作者. (Year). 章节标题. In 编者 (Ed.), 书名 (pp. XX–XX). 出版社."
extracted_to: ["[[条目名]]", "[[Argument_ChapterAuthor_Year_关键词]]"]
processed_date: YYYY-MM-DD
part_of: "[[Author(Ed.)_Year_Publisher]]"
---

# ChapterAuthor_Year_关键词

![[ChapterAuthor_Year_关键词.pdf]]
```

---

## 工作流

### 处理前言（用户标注「(Ed.)」）

```
1. 读取 vault-schema.md
2. 在 books/ 新建文件夹：Author(Ed.)_Year_Publisher/
3. 读取 wiki/index.json，按 vault-schema.md 普通处理流程 提取前言内容，写入对应 wiki/ 条目
4. 在 `wiki/arguments/books/` 新建整本论文集的论证框架：
   读取 `wiki/templates/template-argument-edited-volume.md`
   新建 `Argument_Editor_Year_Publisher.md`
   frontmatter 至少填写：
   - `summary`
   - `book_title`
   - `editors`
   - `publisher`
   - `citation`
5. 新建 books/Author(Ed.)_Year_Publisher/Author(Ed.)_Year_Publisher_书名_overview.md：
   - 填入 citation、extracted_to（含整体 Argument 链接）、processed_date
   - 嵌入前言 PDF
   - 建立「已处理章节」列表（暂为空）
6. 按 vault-schema.md 维护必要的 frontmatter related_*、sources 与正文 wikilink
7. 运行 `python3 scripts/update_wiki_index.py` 更新 `wiki/index.json` 与 `wiki/index.md`
```

### 处理后续章节

```
1. 读取 vault-schema.md
2. 从文件命名识别归属论文集 → 在 books/ 找到对应文件夹
3. 读取该论文集的 Author(Ed.)_Year_Publisher_书名_overview.md 确认归属
4. 根据文件内容判断章节标题和编号
5. 读取 wiki/index.json，按 vault-schema.md 普通处理流程 处理该章节（提取所有 wiki 条目）
6. 在 books/Author(Ed.)_Year_Publisher/ 新建该章 sources 记录：
   文件名：ChX_ChapterAuthor_Year.md（与 PDF 同名）
   填入 citation、extracted_to、processed_date、part_of，嵌入 PDF
7. 在 `wiki/arguments/books/` 新建该章的论证框架条目：
   读取 `wiki/templates/template-argument.md`
   文件名：`Argument_作者姓_年份_章节关键词.md`
   frontmatter 至少填写：
   - `summary`
   - `subtype: book-chapter`
   - `publication_type: book`
   - `book_title`
   - `part_of: "[[Author(Ed.)_Year_Publisher]]"`
8. 用 str_replace 更新 overview.md 的「已处理章节」列表，加入该章 Argument 链接
9. 按 vault-schema.md 维护必要的 frontmatter related_*、sources 与正文 wikilink
```

---

## 注意事项

- 不追踪未处理章节，按需处理即可
- 每章 sources 记录放在 `books/Author(Ed.)_Year_Publisher/`，不放 `sources/`
- frontmatter `extracted_to` 必须用 `["[[条目名]]", "[[条目名]]"]` 格式，否则 Obsidian 无法解析
