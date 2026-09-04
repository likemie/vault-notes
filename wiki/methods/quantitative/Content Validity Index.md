---
title: Content Validity Index
aliases:
  - 内容效度指数
  - CVI
  - I-CVI
  - S-CVI
  - Content Validity Ratio
  - CVR
  - 专家内容效度评估
summary: "在量表编制与测验开发初期用于量化专家对题项及全量表内容适切性、代表性与表述清晰度评价的心理测量学工具，包括题项级内容效度指数（I-CVI）、量表级内容效度指数（S-CVI/Ave）及 Lawshe 内容效度比率（CVR）。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 10
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - statistics/psychometrics
  - theme/scale-development
related_concepts:
  - "[[Content Validity]]"
  - "[[Questionnaire]]"
  - "[[Professional Judgment]]"
  - "[[Construct]]"
  - "[[Rating Scale]]"
  - "[[Item Analysis]]"
related_theories: []
related_methods:
  - "[[Scale Development]]"
  - "[[Delphi Technique]]"
related_instruments:
  - "[[Research Literacy Scale for Teachers]]"
related_arguments:
  - "[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO]]"
confidence: high
status: draft
created: 2026-08-28
updated: 2026-08-28
---

# Content Validity Index

---

## 定义

> [!def] 方法定义
> **[[Content Validity|内容效度]]指数（Content Validity Index, CVI）** 是在[[Scale Development|量表编制]]、[[Questionnaire|问卷]]设计及测验开发初期，由 Lynn（1986）与 Polit & Beck（2006）系统规范的量化心理测量学工具。它通过组织领域同行与测量学者对初始题池中的各题项进行标准化等级评定，将专家的定性[[Professional Judgment|专业判断]]转化为严谨的量化指标，分为**题项级内容效度指数（Item-level CVI, I-CVI）** 与 **量表级内容效度指数（Scale-level CVI, S-CVI）**；在测量学中常与 Lawshe（1975）提出的**内容效度比率（Content Validity Ratio, CVR）** 结合使用。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, pp. 4–5)]]

> [!method-scope] 方法范围
> - **研究对象** 量表编制第一阶段生成的初始题池（Item Pool）及其对应的理论维度定义。
> - **问题类型** 评估题项对目标[[Construct|构念]]内涵的代表性、相关性、表述准确性与语言适切度。
> - **分析单位** 题项（Item）与全量表（Scale）层级。
> - **输出形式** 介于 0 到 1 之间的指数系数（如 $\text{I-CVI} = .89$）或介于 -1 到 1 之间的 CVR 比率。

> [!citation-card]- 关键定义
> 编制量表时，将初始题项提交给由学科专家和测量学者组成的专家组进行独立评审，计算内容效度指数（CVI）与内容效度比率（CVR），能够在实证施测前系统剔除偏离构念定义、表述模糊或存在理解歧义的低质题项。[[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|(Kazancı Tınmaz & Sezgin, 2023, p. 5)]]
>
> *Content Validity Index provides a quantitative evaluation of item relevance by a panel of content experts, establishing rigorous content validity before preliminary administration.*

---

## 专家评定规程与 4 级量表

> [!proc] 专家[[Content Validity|内容效度]]评定标准操作规程
> 1. **遴选专家组** 邀请 5–10 位具有深厚学科背景、教学经验及心理测量学专长的学者（通常 6–9 位专家为最佳配置）。
> 2. **编制专家评审[[Questionnaire|问卷]]** 提供明确的[[Construct|构念]]定义、子维度说明与 4 级相关性李克特[[Rating Scale|评定量表]]：
>    - **1 分** 不相关（Irrelevant）；
>    - **2 分** 弱相关（需大幅修改后方可保留）；
>    - **3 分** 强相关（相关且表述基本清晰，仅需微调）；
>    - **4 分** 极相关（高度切题且表述极为清晰）。
> 3. **计算指标并决策** 将评为 3 分或 4 分视为“赞同”，计算每道题的 I-CVI；对全量表计算 S-CVI/Ave；依据标准判定题项保留、修改或剔除。

---

## 数学原理与计算公式

> [!formula-step] 公式步骤　题项级[[Content Validity|内容效度]]指数（I-CVI）与量表级内容效度指数（S-CVI）
> $$\text{I-CVI} = \frac{n_{\text{agree}}}{N_{\text{experts}}}, \quad \text{S-CVI/Ave} = \frac{1}{k} \sum_{i=1}^{k} \text{I-CVI}_i$$
>
> **这个公式在做什么** 
> - $\text{I-CVI}$：给出 3 分或 4 分（高相关赞同）的专家人数 $n_{\text{agree}}$ 占专家总数 $N_{\text{experts}}$ 的比例；
> - $\text{S-CVI/Ave}$：全量表所有 $k$ 个保留题项的 I-CVI 算术平均值。
>
> > [!result-reading]- 决策判定标准（Lynn 1986 与 Polit & Beck 2006）
> > - **专家人数 $N = 5$** 时：要求 $\text{I-CVI} = 1.00$（全体专家一致赞同）；
> > - **专家人数 $N = 6\sim10$** 时：要求 **$\text{I-CVI} \ge .78$**（例如 9 位专家中至少 8 位赞同，$\text{I-CVI} = 8/9 = .89$）；低于 $.78$ 的题项予以剔除或重写；
> > - **量表级标准** 要求 **$\text{S-CVI/Ave} \ge .90$**，表明量表整体内容代表性卓越。

---

> [!formula-step] 公式步骤　Lawshe 内容效度比率（CVR）
> $$\text{CVR} = \frac{n_e - N/2}{N/2}$$
>
> **这个公式在做什么** 输入将题项评为“该题对于测量该[[Construct|构念]]是必需的（Essential）”的专家人数 $n_e$ 以及专家总人数 $N$。
>
> **数学直觉** 检验赞同题项为“必需”的专家人数是否显著超越由随机猜测所期望的 $50\%$ 偶然赞同基线。
>
> > [!result-reading]- 判定阈值对照（Lawshe 1975 显著性临界表，$p < .05$）
> > - $N=5$ 位专家：$\text{CVR} \ge .99$；
> > - $N=7$ 位专家：$\text{CVR} \ge .75$；
> > - $N=9$ 位专家：$\text{CVR} \ge .78$；
> > - $N=10$ 位专家：$\text{CVR} \ge .62$。

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Kazanci_Tinmaz_Sezgin_2023_SO|Kazancı Tınmaz & Sezgin (2023)]] — 在《[[Research Literacy Scale for Teachers|教师研究素养量表]]》编制的第一阶段，针对 63 道初始题池邀请 9 位领域与测量专家进行 CVI/CVR 独立评审，依据 $\text{I-CVI} \ge .78$ 阈值筛选剔除 11 道效度偏低题项，保留 52 道高质量题项进入后续实证施测。

---

## 条目关联

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Scale Development]] | 宏观方法 | CVI 是量表编制第一阶段保证题项[[Content Validity\|内容效度]]的量化核心工具。 |
> | [[Content Validity]] | 理论概念 | CVI 提供了内容效度量化评定的标准测量学操作。 |
> | [[Delphi Technique]] | 支撑方法 | 常用于组织专家多轮背对背评审以汇聚 CVI 打分。 |
> | [[Item Analysis]] | 后续方法 | 专家 CVI 评审通过后，在预试样本中进一步执行统计项目分析。 |
> | [[Research Literacy Scale for Teachers]] | 测量工具 | 运用 9 位专家 CVI 评审筛选初始题池的实证典范。 |
