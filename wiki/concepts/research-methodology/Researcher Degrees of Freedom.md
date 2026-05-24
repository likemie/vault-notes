---
title: Researcher Degrees of Freedom
aliases:
  - 研究者自由度
summary: "研究者在样本选择、变量处理、模型设定和案例排除等分析决策上的自由度累积效应，用于解释结果偏差和可重复性问题。"
type: concept
tags:
- researcher-degrees-of-freedom
- research-methodology
- questionable-research-practices
- meta-analysis
- evidence-based-education
related_concepts:
  - "[[Developer Effect]]"
  - "[[Implementation Fidelity]]"
  - "[[Effect Size]]"
  - "[[Publication Bias]]"
  - "[[Preregistration]]"
related_theories: []
related_methods: []
related_persons: []
related_facts:
  - "[[What Works Clearinghouse (WWC)]]"
  - "[[Creation of REES 2018]]"
related_arguments: []
sources:
  - "[[Wolf_2020_JREE]]"
confidence: medium
status: draft
created: '2026-05-02'
updated: '2026-05-18'
---

## 定义

> [!info] 定义
> 研究者自由度（Researcher Degrees of Freedom）由 Simmons, Nelson & Simonsohn (2011) 提出，指研究者在数据收集和分析过程中可以做出一系列未被披露的决策——这些决策的累积效应可能使几乎任何结果呈现为统计显著。在教育项目评估中，开发者可能利用这些自由度来优化研究结果，构成[[Developer Effect|开发者效应]]的可能机制之一。
>
> > "Another way that developers could potentially influence study results... is by influencing study design and data cleaning and analysis decisions to produce the most favorable study results possible." (Wolf et al., 2020, p. 429, citing Simmons, Nelson, & Simonsohn, 2011)

## 核心要素

> [!abstract] Simmons et al. (2011) 识别的自由度类型
> Wolf et al. (2020, p. 429) 总结了 Simmons et al. 的框架：
>
> 1. **样本选择**：包含或排除哪些参与者、学校、班级
> 2. **变量选择**：选择哪些结果变量为主要结果、哪些为次要结果（因变量选择）；使用哪些协变量（自变量选择）
> 3. **案例排除**：如何处理离群值（outliers）和缺失数据
> 4. **分析选择**：选择何种统计模型、是否包含交互项、如何处理聚类
>
> > 例：一个教育科技公司评估其数学项目时，可以（1）排除[[Implementation Fidelity|实施忠实度]]低于 80% 的班级（样本选择），（2）使用公司自编的数学测试而非州标准化测试作为主要结果（变量选择），（3）将成绩异常的学生标记为"离群值"予以排除（案例排除），（4）在发现总体效应不显著后转向子组分析（分析选择）。每一种选择单独看都可能合理，但累积使用可大幅抬高最终报告的[[Effect Size|效应量]]。


> [!abstract] 心理学中的证据
> John et al. (2012) 调查了 2,000 名心理学家，发现（Wolf et al., 2020, p. 429）：
> - **63%** 承认未报告所有因变量
> - 其他未披露的做法包括：在数据收集达到预期结果后停止收集、排除数据后才决定是否继续收集


> [!abstract] 在[[Developer Effect|开发者效应]]中的角色
> Wolf et al. (2020, pp. 442–443) 讨论了研究者自由度作为开发者效应的可能解释，但指出两个不确定性：
> - 不清楚开发者是否比独立研究者更滥用自由度——独立研究者同样面临发表压力
> - [[What Works Clearinghouse (WWC)|WWC]] 标准和程序手册（Version 4.0）已经约束了部分自由度（如要求报告特定数据元素和允许的分析方法），但仍有"充裕的空间"（ample room）进行分析选择

## 与相关概念的区别

> [!example] 与相关概念的区别
> - **vs [[Publication Bias]]** — 研究者自由度发生在**分析阶段**（研究内的选择性决策），发表偏倚发生在**发表阶段**（研究间的选择性传播）
> - **vs [[Preregistration]]** — 预注册是限制研究者自由度的主要机制：通过预先锁定分析计划，减少事后自由度；但 Gelman & Loken (2014) 论证预注册不能完全消除自由度——"研究者可以通过观察数据学到很多"

## 实证发现

> [!success] 实证发现
> - Wolf et al. (2020, p. 441) 发现即使控制可观测的研究设计特征，[[Developer Effect|开发者效应]]仍然存在——暗示未被观测的因素（如研究者自由度）可能部分解释了残留的差异
> - 开发者研究中使用研究者/开发者自编测量的比例（29%）远高于独立研究（8%），这可能反映了一种系统性的测量选择自由度（Wolf et al., 2020, p. 434）

## 争议与批评

> [!warning] 争议与批评
> - **Gelman & Loken (2014)** 提出" researcher degrees of freedom "的概念也可被理解为"数据的花园小径"（garden of forking paths）：研究者并非恶意操纵，而是在面对数据后自然做出看似合理的分析选择——问题在于这些选择的累积效应
> - **在开发者研究中的因果不确定性**：Wolf et al. (2020) 承认不能明确判断[[Developer Effect|开发者效应]]在多大程度上来自研究者自由度 vs. [[Publication Bias|发表偏倚]] vs. [[Implementation Fidelity|实施忠实度]]差异

## 相关案例／政策

> [!example] 相关案例／政策
> - [[Creation of REES 2018]] — REES 的[[Preregistration|预注册]]制度直接针对约束研究者自由度
> - [[Developer Effect]] — 研究者自由度是开发者效应的可能解释机制之一

## 来源

- [[Wolf_2020_JREE]]
