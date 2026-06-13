---
title: <% tp.file.title %>
aliases: []
summary: ""
type: theory
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

%% 正文先按理论逻辑组织主题，再在主题内按时间、发展阶段或论证顺序排列；用 callout 区分核心主张、命题、立场、争议和应用。 %%

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


%% CONTENT_START: 以上为写作参考，以下为实际条目内容 %%
---

## 核心主张

> [!tip]
> 理论的基本立场、解释对象和核心问题，附 Argument citation。

> [!quote]
> 中文译文或中文原文。 [[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> Original/English: Original text or English translation.

---

## 核心命题

> [!abstract]
> 主要命题或子理论逐条列出，并说明命题之间如何连接。
> - 命题一：说明其解释什么现象。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 发展脉络

> [!note]
> 理论形成、扩展、转向和进入教育研究的过程。

> [!note]- 阶段名或时间段
> - YYYY [[Person, A. A.]] 提出关键问题或概念。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - YYYY 理论被用于新的教育议题。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 认识论立场

> [!info]
> 说明理论背后的本体论、认识论、主体观和社会观。
> - 本体论与认识论立场：简述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - 常用研究方法：[[质性研究]]、[[民族志]]。

---

## 分析框架

> [!abstract]
> 只有资料足够时写。说明该理论如何转化为分析维度、变量、机制或解释路径。
> - 分析维度一：说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 争议与批评

> [!warning]
> 按批评立场组织，说明批评针对理论前提、解释范围、方法论还是政治立场。
> - 批评描述，附立场。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 相关研究

> [!example]
> 链接到以此理论为框架的 Argument，并用一句话说明该研究如何使用理论。
> - [[Argument_Thomas_2000_RER]] — 使用该理论解释课程改革中的教师实践。

---

## 应用领域

> [!success]
> - [[项目式学习]] — 一句话说明该理论如何支持该领域的研究或实践。
