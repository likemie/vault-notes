---
title: Regression Discontinuity Design
aliases:
  - 断点回归设计
  - 断点回归
  - RDD
  - regression discontinuity
  - Sharp RDD
  - Fuzzy RDD
  - 清晰断点回归
  - 模糊断点回归
summary: "基于连续驱动变量在特定阈值处的刚性或概率性分配规则识别局部平均处理效应（LATE）的准实验方法，在WWC中被赋予与RCT同等的无保留达标最高因果审查资质。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 32
method_related_level: 4
method_related_stars: "⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/regression-discontinuity
  - method/quasi-experimental-design
  - method/quantitative
  - causal-inference
  - econometrics
related_concepts:
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Hypothesis]]"
  - "[[Dependent Variable]]"
  - "[[Academic Achievement]]"
  - "[[Internal Validity]]"
  - "[[Construct]]"
  - "[[Counterfactual]]"
  - "[[Epistemology]]"
  - "[[Postpositivism]]"
  - "[[Paradigm]]"
  - "[[Pre-test and Post-test]]"
  - "[[External Validity]]"
  - "[[Standard Error]]"
  - "[[Falsification]]"
  - "[[Manipulation Check]]"
  - "[[Homework]]"
  - "[[Sample Size Determination]]"
  - "[[Intelligent Tutoring Systems]]"
related_theories:
  - "[[Campbellian Validity Framework]]"
  - "[[Luhmann's Systems Theory]]"
related_methods:
  - "[[Random Assignment]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Time Series Design]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[What Works Clearinghouse]]"
  - "[[Gaokao]]"
  - "[[Home Visiting Evidence of Effectiveness]]"
  - "[[Partnership Schools Kura Hourua]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Wadhwa_2024_RER]]"
confidence: high
status: active
created: 2026-08-22
updated: 2026-08-22
---

# Regression Discontinuity Design

---

## 定义

> [!def] 方法定义
> **断点回归设计（Regression Discontinuity Design, RDD）** 最早由 Donald L. Thistlethwaite 与 Donald T. Campbell 于 1960 年创立，是指依据某个连续**驱动[[Variable|变量]]（Running Variable / Forcing Variable）**在预设**截断阈值（Cut-off Point）**处的分配规则，将受试对象严格或概率性划分为干预组与对照组，进而在阈值邻域内识别干预因果效应的准实验方法([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, pp. 320–324]]; [[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, p. 1327]])。
>
> 其核心[[Causality|因果推断]]逻辑建立在**局域[[Random Assignment|随机化]][[Hypothesis|假设]]（Local Randomization Assumption）**之上：在紧邻阈值的极小带宽（Bandwidth）范围内，个体的潜能、动机与家庭背景等不可测混杂特征均是平滑连续分布的；唯独干预分配状态在阈值处发生非连续阶跃。因此，阈值两侧[[Dependent Variable|结果变量]]的垂直跳跃量可直接无偏地归因为干预的**局部平均处理效应（Local Average Treatment Effect, LATE）**。在美国教育部 [[What Works Clearinghouse|WWC]] 因果设计审查体系中，符合质量标准的 RDD 被赋予与 [[Randomised Controlled Trials|RCT]] 同等的一级最高资质（Meets Standards Without Reservations）([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp. 8–11]])。

> [!method-scope] 方法范围
> - **研究对象** 依赖连续分数进行资源分配的教育与公共政策方案（如中[[Gaokao|高考]]择优录取、奖学金评定、学业辅导划线、贫困家庭资助线、按出生日期划定的小学入学年龄截点）。
> - **问题类型** 评估门槛政策对边界处人群[[Academic Achievement|学业成就]]、出勤率、身心健康及长期收入的净因果增量。
> - **分析单位** 处于驱动变量连续分布中的学生个体、班级或学校集群。
> - **输出形式** 断点处因果跃升跳跃估计值 $\tau_{\text{RDD}}$、局部线性回归斜率、最优带宽（Optimal Bandwidth）及 McCrary 密度检验统计图。

