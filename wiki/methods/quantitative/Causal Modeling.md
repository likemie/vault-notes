---
title: Causal Modeling
aliases:
  - 因果建模
  - 结构方程建模
  - SEM
summary: "通过结构方程等统计模型表示变量之间因果路径并同时估计多重关系的量化方法，常用于检验理论结构与中介机制"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 29
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - causal-modeling
  - structural-equation-modeling
  - sem
  - subject/research-methodology
  - paradigm/positivist
related_concepts:
  - "[[Causality]]"
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Epistemology]]"
  - "[[Evaluation Research]]"
  - "[[Statistical Significance]]"
  - "[[Exogenous and Endogenous Variables]]"
  - "[[Dependent Variable]]"
  - "[[Independent Variable]]"
  - "[[Recommendations for Practice]]"
  - "[[Research Question]]"
  - "[[Screening Off]]"
  - "[[Causal Processes]]"
  - "[[Operationalization]]"
  - "[[Effect Size]]"
  - "[[Standard Error]]"
  - "[[Cultural Capital]]"
related_theories:
  - "[[Potential Outcomes Framework]]"
related_methods:
  - "[[Multiple Regression]]"
  - "[[Matching]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Observational and Correlational Research]]"
  - "[[Covariate Adjustment]]"
related_persons:
  - "[[Herbert Blalock]]"
related_arguments:
  - "[[Argument_Berk_2011_ER]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]"
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Brady_2023_EPR]]"
  - "[[Argument_Trautwein_2007_CEP]]"
confidence: medium
status: draft
created: 2026-05-03
updated: 2026-08-19
---

# Causal Modeling

## 定义

> [!def] 方法定义
> 因果建模（Causal Modeling），也称为结构方程建模（Structural Equation Modeling, SEM），是随机实验之外最常用的[[Causality|因果推断]]替代方法。其目标是对观察性研究施加一个关于"自然如何生成数据"的模型，然后从数据中估计自然使用的参数值。它于 1970 年代进入社会科学领域，承诺将实质性社会科学理论与统计学进行形式上的整合（[[Argument_Berk_2011_ER|Berk, 2011, p.196]]）。

> [!method-scope] 方法范围
> - **研究对象**[[Variable|变量]]之间的因果路径和结构关系，通常基于理论[[Hypothesis|假设]]构建模型。
> - **问题类型** 适合检验理论驱动的因果结构——"这些变量之间的因果方向、中介路径和效应强度是怎样的？"可用于分析直接效应、间接效应和总效应。
> - **分析单位** 个体、群体或组织层面的观察数据。
> - **输出形式** 路径系数、模型拟合指数、直接效应与间接效应估计、总效应分解。

> [!citation-card]- 关键定义
> Its aim is to impose on an observational study a model of how nature generated the data and then from the data, to estimate the values of the parameters nature employed. [[Argument_Berk_2011_ER|(Berk, 2011, p.196)]]

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观**因果建模隐含一种强[[Hypothesis|假设]]——研究者可以通过统计模型捕捉数据生成过程的结构性特征。这与[[Potential Outcomes Framework|潜在结果框架]]形成对比——后者从假设性比较出发定义因果效应，而非从模型假设出发估计因果参数。[[Argument_Berk_2011_ER|Berk (2011, p.196)]] 认为因果建模对[[Evaluation Research|评估研究]]的影响"最好说是好坏参半的"（mixed at best）。
> - **研究者角色** 研究者基于理论构建模型结构（指定[[Variable|变量]]间的因果路径和方向），然后从数据中估计参数。研究者的理论判断决定了模型的形式——模型的力量不可能强大过支撑它的因果假设。
> - **有效性标准** 模型拟合优度（CFI、RMSEA、SRMR 等）、路径系数的[[Statistical Significance|统计显著性]]、理论模型与竞争模型的比较。但模型拟合良好不等于因果结构正确——"模型'足够接近正确'与模型'不正确'之间没有明确的经验界限"（[[Argument_Berk_2011_ER|Berk, 2011, p.197]]）。
> - **不声称回答的问题** 因果建模本身不能证明因果方向——它只能检验预设的因果结构是否与数据一致。它不能替代随机实验来确立[[Causality|因果关系]]。统计工具"可能只是强化已有假设和模型而非识别实际因果性"（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 71]]）。

