---
title: Differential Item Functioning
aliases:
  - 题目功能差异
  - 项目功能差异
  - DIF
  - 测验题目偏倚
  - 项目功能偏侧
summary: "心理测量学与大规模标准化测验中用于诊断题目偏差与跨群体测量等值性的统计分析方法，指在控制了被试真实潜在特质水平相同的条件下，不同亚群体（如性别、种族、文化、语言或国别）被试在特定测试题目上展现出系统性差异的答对概率或得分期望，是检验跨国测评等值空间与跨文化效度的核心计量工具。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 28
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - statistics/psychometrics
  - theme/measurement-invariance
  - theme/test-fairness
related_concepts:
  - "[[Construct]]"
  - "[[Space of Equivalence]]"
  - "[[Cross-cultural Validity]]"
  - "[[Variable]]"
  - "[[Unit of Analysis]]"
  - "[[Commensuration]]"
  - "[[Epistemology]]"
  - "[[Epistemic Stances]]"
  - "[[Interaction Effect]]"
  - "[[Heterogeneity]]"
  - "[[Document]]"
  - "[[Cultural Validity]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Measurement Invariance]]"
  - "[[Questionnaire]]"
  - "[[Item Response Theory]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Item Analysis]]"
  - "[[Sample Size Determination]]"
  - "[[Confirmatory Factor Analysis]]"
  - "[[Matrix Sampling]]"
  - "[[Plausible Values]]"
related_instruments: []
related_facts:
  - "[[Educational Testing Service]]"
  - "[[PISA]]"
  - "[[TIMSS]]"
  - "[[OECD]]"
related_persons: []
related_arguments:
  - "[[Argument_Grek_2009_JEdPolicy]]"
  - "[[Argument_Morgan_Shahjahan_2014_CE]]"
confidence: high
status: draft
created: 2026-10-21
updated: 2026-10-30
---

---

> [!def] Differential Item Functioning
> **题目功能差异（Differential Item Functioning, DIF）**（亦称项目功能差异或题目功能偏侧）是心理测量学、测验编制与大规模教育评估中用于识别测验题目潜在偏差（Item Bias）的核心统计技术。当来自不同人口统计学、文化或语言背景的被试群体（通常划分为焦点组 Focal Group 与参照组 Reference Group），在被测潜在特质能力水平完全相等的条件下，对某一道测验题目的答对概率或得分期望值仍存在统计学上的显著差异时，即判定该题存在题目功能差异。DIF 表明题目测量了目标[[Construct|构念]]之外的多余无关维度（Construct-Irrelevant Variance），是评价测验公平性、检验跨国测评[[Space of Equivalence|等值空间]]真实性及保障[[Cross-cultural Validity|跨文化效度]]的技术防线。[[Argument_Grek_2009_JEdPolicy|(Grek, 2009, pp. 26–27)]]; [[Argument_Morgan_Shahjahan_2014_CE|(Morgan & Shahjahan, 2014, pp. 200–201)]]

> [!method-scope] 方法范围
> - **研究对象** 测验题目的作答反应数据矩阵、受试者群体归属标签[[Variable|变量]]、受试者总分或潜在特质能力参数。
> - **问题类型** 检验测验题目是否存在对特定性别、种族、社会阶层、母语或国别受试群体的系统性偏向。
> - **[[Unit of Analysis|分析单位]]** 测验题目（二级计分或多级计分题项）、焦点组与参照组。
> - **输出形式** DIF [[Effect Size|效应量]]统计量（如 [[Educational Testing Service|ETS]] 分级分类 A/B/C 级）、胜算比（Odds Ratio）、特征曲线差异面积、题目保留或剔除决策清单。

