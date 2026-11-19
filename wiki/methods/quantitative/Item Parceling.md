---
title: Item Parceling
aliases:
  - 题项打包
  - 题项聚合
  - 条目打包
  - parceled indicators
summary: "在结构方程模型与验证性因子分析中，将同一单维潜变量下的两个或多个观测题项按特定规则（如随机分配、因子负荷配对或概念平衡）相加或平均组合成复合观测指标（包裹）的心理计量学方法。该方法能够在保持构念测量效度的同时，显著减少待估参数、降低样本量需求、平抑个别测量误差并改善指示变量的多元正态性，广泛应用于复杂潜变量因果路径模型的构建与拟合。"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 24
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/statistical
related_concepts:
  - "[[Variable]]"
  - "[[Construct]]"
  - "[[Teacher Beliefs]]"
  - "[[Student Motivation]]"
  - "[[Unit of Analysis]]"
  - "[[Scale of Measurement]]"
  - "[[Reliability]]"
  - "[[Construct Validity]]"
related_theories:
  - "[[Classical Test Theory]]"
related_methods:
  - "[[Confirmatory Factor Analysis]]"
  - "[[Causal Modeling]]"
  - "[[Questionnaire]]"
  - "[[Model Fit Indices in SEM and CFA]]"
  - "[[Composite Reliability]]"
  - "[[Differential Item Functioning]]"
  - "[[Exploratory Factor Analysis]]"
  - "[[Random Assignment]]"
  - "[[Sample Size Determination]]"
  - "[[Cronbach's Alpha]]"
  - "[[Average Variance Extracted]]"
  - "[[Scale Development]]"
  - "[[Pre-test and Post-test]]"
  - "[[Internal Consistency]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Hogan_2013_ROE]]"
confidence: high
status: active
created: 2026-11-19
updated: 2026-11-19
---

---