> [!citation-card]- 关键定义
> 断点回归设计是准实验方法中[[Internal Validity|内部效度]]最接近随机实验的设计。当受试者依据连续测量分数的固定切分点被分配到不同处理时，只要驱动变量与结果变量的关系在断点处可被准确建模，断点处的跳跃就能提供因果效应的无偏估计。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, pp. 320–321)]]
>
> *Regression discontinuity designs exploit exogenous administrative cutoffs on continuous running variables to [[Construct]] [[Counterfactual|counterfactuals]]. In the neighborhood of the cutoff, assignment is as good as random, allowing identification of local average treatment effects with causal rigor rivaling randomized trials.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **认识论取向** 秉承[[Postpositivism|后实证主义]]与因果计量经济学[[Paradigm|范式]]，用完全透明的确定性行政规则（Deterministic Rule）替代[[Random Assignment|随机化]]抽签，化解了实验随机分配剥夺弱势群体受助资格的伦理争议。
> - **因果识别定位** 属于基于外生规则识别的[[Counterfactual|反事实]]比较。相比常规倾向得分匹配（PSM）依赖不可检验的“可忽略性[[Hypothesis|假设]]（CIA）”，RDD 的因果有效性仅依赖“潜在结果在断点处关于驱动[[Variable|变量]]的条件期望连续性”，不依赖不可测混杂变量可被完全观测的严苛假定。
> - **与真实验（[[Randomised Controlled Trials|RCT]]）及准实验（[[Quasi-Experimental Designs|QED]]）的张力**
>   - **[[Internal Validity|内部效度]]** 在准实验谱系中居于顶峰，因果识别力远超非等对控制组前[[Pre-test and Post-test|后测]]设计；
>   - **[[External Validity|外部效度]]** 因果效应仅严格代表处于阈值切分点邻域（Cut-off Boundary）的边际群体（Marginal Population），无法直接推论至远离阈值的极端高分或低分群体。

> [!method-stack] 方法层级
> - **设计形态** 清晰断点回归（Sharp RDD）、模糊断点回归（Fuzzy RDD）、拐点断点回归（Regression Kink Design, RKD）。
> - **数据要求** 连续且不可被受试者精准主观操纵的驱动变量（Running Variable）、明确单侧或双侧外生切分阈值（Cutoff $c$）、干预后测指标。
> - **计量估计技术** 非参数局部线性回归（Local Linear Regression）、多项式边界拟合、IK/CCT 最优带宽选择算法、McCrary 密度函数连续性检验、安慰剂断点（Placebo Cutoffs）检验。

---

## 研究程序

> [!proc] 断点回归设计标准实施六步规程
> 1. **确认连续驱动[[Variable|变量]]与刚性阈值** 界定连续且可精确测量的运行变量（如标准化统考成绩 $X$），确定明确无歧义的政策划分截点 $c$。
> 2. **实施 McCrary 密度连续性检验** 绘制驱动变量在阈值 $c$ 两侧的频数分布直方图与核密度估计，排查受试者是否存在人为篡改成绩、虚报年龄等“操纵（Manipulation）”行为。
> 3. **检验协变量平滑性（Covariate Continuity）** 检验学生的性别、种族、家庭社会经济地位（SES）等前置基线特征在阈值两侧是否存在跳跃，确保仅干预状态发生突变。
> 4. **选定局部估计最优带宽（Optimal Bandwidth）** 采用 Imbens-Kalyanaraman (IK) 或 Calonico-Cattaneo-Titiunik (CCT) 数据驱动算法计算均方误差最小化的局部带宽 $h$。
> 5. **拟合局部回归模型** 在区间 $[c - h, c + h]$ 内运行局部线性回归，估计断点处因果跳跃参数 $\tau$ 及其稳健[[Standard Error|标准误]]。
> 6. **开展全面敏感性与稳健性分析** 检验多项式阶数敏感性（线性 vs 二次项）、测试不同带宽区间（$0.5h, 1.5h, 2h$）、并在非断点位置进行伪断点（Placebo Cutoff）[[Falsification|证伪]]检验。

---

### 清晰断点与模糊断点两大模型

