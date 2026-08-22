---
title: Time Series Design
aliases:
  - 时间序列设计
  - time series quasi-experiment
  - interrupted time series
  - ITS
  - 间断时间序列设计
summary: "准实验设计的重要范式，通过在干预前后开展多次等间隔重复测量并拟合分段回归模型，以自身历史演进趋势为反事实基准检验即时水平跃升与斜率变化。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 29
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/experimental-design
  - method/quasi-experimental-design
  - method/quantitative
  - time-series
  - causal-inference
related_concepts:
  - "[[Counterfactual]]"
  - "[[Theories of Policy Change]]"
  - "[[Standard Error]]"
  - "[[Pre-test and Post-test]]"
  - "[[Causality]]"
  - "[[Epistemology]]"
  - "[[Postpositivism]]"
  - "[[Order Effects]]"
  - "[[Hawthorne Effect]]"
  - "[[Dependent Variable]]"
  - "[[Variable]]"
  - "[[Statistical Significance]]"
  - "[[Hypothesis]]"
related_theories:
  - "[[Campbellian Validity Framework]]"
related_methods:
  - "[[Quasi-Experimental Designs]]"
  - "[[Random Assignment]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Single-Case Design]]"
  - "[[Single-Subject Design]]"
  - "[[Regression Discontinuity Design]]"
  - "[[Trend Study]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[What Works Clearinghouse]]"
  - "[[Top Institute for Evidence-Based Education Research]]"
  - "[[Gaokao]]"
  - "[[Home Visiting Evidence of Effectiveness]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
  - "[[Argument_QiMei_2015_EducationalResearchMethods]]"
  - "[[Argument_Wadhwa_2024_RER]]"
  - "[[Argument_Hitchcock_2015_JBE]]"
confidence: high
status: active
created: 2026-06-25
updated: 2026-08-21
---

# Time Series Design

---

## 定义

> [!def] 方法定义
> **时间序列设计（Time Series Design）**，特别是**间断时间序列设计（Interrupted Time Series Design, ITS）**，是指对同一个非随机取样的实验组（或自然行政单位），在接受特定教育干预或政策实施**之前与之后分别开展多次连续等间隔的重复测量**，通过对比干预前后数列变化轨迹来判定干预因果效应的[[Quasi-Experimental Designs|准实验设计]]方法([[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, pp. 328–331]]; [[Argument_QiMei_2015_EducationalResearchMethods|齐梅, 2015, Ch. 4]])。
>
> 其核心统计特征在于：通过分段线性回归（Segmented Linear Regression）将干预前的长期历史趋势外推为[[Counterfactual|反事实]]（Counterfactual）基准线，进而精准分解出干预引发的**即时截距水平跃升（Level Change）**与**长期演化斜率变动（Slope Change）**。在美国教育部 [[What Works Clearinghouse|WWC]] 审查规程中，符合标准的 ITS 设计被赋予 2 级因果审查待遇，对应“有保留达标（Meets Standards With Reservations）”或 ESSA 2015 [[Top Institute for Evidence-Based Education Research|TIER]] 2 中等证据资质([[Argument_Wadhwa_2024_RER|Wadhwa et al., 2024, pp. 8–10]])。

> [!method-scope] 方法范围
> - **研究对象** 宏观教育[[Theories of Policy Change|政策变革]]、学区管理条例修订、全校性行为干预系统（PBIS）、考试评价制度改革、或连续追踪的课堂教学方案。
> - **问题类型** 评估干预是否引起了时间序列趋势的根本性断裂；检验效应是即时爆发、渐进积累还是逐步衰减。
> - **分析单位** 按等间隔时间点（周、月、季度、学期或学年）聚合的班级、学校或学区均值指标。
> - **输出形式** 分段回归方程参数估计值、截距变化量 $\beta_2$、斜率变化量 $\beta_3$、自相关校正后[[Standard Error|标准误]]及时间序列趋势折线图。