---

## 研究程序

> [!proc] 通用操作步骤
> 1. 基于理论构建因果模型——指定[[Variable|变量]]之间的因果路径（箭头方向），区分[[Exogenous and Endogenous Variables|外生变量与内生变量]]
> 2. 从数据中估计路径系数（参数）
> 3. 检验模型拟合度
> 4. 如有必要，修改模型并重复步骤 2–3（模型选择）

> [!warning] 模型选择的危险
> [[Argument_Berk_2011_ER|Berk (2011, p.197)]] 特别警告最后一步：许多因果模型是**模型选择**的产物——"在一组数据上使用一系列模型，并选择一个'最佳'模型。结果是使用该数据集的后续所有统计推断都很可能是错误的，常常是严重错误的"（Leeb & Pötscher, 2005, 2006; Berk, Brown, & Zhao, 2010）。

---

### 递归与非递归模型

因果建模中的因果方向可以通过两种模型结构来描述（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 66–67]]）：

> [!contrast-table] 递归模型 vs 非递归模型
> | 维度 | 递归模型（Recursive） | 非递归模型（Non-Recursive） |
> |------|---------------------|--------------------------|
> | **因果方向** | 单向——外生变量 → 内生变量 | 一个或多个方向——因果可以双向或多向流动 |
> | **变量关系** | 变量角色固定：外生或内生 | 变量可以同时是外生和内生——取决于因果链中的位置 |
> | **复杂性** | 可能过度简化因果方向 | 更能捕捉因果网络——原因集群以多方向共同作用 |
> | **典型应用** | 简单因果链 | 许多结构方程模型 |

许多结构方程模型是非递归的，因为它们捕捉了变量之间更复杂的双向或多向因果依赖关系。外生变量的值在模型外部确定，内生变量的值由模型内的其他变量所解释。

---

## 历史沿革

> [!dev-timeline]+ 发展脉络
> 1. **奠基与推广（1969–1975）**
>    - 1969, 1985, 1991 — [[Herbert Blalock]] 倡导因果建模，将口头理论重构为因果模型以可视化[[Variable|变量]]之间的相互联系。他提出了构建视觉因果图的基本符号规则：[[Dependent Variable|因变量]]置于右侧、[[Independent Variable|自变量]]置于左侧；单向箭头表示因果方向；正负价符号表示关系方向；双向箭头连接未分析关系（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p.58]]）
>    - 1970s — 因果建模在计量经济学推动下进入社会科学，承诺将理论整合与统计建模正式结合
>    - 1973 — Goldberger 发表 "Structural Equation Models: An Overview"
>    - 1975 — Duncan 出版 *Introduction to Structural Equation Models*
> 2. **批评与反思（1983–2005）**
>    - 1983 — Ed Leamer 发表著名批评文章 "Let's Take the Con Out of Econometrics"（[[Argument_Berk_2011_ER|Berk, 2011, p.196]]）
>    - 2004 — Berk 出版 *Regression Analysis: A Constructive Critique*
> - 2005 — David Freedman 出版 *Statistical Models: Theory and Practice*，基于二十年的批判性关切提供了对因果建模"可能最彻底的处理"
> 3. **当代定位（2011–至今）**
>    - 2011 — Berk 系统回顾因果建模的局限，推荐匹配作为替代策略；Cohen, Manion & Morrison 指出 SEM、[[Multiple Regression|多元回归]]和多变量分析"不可能强大过支撑它们的因果[[Hypothesis|假设]]"，在追求简洁清晰模型的过程中"严重简化"了情境中原因的数量或范围（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 71]]）
>    - 2023 — [[Argument_Brady_2023_EPR|Brady et al. (2023)]] 从教育心理学期刊实践层面补充批评：依赖建模的分析更可能包含因果化语言，2010 年后建模类型和用途急剧增加

