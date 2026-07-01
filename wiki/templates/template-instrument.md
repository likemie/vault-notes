---
title: <% tp.file.title %>
aliases: []
summary: ""
type: instrument
instrument_type: scale
part_of: ""
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
> - **开发者与年份** Author et al. (Year)。
> - **测量目的** 用于筛查、诊断、描述、分组、预测、评价还是研究测量。
> - **实施方式** 只写工具本身稳定的自陈、他评、观察、访谈、纸笔、计算机、自适应或其他实施形态。

%% 开发者与年份直接引用原始开发来源。原始来源已有 Argument 时才链接；没有时保留纯文本 APA 文内引用。开发者姓名、开发年份与引用来源不一致时，以原始开发来源为准，不把后来使用该工具的研究写成开发来源。
   只有原始来源提供值得保留的官方定义或开发者表述时，才增加 `[!citation-card]-`，否则不生成该卡片。 %%

---

## 测量构念与维度

%% 对应构念写在 callout 标题中，不在每一行重复。多个维度需要逐行比较，单维工具也保留一行。
   如果不同维度确实对应不同构念，按构念分别建立 construct-table。 %%

> [!construct-table] [[<Concept>]]
> <span class="instrument-dimension-table-marker" aria-hidden="true"></span>
>
> | 维度 | 题项数 | 测量内容 | 计分方式 |
> |---|---|---|---|
> | <维度名称> | — | 该维度测量什么 | 求和、均值、加权或模型分数 |

%% 区分工具声称测量的构念与实际操作化的指标。 %%

---

## 题项与作答方式

%% 题项结构和作答规则使用 callout，只保留有信息的项目，不重复 frontmatter 和维度表中的题项数。
   题项形式、作答格式、反向题与跳题全部无法确认时，本节直接写 —。
   来源提供具体题项时，在下方表格中尽可能逐题记录。 %%

> [!instrument-items] 作答规则
> - **题项形式** 陈述句、情境题、任务、观察指标或开放题。
> - **作答格式** Likert 等级、二分类、多项选择、频率、强度、表现等级或其他格式。
> - **反向题与跳题** 反向题、筛选题、跳题逻辑及注意事项。

%% 每个维度建立一个独立的三级标题和题项表。按实际维度复制下面的完整单元；单维工具保留一个。 %%

### <维度一>

> [!ref-table]- 题项
> <span class="instrument-item-table-marker" aria-hidden="true"></span>
>
> | 编号 | 题项 | 作答选项 | 计分 | 来源 |
> |---|---|---|---|---|
> | 1 | 题项原文或准确译文 | 等级、类别或其他选项 | 分值、反向计分或跳题规则 | [[Argument_Author_Year_Journal\|Author (Year, p. X)]] |

%% 访谈工具使用下面的专表，删除量表题项表和观察重点表。每行记录一个核心问题，追问写在同一行。 %%

> [!interview-guide] 访谈问题
> <span class="instrument-interview-table-marker" aria-hidden="true"></span>
>
> | 编号 | 主题或维度 | 核心问题 | 可选追问 | 来源 |
> |---|---|---|---|---|
> | 1 | 访谈主题 | 问题原文或准确译文 | 追问、提示或探查问题 | [[Argument_Author_Year_Journal\|Author (Year, p. X)]] |

%% 观察工具使用下面的专表，删除量表题项表和访谈问题表。每行记录一个可区分的观察重点。 %%

> [!observation-focus] 观察重点
> <span class="instrument-observation-table-marker" aria-hidden="true"></span>
>
> | 编号 | 观察维度 | 观察重点 | 记录方式 | 判定或编码 | 来源 |
> |---|---|---|---|---|---|
> | 1 | 观察维度 | 需要关注的行为、事件、互动或环境特征 | 频次、时长、事件记录、等级或描述记录 | 判定标准、代码或 — | [[Argument_Author_Year_Journal\|Author (Year, p. X)]] |

---

## 使用该工具的研究

%% 测量属性必须归到提供该证据的具体研究，不另建脱离样本的信效度汇总。原文未报告的项目写 —。 %%

> [!ref-table]- 研究索引
> <span class="instrument-study-table-marker" aria-hidden="true"></span>
>
> | 研究 | 工具版本 | 样本与用途 | 测量属性 | 关键结果 |
> |---|---|---|---|---|
> | [[Argument_Author_Year_Journal\|Author (Year)]] | 实际使用的版本与语言 | N、人群、地区、研究情境及测量用途 | 区分当前样本与既有来源，记录信度、效度、反应过程、测量不变性或 DIF | 描述统计、关系、差异、预测或其他结果 |

%% 同一来源包含多个维度或题项的详细结果时，可在研究索引后增加 `### Author（Year）`，再用一张 `[!ref-table]-` 记录分维度或分题项结果。没有详细数据时不增加。 %%

---

## 版本与适配

%% 只记录真实存在的原始版、修订版、短版、译本或人群适配版。研究中的施测地区、样本和载体写入研究表，不把一次施测当成版本。
   版本来源必须是定义该版本的原始来源，不能用后来使用该工具的研究代替。只有一个版本时保留一行。 %%

> [!ref-table]- 版本索引
> <span class="instrument-version-table-marker" aria-hidden="true"></span>
>
> | 版本 | 语言与地区 | 目标人群 | 题项数 | 主要变化 | 来源 |
> |---|---|---|---|---|---|
> | 原始版 | 语言与地区 | 人群 | — | 原始结构 | Author et al. (Year) |
> | 修订版或译本 | 语言与地区 | 人群 | — | 翻译、删题、增题、维度或评分变化 | Version Author et al. (Year) |
