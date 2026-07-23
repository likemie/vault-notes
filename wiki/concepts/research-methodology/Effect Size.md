---
title: Effect Size
aliases:
  - 效应量
summary: "比较不同干预或变量影响强度的标准化统计指标，被广泛用于元分析与证据排序，但其解释边界、聚合方式和政策用途长期存在争议"
type: concept
domain: "research-methodology"
related_count: 63
related_level: 5
related_stars: "⭐⭐⭐⭐⭐"
related_color: "#fecdd3"
tags:
- effect-size
- meta-analysis
- evidence-based-education
- methodology
- statistics
related_concepts:
  - "[[Visible Learning]]"
  - "[[Critique of Effect Size]]"
  - "[[Statistical Significance]]"
  - "[[Sample Size Determination]]"
  - "[[Confidence Interval]]"
  - "[[Standard Error]]"
  - "[[Developer Effect]]"
  - "[[Evaluation Research]]"
  - "[[Internal Validity]]"
  - "[[Research Purpose]]"
  - "[[Hypothesis]]"
  - "[[Variable]]"
  - "[[Homework]]"
  - "[[Whole Language]]"
  - "[[Professional Judgment]]"
  - "[[Surface and Deep Learning]]"
  - "[[Causality]]"
  - "[[Educational Evidence Clearinghouses]]"
  - "[[Achievement and Aptitude Tests]]"
  - "[[Heterogeneity]]"
  - "[[Document]]"
  - "[[Publication Bias]]"
  - "[[Construct]]"
  - "[[Construct Validity]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Random Assignment]]"
  - "[[Power Analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Covariate Adjustment]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Systematic Review]]"
  - "[[Experimental Research]]"
related_persons:
  - "[[Gene Glass]]"
  - "[[John Hattie]]"
  - "[[Lars Qvortrup]]"
  - "[[Adrian Simpson]]"
  - "[[Jacob Cohen]]"
related_facts:
  - "[[EEF Teaching and Learning Toolkit]]"
  - "[[Education Endowment Foundation]]"
  - "[[Promising Practices Network]]"
  - "[[Best Evidence Encyclopedia]]"
  - "[[What Works Clearinghouse]]"
  - "[[Playing for Success]]"
  - "[[Treasury Briefing on Student-Teacher Ratios]]"
related_arguments:
  - "[[Argument_Wrigley_2019_ERE]]"
  - "[[Argument_Qvortrup_2015_Paideia]]"
  - "[[Argument_Allerup_2015_Paideia]]"
  - "[[Argument_Pampaka_2016_IJRME]]"
  - "[[Argument_Higgins_2016_RE]]"
  - "[[Argument_Terhart_2011_JCS]]"
  - "[[Argument_Simpson_2017_JEP]]"
  - "[[Argument_Simpson_2019_ERE]]"
  - "[[Argument_Wiliam_2019_ERE]]"
  - "[[Argument_Kraft_2023_ER]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_OConnor_2020_AJLL]]"
  - "[[Argument_Sarbiewska_2019_JSR]]"
  - "[[Argument_Hattie_2010_NZJES]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Ross_Morrison_2021_ROE]]"
  - "[[Argument_Wolf_2020_JREE]]"
  - "[[Argument_ONeill_2012_NZJES]]"
confidence: medium
status: draft
created: '2026-05-01'
updated: 2026-07-19
---

## 定义

> [!def] 核心定义
> 效应量（Effect Size）是量化干预措施效果的标准化统计指标，计算方式为干预组与对照组结果差异除以标准差，旨在使不同研究的结果可跨测量工具比较。效应量是[[Meta-analysis|元分析]]的核心分析单位，[[Gene Glass]] 于 1976 年将其确立为跨研究比较的标准化工具，[[John Hattie]] 的 *[[Visible Learning]]*（2009）以效应量排名教学干预使其进入全球教育政策话语。在[[EEF Teaching and Learning Toolkit]]中，效应量被进一步转换为"额外学习月数"（[[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, p. 118]]）。

