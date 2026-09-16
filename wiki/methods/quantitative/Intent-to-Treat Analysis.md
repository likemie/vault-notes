---
title: Intent-to-Treat Analysis
aliases:
  - 意向治疗分析
  - 意向性分析
  - Intention-to-Treat Analysis
summary: "一种按原始随机分配而非实际接受情况来分析结果的 RCT 因果估计方法，评估干预可获得性对总体结果的影响，并构成教育证据清算中心评级的核心基准。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 41
method_related_level: 5
method_related_stars: "⭐⭐⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/intent-to-treat-analysis
  - method/quantitative
related_concepts:
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Counterfactual]]"
  - "[[Variable]]"
  - "[[Causality]]"
  - "[[Internal Validity]]"
  - "[[Hypothesis]]"
  - "[[Attrition]]"
  - "[[Academic Achievement]]"
  - "[[Dependent Variable]]"
  - "[[Independent Variable]]"
  - "[[Educational Evidence Clearinghouses]]"
  - "[[Paradigm]]"
related_theories: []
related_methods:
  - "[[Randomised Controlled Trials]]"
  - "[[Random Assignment]]"
  - "[[Hierarchical Linear Model]]"
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
  - "[[Complier Average Causal Effect]]"
  - "[[Observation Method]]"
  - "[[Multi-Arm Trial]]"
  - "[[Cluster Randomized Trials]]"
  - "[[Factorial Design]]"
  - "[[Pre-test and Post-test]]"
  - "[[Analysis of Covariance]]"
  - "[[Generalized Estimating Equations]]"
  - "[[Imputation Methods]]"
  - "[[Implementation and Process Evaluation]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Ordinary Least Squares]]"
  - "[[Coding in Qualitative Research]]"
  - "[[Triangulation]]"
related_instruments:
  - "[[EEF Padlock Security Rating]]"
related_persons: []
related_facts:
  - "[[Education Endowment Foundation]]"
  - "[[Blueprints for Healthy Youth Development]]"
  - "[[Social Programs That Work]]"
  - "[[Promise Neighborhoods Research Consortium]]"
  - "[[What Works Clearinghouse]]"
related_arguments:
  - "[[Argument_Pampaka_2016_IJRME]]"
  - "[[Argument_Edovald_Nevill_2021_ECNUROE]]"
  - "[[Argument_Wadhwa_2024_RER]]"
confidence: high
status: active
created: 2026-05-02
updated: 2026-09-17
---

# Intent-to-Treat Analysis

---

## 定义

> [!def] 方法定义
> **意向治疗分析（Intent-to-Treat Analysis，简称 ITT）**是[[Randomised Controlled Trials|随机对照试验]]（RCT）中最核心的因果效应估计方法。其基本准则是：所有参与试验的被试必须完全保留在其最初被[[Random Assignment|随机分配]]的组别中进行统计分析，无论他们后续是否实际依从干预、是否中途退出、还是交叉接受了对照组措施。
>
> ITT 估计的核心属性在于：它测量的不是“干预实际接受（treatment uptake）”的技术性潜能，而是“干预可获得性或政策提供（treatment availability or offer）”对总体目标人群产生的净因果效应（[[Argument_Pampaka_2016_IJRME|Pampaka et al., 2016, p. 233]]）。

> [!method-scope] 方法范围
> - **研究对象** 随机对照试验与整群随机对照试验中的处理组与对照组全体参与样本及其学业、心理或行为产出数据。
> - **问题类型** 因果识别问题（回答“政策或项目在现实田野中一旦发布并提供给目标人群，平均带来多少净收益”）。
> - **[[Unit of Analysis|分析单位]]** 学生个体、教师、课堂或学校（需与随机分配层级相匹配或通过[[Hierarchical Linear Model|多水平模型]]处理嵌套结构）。
> - **输出形式** 标准化均值差（[[Effect Size|效应量]]，如 Hedges' $g$、Cohen's $d$）、无偏因果回归系数 $\beta_{\text{ITT}}$ 及其[[Confidence Interval|置信区间]]、显著性水平。

