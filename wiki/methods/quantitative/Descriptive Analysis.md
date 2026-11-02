---
title: Descriptive Analysis
aliases:
  - 描述性分析
  - 描述统计
  - descriptive statistics
  - 描述性统计分析
summary: "量化研究数据分析的基础步骤，通过集中趋势、离散程度与分布形态刻画样本整体图景，并在科学学与教育学中作为探索经验规律与提出因果假设的前提基准"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 23
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/statistical
  - quantitative-research
  - data-analysis
related_concepts:
  - "[[Variable]]"
  - "[[Dependent Variable]]"
  - "[[Independent Variable]]"
  - "[[Construct]]"
  - "[[Unit of Analysis]]"
  - "[[Causality]]"
  - "[[Internal Validity]]"
  - "[[External Validity]]"
related_theories: []
related_methods:
  - "[[Quantitative Research]]"
  - "[[Survey Research]]"
  - "[[Experimental Research]]"
  - "[[Correlational Research]]"
  - "[[Non-intervention Research]]"
  - "[[Statistical Significance]]"
  - "[[Confidence Interval]]"
  - "[[Effect Size]]"
  - "[[Standard Error]]"
  - "[[Multiple Regression]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[National Science Foundation]]"
  - "[[National Institutes of Health]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Stephan_2013_NBER]]"
  - "[[Argument_Liu_2023_NHB]]"
confidence: high
status: completed
created: 2026-06-01
updated: 2026-11-02
---

---

> [!def] Descriptive Analysis
> **描述性分析（Descriptive Analysis）** 是[[Quantitative Research|量化研究]]数据分析的基础步骤，通过对样本中所有预测[[Variable|变量]]与[[Dependent Variable|结果变量]]计算集中趋势（如均值、中位数）、离散程度（如标准差、全距）与频数分布，总结受试样本的基本特征与数据形态，并系统排查与报告缺失数据的程度及处理方案([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch. 8]])。
> 
> 在科学学与计量分析中，描述性分析用于在大规模文献与网络数据中提炼宏观经验规律（Descriptive Regularities，如引文分布与合作网络拓扑），为后续的预测建模与[[Causality|因果推断]]建立基准([[Argument_Liu_2023_NHB|Liu et al., 2023, pp. 341–350]])。

> [!method-scope] 方法范围
> - **研究对象** 问卷调查样本、实验前后测指标、大规模学术出版与资助记录、宏观教育财政与机构纵向统计数据。
> - **问题类型** 刻画样本特征分布、测度变量变异范围、总结历史演进趋势及识别宏观经验规律。
> - **[[Unit of Analysis|分析单位]]** 学生个体、教师、学校、科研学者、学术出版物或公共资助项目。
> - **输出形式** 描述统计汇总表（均值、标准差、分位数、极值）、频数百分比、交叉列联表、缺失值诊断报告与分布可视化图表。

> [!citation-card] 描述性分析的基本功用
> 描述性分析为研究者提供样本整体形态与变异程度的客观总结，是进入推断统计检验与因果估计的前提步骤。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch. 8)]]
>
> *Descriptive analysis provides an overall summary of the sample characteristics, distributions, and degrees of dispersion, establishing the factual foundation prior to conducting inferential tests or causal modeling.*

---

> [!method-position] 认识论与方法定位
> - **知识观** 属于经验描述主义，旨在真实、客观、无偏地汇总与再现可观测样本的数据属性，不预设未观测总体的参数分布假设。
> - **研究者角色** 负责指标定义、测量尺度判定、极端值识别与缺失数据处理规程的制定，确保描述性指标真实反映数据生成过程。
> - **有效性标准** 统计描述准确性、缺失值处理透明度与数据分布特征刻画的完整性。
> - **不声称回答的问题** 描述性分析无法直接检验关于总体的理论假设，亦不能基于变量之间的统计关联确立机制因果关系。

> [!method-stack] 方法层级
> - **研究设计** [[Survey Research|调查研究]]、[[Non-intervention Research|观察研究]]、[[Correlational Research|相关研究]]与[[Experimental Research|实验研究]]的前置探索阶段。
> - **数据收集** 问卷调查、行政普查、文献计量库与纵向历史档案。
> - **分析方法** 频数分析、集中趋势测度、离散度分析、分位数检验与列联交叉分析。
> - **辅助技术** 多重填补（Multiple Imputation）、全信息最大似然估计（FIML）、盒须图与核密度分布图。

