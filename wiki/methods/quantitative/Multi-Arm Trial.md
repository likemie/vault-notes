---
title: Multi-Arm Trial
aliases:
  - 多臂试验
  - 多臂随机对照试验
  - 多组试验
  - Multi-Arm Randomized Controlled Trial
  - Multi-Arm Trials
  - Multi-Arm RCT
summary: "包含三个或更多平行实验组（实验臂）的随机对照试验设计，通过共享对照组评估多种竞争性干预的相对疗效，并依托族系误差率（FWER）校正方法控制多重比较偏误。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 6
method_related_level: 0
method_related_stars: ""
method_related_color: "#dcfce7"
tags:
  - method/quantitative
  - method/experimental
  - method/rct
  - method/trial-design
related_concepts:
  - "[[Business as Usual]]"
related_theories: []
related_methods:
  - "[[Randomised Controlled Trials]]"
  - "[[Cluster Randomized Trials]]"
  - "[[Intent-to-Treat Analysis]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Edovald_Nevill_2021_ROE]]"
  - "[[Argument_Gough_2022_EvidenceOnEIPP]]"
confidence: high
status: active
created: 2026-09-15
updated: 2026-09-15
---

# Multi-Arm Trial

---

## 定义

> [!def] 方法定义
> **多臂试验（Multi-Arm Trial，亦称多臂随机对照试验 Multi-Arm RCT）**是指在单一试验方案中包含**三个或更多平行实验组（实验臂，Arms）**的高级实验设计架构。最经典的多臂形态是“多个互斥的处理组共享一个公共对照组”（Multi-Arm Single-Control Design，如 $K$ 个处理臂对比 1 个对照臂）。该设计通过在同一实验背景下同时检验多种竞争性干预策略、不同实施剂量或不同递送载体，不仅能大幅节省招募独立对照组的样本与财务成本，还能通过直接的头对头（Head-to-Head）比较确立最优实践方案。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, pp. 53–54)]]

> [!method-scope] 方法范围
> - **研究对象** 被随机分配至不同干预臂或对照臂的个体受试者或集群单位（学校/班级）。
> - **问题类型** 相对疗效比较（“在 A、B、C 三种教学策略中哪一种最有效”）、干预递送媒介效能筛选、复合方案独立组件拆解。
> - **分析单位** 学生个体或集群学校。
> - **输出形式** 各处理臂相对于对照组的平均处理效应（ATE）、各处理臂之间的成对均值差、经过多重比较校正的置信区间与调整后 $p$ 值。

> [!citation-card] 多臂试验与复杂因果机制拆解（Edovald & Nevill, 2021; Lord et al., 2017）
> 为彻底打破传统双臂实验将复杂方案打包为单维度黑箱的局限，英国 EEF 大力资助并探索多臂试验与析因架构。在著名的“识字八爪鱼”多臂试验（Lord et al., 2017）中，EEF 动员了全英 800 余所小学，设置多个平行实验臂系统对比了纸质手册、邮件通讯、杂志专栏及网络研讨 4 种证据传播载体，最终证实单向被动推送循证材料对学生成绩的净效应全部为零，有力推动英格兰建立了深入基层的研究学校网络。此外，在 ABRA 在线阅读多臂试验中，评估团队通过多臂设计系统剥离了技术软件自主学习与教师主导辅导的独立与交互效应。[[Argument_Edovald_Nevill_2021_ROE|(Edovald & Nevill, 2021, pp. 53–54)]]
>
> *“To open the black box of complex interventions, the EEF has funded multi-arm trials and factorial designs. In the Literacy Octopus trial (Lord et al., 2017), multiple arms tested distinct dissemination methods across 800 primary schools, providing clear causal evidence on the relative inefficacy of passive research communication.”*

---

## 方法定位与概念辨析