> [!citation-card] 政策干预可获得性与意向性分析的核心定位（[[Argument_Pampaka_2016_IJRME|Pampaka et al., 2016]]）
> 此类模型通常提供意向治疗（ITT）估计值，这对政策与实践具有极其重大的意义，“因为政策制定者和行政管理者往往只能控制某项干预措施的可获得性（availability），而根本无法强制其被实际接受与完全依从（uptake）”。[[Argument_Pampaka_2016_IJRME|(Pampaka et al., 2016, p. 233)]]
>
> *Such models usually offer intent-to-treat (ITT) estimates which is of great importance for policy and practice "as policymakers and administrators often have control only over the availability of an intervention, and not its uptake".*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与因果识别定位
> - **知识观** 坚持[[Counterfactual|反事实]]因果推理框架（Neyman-Rubin Causal Model）。认为[[Random Assignment|随机分配]]是消除混杂偏差与确保两组在可观测与不可观测[[Variable|变量]]上期望相等的唯一黄金标准；破坏最初分配组别将直接摧毁[[Causality|因果推断]]的基础。
> - **研究者角色** 恪守严格的客观分配边界，拒绝依据被试后续的依从表现进行主观事后筛选或分组清洗。
> - **有效性标准** [[Internal Validity|内部效度]]最高（完整维护随机化带来的平衡性，防范由非依从或选择性脱落引发的混杂偏误）；统计结论效度需防范因依从稀释导致的 II 型错误（假阴性）。
> - **不声称回答的问题** ITT 不能直接回答“如果学生或教师百分之百完全依从且高质量执行干预，该干预的理论最大效能是多少”（该问题需由[[Complier Average Causal Effect|依从者平均因果效应]]（CACE）或符合方案集分析回答）。

> [!contrast-table] 因果效应估计策略对比：ITT vs PP vs AT vs CACE
> | 估计策略 | 样本纳入准则 | 随机化平衡性 | 因果参数性质 | 主要优势与现实风险 |
> |---|---|---|---|---|
> | **意向治疗分析（ITT）** | 纳入所有随机分配样本，按原始分配组别分析 | **严格保持**，消除所有基线混杂偏误 | 政策提供效应（Effect of Treatment Availability） | 反映真实田野推广价值，保守稳健；但当非依从率高时严重稀释干预内在效力。 |
> | **符合方案集分析（Per-Protocol, PP）** | 仅纳入完全达到预定依从标准的样本 | **彻底破坏**，引入严重的非随机选择偏误 | 理想依从效能（Ideal Efficacy） | 揭示方案在完美执行下的效力；但破坏组间均衡，高估实际政策收益。 |
> | **实际接受分析（As-Treated, AT）** | 按被试实际接受的处理情况重新划组 | **彻底破坏**，等同于非等价的事后[[Observation Method\|观察研究]] | 实际暴露关联（Observed Exposure Association） | 严重混淆干预效果与个体主动选择特征，丧失因果识别能力。 |
> | **依从者平均因果效应（CACE / LATE）** | 全样本纳入，以随机分配作为工具变量进行两阶段估计 | **数学矫正保持**，依赖单调性与排他性约束[[Hypothesis\|假设]] | 潜在依从者因果效应（Complier Average Causal Effect） | 剥离依从衰减，精准还原真实参与者的净增益；但依赖不可直接检验的排除限制假设。 |

> [!method-stack] 方法层级
> - **研究设计** 双臂或[[Multi-Arm Trial|多臂随机对照试验]]（[[Randomised Controlled Trials|RCT]]）、整群随机对照试验（[[Cluster Randomized Trials|Cluster RCT]]）、[[Factorial Design|析因实验]]设计。
> - **数据收集** 试验前基线测试（Pre-test）、终点[[Pre-test and Post-test|后测]]（Post-test）、行政追踪数据库、实施出勤签到表与数字化学习日志。
> - **分析方法** [[Analysis of Covariance|协方差分析]]（ANCOVA）、多水平[[Hierarchical Linear Model|分层线性模型]]（Hierarchical Linear Modelling, HLM）、意向性[[Generalized Estimating Equations|广义估计方程]]（GEE）。
> - **辅助技术** 工具变量法（IV-2SLS）、全信息最大似然估计（FIML）、多重插补（Multiple [[Imputation Methods|imputation]]）、[[Attrition|流失]]敏感性检验。

