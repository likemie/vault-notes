# Schema：专著（Monograph）— PDF

触发标识：用户标注「专著」或说明该材料来自专著 PDF。

---

## 核心原则

- 用户按章节向 AI 提供文本。
- AI 每次只处理用户当前发送的一章。
- 不自动拆分 PDF。
- 不读取整本 PDF。
- 在整本书处理完成前，不创建 source 记录，不创建阅读页面。
- 章节处理结果累积到全书 Argument 的「各章概览」。
- 用户提供整本 PDF 并要求建立 source 记录后，使用 `scripts/source_record.py monograph-pdf` 建立书籍 source 记录和阅读页面。
- 每次章节处理完成后执行脚本运行规则：只自动运行 `python3 scripts/wiki_index.py`，随后询问用户是否运行标准脚本流程。

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

---

## 单章处理流程

当用户发送某一章文本时：

1. 读取 `vault-schema.md`。
2. 只处理用户当前发送的章节文本。
3. 基于当前章节扫描可提取条目：
   - Concept
   - Theory
   - Method
   - Person
   - Fact
   - Argument
4. 读取 `wiki/index.json` 判断候选条目是否已存在。
5. 将候选分为：
   - 待更新条目
   - 待新建条目
6. 更新已有条目：
   - 读取目标文件。
   - 判断插入位置。
   - 使用 `str_replace` 精确整合。
7. 新建条目：
   - 只读取对应模板。
   - 写入对应正式文件夹。
8. 更新或新建全书 Argument：
   - 位置：`wiki/arguments/books/<book-folder>/Argument_作者姓_年份_出版社.md`
   - 若不存在，读取 `wiki/templates/template-argument-monograph.md` 新建。
   - 若已存在，将当前章节内容整合进「各章概览」。
9. 在正文中自然使用 wikilink，在 `## 来源` 章节列出来源。
10. 不手动维护 YAML `related_*` 和 `sources`。
11. 执行脚本运行规则：只自动运行 `python3 scripts/wiki_index.py`，随后询问用户是否运行标准脚本流程。

12. 当前章节处理完成后停止。

---

## 全书完成后的 source 记录

当用户提供整本 PDF 并要求建立 source 记录时：

1. 确认 PDF 位于：

```text
books/作者姓_年份_出版社/BookName.pdf
```

2. 调用：

```bash
python3 scripts/source_record.py monograph-pdf \
  --book-folder 作者姓_年份_出版社 \
  --file books/作者姓_年份_出版社/BookName.pdf \
  --citation "作者姓, 名字缩写. (年份). 书名. 出版社." \
  --book-title "书名" \
  --authors "作者名" \
  --publisher "出版社" \
  --argument "[[Argument_作者姓_年份_出版社]]" \
  --extracted-to "[[其他条目]],[[其他条目2]]"
```

3. `source_record.py` 会生成：

```text
books/作者姓_年份_出版社/作者姓_年份_出版社.md
```

4. 执行脚本运行规则：只自动运行 `python3 scripts/wiki_index.py`，随后询问用户是否运行标准脚本流程。

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
6. 执行脚本运行规则：只自动运行 `python3 scripts/wiki_index.py`，随后询问用户是否运行标准脚本流程。

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

`wiki_relations.py` 负责同步 wiki 条目的 `related_*` 与 YAML `sources`，并根据 wiki 条目的 `## 来源` 反向维护 source record 的 `extracted_to`。`sources/` 和 `books/` 下的 source record 不参与 `related_*` 自动维护。

## 注意事项

- 每次只处理当前章节。
- 章节文本过长时，可按小节分批处理，但仍视为同一章。
- 所有来源性陈述必须标注页码。
- 如果用户提供的章节文本没有页码，只能记录无页码信息；不得编造页码。
- source 记录和阅读页面只在用户提供整本 PDF 后建立；后续 `extracted_to` 由 `wiki_relations.py` 反向同步。
