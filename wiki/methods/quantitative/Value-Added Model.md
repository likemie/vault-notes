---
title: Value-Added Model
aliases:
  - 增值评价模型
  - 教师增值模型
  - 学校增值模型
  - Value-Added Modeling
summary: "一种基于纵向追踪测验数据的教育统计计量方法，通过控制学生以往学业基线、家庭社会经济背景及学校班级特征等协变量，剥离生源差异以估计单个学校或教师对学生学业进步的净贡献效应。作为规制型治理中基于测验的问责制核心技术构件，该模型在政策实践中面临测量误差、抽样波动、非随机分班偏误与因果识别假定脆弱性的学理批评与法理争议。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 32
method_related_level: 3
method_related_stars: "💎"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - theme/educational-evaluation
  - theme/accountability
  - theme/standardized-testing
  - theme/psychometrics
related_concepts:
  - "[[Learning Gain]]"
  - "[[Academic Achievement]]"
  - "[[Variable]]"
  - "[[Unit of Analysis]]"
  - "[[School Effectiveness]]"
  - "[[Epistemology]]"
  - "[[Internal Validity]]"
  - "[[Construct Validity]]"
  - "[[Social-Emotional Learning]]"
  - "[[Socioeconomic Status]]"
  - "[[Dependent Variable]]"
  - "[[Class Size]]"
  - "[[Reliability]]"
  - "[[Counterfactual]]"
related_theories:
  - "[[Policy Instrumentation Theory]]"
related_methods:
  - "[[Hierarchical Linear Model]]"
  - "[[Random-Effects Model]]"
  - "[[Confidence Interval]]"
  - "[[Fixed-Effect Model]]"
  - "[[Standard Error]]"
  - "[[Covariate Adjustment]]"
  - "[[Analysis of Covariance]]"
  - "[[Intraclass Correlation Coefficient]]"
  - "[[Pearson Product-Moment Correlation]]"
  - "[[Pre-test and Post-test]]"
  - "[[Sample Size Determination]]"
  - "[[Classroom Observation]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Random Assignment]]"
  - "[[Time Series Design]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[Race to the Top]]"
related_arguments:
  - "[[Argument_Verger_2019_Discourse]]"
confidence: high
status: draft
created: 2026-10-21
updated: 2026-10-29
---

---

> [!def] Value-Added Model
> [[Learning Gain|增值评价]]模型（Value-Added Model, VAM）是一类依托纵向追踪测试数据，利用回归分析或[[Hierarchical Linear Model|多层线性模型]]控制学生先期[[Academic Achievement|学业成就]]、个人背景及学校环境[[Variable|变量]]，旨在隔离出特定教师、学校或教育干预对学生学业成长净贡献的教育统计计量方法。在规制型教育治理中，增值模型被广泛作为将标准化考试结果与教师人事评价、绩效激励或学校等级问责直接绑定的量化评估工具。[[Argument_Verger_2019_Discourse|(Verger et al., 2019, pp. 253, 256–257)]]

> [!method-scope] 方法范围
> - **研究对象** 学生跨学年标准化测验成绩轨迹、学生家庭背景协变量、班级生源构成及教师任教匹配数据。
> - **问题类型** 测度特定教育供给者（教师或学校）在既定期限内带来的平均学业增长效应，回答绩效归因与效能增益问题。
> - **[[Unit of Analysis|分析单位]]** 嵌套于班级和学校的学生个体观测值；核心估计参数聚焦于教师或学校层面的固定或[[Random-Effects Model|随机效应]]。
> - **输出形式** 教师或[[School Effectiveness|学校效能]]增值系数（Value-Added Score）、年级百分位排位、增值[[Confidence Interval|置信区间]]及达标分类标签。

> [!citation-card] 增值模型在高利害教师评价中的扩散
> 将学生学业表现与教师评价挂钩的技术受到 2011 年《[[Race to the Top|力争上游]]》计划的强力激励，并在各州和城市学区广泛应用；其中，增值模型因其在大规模政策中的普遍采纳而尤为突出。（[[Argument_Verger_2019_Discourse|Verger et al., 2019, p. 256]]）
>
> *Techniques that tie student performance to teacher evaluations, as incentivized by the Race to the Top Act of 2011, have also emerged. Among them, value-added models feature prominently given its widespread use by several states and urban districts.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 假定学生的学业成长具有可测量性与历时性累积性，且教育组织与教师个体的效能可以通过控制外生混杂[[Variable|变量]]予以统计分离。
> - **研究者角色** 依赖计量经济学家与心理测量专家的技术决策，包括协变量选择规则、[[Fixed-Effect Model|固定效应]]与[[Random-Effects Model|随机效应模型]]设定、跨年度收缩估计（Shrinkage Estimation）以及垂直量表标定。
> - **有效性标准** [[Internal Validity|内部效度]]依赖于非随机分班能否被充分控制（Selection on Observables）；统计结论效度关注年际波动率、[[Standard Error|标准误]]大小与排位稳定性；[[Construct Validity|构念效度]]取决于标准化测验能否完整代表课程目标。
> - **不声称回答的问题** 单纯的增值模型无法解释优异增值背后的具体课堂教学机制，也不能脱离标准化测验覆盖的狭隘学科范围去评定德育、审美或[[Social-Emotional Learning|社会情感能力]]。

