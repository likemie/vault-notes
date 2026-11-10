---
title: Null Hypothesis
aliases:
  - 零假设
  - 虚无假设
  - 无差异假设
  - null hypotheses
  - H₀
  - 原假设
summary: "在推断统计与假设检验中设定变量间无关联或总体参数无实质差异的基准假设（通常记为 H₀）；通过检验样本数据在零假设下的极端概率以决定是否予以拒绝，充当反证逻辑下检验对立理论命题的数理基准。"
type: concept
domain: "research-methodology"
related_count: 27
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
concept_field: "research-methodology"
tags:
  - subject/research-methodology
  - paradigm/positivist
  - quantitative-methods
  - hypothesis-testing
related_concepts:
  - "[[Hypothesis]]"
  - "[[Study Population and Sample]]"
  - "[[Variable]]"
  - "[[Alternative Hypothesis]]"
  - "[[Sampling Error]]"
  - "[[Falsification]]"
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Operationalization]]"
  - "[[Scaffolding]]"
  - "[[Research Question]]"
  - "[[Paradigm]]"
  - "[[Reproducibility Crisis]]"
  - "[[Publication Bias]]"
related_methods:
  - "[[Random Sampling]]"
  - "[[Statistical Significance]]"
  - "[[Qualitative Research]]"
  - "[[Quantitative Research]]"
  - "[[Sample Size Determination]]"
  - "[[Confidence Interval]]"
  - "[[Effect Size]]"
  - "[[Experimental Research]]"
  - "[[Multiple Regression]]"
  - "[[Analysis of Variance]]"
  - "[[Pre-test and Post-test]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch07]]"
confidence: high
status: active
created: 2026-05-31
updated: 2026-11-11
---

---

> [!def] Null Hypothesis
> **零假设（Null [[Hypothesis]]，通常记作 $H_0$）** 是推断统计与假设检验中的基准假设形式，预设在[[Study Population and Sample|目标总体]]中[[Variable|变量]]之间不存在关联，或者处理组与对照组之间不存在系统性差异（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p. 144]]；[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch07|Cohen et al., 2011, Ch. 7, p. 140]]）。零假设确立了若无实质因果效应介入时数据所呈现的[[Random Sampling|随机抽样]]波动基准；研究者通过计算在零假设为真的前提下观察到当前样本或更极端样本的概率（$p$ 值），以确定是否具有充分证据拒绝该基线预设，进而间接为[[Alternative Hypothesis|备择假设]]提供经验支持。

> [!concept-lens|notitle] 概念透镜
> - **含义** 零假设是[[Statistical Significance|统计显著性]]检验中设立的待反驳参照基准，表征系统纯粹受随机[[Sampling Error|抽样误差]]主导时的统计分布状态。
> - **用途** 为量化检验提供可操作的[[Falsification|证伪]]起点，通过将抽样差异与理论零点对比，量化当前实验效应偏离随机预期的置信程度。
> - **边界** 零假设充当待检验的基准参照系，用于评估观察变异是否属于随机抽样波动的合理区间；研究方案写作中通常重点陈述实质性理论假设。

> [!citation-card|notitle] 关键表述
> 零假设预测在总体中变量之间不存在关系或组间不存在差异。其功能在于设定一个待检验的基准命题，使得研究者能够通过统计检验判定样本结果是否与纯粹的随机抽样变异相吻合。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, p. 144)]]
>
> *The null hypothesis makes a prediction that, in the general population, no relationship or no significant difference exists on the variable between groups... it establishes a baseline against which to test whether observed patterns deviate from chance.*

> [!boundary]- 概念边界
> - 不等于 [[Alternative Hypothesis|备择假设]]（$H_1$）。备择假设预测总体中存在实质性差异或因果关联，与零假设在逻辑上互斥且穷尽，共同构成统计决策边界。
> - 不等于 实质性理论命题本身。零假设是为实现数理检验而构建的形式化统计工具，理论研究者所真正关心和探讨的通常是诱发系统性偏离的前因机制。
> - 不适用于 纯粹探索性[[Qualitative Research|质性研究]]。质性研究旨在从深度田野与文本材料中归纳建构理论，不预先设立待拒绝的参数零基准。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 零假设（$H_0$） | [[Alternative Hypothesis\|备择假设]]（$H_1$） | 实质性研究假设（Research Hypothesis） |
> |---|---|---|---|
> | **核心内容** | 总体参数无差异或无关联（$\mu_1 = \mu_2$ 或 $\rho = 0$） | 总体参数存在显著差异或特定方向关联（$\mu_1 \neq \mu_2$ 或 $\mu_1 > \mu_2$） | 阐明[[Independent Variable\|自变量]]影响[[Dependent Variable\|因变量]]的因果机制与理论逻辑 |
> | **检验角色** | 设定待推翻或拒绝的概率对照基准 | 拒绝零假设时被择优接纳的备选命题 | 引导整个实证研究设计与变量[[Operationalization\|操作化]]的理论灵魂 |
> | **表述范例** | “新教学法组与传统教学法组在学业测验成绩上均值相等” | “新教学法组学生在学业测验成绩上显著高于传统教学法组” | “自适应[[Scaffolding\|脚手架]]通过降低外生认知负荷促进学生的深层概念迁移” |
> | **统计决策** | 拒绝（Reject）或无法拒绝（Fail to reject） | 获得经验支持（Supported）或未获支持 | 获得理论证实、修正或面临反例证伪 |

