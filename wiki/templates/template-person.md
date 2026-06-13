---
title: <% tp.file.title %>
aliases: []
summary: ""
type: person
nationality: ""
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

%% 正文先按人物思想主题组织，再在生平、著作与思想发展章节内按时间排列。用 callout 区分简介、核心思想、影响、引用和争议。 %%

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
> `summary` 只用于索引说明，让读者一眼看出此人的身份、代表贡献和相关理论/概念。
> 写法：`国籍/身份 + 代表著作/理论贡献 + 对教育研究的意义`。
> 不写成传记摘要，不堆生平细节；无法概括时留空：`summary: ""`。
>
> [!warning]- Summary YAML 安全规则
> `summary` 外层必须使用双引号包裹：`summary: "一句话索引说明"`。
> 内容内部避开英文冒号 `:`、双引号 `"`、单引号 `'`；需要断句时优先使用中文标点。

> [!warning]- 表达规则
> - 句子不要中英混合；除专名、引文、公式、代码、APA citation 和无法翻译的固定术语外，句子主体使用中文表达。
> - 人名第一次出现必须使用全名；中文正文优先写成中文全名（英文全名），后文再出现可按语境使用中文名、姓氏或代称。
> - 缩写第一次出现必须写成中文（英文全称，缩写）；后文才可单独使用缩写。

> [!info]- 筛选标准
> - 有独立理论或概念贡献，提出有名称的理论、概念或框架。
> - 在领域内有持续影响力，被多篇论文反复引用，或代表一个学派／立场。
> - 文献专门讨论其思想，以该人物的思想作为主要理论资源并详细介绍。
> - 只是论文作者、顺带引用一次或只是受访者时，不建 Person 条目。

> [!info]- Frontmatter 格式规范
> - `tags` 用方括号列表，内容 tag 建议使用英文小写连字符。
> - 推荐 tag 前缀：`region/`、`field/`、`theory/`、`method/`、`discipline/`、`school/`。
> - `related_*` 由脚本自动同步；需要建立关系时在正文使用 wikilink。
> - 非 Argument 条目不写 YAML `sources`，不写正文 `## 来源`。

> [!info]- Person 命名与 aliases 规则
> Person 文件名和 `title` 使用常用英文全名，如 `Stephen Ball`、`Michael W. Apple`。
> `aliases` 写 APA 作者名、英文全名变体、中文全称和必要中文简称，如 `Ball, S. J.`、`Stephen J. Ball`、`斯蒂芬·鲍尔`。
> 不写单独英文姓氏作为 alias，如 `Ball`、`Apple`、`Young`。
> 中文简称只在人物非常著名或中文文献中常用时写，如 `杜威`、`皮亚杰`、`布迪厄`、`阿普尔`、`哈蒂`。


%% CONTENT_START: 以上为写作参考，以下为实际条目内容 %%
---

## 简介

> [!info]
> 身份、国籍、时代背景、主要活跃领域简述。重点说明此人在教育学、社会学、哲学或相关领域中的位置。

---

## 生平与职涯

> [!note]
> 人生轨迹、主要任职、重要活动，按时间顺序记录。资料不足时只写与思想形成有关的关键信息，不强行补传记细节。
> - YYYY 出生于／就读于／任职于…… [[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - YYYY 主要事件或转折点。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - YYYY 逝世（如适用）。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 主要著作

> [!abstract]
> APA 格式列出代表性著作，并用一句话概括每本著作的核心内容或理论贡献。没有足够资料时，只列已知著作，不补不存在的信息。

- Author, A. A. (YYYY). *Title*. Publisher. — 一句话概括核心内容。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 核心思想

> [!tip]
> 综合其主要著作和研究脉络，概括最核心的理论主张。不要与“主要著作”简单重复；这里应提炼跨著作、跨时期的稳定思想。

> [!quote]
> 中文译文或中文原文。 [[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> Original/English: Original text or English translation.

---

## 思想发展

> [!note]
> 可选模块。只有资料足够时才写。优先按著作、阶段或问题转向说明思想如何延续、转向或深化。

### YYYY — 著作名或阶段名

- 核心内容：
- 思想发展：
- 相关概念／理论：

---

## 影响

> [!success]
> 记录此人对后续理论、教育研究、政策话语、研究方法或具体学者的影响。
> - 影响了 [[理论名]] 在教育研究中的使用。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 格言／关键表述

> [!quote]
> 可选模块。只有能确认出处时才写。记录最能代表该人物思想的短句、格言或高频引用；无法确认原文出处时标注“待核”，不要编造。

> 中文译文或中文原文。 [[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> Original/English: Original text or English translation.

---

## 争议与批评

> [!warning]
> - 批评描述，说明批评对象、立场和证据。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