> [!citation-card]- 关键定义
> 时间序列设计通过在干预前后引入一系列连续测量，使受试者成为自身的反事实控制。多次[[Pre-test and Post-test|前测]]建立了稳定的发展基线，有效剥离了自然成熟与已有趋势的假象，从而在缺乏[[Random Assignment|随机分配]]的情况下提供了极其有力的准实验[[Causality|因果推断]]。[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|(Cohen et al., 2011, pp. 328–329)]]
>
> *Interrupted time series designs utilize multiple observations before and after an intervention to project a counterfactual trajectory. By modeling changes in both intercept and slope, ITS distinguishes true intervention effects from secular historical trends and natural maturation.*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **认识论取向** 秉承[[Postpositivism|后实证主义]]动态系统观，承认教育现象随时间自然演化，反对将[[Causality|因果关系]]过度简化为静态单次两点差分（[[Pre-test and Post-test|前测]]—后测）。
> - **因果识别逻辑** 依赖“历史惯性外推”建立[[Counterfactual|反事实]]，假定若无干预发生，干预后的时间序列将完全沿着干预前的趋势线（包含自然成熟与原有演化速度）继续延伸。
> - **与真实验（[[Randomised Controlled Trials|RCT]]）及单被试设计（[[Single-Case Design|SCD]]）的关系** 
>   - 相比组间 RCT，ITS 克服了必须设立平行不处理对照组的伦理与行政限制，尤其适合全员覆盖的宏观政策评估；
>   - 相比个体层面的[[Single-Subject Design|单一被试设计]]（SCD），ITS 是群体/系统层面的宏观时间序列，二者共享相同的“相内密集测量 + 相间趋势对比”逻辑([[Argument_Hitchcock_2015_JBE|Hitchcock et al., 2015, pp. 461–464]])。

> [!method-stack] 方法层级
> - **设计变体** 单组间断时间序列（Single-Group ITS）、控制组间断时间序列（Comparative ITS, C-ITS）、相等时间样本轮换设计（Equivalent Time Samples）、多基线时间序列（Multiple Baseline ITS）。
> - **数据采集** 历史档案行政数据库、等间隔标准化测验、高频出勤与纪律记录系统。
> - **计量分析技术** 分段普通最小二乘回归（OLS）、自回归积分滑动平均模型（ARIMA）、Cochrane-Orcutt / Prais-Winsten 广义自回归纠偏模型、Newey-West 异方差自相关稳健[[Standard Error|标准误]]（HAC）。

---

## 研究程序

> [!proc] 间断时间序列研究标准实施六步规程
> 1. **确定等间隔观测时间轴** 建立干预前后对称或充足的数据采集时间点（通常要求干预前后各至少 3–5 个以上独立时间点）。
> 2. **建立干预前稳定基线趋势** 采集干预前连续数据，检验[[Pre-test and Post-test|前测]]数列的稳定性与历史演进斜率（Slope）。
> 3. **精准记录干预切入时间点（Interruption Point）** 明确界定政策或干预实际落地的明确时间节点，排查实施过渡期（Lag / Transition Phase）。
> 4. **开展干预后持续追踪观测** 在干预发生后继续沿用完全相同的测量工具进行多周期等频度跟踪。
> 5. **构建分段回归统计模型** 运用分段线性回归，同时估计干预带来的即时水平跃升（Level Change）与趋势斜率转变（Trend Change）。
> 6. **实施自相关检验与敏感性排查** 检验 Durbin-Watson 统计量排除一阶序列自相关；对照未受影响的平行学区或控制组排除共时历史事件混杂。

---

### 经典设计亚型与符号模型

> [!framework-table] 时间序列设计四大经典亚型对比（基于 Cohen et al., 2011; 齐梅, 2015）
> | 设计亚型 | 经典符号模型 | 核心机制与控制优势 | 主要效度威胁与防范 | 典型应用情境 |
> |:---|:---:|:---|:---|:---|
> | **单组间断时间序列<br>(Single-Group ITS)** | $O_1 O_2 O_3 O_4 \ \mathbf{X} \ O_5 O_6 O_7 O_8$ | 受试组成为自身对照；多次前测建立动态基线，有效控制成熟与均值回归 | 威胁：**共时历史事件（Co-occurring History）**；防范：查证同期外部政策 | 全校推行新晨读方案对阅读能力的演进影响 |
> | **控制组间断时间序列<br>(Comparative ITS / C-ITS)** | $\frac{O_1 O_2 O_3 O_4 \ \mathbf{X} \ O_5 O_6 O_7 O_8}{O_1 O_2 O_3 O_4 \ \quad\quad \ O_5 O_6 O_7 O_8}$ | 增加平行非等对对照组时间序列；通过双序列差分彻底剥离外部共时历史事件 | 威胁：对照组与干预组的差异性历史事件；防范：选择平行性最优的对照学区 | 某州[[Gaokao\|高考]]改革试点与未改革邻州的历年追踪对比 |
> | **相等时间样本设计<br>(Equivalent Time Samples)** | $X_1 O_1 \ X_0 O_2 \ X_1 O_3 \ X_0 O_4$ | 实验处理 $X_1$ 与常规控制 $X_0$ 在相等时间段交替出现（可采用 ABBA 轮换） | 威胁：**[[Order Effects\|练习效应]]与处理残留污染**；防范：设置充足的重置清洗期 | 两种短期互补课堂教学管理软件的交替测试 |
> | **多基线跨情境时间序列<br>(Multiple Baseline ITS)** | $\begin{aligned} &O O O \ \mathbf{X} \ O O O O O \ &O O O O O \ \mathbf{X} \ O O O \end{aligned}$ | 在不同学校或班级分批次、阶梯式引入干预，通过交错介入点确证因果特异性 | 威胁：处理扩散与外溢效应；防范：物理隔离不同介入试点 | 区域分批次推进数字化教学平台的梯次因果检验 |