---

> [!feature] 核心要素
> - **参数无变异预设（Parameter Invariance）** 在数理模型中将待检效应精确锚定为零点（例如回归斜率 $\beta = 0$、组间均值差 $\Delta\mu = 0$），排除了任何系统性因果倾向。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch07|(Cohen et al., 2011, p. 140)]]
> - **总体指向性（Population-Level Orientation）** 零假设始终指向目标总体的真实参数状态，抽样样本中观察到的非零差异则通过概率分布检验其是否落入随机抽样波动的置信边界内。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, p. 144)]]
> - **统计反证逻辑（Proof by Contradiction Logic）** 遵循归谬法的统计变体：假定零假设成立，推导观察到当前样本或更极端结果的条件概率 $p(D \mid H_0)$；当该概率极低（如低于 $\alpha = 0.05$）时，促使研究者对假定前提产生怀疑并予以拒绝。
> - **决策风险对称性（Decision Error Balance）** 零假设检验面临两类风险：在零假设为真时错误拒绝的 I 型错误（弃真，概率为 $\alpha$），以及在备择假设为真时未能拒绝零假设的 II 型错误（取伪，概率为 $\beta$）。

> [!logic-map]- 零假设检验的逻辑推理图谱
> ```mermaid
> flowchart TD
>     A["研究问题与理论建构"] --> B["确立统计假设对：<br/>H0: 无差异 vs H1: 有差异"]
>     B --> C["假定 H0 成立并构建抽样分布"]
>     C --> D["收集经验数据并计算检验统计量与 p 值"]
>     D --> E{"p 值 < 显著性水平 α ?"}
>     E -- "是 (p < α)" --> F["拒绝零假设 H0<br/>接受备择假设 H1"]
>     E -- "否 (p >= α)" --> G["无法拒绝零假设 H0<br/>证据不足以证明效应存在"]
> ```

---

> [!concept-proposition] 命题一｜零假设提供统计反证逻辑的概率基准而非直接证实理论
> **统计证伪与反证逻辑** 探讨推断统计为何必须通过设立零假设并尝试否定它来间接推进理论，阐明科学知识积累中的证伪进路。

> [!claim] Creswell & Creswell; Cohen et al.
> **零假设作为间接因果检验的概率中介** 在[[Quantitative Research|定量研究]]设计中，理论命题无法被有限经验数据穷尽证实。研究者通过设定一个精确可计算的零假设，将[[Research Question|研究问题]]转化为一个具体的概率断言。当观察数据在零假设下的发生概率极小（达到统计显著性）时，表明偶然误差难以解释当前数据形态，从而以排除随机可能性的方式为对立的实质性假设提供有力支撑。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, p. 144)]]; [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch07|(Cohen et al., 2011, p. 140)]]

---

> [!concept-proposition] 命题二｜无法拒绝零假设并不等同于证明真实效应不存在
> **统计功效瓶颈与接受零假设误区** 揭示未能达到统计显著性时将结论直接等同于“无效应”的方法学风险，论证小样本检验对弱真实效应的识别盲区。

