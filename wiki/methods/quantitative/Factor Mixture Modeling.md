---
title: Factor Mixture Modeling
aliases:
  - "因子混合模型"
  - "FMM"
summary: "一种结合了验证性因子分析（CFA）与潜在剖面分析（LPA）的量化方法。它能够通过考察个体在多维度连续潜在因子上的模式（轮廓）表现，识别出总体数据中隐含的异质性潜在类别（群组）。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 0
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
tags: []
related_concepts:
  - "[[Heterogeneity]]"
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Epistemology]]"
  - "[[Research Question]]"
  - "[[Sample Size Determination]]"
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Greene_2010_JEP]]"
confidence: medium
status: draft
created: 2026-08-15
updated: 2026-08-15
---

# Factor Mixture Modeling

---

## 定义

> [!def] 方法定义
> 因子混合模型（Factor Mixture Modeling, FMM）结合了因子分析降维测量的优势与潜在类别/剖面分析探究[[Heterogeneity|异质性]]的功能。它利用个体在多个连续的潜在因子（潜[[Variable|变量]]）上的表现特征，将其划分至具备不同特征轮廓（profile）的未知类群中。[[Argument_Greene_2010_JEP|(Greene et al., 2010, p. 239)]]

> [!method-scope] 方法范围
> - **研究对象** 具备多维测量结构并[[Hypothesis|假设]]存在群体异质性分类的数据。
> - **问题类型** 探索或验证异质样本中的亚群结构（如划分认知发展阶段类型）。
> - **分析单位** 个体。
> - **输出形式** 潜在类别分配、类别的因子均值轮廓图。

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为人类的心理或行为属性既具有多维度的连续特征，也在总体上包含本质不同的类别群体。
> - **研究者角色** 需要在各类拟合指数中选择合理的模型分类数目，并基于理论为不同类群特征赋予命名和实质解释。
> - **有效性标准** AIC、BIC、调整后 BIC（SABIC）、LMR 检验、bLRT 检验以及模型分类熵（Entropy）。

> [!method-stack] 方法层级
> - **分析方法** 因子混合模型（FMM）。
> - **辅助技术** 验证性因子分析（CFA）、潜在剖面分析（LPA）。

---

## 研究程序

> [!proc] 通用程序
> 1. 明确[[Research Question|研究问题]]、对象以及假定的[[Heterogeneity|异质性]]亚群结构。
> 2. 首先运行标准验证性因子分析（CFA），确认测量模型的合理性。
> 3. 拟合具有递增类别数目（如从2类到6类）的混合模型，并设定不同严格程度的方差/协方差等值限制（如 strict vs strong invariance）。
> 4. 使用多项拟合信息准则（如 AIC、BIC、bLRT 等）对比以确定最佳的类别数量模型。
> 5. 提取最优模型下各潜在类别的因子均值（轮廓特征），并结合理论对其进行实质性解释。

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 横截面或追踪量表数据。
> - **模型或统计量** 因子混合模型、似然比检验。
> - **诊断与检验** LMR 检验、模型收敛性及参数异常判定（如 Heywood case）。

> [!software-impl] 软件实现
> - **推荐软件** Mplus、R。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 具有深层分类学假说、需要在多维度上综合识别异质发展阶段群体的研究场景。[[Argument_Greene_2010_JEP|(Greene et al., 2010, p. 239)]]

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 对起点的初值较为敏感，极大可能面临局部极值和不收敛问题，通常需要充足的[[Sample Size Determination|样本量]]；另外潜在类群的实质解释依赖研究者的理论预设，有主观色彩。

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Greene_2010_JEP]] — 该研究通过因子混合模型，将大样本学生在[[Epistemology|认识论]]维度上的测量得分有效聚类为了理论预设的四个阶段组。
