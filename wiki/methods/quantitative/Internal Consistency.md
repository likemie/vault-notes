---
title: Internal Consistency
aliases:
  - 内部一致性
  - 内部一致性信度
  - internal consistency reliability
summary: "信度作为内部一致性的形式，衡量多项目量表中各条目测量同一底层构念的程度，通过半分法与Spearman-Brown公式或Cronbach alpha量化，后者等效于所有可能半分方式的Spearman-Brown校正值的平均值"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 25
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/measurement
  - quantitative-research
  - reliability
related_concepts:
  - "[[Reliability]]"
  - "[[Construct]]"
  - "[[Variable]]"
  - "[[Unit of Analysis]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Paradigm]]"
  - "[[Construct Validity]]"
  - "[[Operationalization]]"
related_methods:
  - "[[Questionnaire]]"
  - "[[Survey Research]]"
  - "[[Scale Development]]"
  - "[[Rating Scale]]"
  - "[[Item Analysis]]"
  - "[[Exploratory Factor Analysis]]"
  - "[[Sample Size Determination]]"
  - "[[Cronbach's Alpha]]"
  - "[[Confidence Interval]]"
  - "[[Confirmatory Factor Analysis]]"
  - "[[Split-Half Reliability]]"
  - "[[Test-Retest Reliability]]"
  - "[[Inter-Rater Reliability]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10]]"
  - "[[Argument_Creswell_2022_SAGE]]"
related_theories:
  - "[[Classical Test Theory]]"
status: draft
created: 2026-05-31
updated: 2026-10-29
---

---

> [!def] Internal Consistency
> 内部一致性（Internal Consistency）是[[Reliability|信度]]在量化测量中的核心形式，衡量多项目量表中各条目（items）在单次测验中指向同一底层[[Construct|构念]]的统计同质性程度（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|Cohen et al., 2011, Ch. 10, pp. 202–204]]）。

> [!method-scope] 方法范围
> - **研究对象** 心理量表、[[Questionnaire|问卷]]题项、标准化测验试题与多指标评估工具。
> - **问题类型** 适合回答测验题项是否协同测量单一潜[[Variable|变量]]、各题项间相关强度及量表同质性检验。
> - **[[Unit of Analysis|分析单位]]** 测验题项、量表维度与受试者单次反应得分。
> - **输出形式** 半分相关系数、Spearman-Brown 校正系数与 Cronbach's $\alpha$ 估计值。

> [!citation-card] 关键定义
> 对于多项目工具来说，最重要的信度形式是工具的内部一致性——即工具上各组条目以相同方式运作的程度。[[Argument_Creswell_2022_SAGE|(Creswell & Creswell, 2022, Ch. 8)]]
>
> *The most important form of reliability for multi-item instruments is the instrument's internal consistency—the degree to which sets of items on an instrument behave in the same way.*

---

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 属于[[Positivism|实证主义]]测量[[Paradigm|范式]]，预设潜在特质能够通过一组相互关联的经验题项进行抽样表征。
> - **研究者角色** 测量工具的设计者与统计检验者，负责题项筛选、难度与区分度控制以及同质性判定。
> - **有效性标准** 遵循[[Classical Test Theory|经典测验理论]]（Classical Test Theory, CTT），以项目间协方差结构与方差分解评估测量精度。
> - **不声称回答的问题** 不回答跨时间的测量稳定性，也不直接证明题项所测内容是否真实对应目标概念（[[Construct Validity|构念效度]]需外部证据支持）。

> [!method-stack] 方法层级
> - **研究设计** [[Survey Research|调查研究]]、[[Scale Development|量表编制]]与心理测量试验。
> - **数据收集** Likert 量表[[Questionnaire|问卷]]、二分选择测验与多指标[[Rating Scale|评定量表]]。
> - **分析方法** 题项间相关分析、半分相关校正与 Cronbach's $\alpha$ 计算。
> - **辅助技术** [[Item Analysis|项目分析]]、区分度检验与[[Exploratory Factor Analysis|探索性因子分析]]。

---

> [!proc] 通用程序
> 1. **明确潜在[[Construct|构念]]** 界定量表所欲测量的单一心理特质或行为倾向。
> 2. **编制测验题项** 围绕构念[[Operationalization|操作化]]编写一组具有代表性的测量题项。
> 3. **实施单次施测** 在目标样本群体中施测并收集原始作答数据。
> 4. **评估内部一致性** 通过半分法或计算 Cronbach's $\alpha$ 检验题项同质性。
> 5. **题项净化与修订** 排查低相关或降低量表总[[Reliability|信度]]的题项，优化工具结构。

> [!method-stack] 数据、[[Variable|变量]]与模型
> - **数据结构** 单次截面作答矩阵（$N$ 名受试者 $\times$ $k$ 个题项）。
> - **样本与单位** 个体学生或受试者，[[Sample Size Determination|样本量]]通常需满足受试者与题项比至少 5:1 至 10:1。
> - **变量或指标** 各题项连续得分或等级积分，以及量表总分。
> - **模型或统计量** 半分信度系数、Spearman-Brown 公式与 Cronbach's $\alpha$ 系数。
> - **诊断与检验** 题项总分相关（Item-Total Correlation）、删除项后的 $\alpha$ 变化量。