---

## 研究程序

> [!proc] 通用程序
> 1. **确定全样本基线并实施[[Random Assignment|随机分配]]** 严格锁定试验招募池所有被试的身份标识，在基线测验完成后由独立统计师实施随机双盲或单盲分配，生成不可篡改的初始组别名单。
> 2. **全周期追踪与非依从/[[Attrition|流失]]监测** 在干预推进过程中，独立于干预团队进行[[Implementation and Process Evaluation|实施与过程评估]]（IPE），详实记录每位参与者的出勤率、系统登录日志、脱落时间与对照组污染事件。
> 3. **执行全样本终点测试与数据补全** 无论学生或学校是否中途放弃干预，调查团队均必须全力动员其参加终点[[Pre-test and Post-test|后测]]，尽可能将样本流失率控制在最低警戒线以内。
> 4. **构建意向治疗统计模型** 严格按照初始分配[[Variable|变量]]编制哑变量指标，在控制基线协变量与嵌套集群效应的基础上估计主效应 $\beta_{\text{ITT}}$。
> 5. **敏感性分析与依从机制校正** 针对不可避免的样本流失开展流失偏误检验；若现场非依从率显著，进一步利用随机分配作为工具变量拟合 [[Complier Average Causal Effect|CACE]] 模型，对照解释 ITT 估计值的稀释程度。

### 量化分析模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 学生嵌套于班级、学校的层级嵌套实验数据，或多时期重复测量面板数据。
> - **样本与单位** 试验初始登记的全体被试；[[Unit of Analysis|分析单位]]通常为学生个体或学校（若为整群试验需计算校内相关系数 [[Intraclass Correlation Coefficient|ICC]]）。
> - **核心变量**
>   - 处理分配变量 $Z_i$：随机指派状态（1 = 处理组，0 = 对照组），由研究者控制。
>   - 实际接受变量 $D_i$：个体实际接受剂量或依从状态（1 = 达标参与，0 = 未依从或未达标）。
>   - 产出变量 $Y_i$：标准化后测[[Academic Achievement|学业成绩]]或认知/行为测验得分。
>   - 基线协变量 $\mathbf{X}_i$：前测成绩、家庭经济背景（如免费校餐 FSM 资格）、特殊教育需求（SEND）等。
> - **模型形式** 多水平协方差模型（Hierarchical [[Analysis of Covariance|ANCOVA]]）或多群组 [[Ordinary Least Squares|OLS]] 回归。

> [!formula-step] 公式步骤　基础 ITT 回归模型
> $$Y_{ij} = \alpha + \beta_{\text{ITT}} Z_j + \mathbf{X}_{ij}' \boldsymbol{\gamma} + u_j + \varepsilon_{ij}$$
>
> **这个公式在做什么** 以个体终点学业产出 $Y_{ij}$ 为[[Dependent Variable|因变量]]，以初始随机分配指示变量 $Z_j$ 为核心[[Independent Variable|自变量]]，在控制个体与学校基线协变量 $\mathbf{X}_{ij}$ 以及学校随机效应 $u_j$ 的条件下，直接估计政策分配带来的净平均因果效应 $\beta_{\text{ITT}}$。
>
> **符号说明**
> - $Z_j$：学校 $j$ 随机分配状态（1 = 获派处理，0 = 获派对照），严格保持初始指派。
> - $\beta_{\text{ITT}}$：意向治疗因果效应估计值，反映政策可获得性的平均效应。
> - $\mathbf{X}_{ij}$：学生与学校层面的基线预测向量，用于降低残差方差并提升统计功效。
> - $u_j, \varepsilon_{ij}$：学校间随机效应与学生个体水平误差项。
>
> **数学直觉** 回归系数 $\beta_{\text{ITT}}$ 严格等于处理组与对照组在终点产出上的调整均值差（Adjusted Mean Difference）。由于随机化保证了在试验启动时 $\mathbb{E}[\mathbf{X} \mid Z=1] = \mathbb{E}[\mathbf{X} \mid Z=0]$ 且 $\mathbb{E}[\varepsilon \mid Z] = 0$，因此 $\beta_{\text{ITT}}$ 是干预提供政策效果的无偏估计。
>
> **结果怎么读** $\beta_{\text{ITT}} > 0$ 且[[Confidence Interval|置信区间]]不穿过 0，表明向学校提供该干预方案显著提升了学生的学业产出；若数值接近 0，则表明在真实学校生态下提供该方案未带来系统性总体收益。
>
> **注意事项** 当存在严重非依从（Non-compliance）时，模型“不再估计实际处理效应，因为它们并不模拟每个个体实际接受的处理”（[[Argument_Pampaka_2016_IJRME|Pampaka et al., 2016, p. 233]]）。若教师中存在表面依从但实质未落实现象，甚至可能掩盖真实推广困境（[[Argument_Pampaka_2016_IJRME|Pampaka et al., 2016, pp. 233–234]]）。