> [!concept-lens] 概念透镜
> - **含义** 效应量通过除以标准差消除测量单位，回答"干预产生了多大差异"，而非仅回答"差异是否显著"。[[Lars Qvortrup]]（2015）强调其"相对效果"功能——可比较不同研究之间干预组与控制组的相对变化（[[Argument_Qvortrup_2015_Paideia|Qvortrup, 2015, p.27]]）。
> - **用途** 为[[Meta-analysis|元分析]]提供可合并的通用尺度，为实践者和政策制定者提供关于"什么有效"的量化总结。
> - **边界** 效应量不直接说明效果的实质教育意义——同一个 d 值可能对应表层知识记忆或深层概念理解。[[Adrian Simpson]]（2017, 2018, 2019）进一步论证效应量实际测量的是试验清晰度（experimental clarity）而非干预有效性，详见 [[Critique of Effect Size]]。

> [!boundary] 概念边界
> - **不等于教育有效性** 效应量反映的是试验设计的信噪比，大 d 表示差异在统计上清晰，不表示差异大、重要或具有教育显著性。
> - **不等于因果效应** 效应量本身不区分相关与因果。其因果含义完全取决于产生它的研究设计。
> - **不替代原始单位** 标准化消除了原始测量单位，便于跨研究比较，但也抹除了效果的实际教育意义——知道提高了 0.3 SD 并不能直接知道学生多学会了几个单词。

---

## 概念辨析