---

### 效应反应模式与计量模型

> [!contrast-table] 时间序列干预效应的三大核心反应模式（基于 Cohen et al., 2011, p. 329）
> | 效应反应模式 | 趋势线形态特征 | 参数表现 ($\beta_2, \beta_3$) | 因果与政策含义 |
> |:---|:---|:---|:---|
> | **即时水平跃升型 (Immediate Level Change)** | 干预点处数列突然垂直跳升，但后续斜率与先前平行 | $\beta_2 
eq 0, \beta_3 = 0$ | 干预产生了一次性结构性红利，但未改变长期的自主增长速率。 |
> | **斜率持续演进型 (Sustained Slope Change)** | 干预点处无突变跳升，但后续斜率显著变陡并持续拉开差距 | $\beta_2 = 0, \beta_3 
eq 0$ | 干预重塑了发展机制（如培养了自主阅读习惯），效应随时间累积放大。 |
> | **复合跃升与演进型 (Combined Level & Slope)** | 干预点既出现显著垂直跃升，且后续斜率进一步持续加速上升 | $\beta_2 
eq 0, \beta_3 
eq 0$ | 最理想的政策效应，兼具即时止血提分与长期自我造血发展功能。 |
> | **暂时跃升与衰减型 (Transient Decay)** | 干预初期出现垂直跃升，但后续斜率转为向下并回归原趋势 | $\beta_2 > 0, \beta_3 < 0$ | 提示存在典型的**[[Hawthorne Effect\|霍桑效应]]（新奇效应）**，政策缺乏长效机制。 |

> [!formula-step] 分段线性回归模型（Segmented Linear Regression）
> 间断时间序列的标准双向分段回归模型表达为：
>
> $$Y_t = \beta_0 + \beta_1 \cdot T_t + \mathbf{\beta_2} \cdot D_t + \mathbf{\beta_3} \cdot P_t + \varepsilon_t$$
>
> - **$Y_t$** 在时间点 $t$ 观测到的[[Dependent Variable|结果变量]]聚合均值；
> - **$T_t$** 连续时间[[Variable|变量]]（$T_t = 1, 2, 3, \dots, N$），代表干预前的自然演化时间趋势；
> - **$\beta_1$** 干预前基线斜率（Baseline Slope）；
> - **$D_t$** 虚拟变量（干预前 $D_t = 0$，干预后 $D_t = 1$）；
> - **$\mathbf{\beta_2}$** **即时因果效应（Level Change）**，代表干预引入瞬间截距的跳升幅度；
> - **$P_t$** 干预后持续时间计数变量（干预前 $P_t = 0$，干预后 $P_t = 1, 2, 3, \dots$）；
> - **$\mathbf{\beta_3}$** **斜率变动因果效应（Slope Change）**，代表干预引入后演化斜率相对基线斜率的净变化增量；
> - **自相关校正** 若误差项 $\varepsilon_t$ 存在一阶自相关（$\varepsilon_t = 
ho \varepsilon_{t-1} + u_t$），必须采用 Newey-West HAC 估计或 Prais-Winsten GLS 变换校正[[Standard Error|标准误]]，防范 I 类错误。

---

### 政策与清算体系中的审查标准

> [!framework-table] 循证清算中心（[[What Works Clearinghouse|WWC]] / [[Home Visiting Evidence of Effectiveness|HomVEE]]）对 ITS 的审查规程与门槛（基于 Wadhwa et al., 2024）
> | 审查维度 | WWC / HomVEE 规定技术门槛 | 未达标裁定结果 |
> |:---|:---|:---|
> | **因果设计评级** | **2 级（明确规程）**；最高评定为 **Meets Standards With Reservations** 或 ESSA [[Top Institute for Evidence-Based Education Research\|TIER]] 2 | 无法单独支撑 WWC 一级最高认证（Tier 1 无保留达标）。 |
> | **时间点数量底线** | 要求干预前与干预后必须分别具备 **至少 3–5 个以上等间隔独立观测点** | 若时间点不足，退化为普通单组前后测，直接裁定为未达标（Does Not Meet）。 |
> | **趋势与自相关建模** | 必须采用分段回归、ARIMA 或广义最小二乘法显式建模时间趋势并校正序列相关 | 若仅比较前后平均值而忽略时间趋势，裁定为方法学不合格。 |
> | **排除共时混杂干预** | 必须论证在干预切入时间点没有发生其他足以解释效应的共时重大政策或外部冲击 | 若存在未控制共时事件，因果归因失效。 |

