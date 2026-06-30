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

> [!instrument-profile] 工具定位
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
> - **完成时间** 官方或研究报告中的典型完成时间。

> [!ref-table]- 题项记录
> | 编号 | 题项 | 所属维度 | 作答与计分 | 来源 |
> |---|---|---|---|---|
> | 1 | 题项原文或准确译文 | 维度名称 | 作答选项、分值、反向计分或跳题规则 | [[Argument_Author_Year_Journal\|Author (Year, p. X)]] |

---

## 测量属性

%% 测量属性会随研究、版本和样本变化，使用表格逐项累计。不得只写“信效度良好”。没有对应证据时删除整张表。 %%

> [!ref-table]- 信度证据
> | 研究 | 版本与样本 | 信度类型 | 指标 | 结果与区间 | 判断 |
> |---|---|---|---|---|---|
> | [[Argument_Author_Year_Journal\|Author (Year)]] | 版本、N、人群与地区 | 内部一致性、重测、评分者间或其他 | α、ω、ICC、r 或 κ | 数值与 CI | 该结果支持什么，不支持什么 |

> [!ref-table]- 效度证据
> | 研究 | 版本与样本 | 证据类型 | 方法 | 关键结果 | 判断 |
> |---|---|---|---|---|---|
> | [[Argument_Author_Year_Journal\|Author (Year)]] | 版本、N、人群与地区 | 内容、内部结构、与其他变量关系、效标、反应过程或后果 | 专家评审、EFA、CFA、相关、预测或其他 | 载荷、拟合、相关、效应或分类表现 | 证据支持的解释范围 |

> [!ref-table]- 可比性与测量不变性
> | 研究 | 比较群体 | 检验层级 | 结果 | 可否比较 | 来源 |
> |---|---|---|---|---|---|
> | [[Argument_Author_Year_Journal\|Author (Year)]] | 性别、语言、文化、时期或群体 | 构型、载荷、截距、残差或 DIF | 指标与判断 | 仅结构、关系、均值或不可直接比较 | 页码 |

%% 没有报告测量不变性或跨群体可比性时可删除最后一张表，不得把“分别具有良好信度”写成“群体间可比较”。 %%

---

## 实施条件

%% 实施要求是一组操作说明，使用 callout。 %%

> [!instrument-use] 实施条件
> - **施测资格** 是否要求培训、认证或专业资质。
> - **材料与环境** 所需材料、设备、场地和标准化条件。
> - **时间与成本** 施测、评分和反馈所需时间及费用。
> - **数据质量** 无效作答、反应偏差、天花板／地板效应及质量检查。
> - **伦理要求** 知情同意、隐私、敏感结果反馈和高风险用途。

---

## 使用该工具的研究

%% 每项研究都是可重复累积的记录，使用表格，方便比较版本、样本、用途和结果。 %%

> [!ref-table]- 研究索引
> | 研究 | 工具版本 | 样本与情境 | 测量用途 | 提供的信息 |
> |---|---|---|---|---|
> | [[Argument_Author_Year_Journal\|Author (Year)]] | 版本与语言 | N、人群、地区与研究情境 | 测量什么构念，作为自变量、因变量、协变量或筛查指标 | 信效度、描述统计、关系、差异或其他结果 |

---

## 版本与适配

%% 版本、语言、地区和目标人群统一在此记录，不在工具定位中重复。只有一个版本时保留一行。 %%

> [!ref-table]- 版本索引
> | 版本 | 语言与地区 | 目标人群 | 题项数 | 主要变化 | 来源 |
> |---|---|---|---|---|---|
> | 原始版 | 语言与地区 | 人群 | — | 原始结构 | [[Argument_Author_Year_Journal\|Author (Year)]] |
> | 修订版或译本 | 语言与地区 | 人群 | — | 翻译、删题、增题、维度或评分变化 | [[Argument_Author_Year_Journal\|Author (Year)]] |