> [!contrast-table] 与相关概念的区别
> - **vs [[Statistical Significance]]** — 效应量测量效果的大小，统计显著性测量效果是否可能仅由随机因素产生。统计显著性依赖于效应量和[[Sample Size Determination|样本量]]的乘积：$t = d\sqrt{n}$([[Argument_Allerup_2015_Paideia|Allerup, 2015, p.45]])。在 n=25 的双侧检验中，临界 $t=2.060$ 对应 $d \approx 0.412$，刚好接近《[[Visible Learning|可见的学习]]》的 0.40 阈值，这意味着 0.40 在特定样本量下才与 p≈0.05 相连，并非脱离样本量的普遍边界。
> - **vs [[Confidence Interval]]** — 效应量给出点估计，置信区间呈现该估计的误差范围。没有置信区间或[[Standard Error|标准误]]时，相邻效应量排名无法判断是否真的不同([[Argument_Allerup_2015_Paideia|Allerup, 2015, pp.47–48]])。Hattie 的效应量排名仅给 d 的点估计，未系统报告置信区间或[[Standard Error|标准误]]，也未进行相邻排名之间的显著性检验。
> - **vs 原始分数差异（Raw Score Difference）** — 原始分数差异保留了原始测量单位，效应量通过除以标准差消除了单位——这使跨研究比较成为可能，但也抹除了效果的实际教育意义。
> - **vs 意向处理分析效应** — 意向处理分析按原始[[Random Assignment|随机分配]]分析（无论实际接受与否），反映干预可获得性而非实际接受效果；效应量本身不区分这两种估计，但所基于的研究设计决定了其政策含义([[Argument_Pampaka_2016_IJRME|Pampaka et al., 2016, p.233]])。
> - **vs 最小可检测效应量** — 效应量是事后度量（干预实际产生了多大效果），最小可检测效应量是事前设计参数（研究能够检测到多大效果），详见下方[[#最小可检测效应量]]。

---

## 概念演变

> [!dev-timeline] 效应量的概念演变
> - **1964** — Benjamin Bloom 在 Stability and Change in Human Characteristics 中呈现了相关系数的聚合图表，其"两个标准差问题"（寻找与一对一辅导同样有效的小组教学方法）以标准差单位表述，为效应量在教育研究中的使用提供了早期范例([[Argument_Higgins_2016_RE|Higgins, 2016, p.37]])。
> - **1966** — Robert Rosenthal 出版 Experimenter Effects in Behavioral Research，包含大量标准化平均差异的计算并跨领域比较。Glass 本人承认 Rosenthal 发展了效应量的基础度量。
> - **1969** — [[Jacob Cohen]] 出版 [[Power Analysis|statistical power analysis]] for the Behavioral Sciences 第 1 版，引入 Cohen's d 作为标准化均值差的度量。
> - **1976** — [[Gene Glass]] 提出[[Meta-analysis|元分析]]概念，将效应量作为跨研究比较的标准化工具([[Argument_Higgins_2016_RE|Higgins, 2016, pp.36–37]])。
> - **1980** — Cooper 和 Rosenthal 的实证检验表明，[[Meta-analysis|元分析]]比传统叙事综述更不容易低估证据([[Argument_Higgins_2016_RE|Higgins, 2016, p.32]])。
> - **1988** — Cohen 出版 Statistical Power Analysis 第 2 版，以身高类比等直观方式解释效应量的实质含义([[Argument_Terhart_2011_JCS|Terhart, 2011, p.427]])。
> - **2009** — [[John Hattie]] 出版《[[Visible Learning|可见的学习]]》，综合 800 多项元分析和 50,000 多项研究，以效应量排名各类教育干预，使效应量概念进入全球教育政策和实践话语。
> - **2014** — [[EEF Teaching and Learning Toolkit]] 以效应量转换为"额外学习月数"的格式传播教育干预证据。
> - **2017 至 2018** — Simpson 发表系统批判，论证效应量测量的是试验灵敏度而非干预有效性（[[Argument_Simpson_2017_JEP|Simpson, 2017]], 2018）。
> - **2019** — Simpson 用"教一个匈牙利单词"思想实验展示同一干预可因测试设计产生 0 到无穷大的效应量；Wrigley & McCusker 通过 [[Education Endowment Foundation|EEF]] Toolkit 体育参与案例展示[[Meta-meta-analysis|元-元分析]]层面的三级失真；Wiliam 提出 11 点元分析评估清单([[Argument_Simpson_2019_ERE|Simpson, 2019]]; [[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019]]; [[Argument_Wiliam_2019_ERE|Wiliam, 2019]])。
> - **2020 至 2023** — Kraft 以教育[[Randomised Controlled Trials|随机对照试验]]中标准化学业成绩结果的经验分布替代 Cohen 基准，并强调 36% 的效应量小于 0.05 这一"失败频率"应成为解释政策相关性的核心参照([[Argument_Kraft_2023_ER|Kraft, 2023, pp.183–184]])。

---

## 核心要素

> [!feature] 效应量的核心要素
> - **技术定义与计算** 标准化均值差公式、与显著性检验和统计功效的关系、最小可检测效应量的设计含义
> - **解释框架** Cohen 的经验法则、Hattie 的影响气压计与关节点、Terhart 的实质解释、Kraft 的教育 [[Randomised Controlled Trials|RCT]] 经验基准、清算中心的政策阈值
> - **效应量变异的系统性来源** 测量类型、[[Sample Size Determination|样本量]]、研究设计、项目类型、[[Developer Effect|开发者效应]]和干预定义模糊性六类因素如何系统性地改变效应量

---

## 解释框架

### 技术定义与计算

> [!info] Fitz-Gibbon 的早期推动（1985）
> Fitz-Gibbon（1985: 45）在[[Meta-analysis|元分析]]发展早期即主张以效应量替代[[Statistical Significance|统计显著性]]作为[[Evaluation Research|评估研究]]的主要指标，将统计显著性重新定位为"[[Internal Validity|内部效度]]众多可能威胁中的一个"——效应大小是否满足[[Research Purpose|研究目的]]，而非是否跨过了显著性水平的任意截断点（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17|Cohen et al., 2011, Ch17, pp.339–340]]）。