---

## 适用场景

> [!fit-grid] 适用判断
> - **适合使用** 评估全州或全学区范围内的宏观课程改革与法规变更；全校推行统一的教学技术系统；拥有连续多年的稳定标准化考试档案数据（Administrative Panel Data）；无法设立随机对照组但能获得高频历史[[Pre-test and Post-test|前测]]的自然情境。
> - **谨慎使用** 观测时间过长导致历史混杂事件概率剧增；测量工具在时间序列中发生版本更迭（测试工具漂移）。
> - **不适合使用** 仅有 1–2 个离散时间点的数据；干预时间点模糊、渐进渗透且无法精确定位切入时期的方案。

---

## 局限性

> [!method-limits] 效度威胁、偏误来源与误用风险
> - **共时历史事件混杂（Co-occurring History Threat）** 单组 ITS 最根本的软肋：若干预推行的同时恰逢新校长上任或财政注资，分段回归无法在数理上区分哪个是真正原因（需借助 C-ITS 对照组缓解）。
> - **测量工具漂移与敏感化（Instrumentation & Testing）** 高频重复测试可能引入[[Order Effects|练习效应]]、疲劳效应或测验难度微调带来的虚假波动。
> - **自相关导致的假阳性显著（Autocorrelation Bias）** 时间序列数据天然存在相邻点高度相关性，若直接套用普通 OLS 回归，将严重低估[[Standard Error|标准误]]，导致原本不显著的 $\beta_2, \beta_3$ 呈现出虚假的[[Statistical Significance|统计显著性]]。
> - **延迟反应与模型误设（Lagged Effects & Model Misspecification）** 若真实干预需要 3 个月才起效，而研究者[[Hypothesis|假设]]即时跳升，可能将真实的渐进斜率误判为无效果。

---

## 相关理论与方法

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Quasi-Experimental Designs]] | 母类方法 | ITS 是准实验设计中控制成熟与历史演变最强有力的亚型之一。 |
> | [[Single-Case Design]] | 孪生方法 | SCD 是微观个体层面的密集时间序列，二者共享相内测量与相间对比逻辑。 |
> | [[Quasi-Experimental Designs\|断点回归设计（RDD）]] | 关联设计 | [[Regression Discontinuity Design\|RDD]] 基于评价值（Score）断点，ITS 基于时间（Time）断点，共享局域因果跳跃识别逻辑。 |
> | [[Campbellian Validity Framework]] | 理论基础 | 提供 ITS 排查成熟、历史、测验与均值回归等效度威胁的系统框架。 |
> | [[Causality]] | 核心概念 | ITS 通过历史轨迹外推的[[Counterfactual\|反事实]]模型确立概率性因果关系。 |
> | [[What Works Clearinghouse]] | 评价机构 | 为 ITS 建立了包含时间点底线与自相关校正的独立审查标准。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al. (2011)]] — 详析间断时间序列设计的符号模型、[[Trend Study|趋势分析]]、即时跃升与延迟演进模式及效度控制机制(Ch. 16, pp. 328–331)。
> - [[Argument_Wadhwa_2024_RER|Wadhwa et al. (2024)]] — 比较 12 所清算中心对 ITS 因果设计的审查规程（ITS=2），详述 [[What Works Clearinghouse|WWC]] 与 [[Home Visiting Evidence of Effectiveness|HomVEE]] 对时间点数量与自相关建模的技术标准(pp. 8–11)。
> - [[Argument_QiMei_2015_EducationalResearchMethods|齐梅 (2015)]] — 系统阐释单组时间序列、控制组时间序列与相等时间样本轮换设计在教育教学实验中的操作流程(Ch. 4)。
> - [[Argument_Hitchcock_2015_JBE|Hitchcock et al. (2015)]] — 论证群体级间断时间序列与个体级单一被试实验（[[Single-Case Design|SCD]]）在因果[[Counterfactual|反事实]]推断上的同构逻辑(pp. 461–464)。
