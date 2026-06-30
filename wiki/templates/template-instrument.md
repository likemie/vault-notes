---
title: <% tp.file.title %>
aliases: []
summary: ""
type: instrument
instrument_type: scale
developers: []
original_year: ""
languages: []
item_count: ""
administration_mode: self-report
response_format: ""
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments: []
confidence: medium
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

---

## 工具定位

%% 单一工具的整体说明使用 callout，不做键值表。 %%

> [!instrument-profile] <工具>
> - **工具类型** 量表、问卷、测验、清单、评分规程、观察工具、访谈工具或其他测量工具。
> - **开发者与年份** 谁在何时开发，基于什么研究或实践需求。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
> - **测量目的** 用于筛查、诊断、描述、分组、预测、评价还是研究测量。
> - **实施方式** 自陈、他评、观察、访谈、纸笔、计算机、自适应或其他方式。

> [!citation-card]- 官方定义或开发者表述
> 中文译文或中文原文。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
>
> *Original text or English translation.*

---

## 测量构念与维度

%% 多个维度需要逐行比较，使用表格。单维工具也保留一行。 %%

> [!entry-map]
>
> | 维度 | 对应构念 | 题项数 | 测量内容 | 计分方式 |
> |---|---|---|---|---|
> | <维度名称> | [[<Concept>]] | — | 该维度测量什么 | 求和、均值、加权或模型分数 |

%% 区分工具声称测量的构念与实际操作化的指标。单维工具也必须明确写出唯一构念。 %%

---

## 题项与作答方式

%% 题项结构和作答规则使用 callout。来源提供具体题项时，在下方表格中尽可能逐题记录。 %%

> [!instrument-items] 题项结构
> - **题项数量** 总题项数及各维度题项数。
> - **题项形式** 陈述句、情境题、任务、观察指标或开放题。
> - **作答格式** Likert 等级、二分类、多项选择、频率、强度、表现等级或其他格式。
> - **反向题与跳题** 反向题、筛选题、跳题逻辑及注意事项。

%% 每个维度建立一个独立的三级标题和题项表。按实际维度复制下面的完整单元；单维工具保留一个。 %%

### <维度一>

> [!ref-table]- 题项
> | 编号 | 题项 | 作答选项 | 计分 | 来源 |
> |---|---|---|---|---|
> | 1 | 题项原文或准确译文 | 等级、类别或其他选项 | 分值、反向计分或跳题规则 | [[Argument_Author_Year_Journal\|Author (Year, p. X)]] |

---

## 使用该工具的研究

%% 测量属性必须归到提供该证据的具体研究，不另建脱离样本的信效度汇总。原文未报告的项目写 —。 %%

> [!ref-table]- 研究索引
> <span class="instrument-study-table-marker" aria-hidden="true"></span>
> | 研究 | 工具版本 | 样本与用途 | 信度及来源 | 效度与可比性 | 实证结果 |
> |---|---|---|---|---|---|
> | [[Argument_Author_Year_Journal\|Author (Year)]] | 版本与语言 | N、人群、地区、研究情境及测量用途 | 当前样本或既有证据，随后写 α、ω、ICC、重测或评分者间结果 | 内容、结构、效标、反应过程、测量不变性或 DIF | 描述统计、关系、差异、预测或其他结果 |

%% 一项研究报告多个维度或题项的详细结果时，可在研究索引后增加 `### Author（Year）`，再用一张 `[!ref-table]-` 记录分维度或分题项结果。没有详细数据时不增加。 %%

---

## 版本与适配

%% 版本、语言、地区和目标人群统一在此记录，不在工具定位中重复。只有一个版本时保留一行。 %%

> [!ref-table]- 版本索引
> | 版本 | 语言与地区 | 目标人群 | 题项数 | 主要变化 | 来源 |
> |---|---|---|---|---|---|
> | 原始版 | 语言与地区 | 人群 | — | 原始结构 | [[Argument_Author_Year_Journal\|Author (Year)]] |
> | 修订版或译本 | 语言与地区 | 人群 | — | 翻译、删题、增题、维度或评分变化 | [[Argument_Author_Year_Journal\|Author (Year)]] |
