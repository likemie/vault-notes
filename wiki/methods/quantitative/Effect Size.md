---
title: Effect Size
aliases:
  - 效应量
summary: "比较不同干预或变量影响强度的标准化统计指标，被广泛用于元分析与证据排序，但其解释边界、聚合方式和政策用途长期存在争议"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 83
method_related_level: 6
method_related_stars: "⭐⭐⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
- effect-size
- meta-analysis
- evidence-based-education
- methodology
- statistics
related_concepts:
  - "[[Unit of Analysis]]"
  - "[[Visible Learning]]"
  - "[[Critique of Effect Size]]"
  - "[[Going Native]]"
  - "[[Academic Achievement]]"
  - "[[Developer Effect]]"
  - "[[Evaluation Research]]"
  - "[[Internal Validity]]"
  - "[[Research Purpose]]"
  - "[[Variable]]"
  - "[[Hypothesis]]"
  - "[[Formative Assessment]]"
  - "[[Homework]]"
  - "[[Grade Retention]]"
  - "[[Evidence-Based Education]]"
  - "[[Causality]]"
  - "[[Learning Gain]]"
  - "[[Educational Evidence Clearinghouses]]"
  - "[[Educational Brokerage Agency]]"
  - "[[Attrition]]"
  - "[[Preregistration]]"
  - "[[Business as Usual]]"
  - "[[Achievement and Aptitude Tests]]"
  - "[[Dependent Variable]]"
  - "[[Professional Learning Community]]"
  - "[[Learned Helplessness]]"
  - "[[Heterogeneity]]"
  - "[[Construct]]"
  - "[[External Validity]]"
  - "[[Floor and Ceiling Effects]]"
  - "[[Document]]"
  - "[[Construct Validity]]"
  - "[[Epistemology]]"
  - "[[Implementation Fidelity]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Statistical Significance]]"
  - "[[Sample Size Determination]]"
  - "[[Confidence Interval]]"
  - "[[Standard Error]]"
  - "[[Random Assignment]]"
  - "[[Power Analysis]]"
  - "[[Effect Size Conversion]]"
  - "[[Meta-meta-analysis]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Pre-test and Post-test]]"
  - "[[Covariate Adjustment]]"
  - "[[Meta-regression]]"
  - "[[Systematic Review]]"
  - "[[Experimental Research]]"
  - "[[Correlational Research]]"
related_persons:
  - "[[Gene Glass]]"
  - "[[John Hattie]]"
  - "[[Lars Qvortrup]]"
  - "[[Adrian Simpson]]"
  - "[[Jacob Cohen]]"
related_facts:
  - "[[EEF Teaching and Learning Toolkit]]"
  - "[[Australian Council for Educational Research]]"
  - "[[Education Endowment Foundation]]"
  - "[[TIMSS]]"
  - "[[Promising Practices Network]]"
  - "[[Best Evidence Encyclopedia]]"
  - "[[What Works Clearinghouse]]"
  - "[[National Center for Education Evaluation and Regional Assistance]]"
  - "[[National Pupil Database]]"
related_arguments:
  - "[[Argument_Wrigley_2019_ERE]]"
  - "[[Argument_Qvortrup_2015_Paideia]]"
  - "[[Argument_Allerup_2015_Paideia]]"
  - "[[Argument_Pampaka_2016_IJRME]]"
  - "[[Argument_Higgins_2016_ROE]]"
  - "[[Argument_Terhart_2011_JCS]]"
  - "[[Argument_Hattie_2005_ACER]]"
  - "[[Argument_Simpson_2017_JEP]]"
  - "[[Argument_Simpson_2019_ERE]]"
  - "[[Argument_Wiliam_2019_ERE]]"
  - "[[Argument_Kraft_2023_ER]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17]]"
  - "[[Argument_OConnor_2020_AJLL]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Ross_Morrison_2021_ECNUROE]]"
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
  - "[[Argument_Wolf_2020_JREE]]"
related_instruments:
  - "[[Assessment Tools for Teaching and Learning]]"
  - "[[EEF Padlock Security Rating]]"
confidence: high
status: active
created: '2026-05-01'
updated: 2026-09-18
---

## 定义

> [!def] 核心定义
> 效应量（Effect Size）是量化干预措施效果的标准化统计指标，计算方式为干预组与对照组结果差异除以标准差，旨在使不同研究的结果可跨测量工具比较。效应量是[[Meta-analysis\|元分析]]的核心[[Unit of Analysis\|分析单位]]，[[Gene Glass]] 于 1976 年将其确立为跨研究比较的标准化工具，[[John Hattie]] 的 *[[Visible Learning]]*（2009）以效应量排名教学干预使其进入全球教育政策话语。在[[EEF Teaching and Learning Toolkit]]中，效应量被进一步转换为"额外学习月数"（[[Argument_Wrigley_2019_ERE\|Wrigley & McCusker, 2019, p. 118]]）。

