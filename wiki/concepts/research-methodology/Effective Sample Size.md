---
title: Effective Sample Size
aliases:
  - 有效样本量
  - 实际有效样本量
  - ESS
  - Effective Sample Size (ESS)
  - 有效样本规模
summary: "在整群随机试验与分层复杂抽样中，剔除群内相关系数（ICC）导致的设计效应（Design Effect）损耗后，样本实际承载的相当于独立同分布简单随机抽样的真实统计信息量与推断功效。"
type: concept
domain: "research-methodology"
related_count: 27
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - concept/research-methodology
  - method/randomised-controlled-trials
  - method/cluster-randomised-trials
  - theme/statistical-power
  - theme/evidence-based-education
related_concepts:
  - "[[Causality]]"
  - "[[Evaluation Research]]"
  - "[[Type I and Type II Errors]]"
  - "[[Attrition]]"
  - "[[Variable]]"
  - "[[Internal Validity]]"
  - "[[What Works Movement]]"
  - "[[Unit of Analysis]]"
  - "[[Evidence-Based Education]]"
  - "[[Business as Usual]]"
  - "[[Clinical Trial]]"
related_theories: []
related_methods:
  - "[[Sample Size Determination]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Random Sampling]]"
  - "[[Confidence Interval]]"
  - "[[Effect Size]]"
  - "[[Cluster Randomized Trials]]"
  - "[[Cluster Sampling]]"
  - "[[Random Assignment]]"
  - "[[Standard Error]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Meta-analysis]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Education Endowment Foundation]]"
  - "[[National Center for Education Evaluation and Regional Assistance]]"
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
confidence: high
status: completed
created: 2026-09-14
updated: 2026-09-17
---

# Effective Sample Size

---

## 定义

> [!def] 核心定义
> **有效[[Sample Size Determination|样本量]]（Effective Sample Size，ESS）**指在复杂抽样设计、多层嵌套模型或整群[[Randomised Controlled Trials|随机对照试验]]（Cluster-Randomised Controlled Trials）中，扣除由聚集性（Clustering）和[[Intraclass Correlation Coefficient|群内相关系数]]（Intra-Cluster Correlation Coefficient，ICC）所引起的方差膨胀与设计效应（Design Effect，Deff）后，样本在统计学上实际等价于“独立同分布[[Random Sampling|简单随机抽样]]（Simple Random Sampling）”的观测单位数量。它直接决定了统计检验力（Statistical Power）与参数估计的精度（即[[Confidence Interval|置信区间]]宽度）。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 56–57)]]

> [!concept-lens] 概念透镜
> - **含义** 这个概念指向复杂研究设计中“表面观察人头数（名义样本量）”与“实际独立统计信息量（有效样本量）”之间的本质落差，揭示了同校同班学生相似性对[[Causality|因果推断]]功效的内在稀释。
> - **用途** 帮助[[Evaluation Research|评估研究]]者在规划整群试验时穿透名义规模假象，精确计算达成预设检验力（如 80% 功效检测最小可测[[Effect Size|效应量]] MDES）所需的最少学校数量（集群数）与每校学生数。
> - **边界** 它解决的是样本量对估计精度与假阴性错误（[[Type I and Type II Errors|Type II error]]）的控制能力，无法自动消除由选择性[[Attrition|流失]]、混淆[[Variable|变量]]或测量偏倚带来的[[Internal Validity|内部效度]]系统性偏差。

> [!citation-card] 试验样本规模演进与信息量积累
> “对英格兰[[Education Endowment Foundation|教育捐赠基金会]]（EEF）与美国[[National Center for Education Evaluation and Regional Assistance|国家教育评估与区域援助中心]]（NCEE）资助的 141 项 RCT 进行的重新分析显示，多数试验效应量微弱（均值 0.06 个标准差）且置信区间过宽（均值宽度 0.30 个标准差），据此得出这些试验缺乏信息量的结论；然而这忽视了试验质量的动态演进。有效性运动的基本前提是不仅持续探究‘何为有效’，更要不断探究‘如何更好地研究何为有效’。一个明证是：EEF 试验的有效样本量随着时间推移持续大幅攀升（与早期试验相比，2014 年后的有效样本量几乎翻番），这意味着 EEF 资助的试验正在变得越来越具备实质信息量。”[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 56–57)]]
>
> *"A fundamental premise of the [[What Works Movement]] is to keep learning not just about what works but also about how to best research what works. A good example of this is that the effective sample size of EEF trials over time has risen over time (and almost doubled in 2014 when compared to earlier trials), meaning that EEF trials have become progressively more informative (Sanders, 2019)."*

