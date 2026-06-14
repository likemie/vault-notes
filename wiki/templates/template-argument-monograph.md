---
title: <% tp.file.title %>
authors:
  - "[[Author, A. A.]]"
summary: ""
type: argument
subtype: monograph
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

%% 专著 Argument 粒度由用户指定：整本书一个 Argument，或全书 overview + 分章节 Argument。 %%

>
> [!info]- 自动维护字段
> - `title` 保持与文件名一致，使用稳定技术命名。
> - `authors` 使用 Person wikilink，每位作者单独一项。
> - `related_*` 与 YAML `sources` 由脚本维护。
> - `## 来源` 只列整本书 source record wikilink。
> - 处理完成后只自动运行基础索引：`.venv/bin/python3 scripts/vault_index.py`。

> [!info]- Citation 规则
> - 著作没有 DOI 时，`doi` 可留空；若能确认 ISBN，写入 `isbn`。
> - `citation_aliases` 由 `scripts/citation_index.py` 根据 `authors` 和 `year` 自动维护，只保留 `Author, Year` 与 `Author (Year)` 两种基本形式。
> - 英文 alias 按 APA：双作者用 `&`，三位及以上用 `et al.`；中文著作若 `citation` 字段含中文作者名，会额外生成中文 alias，如 `郑雅君, 2023` 与 `郑雅君 (2023)`，双作者用“和”，三位及以上用“等”。
> - 同一作者同一年多部文献时，`citation_index.py` 自动追加 `a`、`b`、`c` 后缀。
> - 正文引用当前书籍只写页码，如（p.12）或（pp.12–15）。
> - 正文引用其他已处理文献使用 APA 短引用，如 `(Ball, 2008a, p. 12)` 或 `Ball (2008a, p. 12)`。

> [!info]- Summary 规则
> `summary` 用一句话说明全书的核心论证，不写成书籍简介。
> 写法：`研究对象/核心问题 + 理论视角/材料 + 全书论证或发现`。

> [!warning]- 表达规则
> - 句子不要中英混合；除专名、引文、公式、代码、APA citation 和无法翻译的固定术语外，句子主体使用中文表达。
> - 人名第一次出现必须使用全名；中文正文优先写成中文全名（英文全名），后文再出现可按语境使用中文名、姓氏或代称。
> - 缩写第一次出现必须写成中文（英文全称，缩写）；后文才可单独使用缩写。

> [!warning]- 章节处理规则
> - Argument 粒度按用户指定。
> - 若采用整本书一个 Argument，每章处理结果追加到「各章概览」。
> - 若采用分章节 Argument，本页作为全书 overview，只保留章节索引、章节短摘要和跨章综合。
> - 「各章概览」只记录章节问题和论证链条，不写成完整小型笔记；详细章节内容写入章节 Argument。
> - 关键引用持续补充到「关键引用」章节，标注章节与页码。
> - 没有页码时只标注章节，不编造页码。

%% CONTENT_START: 以上为写作参考，以下为实际条目内容 %%
---

## 研究问题

> [!question]
> 直接陈述全书要回答的核心问题，综合各章提炼，不以“本书、本章、作者、研究者、论证”等作常规句子主语。

---

## 理论框架

> [!framework-table] 理论框架
> | 理论 / 概念 | 在全书中的作用 |
> |---|---|
> | [[理论名]] | 一句话说明如何贯穿全书运用。（p.X） |

---

## 研究方法

> [!method-panel] 研究方法
> | 环节 | 说明 |
> |---|---|
> | 方法 | [[研究方法名]] |
> | 样本 | 描述。（p.X） |
> | 数据来源 | 描述。（p.X） |

---

## 论证结构

> [!argument-map] 全书论证路径
> 综合各章要点，详细拆解整体论证脉络。每一个论证步骤独立成段，步骤之间使用分割线。抽象处加入例子。

1. 问题起点。

---

2. 理论／概念工具。

---

3. 关键前提。

---

4. 证据支撑。

---

5. 中间推论。

---

6. 结论。

---

7. 可疑跳跃。

---

## 各章概览

### 第X章 章节标题

> [!chapter-question]

说明该章要回答的问题，或它在全书论证中的位置。

#### 论证链条

按前提、证据、中间推论、结论拆解章节论证。每一个论证步骤独立成段，步骤之间使用分割线。

---

## 主要发现

> [!finding-cards] 主要发现
> 综合各章提炼的核心发现，附页码来源。
> - **发现一**：发现描述。（p.X）
> - **发现二**：发现描述。（p.X）

> [!stat-cards]- 核心数据
> 有具体数字、样本量、效应量或比例时，单独放在这里。（p.X）

---

## 关键引用

> [!citation-card] 关键引用
> 中文译文。（第X章，p.X）
> Original/English: Original text or English translation.

---

## 自述局限

> [!warning]
> 只写书中明确自述的局限、边界条件或未来研究方向，并附页码。不要补写外部批评或原书没有说明的缺陷。

---

## 来源

%% 只列整本书 source record wikilink。 %%

- [[Source_Name]]