> [!concept-lens] 概念透镜
> - **含义** 效应量通过除以标准差消除测量单位，回答"干预产生了多大差异"，而非仅回答"差异是否显著"。[[Lars Qvortrup]]（2015）强调其"相对效果"功能——可比较不同研究之间干预组与控制组的相对变化（[[Argument_Qvortrup_2015_Paideia\|Qvortrup, 2015, p.27]]）。
> - **用途** 为[[Meta-analysis\|元分析]]提供可合并的通用尺度，为实践者和政策制定者提供关于"什么有效"的量化总结。
> - **边界** 效应量不直接说明效果的实质教育意义——同一个 d 值可能对应表层知识记忆或深层概念理解。[[Adrian Simpson]]（2017, 2018, 2019）进一步论证效应量实际测量的是试验清晰度（experimental clarity）而非干预有效性，详见 [[Critique of Effect Size]]。

> [!boundary] 概念边界
> - **不等于教育有效性** 效应量反映的是试验设计的信噪比，大 d 表示差异在统计上清晰，不表示差异大、重要或具有教育显著性。
> - **不等于因果效应** 效应量本身不区分相关与因果。其因果含义完全取决于产生它的研究设计。
> - **不替代原始单位** 标准化消除了原始测量单位，便于跨研究比较，但也抹除了效果的实际教育意义——知道提高了 0.3 SD 并不能直接知道学生多学会了几个单词。

---

## 概念辨析

> [!contrast-table] 与相关概念的区别
> - **vs [[Statistical Significance]]** — 效应量测量效果的大小，统计显著性测量效果是否可能仅由随机因素产生。统计显著性依赖于效应量和[[Sample Size Determination\|样本量]]的乘积：$t = d\sqrt{n}$([[Argument_Allerup_2015_Paideia\|Allerup, 2015, p.45]])。在 n=25 的双侧检验中，临界 $t=2.060$ 对应 $d \approx 0.412$，刚好接近《[[Visible Learning\|可见的学习]]》的 0.40 阈值，这意味着 0.40 在特定样本量下才与 p≈0.05 相连，并非脱离样本量的普遍边界。
> - **vs [[Confidence Interval]]** — 效应量给出点估计，置信区间呈现该估计的误差范围。没有置信区间或[[Standard Error\|标准误]]时，相邻效应量排名无法判断是否真的不同([[Argument_Allerup_2015_Paideia\|Allerup, 2015, pp.47–48]])。Hattie 的效应量排名仅给 d 的点估计，未系统报告置信区间或[[Standard Error\|标准误]]，也未进行相邻排名之间的显著性检验。
> - **vs 原始分数差异（Raw Score Difference）** — 原始分数差异保留了原始测量单位，效应量通过除以标准差消除了单位——这使跨研究比较成为可能，但也抹除了效果的实际教育意义。
> - **vs 意向处理分析效应** — 意向处理分析按原始[[Random Assignment\|随机分配]]分析（无论实际接受与否），反映干预可获得性而非实际接受效果；效应量本身不区分这两种估计，但所基于的研究设计决定了其政策含义([[Argument_Pampaka_2016_IJRME\|Pampaka et al., 2016, p.233]])。
> - **vs 最小可检测效应量** — 效应量是事后度量（干预实际产生了多大效果），最小可检测效应量是事前设计参数（研究能够检测到多大效果），详见下方[[#最小可检测效应量]]。

---

## 概念演变

> [!dev-timeline] 效应量的概念演变
> - **1964** — Benjamin Bloom 在 Stability and Change in Human Characteristics 中呈现了相关系数的聚合图表，其"两个标准差问题"（寻找与一对一辅导同样有效的小组教学方法）以标准差单位表述，为效应量在教育研究中的使用提供了早期范例([[Argument_Higgins_2016_ROE\|Higgins, 2016, p.37]])。
> - **1966** — Robert Rosenthal 出版 Experimenter Effects in Behavioral Research，包含大量标准化平均差异的计算并跨领域比较。Glass 本人承认 Rosenthal 发展了效应量的基础度量。
> - **1969** — [[Jacob Cohen]] 出版 [[Power Analysis\|statistical power analysis]] for the Behavioral Sciences 第 1 版，引入 Cohen's d 作为标准化均值差的度量。
> - **1976** — [[Gene Glass]] 提出[[Meta-analysis\|元分析]]概念，将效应量作为跨研究比较的标准化工具([[Argument_Higgins_2016_ROE\|Higgins, 2016, pp.36–37]])。
> - **1980** — Cooper and Rosenthal 的实证检验表明，[[Meta-analysis\|元分析]]比传统叙事综述更不容易低估证据([[Argument_Higgins_2016_ROE\|Higgins, 2016, p.32]])。
> - **1988** — Cohen 出版 Statistical Power Analysis 第 2 版，以身高类比等直观方式解释效应量的实质含义([[Argument_Terhart_2011_JCS\|Terhart, 2011, p.427]])。
> - **2005** — [[John Hattie\|约翰·哈蒂]]（[[John Hattie]]）在 [[Australian Council for Educational Research\|ACER]] 会议报告中基于 100 余项元分析与 50 余万个效应量确立 $d = 0.40$ 为教学干预的“关节点（hinge point）”，提出批判教育界将门槛定得过低的“零门槛谬误”，并依托[[Assessment Tools for Teaching and Learning\|教学与学习评估工具]]（[[Assessment Tools for Teaching and Learning\|asTTle]]）推动效应量在中小学校本评价与教师教学改进中的[[Going Native\|本土化]]应用（[[Argument_Hattie_2005_ACER\|Hattie, 2005, pp. 15–17]]）。
> - **2009** — [[John Hattie]] 出版《[[Visible Learning\|可见的学习]]》，综合 800 多项元分析和 50,000 多项研究，以效应量排名各类教育干预，使效应量概念进入全球教育政策和实践话语。
> - **2014** — [[EEF Teaching and Learning Toolkit]] 以[[Effect Size Conversion\|效应量转换]]为"额外学习月数"的格式传播教育干预证据。
> - **2017 至 2018** — Simpson 发表系统批判，论证效应量测量的是试验灵敏度而非干预有效性（[[Argument_Simpson_2017_JEP\|Simpson, 2017]], 2018）。
> - **2019** — Simpson 用"教一个匈牙利单词"思想实验展示同一干预可因测试设计产生 0 到无穷大的效应量；Wrigley & McCusker 通过 [[Education Endowment Foundation\|EEF]] Toolkit 体育参与案例展示[[Meta-meta-analysis\|元-元分析]]层面的三级失真；Wiliam 提出 11 点元分析评估清单([[Argument_Simpson_2019_ERE\|Simpson, 2019]]; [[Argument_Wrigley_2019_ERE\|Wrigley & McCusker, 2019]]; [[Argument_Wiliam_2019_ERE\|Wiliam, 2019]])。
> - **2020 至 2023** — Kraft 以教育[[Randomised Controlled Trials\|随机对照试验]]中标准化[[Academic Achievement\|学业成绩]]结果的经验分布替代 Cohen 基准，并强调 36% 的效应量小于 0.05 这一"失败频率"应成为解释政策相关性的核心参照([[Argument_Kraft_2023_ER\|Kraft, 2023, pp.183–184]])。

---

## 核心要素

> [!feature] 效应量的核心要素
> - **技术定义与计算** 标准化均值差公式、与显著性检验和统计功效的关系、最小可检测效应量的设计含义。
> - **解释框架** Cohen 的经验法则、Hattie 的影响气压计与关节点（$d=0.40$）、Terhart 的实质解释、Kraft 的教育 [[Randomised Controlled Trials\|RCT]] 经验基准、清算中心的政策阈值。
> - **效应量变异的系统性来源** 测量类型、[[Sample Size Determination\|样本量]]、研究设计、项目类型、[[Developer Effect\|开发者效应]]和干预定义模糊性六类因素如何系统性地改变效应量。

---

## 解释框架

### 技术定义与计算

> [!info] Fitz-Gibbon 的早期推动（1985）
> Fitz-Gibbon（1985, p. 45）在[[Meta-analysis\|元分析]]发展早期即主张以效应量替代[[Statistical Significance\|统计显著性]]作为[[Evaluation Research\|评估研究]]的主要指标，将统计显著性重新定位为"[[Internal Validity\|内部效度]]众多可能威胁中的一个"——效应大小是否满足[[Research Purpose\|研究目的]]，而非是否跨过了显著性水平的任意截断点（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch17\|Cohen et al., 2011, Ch17, pp.339–340]]）。