> [!boundary]- 概念边界
> - 不等于 名义样本量（Nominal Sample Size） — 名义样本量仅指研究中登记或收集的总人头数（$N$）；有效样本量则是经群内相关系数折扣后的统计信息量（$N_{eff}$），在整群试验中 $N_{eff} \le N$。
> - 不等于 [[Unit of Analysis|分析单位]]（Unit of Analysis） — 分析单位是数据分析和统计模型中的基本观测实体（如学生或学校）；有效样本量是对整个样本统计推断信息当量的连续度量。

---

## 概念辨析

> [!contrast-table] 统计样本概念横向对比
> | 维度 | 有效[[Sample Size Determination\|样本量]]（Effective Sample Size） | 名义样本量（Nominal Sample Size） | 最小可测[[Effect Size\|效应量]]（MDES） |
> |---|---|---|---|
> | **核心含义** | 考虑多层相关性后等效于[[Random Sampling\|简单随机抽样]]的独立信息量 | 试验中实际招募并测量的总受试者人数 | 在既定功效与显著性水平下能可靠检出的最小效应门槛 |
> | **计算要素** | 名义样本量 $N$、集群规模 $m$ 与群内相关系数 $\rho$ | 收集到的原始记录总行数 | 有效样本量、双尾 $\alpha$ 水平、统计功效 $1-\beta$、协变量解释方差 $R^2$ |
> | **方法学功能** | 真实反映参数估计方差与[[Confidence Interval\|置信区间]]收窄极限 | 反映项目实施的物理覆盖面与田野组织负荷 | 决定研究能否识别现实中微弱而有教育学价值的微小进步 |
> | **局限性** | 不直接反映外部代表性与实施质量 | 存在“大样本假象”，极易高估真实统计推断精度 | 依赖事前参数假定，若实际 [[Intraclass Correlation Coefficient\|ICC]] 高于预期则 MDES 显著恶化 |

---

## 核心要素

> [!feature] 核心要素与数学逻辑
> - **设计效应（Design Effect，Deff）** 在[[Cluster Randomized Trials|整群随机试验]]中，设计效应度量了[[Cluster Sampling|整群抽样]]相较于[[Random Sampling|简单随机抽样]]导致的估计方差膨胀倍数，其经典形式为：
>   $$Deff = 1 + (m - 1)\rho$$
>   其中 $m$ 为每个集群（如学校或班级）的平均分析受试者数，$\rho$ 为主要结局指标的[[Intraclass Correlation Coefficient|群内相关系数]]（ICC）。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, p. 57)]]
> - **有效[[Sample Size Determination|样本量]]数学表达（ESS Formula）** 当总名义样本量为 $N$、划分为 $K$ 个规模为 $m$ 的集群时（$N = K \times m$），有效样本量计算为：
>   $$N_{eff} = \frac{N}{Deff} = \frac{N}{1 + (m - 1)\rho} = \frac{K \cdot m}{1 + (m - 1)\rho}$$
>   当 $\rho > 0$ 且 $m$ 较大时，集群内新增样本的边际信息贡献急剧递减，有效样本量趋向于 $K / \rho$。
> - **集群数量的主导决定性** 在教育试验中，由于校内学生存在相似的生源背景与师资环境，ICC 通常处于 0.10 至 0.20 之间。单纯在既有学校内增加测试学生数（增大 $m$）对扩增有效样本量收效甚微；唯一能显著扩大有效样本量的途径是增加参与试验的独立学校总数（增大 $K$）。

> [!logic-map]- 群体聚集效应与有效样本量损耗机制
> ```mermaid
> flowchart TD
>     A["学校环境与师资同质性<br>(Intra-cluster Correlation: ρ > 0)"] --> B["学生间观测值非独立"]
>     B --> C["设计效应方差膨胀<br>(Deff = 1 + (m-1)ρ)"]
>     C --> D["名义样本量 N 严重损耗"]
>     D --> E["真实有效样本量 Neff = N / Deff"]
>     E --> F["标准误增大 / 置信区间展宽"]
>     G["扩增独立学校数量 K<br>(而非单校学生数 m)"] --> H["直接冲破设计效应瓶颈"]
>     H --> E
> ```

---

## 围绕概念形成的命题