---

> [!proc] 描述统计标准分析规程
> 1. **数据核验与缺失诊断** 检查各变量有效样本量，计算缺失值比例与缺失模式，评估缺失是否满足完全随机缺失条件。
> 2. **缺失处理策略确立** 依据缺失机制选择直接剔除、多重填补或全信息最大似然估计，确保分析样本的可比性。
> 3. **计算集中趋势与离散测度** 对连续变量计算均值、标准差与得分范围；对分类变量计算频数与百分比。
> 4. **分布形态与异常值排查** 检验偏度与峰度，绘制直方图或核密度曲线，排查输入录入错误或极端异常观测点。
> 5. **编制标准化描述统计表** 按照学术规范呈现样本全貌，并在实验研究中分别呈现处理组与对照组的基线特征。

> [!method-stack] 数据与变量
> - **数据结构** 截面问卷数据、长周期面板数据或多机构纵向统计序列。
> - **样本与单位** 依据研究问题确立的独立个体、学术机构或项目资助样本。
> - **变量或测量** 连续变量（成绩、经费、引用数）与分类变量（性别、学科、机构类型）。

---

> [!method-fit] 适用判断
> - **适合使用** 任何量化研究的初始数据探索阶段；梳理大规模历史档案或宏观指标演进轨迹（如联邦科研资助与博士规模的半世纪变动趋势）。[[Argument_Stephan_2013_NBER|(Stephan, 2013)]]; [[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch. 8)]]
> - **谨慎使用** 变量分布严重偏态或存在极端厚尾时，需辅以中位数与分位数指标，避免被算术均值误导。
> - **不适合使用** 试图单独依据描述统计量推断未抽样总体特征，或依据两变量同向演变断言存在因果促进机制。[[Argument_Liu_2023_NHB|(Liu et al., 2023, pp. 341–350)]]

---

> [!method-limits] 方法局限
> - **偏误来源** 样本选择偏误、测量误差与缺失数据处理不当引发的参数扭曲。
> - **适用边界** 结论严格受限于当前观测样本的特征空间，缺乏向未观测情境推论的统计依据。
> - **误用风险** 将描述性规律（如发表量与影响力的正向关联）混淆为因果机制，忽视潜在混杂因素引发的内生性问题。
> - **补救方式** 结合[[Statistical Significance|推断统计]]报告[[Confidence Interval|置信区间]]，并引入准实验或实验因果设计检验潜在机制。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Quantitative Research]] | 母类方法 | 描述性分析构成全部量化实证研究的数据分析基石。 |
> | [[Survey Research]] | 应用场景 | 调查问卷数据清理与报告人口统计学特征的标准入口。 |
> | [[Experimental Research]] | 配合方法 | 在实验开展前用于检验处理组与对照组的基线可比性。 |
> | [[Correlational Research]] | 后续延伸 | 以描述统计为基础进一步测度变量间的共变关系。 |
> | [[Statistical Significance]] | 互补工具 | 推断统计通过显著性检验弥补描述分析无法推论总体的缺陷。 |
> | [[Causality]] | 对照范式 | 描述性经验规律为因果识别提供假说，因果设计则检验规律背后的机制。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Creswell_2022_SAGE|Creswell and Creswell (2022)]] — 阐释在调查与实验量化研究中规范开展描述统计、诊断并填补缺失数据的标准程序(Ch. 8)。
> - [[Argument_Stephan_2013_NBER|Stephan (2013)]] — 通过对美国 1950 至 2010 年代 [[National Science Foundation|NSF]]、[[National Institutes of Health|NIH]] 联邦资助、博士授权机构数、在读时间、资助集中度及医学院债务等宏观统计数据展开长时段历史描述性分析，揭示战后科研体制扩张的结构性压力。
> - [[Argument_Liu_2023_NHB|Liu et al. (2023)]] — 阐明科学学从描述性经验规律提炼（如引文幂律与网络拓扑）跨越至机器学习预测与微观计量因果推断的方法论演进路径（pp. 341–350）。
