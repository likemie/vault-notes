# Schema：专著 — epub

**触发格式：** 文件副档名为 `.epub`（无需标注「专著」）

---

## 文件夹结构

```text
books/
  作者姓_年份_出版社/
    BookName.epub            ← 原书 epub（全程保留，无需拆分）
```

整合完成后建立 sources 记录：

```text
books/
  作者姓_年份_出版社/
    BookName.epub
    作者姓_年份_出版社.md      ← sources 记录（永久保留，放在书籍文件夹内）

wiki/arguments/books/
  Argument_作者姓_年份_出版社.md  ← 全书论证框架
```

epub 全程保留在 `books/` 文件夹，用 Obsidian Epub Reader 插件本地阅读。

Quartz 网页端阅读通过统一配置好的静态脚本实现：

```text
/static/jszip.min.js
/static/epub.min.js
/static/epub-loader.js
/static/epub-init.js
```

> 注意：`epub-loader.js` 与 `epub-init.js` 已在 `/static/` 中统一配置，不要在每本书的 sources 文件或模板中重复写入 JS 源码。

---

## 进度追踪

不追踪章节处理进度，按需处理：

- 用户指定哪章就处理哪章，已处理的章节也可重新处理
- 已处理章节内容累积在 Argument 的「各章概览」里，可作参考

---

## 工作流

### 第一次处理新书

```text
1. 读取 vault-schema.md
2. 在 books/ 下新建文件夹：作者姓_年份_出版社/
3. 列出 epub 所有章节（只读文件结构，不读正文内容）：
   python3 -c "
   import ebooklib
   from ebooklib import epub
   book = epub.read_epub('books/BOOKFOLDER/BookName.epub')
   for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)):
       print(i, item.get_name())
   "
4. 将章节列表展示给用户，停下等待用户指定章节：
   「以上是全书章节列表，请告知需要处理哪一章？」
5. 不处理正文内容，停下等待用户指定章节；首次真正写入 Argument 或条目后，再运行 `python3 scripts/update_wiki_index.py`
```

---

### 单章处理流程

```text
1. 读取 vault-schema.md

2. 用 Python 提取用户指定章节的正文：
   python3 -c "
   import ebooklib
   from ebooklib import epub
   from bs4 import BeautifulSoup
   book = epub.read_epub('books/BOOKFOLDER/BookName.epub')
   for item in book.get_items_of_type(ebooklib.ITEM_DOCUMENT):
       if item.get_name() == 'CHAPTER_FILENAME':
           soup = BeautifulSoup(item.get_content(), 'html.parser')
           print(soup.get_text())
   "

   注意：只读用户指定的章节，不读其他章节内容。

3. 基于 vault-schema.md 提取规范扫描章节内容，列出可提取条目。

4. 读取 `wiki/index.json`，将条目分为待更新和待新建两组，标注类型与目标二级文件夹。

5. 按 vault-schema.md 的更新／新建条目规则 执行：
   - 步骤 8：逐条读取已有条目，检查格式与重构需求，整合新内容
   - 步骤 9：按类型逐条读取模板新建条目，写入 wiki/类型/ 正式文件夹

6. 将本章内容追加到 Argument 的「各章概览」：
   - 若 Argument 尚不存在 → 读取 `wiki/templates/template-argument-monograph.md`，在 `wiki/arguments/books/` 新建文件，至少填写 `summary`、`book_title`、`authors`、`publisher`、`citation`，正文可先只填「各章概览」章节
   - 若 Argument 已存在 → 用 str_replace 追加本章内容到「各章概览」末尾
   - 格式自由，忠实记录该章论点、论据、关键引用，不套模板

7. 按 vault-schema.md 维护必要的 frontmatter related_*、sources 与正文 wikilink。

8. 停下，告知用户：
   「第 XX 章《章节名》处理完成。」
```

---

### 重新开始（session 重开后）

```text
1. 读取 vault-schema.md
2. 列出 epub 所有章节（只读文件结构），停下等待用户指定：
   「请告知需要处理哪一章？」
3. 用户指定后，执行单章处理流程
```

---

### 整合 Argument（用户发出整合指令后）

```text
1. 读取 Argument 文件中已累积的「各章概览」内容。

2. 读取 wiki/templates/template-argument-monograph.md。

3. 按模板结构整合：
   - 从各章概览中提炼全书研究问题、理论框架、论证结构、主要发现、关键引用、局限性
   - 用 str_replace 在「各章概览」之前写入正式章节
   - 「各章概览」保留在最后，作为原始章节记录

4. 新建 sources 记录：
   books/作者姓_年份_出版社/作者姓_年份_出版社.md

   sources 记录应包含：
   - citation（APA）
   - extracted_to（所有提取条目的完整列表 + Argument 链接）
   - processed_date
   - epub_viewer HTML 调用块

5. 运行 `python3 scripts/update_wiki_index.py` 更新 `wiki/index.json` 与 `wiki/index.md`，重新生成静态索引。
```

---

## Sources 记录模板

文件位置：

```text
books/作者姓_年份_出版社/作者姓_年份_出版社.md
```

模板：

```markdown
---
title: 作者姓_年份_出版社
type: source
subtype: monograph-epub
citation: "作者姓, 名字缩写. (年份). 书名. 出版社."
book_file: "books/作者姓_年份_出版社/BookName.epub"
extracted_to: []
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

## EPUB Reader

<div id="epub-viewer" style="width:100%;height:560px;border:1px solid rgb(204,204,204);" data-epub="/books/作者姓_年份_出版社/BookName.epub"></div>
---

## Notes

- Obsidian 本地不渲染此 HTML，本地阅读用 Epub Reader 插件直接打开 epub。
- Quartz 网页端通过 `/static/` 中已配置的脚本渲染。
- 每本书只需要修改 `data-epub` 路径。
- 不要在本文件中重复写入 `epub-loader.js` 或 `epub-init.js` 源码。
```

---

## 注意事项

- 列出章节列表只读文件结构，不读正文内容。
- 必须等用户明确指定章节后，才读取该章正文，不得自行决定处理顺序。
- 每次只处理一章，处理完必须停下等待用户指令。
- 章节文本过长时，按小节拆分处理。
- frontmatter `extracted_to` 必须用 `["[[条目名]]", "[[条目名]]"]` 格式。
- Argument 整合须等用户发出指令才执行。
- `epub-loader.js` 与 `epub-init.js` 只在 `/static/` 中维护，不在模板或 sources 文件中重复写入。