---

## 局限性

### 模型选择与假设依赖

> [!method-limits] 模型选择的根本性局限
> [[Argument_Berk_2011_ER|Berk (2011, p.197)]] 识别的最核心问题：因果建模的常见实践涉及在多个模型中选择"最佳"模型，但这使得基于同一数据集的统计推断变得无效（Leeb & Pötscher, 2005, 2006; Berk, Brown, & Zhao, 2010）。

> [!critique-logic] [[Hypothesis|假设]]先于统计——模型无法超越其前提
> 因果建模的力量不可能强大过支撑它的因果假设。统计——即使是 SEM、[[Multiple Regression|多元回归]]和多[[Variable|变量]]分析——"可能只是强化已有假设和模型而非识别实际[[Causality|因果性]]"。在追求简洁清晰模型的过程中，它们经常"严重简化了情境中原因的数量或范围"（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, p. 71]]）。

> [!critique-logic] 缺乏明确的经验边界
> "因果建模的错误是程度问题。模型'足够接近正确'与模型'不正确'之间没有明确的经验界限。结果之一就是大量的回旋余地"（[[Argument_Berk_2011_ER|Berk, 2011, p.197]]）。

---

### 操作与修辞问题

> [!critique-method] 点按软件使因果建模"看似容易"
> [[Argument_Berk_2011_ER|Berk (2011, p.197)]] 提供了一个更具批判性的解释：广泛可用的点按式统计软件包使因果建模看似容易——"不需要深入理解"。他观察到许多论文"所使用的统计建模程序被以软件包的名称来引用（如'进行了一项 LISREL 分析'）"——"稍微不那么虔诚的关切是引用所使用的软件，仿佛这就是全部需要知道的（如'使用 proc mixed 进行分析'）"。

> [!critique] 对批评的修辞性回应
> [[Argument_Berk_2011_ER|Berk (2011, p.197)]] 引用了 Freedman (2005, p.195) 编纂的一份"有启发性但不完整"的清单，列举了因果建模支持者对批评的常见修辞性回应：
>
> > "我们都知道。没有什么是完美的。线性必须是一个好的第一近似。对数线性必须是一个好的第一近似。假设是合理的。假设不重要。假设是保守的。你无法证明假设是错误的。偏误会相互抵消。我们可以对偏误建模。我们只是在做其他人都在做的事。现在我们将使用更复杂的技术。如果我们不做，其他人会做。你会怎么做？决策者有了我们比没有我们更好。我们都有心智模型，不使用模型仍然是一个模型。模型并非完全无用。你必须尽可能利用数据。你必须做出假设才能取得进展。你必须给模型怀疑的好处。这有什么害处？"

---

### 与替代方法的比较

> [!contrast-table] 因果建模 vs 匹配
> | 维度 | 因果建模（SEM 等） | [[Matching\|匹配]] |
> |------|------------------|-------------------|
> | 假设依赖 | 较多——依赖不可检验的模型假设 | 较少——更多受实证诊断约束 |
> | 模型选择 | 面临模型选择问题 | 匹配[[Variable\|变量]]在不参考结果变量的情况下确定 |
> | 透明度 | 模型修改过程可能不透明 | 协变量平衡可通过标准化均值差等诊断评估 |
> | Berk 的推荐 | — | **推荐替代策略（[[Argument_Berk_2011_ER\|Berk, 2011, pp.197–198]]）** |

---

### 因果语言风险