> [!formula-step] 公式步骤　Spearman-Brown 折半校正公式
> $$r_{sb} = \frac{2r}{1 + r}$$
>
> **这个公式在做什么** 从两半测验得分的相关系数 $r$，推算测验长度恢复为完整原长时的全量表信度。
>
> **符号说明**
> - $r$ 为将测验均分为对等两半后计算的 Pearson 积矩相关系数。
> - $r_{sb}$ 为经题项长度校正后的完整量表信度估计值。
>
> **数学直觉** 测验信度随测验长度增加而提高，公式逆向弥补将项目折半造成的信度人为衰减。
>
> **结果怎么读** 数值介于 0 到 1 之间，越接近 1 表明两半题项测量的内容越趋于一致。

> [!formula-step] 公式步骤　[[Cronbach's Alpha]] 内部一致性系数
> $$\alpha = \frac{k}{k - 1} \left(1 - \frac{\sum_{i=1}^k \sigma^2_i}{\sigma^2_{\text{total}}}\right)$$
>
> **这个公式在做什么** 计算所有项目方差和与总分方差的比值，表征题项间共同变异占总变异的份额。
>
> **符号说明**
> - $k$ 为量表包含的有效测验题项总数。
> - $\sum_{i=1}^k \sigma^2_i$ 为各单项得分方差的总和。
> - $\sigma^2_{\text{total}}$ 为所有受试者量表总分的方差。
>
> **数学直觉** 当题项高度协同测量同一特质时，协方差推高总分方差，使单项方差和占比缩减，$\alpha$ 逼近 1。数学上等效于所有可能折半方式下 Spearman-Brown 校正值的均值。
>
> **结果怎么读**
> - $\alpha \ge 0.90$：极高一致性，但需排查题项表述高度雷同带来的内容冗余。
> - $0.70 \le \alpha < 0.90$：处于最佳区间，题项同质且保有独特信息增量。
> - $\alpha < 0.70$：内部一致性偏低，需审查题项质量或是否存在多维度混杂。

> [!software-impl] 软件实现
> - **数据处理** 确认反向计分题已正确转换，排查缺失值与极端异常反应。
> - **推荐软件** R (`psych::alpha`)、Python (`pingouin.cronbach_alpha`)、SPSS (`Analyze -> Scale -> Reliability Analysis`)。
> - **核心包或命令** R 语言运行 `psych::alpha(data)`，直接输出原始 $\alpha$、标准化 $\alpha$ 以及各题项删除后的信度变动（alpha if item deleted）。
> - **报告标准** 报告题项总数 $k$、样本量 $N$、$\alpha$ 点估计及 95% [[Confidence Interval|置信区间]]。

---

> [!method-fit] 适用判断
> - **适合使用** 多项目单维度[[Scale Development|量表编制]]、态度与心理特质测量工具[[Reliability|信度]]检验、单次施测[[Questionnaire|问卷]]的质量评估（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022]]）。
> - **谨慎使用** 包含明显子维度的综合性多维量表，需按各个独立子维度分别计算内部一致性，不可盲目合并计算全量表 $\alpha$。
> - **不适合使用** 速度测验（Speed Tests，未作答题目会导致一致性虚高）或动态追踪跨期稳定性的研究设计。

---

> [!method-limits] 方法局限
> - **偏误来源** 题项数量膨胀效应。$\alpha$ 数值直接受题项数量 $k$ 影响，长量表即便各题项相关较弱亦可获得高 $\alpha$，易掩盖测量质量缺陷。
> - **适用边界** 依赖 $\tau$ 等值假设（$\tau$-equivalent model），即假定所有题项对潜在[[Construct|构念]]的负荷均等；若因子负荷差异显著，$\alpha$ 将低估真实[[Reliability|信度]]，此时分层 $\omega$（McDonald's $\omega$）为更优估计。
> - **误用风险** 盲目追求高 $\alpha$（如 $>0.95$）导致题项语义过度重合，窄化构念内涵并损害[[Construct Validity|构念效度]]。
> - **补救方式** 结合[[Confirmatory Factor Analysis|验证性因子分析]]（CFA）检验单维度性，辅以 McDonald's $\omega$ 系数作为交叉验证。

---

> [!entry-map] 相关理论与方法
>
> | 条目 | 类型 | 关系 |
> |:---|:---|:---|
> | [[Reliability]] | 概念母体 | 内部一致性是实证信度体系中与稳定性、等值性并列的核心支柱。 |
> | [[Cronbach's Alpha]] | 专用指标 | 内部一致性最广泛采用的数学估计公式与[[Operationalization\|操作化]]指标。 |
> | [[Split-Half Reliability]] | 前置方法 | 内部一致性检验的早期基础算法，通过两半相关推导全量表信度。 |
> | [[Test-Retest Reliability]] | 互补方法 | 评估跨时间稳定性的信度形式，需两次施测。 |
> | [[Inter-Rater Reliability]] | 互补方法 | 评估跨观察者评分一致性的信度形式。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch10|Cohen et al. (2011, Ch. 10)]] — 系统界定教育测量中的量化内部一致性、半分法推导与 $\alpha$ 解释标准。
> - [[Argument_Creswell_2022_SAGE|Creswell and Creswell (2022, Ch. 8)]] — 阐释量表研发中内部一致性的首要地位，并以 PSS 知觉压力量表示范[[Reliability|信度]]检验规程。