> [!method-stack] 方法层级
> - **研究设计** 观察性纵向追踪面板设计（Longitudinal Panel Design）或准实验[[Covariate Adjustment|协变量调整]]设计。
> - **数据收集** 连续多学年的全员标准化统一测验成绩（如 3–8 年级阅读与数学）、学籍管理系统与人事行政档案。
> - **分析方法** 协变量调整多元线性回归（[[Analysis of Covariance|ANCOVA]]）、固定效应面板回归、[[Hierarchical Linear Model|分层线性模型]]（HLM）及经验贝叶斯收缩估计（Empirical Bayes Shrinkage）。
> - **辅助技术** 垂直尺度等值转换（Vertical Scaling）、多重插补处理缺失值、聚类稳健标准误与学生-教师非等权重匹配算法。

---

> [!proc] 通用程序
> 1. 构建跨学年度的学生-教师-学校纵向链接数据库，核验测验垂直量表可比性。
> 2. 确定基线[[Academic Achievement|学业成绩]]与学生个人背景、家庭[[Socioeconomic Status|社会经济地位]]等控制[[Variable|变量]]。
> 3. 拟定统计模型结构，分解学生学业成长的各层级方差成分，估计单位效能系数。
> 4. 应用贝叶斯经验收缩方法调控小样本班级的抽样波动，生成稳健效能估计值与[[Confidence Interval|置信区间]]。
> 5. 开展模型诊断与敏感性分析，评估不同模型设定对教师等级分类的变动影响。

> [!method-stack] 数据、变量与模型
> - **数据结构** 纵向嵌套面板数据（学生跨年份观测重复测量，嵌套于班级、教师与学校层级）。
> - **样本与单位** 参与跨年标准化统考的全体学生记录，以任课教师或学校为核心聚合单位。
> - **变量或指标** 
>   - [[Dependent Variable|因变量]]（$Y_{ijt}$）：$t$ 年学生 $i$ 在教师 $j$ 班级内的标准化期末测试成绩。
>   - 先期基线变量（$Y_{i,t-1}$）：学生在前一学年同一学科或相关学科的统考成绩。
>   - 个体协变量（$\mathbf{X}_{ijt}$）：家庭社会经济背景、少数族裔身份、特殊教育需求及缺勤率。
>   - 班级协变量（$\mathbf{C}_{jt}$）：班级平均基线成绩、[[Class Size|班级规模]]及同伴背景分布。
>   - 效能参数（$\theta_j$）：教师 $j$ 对学生学业增值的独特影响。
> - **模型与统计量** [[Covariate Adjustment|协变量调整]]混合效应模型与限制性极大似然估计（REML）。
> - **诊断与检验** 残差正态性检验、[[Intraclass Correlation Coefficient|组内相关系数]]（ICC）测算及年际稳定性[[Pearson Product-Moment Correlation|皮尔逊相关]]系数。

> [!formula-step] 公式步骤　基础协变量调整增值回归模型
> $$Y_{ijt} = \alpha + \beta Y_{i,t-1} + \boldsymbol{\gamma}' \mathbf{X}_{ijt} + \boldsymbol{\delta}' \mathbf{C}_{jt} + \theta_j + \varepsilon_{ijt}$$
>
> **这个公式在做什么** 控制学生往年先期基线水平与外生社会经济背景后，将剩余的班级平均学业超额增长归因于教师效能。
>
> **符号说明**
> - $Y_{ijt}$：学生 $i$ 在第 $t$ 年的标准化测验期末成绩。
> - $Y_{i,t-1}$：学生 $i$ 在第 $t-1$ 年的[[Pre-test and Post-test|前测]]成绩（学业基线）。
> - $\theta_j$：教师 $j$ 的净效能增值效应估计值。
> - $\varepsilon_{ijt}$：学生层面的随机误差项。
>
> **数学直觉** 假定不同教师面对的生源条件存在客观差异，通过线性回归剥离先期基础与背景因素所能预测的期望值，将实际表现超出期望表现的净增量视为教师贡献。
>
> **结果怎么读** $\theta_j > 0$ 表示该教师带教学生的平均增长超出统计预期；$\theta_j < 0$ 表示平均增长低于具有相同基线与背景特征学生的统计预期。
>
> **注意事项** 假定生源向不同教师的分配完全取决于模型中纳入的观察变量（Selection on Observables）；若存在未被测量的家长择班或校内分流因素，$\theta_j$ 将包含严重的选择性遗漏变量偏误。

