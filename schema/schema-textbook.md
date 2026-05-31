# Schema：教材（Textbook）

触发标识：用户标注「教材」，或说明材料来自教材、教科书、课程用书、入门读本。

---

## 核心原则

- 用户按章节向 AI 提供文本，AI 每次只处理当前章节。
- 先确定 `<book-folder>`，并建立 `books/<book-folder>/`；后续 source 记录、整合书籍文件和阅读页面文件名可与 `<book-folder>` 保持一致。
- 在所有章节处理完成前，不创建 source 记录，不创建阅读页面。
- 章节处理结果累积到教材 Argument 的「章节结构」「章节概览」和「重要摘录」。
- 具体定义、分类、争议、例子、方法步骤和理论说明，优先沉淀到对应 Concept / Theory / Method / Fact / Person 条目。
- 教材面向初学者；新建 Concept / Theory / Method / Fact / Person 条目时应适当详细。
- 教材 Argument 页只简单提及已经建立条目的概念、理论、方法、事实和人物，不在论证页展开；详细内容在具体条目里展开。
- 章节概览中自然使用相关术语；wikilink 由 `wiki_linker.py` 自动补充。
- 每次章节处理完成后，只自动运行 `.venv/bin/python3 scripts/wiki_index.py`，随后询问用户是否运行标准脚本流程。

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
```

`<book-folder>` 建议使用：

```text
作者姓_年份_出版社
```

---

## 教材 Argument 记录要求

`template-argument-textbook.md` 固定保留：

```markdown
## 章节结构

## 章节概览

## 重要摘录

## 来源
```

「章节结构」表格只保留三列：

```markdown
| 章节 | 内容概要 | 主要关联条目 |
|---|---|---|
| 第X章 章节标题 | 用一两句话说明这一章主要讲什么。 | Concept A、Theory B、Fact C |
```

`主要关联条目` 只列 3–5 个最核心的 Concept / Theory / Method / Fact / Person；不同章节的主要关联条目尽量拉开差异，避免每章机械重复同一组条目。

「章节概览」按教材自身的知识推进逻辑组织内容，跟随作者每一步思路，记录概念、理论、证据、案例、表格、图片和结论如何依次展开。建立条目的内容只简单提及，不在教材 Argument 页展开；详细内容进入具体条目。图片、表格和新建条目的 Argument 提及规则按 `vault-schema.md` 执行。

每章追加时使用：

```markdown
### 第X章 章节标题

#### 概览

跟随教材自身逻辑，记录作者每一步思路如何展开。文本表格和图片按 `vault-schema.md` 处理：

> [!example]- 图片占位
> 图X-X：名称  
> ![](https://img.mylikemie.icu/books/<book-folder>/figures/Figure_X-X_Descriptive_Name.jpg)
```

写作时不以“论文 / 本文 / 本章 / 作者 / 研究者 / 本研究 / 论证”作为常规主语，直接叙述论证、证据和结论。

「重要摘录」从第一章开始持续补充，只保留有意思、有启发或表述精炼的观点。每条摘录必须标注章节与页码；如果用户提供的文本没有页码，只能记录章节信息，不得编造页码。

---

## 单章处理流程

当用户发送某一章文本时：

1. 读取 `vault-schema.md` 和 `schema/schema-textbook.md`。
2. 只处理用户当前发送的章节文本。
3. 扫描当前章节中可提取或更新的 Concept / Theory / Method / Person / Fact / Argument。
4. 读取 `wiki/index.json`，判断候选条目是否已存在。
5. 更新已有条目：读取目标文件，判断插入位置，使用 `str_replace` 精确整合。
6. 新建条目：只读取对应模板，写入对应正式文件夹；教材来源的新条目面向初学者，应适当详细，并标注章节与页码。
7. 更新或新建教材 Argument：
   - 位置：`wiki/arguments/books/<book-folder>/Argument_<book-folder>.md`
   - 若不存在，读取 `wiki/templates/template-argument-textbook.md` 新建。
   - 若已存在，将当前章节内容整合进「章节结构」「章节概览」和「重要摘录」。
   - 「章节结构」中每章只保留 3–5 个核心关联条目；不同章节尽量选择不同的核心条目，避免重复。
   - 「章节概览」跟随作者每一步思路，记录概念、理论、证据、案例、表格和结论如何依次展开；已建条目只简单提及。
   - 文本表格和图片按 `vault-schema.md` 处理。
8. 在 `## 来源` 章节列出来源。
9. 执行脚本运行规则。
10. 当前章节处理完成后停止。

---

## 全书完成后的 source 记录

当用户提供整合后的 PDF / EPUB 并要求建立 source 记录时：

1. 确认文件位于：

```text
books/<book-folder>/<book-folder>.pdf
```

或：

```text
books/<book-folder>/<book-folder>.epub
```

2. PDF 教材可调用：

```bash
.venv/bin/python3 scripts/source_record.py monograph-pdf \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.pdf \
  --citation "作者姓, 名字缩写. (年份). 书名. 出版社." \
  --book-title "书名" \
  --authors "作者名" \
  --publisher "出版社" \
  --argument "[[Argument_<book-folder>]]"
```

3. EPUB 教材可调用：

```bash
.venv/bin/python3 scripts/source_record.py monograph-epub \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.epub \
  --citation "作者姓, 名字缩写. (年份). 书名. 出版社." \
  --book-title "书名" \
  --authors "作者名" \
  --publisher "出版社" \
  --argument "[[Argument_<book-folder>]]"
```

4. `source_record.py` 生成：

```text
books/<book-folder>/<book-folder>.md
```

5. 执行脚本运行规则。

---

## 脚本运行规则

处理完成后，AI 只自动运行索引脚本：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
.venv/bin/python3 scripts/wiki_index.py
```

随后询问用户是否运行标准脚本流程。只有用户确认后，才运行：

```bash
cd /Users/shaoyangwu/Documents/MyNotes
.venv/bin/python3 scripts/wiki_linker.py sync
.venv/bin/python3 scripts/wiki_relations.py sync
.venv/bin/python3 scripts/wiki_index.py
.venv/bin/python3 scripts/vault_lint.py
```
