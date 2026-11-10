---
title: Interaction Effect
aliases:
  - 交互效应
  - 交互作用
  - 调节效应
  - interaction effects
  - moderation effect
summary: "指多因子实验或观测研究中一个自变量对因变量的效应依赖于另一个变量或调节变量水平的非可加性现象。作为因果推断与条件异质性分析的核心，它揭示了教学干预在不同学习者认知特征与教学时序中的情境边界。"
type: concept
domain: "research-methodology"
related_count: 37
related_level: 3
related_stars: "💎"
related_color: "#fde68a"
concept_field: "research-methodology"
tags:
  - subject/research-methodology
  - experiment
  - causal-inference
  - quantitative-methods
related_concepts:
  - "[[Independent Variable]]"
  - "[[Dependent Variable]]"
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Heterogeneity]]"
  - "[[Evidence-Based Education]]"
  - "[[Sampling Error]]"
  - "[[Inquiry-Based Learning]]"
  - "[[Executive Function]]"
  - "[[Metacognition]]"
  - "[[Problem Solving]]"
  - "[[Inhibitory Control]]"
  - "[[Self-Efficacy]]"
  - "[[Direct Instruction]]"
  - "[[Productive Failure]]"
  - "[[Feedback]]"
  - "[[Student-Teacher Relationship]]"
  - "[[Socioeconomic Status]]"
  - "[[Differentiated Instruction]]"
  - "[[Working Memory]]"
  - "[[Paradigm]]"
  - "[[Visible Learning]]"
related_methods:
  - "[[Randomised Controlled Trials]]"
  - "[[Meta-analysis]]"
  - "[[Pre-test and Post-test]]"
  - "[[Effect Size]]"
  - "[[Research Synthesis]]"
  - "[[Analysis of Variance]]"
  - "[[Factorial Design]]"
  - "[[Intervention Research]]"
  - "[[Sample Size Determination]]"
  - "[[Statistical Significance]]"
  - "[[Multi-Arm Trial]]"
related_persons:
  - "[[Louis Cohen]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_DeJong_2023_ERR]]"
  - "[[Argument_Nielsen_2021_IRTP]]"
confidence: high
status: active
created: 2026-07-12
updated: 2026-11-11
---

---

> [!def] Interaction Effect
> **交互效应（Interaction Effect）** 指在多因子实验或观测研究中，一个[[Independent Variable|自变量]]（或干预措施）对[[Dependent Variable|因变量]]（或结果指标）的效应随另一个自[[Variable|变量]]或调节变量的水平发生系统性改变，表现出条件依赖性与相互调节的非可加性关系（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 323–324]]）。在统计建模中，交互效应通过乘积项（Product Term）捕获；在[[Causality|因果推断]]中，交互效应表征了因果[[Heterogeneity|异质性]]。
>
> 交互效应与**主效应（Main Effect）** 相对：主效应指某个自变量跨越其他所有条件后的独立平均效应；交互效应则揭示自变量的因果作用强度或方向随情境与对象特征转移的条件性规律。在现代学习科学与[[Evidence-Based Education|循证教育]]研究中，探究议题聚焦于教学法在何种条件、经由何种序列、针对具备何种认知特征的学生最为有效的高阶交互机制（[[Argument_DeJong_2023_ERR|De Jong et al., 2023, pp. 7–9]]）。

> [!concept-lens|notitle] 概念透镜
> - **含义** 交互效应构建了“X 对 Y 的影响取决于 Z（$X \to Y \mid Z$）”的条件因果结构，反映系统内部多重因素协同作用的非线性本质。
> - **用途** 识别干预的适用边界与受益人群，解释实验结果的分歧与异质性，指导自适应支架系统与分层教学序列的设计。
> - **边界** 交互效应独立于主效应（二者在方差分解中相互正交）；交互项显著时直接解释主效应极易产生严重误导；交互效应区别于中介效应（中介阐明因果传导链条 $X \to M \to Y$，交互阐明因果边界条件 $X \times Z \to Y$）。