> [!framework-table] 清晰断点（Sharp RDD） vs 模糊断点（Fuzzy RDD）对比
> | 比较维度 | 清晰断点回归 (Sharp RDD) | 模糊断点回归 (Fuzzy RDD) |
> |:---|:---|:---|
> | **干预分配规则** | **完全确定性分配** 跨过阈值者 100% 接受干预，未跨过者 100% 不接受干预（无不顺从）。 | **概率性分配** 跨过阈值使接受干预的概率发生显著跳跃（如从 20% 跳至 80%），存在违约者。 |
> | **数学分配条件** | $D_i = 1(X_i \ge c)$，分配概率跃升 $\Delta P(D_i=1 \mid X_i=c) = 1$ | $0 < \lim_{x \downarrow c} P(D_i=1 \mid X_i=x) - \lim_{x \uparrow c} P(D_i=1 \mid X_i=x) < 1$ |
> | **统计估计方法** | 局部 OLS 线性回归模型直接估计截距差。 | **两阶段最小二乘法（2SLS）** 以断点赋值状态 $T_i = 1(X_i \ge c)$ 作为实际接受干预 $D_i$ 的工具变量。 |
> | **因果效应解释** | 断点处边际人群的**局部平均处理效应（LATE）**。 | 断点处**顺从者群体的局部平均处理效应（Complier LATE）**。 |
> | **典型教育案例** | 依据会考成绩是否达标严格决定能否升学或拿奖学金。 | 依据成绩线推荐参加课后辅导，但学生可自主选择是否出勤。 |

---

### 计量模型与 WWC 审查标准

> [!formula-step] 断点回归计量方程与因果识别公式
> 
> 1. **清晰断点回归（Sharp RDD）局部线性估计模型**
>    在带宽 $X_i \in [c - h, c + h]$ 内，设定回归方程：
>    $$Y_i = \alpha + \mathbf{\tau} \cdot D_i + \beta_1 (X_i - c) + \beta_2 \cdot D_i (X_i - c) + \mathbf{\gamma}' \mathbf{Z}_i + \varepsilon_i$$
>    - **$Y_i$** [[Dependent Variable|结果变量]]（如[[Pre-test and Post-test|后测]][[Academic Achievement|学业表现]]）；
>    - **$X_i - c$** 驱动变量中心化数值；
>    - **$D_i = 1(X_i \ge c)$** 断点赋值虚拟变量；
>    - **$\mathbf{\tau}$** **核心因果效应参数**，代表断点两侧回归线在切分点 $c$ 处的垂直距离（跳跃量）；
>    - **$\beta_1, \beta_2$** 允许断点两侧回归线具有不同的演化斜率。
>
> 2. **模糊断点回归（Fuzzy RDD）工具变量局部瓦尔德估计量**
>    $$\tau_{\text{Fuzzy}} = \frac{\lim_{x \downarrow c} E[Y_i \mid X_i = x] - \lim_{x \uparrow c} E[Y_i \mid X_i = x]}{\lim_{x \downarrow c} E[D_i \mid X_i = x] - \lim_{x \uparrow c} E[D_i \mid X_i = x]} = \frac{\text{结果变量跳跃量}}{\text{处理概率跳跃量}}$$

> [!framework-table] 循证清算中心（[[What Works Clearinghouse|WWC]] / [[Home Visiting Evidence of Effectiveness|HomVEE]]）对 RDD 的审查规程与门槛（基于 Wadhwa et al., 2024）
> | 审查维度 | WWC / HomVEE 规定技术门槛 | 违规或不达标处理结果 |
> |:---|:---|:---|
> | **因果设计评级** | **3 级（建立专属完整审查标准）**；达标者评为 **Meets Standards Without Reservations**（一级最高认证）。 | 全库仅 WWC 与 HomVEE 赋予 RDD 与 [[Randomised Controlled Trials\|RCT]] 相同的最高准入地位。 |
> | **驱动变量[[Manipulation Check\|操纵检验]]** | 强制要求提供驱动变量在断点处的分布直方图与 McCrary 密度检验，证明无统计显著跳跃。 | 若存在人为扎堆操纵（Manipulation），直接判定未达标（Does Not Meet）。 |
> | **带宽与函数形式拟合** | 优先推荐局部线性回归或局部二次回归；限制使用全样本高阶多项式（防止边缘摆动假象）。 | 若使用 3 阶以上多项式且未作带宽截断，要求提供敏感性检验。 |
> | **共时外生政策排查** | 必须论证在断点 $c$ 处不存在其他同时发生截断的混杂政策（如免学费线与资优生辅导线重合）。 | 若存在共时政策重叠，因果归因失效。 |