> [!formula-step] 标准化均值差（Cohen's d）
> $$d = \frac{M_{\text{干预组}} - M_{\text{对照组}}}{SD_{pooled}}$$
>
> **这个公式在做什么** 用干预组与对照组（或[[Pre-test and Post-test\|后测]]与前测）的平均得分之差，除以两组的合并标准差（$SD_{pooled}$），产出无量纲的标准化效应度量。
>
> **符号说明**
> - $M_{\text{干预组}}, M_{\text{对照组}}$ 分别为实验组与对照组在结果测验上的样本均值。
> - $SD_{pooled}$ 为两组样本的合并标准差（$\sqrt{\frac{(n_1-1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2}}$）。
>
> **读法与数学直觉** $d = 0.5$ 表示实验组均值比控制组高出半个标准差。$d = 0$ 表示两组无差异，$d$ 为负表示实验组表现更差。标准化消除了不同测量工具的量表差异，使跨研究比较成为可能（[[Argument_Wrigley_2019_ERE\|Wrigley & McCusker, 2019, p. 118]]）。
>
> **与显著性检验的关系** 若比较干预前后两个分布，均值差 $\mu_1 - \mu_2$ 只有放到标准差 $\sigma$ 的尺度上才有意义。$d$ 本身不是可直接判定[[Statistical Significance\|统计显著性]]的统计量；只有乘以 $\sqrt{n}$，得到 $t = d\sqrt{n}$，才接近用于检验 $\mu_1 = \mu_2$ 的 $t$ 统计量（[[Argument_Allerup_2015_Paideia\|Allerup, 2015, pp.42–43]]）。
>
> **统计前提** $d$ 的直观解释依赖于三个前提：（1）前后分布近似对称且接近正态；（2）两个分布的标准差相同，均值差才可解释为简单位移；（3）若分布右偏或左偏，均值并不在分布中心。极端情况下，若基础分布类似柯西分布（Cauchy distribution），均值和方差本身不稳定，$d$ 的计算基础会崩塌（[[Argument_Allerup_2015_Paideia\|Allerup, 2015, pp.45–49]]）。
>
> **第三[[Variable\|变量]]影响** 边际分析与多[[Variable\|变量]]控制会显著改变 $d$。[[TIMSS]] 2011 丹麦四年级数学中，教师学科专业资格的未控制效应量约 0.15，控制学生社会经济背景后降至 0.08 且不再显著——说明单个 $d$ 不能脱离第三变量独立解释（参见 [[Covariate Adjustment]]）。

---

### 效应量族系与指标转换

> [!proc] 核心效应量族系与转换路径
> 在元分析与证据合成中，不同研究设计报告的效应指标可通过标准数学公式统一换算：
> 1. **两组均值差族系（$d$ 与 $g$）** 实验组与对照组比较，小样本下通过 $g = J(df) \times d$ 进行小样本无偏校正。
> 2. **关联与相关族系（$r$）** 连续变量线性关联，平衡样本下通过 $r = \frac{d}{\sqrt{d^2 + 4}}$ 与 $d = \frac{2r}{\sqrt{1 - r^2}}$ 实现与 $d$ 的相互转换。
> 3. **分类与概率比族系（$OR$）** 二分类变量比值比通过 $d \approx \frac{\ln(OR)}{1.814}$ 转换为连续均值差。
> 4. **正态化与方差稳定化（Fisher's $z$）** 元分析在统计加权前需通过 $z = \operatorname{arctanh}(r)$ 稳定方差，合并后再逆转换为 $r$ 呈现。
>
> 完整数学推导、组间样本比率校正公式与数值对照矩阵见方法条目 **[[Effect Size Conversion\|效应量转换]]**。

---

### Cohen 的直观解释框架（1988）

> [!info] Cohen 的经验法则
> Cohen（1988）使用人体身高提供直观类比：$d = 1.0$ 表示 160cm 和 183cm 之间的差异([[Argument_Terhart_2011_JCS\|Terhart, 2011, p.427]])。Cohen 同时定义了经验法则：
>
> | 效应量 | 标签 | 含义（[[Hypothesis\|假设]]正态分布） |
> |---|---|---|
> | $d = 0.2$ | 小 | 实验组均值高于对照组约 58% |
> | $d = 0.5$ | 中 | 实验组均值高于对照组约 69% |
> | $d = 0.8$ | 大 | 实验组均值高于对照组约 79% |

> [!warning] Cohen 框架的使用边界
> Cohen 本人强调这些标签是操作性的经验法则，不应被机械套用。[[Argument_Kraft_2023_ER\|Kraft (2023)]]进一步论证教育[[Randomised Controlled Trials\|随机对照试验]]的实际效应量分布远低于 Cohen 的锚点（详见下方[[#Kraft 的教育随机对照试验经验基准]]）。

---

### Hattie 的关节点、影响气压计与“零门槛谬误”

> [!info] Hattie 的经验分布与关节点（Hinge Point）
> [[John Hattie\|约翰·哈蒂]]（John Hattie）在 2005 年 [[Australian Council for Educational Research\|ACER]] 大会报告与后续专著中，基于 100 多项一阶元分析、50 余万个效应量（涵盖 50,000 余项原始研究与数千万学生）绘制了教育创新的效应量正态分布曲线（$M = 0.40, SD \approx 0.20$），并确立 $d = 0.40$ 为教学有效性的关节点（Hinge Point，[[Argument_Hattie_2005_ACER\|Hattie, 2005, pp. 15–16]]；[[Argument_OConnor_2020_AJLL\|O'Connor, 2020, p. 142]]）。他将效应量分布划分为四个实质区域（[[Argument_Hattie_2005_ACER\|Hattie, 2005, p. 16]]；[[Argument_Terhart_2011_JCS\|Terhart, 2011, pp. 427–428]]）：
>
> - **期望效应区（$d > 0.40$）** 超越常规教学平均增长的优质创新，如[[Formative Assessment\|形成性评价]]/反馈 $d = 0.73$、互惠教学 $d = 0.86$、自我报告成绩 $d = 1.44$。
> - **教师效应区（$d = 0.15$–$0.40$）** 普通教师在常规课堂中一学年达成的平均教学增益（如[[Homework\|家庭作业]] $d = 0.29$）。
> - **发展效应区（$d = 0.0$–$0.15$）** 学生即使不上学、仅凭自然成熟与日常生活也能发生的发展增益（约每年 0.10–0.15 SD）。
> - **负面效应区（$d < 0$）** 损害学生学习的逆向实践，如[[Grade Retention\|留级]] $d = -0.16$、过度看电视 $d = -0.18$。

> [!danger] 批判“零门槛谬误”（The Zero Barrier Fallacy）
> [[Argument_Hattie_2005_ACER\|Hattie (2005, pp. 15–16)]]尖锐指出，传统教育研究与政策常犯“把门槛设在零点（Setting the bar at zero）”的严重错误：
> 1. **90%–95% 的创新天然有效** 实证数据显示，教育领域 90% 到 95% 的干预效应量都大于 0（$d > 0$），几乎所有政策和创新宣称“统计显著有效（$p < .05$）”都能轻易过关。
> 2. **真实基线是 $d = 0.40$ 而非 $d = 0$** 任何干预只要未能超过一学年常规教学与自然成熟的基准线（$d = 0.40$），实质上就是低于平均水准或在浪费教学时间。因此，[[Evidence-Based Education\|循证教育]]决策必须以 $d = 0.40$ 作为判断干预是否产生实质净增值的最低关节点。

> [!tip] 课堂层面的效应量测算与校本应用
> 为使效应量走出象牙塔并直接赋能一线教师，Hattie 团队在新西兰开发了“[[Assessment Tools for Teaching and Learning\|教学与学习评估工具]]”（[[Assessment Tools for Teaching and Learning\|asTTle]]）软件系统。教师只需录入班级前后测数据，系统即可自动计算班级和个体层面的效应量（$d = \frac{M_{\text{后测}} - M_{\text{前测}}}{SD_{\text{合并}}}$），并对照全国常模生成雷达图与进阶路径。这使教师能将效应量作为自我诊断教学成效的常态化镜子，而非外在的惩罚性问责工具（[[Argument_Hattie_2005_ACER\|Hattie, 2005, pp. 16–17]]）。

---

### [[Argument_Terhart_2011_JCS|Terhart (2011)]] 的详细解释

> [!info] 效应量的实质含义
> [[Argument_Terhart_2011_JCS\|Terhart (2011, p.427)]]对效应量的技术含义提供了补充说明：
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
> Terhart 同时补充了关键警告：效应量不表示[[Causality\|因果关系]]（p.427）。

---

### Kraft 的教育随机对照试验经验基准

> [!info] Kraft 的经验基准
> [[Argument_Kraft_2023_ER\|Kraft (2023)]]主张以教育干预随机对照试验中标准化[[Academic Achievement\|学业成就]]效应量的经验分布替代 Cohen 的 $0.2/0.5/0.8$ 通用锚点。他在 3,426 个效应量中发现分布相当稳定：30 百分位 0.02、50 百分位 0.10、70 百分位 0.21（[[Argument_Kraft_2023_ER\|Kraft, 2023, pp.183–184]]）。
>
> Kraft 的基准同时考虑年度[[Learning Gain\|学习增益]]、教师与学校效应等经验参照点，聚焦"正向效应量的政策相关性"，因此承认这些基准具有主观性——更合适的做法是随新增研究检验既有基准在分布中的相对排名（[[Argument_Kraft_2023_ER\|Kraft, 2023, pp.185-186]]）。Kraft and Simpson 的分歧在于：Simpson（2021）认为跨研究效应量因设计、测量、样本差异而本质不可比；Kraft 则认为完全禁止比较会削弱证据本位政策，只要承认噪声和限制，仍可从因果研究中获得粗略参照，但同意按"联盟表"排名是可疑的（[[Argument_Kraft_2023_ER\|Kraft, 2023, p.184]]）。

---

### 清算中心的最低效应阈值

> [!info] 清算中心的最低效应阈值
> [[Argument_Wadhwa_2024_RER\|Wadhwa et al. (2024)]]显示，部分[[Educational Evidence Clearinghouses\|教育证据清算中心]]把最低效应量阈值直接写入项目评级规则：[[Promising Practices Network]] 的最高评级要求至少 0.25 个标准差的差异，[[Best Evidence Encyclopedia]] 要求至少 0.20 个标准差的影响。相比之下，[[What Works Clearinghouse]] 的最高项目效果判断要求统计显著正向效果，但不要求平均效果达到特定大小([[Argument_Wadhwa_2024_RER\|Wadhwa et al., 2024, pp.12–15]])。这说明效应量不仅是研究报告中的统计指标，也会成为[[Educational Brokerage Agency\|证据中介机构]]划定"推荐/有希望/不推荐"边界的制度阈值。

---

### 实践者解释中的效应量与挂锁安全评级

> [!info] 实践者解释中的效应量与安全锁互补机制
> 在学校采购和项目评价中，教育产品消费者并不总能理解效应量和统计显著性等有效性指标，也常觉得正式证据来源缺少实施要求、使用满意度、成本和情境信息。效应量因此不是“读者看到数字就能行动”的指标，而需要和项目目标、使用强度、对照条件、测量工具和地方需求一起解释([[Argument_Ross_Morrison_2021_ECNUROE\|Ross & Morrison, 2021, pp.120-121]])。
>
> 针对单一指标沟通的局限，英国[[Education Endowment Foundation\|教育捐赠基金会]]（EEF）在《[[EEF Teaching and Learning Toolkit\|教学与学习工具包]]》与官方评估报告中，建立了**效应量（额外学习月数）与[[EEF Padlock Security Rating\|挂锁安全评级]]（Padlock Rating）**的二元互补机制（The EEF, 2019c；[[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill, 2021, p. 57]]）。实践者不能仅凭孤立的效应量大小做决策：一个看似巨大的效应量（如 $d = 0.50$）若仅获得 1 把锁，说明其面临严重的[[Sample Size Determination\|样本量]]不足、高[[Attrition\|流失]]率或未[[Preregistration\|预注册]]等偏倚风险；反之，一个微弱的效应量（如 $d = 0.06$）若拥有 4 或 5 把安全锁（高统计功效、低流失、预注册分析与独立实施），则反映了在真实[[Business as Usual\|常态教学]]基线下的高确定性因果证据。这种将“效应量大小”与“因果证据安全性”解耦并列的双轨呈现，有效避免了决策者对孤立统计量或 $p < 0.05$ 门槛的机械迷信（Wasserstein et al., 2019）。

> [!example]
> 一个补充性教育技术项目可能只在每周少量课堂时间中使用。若它在标准化[[Achievement and Aptitude Tests\|成就测验]]上的效应量很小，这不必然说明项目无价值；它可能主要改善学生动机、释放教师个别辅导时间或增加技术接入公平。反过来，一个较大的效应量若来自低质量对照组，也不能直接说明项目在本地学区一定值得采购([[Argument_Ross_Morrison_2021_ECNUROE\|Ross & Morrison, 2021, pp.110-112]])。

---

### 效应量与统计功效

> [!math-principle] 效应量与统计功效
> 效应量与统计功效存在直接的函数关系。对于固定的[[Sample Size Determination\|样本量]]、显著性水平和统计检验，统计功效和效应量是同一个东西的连续变换([[Argument_Simpson_2019_ERE\|Simpson, 2019, p. 103, Figure 1]])。这意味着：
> - 更大的效应量 → 更高的统计功效 → 更容易检测到"显著"结果
> - 但这不意味着干预更有效，只意味着试验设计使组间差异更清晰可见

---

### 最小可检测效应量

> [!info] 最小可检测效应量
> [[Argument_Pampaka_2016_IJRME\|Pampaka et al. (2016, p.233)]]介绍了与效应量密切相关的另一个概念：在给定统计功效下，研究设计能够检测到的最小效应量。最小可检测效应量是研究精度的度量：
>
> - 最小可检测效应量是"近期争论的焦点，因为其主要由经验法则决定"，缺乏系统性的精度标准
> - 最小可检测效应量越小，研究精度越高；精度提高意味着可检测到更小的干预效果
> - 与效应量的区别：效应量衡量干预"实际产生了多大的效果"（事后），最小可检测效应量描述研究"能够检测到多大的效果"（事前设计参数）

---

## 实证数据

> [!effect-table]- 原始研究结果与干预效应量
> <span class="concept-effect-table-marker" aria-hidden="true"></span>
>
> | 研究 | 比较或干预 | [[Dependent Variable\|结果变量]] | 分析样本 | 组别统计 | 效应量 | 显著性或不确定性 | 设计与解释边界 |
> |---|---|---|---|---|---|---|---|
> | [[Argument_Hattie_2005_ACER\|Hattie (2005)]]（引述 Timperley, 2004, 2005） | 新西兰 7 所极低 SES（Decile 1）小学基于读写评估数据的教师[[Professional Learning Community\|专业学习共同体]]干预 | 阅读理解与读写达标成绩 | 7 所小学全体低年级学生（毛利与太平洋岛裔占多数） | 干预前读写达标率严重落后全国常模；干预后两年年均进步达全国预期 2–3 倍 | $d > 0.80$ | 统计显著 | 准实验校本追踪；证实校本证据反馈可打破教师赤字归因与[[Learned Helplessness\|习得性无助]] |
> | [[Argument_Wolf_2020_JREE\|Wolf et al. (2020)]] | [[What Works Clearinghouse\|WWC]] 数据库中开发者研究 vs 独立[[Evaluation Research\|评估研究]] | [[Academic Achievement\|学业成就]]效应量 | 755 个效应量（169 项研究） | 开发者研究未调均值 0.309；独立评估未调均值 0.168 | $ES_{\text{差异}} = +0.141$ | 95% PI 独立 $[-0.45, +0.79]$；开发者 $[-0.31, +0.93]$ | [[Meta-regression\|元回归]]多层模型；证实开发者利益冲突与自编测验系统性推高效应量 |
> | [[Argument_Ross_Morrison_2021_ECNUROE\|Ross & Morrison (2021)]]（引述 Lortie-Forgues & Inglis, 2019） | 英美大型现场 [[Randomised Controlled Trials\|RCT]]（[[Education Endowment Foundation\|EEF]] 82 项 + [[National Center for Education Evaluation and Regional Assistance\|NCEE]] 59 项） | 标准化统考学业成就 | 141 项试验（涵盖 1,222,024 名学生） | 77% 的试验结果在统计上不显著 | 平均 $d = 0.06$ | 平均 95% CI $[-0.09, +0.21]$ | 独立大规模现场 RCT；证实真实学校生态下微弱效应量属于常态 |

> [!ma-table]- 一阶与[[Meta-meta-analysis\|二阶元分析]]总体结果
> <span class="concept-meta-analysis-table-marker" aria-hidden="true"></span>
>
> | [[Meta-analysis\|元分析]] | 当前概念角色与总体结果 | 证据规模 $M$ / $E$ / $k$ / $N$ | 效应指标与模型 | 汇总效应与 95% CI | [[Heterogeneity\|异质性]]与 95% PI | 关键解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Hattie_2005_ACER\|Hattie (2005)]] | 全球教育创新与教学干预总体综合效应 | $M > 100$；$E > 500,000$；$k > 50,000$；$N > 20,000,000$ | Cohen's $d$ / 经验正态分布 | 总体均值 $d = 0.40$ | 正态分布 $SD \approx 0.20$；90%–95% 效应量为正 | 宏观二阶元分析概括；确立 $d=0.40$ 关节点，但包含不同研究质量混合 |
> | [[Argument_Kraft_2023_ER\|Kraft (2023)]] | 美国 K-12 教育干预因果试验经验分布 | $k = 3,426$ 个效应量（来自因果 RCT 研究） | 标准化均差（SMD） | 中位数 $d = 0.10$；30 百分位 0.02；70 百分位 0.21 | 36% 的效应量 $< 0.05$ | 严格限定于因果评估与标准化[[Achievement and Aptitude Tests\|成就测验]]；剔除开发者自编测验偏倚 |

---

## 围绕概念形成的命题

> [!concept-lens] 效应量变异的系统性来源
> 多项[[Meta-analysis\|元分析]]识别了独立于干预实际有效性的方法论因素，它们系统性地与更大或更小的效应量相关联（[[Argument_Wolf_2020_JREE\|Wolf et al., 2020, pp. 430–432]]）。以下六条命题分别对应六类系统性偏差来源。

---

### 命题一　效应量随测量类型而变化：自编测量产生系统性更大的效应量

> [!concept-lens] 测量工具的敏感性差异
> 不同结果测量工具对干预效果的敏感度不同。研究者或开发者自编的测量往往比独立标准化测量更贴近干预内容，因此产生更大的效应量——这一差异并非反映干预真实效果的变化，而是测量工具与被测[[Construct\|构念]]的对齐程度差异。

> [!claim] [[Argument_Wolf_2020_JREE\|Wolf et al. (2020)]]
> Cheung & Slavin（2016）、de Boer, Donker & van der Werf（2014）、Li & Ma（2010）等多个[[Meta-analysis\|元分析]]发现自编测量产生的效应量比独立测量高 **0.20–0.29** 标准差。de Boer et al.（2014）发现其综述中 180 个测量中约三分之二是研究者或开发者自编的（[[Argument_Wolf_2020_JREE\|Wolf et al., 2020, p. 431]]）。例：同一数学干预使用项目团队自编测试时效应量可能为 +0.45，使用州标准化测试时可能仅为 +0.20。
> [!claim] [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]]
> **独立高[[External Validity\|外部效度]]测验与行政统考对接规程** 针对自编测量系统性虚增效应量的顽疾，英国[[Education Endowment Foundation\|教育捐赠基金会]]（EEF）早在 2012 年即出台严格的《评估测验选用指南》（The EEF, 2012b；Edovald & Nevill, 2021, p. 54）。指南硬性规定：试验的主要学业产出指标严禁采用开发者或评估团队自编的非标准化测验，必须选用具有广泛[[External Validity\|外部效度]]、与英格兰国家关键考试（GCSE 或[[National Pupil Database\|国家学生数据库]]（NPD）核心统考成绩）高度相关的全国商业标准化测验或官方行政统考，并严格排查[[Floor and Ceiling Effects\|天花板效应]]与地板效应。这一制度安排从源头上锁死了通过定制贴合干预内容的近端测验来人为推高效应量的投机空间。

---

### 命题二　效应量随样本量增大而系统性减小

> [!concept-lens] [[Sample Size Determination\|样本量]]与统计功效的关联
> 效应量与样本量之间存在负向、准对数关系。小规模研究更容易控制实施质量且需要较大效应量才能达到统计显著，导致小样本研究的效应量系统性偏高。

> [!claim] Slavin & Smith (2009)
> 效应量与样本量的经验关系（引自 [[Argument_Wolf_2020_JREE\|Wolf et al., 2020, p. 431]]）：
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

> Kulik & Fletcher（2016）在智能辅导[[Systematic Review\|系统综述]]中报告了类似模式：<80 人 +0.78，81–250 人 +0.53，>250 人 +0.30。两种理论解释：小规模研究更容易控制实施质量；小规模研究需要非常大的效应量才能达到统计显著，只有效应量足够大的小研究才被发表（[[Argument_Wolf_2020_JREE\|Wolf et al., 2020, p. 431]]）。

---

### 命题三　效应量随研究设计类型而变化：实验与非实验设计的差异证据不一

> [!concept-lens] 研究设计的[[Causality\|因果推断]]强度
> 研究设计（实验 vs 非实验）对效应量的影响方向在[[Document\|文献]]中并无一致结论，需要区分具体领域和干预类型。

> [!claim] 研究设计对效应量的影响
> Cheung & Slavin（2016）在 645 项研究的综合元分析中发现非实验设计平均效应量 +0.23 vs 实验设计 +0.16；Wilson, Gottfredson & Najaka（2001）发现非[[Experimental Research\|实验研究]]效应量高 0.17 个标准差。但 Cook（2002）、de Boer et al.（2014）、Gersten et al.（2009）、Wilson & Lipsey（2001）均未发现实验与非实验设计间效应量的显著差异（[[Argument_Wolf_2020_JREE\|Wolf et al., 2020, pp. 431–432]]）。

---

### 命题四　效应量随项目类型与交付层面而变化：近端干预产生更大效应

> [!concept-lens] 干预的层级与距离
> 干预越接近学生个体、越直接作用于学习过程，效应量越大。这与"干预对近端结果影响最大"的假说一致。

> [!claim] 干预层级与效应量差异
> Lipsey et al.（2012）发现个体/小组干预效应量（+0.40/+0.26）> 全班（+0.18）> 全校（+0.10）；教学技巧（+0.35）和教学补充（+0.36）> 课程改革（+0.13）和全校倡议（+0.11）。Slavin & Lake（2008）在小学数学中发现类似模式（[[Argument_Wolf_2020_JREE\|Wolf et al., 2020, p. 432]]）。

---

### 命题五　效应量随研究者身份而变化：开发者研究产生系统性更大的效应量

> [!concept-lens] 研究者的利益关联
> 项目开发者委托或实施的研究平均效应量系统性高于独立评估，这一差异部分源于开发者更可能使用自编测量和较弱的研究设计。

> [!claim] [[Argument_Wolf_2020_JREE\|Wolf et al. (2020)]]
> 发现由项目开发者委托或实施的研究平均效应量比独立评估高 0.141 个标准差（全样本），约为独立研究的 1.8 倍。详见 [[Developer Effect]]。

---

### 命题六　效应量随干预定义的模糊性而变化：同一标签可能涵盖实质不同的干预

> [!concept-lens] 术语的[[Construct Validity\|构念效度]]
> 同一术语在不同研究中可能涵盖实质不同的干预实践，使效应量的跨研究聚合失去意义。

> [!claim] [[Argument_Higgins_2016_ROE\|Higgins (2016)]]
> [[Argument_Higgins_2016_ROE\|Higgins (2016, pp.37–38)]]以"[[Homework\|家庭作业]]"为例：五岁儿童带书回家与父母共读、在家背单词、在"作业俱乐部"中做作业、为课堂做预习阅读、为考试背乘法表、在家完成考试课程作业——这些是否都是同一回事？如果合并所有这些研究得出"作业有效"，这并不意味着作业总是有效的。元分析聚合的不是同一种干预，而是同一标签下的不同实践。

---

## 争议与批评

> [!warning] 批判总览
> 效应量在教育研究中的使用面临来自计算口径、聚合综合和政策解释三个层面的系统批判。不同公式产生不可比的排名、逐级聚合中[[Standard Error\|标准误]]混淆和错误加权扭曲结果、平均值掩盖变异性——这些批评共同质疑了将效应量作为跨研究比较尺度和教育有效性排名的合法性。详细的批判论证见 [[Critique of Effect Size]]。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Effect Size Conversion]] | 补充方法 | 解决跨研究设计与不同统计量（$d, g, r, OR, z$）之间的标准化数学换算。 |
> | [[Meta-analysis]] | 宏观方法 | 效应量是元分析合成证据与估计合并效应量的核心统计单位。 |
> | [[Power Analysis]] | 前置方法 | 统计功效与最小可检测效应量构成试验[[Sample Size Determination\|样本量]]规划与检验精度的前置基础。 |
> | [[Critique of Effect Size]] | 理论批评 | 深度剖析效应量跨研究聚合与政策排名中的方法学与[[Epistemology\|认识论]]争议。 |
> | [[Visible Learning]] | 理论框架 | Hattie 采用效应量对各类教育与教学干预进行全球综合与关节点划定。 |
> | [[EEF Teaching and Learning Toolkit]] | 政策工具 | 将效应量转换为“额外学习月数”并结合[[EEF Padlock Security Rating\|挂锁安全评级]]的循证决策工具。 |

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research\|相关研究]]索引
> - [[Argument_Hattie_2005_ACER\|Hattie (2005)]] — 提倡将效应量直接作为学校与教师评估教学成效的通用工具，基于 100 余项[[Meta-analysis\|元分析]]确立 $d=0.40$ 为判断干预增值的关节点基准，并揭示“零门槛谬误”。
> - [[Argument_Kraft_2023_ER\|Kraft (2023)]] — 基于 3,426 个教育 [[Randomised Controlled Trials\|RCT]] 效应量构建经验分布，提出以实证分布与失败频率替代传统 Cohen 经验法则。
> - [[Argument_Wolf_2020_JREE\|Wolf et al. (2020)]] — 运用[[Meta-regression\|元回归分析]] 755 个效应量，实证量化了[[Developer Effect\|开发者效应]]与测量工具紧密性对效应量的系统性推升。
> - [[Argument_Wrigley_2019_ERE\|Wrigley & McCusker (2019)]] — 追踪 [[Education Endowment Foundation\|EEF]] 工具包中效应量转化为月数时的逐级失真案例。
> - [[Argument_Ross_Morrison_2021_ECNUROE\|Ross & Morrison (2021)]] — 论证效应量与[[Statistical Significance\|统计显著性]]必须与成本、[[Implementation Fidelity\|实施保真度]]及地方语境综合解释。
> - [[Argument_Edovald_Nevill_2021_ECNUROE\|Edovald & Nevill (2021)]] — 论述在大规模因果评估中确立标准化测验首要地位与排查[[Floor and Ceiling Effects\|天花板效应]]的规程。