> [!citation-card|notitle] 关键界定
> 两个变量相互作用，意味着一个自变量在某一水平下的效应与它在另一水平下的效应存在实质性差异。当两个自变量之间存在交互作用时，研究者无法仅凭一个自变量的主效应就对因变量的变化做出完整推断，必须同时审视另一个变量所处的状态。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch. 16, p. 323)]]
>
> *An interaction effect occurs when the effect of one independent variable on a dependent variable depends on the level of another independent variable... When interaction is present, the impact of one factor cannot be understood in isolation.*

> [!boundary]- 概念边界
> - 不等于主效应的缺失。主效应与交互效应在方差分解中完全正交；交互项显著时，孤立断言主效应平均值会导致微观机制被算术平均抹平。
> - 不等于中介效应（Mediation Effect）。中介效应旨在解释因果关系的内部传递路径（因果链条），交互效应旨在刻画因果关系成立的外部调节条件与适用界限。
> - 不等于简单的测量误差或随机波动。统计学意义上的交互效应特指总体参数中超出[[Sampling Error|抽样误差]]预期的系统性乘积增量。

---

> [!contrast-table|notitle] 概念辨析
> | 维度 | 主效应（Main Effect） | 交互效应（Interaction Effect / 调节） | 中介效应（Mediation Effect） |
> |---|---|---|---|
> | **核心问题** | [[Independent Variable\|自变量]] X 是否独立影响结果 Y？ | X 对 Y 的影响在何种条件 Z 下更强或更弱？ | X 是通过何种中间机制 M 导致了 Y？ |
> | **模型结构** | $X \to Y$ | $X \times Z \to Y$（Z 调节 X 与 Y 的关系） | $X \to M \to Y$（M 充当因果中介桥梁） |
> | **因果角色** | 平均因果效应（Averaged Effect） | 条件因果效应与边界条件（Boundary Conditions） | 内部传导机制与中间[[Variable\|变量]]（Causal Mechanism） |
> | **教育解释示例** | [[Inquiry-Based Learning\|指导式探究]]平均提升科学学习成绩 | 探究教学对高[[Executive Function\|执行功能]]学生的促进显著高于低执行功能学生 | 探究教学通过增强[[Metacognition\|元认知监控]]从而提高[[Problem Solving\|问题解决能力]] |

---

> [!feature] 核心要素
> - **条件依赖性与非可加性（Conditional Dependency）** 干预有效性随调节变量取值发生系统性变动。在线性模型中，$Y = \beta_0 + \beta_1 X_1 + \beta_2 X_2 + \beta_3 (X_1 X_2) + \epsilon$，交互项系数 $\beta_3 \neq 0$ 证实联合效应偏离简单线性相加基准。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, p. 323)]]
> - **几何形态多样性（Geometric Patterns）** 
>   - *平行线（无交互作用）*：不同调节水平下的回归线保持平行，处理效应在各群体间保持恒定。
>   - *相交线/交叉交互（Crossover Interaction）*：两条趋势线在观察范围内交叉，表明干预在一个群体中产生积极增益，而在另一群体中产生抑制影响（质性反转）。
>   - *发散或趋近形态（Ordinal Interaction）*：斜率方向一致但陡峭程度不同，表明干预在某一群体中效果被显著放大或稀释（量级差异）。
> - **统计检力瓶颈（Statistical Power Demands）** 检验交互项（乘积项）所需的样本容量显著高于主效应检验；在测量误差较大的教育现场实验中，交互效应容易受制于检力不足，需依托大样本[[Randomised Controlled Trials|随机对照试验]]或[[Meta-analysis|元分析]]中的亚组调节模型。

> [!logic-map]- 要素关系
> ```mermaid
> flowchart LR
>     X["自变量 X（教学干预）"] --> Y["因变量 Y（学业成就/迁移能力）"]
>     Z["调节变量 Z（认知特征/时序编排）"] -. "交互调节 (X × Z)" .-> Y
>     subgraph Patterns["交互几何形态"]
>         P1["平行线：无交互"]
>         P2["相交线：方向反转"]
>         P3["趋近/发散：量级调节"]
>     end
> ```

---