> [!method-position] 认识论与方法定位
> - **效率与生态可比性** 相比于分别开展多个独立的双臂试验（Two-Arm Trials），多臂试验通过共享对照组（Shared Control），显著减少了所需的总体样本量；更重要的是，所有处理臂在完全相同的时间窗口、宏观政策背景与测验标尺下接受评估，彻底排除了跨试验历史时间偏误。
> - **统计核心挑战** **多重比较（Multiple Comparisons）与第一类错误膨胀**。当同时对多个处理臂进行假设检验时，全试验至少犯一次 I 型错误的族系误差率（Family-Wise Error Rate, FWER）显著上升，必须引入适宜的多重推断校正策略。

> [!contrast-table] 核心概念辨析：多臂试验 vs 析因设计 vs 传统双臂 RCT
> | 比较维度 | 传统双臂试验（Two-Arm RCT） | 多臂试验（Multi-Arm Trial） | 析因设计（Factorial Design） |
> |---|---|---|---|
> | **实验组结构** | 仅 2 组（1 处理组 vs 1 对照组） | $\ge 3$ 组（如 Treatment A, B, C vs Control） | 因子水平正交完全交叉（如 $2 \times 2$ 形成 4 个处理组合） |
> | **干预性质** | 单一干预方案的孤立有效性 | 多个独立/竞争性方案、不同剂量或媒介 | 两个或多个离散因子的独立组合与协同 |
> | **核心分析目标** | 检验干预是否存在主效应 | 比较多个干预的相对优劣（A vs B vs Control） | **同时估计各因子的主效应与因子间的交互效应** |
> | **组间交叉关系** | 无交叉 | 并行互斥（各臂为独立的干预方案） | 结构化正交交叉（每一受试单元处于特定因子组合） |
> | **统计关注重点** | 基础双样本均值推断 | **族系误差率（FWER）校正、共享对照组样本配比** | **交互效应项（$A \times B$）统计检验力** |
> | **包含关系定位** | 最简特例 | **上位广义框架**（涵盖非析因多臂与析因架构） | **多臂试验的特化正交结构**（用于检验交互作用） |

> [!method-stack] 方法层级
> - **研究设计** 并行多臂随机对照试验（Parallel Multi-Arm RCT）、多臂多阶段自适应试验（MAMS）。
> - **数据收集** 统一基线前测、多臂干预递送监测、标准化终结性测验（NPD 考分）。
> - **分析方法** 单因素多水平方差分析（ANOVA）、引入协变量的 OLS 回归、多层线性模型（HLM）。
> - **辅助技术** Dunnett 检验（处理组对比对照组）、Tukey HSD 检验（处理组两两互比）、Bonferroni / Benjamini-Hochberg FDR 校正。

---

## 研究程序

> [!proc] 通用程序
> 1. **定义干预臂与理论机制假设** 界定清晰的对照臂（通常为常态对照）以及各个处理臂的具体内容，确保各臂之间在操作定义上清晰分离。
> 2. **优化样本量与组间分配比例** 依据最优配比准则（如 Dunnett 根号原则），适当增加共享对照组的分配比例以提升整体统计功效。
> 3. **执行随机化分组** 采用区组分层随机化或整群随机化将受试者（或学校）分配至各个实验臂。
> 4. **主效应与成对均值估计** 拟合协变量调整回归方程，提取各个干预臂相对于对照组的点估计与未调整标准误。
> 5. **执行多重比较校正** 针对预先设定的关键假设检验，执行 Dunnett 校正或 FDR 控制，汇报校正后的 $p$ 值与置信区间。

### 量化分析模块

> [!method-stack] 数据、变量与模型
> - **数据结构** 包含 $K$ 个处理臂与 1 个对照臂的样本数据，总组数 $G = K + 1$。
> - **核心变量**
>   - 因变量 $Y_i$：后测标准化成绩。
>   - 实验臂类别指示变量 $\text{Arm}_i \in \{0, 1, 2, \dots, K\}$（0 为对照组）。
>   - 协变量矩阵 $\mathbf{X}_i$：基线前测考分与学生人口学特征。
> - **诊断与检验** 多重比较方差齐性检验、各臂样本流失率均衡性诊断。

