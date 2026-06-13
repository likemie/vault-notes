---
title: <% tp.file.title %>
aliases: []
summary: ""
type: fact
subtype: event
region: ""
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
confidence: medium
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

%% 正文先按事件逻辑组织主题；背景、经过、影响、争议分开写，经过章节内部按时间排列。用 callout 改善阅读层次。 %%

>
> [!info]- 自动维护字段（对齐脚本）
> - `related_*` 由 `scripts/wiki_relations.py` 自动维护，AI 不手动填写。
> - 正文中的 wikilink 会同步到对应 `related_*`。
> - 非 Argument 条目不写 YAML `sources`，也不写正文 `## 来源`。
> - 来源性陈述使用 APA 短引用链接到对应 Argument，例如 `[[Argument_Ball_2008a_JEP|(Ball, 2008a, p. 12)]]`。
> - 正文自动补链由 `scripts/wiki_linker.py sync` 完成；`aliases` 是自动补链白名单。
> - 处理完成后只自动运行基础索引：`.venv/bin/python3 scripts/vault_index.py`。
> - 如需继续维护链接、关系和检查，先询问用户是否运行标准脚本流程。


> [!info]- Summary 规则（索引用，不是摘要）
> `summary` 只用于索引说明，让读者一眼看出本条目的对象、核心含义和使用场景。
> 写法：`对象类型 + 核心含义/贡献 + 教育研究中的意义`。
> 不围绕某一篇论文写摘要，不堆材料细节；无法概括时留空：`summary: ""`。
>
> [!warning]- Summary YAML 安全规则
> `summary` 外层必须使用双引号包裹：`summary: "一句话索引说明"`。
> 内容内部避开英文冒号 `:`、双引号 `"`、单引号 `'`；需要断句时优先使用中文标点。

> [!warning]- 表达规则
> - 句子不要中英混合；除专名、引文、公式、代码、APA citation 和无法翻译的固定术语外，句子主体使用中文表达。
> - 人名第一次出现必须使用全名；中文正文优先写成中文全名（英文全名），后文再出现可按语境使用中文名、姓氏或代称。
> - 缩写第一次出现必须写成中文（英文全称，缩写）；后文才可单独使用缩写。

> [!info]- Frontmatter 格式规范
> - `tags` 用方括号列表，内容 tag 使用英文小写连字符。
> - 推荐 tag 前缀：`region/`、`field/`、`theory/`、`method/`、`discipline/`、`policy/`、`theme/`。
> - `related_*` 若引用条目，必须写成带引号的 wikilink，如 `"[[Cultural Capital]]"`。
> - `related_*` 由脚本自动同步；需要建立关系时，在正文自然使用 wikilink。
> - 不确定是否已有条目时先写纯文字，不在 frontmatter 中写普通文本。

> [!info]- Fact Event 写法
> - 事件条目必须有明确时间、地点和主体。
> - 事实性陈述要标注 Argument citation，例如 `[[Argument_OECD_2012_Report|(OECD, 2012, p. X)]]`。
> - 不写 YAML `sources`，不写正文 `## 来源`。


> [!warning]- 写入规则（每次写入前必须执行）
> 1. 确定新内容属于哪个 `##` 章节。
> 2. 先判断新内容属于哪个主题或子主题，再判断该主题内部的时间位置、论证位置或概念层级。
> 3. 分点 ≥ 8 条时按主题建立 `###` 子主题，组内按时间或论证顺序排列；分点 < 8 条时按模板逻辑插入正确位置。
> 4. 写入前声明：「归属章节 > 子主题 > 插入位置」，再用 `str_replace` 精确写入。
> 5. 不使用来源以外的知识；资料不足时写“待核”或删除空章节。


%% CONTENT_START: 以上为写作参考，以下为实际条目内容 %%
---

## 背景

> [!info]
> 事件发生的社会、政治、教育或制度背景。说明为什么这一事件值得作为 Fact 条目记录。

---

## 经过

> [!note]
> 事件的主要经过，按时间顺序呈现。
> - YYYY-MM 事件节点。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!note]- 阶段名或时间段
> - YYYY-MM 关键节点。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - YYYY-MM 后续发展。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 关键文件／声明

> [!quote]
> 中文译文或中文原文。 [[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> Original/English: Original text or English translation.

---

## 影响与后果

> [!success]
> 对政策、学界、学校实践、社会舆论或制度安排的影响。
> - 影响描述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 争议与评论

> [!warning]
> 按立场组织不同解释和评论。
> - 立场一：评论描述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 相关概念／政策

> [!example]
> - [[国际比较评估]] — 一句话说明关系。