> [!formula-step] 标准化均值差（Cohen's d）
> $$d = \frac{M_{\text{干预组}} - M_{\text{对照组}}}{SD_{pooled}}$$
>
> **读法** $d = 0.5$ 表示实验组均值比控制组高出半个标准差。$d = 0$ 表示两组无差异，$d$ 为负表示实验组表现更差。
>
> **目的** 标准化消除了不同测量工具的量表差异，使跨研究比较成为可能。但 Simpson（2017, 2018）论证了这一[[Hypothesis|假设]]的问题性——效应量实际上反映试验设计特征，而非干预有效性的纯粹测量（[[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, p. 118]]）。
>
> **与显著性检验的关系** 若比较干预前后两个分布，均值差 $\mu_1 - \mu_2$ 只有放到标准差 $\sigma$ 的尺度上才有意义。$d$ 本身不是可直接判定[[Statistical Significance|统计显著性]]的统计量；只有乘以 $\sqrt{n}$，得到 $t = d\sqrt{n}$，才接近用于检验 $\mu_1 = \mu_2$ 的 $t$ 统计量（[[Argument_Allerup_2015_Paideia|Allerup, 2015, pp.42–43]]）。
>
> **统计前提** $d$ 的直观解释依赖于三个前提：（1）前后分布近似对称且接近正态；（2）两个分布的标准差相同，均值差才可解释为简单位移；（3）若分布右偏或左偏，均值并不在分布中心。极端情况下，若基础分布类似柯西分布（Cauchy distribution），均值和方差本身不稳定，$d$ 的计算基础会崩塌（[[Argument_Allerup_2015_Paideia|Allerup, 2015, pp.45–49]]）。
>
> **第三[[Variable|变量]]影响** 边际分析与多[[Variable|变量]]控制会显著改变 $d$。TIMSS 2011 丹麦四年级数学中，教师学科专业资格的未控制效应量约 0.15，控制学生社会经济背景后降至 0.08 且不再显著——说明单个 $d$ 不能脱离第三变量独立解释（参见 [[Covariate Adjustment]]）。

---

### Cohen 的直观解释框架（1988）

> [!info] Cohen 的经验法则
> Cohen（1988）使用人体身高提供直观类比：$d = 1.0$ 表示 160cm 和 183cm 之间的差异([[Argument_Terhart_2011_JCS|Terhart, 2011, p.427]])。Cohen 同时定义了经验法则：
>
> | 效应量 | 标签 | 含义（假设正态分布） |
> |---|---|---|
> | $d = 0.2$ | 小 | 实验组均值高于对照组约 58% |
> | $d = 0.5$ | 中 | 实验组均值高于对照组约 69% |
> | $d = 0.8$ | 大 | 实验组均值高于对照组约 79% |