> [!claim] Cohen et al.
> **无法拒绝零假设与缺乏统计检力的混淆** 当统计检验未能拒绝零假设时，该结果仅说明当前样本证据不足以推翻无差异基线，绝不代表总体中真实效应等同于绝对零。若研究受限于微小[[Sample Size Determination|样本量]]或较大的测量噪声，统计功效（$1-\beta$）将大幅受损，即使真实干预具有重要实践价值，检验程序仍有极大概率产生无法拒绝零假设的假阴性结论（II 型错误）。研究者必须结合[[Confidence Interval|置信区间]]与[[Effect Size|效应量]]指标审视阴性结果。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch07|(Cohen et al., 2011, pp. 140–141)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **反证逻辑命题** | 零假设通过概率计算排除纯随机解释，间接为实质性假设提供检验基准 | 因子[[Experimental Research\|实验设计]]、[[Multiple Regression\|多元回归]]与参数假设检验 | [[Argument_Creswell_2022_SAGE\|Creswell and Creswell (2022)]] |
> | **功效误区命题** | 无法拒绝零假设不等于证明真实无效应，受样本检力制约容易产生假阴性 | 小样本试验分析、阴性实证结果解读与效应评估 | [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch07\|Cohen et al. (2011)]] |

---

> [!dev-timeline] 概念演变
> - **1935 年 — 费雪试验设计与零假设确立** 罗纳德·费雪（Ronald A. Fisher）在《试验设计》（*The Design of Experiments*）中系统阐释零假设，指出科学实验中的零假设“永远不能被完全证实，但能够被经验反驳”，确立了以 $p$ 值判定证据强度的推断逻辑。
> - **1933 年–1938 年 — 内曼-皮尔逊双假设决策框架** 耶日·内曼（Jerzy Neyman）与埃贡·皮尔逊（Egon Pearson）引入备择假设、I 型错误 $\alpha$ 与 II 型错误 $\beta$，将零假设检验拓展为两类错误权衡的量化决策[[Paradigm|范式]]。
> - **2010 年代至今 — 零假设显著性检验（NHST）反思与效应量转向** 面对[[Reproducibility Crisis|可重复性危机]]，社会科学与教育研究界反思将 $p < 0.05$ 等同于真理的机械主义倾向，倡导将零假设检验与效应量报告、置信区间及研究预注册紧密结合。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, pp. 144–146)]]

---

> [!debates|notitle] 学术争议
>
> > [!axis] 费雪纯显著性检验 vs 内曼-皮尔逊假设决策
> > 争论推断统计应聚焦于单纯评估零假设被观察数据证伪的概率（$p$ 值），还是应在零假设与备择假设间权衡长期决策错误率（$\alpha$ 与 $\beta$）。
> >
> > - **费雪进路** 强调科学探索是渐进积累过程，零假设检验仅提供证据强度的连续刻画，反对将固定显著性门槛作为决策硬性标准。
> > - **内曼-皮尔逊进路** 强调实践行动中的最优决策规则，要求预先根据损失函数设定两类错误控制边界。
>
> > [!axis] 机械显著性检验（NHST）存废之争
> > 争鸣现代实证研究是否应彻底废除依赖零假设拒绝的显著性二元标签。
> >
> > - **改良拥护派** 认为零假设提供了明确的概率滤网，能有效防范研究者将纯粹的抽样噪声过度解读为实质性科学突破。
> > - **废除激进派** 指出过度迷信拒绝零假设诱发了[[Publication Bias|发表偏倚]]与 $p$ 值操纵，主张全面转向贝叶斯后验概率或直接依赖效应量与置信区间。

> [!warning|limits] 适用局限
> 大样本下的虚假显著性陷阱：当样本容量极端庞大时，微不足道且缺乏实质实践意义的细微差异亦可能在统计上轻松达到显著水平并拒绝零假设；相反，小样本下微弱的统计检力极易将具有重大价值的效应判定为无法拒绝零假设。研究者不得将拒绝零假设直接等同于获得重大理论突破。

---

> [!entry-map] 条目关联
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Alternative Hypothesis]] | 概念 | 与零假设成对出现并构成逻辑互斥的备择命题。 |
> | [[Variable]] | 概念 | 零假设用于设定其间无关联或无效应的核心测量维度。 |
> | [[Operationalization]] | 概念 | 将宏观理论命题转化为具体可检验零假设的操作化过程。 |
> | [[Quantitative Research]] | 方法 | 普遍应用零假设显著性检验的实证方法体系。 |
> | [[Analysis of Variance]] | 方法 | 检验多个总体均值相等的经典零假设统计工具。 |
> | [[Pre-test and Post-test]] | 方法 | 通过比较前后测差异是否显著偏离零假设以评估干预效应的设计。 |

---

> [!evidence-grid-a|notitle] 相关研究索引
> - [[Argument_Creswell_2022_SAGE|Creswell and Creswell (2022)]] — 系统介绍零假设在量化研究方案写作中的形式要求与假设检验操作流程。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch07|Cohen et al. (2011)]] — 详述零假设在实验与调查设计中的逻辑角色及其与备择假设的配对关系。