> [!formula-step] 公式步骤　工具变量与 CACE 关联调整
> $$\beta_{\text{CACE}} = \frac{\beta_{\text{ITT}}}{\Pr(D = 1 \mid Z = 1) - \Pr(D = 1 \mid Z = 0)}$$
>
> **这个公式在做什么** 利用随机分配状态 $Z$ 作为实际干预接受状态 $D$ 的外生工具变量（Wald 估计量），将意向治疗效应 $\beta_{\text{ITT}}$ 按实际依从比例进行缩放，还原出真正依从干预方案者的平均因果效应（CACE）。
>
> **符号说明**
> - $\beta_{\text{CACE}}$：依从者平均因果效应（Complier Average Causal Effect）。
> - $\Pr(D=1 \mid Z=1)$：分配到处理组的样本中实际达标执行干预的比例（处理组依从率）。
> - $\Pr(D=1 \mid Z=0)$：分配到对照组的样本中交叉接受干预的比例（对照组污染率；单侧非依从下为 0）。
>
> **数学直觉** ITT 效应实际上等于“依从者效应”乘以“依从者在全人群中所占的比例”。因此，当且仅当干预分配对非依从者产出无直接影响（排他性约束，Exclusion Restriction）时，将 ITT 除以依从率差值即可消除非依从稀释，重构出真实介入强度下的因果贡献。
>
> **结果怎么读** 当依从率小于 100% 时，分母小于 1，必有 $|\beta_{\text{CACE}}| > |\beta_{\text{ITT}}|$。依从率越低，ITT 与 CACE 差距越大，直观体现出政策稀释的严重程度。
>
> **注意事项** 该调整高度依赖单调性[[Hypothesis|假设]]（无逆反者 Defiers）与排他性约束假设。在英国[[Education Endowment Foundation|EEF]]的大规模实证评估中，研究团队普遍将 ITT 作为首要报告指标，并配合 CACE 作为关键探索性分析，以科学解释为何总体效应较小（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 50, 53]]）。

> [!software-impl] 软件实现
> - **推荐软件** R (`lme4`, `AER`, `clubSandwich`), Stata (`mixed`, `ivregress`), Python (`statsmodels`).
> - **实现流程**
>   1. 数据清洗：保留所有随机化样本，[[Coding in Qualitative Research|编码]] $Z$（初始分配）与实际出勤时长 $D$。
>   2. 估计基准 ITT 模型：
>      - Stata: `mixed math_post treat_assign math_pre fsm || school_id:, vce(cluster school_id)`
>      - R: `lmer(math_post ~ treat_assign + math_pre + fsm + (1 | school_id), data = rct_data)`
>   3. 估计 CACE 工具变量模型：
>      - Stata: `ivregress 2sls math_post math_pre fsm (treatment_uptake = treat_assign), vce(cluster school_id)`
> - **报告标准** 完整呈现试验入组基线 $N$、后测分析 $N$、总流失率与组间差异流失率、ITT 点估计值与 95% 置信区间、Hedges' $g$ [[Effect Size|效应量]]。

---

## 证据清算中心与制度化标准

