---
title: Floor and Ceiling Effects
aliases:
  - 天花板与地板效应
  - 天花板效应
  - 地板效应
  - ceiling effect
  - floor effect
  - range restriction
summary: "测量工具因题项难度分布或量程受限导致得分在最高端或最低端过度聚集的数据截断缺陷，会导致方差缩减并人为低估干预的真实因果效应量，是导致教育试验微弱效应的关键测量学根源"
type: concept
domain: "research-methodology"
related_count: 29
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - floor-and-ceiling-effects
  - psychometrics
  - research-methodology
  - educational-measurement
  - effect-size
  - validity
related_concepts:
  - "[[Scale of Measurement]]"
  - "[[Predictive Validity]]"
  - "[[Learning Gain]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Computerized Adaptive Testing]]"
  - "[[Causality]]"
  - "[[Didaktik]]"
  - "[[Business as Usual]]"
  - "[[Evidence-Based Education]]"
  - "[[Reliability]]"
  - "[[Document]]"
  - "[[Variable]]"
  - "[[Academic Achievement]]"
related_theories:
  - "[[Classical Test Theory]]"
  - "[[Item Response Theory]]"
related_methods:
  - "[[Questionnaire]]"
  - "[[Effect Size]]"
  - "[[Pre-test and Post-test]]"
  - "[[Item Analysis]]"
  - "[[Implementation and Process Evaluation]]"
  - "[[Internal Consistency]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Meta-analysis]]"
related_persons: []
related_facts:
  - "[[Catch Up Numeracy]]"
  - "[[Education Endowment Foundation]]"
  - "[[SPECTRUM]]"
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
  - "[[Argument_Lei_Ding_Chiu_2026_ERR]]"
related_instruments:
  - "[[Consensual Assessment Technique]]"
confidence: high
status: completed
created: 2026-09-15
updated: 2026-09-15
---

# Floor and Ceiling Effects

---

## 定义

> [!def] 核心定义
> 天花板与地板效应（Floor and Ceiling Effects，亦称量程截断效应）指测评工具（考试、[[Questionnaire|问卷]]、心理量表）因题项难度设置不合理或有效测量量程（Range）受限，导致受试群体得分严重偏态地堆积在量表最高端（天花板效应）或最低端（地板效应）的心理计量学缺陷（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, p. 54]]）。这种人为造成的方差收缩（Variance Restriction）抹平了受试者之间的真实能力差异，导致统计模型严重低估教学干预的真实因果[[Effect Size|效应量]]，成为大规模教育试验频现“微弱效应”或“零效应”的关键技术根源之一。

> [!concept-lens] 概念透镜
> - **含义** 指向测量工具敏感度在能力分布极端区间的结构性瘫痪，本质是[[Scale of Measurement|测量尺度]]与受试人群真实分布脱节。
> - **用途** 用于诊断评估测验是否具备足够的区分度，解释教育因果试验中效应量出现异常萎缩的方法学诱因。
> - **边界** 区别于干预本身的无效性；当两组真实学业差距确实存在但测验无法捕捉时，属于测量工具效度赤字而非实践失败。

> [!citation-card] 商业标准化测验的量程截断危机（Hodgen et al., 2019; [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）
> 在[[Catch Up Numeracy|小学数学干预]]试验 Catch Up Numeracy 中，评估团队采用市售标准化数学测试作为终结性[[Pre-test and Post-test|后测]]工具。然而，由于该商业测验题项难度阶梯分布不当、有效量程严重受限，导致最终测试数据遭遇了严重的天花板效应（高水平学生轻易取得满分）与地板效应（基础薄弱学生大量得零分）。这种量程截断人为抹平了干预组与对照组在分布两端的细微真实差距，严重低估了干预的真实效应量，动摇了统计推断的稳健性。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, p. 54)]]
>
> *“Recent analysis of archived data has shown that many assessments offer only moderate [[Predictive Validity]], and some evaluations have suffered from floor and ceiling effects (e.g., Hodgen et al., 2019)... truncation of variance artificially obscures real educational gains.”*

> [!boundary] 概念边界
> - **天花板效应（Ceiling Effect）** 测验整体过于容易，大量受试者达到满分或接近满分阈值，无法区分中等优秀与卓越能力者，干预组的高阶增益被尺度封顶。
> - **地板效应（Floor Effect）** 测验整体难度过大，后进生与弱势群体大面积取得零分或最低基线分，无法区分完全未学与取得微小进步者，补偿性干预效果被尺度垫底。
> - **不等于 样本同质性（Sample Homogeneity）** 样本同质性指抽样群体本身能力高度一致；而天花板与地板效应是即便总体能力高度异质，工具也强行将极端群体压缩至同一分值。

---

## 概念辨析

