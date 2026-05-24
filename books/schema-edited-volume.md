# Schema：论文集／编著（Edited Volume）

触发标识：用户标注「(Ed.)」、编著、论文集，或明确说明该材料属于 edited volume。

---

## 文件夹结构

```text
books/
  Editor_Year_Publisher/
    Editor_Year_Publisher_overview.md
    Preface.pdf
    Ch3_ChapterAuthor_Year.pdf
    Ch3_ChapterAuthor_Year.md
    Ch7_ChapterAuthor_Year.pdf
    Ch7_ChapterAuthor_Year.md

wiki/arguments/books/<book-folder>/
  Argument_Editor_Year_Publisher.md
  Argument_ChapterAuthor_Year_关键词.md
```

论文集每章独立处理，各自有：

- `books/Editor_Year_Publisher/ChX_ChapterAuthor_Year.md` + `.pdf`：章节 source 记录与 PDF
- `wiki/arguments/books/<book-folder>/Argument_ChapterAuthor_Year_关键词.md`：该章论证框架
- `wiki/arguments/books/<book-folder>/Argument_Editor_Year_Publisher.md`：整本论文集框架

---

## 处理前言／整本论文集 overview

1. 读取 `vault-schema.md`。
2. 在 `books/` 新建文件夹：`Editor_Year_Publisher/`。
3. 若有前言 PDF，将其放入该文件夹。
4. 读取 `wiki/index.json`，按普通处理流程提取前言或导论中的 wiki 条目。
5. 在 `wiki/arguments/books/<book-folder>/` 新建整本论文集的论证框架：
   - 读取 `wiki/templates/template-argument-edited-volume.md`
   - 新建 `Argument_Editor_Year_Publisher.md`
   - 至少填写 `summary`、`book_title`、`editors`、`publisher`、`citation`
6. 使用 `source_record.py edited-volume-overview` 创建 overview source 记录：

```bash
python3 scripts/source_record.py edited-volume-overview \
  --book-folder Editor_Year_Publisher \
  --file books/Editor_Year_Publisher/Preface.pdf \
  --citation "Editor, E. (Ed.). (Year). Book title. Publisher." \
  --book-title "Book title" \
  --editors "Editor Name" \
  --publisher "Publisher" \
  --argument "[[Argument_Editor_Year_Publisher]]" \
  --extracted-to "[[其他条目]],[[其他条目2]]"
```

若没有前言 PDF，可省略 `--file`。

7. 在正文中自然使用 wikilink，在 `## 来源` 章节列出来源。
8. 不手动维护 YAML `related_*` 和 `sources`。
9. 运行标准同步与检查流程。

---

## 处理后续章节

1. 读取 `vault-schema.md`。
2. 从文件命名识别归属论文集 → 在 `books/` 找到对应文件夹。
3. 读取该论文集的 overview source 记录，确认归属。
4. 根据用户提供的章节 PDF 或章节文本判断章节标题和编号。
5. 读取 `wiki/index.json`，按普通处理流程处理该章节。
6. 在 `books/Editor_Year_Publisher/` 中放置该章 PDF。
7. 使用 `source_record.py book-chapter` 创建该章 source 记录：

```bash
python3 scripts/source_record.py book-chapter \
  --book-folder Editor_Year_Publisher \
  --file books/Editor_Year_Publisher/Ch3_ChapterAuthor_Year.pdf \
  --citation "ChapterAuthor, A. (Year). Chapter title. In Editor Name (Ed.), Book title (pp. xx-xx). Publisher." \
  --book-title "Book title" \
  --chapter-title "Chapter title" \
  --authors "Chapter Author" \
  --editors "Editor Name" \
  --publisher "Publisher" \
  --extracted-to "[[Argument_ChapterAuthor_Year_关键词]],[[其他条目]]" \
  --part-of "[[Editor_Year_Publisher]]"
```

8. 在 `wiki/arguments/books/<book-folder>/` 新建该章论证框架：
   - 读取 `wiki/templates/template-argument.md`
   - 文件名：`Argument_作者姓_年份_章节关键词.md`
   - frontmatter 至少填写：
     - `summary`
     - `subtype: book-chapter`
     - `publication_type: book`
     - `book_title`
     - `part_of: "[[Editor_Year_Publisher]]"`
9. 用 `str_replace` 更新 overview 的「已处理章节」列表，加入该章 Argument 链接。
10. 在正文中自然使用 wikilink，在 `## 来源` 章节列出 source wikilink。
11. 不手动维护 YAML `related_*` 和 `sources`。
12. 运行标准同步与检查流程。

---

## 注意事项

- 不追踪未处理章节，按需处理即可。
- 每章 source 记录放在 `books/Editor_Year_Publisher/`，不放 `sources/`。
- 论文集章节 Argument 放在 `wiki/arguments/books/<book-folder>/`。
- `source_record.py` 负责 source 记录 frontmatter、PDF 嵌入和 `extracted_to` 格式。
- `wiki_relations.py` 负责同步 `related_*` 与 YAML `sources`。
- `vault_lint.py` 用于检查生成结果。