> [!concept-proposition] 命题一｜教学干预效能取决于学习者认知特征与外在指导结构的条件性匹配
> **适资因材教学交互机制（ATI）** 探讨教学干预的有效性如何受制于学习者的先前知识、[[Inhibitory Control|抑制控制]]能力及初始[[Self-Efficacy|自我效能感]]，论证教学结构与个体认知状态之间的高阶交互作用。

> [!claim] De Jong et al.
> **学习者认知特征对探究指导结构的强力调节** 教学干预的实际获益程度依赖学习者内部认知图式与外部指导形态的交互状态。在科学概念获得中，低抑制控制学生在缺乏结构化支架的开放探究中容易因无关干扰产生认知超载，而外源支架能有效补偿其抑制控制不足；同时，先验知识水平决定了直接指导的边界，高先验知识学生在显性讲授下容易出现专业逆转效应，而在开放探索中保持高效率。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, pp. 5–8)]]

---

> [!concept-proposition] 命题二｜教学时序与认知目标深度的交互作用决定知识的即时获取与长期迁移
> **时序反转与必要难度交互机制** 探讨先探索后讲授与先讲授后练习两种不同时序编排在面对机械识记与概念迁移目标时展现的截然相反的因果效应。

> [!claim] De Jong et al.
> **时序编排与认知目标深度的交叉交互** 教学时序与目标深度呈现显著交叉交互关系：若目标局限于机械事实提取，先期[[Direct Instruction|直接讲授]]表现出较高的即时答题效率；若目标指向深层概念理解与远迁移应用，以[[Productive Failure|生产性失败]]为代表的“先探究后讲授”序列显著优于纯讲授结构。此外，即时[[Pre-test and Post-test|后测]]往往掩盖这种优势，先探究学习者在经历尝试与辨析后所形成的认知韧性主要在数周后的延迟保持测验中显现。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, pp. 8–9)]]

---

> [!concept-proposition] 命题三｜以孤立主效应替代交互效应会导致循证政策推断的系统性失真
> **情境复杂性与证据合成失真** 揭示宏观循证排行榜通过清洗情境调节变量、将复杂交互关系降格为单一平均[[Effect Size|效应量]]所引发的方法学困境。

> [!claim] Nielsen & Klitmøller
> **消除调节变量与主效应排行榜的实践脱节** 循证证据合成若预先假定教学干预能独立产生特定的普适增益，将各个变量按孤立效应量大小排队，会系统性抹杀[[Feedback|教学反馈]]与[[Student-Teacher Relationship|师生关系]]、家庭[[Socioeconomic Status|社会经济地位]]及学生初始基础的交互效应。消除调节变量的单一因果处方在真实复杂的课堂情境中难以复现预期效果。[[Argument_Nielsen_2021_IRTP|(Nielsen & Klitmøller, 2021b, p. 80)]]

---

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **适资因材交互命题** | 干预效能受制于学习者认知特征（抑制控制、先验知识）与外在支架的匹配 | 科学教育模拟探究与自适应支架设计 | [[Argument_DeJong_2023_ERR\|De Jong et al. (2023)]] |
> | **教学时序目标命题** | 先探究后讲授序列在远迁移与深层理解上优于传统讲授，具有延迟显现特征 | 生产性失败设计与概念迁移实验 | [[Argument_DeJong_2023_ERR\|De Jong et al. (2023)]] |
> | **证据合成失真命题** | 消除情境调节变量并将多重交互降格为单一主效应排行榜导致政策失效 | 循证教育[[Research Synthesis\|证据综合]]与元分析解释 | [[Argument_Nielsen_2021_IRTP\|Nielsen and Klitmøller (2021b)]] |

---