> [!def] Item Parceling
> 题项打包（Item Parceling）指在[[Confirmatory Factor Analysis|验证性因子分析]]（CFA）与结构方程模型（[[Causal Modeling|SEM]]）中，将测量同一单维潜[[Variable|变量]]的两个或多个原始题目得分通过求和或求均值的方式合并为一个复合观测指标（称为包裹，Parcel）的量化处理技术。该技术输入原始李克特连续或有序量表题项得分，通过减少估计参数与平抑测量噪声，输出稳健的潜变量负荷与路径估计结果。[[Argument_Hogan_2013_ROE|(Bandalos & Finney, 2001; cited in Hogan et al., 2013, pp. 62–63)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 心理与教育量表测查的连续潜变量（Continuous Latent Variables）与复杂[[Construct|构念]]（如教学策略、[[Teacher Beliefs|教师信念]]、[[Student Motivation|学习动机]]）。
> - **问题类型** 测量模型降维、模型过辨识优化、多元正态性校准与复杂潜变量因果路径识别。
> - **[[Unit of Analysis|分析单位]]** 填答[[Questionnaire|问卷]]的学生、教师个体或班级聚合均值。
> - **输入数据** 同一维度下 4 个及以上具有相同[[Scale of Measurement|测量尺度]]的原始题项得分；各题项需满足单维性（Unidimensionality）假定。
> - **输出形式** 打包指标分值、标准化因子载荷（Factor Loadings）、测量误差方差（Measurement Error Variances）以及整体[[Model Fit Indices in SEM and CFA|模型拟合指数]]。

> [!citation-card] 关键定义
> 题项打包能够有效缓解大题量测量模型中参数过度膨胀的问题。当构念本身满足单维性要求时，将原始题项组合为包裹可以降低测量误差、提升指标[[Reliability|信度]]，并减少违反多元正态性假设的风险，从而为复杂的全潜变量结构方程建模提供具有统计稳定性的参数估计基础。[[Argument_Hogan_2013_ROE|(Bandalos & Finney, 2001; Coffman & MacCallum, 2005; Sass & Smith, 2006; cited in Hogan et al., 2013, p. 62)]]
>
> *Item parceling involves aggregating individual items into small subsets (parcels) that serve as indicators of latent variables in SEM. When unidimensionality holds, parcels have higher reliability, lower skewness and kurtosis, and yield more parsimonious models with better fit.*

---

> [!method-position] 方法定位
> - **[[Construct Validity|构念效度]]** 打包的前提是严格确证构成单维维度的同质题项。若构念本身为多维复合结构，机械打包会掩盖真实次级因子结构并导致构念效度失真。
> - **研究者判断** 决定具体的打包策略（平衡负荷配对法、随机抽取法或内容语义领域法），以及每个潜变量构建的包裹数量（通常为 3 至 4 个包裹）。
> - **有效性标准** [[Composite Reliability|构念信度]]（Composite Reliability, CR $\ge .70$）、各包裹因子载荷高度显著（$\lambda \ge .70$）以及 CFA 测量模型拟合良好（$p > .05$, CFI $\ge .95$, RMSEA $\le .05$）。
> - **不声称回答的问题** 该方法无法诊断单个具体题项的测量特异性偏差（如差异题项功能 [[Differential Item Functioning|DIF]]），亦不能替代对新开发量表题项质量的逐题检验。

> [!method-stack] 方法层级
> - **上位方法** [[Confirmatory Factor Analysis|验证性因子分析]]（CFA）、全潜变量结构方程模型（SEM）。
> - **前置步骤** 单因子[[Exploratory Factor Analysis|探索性因子分析]]（EFA）检验单维性、项目间相关分析、极端值清洗与反向题转换。
> - **变体与扩展** 
>   1. **因子负荷平衡法（Balanced Approach）** 依据单因子载荷高低交替配对聚合，使各包裹载荷趋向均等；
>   2. **内容领域法（Domain-Representative Approach）** 确保每个包裹均等包含子领域题项；
>   3. **随机打包法（[[Random Assignment]]）** 在题项高度同质时随机抽取组合。

---

> [!formula-step] 步骤一　题项均值聚合与包裹生成
> $$P_j = \frac{1}{k_j} \sum_{i=1}^{k_j} X_{ji}$$
>
> **这个公式在做什么** 计算第 $j$ 个包裹的观测得分 $P_j$。输入为分配至该包裹的 $k_j$ 个原始题目得分 $X_{ji}$，输出为该包裹的合成算术均值。[[Argument_Hogan_2013_ROE|(Hogan et al., 2013, p. 62)]]
>
> **符号说明** 
> - $P_j$ 表示第 $j$ 个题项包裹（Parcel）的观测分值。
> - $k_j$ 表示打包入该包裹的原始题目数量（通常为 2 至 4 题）。
> - $X_{ji}$ 表示被分配至该包裹的第 $i$ 个原始测验题目得分。
>
> **数学直觉** 根据[[Classical Test Theory|经典测验理论]]，将多个具有正相关与共同特质的观测题项加总平均，能够相互抵消个别题项中的特异随机误差方差，从而放大共有特质方差的比例。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 连续变量性质 | 打包后的均值指标由原始离散有序得分转化为近似连续正态分布的数值。 |
> > | 注意 | 单维性前提 | 打包前必须通过严密的因子分析验证题项集合的单维性，严禁跨维度混合打包。 |

> [!formula-step] 步骤二　预设参数约束或全自由 CFA 估计
> 当[[Sample Size Determination|样本量]]有限或模型过度饱和时，研究者可依据单个构念的信度与方差预先设定包裹的负荷与误差方差；亦可在样本量充分时采用全自由估计：
>
> $$\lambda_j = \sigma_P \sqrt{\alpha}, \quad \theta_j = \sigma^2_P (1 - \alpha)$$
>
> **这个公式在做什么** 输入包裹的方差 $\sigma^2_P$ 与 Cronbach's $\alpha$ 信度，输出潜变量至包裹的预设固定因子载荷 $\lambda_j$ 与测量残差方差 $\theta_j$。[[Argument_Hogan_2013_ROE|(Jöreskog, 1971; Bandalos & Finney, 2001; cited in Hogan et al., 2013, p. 63)]]
>
> **符号说明** 
> - $\lambda_j$ 表示潜变量对第 $j$ 个包裹的因子载荷。
> - $\theta_j$ 表示第 $j$ 个包裹的测量误差方差。
> - $\sigma^2_P$ 表示包裹的总体方差，$\sigma_P$ 为其标准差。
> - $\alpha$ 表示构念内各题项的[[Cronbach's Alpha|内部一致性信度系数]]。
>
> **数学直觉** 将已知的单变量信度分解为真实方差与误差方差，从而减轻大样本非线性迭代中的参数估计负担，提升复杂因果网络模型的运算稳定性。

> [!software-impl] 软件实现
> - **数据来源** 问卷调查原始数字矩阵（如 CSV 或 SAV 格式）。
> - **核心包或命令** R 语言 `lavaan` 包、Python `semopy` 包、`Mplus` 或 `LISREL`。
> - **实现流程** 1. 运行单因子 CFA 提取因子载荷；2. 按负荷高低平衡配对生成 3 个打包变量；3. 构建潜变量 CFA 评估拟合指数。
> - **报告标准** 报告打包方法选择依据、包裹数量、各包裹包含题项清单、构念信度（CR）、[[Average Variance Extracted|平均方差变异抽取量]]（AVE）以及整体 CFA 拟合指标。

> [!formula] Python 计算骨架
> ```python
> import pandas as pd
> import numpy as np
>
> # 假设 df 包含测量同一单维构念的 6 个原始题项 (item1 到 item6)
> # 按单因子载荷平衡配对 (如高载荷与低载荷互补组合)
> # Parcel 1: 题项 1 与 题项 6
> # Parcel 2: 题项 2 与 题项 5
> # Parcel 3: 题项 3 与 题项 4
>
> def create_balanced_parcels(data, parcel_pairs):
>     parcels = pd.DataFrame()
>     for p_name, items in parcel_pairs.items():
>         parcels[p_name] = data[items].mean(axis=1)
>     return parcels
>
> # parcels 作为连续指示变量进入 semopy 或 lavaan 结构方程建模
> ```

---

> [!method-fit] 适用判断
> - **适合使用** 问卷包含大量题目（如 Hogan et al., 2013 包含 230 个题项与 22 个复杂构念），需要构建多构念因果路径全模型，且样本量与自由度比例偏紧的情境。[[Argument_Hogan_2013_ROE|(Hogan et al., 2013, pp. 62–63)]]
> - **谨慎使用** 原始题项存在多维次级结构倾向或跨维度交叉载荷时，需先理顺子构念再分别打包。
> - **不适合使用** 处于探索阶段的[[Scale Development|量表开发]]研究、需要逐题删减优化问卷题项的研究，或旨在检验特定题项歧视度与语义效应的情境。

---

> [!method-limits] 方法局限
> - **掩盖局部多维性** 若原始题项未严格经过单维性检验，打包操作可能人为平滑并掩盖次级因子维度的存在，产生虚假的高模型拟合度。
> - **组合敏感性风险** 不同的打包配对方式可能导致参数估计值轻微浮动，研究者需报告敏感性分析或采用标准平衡算法以确保结果稳健。
> - **信息损失** 打包后无法在最终结构方程模型中追踪单个题项的特异变异。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Confirmatory Factor Analysis]] | 方法 | 检验单维构念信效度及检验打包指标测量模型的基础统计方法。 |
> | [[Causal Modeling]] | 方法 | 题项打包在全潜变量结构方程模型中充当降低估计负荷的关键技术支架。 |
> | [[Model Fit Indices in SEM and CFA]] | 方法 | 用于判定题项打包前[[Pre-test and Post-test\|后测]]量模型与结构模型优劣的一系列评估指标。 |
> | [[Construct]] | 概念 | 题项打包技术所测量的抽象潜变量理论概念。 |
> | [[Variable]] | 概念 | 经题项打包运算后生成的包裹属于连续可观测指示变量。 |
> | [[Reliability]] | 概念 | 题项打包通过聚合多个观测题项显著提升测量指标的统计信度。 |
> | [[Composite Reliability]] | 概念 | 评估题项打包后潜变量测量模型[[Internal Consistency\|内部一致性]]的核心拟合参数。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Hogan_2013_ROE|Hogan et al. (2013)]] — 在新加坡 32 所中学 4000 余名中三学生的大规模课堂调查中，使用题项打包技术将 230 个问卷题项高效聚合为 22 个教学实践潜变量的 3 至 4 个包裹指标，测量模型信度达 .79–.90 且均获得优良拟合（pp. 62–63）。