> [!citation-card] 跨国测验中的度量等值性检验
> 跨国大规模测评依赖于制造[[Commensuration|通约]]的度量空间，当测验题目被翻译并移植至不同语言与文化环境时，若无法排除题目功能差异对跨国均值比较的系统性干扰，基于排名的政策推论便会面临效度质疑。[[Argument_Morgan_Shahjahan_2014_CE|(Morgan & Shahjahan, 2014, pp. 200–201)]]
>
> *When test instruments developed in specific contexts are directly transferred cross-nationally, cultural differences and linguistic nuances frequently trigger differential item functioning... threatening the foundational assumption of a universal space of equivalence.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **关键概念辨析：题目影响（Impact）与题目偏差（DIF/Bias）**
>   - **题目影响（Impact）** 两组人群在题目得分上的原始平均差异，反映了两组在所测目标[[Construct|构念]]整体能力分布上的真实差距。
>   - **题目功能差异（DIF）** 在严格控制了两组学生真实能力水平完全相同（Matched Ability）后依然残存的作答差异，属于测量技术上的系统偏差。
> - **[[Epistemic Stances|认识论立场]]** 现代测验公平观认为，测验题目的有效性必须建立在跨群体[[Measurement Invariance|测量不变性]]（Measurement Invariance）的基础之上；任何未加控制的文化、语言或情境特异性载荷均是对被测构念纯粹性的污染。
> - **有效性标准** 显著性检验（卡方值）与[[Effect Size|效应量]]门槛（如 Mantel-Haenszel 变换效应量绝对值判定）的双重把关。
> - **不声称回答的问题** DIF 统计检验只能指出“某道题在两组能力相等的学生中存在表现差异”，不能直接自动解释“差异由何种具体的文化、语言或翻译漏洞所致”；最终定性必须依赖领域专家与语言学家的质性内容审查。

> [!method-stack] 方法层级
> - **研究设计** 跨组准实验对照设计、大规模测验预试与正式实施数据质控。
> - **数据收集** 统一试卷多语种翻译施测数据、人口学背景[[Questionnaire|问卷]]。
> - **分析方法** 非参数方法（曼特尔-亨斯泽尔检验，Mantel-Haenszel, MH）、参数方法（逻辑斯蒂回归法，Logistic Regression）、基于[[Item Response Theory|项目反应理论]]（IRT）的似然比检验（Likelihood Ratio Test）与 Lord 面积法。
> - **辅助技术** 匹配准则选择（总分分层 vs. 纯化后潜[[Variable|变量]]能力估计）、题目纯化迭代循环（Item Purification）。

---

> [!taxonomy] 题目功能差异的核心类型
> - **一致性 DIF（Uniform DIF）** 在所有能力水平 $\theta$ 上，参照组的答对概率均系统性高于（或低于）焦点组；在项目特征曲线（[[Intraclass Correlation Coefficient|ICC]]）上表现为两条曲线仅发生水平平移，彼此平行而不相交（主要由[[Item Analysis|题目难度]]参数 $b_i$ 的组间差异引起）。
> - **非一致性 DIF（Non-uniform DIF）** 答对概率的优势方向随被试能力水平的变化而改变；在项目特征曲线上表现为两条曲线斜率不同且相互交叉（主要由题目区分度参数 $a_i$ 的组间差异引起）。

> [!formula-step] 公式步骤一　曼特尔-亨斯泽尔（Mantel-Haenszel）胜算比
> $$\alpha_{\text{MH}} = \frac{\sum_{j=1}^K A_j D_j / N_j}{\sum_{j=1}^K B_j C_j / N_j}, \quad \Delta_{\text{MH}} = -2.35 \ln(\alpha_{\text{MH}})$$
>
> **这个公式在做什么** 在将受试者按测验总分划分为 $K$ 个能力匹配层级的条件下，汇总各层级中参照组与焦点组答对该题的加权相对优势，并转换为 [[Educational Testing Service|ETS]] 测验量尺[[Effect Size|效应量]]指标。
>
> **符号说明**
> - $K$：依据总分划分的能力匹配层数（通常划分为若干分段）。
> - $A_j, B_j$：在第 $j$ 层级中参照组答对与答错该题目的人数。
> - $C_j, D_j$：在第 $j$ 层级中焦点组答对与答错该题目的人数；$N_j$ 为该层总人数。
> - $\Delta_{\text{MH}}$：ETS 标准化效应量（$|\Delta_{\text{MH}}| < 1.0$ 为 A 级微弱 DIF，忽略不计；$|\Delta_{\text{MH}}| \ge 1.5$ 且统计显著为 C 级严重 DIF，通常须剔除或重写）。

> [!formula-step] 公式步骤二　逻辑斯蒂回归检验模型
> $$\operatorname{logit}[P(Y = 1)] = \beta_0 + \beta_1 X + \beta_2 G + \beta_3 (X \cdot G)$$
>
> **这个公式在做什么** 同时检验题目是否存在一致性 DIF 与非一致性 DIF。
>
> **符号说明**
> - $X$：受试者的匹配能力得分（总分或标准化潜[[Variable|变量]]值）。
> - $G$：群体归属虚拟变量（参照组 = 0，焦点组 = 1）。
> - $\beta_2$：群体主效应系数（若 $\beta_2 \neq 0$ 且 $\beta_3 = 0$，表示存在一致性 DIF）。
> - $\beta_3$：能力与群体的[[Interaction Effect|交互效应]]系数（若 $\beta_3 \neq 0$，表示存在非一致性 DIF）。