> [!formula-step] 公式步骤　经验贝叶斯收缩估计（Empirical Bayes Shrinkage）
> $$\theta_j^* = \lambda_j \hat{\theta}_j + (1 - \lambda_j) \bar{\theta}$$
>
> **这个公式在做什么** 对[[Sample Size Determination|样本量]]较小或估计误差较大的教师增值系数向总体均值实施自适应平滑收缩，降低极端抽样偶然性。
>
> **符号说明**
> - $\hat{\theta}_j$：教师 $j$ 的原始增值参数估计值。
> - $\bar{\theta}$：全样本教师增值的总体平均水平（通常标准化为 0）。
> - $\lambda_j$：[[Reliability|信度]]收缩权重因子，取决于估计值抽样方差与教师间真实方差的比例（$\lambda_j = \frac{\sigma_\theta^2}{\sigma_\theta^2 + \text{SE}_j^2}$）。
>
> **数学直觉** 针对带班人数较少或测试天数异常的教师，原始估计往往具有较大的测量噪声，模型自动给予其较低权重并拉向总体平均值，以防止样本量小导致误判。
>
> **结果怎么读** $\lambda_j$ 接近 1 时，表明样本充分、估计精确，保留其原始高分或低分；$\lambda_j$ 接近 0 时，估计受噪声主导，自动调整为中庸均值。
>
> **注意事项** 经验贝叶斯虽然能够降低均方误差，但在高利害解聘评估中可能引发公平性质疑，因为小样本教师的极端高表现和极端低表现均会被机械削弱。

> [!software-impl] 软件实现
> - **数据处理** 依托清洗流程匹配跨年统一学籍代码（Student ID）与教师任职记录，剔除转校生与缺考样本。
> - **推荐软件** R、Stata、Python。
> - **核心包或命令** R 语言采用 `lme4::lmer`、`lavaan` 及专门的 `vam` 工具包；Stata 采用 `mixed`、`areg` 或 `xtreg`；Python 采用 `statsmodels.regression.mixed_linear_model`。
> - **实现流程** 
>   1. 数据集按学生标识构建多期面板结构。
>   2. 拟合基准[[Fixed-Effect Model|固定效应]]或随机截距模型，提取固定协变量系数与残差方差。
>   3. 提取[[Random-Effects Model|随机效应]] Best Linear Unbiased Predictions (BLUPs) 并计算[[Standard Error|标准误]]。
>   4. 导出教师增值分值与置信区间，开展百分位排序。
> - **报告标准** 完整呈现模型各层级方差分量、组内相关系数、协变量效应大小、样本损耗率及跨年份排位稳定度相关系数。

---

> [!method-fit] 适用判断
> - **适合使用** 具备连续全员历时性统一测验、大规模集中数据库及高精度学籍关联系统的区域教育系统；用于宏观研究政策干预的群体性增值效果，或作为校本教学反思的内部参考。[[Argument_Verger_2019_Discourse|(Verger et al., 2019, pp. 253, 256)]]
> - **谨慎使用** 用于个体教师的形成性指导时，必须充分附带[[Confidence Interval|置信区间]]，并结合[[Classroom Observation|课堂观察]]与同行评议等多元质性证据。
> - **不适合使用** 严禁脱离置信区间将单一单年增值分数直接用于教师解聘、薪资剥夺或关闭学校等不可逆的高利害行政裁决；不适用于跨学段缺乏垂直量表对齐的孤立测验。[[Argument_Verger_2019_Discourse|(Verger et al., 2019, pp. 256, 260–261)]]

---

> [!method-limits] 方法局限
> - **年际波动剧烈与[[Reliability|信度]]赤字** 实证研究显示教师增值排位的年际相关系数普遍处于 0.20 至 0.40 的低水平，同一教师在相邻年份从前 10% 跌落至后 10% 的概率高达 20% 以上，存在极高分类假阳性与假阴性风险。（Baker et al., 2013）
> - **非随机分班与混杂偏差** 优秀学生与问题学生在学校内部往往存在隐性聚类（如家长选老师或校方策略性配班），[[Covariate Adjustment|协变量调整]]无法完全消除未观测的心理与动机差异。
> - **教学窄化与应试操纵反冲** 将 VAM 绑定高利害问责诱发坎贝尔定律效应，促使教师将教学精力和时间收缩至易测知识点，甚至引发集体修改答卷等系统性舞弊行为。（Amrein-Beardsley & Holloway, 2017）
> - **补救方式** 采用多年度移动平均值（3 年以上）平滑单年波动，引入多元评价矩阵，严格限制 VAM 在人事决定中的权重比例。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Policy Instrumentation Theory]] | 理论 | 政策工具社会学指出增值模型是典型的技术化治理装置，借助数学客体化掩盖了问责政治决断。 |
> | [[Hierarchical Linear Model]] | 前置方法 | 分层线性模型提供了处理学生嵌套于班级和学校数据的方差分解统计数学基础。 |
> | [[Randomised Controlled Trials]] | 替代方法 | 随机对照试验通过[[Random Assignment\|随机分配]]直接解决[[Counterfactual\|反事实]]问题，是检验干预因果效应的黄金标准，而增值模型属于非实验替代手段。 |
> | [[Time Series Design]] | 补充方法 | 多时点间断时间序列分析可与增值模型结合，评估宏观政策干预对学业增长轨迹的长周期动态影响。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Verger_2019_Discourse|Verger et al. (2019)]] — 考证增值模型作为量化治理工具在美国《[[Race to the Top|力争上游]]》计划、英格兰及意大利绩效改革中的扩散历程与引发的社会反弹。