> [!contrast-table] 测量量程偏倚与有效性对比
> | 考察维度 | 天花板效应 (Ceiling Effect) | 地板效应 (Floor Effect) | 理想等距高灵敏量表 |
> |---|---|---|---|
> | **数据分布形态** | 极端负偏态，高分端出现尖锐垂直截断峰 | 极端正偏态，低分端出现尖锐垂直截断峰 | 围绕被试群体真实水平呈现平滑正态或均匀分布 |
> | **直接后果** | 掩盖高能力受试者的额外[[Learning Gain\|学业增益]] | 抹杀学困生与薄弱班级的微观认知进步 | 高保真捕捉从弱势到卓越全谱系的干预因果效应 |
> | **对[[Effect Size\|效应量]]的扭曲** | 方差分母被压缩但分子差异截断更甚，效应量严重衰减 | 组间差异在底部归零，干预组微小进步被完全稀释 | 提供无偏因果效应量（$d$ 或 Hedges' $g$）估计 |
> | **典型发生场景** | 用常规结业测验评估拔尖培优或[[Higher-Order Thinking Skills\|高阶思维]]干预 | 用统考难度大题评估早期学困生基础补习干预 | 采用[[Computerized Adaptive Testing\|计算机自适应测验]]（[[Consensual Assessment Technique\|CAT]]）或长量程自适应题库 |

---

## 核心要素

> [!feature] 核心要素
> - **题项难度梯度失衡（[[Item Analysis|item difficulty]] Imbalance）** 测验缺乏足够数量的高难度题项（导致天花板）或缺乏足够的基础台阶题（导致地板），题项难度未能覆盖受试总体的完整能力潜能。
> - **方差人为收缩（Artificial Variance Truncation）** 由于两极数据被强行折叠至极值，样本实测方差远低于受试人群的潜在真实方差，违背多元统计分析的连续正态假定。
> - **[[Effect Size|效应量]]系统性衰减（Effect Size Attenuation）** 组间均值差因尺度边界而被人为缩减，使得原本具有实质教育意义的教学干预在数据报表上呈现为“无统计显著差异”（$d \approx 0.00$）。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, p. 54)]]
> - **弱势亚组评估失真（Subgroup Inequity Masking）** 地板效应最常发生在处境不利学生身上，导致旨在弥合贫困成就差距的补偿性干预无法在量化指标上展现成效。