> [!formula-step] 公式步骤　共享对照组的最优样本配比准则（Dunnett 根号 K 原则）
> $$\frac{N_C}{N_k} \approx \sqrt{K}$$
>
> **这个公式在做什么** 在总样本量固定的约束下，计算当有 $K$ 个处理臂同时与同一个对照臂进行比较时，对照组样本量与单个处理组样本量的最优比例。
>
> **符号说明**
> - $N_C$：对照组分配的样本量。
> - $N_k$：每个单独处理臂分配的样本量（假设各处理臂规模对称，即 $N_1 = N_2 = \dots = N_K$）。
> - $K$：处理臂的数量。
>
> **数学直觉** 对照组作为所有处理组计算处理效应（$\bar{Y}_k - \bar{Y}_C$）的共有基准，其估算误差会进入所有成对比较中。因此，为对照组赋予更大的样本量（正比于 $\sqrt{K}$），能够以最低的总样本成本最小化所有成对差异估计量的联合方差。例如当 $K = 4$ 时，对照组规模应当是单个处理组的 2 倍（即比例为 2:1:1:1:1）。
>
> **结果怎么读** 指导试验招募计划：切忌盲目平均分配样本；合理倾斜对照组能显著提升试验整体统计功效。
>
> **注意事项** 若核心研究目的并非“各处理组与对照组比较”，而是“处理组之间两两互比”，则最优分配比例重新退回 1:1:1...。

> [!formula-step] 公式步骤　多重检验族系误差率（FWER）与 Dunnett 校正
> $$\alpha_{\text{FWER}} = 1 - (1 - \alpha_{\text{per-comparison}})^K \approx K \cdot \alpha$$
>
> **这个公式在做什么** 测算在未做校正时多重比较导致的整体第一类错误膨胀幅度，并说明专门校正方法的必要性。
>
> **符号说明**
> - $\alpha_{\text{FWER}}$：整个试验中至少出现一次假阳性显著的总体概率。
> - $\alpha_{\text{per-comparison}}$：单个假设检验的名义显著性水平（通常为 0.05）。
> - $K$：独立检验的假设数量。
>
> **数学直觉** 当 $K = 4$ 时，未校正的 $\alpha_{\text{FWER}} \approx 1 - (0.95)^4 \approx 18.5\%$。这意味着即使所有干预完全无效，研究者依然有接近两成的概率宣称某一个干预“显著有效”。Dunnett 检验利用了各检验统计量之间因共享对照组而产生的多元 $t$ 联合分布相关性（$\rho = 0.5$），相比保守的 Bonferroni 检验具有更高的检验功效。
>
> **结果怎么读** 必须汇报经多重比较校正后的临界值与调整后 $p$ 值，只有校正后依然达标的效应才能定性为实质因果有效。
>
> **注意事项** 在探索性多臂筛选阶段，过于严厉的 FWER 惩罚可能增加 II 型错误（误杀潜在有效方案），需在研究方案中明确区分证实性主检验与探索性次要检验。

