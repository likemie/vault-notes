# Schema：专著 — EPUB

触发格式：文件副档名为 `.epub`。若用户明确说明该 EPUB 是论文集／编著，则转入 `schema-edited-volume.md`。

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

EPUB 全程保留在 `books/` 文件夹，用 Obsidian Epub Reader 插件本地阅读。

Quartz 网页端阅读通过统一配置好的静态脚本实现：

```text
/static/jszip.min.js
/static/epub.min.js
/static/epub-loader.js
/static/epub-init.js
```

不要在每本书的 sources 文件或模板中重复写入 JS 源码。

---

## 进度追踪

不追踪章节处理进度，按需处理：

- 用户指定哪章就处理哪章，已处理的章节也可重新处理。
- 已处理章节内容累积在 Argument 的「各章概览」里，可作参考。

---

## 第一次处理新书

1. 读取 `vault-schema.md`。
2. 在 `books/` 下新建文件夹：`作者姓_年份_出版社/`。
3. 将 EPUB 放入：

```text
books/作者姓_年份_出版社/BookName.epub
```

4. 列出 EPUB 所有章节，只读文件结构，不读正文内容：

```bash
python3 -c "
import ebooklib
from ebooklib import epub
book = epub.read_epub('books/BOOKFOLDER/BookName.epub')
for i, item in enumerate(book.get_items_of_type(ebooklib.ITEM_DOCUMENT)):
    print(i, item.get_name())
"
```

5. 将章节列表展示给用户，停下等待用户指定章节。
6. 不处理正文内容，不创建 source 记录。
7. 用户指定章节后，进入单章处理流程。

---

## 单章处理流程

1. 读取 `vault-schema.md`。
2. 用 Python 提取用户指定章节的正文，只读该章，不读其他章节：

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

3. 基于章节内容扫描可提取条目。
4. 读取 `wiki/index.json`，将条目分为待更新和待新建两组。
5. 按 `vault-schema.md` 的更新／新建条目规则执行。
6. 将本章内容追加到 Argument 的「各章概览」：
   - 若 Argument 尚不存在 → 读取 `wiki/templates/template-argument-monograph.md`，在 `wiki/arguments/books/<book-folder>/` 新建。
   - 若 Argument 已存在 → 用 `str_replace` 追加本章内容到「各章概览」末尾或更新对应章节。
7. 在正文中自然使用 wikilink，在 `## 来源` 章节列出来源。
8. 不手动维护 YAML `related_*` 和 `sources`。
9. 运行标准同步与检查流程。
10. 停下，告知用户当前章节处理完成。

---

## 创建 source 记录与阅读页面

当用户要求建立 EPUB source 记录时，调用：

```bash
python3 scripts/source_record.py monograph-epub \
  --book-folder 作者姓_年份_出版社 \
  --file books/作者姓_年份_出版社/BookName.epub \
  --citation "作者姓, 名字缩写. (年份). 书名. 出版社." \
  --book-title "书名" \
  --authors "作者名" \
  --publisher "出版社" \
  --argument "[[Argument_作者姓_年份_出版社]]" \
  --extracted-to "[[其他条目]],[[其他条目2]]"
```

脚本会生成：

```text
books/作者姓_年份_出版社/作者姓_年份_出版社.md
```

并写入 EPUB Reader HTML：

```html
<div id="epub-viewer" style="width:100%;height:560px;border:1px solid rgb(204,204,204);" data-epub="/books/作者姓_年份_出版社/BookName.epub"></div>
```

完成后运行标准同步与检查流程。

---

## 整合 Argument

当用户发出整合指令后：

1. 读取 Argument 文件中已累积的「各章概览」。
2. 读取 `wiki/templates/template-argument-monograph.md`。
3. 按模板结构整合：
   - 全书研究问题
   - 理论框架
   - 论证结构
   - 主要发现
   - 关键引用
   - 局限性
4. 用 `str_replace` 在「各章概览」之前写入正式章节。
5. 「各章概览」保留在最后，作为原始章节记录。
6. 运行标准同步与检查流程。

---

## 注意事项

- 列出章节列表只读文件结构，不读正文内容。
- 必须等用户明确指定章节后，才读取该章正文。
- 每次只处理一章。
- 章节文本过长时，按小节拆分处理。
- source 记录由 `source_record.py monograph-epub` 生成。