> [!dev-timeline] 概念演变
> - **1920 年代–1930 年代 — [[Analysis of Variance|方差分析]]与乘积项数学确立** 罗纳德·费雪（Ronald A. Fisher）在农业试验设计中引入双因素与多因素方差分析，首次在数学上将交互效应从随机误差中解构出来。
> - **1977 年 — 适资因材教学交互（ATI）提出** 李·克隆巴赫（Lee Cronbach）与理查德·斯诺（Richard Snow）系统阐释学习者能力特质与教学干预方式的交互作用，奠定了[[Differentiated Instruction|差异化教学]]的实验方法学基础。
> - **2011 年 — 教育研究方法学中的多因子模型深化** [[Louis Cohen|路易斯·科恩]]（Louis Cohen）等人在教育科学研究方法中系统论证[[Factorial Design|因子设计]]、方差分析与交互效应图示解读规范。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, Ch. 16, pp. 323–325)]]
> - **2021 年–2023 年 — 现代学习科学时序交互与循证反思** 通用主效应神话被现代学习科学破除，学术界聚焦认知负荷、自适应支架与先探究后讲授时序在迁移测评中的深层交互机制。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, pp. 7–9)]]; [[Argument_Nielsen_2021_IRTP|(Nielsen & Klitmøller, 2021b, p. 80)]]

---

> [!debates|notitle] 学术争议
>
> > [!axis] 主效应普适推断 vs 条件性交互推断
> > 争鸣聚焦于教育[[Intervention Research|干预研究]]究竟应追求普遍有效的主效应，还是应深耕情境边界条件。
> >
> > - **主效应排行榜派** 主张通过大样本元分析计算单一平均效应量，为宏观政策决策提供直观的优先级排序依据。
> > - **条件交互批判派** 认为教学实践具有高度情境依赖性，抹杀调节变量与交互效应会导致实践指导失真。[[Argument_Nielsen_2021_IRTP|(Nielsen & Klitmøller, 2021b, p. 80)]]
>
> > [!axis] 显性指导优先 vs 适时支架与时序反转
> > 争论直接讲授与探究学习在教学流程中的最优配置方案。
> >
> > - **直接指导派** 强调[[Working Memory|工作记忆]]容量限制，主张始终以强外源指导优先以防范认知负荷超载。
> > - **时序交互派** 证明“先探索激活图式、后直接讲授巩固”的时序组合在深层概念迁移上显著优于纯直接讲授。[[Argument_DeJong_2023_ERR|(De Jong et al., 2023, pp. 8–9)]]

> [!warning|limits] 适用局限
> 检验交互项（乘积项）所需的统计检力（Statistical Power）显著高于主效应检验。在[[Sample Size Determination|样本量]]受限或测量误差较大的教育现场实验中，真实存在的弱交互作用极易被判定为不显著；研究者应避免将未达统计显著的交互项等同于各组效应完全均质。

---

> [!entry-map] 条目关联
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Factorial Design]] | 方法 | 因子设计是系统析离并检验主效应与交互效应的标准实验[[Paradigm\|范式]]。 |
> | [[Analysis of Variance]] | 方法 | 方差分析中的双因素或多因素模型提供了检验交互项[[Statistical Significance\|统计显著性]]的基本工具。 |
> | [[Randomised Controlled Trials]] | 方法 | 大样本[[Multi-Arm Trial\|多臂随机对照试验]]是检验教育干预异质性与条件因果效应的金标准。 |
> | [[Causality]] | 概念 | 交互效应刻画了因果关系的条件依赖性与情境敏感性。 |
> | [[Executive Function]] | 概念 | 执行功能（尤其是抑制控制）是调节探究学习成效的关键学习者特征。 |
> | [[Self-Efficacy]] | 概念 | 学生初始效能感与支架设计存在动态交互，优质探究环境能抹平效能鸿沟。 |
> | [[Productive Failure]] | 概念 | 生产性失败通过“先探索后讲授”的时序交互最大化概念理解与深度迁移。 |
> | [[Visible Learning]] | 概念 | 其单一效应量排行榜因系统性消除交互效应与关键调节变量而遭遇方法学批评。 |

---

> [!evidence-grid-a|notitle] 相关研究索引
> - [[Argument_DeJong_2023_ERR|De Jong et al. (2023)]] — 权威综述提出破除两派二元对立，强调基于学习者特征与时序交互整合教学。
> - [[Argument_Nielsen_2021_IRTP|Nielsen and Klitmøller (2021b)]] — 批判《可见的学习》抹杀交互效应与家庭背景，将复杂教学降格为线性因果处方。
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011)]] — 系统阐述双因素方差分析中主效应与交互效应的数学关系与几何图示。
