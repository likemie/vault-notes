---
title: Statistical Process Control
aliases:
  - 统计过程控制
  - SPC
  - 统计制程管制
summary: "统计过程控制（Statistical Process Control, SPC）是由休哈特奠基的量化质量控制与过程监测方法体系。该方法运用正态分布与中心极限定理，通过控制图及 3-sigma 控制界限区分偶然变异与异常变异，并结合工序能力指数评估系统稳态，广泛用于装备中试与教育纵向监测。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 25
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - quantitative-method
  - statistical-process-control
  - quality-control
  - longitudinal-monitoring
  - process-capability
related_concepts:
  - "[[Unit of Analysis]]"
  - "[[Cost of Ownership]]"
  - "[[Reliability]]"
  - "[[Epistemology]]"
  - "[[Center of Calculation]]"
  - "[[Variable]]"
  - "[[Academic Achievement]]"
  - "[[Total Quality Management]]"
related_theories:
  - "[[Central Limit Theorem]]"
related_methods:
  - "[[Process Tracing]]"
  - "[[Stratified Sampling]]"
  - "[[Standard Error]]"
  - "[[Confidence Interval]]"
  - "[[Fieldwork]]"
  - "[[Effect Size]]"
  - "[[Industrial Benchmarking]]"
  - "[[Time Series Design]]"
  - "[[Analytic Framework]]"
  - "[[Longitudinal Study]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Department of Energy]]"
  - "[[Competitive Semiconductor Manufacturing Program]]"
  - "[[Sematech]]"
related_arguments:
  - "[[Argument_Grindley_1994_JPAM]]"
  - "[[Argument_Macher_1998_CMR]]"
confidence: high
status: active
created: 2026-10-04
updated: 2026-10-04
---

# Statistical Process Control

---

## 定义

> [!def] 方法定义
> **统计过程控制（Statistical Process Control, SPC）**是一种运用统计学原理对生产制造、组织运营或教育服务等连续过程进行实时监测、变异诊断与质量受控状态评估的量化方法。其核心在于利用时序抽样数据绘制控制图（Control Charts），依据正态分布与随机波动规律设立上下控制界限（$\pm 3\sigma$），在过程发生系统性漂移或异常扰动时发出早期预警，从而实现由“事后检验筛选”向“事前预防与过程稳态控制”的根本转变。在半导体高精制造中，SPC 通过全流程在线参数监控消除工艺偏差，直接驱动缺陷密度压降与良率爬坡。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, pp. 735, 746)]]; [[Argument_Macher_1998_CMR|(Macher et al., 1998, pp. 113–118)]]

> [!method-scope] 方法范围
> - **研究对象** 连续制造工序参数、设备运行物理指标（如线宽、氧化层厚度、刻蚀速率、洁净室颗粒数）、晶圆缺陷密度（$D_0$）、每百万缺陷数（PPM）、学校学生日常测验成绩时序轨迹及行政服务周期。
> - **问题类型** 过程稳定性诊断、异常变异识别、工序制造能力评价、质量改进干预前后的稳态对比。
> - **[[Unit of Analysis|分析单位]]** 连续生产批次、晶圆批次（Lot）、样本子组（Subgroups）、时序周/月观测单元、班级或学校学期数据点。
> - **输出形式** 休哈特控制图（$\bar{X}-R$ 图、$\bar{X}-S$ 图、$p$ 图、$c$ 图）、工序能力指数（$C_p, C_{pk}, P_p, P_{pk}$）、受控状态诊断报告与异常归因警报。

> [!citation-card]- 关键定义
> 统计过程控制（SPC）与[[Cost of Ownership|所有权成本]]（COO）标准在全产业链的推广，促使中小设备商建立了严格的质量与[[Reliability|可靠性]]度量体系，将设备在役平均无故障工作时间（MTBF）提升数倍，并有效遏制了制造过程中的随机缺陷蔓延。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, p. 735)]]
>
> *Implementing statistical process control across supplier facilities enabled suppliers to monitor tool performance objectively, eliminate process variations, and significantly boost mean time between failures (MTBF).*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为任何现实系统均存在内在的随机变异（偶然原因）与外在的扰动变异（异常原因）；科学管理的本质是通过统计界限区分两者，避免在受控系统中过度调整（Overcontrol/Tampering）或对异常系统视而不见。
> - **研究者角色** 负责建立合理的子组抽样方案（Rational Subgrouping）、选择适配的统计分布模型、标定规范公差与控制界限，并引导一线团队排查异常根因。
> - **有效性标准** 控制图的灵敏度（低第 II 类错误率/漏报率）、警报的虚警率（控制在正态分布下的 $\alpha = 0.27\%$ 水平）以及过程能力指数的稳定性。
> - **不声称回答的问题** 不直接提供变异产生的物理或社会学机制（需配合因果图或试验设计），不能替代对价值目标与质量标准本身的合理性论证。

