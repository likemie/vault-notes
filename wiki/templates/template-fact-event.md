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

%% Fact Event 页写事件、项目、组织行动或可核查事实。具体字段、引用、写入和 callout 规则见 TEMPLATE-SPEC.md 与 CALLOUTS.md；正式条目不得保留这些说明注释。 %%

%% TEMPLATE BODY: 生成正式条目时删除所有模板说明注释。 %%
---

## 背景

> [!abstract] 事件背景
> 说明事件发生的时间、地点、主体和社会、政治、教育或制度背景。只写可由来源支持的事实。

---

## 经过

> [!timeline] 事件经过
> 事件的主要经过，按时间顺序呈现；如果节点很多、阶段差异明显，改用下方 `[!phase]` 或 `[!dev-timeline]` 分阶段，不要把复杂过程挤成单条时间线。
> - YYYY-MM-DD 事件节点：主体、行动和直接结果。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!phase]- 阶段名或时间段
> - YYYY-MM 关键节点。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - YYYY-MM 后续发展。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!dev-timeline]- 复杂阶段时间线
> - **YYYY–YYYY 阶段一**：说明阶段主题、关键行动者和转折点。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
>   - YYYY-MM 子事件或关键节点。
>   - YYYY-MM 后续发展。

---

## 关键文件／声明

> [!citation-card] 关键文件或声明
> 中文译文或中文原文。 [[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> Original text or English translation.

---

## 影响与后果

> [!finding-cards] 影响与后果
> 对政策、学界、学校实践、社会舆论或制度安排的影响。
> - **政策影响**：影响描述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **实践影响**：影响描述。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **知识影响**：对概念、理论或研究议程的影响。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

---

## 争议与评论

%% 根据材料选择保留：如果只有单一争议焦点，用 tension；如果有多类行动者或评论者，先用 actor-grid 区分视角，再用 tension 展开；代表性评论原文用 citation-card。 %%

> [!actor-grid] 评论视角图
> - **当事方 / 机构视角**：说明该主体如何界定事件、责任或后果。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **政策 / 制度视角**：说明评论如何指向规则、治理、资源或问责。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **学术 / 方法视角**：说明研究者如何解释事件机制、证据或概念。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **公共 / 媒体视角**：说明舆论、媒体或公众如何框定事件。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]

> [!tension] 争议焦点
> - **焦点一**：不同评论者在哪个事实、责任、价值或解释上发生分歧。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **焦点二**：说明另一组分歧，或删除本条。

> [!citation-card]- 代表性评论
> 中文译文或中文原文。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> Original text or English translation.

---

## 相关概念／政策

> [!ref-table] 相关条目索引
> | 条目 | 关系 | 来源 |
> |---|---|---|
> | [[国际比较评估]] | 一句话说明关系。 | [[Argument_Author_Year_Journal|(Author, Year, p. X)]] |