---

> [!method-fit] 适用判断
> - **适合使用**
>   1. **跨国测验的翻译与文化适应性审查** 在 [[PISA]]、[[TIMSS]] 等跨国评估中，检验源语言试题（英语/法语）翻译为数十种本土语言版本后，是否因语意多义性或文化习俗差异导致特定国家学生答题受损。
>   2. **测验性别公平性审查** 检验数理题目是否过度引入具有特定性别经验偏向的情境（如汽车发动机机械构造或特定编织工艺）。
>   3. **高利害标准化入学与资格考试** SAT、ACT、GRE、教师资格统考题库在投入正式实测前的预试筛选与偏差剔除。
> - **谨慎使用**
>   - [[Sample Size Determination|样本量]]在数万人以上的超大型数据集；此时极微弱且无实质教学意义的细微差异也会表现为卡方统计学显著，研究者必须以实际[[Effect Size|效应量]]大小而非 $p$ 值作为主要决策依据。
> - **不适合使用**
>   - 参照组与焦点组在目标[[Construct|构念]]上存在极端巨大的真实能力鸿沟（Ability Distribution Overlap 极低）的数据集；匹配层中缺乏可比重叠样本会导致估计严重发散。

---

> [!method-limits] 方法局限与风险
> - **对匹配准则纯净度的依赖（污染效应）** 若使用包含待测题目的测验总分作为匹配标准，当测验中包含多道带有偏倚的题目时，匹配标准本身已被污染，必须采用多轮迭代纯化（Item Purification）程序逐步剔除偏倚题。
> - **跨国测验中的广泛存在与政治化处理** 比较教育学者尖锐指出，在跨国大型测评中，几乎绝大多数题目在跨越几十个不同语言文化体系时均存在不同程度的 DIF；为了维持“跨国统一标尺”的运作，跨国组织常通过合并国家参数或放宽容忍门槛来掩盖文化特异性，引发学术界对跨国[[Commensuration|通约]]度量空间虚构性的深刻批判。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Measurement Invariance]] | 方法 | 检验因子负荷与截距跨组等值的多组[[Confirmatory Factor Analysis\|验证性因子分析]]方法，与 DIF 共享测验公平计量目标。 |
> | [[Item Response Theory]] | 方法 | 建立不受样本分布影响的题目特征曲线、开展参数化 DIF 检验的模型基础。 |
> | [[Matrix Sampling]] | 方法 | 跨国评估中生成稀疏数据、需要依靠无偏锚题维系跨卷本连接的抽样设计。 |
> | [[Plausible Values]] | 方法 | 依赖于无偏题目参数估计以准确抽取后验潜在能力的插补技术。 |
> | [[Cross-cultural Validity]] | 概念 | DIF 检验旨在维护与求证的核心效度类型。 |
> | [[Space of Equivalence]] | 概念 | 批判跨国评估试图利用 DIF 统计净化抹平文化[[Heterogeneity\|异质性]]、虚构等值空间的理论透镜。 |
> | [[PISA]] | 事实 | 广泛应用国际 DIF 检验、同时在学界遭遇最激烈文化偏倚指责的大规模跨国测评。 |
> | [[Argument_Grek_2009_JEdPolicy\|Grek (2009)]] | 论证 | 剖析 PISA 依托统计规程抹平文化多样性、建立跨国[[Commensuration\|通约]]技术界面的文献。 |
> | [[Argument_Morgan_Shahjahan_2014_CE\|Morgan and Shahjahan (2014)]] | 论证 | 剖析跨国测评试题直接移植中遭遇的跨文化水土不服与测量效度危机的[[Document\|文献]]。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Grek_2009_JEdPolicy|Grek (2009)]] — 揭示国际评估项目如何通过心理测量技术过滤国家具体文化背景，将复杂的教育生活压缩为统一的可[[Commensuration|通约]]技术指标。
> - [[Argument_Morgan_Shahjahan_2014_CE|Morgan and Shahjahan (2014)]] — 追踪[[OECD|经合组织]]试图直接跨国移植测评表现性任务时遭遇的[[Cultural Validity|文化效度]]危机与试题参数适应性修正历程。