---

### 命题一　整群随机试验由于群内相关系数的存在必然导致名义样本量的统计信息量衰减

> [!concept-lens] 集群聚集与信息冗余机制
> 探讨教育场景中个体嵌套于班级和学校所必然带来的观测值自相关，以及名义大样本如何掩盖实际推断功效匮乏的方法学陷阱。

> [!claim] Hedges, L. V.
> **集群设计效应的方差膨胀定律** 在学校层级进行[[Random Assignment|随机分配]]时，即使名义招募了数万名学生，由于同一学校内学生共享教育环境与社区背景，其测验得分残差高度相关（典型 [[Intraclass Correlation Coefficient|ICC]] 为 0.10–0.25）；若忽视有效[[Sample Size Determination|样本量]]折算而将学生直接视为独立个体进行简单回归或 t 检验，[[Standard Error|标准误]]将被严重低估达 2 至 5 倍，导致假阳性错误率从 5% 剧增至 30% 以上；必须严格以有效样本量为基准重新校正参数估计的不确定性。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, p. 57)]]

> [!claim] Demack, S.
> **多层教育试验样本量规划与 ICC 敏感性** 在设计以学校为单位的整群 [[Randomised Controlled Trials|RCT]] 时，决定统计功效的核心瓶颈几乎完全取决于学校数量而非学生数量。若 ICC 为 0.15、单校样本为 50 人，设计效应为 $1 + 49 \times 0.15 = 8.35$，意味着 5,000 名学生的名义样本实际承载的有效样本量仅相当于约 598 名独立随机学生；若盲目追求大名义样本而压缩学校总数，试验将陷入严重的统计检验力赤字。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, p. 57)]]

---

### 命题二　通过扩展独立整群数量实现有效样本量翻番是破解微弱效应与置信区间过宽的决定性途径

> [!concept-lens] 统计精度与证据信息量积累机制
> 探讨试验机构如何通过大规模招募网络扩增学校总数，以有效样本量的实质增长回应学术界关于教育试验“缺乏信息量”的方法学指责。

> [!claim] Sanders, M.
> **有效样本量翻番与试验信息量演进** 早期教育试验常受限于招募能力，平均每项试验仅涵盖 20 至 30 所学校，导致有效样本量过小，其 95% [[Confidence Interval|置信区间]]宽度达 0.30 个标准差，无法与现实中 0.05 至 0.10 的细微教育干预进展相匹配；自 2014 年起，[[Education Endowment Foundation|EEF]] 通过国家级招募动员将单项试验规模扩充至 80 至 100 所学校以上（受试学生常超 8,000 人），推动实际有效样本量翻番，使置信区间显著收窄，从而能够以高确定性将微弱成效与零效应精准剥离。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 56–57)]]

> [!claim] Edovald, T. & Nevill, C.
> **有效样本量扩张对“无信息量论”的有力反驳** 孤立地将早期试验平均置信区间较宽定性为“试验缺乏信息量”是静态且片面的。在[[Evidence-Based Education|循证教育]]实践中，机构的方法学生产能力随时间显著进化；有效样本量的持续增长证明大规模田野试验正稳步具备分辨微弱效应的高阶推断精度，能够向政策制定者清晰判定哪些广受欢迎的教学方案并不优于[[Business as Usual|常态教学]]，为优化公共教育资源配置提供刚性决策依据。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, p. 57)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **集群效应方差膨胀命题** | 群内相关系数必然大幅折损名义样本量，造成推断功效严重衰减 | 学校、班级、学区等具有层级嵌套特征的教育现场试验 | Hedges (2007); Demack (2019) |
> | **有效样本量扩增与精度提升命题** | 唯有大幅增加独立集群（学校）数量才能实质倍增有效样本量，收窄置信区间并支撑微弱效应检出 | 大规模国家级循证干预试验、跨校推广性评估与中介机构方法学演进 | Sanders (2019); [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]] |

---

## 概念演变

