# Schema：专著 — EPUB

触发标识：文件副档名为 `.epub`，或用户说明材料来自 EPUB 专著。

---

## 核心原则

- EPUB 文件保留在 `books/` 文件夹中。
- 首次处理时只列出章节结构，不读取正文。
- 用户指定章节后，AI 每次只处理该章正文。
- 已处理章节内容累积到全书 Argument 的「各章概览」。
- 只有用户要求整合全书 Argument 时，才从「各章概览」提炼正式论证结构。
- 只有整本书需要建立阅读页面时，才新建书籍 source 记录。
- `related_*` 与 `sources` 不要求 AI 手动维护，由脚本根据正文 wikilink 与 `## 来源` 自动同步。

---

## 文件夹结构

```text
books/
  作者姓_年份_出版社/
    BookName.epub
    作者姓_年份_出版社.md

wiki/arguments/books/<book-folder>/
  Argument_作者姓_年份_出版社.md
```

说明：

- EPUB 全程保留在 `books/<book-folder>/`。
- `作者姓_年份_出版社.md` 是整本书 source 记录，需要建立阅读页面时再创建。
- 全书 Argument 放在 `wiki/arguments/books/<book-folder>/`。

---

## Quartz EPUB 阅读脚本

Quartz 网页端阅读通过统一静态脚本实现：

```text
/static/jszip.min.js
/static/epub.min.js
/static/epub-loader.js
/static/epub-init.js
```

不要在每本书的 source 文件或模板中重复写入 JS 源码。

---

## 首次处理新书

1. 读取 `vault-schema.md`。
2. 读取 `books/schema-monograph-epub.md`。
3. 在 `books/` 下新建文件夹：

```text
books/作者姓_年份_出版社/
```

4. 将 EPUB 放入该文件夹。
5. 用 Python 只列出 EPUB 章节结构，不读取正文内容：

```bash
python3 -c "
import ebooklib
from ebooklib import epub
book = epub.read_epub('books/BOOKFOLDER/BookName.epub')
for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)):
    print(i, item.get_name())
"
```

6. 将章节列表展示给用户，并停止：

```text
以上是全书章节列表，请告知需要处理哪一章。
```

---

## 单章处理流程

当用户指定某一章时：

1. 读取 `vault-schema.md`。
2. 读取 `books/schema-monograph-epub.md`。
3. 只提取用户指定章节的正文：

```bash
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
```

4. 基于当前章节文本扫描可提取条目：
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
7. 按 `vault-schema.md` 更新或新建条目。
8. 更新或新建全书 Argument：

```text
wiki/arguments/books/<book-folder>/Argument_作者姓_年份_出版社.md
```

若不存在，读取：

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

9. 将当前章节内容整合进「各章概览」。
10. 维护正文 wikilink 和 `## 来源`；不手动维护 `related_*`。
11. 运行：

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

12. 当前章节处理完成后停止。

---

## 重新开始

如果 session 重开：

1. 读取 `vault-schema.md`。
2. 读取 `books/schema-monograph-epub.md`。
3. 只列出 EPUB 章节结构，不读取正文。
4. 等待用户指定章节。
5. 用户指定后执行单章处理流程。

---

## 整合 Argument

当用户发出整合全书 Argument 的指令后：

1. 读取全书 Argument 中的「各章概览」。
2. 读取 `wiki/templates/template-argument-monograph.md`。
3. 从各章概览中提炼：
   - 全书研究问题
   - 理论框架
   - 核心概念
   - 论证结构
   - 章节推进关系
   - 主要发现
   - 关键引用
   - 局限性与批评
4. 用 `str_replace` 在「各章概览」之前写入正式章节。
5. 保留「各章概览」作为原始章节记录。
6. 运行：

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

---

## 建立 source 记录与阅读页面

当用户要求为整本 EPUB 建立 source 记录或阅读页面时：

1. 新建：

```text
books/作者姓_年份_出版社/作者姓_年份_出版社.md
```

2. source 记录格式：

```markdown
---
title: 作者姓_年份_出版社
summary: ""
type: source
subtype: monograph-epub
citation: "作者姓, 名字缩写. (年份). 书名. 出版社."
book_title: ""
authors: []
publisher: ""
book_file: "books/作者姓_年份_出版社/BookName.epub"
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

## EPUB Reader

<div id="epub-viewer" style="width:100%;height:560px;border:1px solid rgb(204,204,204);" data-epub="/books/作者姓_年份_出版社/BookName.epub"></div>

---

## Notes

- Obsidian 本地阅读用 Epub Reader 插件直接打开 EPUB。
- Quartz 网页端通过 `/static/` 中已配置脚本渲染。
- 不要在本文件中重复写入 `epub-loader.js` 或 `epub-init.js` 源码。
```

3. 根据已经提取的条目补全 `extracted_to`。
4. 运行：

```bash
python3 scripts/wiki_index.py
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
```

---

## 注意事项

- 列章节时只读 EPUB 文件结构，不读正文内容。
- 必须等用户指定章节后，才读取该章正文。
- 每次只处理一章。
- 章节文本过长时，按小节拆分处理，但仍视为同一章。
- `related_*` 由 `wiki_relations.py` 自动维护，AI 不手动填写。
- `sources` 由 `## 来源` 章节同步，AI 只需维护正文来源列表。
- `extracted_to` 必须使用数组格式，元素为带引号的 wikilink。