> [!method-stack] 方法层级
> - **研究设计** 纵向时间序列监测设计、准实验[[Process Tracing|过程追踪]]设计、全面质量改进干预评估。
> - **数据收集** 自动化传感器在线量测、高频标准化抽样测验、定期行政考勤与业务记录汇总。
> - **分析方法** 休哈特控制图构建、八大判异准则检验（Western Electric Rules）、工序能力比率估计。
> - **辅助技术** 有理[[Stratified Sampling|分层抽样]]、Box-Cox 偏态数据变换、指数加权移动平均（EWMA）、累积和控制图（CUSUM）。

---

## 研究程序

> [!proc] 通用程序
> 1. **确定关键控制特性（CTQ）** 识别对最终产品或教育质量具有决定性影响的关键过程指标（如刻蚀均匀性、学生基础读写能力周测分）。
> 2. **制定合理子组抽样方案** 遵循“组内变异仅由偶然原因引起，组间差异反映异常原因”的原则进行时序抽样（如每班每周抽取 5 份样本）。
> 3. **计算基线统计量与试探控制界限** 收集处于典型运行状态下的 20–25 组样本，[[Center of Calculation|计算中心]]线（CL）及上下控制界限（UCL / LCL）。
> 4. **剔除异常并建立标准控制图** 检验并消除初始阶段由特殊原因引起的失控点，重新拟合得到稳态控制界限。
> 5. **实时监控与判异干预** 将后续时序数据点连线绘制入图，依据越界规则或趋势规则判断是否发生异常，并在失控时启动根因排查。
> 6. **过程能力评估与持续改进** 在过程稳定受控的前提下，计算 $C_p$ 与 $C_{pk}$ 指数，评估当前过程满足外部公差标准的能力。

---

### 量化方法模块

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 按时间先后顺序排列的子组计量型连续数据（如 $k$ 个子组，每组容量 $n$）或计数型离散数据。
> - **样本与单位** 连续 $k \ge 20$ 个子组，典型子组容量 $n \in [3, 5]$。
> - **变量或指标** 子组样本均值 $\bar{X}$、极差 $R$、标准差 $S$、不合格品率 $p$、单位缺陷数 $u$。
> - **模型与控制界限** 基于正态分布假定（$\mu \pm 3\sigma$），理论上覆盖 99.73% 的自然变异区间。
> - **诊断与检验** 正态性检验（Shapiro-Wilk）、自相关诊断（Durbin-Watson）及过度拟合检验。

> [!formula-step] 公式步骤　休哈特均值-极差控制图（$\bar{X}-R$ 图）界限计算
> $$\begin{aligned} \text{UCL}_{\bar{X}} &= \bar{\bar{X}} + A_2 \bar{R} \\ \text{CL}_{\bar{X}} &= \bar{\bar{X}} \\ \text{LCL}_{\bar{X}} &= \bar{\bar{X}} - A_2 \bar{R} \end{aligned} \qquad \begin{aligned} \text{UCL}_R &= D_4 \bar{R} \\ \text{CL}_R &= \bar{R} \\ \text{LCL}_R &= D_3 \bar{R} \end{aligned}$$
>
> **这个公式在做什么** 利用各子组均值的总均值 $\bar{\bar{X}}$ 作为中心线，利用平均极差 $\bar{R}$ 乘以常数系数 $A_2$（由样本容量 $n$ 决定）推算 $3\sigma$ 统计波动边界，建立均值控制图；同理利用系数 $D_3, D_4$ 构建极差波动控制图。
>
> **符号说明**
> - $\bar{\bar{X}}$：全部 $k$ 个子组均值的总平均值，反映过程的中心位置。
> - $\bar{R}$：全部 $k$ 个子组极差的平均值，反映过程固有的偶然变异离散度。
> - $A_2, D_3, D_4$：基于标准正态抽样理论预先制表的无偏修正控制图系数（例如 $n=5$ 时，$A_2=0.577, D_3=0, D_4=2.114$）。
>
> **数学直觉** 极差 $\bar{R}$ 是组内标准差 $\sigma$ 的无偏估计量替代（$\hat{\sigma} = \bar{R} / d_2$）。由于[[Central Limit Theorem|中心极限定理]]，即使总体微弱偏态，子组均值 $\bar{X}$ 的分布也迅速逼近正态分布，因此其[[Standard Error|标准误]]为 $\sigma / \sqrt{n} = \bar{R} / (d_2 \sqrt{n}) = A_2 \bar{R}$，$\pm 3$ 倍标准误自然构成 $99.73\%$ [[Confidence Interval|置信区间]]的统计边界。
>
> **结果怎么读** 当样本点落在 $[\text{LCL}, \text{UCL}]$ 之间且无非随机排列（如连续 9 点在中心线同侧）时，过程处于统计受控状态（In Control）；任一点超出界限即表明存在需要排查的“异常原因”（Out of Control）。
>
> **注意事项** 必须先检验极差控制图（$R$ 图）是否受控；若极差图失控（说明过程变异不稳定），则均值控制图（$\bar{X}$ 图）的界限失去数学有效性。