> [!summary-card] [[Educational Evidence Clearinghouses|教育证据清算中心]]的 ITT 规范化准入基准
> 在国际主要[[Educational Evidence Clearinghouses|教育证据清算中心]]的评估体系中，ITT 已从一项统计学方法演化为判定证据质量的显性准入门槛（[[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, p. 9]]）：
>
> 1. **全样本分析的强制约束**
>    - [[Blueprints for Healthy Youth Development]]、[[Social Programs That Work]]（SPTW）与 [[Promise Neighborhoods Research Consortium]]（PNRC）**明确强制要求 ITT 分析**。任何剔除非依从学校、剔除未完成干预学童或按实际执行情况重新分组的评估报告，将直接被剥夺最高证据评级资格。
>    - 美国联邦教育部[[What Works Clearinghouse|WWC]]在因果标准中确立：只有基于原始随机组别的 ITT 分析且[[Attrition|流失]]率达标的 [[Randomised Controlled Trials|RCT]]，才具备获评“无保留满足标准（Meets Standards Without Reservations）”的资格；在特定合规监测条件下，允许补充报告 [[Complier Average Causal Effect|CACE]]。
> 2. **样本流失与[[EEF Padlock Security Rating|挂锁安全评级]]的联动约束**
>    - 英国[[Education Endowment Foundation|EEF]]将 ITT 确立为所有评估报告第一标题[[Effect Size|效应量]]（Headline Effect Size）的法定计算口径（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, p. 50]]）。
>    - 然而，若试验遭遇严重的随访流失（Attrition），即使遵循 ITT 统计口径，组间基线可比性亦可能荡然无存。为此 EEF 实施了严格的[[EEF Padlock Security Rating|挂锁安全评级]]：将流失率作为核减挂锁数量的核心依据。全英试验通过专业招募与留存规程，使 85% 的试验将样本流失率控制在 30% 以内，稳健维持了 3 把挂锁以上的证据信用（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 49–51]]）。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 评估具有普适推广属性的政策、全校性改革或教学干预项目。
>   - 需要向政策制定者、行政管理者提供真实田野预期回报的评估报告（[[Argument_Pampaka_2016_IJRME|Pampaka et al., 2016]]）。
>   - 申报[[Educational Evidence Clearinghouses|证据清算中心]]高等级认证的严格因果实证研究（[[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024]]）。
> - **谨慎使用**
>   - 早期原型测试（Feasibility / Pilot Stage）与探索性机制试验。在此阶段方案尚未成熟，实施障碍极多，若单纯汇报 ITT 可能过早将具有潜力的创新方案否定。
>   - 存在极高非依从率或大规模交叉污染的现实试验，此时必须联合使用 [[Complier Average Causal Effect|CACE]] 和实施过程分析进行多重视角报告。
> - **不适合使用**
>   - 纯粹探讨人类认知加工极限或生物物理机理的基础心理学实验室研究（此类研究追求在严格依从条件下的机制因果验证，无需承担政策推广可获得性解释）。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源**
>   - **假阴性与稀释偏误（Dilution Bias）** 当许多受派学校并未真实开展干预活动时，由于 ITT 机械地将未受干预样本的零产出混入处理组计算，会导致估计出的[[Effect Size|效应量]]趋近于零，掩盖方案在真实落实时的有效性。
>   - **样本选择性[[Attrition|流失]]（Differential Attrition）** 若困难学生更倾向于从处理组脱落，将造成两组基线破缺。ITT 无法自动解决非随机流失问题（Schweig & Pane, 2016; [[Argument_Pampaka_2016_IJRME|Pampaka et al., 2016]]）。
> - **适用边界** 仅能回答“政策提供”的因果效应，无法解释因果机制与黑箱过程。
> - **误用风险** 将 ITT 估计的微弱正向效应直接等同于“干预毫无价值”，忽视实施剂量与保真度短板；或将名义上的技术依从等同于实质高质量落实，导致推广至真实世界时效果再次受挫（[[Argument_Pampaka_2016_IJRME|Pampaka et al., 2016, pp. 233–234]]）。
> - **补救方式** 建立“量化 ITT + 质性/量化 [[Implementation and Process Evaluation|IPE]] 过程评估 + 工具[[Variable|变量]] [[Complier Average Causal Effect|CACE]]”三位一体的[[Triangulation|三角互证]]链条（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021, pp. 53–54]]）。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 政策真实性 vs 科学效力辨识
> > 方法学界关于 ITT 与符合方案集（PP）优先级的长期争辩。
> >
> > - **循证政策派主张** 坚定维护 ITT 的基础地位，指出政策制定者不可能监督每一位教师，现实中的参与摩擦正是干预本身的内生属性，ITT 能够提供最真实的政策参考参数（[[Argument_Pampaka_2016_IJRME|Pampaka et al., 2016]]）。
> > - **干预开发者反驳** 主张在研发早期应当剔除非依从样本，否则在低保真度实施下的微弱 ITT 效应会直接导致极具价值的教学创新被证据清算机构过早否定。
>
> > [!axis] 单一因果点估计 vs 过程黑箱遮蔽
> > 传统循证评估仅公布单一 ITT [[Effect Size|效应量]]，引发实证学界对“只问疗效、不问机理”的批评。
> >
> > - **黑箱批评** 传统 ITT 报告无法回答干预“为何起效”或“为何失效”，无法区分是“理论方案本身的缺陷”还是“现场未能落实的缺陷”（[[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill, 2021]]）。
> > - **双轨评估[[Paradigm|范式]]** [[Education Endowment Foundation|EEF]] 创设了“双独立团队模式”与强制 [[Implementation and Process Evaluation|IPE]] 规程，确立了必须将 ITT 统计量与全过程质性量化实施评估紧密并置的当代因果评估范式。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Randomised Controlled Trials]] | 前置方法 | ITT 因果识别的基础设计框架，[[Random Assignment\|随机分配]]为 ITT 提供[[Internal Validity\|内部效度]]前提。 |
> | [[Random Assignment]] | 前置方法 | 决定初始组别归属的核心机制，ITT 必须严格按该分配状态划分样本。 |
> | [[Complier Average Causal Effect]] | 补充方法 | 借助工具[[Variable\|变量]]法从 ITT 估计量中剥离非依从稀释，重构实际依从者的因果效应。 |
> | [[Cluster Randomized Trials]] | 前置方法 | 学校/班级水平整群试验中应用 ITT 需校正集群误差与部分嵌套设计影响。 |
> | [[Implementation and Process Evaluation]] | 补充方法 | 提供剂量、合规度与保真度现实证据，为解释 ITT 估计量提供机制链条支撑。 |
> | [[Educational Evidence Clearinghouses]] | 评价标准 | 国际证据清算中心将 ITT 确立为评定研究质量最高等级的显性门槛。 |
> | [[EEF Padlock Security Rating]] | 评价标准 | 联合监测 ITT 试验的[[Attrition\|样本流失]]与设计风险，确保因果推论的安全等级。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Pampaka_2016_IJRME|Pampaka et al. (2016)]] — 系统论述了部分嵌套 [[Randomised Controlled Trials|RCT]] 中集群效应与非依从性对 ITT 估计统计推断的影响，阐明了 ITT 在反映政策可获得性与解释大规模推广困境中的核心价值。
> - [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]] — 跨国[[Educational Evidence Clearinghouses|证据清算中心]]元综述，证实 [[Blueprints for Healthy Youth Development|Blueprints]]、[[Social Programs That Work|SPTW]]、[[Promise Neighborhoods Research Consortium|PNRC]] 与 [[What Works Clearinghouse|WWC]] 将 ITT 确立为筛选高质量因果证据的刚性制度化基准。
> - [[Argument_Edovald_Nevill_2021_ECNUROE|Edovald & Nevill (2021)]] — 英国 [[Education Endowment Foundation|EEF]] 十年循证评估综述，阐述将 ITT 作为全英大规模田野 RCT 首要指标的制度实践，及其与[[EEF Padlock Security Rating|挂锁安全评级]]、[[Implementation and Process Evaluation|IPE]] 过程评估和 [[Complier Average Causal Effect|CACE]] 工具[[Variable|变量]]调整的协同运作机制。