> [!logic-map] 天花板与地板效应对[[Causality|因果推断]]的侵蚀逻辑
> ```mermaid
> flowchart TD
>     A["教学干预产生真实学业改进"] --> B["终结性测验测量量程不足"]
>     B --> C["高分端题项不足: 天花板效应"]
>     B --> D["低分端梯度缺失: 地板效应"]
>     C --> E["优等生全部撞顶，差异归零"]
>     D --> F["薄弱生全部触底，进步抹平"]
>     E & F --> G["两极真实方差与组间均值差被人为截断"]
>     G --> H["统计效应量人为断崖式衰减 (d ≈ 0.00)"]
>     H --> I["错误得出干预无效的虚假结论"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　量程截断是导致教育因果试验大面积呈现微弱效应与发表偏倚的隐形测量根源

> [!concept-lens] 探讨维度：测量工具心理计量属性对[[Causality|因果推断]]精度的系统性制约
> 评估方法学研究指出：学界常将试验呈现的零效应归咎于[[Didaktik|教学理论]]无效或[[Business as Usual|常态教学]]基线过高，却往往忽视了市售商业测验因量程截断造成的测量失效。

> [!claim] [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021, p. 54)]]; Hodgen et al. (2019)
> **测验截断引发的因果遮蔽** 在 [[Education Endowment Foundation|EEF]] 资助的 [[Catch Up Numeracy]] 数学试验中，由于选用的商业测验在两端存在严重的题项截断，评估数据显示干预成效微乎其微。然而[[Implementation and Process Evaluation|过程评估]]却表明学生在特定算术策略上取得了明显突破。深入的计量审计表明，这种假阴性结果很大程度上是由天花板与地板效应直接诱发的。由于缺乏跨学段的足够量程，工具强行把连续的能力增益压缩成离散的极值堆积，从而使高标准的量化试验沦为钝器。

---

### 命题二　防范量程截断面临两难抉择：自编测验的人为虚高 vs 商业测验的截断钝化

> [!concept-lens] 探讨维度：测量工具外部公信力与微观干预灵敏度的内在张力
> [[Evidence-Based Education|循证教育]]治理揭示：研究者在选择主要结局工具时，始终在“过度敏感的自编题”与“量程受限的通用商业题”之间艰难权衡。

> [!claim] [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021, p. 54)]]; Cheung & Slavin (2016)
> **测验选择的双重心理计量陷阱** 若采用紧密贴合教材的自编测验，极易与干预内容高度同构，从而人为夸大 50% 至 100% 的[[Effect Size|效应量]]（Cheung & Slavin, 2016）；但若严格遵循循证标准采纳独立的通用商业测验，又极其普遍地遭遇天花板与地板效应，导致对真实干预不敏感。破除此两难困境的唯一出路，在于资助机构必须前置委托专业计量团队开发高[[Reliability|信度]]、宽量程的权威测验库，并优先锚定国家级长期高利害普查数据（如英国 NPD 统考）。

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者与[[Document\|文献]] |
> |---|---|---|---|
> | **因果遮蔽命题** | 揭示天花板与地板效应如何通过截断方差人为稀释效应量，制造假阴性证据 | 量化因果评估、测验误差诊断、试验复盘 | Hodgen et al. (2019); [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]] |
> | **测量治理命题** | 阐明自编测验虚高与商业测验截断的两难困境，提出前置准入测量库的治理方案 | 证据中介机构规范、测验选择准则、测评基础设施 | Allen et al. (2018) |

---

## 概念演变

> [!dev-timeline] 概念演变与学术脉络
> - **1950s–1960s — [[Classical Test Theory|经典测验理论]]（CTT）下的截断表征** 心理统计学界在研究智力测验与学业测验时首次定义 ceiling and floor effects，主要视其为常模代表性不足导致的偏态分布问题。
> - **1970s–1980s — 题项反应理论（[[Item Response Theory|IRT]]）与信息函数突破** 随着罗施模型（Rasch）与多参数 IRT 的兴起，学者通过检验测验信息函数（Test Information Function, TIF）的覆盖范围，从数学形式上精确形式化了量表在极端能力区间的测量误差激增。
> - **2010s — 循证试验大浪潮下的实践暴露** 伴随英美大规模教育因果试验爆发，研究者大量依赖市售商业标准化测验（如阅读与数学标准化测试），导致天花板与地板效应在实地田野中大面积爆发，成为试验解释失败的显性危机。
> - **2014–至今 — 权威测量工具基准库的建立** [[Education Endowment Foundation|EEF]] 等机构在遭遇 [[Catch Up Numeracy]] 等截断案例后，全面推行涵盖学科统考（NPD）与非认知测评（[[SPECTRUM]]）的准入审查，将量程广度与极端分布灵敏度确立为资助前置硬指标。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021)]]

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 短量程精准聚焦 vs 宽量程常模通用
> > 争论焦点在于试验评估应针对特定年级能力范围设计紧凑精准的短量程试卷，还是使用跨学段的大规模通用量表。
> >
> > - **短量程针对性立场** 认为测验题项必须高度聚焦当前教学年段的核心认知目标，过多引入过难或过易题项会增加不必要的受试者答题疲劳。
> > - **宽量程跨学段立场（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）** 强调在真实班级中，弱势学童与拔尖学生的能力分布跨度极其宽广；唯有包含充分难度冗余的宽量程测验，才能同时避免天花板与地板效应。

> [!critique] 外部批评
> - **商业测验技术透明度赤字** Allen et al. (2018) 批评指出，许多商业测验开发商在技术白皮书中刻意隐瞒极值区间的测量误差与[[Predictive Validity|预测效度]]数据，仅提供全样本平均的[[Internal Consistency|内部一致性]]克隆巴赫 $\alpha$，误导了试验评估团队。

> [!warning] 适用局限
> 在自适应测试（[[Computerized Adaptive Testing]], [[Consensual Assessment Technique|CAT]]）或具备高低水平自动分支跳转的现代多阶段测验中，天花板与地板效应可通过算法动态派发适宜难度题目得到极大缓解。

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | Hodgen et al. (2019); [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]] | 英国 [[Catch Up Numeracy]] 小学数学干预效果试验 | 学校[[Randomised Controlled Trials\|随机对照试验]]（RCT）终结性测验质量审计 | 市售商业标准化数学测验题项难度与得分极值分布 | 数据呈现出严重的天花板效应（拔尖生极易满分）与地板效应（弱势生大面积零分），有效量程受阻 | 效应量估算受到严重削弱，未能准确反映[[Implementation and Process Evaluation\|过程评估]]中记录的认知突破 | 证明量程截断直接导致大规模教育试验呈现假性微弱效应 |
> | Allen et al. (2018) | 英国 [[Education Endowment Foundation\|EEF]] 试验数据库中广泛使用的商业阅读与数学测验 | 归档试验数据微观二次分析与[[Predictive Validity\|预测效度]]检验 | 商业测验得分与数年后英国官方高利害统考（GCSE）的相关性 | 绝大多数商业测试的预测效度仅达到中等程度，且对分布两端学生的[[Academic Achievement\|学业表现]]存在系统性测量漂移 | 预测效度中等，极端值误差显著 | 推动循证机构建立前置的标准化测验准入标准 |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 结合 [[Catch Up Numeracy]] 等实证案例，系统剖析商业测验天花板与地板效应如何侵蚀 [[Randomised Controlled Trials|RCT]] [[Causality|因果推断]]效度，并阐述 [[Education Endowment Foundation|EEF]] 建立前置测量工具库的治理经验。
> - [[Argument_Lei_Ding_Chiu_2026_ERR|Lei, Ding, & Chiu (2026)]] — 在跨学段[[Meta-analysis|元分析]]中反思学业测评工具难度受限对认知干预[[Effect Size|效应量]]的潜在衰减效应。