> [!formula-step] 公式步骤　过程能力指数（$C_p$ 与 $C_{pk}$）计算
> $$C_p = \frac{\text{USL} - \text{LSL}}{6\hat{\sigma}}, \qquad C_{pk} = \min\left(\frac{\text{USL} - \mu}{3\hat{\sigma}}, \; \frac{\mu - \text{LSL}}{3\hat{\sigma}}\right)$$
>
> **这个公式在做什么** 比较外部设定的技术公差范围（Specification Width, $\text{USL}-\text{LSL}$）与过程固有的自然波动范围（$6\hat{\sigma}$），计算在过程稳定受控状态下满足质量规格的裕度水平。
>
> **符号说明**
> - $\text{USL}, \text{LSL}$：外部公差上限（Upper Specification Limit）与公差下限（Lower Specification Limit）。
> - $\mu, \hat{\sigma}$：过程的总平均值与估计的固有标准差（$\hat{\sigma} = \bar{R} / d_2$）。
> - $C_p$：潜在过程能力指数（假定中心无偏移）。
> - $C_{pk}$：考虑中心偏移后的实际工序能力指数。
>
> **数学直觉** $C_p$ 衡量“分布宽度够不够窄”，$C_{pk}$ 衡量“在考虑中心偏离目标值时，距离最近公差边缘的安全裕度是否足够”。
>
> **结果怎么读**
> - $C_{pk} \ge 1.33$：过程能力充分（在半导体高精制造中通常要求 $C_{pk} \ge 1.67$ 或达到 $6\sigma$ 水平）。
> - $1.00 \le C_{pk} < 1.33$：过程能力勉强合格，需密切监控。
> - $C_{pk} < 1.00$：过程能力不足，必然产生超出公差的缺陷品，必须立即进行技术或系统改进。
>
> **注意事项** 计算过程能力指数的前提是过程必须已经处于统计受控状态（即控制图上无异常点）；对未受控过程计算 $C_{pk}$ 无任何统计意义。

> [!software-impl] 软件实现
> - **数据处理** 导入按时间排序的测度数据，按 `subgroup_id` 进行分组聚合计算均值与极差。
> - **推荐软件** R（`qcc`、`SixSigma`）、Python（`scipy.stats`、`matplotlib`）、Minitab、JMP、SPSS。
> - **核心包或命令**
>   - R: `library(qcc); obj <- qcc(data, type="xbar", std.dev="UWAVE-R"); process.capability(obj, spec.limits=c(LSL, USL))`
>   - Python: 运用 `scipy.stats` 计算 $\bar{\bar{X}}$ 及控制限，绘制交互式时序图表。
> - **报告标准** 明确报告子组容量 $n$、总子组数 $k$、中心线与控制限数值、检验出的失控准则编号、估计的标准差 $\hat{\sigma}$ 及计算得到的 $C_p / C_{pk}$ 值。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用** 高端装备中试工艺参数认证、晶圆及高精零部件连续加工监控、教育系统中跨学期/跨周学生[[Academic Achievement|学业成绩]]的纵向稳定性监测与异常预警。[[Argument_Grindley_1994_JPAM|(Grindley et al., 1994, pp. 735, 746)]]
> - **谨慎使用** 样本极度偏态（需做非正态转换或改用秩和控制图）、时序数据存在强一阶自相关（需采用残差控制图或 ARIMA-SPC 整合模型）。
> - **不适合使用** 一次性小样本项目评估、完全无重复生产的孤立定制任务、缺乏客观量化指标的主观体验评价。

