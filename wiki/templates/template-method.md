---
title: <% tp.file.title %>
aliases: []
summary: ""
type: method
method_type: qualitative
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

%% 正文先按方法逻辑组织主题，再在主题内按时间、发展阶段或论证顺序排列；用 callout 区分定义、程序、适用场景、局限和案例。 %%

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

> [!info]- 方法案例规则
> - 非思辨/评论性文章，必须至少把一个核心方法案例记录到「使用此方法的研究」。
> - 方法案例只写一句话，链接当前 Argument，不展开文献摘要。



%% CONTENT_START: 以上为写作参考，以下为实际条目内容 %%
---

## 定义

> [!info]
> 方法的核心定义、研究对象、适用问题和基本单位，附 Argument citation。

> [!quote]
> 中文译文或中文原文。 [[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> Original/English: Original text or English translation.

---

## 认识论立场

> [!abstract]
> 属于哪个研究范式，依赖什么知识观、证据观和研究者角色。
> - 认识论立场：说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 研究程序

> [!example]
> 说明如何执行，按步骤、材料、样本、编码或分析单位组织。
> 1. 步骤一：说明。
> 2. 步骤二：说明。
> 3. 步骤三：说明。

---

## 资料与分析

> [!info]
> 说明常见资料类型、分析策略、质量控制方式和报告要求。
> - 资料类型：访谈、观察、文本、问卷、行政数据等。
> - 分析策略：编码、比较、建模、统计检验等。

---

## 适用场景

> [!success]
> 适合回答什么类型的问题，不适合回答什么类型的问题。
> - 适用场景：说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 局限性

> [!warning]
> 方法的主要限制、偏误来源、可推广性边界和伦理问题。
> - 局限描述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 相关理论

> [!tip]
> - [[建构主义]] — 一句话说明该理论如何支撑此方法。

---

## 使用此方法的研究

> [!example]
> - [[Argument_Lave_1991]] — 该研究使用此方法分析学习如何嵌入实践共同体。