> [!warning] 观察数据中的因果语言风险
> [[Argument_Brady_2023_EPR|Brady et al. (2023)]] 从教育心理学期刊实践层面补充了方法论批评：Reinhart et al. (2013) 曾发现，依赖建模作为分析方法的观察/相关研究更可能包含[[Recommendations for Practice|实践建议]]（RFP），可能因为建模语汇会"导致"更多类似 "predictors""mediators""outcomes" 的因果化命名。Brady et al. 原本计划继续[[Coding in Qualitative Research|编码]]"建模"，但 2010 年后建模类型和用途急剧增加，以至于区分"什么算建模"已不再有实质意义（[[Argument_Brady_2023_EPR|Brady et al., 2023, p.9]]）。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 当[[Research Question|研究问题]]涉及检验预设的理论因果结构、估计多重路径的直接和间接效应时。在研究者能对模型[[Hypothesis|假设]]提供有力辩护、且模型选择过程透明且预先注册的情况下，才可能产生可信的结果。
> - **谨慎使用** 在观察性研究中用于[[Causality|因果推断]]——因果建模不能替代随机实验来确立因果关系。模型拟合良好不等于因果结构正确。需要同时使用[[Screening Off|筛选隔离]]等方法识别并控制混淆[[Variable|变量]]（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 59–60]]）。
> - **不适合使用** 当理论基础薄弱、模型假设无法辩护时；当主要研究目标是确立因果关系而非检验因果结构时——此时真实验是更强的设计。不适合回答[[Causal Processes|因果过程]]"如何"运作的问题——因果建模能建立因果的"是什么"但不能建立"如何"（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04|Cohen et al., 2011, pp. 70–71]]）。

---

## 相关理论与方法

> [!frames-ref] 相关理论
> - [[Potential Outcomes Framework]] — 为评估因果建模的因果主张提供了替代性概念框架，强调因果效应的定义独立于估计模型

> [!ref-table] 相关概念
> | 概念 | 关系 | 说明 |
> |------|------|------|
> | [[Causality]] | 核心对象 | 因果性是因果建模所[[Operationalization\|操作化]]的核心概念，时间顺序是构建因果模型的基本前提 |
> | [[Exogenous and Endogenous Variables]] | 结构基础 | 外生和内生[[Variable\|变量]]的区分是因果模型结构的基础，递归与非递归模型的选择决定了因果方向的设定 |
> | [[Variable]] | 分析单位 | 因果模型中的基本分析单位，包括[[Independent Variable\|自变量]]、[[Dependent Variable\|因变量]]、中介变量和调节变量 |
> | [[Screening Off]] | 辅助工具 | Pearl 的图形方法可用于识别因果模型中应被筛选掉的因素（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch04]]） |

> [!ref-table] 相关方法
> | 方法 | 关系 | 说明 |
> |------|------|------|
> | [[Observational and Correlational Research]] | 数据来源 | 因果建模通常在此类数据中估计因果路径，推论风险直接相关 |
> | [[Matching]] | 替代策略 | [[Argument_Berk_2011_ER\|Berk (2011)]] 推荐的替代方法，以协变量平衡降低混杂风险 |
> | [[Covariate Adjustment]] | 配套技术 | 通过纳入协变量调整效应估计，变量选择影响[[Effect Size\|效应量]]与显著性 |
> | [[Multiple Regression]] | 基本构件 | 估计单个路径系数；[[Standard Error\|SEM]] 扩展了多元回归以同时处理多方程系统 |
> | [[Recommendations for Practice]] | 风险关联 | [[Argument_Brady_2023_EPR\|Brady et al. (2023)]] 关注建模语汇推动越界实践建议的风险 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Trautwein_2007_CEP|Trautwein & Lüdtke (2007)]] — 在 Mplus 中使用复合抽样校正（Type=Complex）构建潜[[Variable|变量]]结构方程模型，检验了科学知识确定性信念在中介认知能力、家庭[[Cultural Capital|文化资本]]与高中毕业成绩之间的因果路径，并估计了跨期潜变量回归。