> [!warning] Cohen 框架的使用边界
> Cohen 本人强调这些标签是操作性的经验法则，不应被机械套用。[[Argument_Kraft_2023_ER|Kraft (2023)]]进一步论证教育[[Randomised Controlled Trials|随机对照试验]]的实际效应量分布远低于 Cohen 的锚点（详见下方[[#Kraft 的教育随机对照试验经验基准]]）。

---

### Hattie 的关节点与影响气压计

> [!info] Hattie 的影响气压计
> Hattie（2009）将 $d = 0.40$ 设定为教学有效性的基准或关节点（hinge point），认为它”设定了一个水平，创新的效果在此增强成绩的方式使我们能注意到真实世界的差异”（[[Argument_OConnor_2020_AJLL|O'Connor, 2020, p.142]]）。他将影响气压计分为四个区域（[[Argument_Terhart_2011_JCS|Terhart, 2011, pp.427–428]]；[[Argument_Sarbiewska_2019_JSR|Sarbiewska, 2019, p.121]]）：
>
> - **期望效应区（$d > 0.40$）** 最强正面影响，如教师清晰度 $d = 0.75$、自我报告成绩 $d = 1.44$
> - **教师效应区（$d = 0.15$–$0.40$）** 与教师一学年效果相当，如[[Homework|家庭作业]] $d = 0.29$
> - **发展效应区（$d = 0.0$–$0.15$）** 不上学也会发生的发展效应，如教师学科知识 $d = 0.09$
> - **负面效应区（$d < 0$）** 负面效果，如留级 $d = -0.16$、看电视 $d = -0.18$
>
> 约一半因素的效应量超过 0.4。Hattie 据此将[[Whole Language|全语言]]的 $d = 0.06$ 解释为零实际影响。[[Argument_Hattie_2010_NZJES|Hattie (2010, p.89)]]事后澄清该截断值基于 800 多项元分析的经验平均值，是”创造一个故事”的叙事工具而非绝对阈值。关于户外教育 $d = 0.17$ 的不一致，Hattie 澄清这是罕见的”附加效应”案例：该 0.17 叠加在项目立即效应 $d = 0.60$ 之上，总效应达 0.77。在 2015 年 Paideia 文章中，他进一步将 $d = 0.40$ 定位为所有可见教育影响的平均值——小学约 $d = 0.55$，中学约 $d = 0.25$——同一 $d$ 值必须结合学段和同类研究背景解释。他用网络学习三项元分析的平均 $d = 0.18$ 说明低于 0.40 的效果不必然无价值（Hattie, 2015, pp.11, 17）。

> [!tip] 如何理解关节点
> $d = 0.40$ 更像体检报告里的参考范围，而不是红绿灯。它能提醒教师这里值得追问，但不能替代[[Professional Judgment|专业判断]]。若一个中学阶段干预达到 $d = 0.30$，它可能低于《[[Visible Learning|可见的学习]]》总平均，却高于某些中学同类干预的常见水平；反之，一个 $d = 0.45$ 的项目若只测量短期记忆，也不能自动说明它促进了[[Surface and Deep Learning|深层学习]]。该关节点的争议详见 [[Critique of Effect Size]]。

---

### [[Argument_Terhart_2011_JCS|Terhart (2011)]]的详细解释

> [!info] 效应量的实质含义
> [[Argument_Terhart_2011_JCS|Terhart (2011, p.427)]]对效应量的技术含义提供了补充说明：
>
> **与统计显著性的关系** 如果将分析进行 100 次，只有 5 次实验组和对照组之间的差异可被解释为随机的，95 项研究中差异将是系统性的。但统计显著性不告诉任何人效应有多大或其实际意义是什么。
>
> **$d$ 的实质含义** $d = 1.0$ 意味着由于该因素，组的平均表现提高了一个标准差。如果在课堂中引入 $d = 1.0$ 的因素，意味着参与该项目的学生平均高于 84% 的未参与该项目的学生。
>
> **作业效应的具体示例** Hattie 报告的作业效应量 $d = 0.29$，其含义是：
> - 161 项研究中，65% 显示正面效应，35% 显示中性或负面效应
> - 有作业的班级平均表现高于 62% 的无作业班级学生
> - 在 Cohen 身高类比中，$d = 0.29$ 表示约 180cm 和 182cm 之间的差异
> - 如果在 100 个之前没有作业的班级引入作业，仅 21 个班级会看到学生表现提高
>
> Terhart 同时补充了关键警告：效应量不表示[[Causality|因果关系]]（p.427）。

---

### Kraft 的教育随机对照试验经验基准

> [!info] Kraft 的经验基准
> [[Argument_Kraft_2023_ER|Kraft (2023)]]主张以教育干预随机对照试验中标准化学业成就效应量的经验分布替代 Cohen 的 $0.2/0.5/0.8$ 通用锚点。他在 3,426 个效应量中发现分布相当稳定：30 百分位 0.02、50 百分位 0.10、70 百分位 0.21（[[Argument_Kraft_2023_ER|Kraft, 2023, pp.183–184]]）。
>
> Kraft 的基准同时考虑年度学习增益、教师与学校效应等经验参照点，聚焦"正向效应量的政策相关性"，因此承认这些基准具有主观性——更合适的做法是随新增研究检验既有基准在分布中的相对排名（[[Argument_Kraft_2023_ER|Kraft, 2023, pp.185-186]]）。Kraft 与 Simpson 的分歧在于：Simpson（2021）认为跨研究效应量因设计、测量、样本差异而本质不可比；Kraft 则认为完全禁止比较会削弱证据本位政策，只要承认噪声和限制，仍可从因果研究中获得粗略参照，但同意按"联盟表"排名是可疑的（[[Argument_Kraft_2023_ER|Kraft, 2023, p.184]]）。

---

### 清算中心的最低效应阈值

> [!info] 清算中心的最低效应阈值
> [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]]显示，部分[[Educational Evidence Clearinghouses|教育证据清算中心]]把最低效应量阈值直接写入项目评级规则：[[Promising Practices Network]] 的最高评级要求至少 0.25 个标准差的差异，[[Best Evidence Encyclopedia]] 要求至少 0.20 个标准差的影响。相比之下，[[What Works Clearinghouse]] 的最高项目效果判断要求统计显著正向效果，但不要求平均效果达到特定大小([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp.12–15]])。这说明效应量不仅是研究报告中的统计指标，也会成为证据中介机构划定"推荐/有希望/不推荐"边界的制度阈值。

---

### 实践者解释中的效应量

> [!info] 实践者解释中的效应量
> 在学校采购和项目评价中，教育产品消费者并不总能理解效应量和统计显著性等有效性指标，也常觉得正式证据来源缺少实施要求、使用满意度、成本和情境信息。效应量因此不是“读者看到数字就能行动”的指标，而需要和项目目标、使用强度、对照条件、测量工具和地方需求一起解释([[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, pp.120-121]])。

> [!example]
> 一个补充性教育技术项目可能只在每周少量课堂时间中使用。若它在标准化[[Achievement and Aptitude Tests|成就测验]]上的效应量很小，这不必然说明项目无价值；它可能主要改善学生动机、释放教师个别辅导时间或增加技术接入公平。反过来，一个较大的效应量若来自低质量对照组，也不能直接说明项目在本地学区一定值得采购([[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, pp.110-112]])。

---

### 效应量与统计功效

> [!math-principle] 效应量与统计功效
> 效应量与统计功效存在直接的函数关系。对于固定的[[Sample Size Determination|样本量]]、显著性水平和统计检验，统计功效和效应量是同一个东西的连续变换([[Argument_Simpson_2019_ERE|Simpson, 2019, p. 103, Figure 1]])。这意味着：
- 更大的效应量 → 更高的统计功效 → 更容易检测到"显著"结果
- 但这不意味着干预更有效，只意味着试验设计使组间差异更清晰可见

---

### 最小可检测效应量

> [!info] 最小可检测效应量
> [[Argument_Pampaka_2016_IJRME|Pampaka et al. (2016, p.233)]]介绍了与效应量密切相关的另一个概念：在给定统计功效下，研究设计能够检测到的最小效应量。最小可检测效应量是研究精度的度量：
>
> - 最小可检测效应量是"近期争论的焦点，因为其主要由经验法则决定"，缺乏系统性的精度标准
> - 最小可检测效应量越小，研究精度越高；精度提高意味着可检测到更小的干预效果
> - 与效应量的区别：效应量衡量干预"实际产生了多大的效果"（事后），最小可检测效应量描述研究"能够检测到多大的效果"（事前设计参数）

---

## 实证数据

> [!success] 独立研究与开发者研究的差异
> [[What Works Clearinghouse|WWC]] 数据库的系统性分析揭示了独立研究与开发者研究之间的效应量差异([[Argument_Wolf_2020_JREE|Wolf et al., 2020]])：
>
> - 全样本平均效应量为 +0.216（755 个效应量，169 项研究）（p. 441）
> - 控制协[[Variable|变量]]后，独立研究效应量为 +0.168，开发者研究为 +0.309（p. 441）
> - 同一干预子样本中，独立研究为 +0.194，开发者研究为 +0.324（p. 439）
> - 开发者研究更可能使用自编测量（29% vs. 8%）和[[Quasi-Experimental Designs|准实验设计]]（51% vs. 15%）（p. 434）
> - 独立研究的 95% 预测区间为 (−0.452, +0.788)，开发者研究为 (−0.311, +0.929），显示大量[[Heterogeneity|异质性]]（p. 441）

> [!success] 教育[[Randomised Controlled Trials|随机对照试验]]的经验分布
> 大规模教育随机对照试验的效应量分布显示，大多数干预的效果很小([[Argument_Kraft_2023_ER|Kraft, 2023]]; [[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021]])：
>
> - 36% 的教育干预随机对照试验标准化学业成就效应量小于 0.05，这比"小/中/大"标签更应成为解释政策相关性的核心基准([[Argument_Kraft_2023_ER|Kraft, 2023, p.183]])
> - 教育随机对照试验效应量分布的中位数约为 0.10；美国教育部委托的研究子样本中位数仅为 0.03，说明发表[[Document|文献]]中的效应量分布可能因[[Publication Bias|发表偏倚]]而偏向较大正值([[Argument_Kraft_2023_ER|Kraft, 2023, p.186]])
> - 141 项大型教育随机对照试验的平均成就效应量仅为 0.06 个标准差，且只有 23% 的效应显著大于零([[Argument_Ross_Morrison_2021_ROE|Ross & Morrison, 2021, p.112]])
> - 95% 的效应量为正，几乎所有被纳入的因素似乎都有正面效应，只是程度不同([[Argument_Terhart_2011_JCS|Terhart, 2011, p.427]])

---

## 围绕概念形成的命题

> [!concept-lens] 效应量变异的系统性来源
> 多项[[Meta-analysis|元分析]]识别了独立于干预实际有效性的方法论因素，它们系统性地与更大或更小的效应量相关联（[[Argument_Wolf_2020_JREE|Wolf et al., 2020, pp. 430–432]]）。以下六条命题分别对应六类系统性偏差来源。

---

### 命题一　效应量随测量类型而变化：自编测量产生系统性更大的效应量

> [!concept-lens] 测量工具的敏感性差异
> 不同结果测量工具对干预效果的敏感度不同。研究者或开发者自编的测量往往比独立标准化测量更贴近干预内容，因此产生更大的效应量——这一差异并非反映干预真实效果的变化，而是测量工具与被测[[Construct|构念]]的对齐程度差异。

> [!claim] [[Argument_Wolf_2020_JREE|Wolf et al. (2020)]]
> Cheung & Slavin（2016）、de Boer, Donker & van der Werf（2014）、Li & Ma（2010）等多个[[Meta-analysis|元分析]]发现自编测量产生的效应量比独立测量高 **0.20–0.29** 标准差。de Boer et al.（2014）发现其综述中 180 个测量中约三分之二是研究者或开发者自编的（[[Argument_Wolf_2020_JREE|Wolf et al., 2020, p. 431]]）。例：同一数学干预使用项目团队自编测试时效应量可能为 +0.45，使用州标准化测试时可能仅为 +0.20。

---

### 命题二　效应量随样本量增大而系统性减小

> [!concept-lens] [[Sample Size Determination|样本量]]与统计功效的关联
> 效应量与样本量之间存在负向、准对数关系。小规模研究更容易控制实施质量且需要较大效应量才能达到统计显著，导致小样本研究的效应量系统性偏高。

> [!claim] Slavin & Smith (2009)
> 效应量与样本量的经验关系（引自 [[Argument_Wolf_2020_JREE|Wolf et al., 2020, p. 431]]）：
>
> | 样本量 | 平均效应量 |
> |---|---|
> | <50 | +0.44 |
> | 51–100 | +0.29 |
> | 101–150 | +0.22 |
> | 151–250 | +0.23 |
> | 251–400 | +0.15 |
> | 401–1,000 | +0.12 |
> | 1,001–2,000 | +0.20 |
> | 2,000+ | +0.09 |

> Kulik & Fletcher（2016）在智能辅导[[Systematic Review|系统综述]]中报告了类似模式：<80 人 +0.78，81–250 人 +0.53，>250 人 +0.30。两种理论解释：小规模研究更容易控制实施质量；小规模研究需要非常大的效应量才能达到统计显著，只有效应量足够大的小研究才被发表（[[Argument_Wolf_2020_JREE|Wolf et al., 2020, p. 431]]）。

---

### 命题三　效应量随研究设计类型而变化：实验与非实验设计的差异证据不一

> [!concept-lens] 研究设计的[[Causality|因果推断]]强度
> 研究设计（实验 vs 非实验）对效应量的影响方向在[[Document|文献]]中并无一致结论，需要区分具体领域和干预类型。

> [!claim] 研究设计对效应量的影响
> Cheung & Slavin（2016）在 645 项研究的综合元分析中发现非实验设计平均效应量 +0.23 vs 实验设计 +0.16；Wilson, Gottfredson & Najaka（2001）发现非[[Experimental Research|实验研究]]效应量高 0.17 个标准差。但 Cook（2002）、de Boer et al.（2014）、Gersten et al.（2009）、Wilson & Lipsey（2001）均未发现实验与非实验设计间效应量的显著差异（[[Argument_Wolf_2020_JREE|Wolf et al., 2020, pp. 431–432]]）。

---

### 命题四　效应量随项目类型与交付层面而变化：近端干预产生更大效应

> [!concept-lens] 干预的层级与距离
> 干预越接近学生个体、越直接作用于学习过程，效应量越大。这与"干预对近端结果影响最大"的假说一致。

> [!claim] 干预层级与效应量差异
> Lipsey et al.（2012）发现个体/小组干预效应量（+0.40/+0.26）> 全班（+0.18）> 全校（+0.10）；教学技巧（+0.35）和教学补充（+0.36）> 课程改革（+0.13）和全校倡议（+0.11）。Slavin & Lake（2008）在小学数学中发现类似模式（[[Argument_Wolf_2020_JREE|Wolf et al., 2020, p. 432]]）。

---

### 命题五　效应量随研究者身份而变化：开发者研究产生系统性更大的效应量

> [!concept-lens] 研究者的利益关联
> 项目开发者委托或实施的研究平均效应量系统性高于独立评估，这一差异部分源于开发者更可能使用自编测量和较弱的研究设计。

> [!claim] [[Argument_Wolf_2020_JREE|Wolf et al. (2020)]]
> 发现由项目开发者委托或实施的研究平均效应量比独立评估高 0.141 个标准差（全样本），约为独立研究的 1.8 倍。详见 [[Developer Effect]]。

---

### 命题六　效应量随干预定义的模糊性而变化：同一标签可能涵盖实质不同的干预

> [!concept-lens] 术语的[[Construct Validity|构念效度]]
> 同一术语在不同研究中可能涵盖实质不同的干预实践，使效应量的跨研究聚合失去意义。

> [!claim] [[Argument_Higgins_2016_RE|Higgins (2016)]]
> [[Argument_Higgins_2016_RE|Higgins (2016, pp.37–38)]]以"[[Homework|家庭作业]]"为例：五岁儿童带书回家与父母共读、在家背单词、在"作业俱乐部"中做作业、为课堂做预习阅读、为考试背乘法表、在家完成考试课程作业——这些是否都是同一回事？如果合并所有这些研究得出"作业有效"，这并不意味着作业总是有效的。元分析聚合的不是同一种干预，而是同一标签下的不同实践。

---

## 争议与批评

> [!warning] 批判总览
> 效应量在教育研究中的使用面临来自计算口径、聚合综合和政策解释三个层面的系统批判。不同公式产生不可比的排名、逐级聚合中[[Standard Error|标准误]]混淆和错误加权扭曲结果、平均值掩盖变异性——这些批评共同质疑了将效应量作为跨研究比较尺度和教育有效性排名的合法性。详细的批判论证见 [[Critique of Effect Size]]。

---
## 应用案例

> [!info] 如何读这些案例
> 效应量案例可按用途区分：有些把效应量做成排名工具，有些显示排名被政策误用，有些说明效应量必须与实施和地方情境一起解释。

### 排名工具

> [!evidence-grid-a] 排名工具案例
> - [[EEF Teaching and Learning Toolkit]] — 以效应量转换的”额外学习月数”为核心排名格式（[[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp.120-123]]）
> - [[Visible Learning]] — 以效应量排名为核心方法论的全球教育影响项目（Hattie, 2015, p.82）

### 政策误用与来源追踪

> [!evidence-grid-a] 政策误用案例
> - [[Playing for Success]] — [[Education Endowment Foundation|EEF]] 体育参与效应量 0.80 的来源案例，与普通”体育参与”几乎不可比（[[Argument_Wrigley_2019_ERE|Wrigley & McCusker, 2019, pp.120-123]]）
> - [[Treasury Briefing on Student-Teacher Ratios]] — 政策行动者从效应量排名直接选取方案的典型案例（[[Argument_ONeill_2012_NZJES|O'Neill, 2012, pp.6-8]]）

### 实践者解释

> [!evidence-grid-a] 实践者解释案例
> - [[Argument_Ross_Morrison_2021_ROE|Ross & Morrison (2021)]] — 效应量和[[Statistical Significance|统计显著性]]必须与成本、实施、用户体验和地方语境一起解释。

---

