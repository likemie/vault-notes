# Schema：专著（Monograph）

触发标识：用户标注「专著」或说明该材料来自书籍材料。

---

## 核心原则

- 用户按章节向 AI 提供文本。
- AI 每次只处理用户当前发送的一章。
- 在整本书处理完成前，不创建 source 记录，不创建阅读页面。
- 处理开始时先确定 `<book-folder>`；后续 source 记录、整合书籍文件和阅读页面文件名可与 `<book-folder>` 相同。
- 章节处理结果累积到全书 Argument 的「各章概览」。
- 用户提供整合后的书籍文件并要求建立 source 记录后，根据文件格式生成阅读页面：PDF 与 EPUB 的处理流程相同，但阅读页写法不同。
- 每次章节处理完成后执行脚本运行规则：只自动运行 `python3 scripts/wiki_index.py`，随后询问用户是否运行标准脚本流程。

---

## 文件夹结构

```text
books/
  <book-folder>/
    <book-folder>.<ext>
    <book-folder>.md
    figures/
      argument-structure.svg

wiki/arguments/books/<book-folder>/
  Argument_<book-folder>.md
```

---

## 单章 Argument 记录要求

`template-argument-monograph.md` 中，「各章概览」用于保留每章在全书论证中的位置，不写成完整小型笔记。每章追加时只记录两个核心内容：

```markdown
### 第X章 章节标题

#### 章节问题
说明该章要回答的问题，或它在全书论证中的位置。

#### 论证链条
按前提、证据、中间推论、结论拆解章节论证，不直接跳到结论。每一个论证步骤独立成段，步骤之间使用 `---` 分割线。
```

关键引用不放入「各章概览」里堆积，而是从第一章开始持续补充到全书 Argument 的「关键引用」章节。每条引用必须标注章节与页码；如果用户提供的文本没有页码，只能记录章节信息，不得编造页码。

若章节涉及 figure / 图片等图像型材料，不读取独立 schema；先在当前 Argument 的对应章节中写图片占位，后续由用户手动补图。文本表格、可复制表格或可转写表格应尽量直接读取、整理为 Markdown 表格。

---

## 单章处理流程

当用户发送某一章文本时：

1. 读取 `vault-schema.md`。
2. 只处理用户当前发送的章节文本。
3. 基于当前章节扫描可提取条目：Concept / Theory / Method / Person / Fact / Argument。
4. 读取 `wiki/index.json` 判断候选条目是否已存在。
5. 将候选分为待更新条目和待新建条目。
6. 更新已有条目：读取目标文件，判断插入位置，使用 `str_replace` 精确整合。
7. 新建条目：只读取对应模板，写入对应正式文件夹。
8. 更新或新建全书 Argument：
   - 位置：`wiki/arguments/books/<book-folder>/Argument_<book-folder>.md`
   - 若不存在，读取 `wiki/templates/template-argument-monograph.md` 新建。
   - 若已存在，将当前章节内容整合进「各章概览」。
   - 「各章概览」只记录章节问题和论证链条。
   - 关键引用直接追加到「关键引用」章节，并标注章节与页码。
9. 在 `## 来源` 章节列出来源；不手动维护 YAML `related_*` 和 `sources`。
10. 执行脚本运行规则。
11. 当前章节处理完成后停止。

---

## 全书完成后的 source 记录和阅读页面

当用户提供整合后的书籍文件并要求建立 source 记录时：

1. 确认文件位于：

```text
books/<book-folder>/<book-folder>.<ext>
```

2. PDF 与 EPUB 使用同一套专著处理流程，但创建阅读页面时按文件格式分支。

### PDF 或其他可直接嵌入文件

```bash
python3 scripts/source_record.py monograph-pdf \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.pdf \
  --citation "作者姓, 名字缩写. (年份). 书名. 出版社." \
  --book-title "书名" \
  --authors "作者名" \
  --publisher "出版社" \
  --argument "[[Argument_<book-folder>]]"
```

### EPUB

```bash
python3 scripts/source_record.py monograph-epub \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.epub \
  --citation "作者姓, 名字缩写. (年份). 书名. 出版社." \
  --book-title "书名" \
  --authors "作者名" \
  --publisher "出版社" \
  --argument "[[Argument_<book-folder>]]"
```

EPUB 阅读页使用已配置的静态脚本：

```text
/static/jszip.min.js
/static/epub.min.js
/static/epub-loader.js
/static/epub-init.js
```

EPUB source record 中只写阅读器容器，不重复写入 JS 源码：

```html
<div id="epub-viewer" style="width:100%;height:560px;border:1px solid rgb(204,204,204);" data-epub="/books/<book-folder>/<book-folder>.epub"></div>
```

3. `source_record.py` 生成：

```text
books/<book-folder>/<book-folder>.md
```

4. 执行脚本运行规则。
---

## 整合 Argument

当用户要求整合全书 Argument 时：

1. 读取全书 Argument 中的「各章概览」。
2. 读取 `wiki/templates/template-argument-monograph.md`。
3. 按模板结构整合各章材料，提炼全书研究问题、理论框架、研究方法、核心概念、论证结构、章节推进关系、主要发现、关键引用和自述局限。
4. 从各章概览中筛选最有代表性的发现与引用，分别写入「主要发现」和「关键引用」；不要把所有章节记录机械搬入正式章节。
5. 用 `str_replace` 在「各章概览」之前写入正式论证结构。
6. 保留「各章概览」作为原始章节记录。
7. 执行脚本运行规则。

---

## 脚本运行规则

处理完成后，AI 只自动运行索引脚本：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/wiki_index.py
```

随后询问用户是否运行标准脚本流程。只有用户确认后，才运行：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
python3 scripts/wiki_linker.py sync
python3 scripts/wiki_relations.py sync
python3 scripts/wiki_index.py
python3 scripts/vault_lint.py
```

必要时全量运行：

```bash
python3 scripts/wiki_linker.py sync --full
python3 scripts/wiki_relations.py sync --full
python3 scripts/vault_lint.py --full
```

---

## 注意事项

- 每次只处理当前章节。
- 章节文本过长时，可按小节分批处理，但仍视为同一章。
- 所有来源性陈述必须标注页码。
- 如果用户提供的章节文本没有页码，只能记录无页码信息；不得编造页码。
- source 记录和阅读页面只在用户提供整合后的书籍文件后建立；EPUB 阅读页必须使用 epub.js 阅读器容器；后续 `extracted_to` 由 `wiki_relations.py` 反向同步。