> [!dev-timeline] 统计功效与有效[[Sample Size Determination|样本量]]演进历程
> - **1970s–1980s — 统计学奠基阶段** 抽样统计学家（Kish, 1965; Cochran, 1977）形式化定义复杂抽样中的设计效应（Design Effect）与有效样本量概念，主要用于全国性人口普查与社会调查。
> - **1990s–2000s — 多层模型与整群试验规程化** 随着[[Hierarchical Linear Model|多层线性模型]]（HLM）的成熟，以 Donald Rubin、Larry Hedges 等为代表的方法学家将有效样本量推导引入[[Clinical Trial|临床试验]]与教育实验，确立整群 [[Randomised Controlled Trials|RCT]] 的样本量测算公式。
> - **2010–2014 — 教育有效性运动早期的功效危机** 英国 [[Education Endowment Foundation|EEF]] 与美国 [[National Center for Education Evaluation and Regional Assistance|NCEE]] 早期资助的 RCT 由于招募学校偏少，有效样本量普遍偏低，导致多数试验[[Confidence Interval|置信区间]]极宽，被部分学者批评为“耗资巨大但缺乏实质信息量”。
> - **2014–至今 — 国家尺度动员与有效样本量倍增** EEF 建立全国性学校动员网络与统一数据归档机制，单项试验平均纳入学校数量翻倍，推动有效样本量整体翻番，确立了全球教育现场因果评估的精度新基准。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] [[Confidence Interval|置信区间]]宽度与教育试验的“信息量”标准之争
> > 学界围绕如何判定大规模整群教育试验的学术价值存在尖锐分歧。
> >
> > - **Lortie-Forgues & Inglis（2019）** 对 141 项 [[Education Endowment Foundation|EEF]]/[[National Center for Education Evaluation and Regional Assistance|NCEE]] 试验进行二阶重分析，指出其平均[[Effect Size|效应量]]仅为 0.06 个标准差，而置信区间宽度高达 0.30 个标准差，断言多数试验因统计推断极其不精确而“缺乏信息量（uninformative）”，难以指导实践。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, p. 56)]]
> > - **Sanders & Nevill（2019）** 反驳指出单纯基于早期静态置信区间宽度做出全盘否定是片面的；随着有效[[Sample Size Determination|样本量]]翻番，后续试验精度已大幅提高；更重要的是，证明干预“未优于常态实践”本身就是极为宝贵的负向信息，能避免公共教育财政浪费。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, pp. 56–57)]]

> [!warning] 追求超大有效样本量引发的干预保真度稀释
> 为了追求充足的有效样本量以获取微弱效应的统计检验力，研究者被迫招募成百上千所学校展开超大规模试验。然而，随着组织规模急剧膨胀，跨校培训质量、材料递送与教师依从度极易发生剧烈衰减，导致干预在现场被严重稀释，最终陷入“样本量足够大但干预实质已经名存实亡”的效度悖论。[[Argument_Edovald_Nevill_2021_ECNUROE|(Edovald & Nevill, 2021, p. 57)]]

---

## 实证数据

> [!ref-table]- 国际大规模教育现场试验[[Sample Size Determination|样本量]]与统计精度实证结果
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无[[Effect Size\|效应量]]） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021, p. 56)]]<br>(重审 Lortie-Forgues & Inglis, 2019) | $N = 1,222,024$ 名学生，涵盖英美 141 项 RCT 试验 | 二阶试验[[Meta-analysis\|元分析]]与统计精度重审 | 核心学业产出效应量分布与精度 | 平均效应量为 0.06 个标准差；平均 95% [[Confidence Interval\|置信区间]]宽度为 0.30 个标准差 | 多数试验置信区间横跨零点且极宽 | 批评早期教育试验有效样本量不足导致检验力匮乏，许多试验无法区分真实效应与测量噪音。 |
> | [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021, p. 57)]]<br>(引述 Sanders, 2019) | 英国 [[Education Endowment Foundation\|EEF]] 资助的 150 余项学校现场 [[Randomised Controlled Trials\|RCT]]（覆盖逾 14,000 所中小学） | 长期机构发展追踪分析 | 试验有效样本量（ESS）时间演进趋势 | 2014 年后 EEF 资助试验的平均有效样本量相较于 2011–2013 年早期试验几乎翻倍 | 单校招募规模与学校总数显著扩增 | 表明随着招募与交付体系成熟，机构有能力成倍提升试验推断精度，化解早期信息量不足问题。 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 详尽记录了面对学界对 141 项英美教育 [[Randomised Controlled Trials|RCT]] 效应微弱且[[Confidence Interval|置信区间]]过宽（0.30 SD）的批评，[[Education Endowment Foundation|EEF]] 如何通过系统化制度动员将 2014 年后的试验有效[[Sample Size Determination|样本量]]翻番，使大规模试验逐步演变为能够高精度识别真实微弱效应的决策支持工具。

