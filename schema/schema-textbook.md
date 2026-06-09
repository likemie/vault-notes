# Schema：教材（Textbook）

触发标识：用户说明材料为教材、教科书、课程用书、入门读本。

---

## 核心原则

- 每次只处理用户当前发送的一章。
- 处理开始时确定 `<book-folder>`，并使用 `books/<book-folder>/` 与 `wiki/arguments/books/<book-folder>/`。
- 所有章节处理完成前，不创建 source 记录，不创建阅读页面。
- 教材 Argument 使用 `wiki/templates/template-argument-textbook.md`。
- 章节处理结果累积到「章节结构」「章节概览」和「重要摘录」。
- 具体定义、分类、争议、例子、方法步骤和理论说明优先沉淀到对应 Concept / Theory / Method / Fact / Person 条目。
- 教材来源的新条目面向初学者，说明应适当详细。
- Concept / Theory / Method / Fact / Person 条目不写 YAML `sources` 和正文 `## 来源`；来源性陈述通过 Argument 链接进入 `related_arguments`。
- 图片、表格、新建条目提及规则和脚本运行规则按 `vault-schema.md` 执行；基础索引统一运行 `.venv/bin/python3 scripts/vault_index.py`。

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

`<book-folder>` 使用 `Author_Year_Publisher` 或稳定的英文教材短名。

---

## 教材 Argument 记录

`template-argument-textbook.md` 固定保留：

```markdown
## 章节结构
## 章节概览
## 重要摘录
## 来源
```

「章节结构」只保留三列：

```markdown
| 章节 | 内容概要 | 主要关联条目 |
|---|---|---|
| 第X章 章节标题 | 用一两句话说明这一章主要讲什么。 | Concept A、Theory B、Fact C |
```

`主要关联条目` 只列 3–5 个最核心的 Concept / Theory / Method / Fact / Person；不同章节尽量拉开差异。

「章节概览」跟随教材自身知识推进逻辑，记录概念、理论、证据、案例、表格、图片和结论如何展开。已建条目只简单提及，详细内容写入具体条目。

「重要摘录」只保留有启发或表述精炼的观点，标注章节与页码。没有页码时只标注章节，不编造页码。

---

## 单章处理流程

1. 读取 `vault-schema.md` 和 `schema/schema-textbook.md`。
2. 只处理当前章节文本。
3. 扫描可提取或更新的 Concept / Theory / Method / Person / Fact / Argument。
4. 读取 `wiki/index.json` 判断候选条目是否已存在。
5. 更新已有条目或按模板新建条目。
6. 更新或新建 `wiki/arguments/books/<book-folder>/Argument_<book-folder>.md`。
7. 将当前章节整合进「章节结构」「章节概览」和「重要摘录」。
8. 在 `## 来源` 列出 source wikilink。
9. 执行 `vault-schema.md` 的脚本运行规则，即运行 `.venv/bin/python3 scripts/vault_index.py`。
10. 当前章节处理完成后停止。

---

## Source 记录和阅读页面

用户提供整合后的 PDF / EPUB 并要求建立 source 记录时，文件放在：

```text
books/<book-folder>/<book-folder>.<ext>
```

PDF：

```bash
.venv/bin/python3 scripts/source_record.py monograph-pdf \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.pdf \
  --citation "Author, A. A. (Year). Book title. Publisher."
```

EPUB：

```bash
.venv/bin/python3 scripts/source_record.py monograph-epub \
  --book-folder <book-folder> \
  --file books/<book-folder>/<book-folder>.epub \
  --citation "Author, A. A. (Year). Book title. Publisher."
```

执行 `vault-schema.md` 的脚本运行规则，即运行 `.venv/bin/python3 scripts/vault_index.py`。