---

## 局限性

> [!method-limits] 方法局限
> - **偏误来源** 抽样不当导致组内混入系统性变异、对非正态数据机械套用正态常数引发虚警率激增。
> - **适用边界** 控制图只能判定“系统是否异常”，无法自动推断“异常由何产生”，必须配合物理失效分析或一线定性[[Fieldwork|实地调查]]。
> - **误用风险** “过度调整陷阱”——管理者将正常的偶然波动误判为系统故障而频繁调整工艺参数，反而人为向系统注入额外变异（戴明漏斗实验）。
> - **补救方式** 采用严格的有理子组抽样法则，结合因果鱼骨图（Ishikawa Diagram）与实验设计（[[Department of Energy|DOE]]）开展后续根因溯源。

---

## 实证数据与标杆案例

> [!ref-table]- 实证研究标杆数据（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Macher_1998_CMR\|Macher et al. (1998)]] | 1980–1996 年全球数十座先进商业与内部晶圆制造厂（伯克利 [[Competitive Semiconductor Manufacturing Program\|CSM 项目]]） | [[Industrial Benchmarking\|产业标杆分析]]与产线微观追踪 | 出厂每百万缺陷数（PPM）、0.7–0.9 微米 CMOS 逻辑缺陷密度、晶圆探针良率 | 1980–1992 年美国商用半导体缺陷率由 **780 PPM 压降至 <100 PPM**；0.7–0.9 微米逻辑缺陷密度由 1990 年的 **1.3 个/$\text{cm}^2$ 降至与日本相当（~0.4）**；逻辑制程平均探针良率追平日本（**60% vs 60%**） | 微观晶圆产线归一化实测数据（原文报告） | 证实全面推行 SPC 与过程控制使逻辑制程制造能力追平日本，推翻 DRAM 是尖端制造唯一驱动器的假设 |
> | [[Argument_Grindley_1994_JPAM\|Grindley et al. (1994)]] | 1988–1992 年 [[Sematech]] 联盟资助的 100 余家上游制造装备与材料供应商 | 联盟项目评估与纵向追踪 | SPC/[[Total Quality Management\|TQM]] 培训完成率、在役设备平均无故障工作时间（MTBF） | 联盟资助 **90%+** 合作供应商完成 SPC 质量体系培训，关键工艺设备 MTBF **提升数倍**，美日装备全球市场份额逆转为 **51% vs 41%** | 描述性统计与产业追踪档案（原文报告） | 揭示将 SPC 推广至设备供应链是提升系统级在役[[Reliability\|可靠性]]的关键抓手 |

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Total Quality Management]] | 理论 | 为 SPC 提供全员参与、持续改进与基于数据决策的组织治理哲学支撑。 |
> | [[Industrial Benchmarking]] | 补充方法 | 结合微观晶圆厂标杆分析，跨期度量 SPC 导入前后缺陷密度与探针良率的收敛轨迹。 |
> | [[Cost of Ownership]] | 补充方法 | SPC 提升设备运行[[Reliability\|可靠性]]（MTBF），直接降低 COO 模型中的停机与缺陷损失。 |
> | [[Time Series Design]] | 前置方法 | 提供时序数据采集、平稳性检验与自相关建模的基础时间序列[[Analytic Framework\|分析框架]]。 |
> | [[Longitudinal Study]] | 补充方法 | 在教育研究中将 SPC 控制图作为纵向追踪学生与学校表现动态波动的分析工具。 |

---

## 使用此方法的研究

> [!evidence-grid] [[Correlational Research|相关研究]]索引
> - [[Argument_Grindley_1994_JPAM|Grindley et al. (1994)]] — 详述 [[Sematech]] 推动半导体制造全产业链采用 SPC 工具进行设备中试验证与[[Reliability|可靠性]]（MTBF）提升。
> - [[Argument_Macher_1998_CMR|Macher et al. (1998)]] — 借助加州大学伯克利分校 [[Competitive Semiconductor Manufacturing Program|CSM]] 项目微观标杆数据，实证论证美企通过 SPC 与 [[Total Quality Management|TQM]] 将缺陷率压降至 100 PPM 以下并在先进逻辑制程中实现良率追赶。