---

## 适用场景

> [!fit-grid] 适用判断
> - **适合使用** 依据连续分数或测量值切分资格的政策干预（如托福/GRE 奖学金线、中考划线[[Partnership Schools Kura Hourua|特许学校]]、特教筛查临界值）；按法定出生日期划定的小学入学年龄断点（Age-Cutoff RDD）；贫困生助学金申请打分门槛。
> - **谨慎使用** 驱动[[Variable|变量]]易被基层教师或受试者主观调控（如平时[[Homework|作业]]打分）；[[Sample Size Determination|样本量]]过小导致断点局部有效观测点稀疏。
> - **不适合使用** 分配规则模糊、多重标准混杂或缺乏连续运行变量的常态课程对比（应选用配对准实验或 [[Randomised Controlled Trials|RCT]]）。

---

## 局限性

> [!method-limits] 效度威胁、偏误来源与误用风险
> - **局部外推局限（Local [[External Validity]]）** 因果结论严格局限于临界分数附近的“摇摆群体（Marginal Students）”，无法直接外推至极高分资优生或极低分学困生。
> - **操纵与自选择威胁（Manipulation Bias）** 若学生或家长通过提前获知阈值进行反复重考或人情微调分数，将导致断点两侧群体产生系统性能力失衡。
> - **高阶多项式的虚假波动（Runaway Polynomials）** Gelman & Imbens (2019) 指出，全样本高阶多项式回归容易在数据边界产生剧烈的虚假跳跃，必须采用局部低阶线性回归规避。
> - **大样本依赖性** RDD 仅利用带宽内局部样本估计效应，有效[[Sample Size Determination|样本量]]远小于全样本，通常需要比 [[Randomised Controlled Trials|RCT]] 多数倍的总样本量方能获得同等统计功效（Statistical Power）。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Quasi-Experimental Designs]] | 母类方法 | RDD 是准实验设计体系中内部效度最高、[[Causality\|因果推断]]力最强的亚型。 |
> | [[Randomised Controlled Trials]] | 黄金参照 | RDD 在断点邻域内实现局部[[Random Assignment\|随机化]]，被 [[What Works Clearinghouse\|WWC]] 视作与 RCT 并列的一级证据。 |
> | [[Time Series Design]] | 关联设计 | [[Intelligent Tutoring Systems\|ITS]] 属于“时间维度断点”，RDD 属于“属性分数维度断点”，二者共享局部跃升检验逻辑。 |
> | [[Campbellian Validity Framework]] | 理论基础 | 提供排查选择、历史与工具测量偏倚的[[Luhmann's Systems Theory\|系统理论]]工具。 |
> | [[Causality]] | 核心概念 | LATE 因果推断的现代计量[[Paradigm\|范式]]。 |
> | [[What Works Clearinghouse]] | 评价机构 | 制定了国际最完备的 RDD 强迫[[Variable\|变量]]操纵与带宽审查技术手册。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011)]] — 详述 Campbell & Stanley 创立的断点回归设计原理、符号模型、前[[Pre-test and Post-test|后测]]跳跃与效度特征(Ch. 16, pp. 320–324)。
> - [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]] — 比较 12 所清算中心对 RDD 因果设计的审查规程（RDD=3），揭示 [[What Works Clearinghouse|WWC]] 与 [[Home Visiting Evidence of Effectiveness|HomVEE]] 对强迫[[Variable|变量]][[Manipulation Check|操纵检验]]与带宽拟合的技术标准(pp. 8–11)。
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022)]] — 阐释断点回归作为高级[[Quasi-Experimental Designs|准实验设计]]在教育政策门槛评估中的实证应用规程(Ch. 8, p. 1327)。