> [!software-impl] 软件实现
> - **推荐软件** R (`multcomp`, `emmeans`), Stata (`pwcompare`).
> - **核心命令**
>   - R:
>     ```R
>     library(multcomp)
>     model <- lm(post_score ~ arm + pre_score, data = df)
>     # Dunnett 检验（所有处理臂对比对照组 Arm 0）：
>     dunnett_test <- glht(model, linfct = mcp(arm = "Dunnett"))
>     summary(dunnett_test)
>     ```
>   - Stata:
>     ```stata
>     reg post_score i.arm pre_score
>     pwcompare arm, mcompare(dunnett) pveffects
>     ```
> - **实现流程**
>   1. 拟合基准协变量调整模型；
>   2. 构建处理组与对照组对比矩阵；
>   3. 运用 Dunnett 联合多元分布计算调整后标准误与 $p$ 值；
>   4. 绘制各臂效应量森林图与置信区间带。
> - **报告标准** 完整汇报各臂样本量、未调整均值、协变量调整后均值差、未调整 $p$ 值、多重比较校正后 $p$ 值及校正后 95% 置信区间。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**
>   - 评估多种具有竞争性的不同教学法、课程材料或师资培训模式（如识字八爪鱼试验对比 4 种传播手段）；
>   - 探究干预措施的最佳实施剂量（如低频辅导 vs 高频辅导 vs 对照组）；
>   - 自适应多阶段试验（Multi-Arm Multi-Stage, MAMS），在中期评估中动态淘汰无效臂（Drop the loser）。
> - **谨慎使用**
>   - 总样本资源极度有限的研究（过多分支会导致每个实验臂样本量严重不足，统计功效断崖式下跌）；
>   - 混杂了多个同时变化的复合维度而无法形成清晰单维度梯度的研究。
> - **不适合使用**
>   - 仅包含单一处理方案与对照组的简单因果验证（直接使用双臂 RCT 即可）；
>   - 核心研究目的在于检验两个因子之间是否存在协同交互增益的研究（必须升级为严格的[[Factorial Design|析因设计]]）。

---

## 局限性

> [!method-limits] 方法局限
> - **样本招募负担与管理复杂度高** 多臂试验需要动员成倍的学校与受试者，且现场多套方案并行递送极易发生混淆与交叉污染。
> - **对照组污染风险翻倍** 由于存在多个活跃的处理臂，对照组学校通过日常交流接触到某一试验臂教学法而发生常态基线提升的风险成倍增加。
> - **统计功效权衡困境** 若强行严格校正 FWER，检测微小效应量的统计功效会显著下降；若不校正，假阳性风险不可忽视。
> - **补救方式** 采用预注册统计分析计划（SAP）预先锁定主对比；运用 Dunnett 针对性校正；强化实施保真度监测。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 多重比较校正的必要性 vs 科学发现的保守性
> > 证据方法学界围绕多臂试验是否必须强制调整显著性阈值的争辩。
> >
> > - **严格计量派观点** 坚持多重比较必然诱发全试验假阳性概率膨胀。若不惩罚显著性门槛，所谓的“显著干预”很可能只是多轮抽样随机涨落的产物，严重损害循证决策的可靠性。
> > - **实践实用派反驳** 认为在教育与社会政策评估中，各处理臂往往代表着完全不同的独立理论实体；强行采用过度保守的校正会大幅增加 II 型错误，将原本具有实践潜力的优秀教育方案判为无效。现代折中标准主张将主效应检验与探索性比较在预注册阶段予以明确分流。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Randomised Controlled Trials]] | 上位范式 | 多臂试验所属的广义随机实验因果推断框架。 |
> | [[Factorial Design]] | 特化正交结构 | 析因设计是多臂试验中因子正交交叉的特例，专门用于检验交互效应。 |
> | [[Cluster Randomized Trials]] | 组织形态 | 当多臂试验在学校或班级层面进行分配时的整群实验形态。 |
> | [[Literacy Octopus]] | 经典案例 | EEF 运用多臂试验检验 4 类知识传播样态并证实全部无效的标志性试验。 |
> | [[Business as Usual]] | 基线对照 | 多臂试验中所有处理臂共同依存的基准对照状态。 |
> | [[Intent-to-Treat Analysis]] | 分析准则 | 多臂试验评估各臂平均因果效应所遵循的标准意向性分析规程。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Edovald_Nevill_2021_ROE|Edovald & Nevill (2021)]] — 阐述了英国 EEF 通过多臂试验与析因设计打开复杂教育干预黑箱的演进历程，重点评述了“识字八爪鱼”多臂试验与 ABRA 在线阅读多臂试验的方法学价值。
> - [[Argument_Gough_2022_EvidenceOnEIPP|Gough et al. (2022)]] — 详析了“识字八爪鱼”大规模多臂 RCT 的因果结论，证明单纯单向推送实证成果对改善学生终考成绩毫无统计显著性。
