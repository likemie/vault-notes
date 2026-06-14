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

> [!claim] 核心主张
> 理论的基本立场、解释对象和核心问题，附 Argument citation。

> [!concept-lens]- 理论透镜
> - **解释对象**：该理论主要解释什么现象。
> - **核心机制**：该理论认为关键机制是什么。
> - **适用边界**：该理论在哪些情境下更有解释力。

> [!citation-card]- 关键表述
> 中文译文或中文原文。 [[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> Original/English: Original text or English translation.

---

## 核心命题

> [!finding-cards] 核心命题
> - **命题一**：说明其解释什么现象。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **命题二**：说明其与命题一的关系。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!logic-map]- 命题关系
> ```mermaid
> flowchart LR
>   A["前提"] --> B["机制"]
>   B --> C["结果"]
> ```

---

## 发展脉络

> [!timeline] 发展脉络
> - YYYY [[Person, A. A.]] 提出关键问题或概念。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - YYYY 理论被用于新的教育议题。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 认识论立场

> [!assumptions] 理论前提
> - **本体论**：简述该理论如何理解社会、制度或行动者。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **认识论**：简述该理论如何理解知识和证据。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **方法论含义**：常用研究方法，如 [[质性研究]]、[[民族志]]。

---

## 分析框架

> [!framework-table] 分析框架
> 只有资料足够时写。说明该理论如何转化为分析维度、变量、机制或解释路径。
> | 维度 | 用法 |
> |---|---|
> | 分析维度一 | 说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]] |

---

## 争议与批评

%% 根据实际材料选用 tension、critique-*、contrast-table；没有充分材料时可删除本节。 %%

> [!tension] 理论争议
> 按批评立场组织，说明批评针对理论前提、解释范围、方法论还是政治立场。
> - **立场 A**：观点说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **立场 B**：观点说明。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!critique] 批评索引
> - 批评描述，附立场。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> 链接到以此理论为框架的 Argument，并用一句话说明该研究如何使用理论。
> - [[Argument_Thomas_2000_RER]] — 使用该理论解释课程改革中的教师实践。

---

## 应用领域

> [!case] 应用领域索引
> - [[项目式学习]] — 一句话说明该理论如何支持该领域的研究或实践。
