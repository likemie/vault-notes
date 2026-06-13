---
title: <% tp.file.title %>
authors:
  - "[[Author, A. A.]]"
summary: ""
type: argument
subtype: textbook
publication_type: book
book_title: ""
publisher: ""
year:
doi: ""
isbn: ""
citation_aliases: []
citation: ""
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
sources: []
part_of:
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

%% BEFORE USE:
1. Read wiki/templates/TEMPLATE-SPEC.md.
2. Read wiki/templates/CALLOUTS.md.
3. Then use this template.
%%

%% 教材 Argument 记录教材的知识推进结构；具体定义、分类、方法步骤、理论说明和案例优先沉淀到对应 wiki 条目。 %%

>
> [!info]- 自动维护字段
> - `title` 保持与文件名一致，使用稳定技术命名。
> - `authors` 使用 Person wikilink，每位作者单独一项。
> - `related_*` 与 YAML `sources` 由脚本维护。
> - `## 来源` 只列教材 source record wikilink。
> - 处理完成后只自动运行基础索引：`.venv/bin/python3 scripts/vault_index.py`。

> [!info]- Citation 规则
> - 教材没有 DOI 时，`doi` 可留空；若能确认 ISBN，写入 `isbn`。
> - `citation_aliases` 由 `scripts/citation_index.py` 根据 `authors` 和 `year` 自动维护，只保留 `Author, Year` 与 `Author (Year)` 两种基本形式。
> - 英文 alias 按 APA：双作者用 `&`，三位及以上用 `et al.`；中文教材若 `citation` 字段含中文作者名，会额外生成中文 alias，如 `郑雅君, 2023` 与 `郑雅君 (2023)`，双作者用“和”，三位及以上用“等”。
> - 同一作者同一年多部文献时，`citation_index.py` 自动追加 `a`、`b`、`c` 后缀。
> - 正文引用当前教材只写页码，如（p.12）或（pp.12–15）。
> - 正文引用其他已处理文献使用 APA 短引用，如 `(Ball, 2008a, p. 12)` 或 `Ball (2008a, p. 12)`。

> [!info]- 教材写作规则
> - 「章节结构」只保留 3–5 个最核心关联条目；不同章节尽量拉开差异。
> - 「章节概览」跟随教材自身知识推进逻辑，记录概念、理论、证据、案例、表格、图片和结论如何展开。
> - 已建条目只简单提及，详细内容写入具体 Concept / Theory / Method / Fact / Person 条目。
> - 「重要摘录」只保留有启发或表述精炼的观点，标注章节与页码。
> - 没有页码时只标注章节，不编造页码。

> [!warning]- 表达规则
> - 句子不要中英混合；除专名、引文、公式、代码、APA citation 和无法翻译的固定术语外，句子主体使用中文表达。
> - 人名第一次出现必须使用全名；中文正文优先写成中文全名（英文全名），后文再出现可按语境使用中文名、姓氏或代称。
> - 缩写第一次出现必须写成中文（英文全称，缩写）；后文才可单独使用缩写。

%% CONTENT_START: 以上为写作参考，以下为实际条目内容 %%
---

## 章节结构

| 章节 | 内容概要 | 主要关联条目 |
|---|---|---|
| 第X章 章节标题 | 用一两句话说明这一章主要讲什么。 | Concept A、Theory B、Fact C |

---

## 章节概览

### 第X章 章节标题

#### 概览

跟随教材自身逻辑，记录知识如何展开。figure 写图片占位；table 只要可读就复刻为 Markdown 表格。已建条目只简单提及，详细内容写入具体条目。

---

## 重要摘录

> [!quote]
> 中文译文或中文原文。（第X章，p.X）
> Original/English: Original text or English translation.

---

## 来源

%% 只列教材 source record wikilink。 %%

- [[Source_Name]]
