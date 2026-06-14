---
title: Coupling Coordination Model
aliases:
  - 耦合协调模型
  - CCDM
  - Coupling Coordination Degree Model
summary: "一种基于系统论的多子系统协同发展水平测度方法，通过耦合度C衡量相互作用强度、协调度D综合评估协同演进水平，广泛应用于教育、经济、环境等复杂系统的综合评价"
type: method
method_type: quantitative
tags:
  - method/composite-index
  - method/spatial-analysis
  - theme/systems-theory
related_concepts:
  - "[[Causality]]"
related_theories:
  - "[[Coupling Coordination Theory]]"
related_methods:
  - "[[Combined Weighting AHP-EWM]]"
  - "[[LISA Time Path]]"
  - "[[LISA Spatiotemporal Transition]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Fan_Song_Zhai_2024_RSEE]]"
confidence: medium
status: draft
created: 2026-06-12
updated: 2026-06-14
---

# Coupling Coordination Model

---

## 定义

> [!def] 方法定义
> 耦合协调模型（Coupling Coordination Degree Model, CCDM）是一种基于系统论的多子系统协同发展水平测度方法。它先用耦合度 $C$ 衡量若干子系统发展水平之间的相互贴合程度，再用协调度 $D$ 将耦合强度与综合发展水平 $T$ 合成，用于判断系统是否处于高水平协同、低水平贴合或失调状态。该模型的核心用途不是识别因果机制，而是把多维指标体系压缩为可比较的综合评价结果。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 66-68)]]

> [!method-scope] 方法范围
> - **研究对象**：由两个或多个相互关联子系统构成的复杂系统，例如教育、科技、人才三系统。
> - **问题类型**：适合回答综合测度、时空比较、区域分异和协同状态评价问题。
> - **分析单位**：地区、年份、城市、省份、国家、政策单元或其他可构建指标体系的空间/组织单元。
> - **输出形式**：子系统发展水平 $e_j$、耦合度 $C$、综合发展指数 $T$、协调度 $D$、等级分类和时空格局。

> [!citation-card]- 关键定义
> 耦合指两个或多个子系统之间相互影响和相互作用的程度，也可以反映不同子系统之间的约束程度。耦合度可以衡量不同子系统之间的协同发展水平，并在一定程度上描述不同子系统发展水平的差异。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]
>
> Original: Coupling refers to the extent of mutual influence and interaction among two or more subsystems, and it can also reflect the degree of constraint between different subsystems. The degree of coupling can measure the level of collaborative development between different subsystems.

---

## 方法定位

> [!assumptions] 认识论与方法定位
> - **知识观**：耦合协调模型把复杂系统状态视为可通过指标体系近似测量的综合发展水平。它依赖后实证主义式的量化表示，但不等同于对系统因果机制的完整解释。
> - **研究者角色**：研究者在子系统划分、指标选择、正负向指标处理、权重设定和等级阈值选择中发挥实质判断作用。这些判断会影响 $D$ 值和空间分类。
> - **有效性标准**：评价重点包括指标体系的内容效度、权重设定的透明度、标准化口径的一致性、分类阈值的可解释性和敏感性检查。
> - **不声称回答的问题**：$D$ 值只能描述综合协调状态，不能直接证明教育促进科技、科技吸引人才或人才反哺教育等[[Causality|因果关系]]。

> [!method-panel] 方法层级
> | 层级 | 说明 |
> |---|---|
> | 研究设计 | 综合评价设计，常与面板数据、空间分析或政策区域比较结合。 |
> | 数据收集 | 公开统计数据、行政数据、地区年度指标、政策或行业统计指标。 |
> | 分析方法 | 指标标准化、综合赋权、耦合度计算、协调度计算、等级划分。 |
> | 辅助技术 | [[Combined Weighting AHP-EWM|AHP-熵权法组合赋权]]、自然断点分类、地图可视化、[[LISA Time Path|LISA时空路径]]和[[LISA Spatiotemporal Transition|LISA时空转移]]。 |

---

## 研究程序

> [!proc] 通用程序
> 1. 确定需要评价的复杂系统及其子系统，例如教育、科技和人才。
> 2. 为每个子系统建立指标体系，区分正向指标和负向指标。
> 3. 对原始指标进行标准化，得到可比较的无量纲指标 $g_{ij}$。
> 4. 确定指标权重 $f_i$，并计算各子系统发展水平 $e_j$。
> 5. 计算耦合度 $C$，判断子系统发展水平之间的贴合程度。
> 6. 计算综合发展指数 $T$ 和协调度 $D$，避免低水平高耦合误判。
> 7. 按自然断点、分位数、等距或理论阈值对 $D$ 进行等级划分。
> 8. 结合地图、时序图或空间统计方法解释区域差异和时间演变。

> [!formula-set] 公式链总览
> - **指标标准化得到 $g_{ij}$**：把不同单位和方向的指标放到同一尺度。
> - **加权合成得到 $e_j$**：把每个子系统内的多个指标合成为一个发展水平。
> - **比较均衡程度得到 $C$**：判断多个子系统的发展水平是否贴合。
> - **综合发展水平得到 $D$**：同时考虑均衡贴合和整体发展水平，避免低水平高耦合误判。

> [!formula-step] 步骤一：指标标准化
> $$g_{ij}=\frac{X_{ij}-\min X_{ij}}{\max X_{ij}-\min X_{ij}} \quad \text{正向指标}$$
> $$g_{ij}=\frac{\max X_{ij}-X_{ij}}{\max X_{ij}-\min X_{ij}} \quad \text{负向指标}$$
>
> **这个公式在做什么**：把原始指标 $X_{ij}$ 转换成 $[0,1]$ 区间内的无量纲指标 $g_{ij}$，让教育投入、科研产出、人才数量等不同单位的指标可以比较。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 66-67)]]
>
> **数学直觉**：min-max 标准化用“当前位置距离最小值多远”除以“最大值和最小值之间的总跨度”。正向指标越大越好，负向指标越小越好，所以负向指标要反过来算。
>
> **结果怎么读**：$g_{ij}$ 越接近 1，表示该单位在这个指标上越接近样本中的最好水平；越接近 0，表示越接近样本中的最低水平。
>
> **注意事项**：标准化结果依赖样本范围。若加入新年份或新地区，最大值和最小值可能改变，历史得分也可能随之变化。

> [!formula-step] 步骤二：计算子系统发展水平
> $$e_j=\sum_{i \in j}f_i g_{ij}$$
>
> **这个公式在做什么**：把同一子系统中的多个标准化指标合成为一个子系统得分 $e_j$。例如教育子系统可以由经费、入学率、师资等指标加权合成。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 66-67)]]
>
> **数学直觉**：这是加权平均。权重 $f_i$ 决定每个指标在子系统得分中说话的分量，权重越高，指标对 $e_j$ 的影响越大。
>
> **结果怎么读**：$e_j$ 是第 $j$ 个子系统的相对发展水平。它可以帮助识别短板，例如教育系统高、科技系统低、人才系统中等。
>
> **注意事项**：$e_j$ 对权重很敏感。若权重来自 AHP、熵权法或组合赋权，应报告权重来源，并检查替换权重后排序是否稳定。

> [!formula-step] 步骤三：计算耦合度
> $$C=\left[\frac{\prod_{j=1}^{K}e_j}{\left(\frac{1}{K}\sum_{j=1}^{K}e_j\right)^K}\right]^{1/K}$$
> 三系统时：
> $$C=\left[\frac{e_1e_2e_3}{\left(\frac{e_1+e_2+e_3}{3}\right)^3}\right]^{1/3}$$
>
> **这个公式在做什么**：计算 $K$ 个子系统发展水平之间的均衡贴合程度。$C$ 越高，表示各子系统水平越接近。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]
>
> **数学直觉**：这个公式本质上比较几何均值和算术均值。由均值不等式可知，几何均值不大于算术均值；当各子系统数值越接近，两者越接近，$C$ 越高。
>
> **结果怎么读**：高 $C$ 表示“均衡”或“贴合”，不是“高水平”。如果三个子系统都很低但一样低，$C$ 也可能很高。
>
> **注意事项**：这就是耦合度陷阱。若 $e_1=e_2=e_3=0.1$，$C$ 仍可达到 1，因此不能只看 $C$ 判断协调发展。

> [!formula-step] 步骤四：计算协调度
> $$T=\sum_{j=1}^{K}\alpha_j e_j$$
> $$D=\sqrt{C \times T}$$
>
> **这个公式在做什么**：先用 $T$ 表示综合发展水平，再用 $D$ 把耦合度 $C$ 和综合发展水平 $T$ 合成一个协调度。Fan et al. 在教育、科技、人才三系统中采用等权设定。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 67-68)]]
>
> **数学直觉**：$D$ 使用几何平均连接 $C$ 和 $T$。几何平均具有短板惩罚效果，只要耦合度或发展水平任一偏低，最终协调度都会被拉低。
>
> **结果怎么读**：$D$ 越高，表示系统越接近“高水平且均衡”的协调状态；$D$ 低可能来自系统整体水平低，也可能来自子系统之间不均衡。
>
> **注意事项**：$D$ 是描述性综合指标，不是因果估计。高 $D$ 不能说明某个子系统导致另一个子系统发展。

> [!ref-table] 参数、权重与分类
> | 项目 | 取值或规则 | 解释 |
> |---|---|---|
> | 子系统数量 $K$ | 通常为 2 或 3，也可扩展到更多子系统。 | $K$ 改变会影响耦合度公式的阶数和解释。 |
> | 指标权重 $f_i$ | 可用等权、AHP、熵权法、AHP-EWM-LSD 组合赋权等。 | 权重直接影响子系统发展水平 $e_j$，是最重要的敏感性来源之一。 |
> | 子系统权重 $\alpha_j$ | 常见做法为等权，例如三系统各取 $1/3$。 | 等权表达“同等重要”的规范判断，不是数据自动给出的事实。 |
> | 等级阈值 | Fan et al. 使用 ArcGIS 10.8 的自然断点法。 | 自然断点最小化组内差异、最大化组间差异，但分类结果依赖样本分布。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 68)]] |
> | 空间分析扩展 | LISA 时空路径和 LISA 时空转移。 | 用于分析协调度的空间关联、路径移动和类型转移，不属于 CCDM 本体公式。 |

> [!result-reading] 结果解读
> - **先看 $e_j$**：哪个子系统高、哪个子系统低，用来找短板。不要把标准化得分当成绝对真实水平。
> - **再看 $C$**：子系统之间是否均衡。高 $C$ 只说明“接近”，不说明“高水平”。
> - **再看 $T$**：整体发展基础是否高。它能补上 $C$ 不看发展水平的缺口。
> - **最后看 $D$**：系统是否既有均衡关系，又有较高发展水平。$D$ 是描述性协调度，不是政策净效果。
> - **分类和地图只用于展示格局**：自然断点、分位数或等距分类会影响边界，不能把分类线当成自然断裂。
> - **LISA 是扩展读法**：它显示空间关联和时空转移，但空间相关不等于空间溢出因果。

---

## 资料与分析

> [!method-panel] 数据、变量与模型
> | 环节 | 说明 |
> |---|---|
> | 数据结构 | 面板数据，通常为 $N$ 个空间单元 $\times$ $T$ 个年份 $\times$ $m$ 个指标。 |
> | 样本与单位 | 省份、城市、国家、学校系统或其他可持续观测的空间/组织单元。 |
> | 变量或指标 | 每个子系统至少需要若干可解释指标，并说明正向指标与负向指标。 |
> | 模型或统计量 | 标准化指标 $g_{ij}$、子系统水平 $e_j$、耦合度 $C$、综合发展指数 $T$、协调度 $D$。 |
> | 诊断与检验 | 权重敏感性、指标替换、分类阈值敏感性、缺失值处理、异常值和空间自相关检查。 |

> [!software-impl] 软件实现
> | 环节 | 说明 |
> |---|---|
> | 数据处理 | 用 R、Python、Stata 或 Excel 完成指标清洗、正负向识别、min-max 标准化和权重合成。 |
> | 推荐软件 | Python 和 R 适合可复现计算；ArcGIS 或 GeoDa 适合空间可视化和 LISA 扩展；Stata 适合面板数据整理。 |
> | 核心包或命令 | Python 可用 `pandas`、`numpy`、`jenkspy`、`geopandas`；R 可用 `tidyverse`、`classInt`、`sf`、`spdep`。 |
> | 实现流程 | 先生成标准化指标矩阵，再按权重计算 $e_j$，随后计算 $C$、$T$、$D$，最后进行等级分类和地图展示。 |
> | 报告标准 | 报告指标清单、正负向规则、权重来源、标准化范围、等级阈值、软件版本和敏感性检查。 |

> [!formula] Python 计算骨架
> ```python
> import numpy as np
> import pandas as pd
> 
> def minmax_normalize(x, positive=True):
>     denom = x.max() - x.min()
>     if denom == 0:
>         return np.zeros_like(x, dtype=float)
>     if positive:
>         return (x - x.min()) / denom
>     return (x.max() - x) / denom
> 
> # normalized_data shape: n_observations x K_subsystems
> # each subsystem score e_j is already a weighted sum of its indicators
> E = normalized_subsystem_scores
> geo_mean = np.prod(E, axis=1) ** (1 / E.shape[1])
> arith_mean = np.mean(E, axis=1)
> C = geo_mean / arith_mean
> T = np.average(E, axis=1, weights=system_weights)
> D = np.sqrt(C * T)
> ```
>
> 这段代码只展示 $C$ 和 $D$ 的核心计算。完整复现还需要报告指标表、权重向量、缺失值处理和等级分类规则。

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**：多个子系统都有稳定指标，研究目标是比较协同发展水平、空间分异或时间演变。教育-科技-人才、经济-环境-能源、城镇化-生态环境等综合评价问题都适合。
> - **谨慎使用**：指标体系不稳定、权重依据不足、地区之间统计口径不一致、或研究者希望解释因果机制时，需要补充理论解释、稳健性检查或因果识别设计。
> - **不适合使用**：不适合单独回答“哪个子系统导致另一个子系统变化”“某项政策是否提高协调度”或“空间高值是否由邻近地区溢出造成”等因果问题。

---

## 局限性

> [!critique-method] 方法局限
> - **耦合度陷阱**：当子系统均处于低发展水平时，$C$ 可能虚高，必须结合 $T$ 和 $D$ 综合判断。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]
> - **[[Causality|因果性]]缺失**：$D$ 是描述性综合指标，高协调度不等于子系统之间存在因果促进关系。
> - **权重敏感性**：指标权重 $f_i$ 和子系统权重 $\alpha_j$ 会影响 $e_j$、$T$ 和 $D$，不同权重设定可能改变区域排序和等级分类。
> - **分类阈值依赖样本**：自然断点、分位数和等距分类会产生不同的等级边界，地图展示可能放大边界附近地区的差异。
> - **时间可比性问题**：如果标准化范围或权重基于全时段数据，结果隐含时间不变性假设；如果逐年标准化，又会削弱跨年绝对比较。
> - **指标体系主观性**：模型的数学部分看似客观，但指标选择、正负向设定和缺失值处理都带有研究者判断。

---

## 相关理论与方法

> [!frames-ref] 相关理论
> - [[Coupling Coordination Theory]] — 为模型提供系统论解释框架，将教育、科技、人才等对象理解为相互关联的子系统。
> - General Systems Theory — 为“子系统相互作用构成整体状态”的基本假设提供理论背景。

> [!ref-table] 相关方法
> | 方法 | 关系 | 区别 |
> |---|---|---|
> | [[Combined Weighting AHP-EWM]] | 前置或子模块。 | 决定指标权重 $f_i$，不直接计算协调度 $D$。 |
> | [[LISA Time Path]] | 空间分析扩展。 | 分析协调度的时空移动路径，不替代 CCDM 的综合评价。 |
> | [[LISA Spatiotemporal Transition]] | 空间分析扩展。 | 分析局部空间关联类型转移，不直接构建综合指数。 |

---

## 使用此方法的研究

> [!evidence-grid-a] 研究索引
> - [[Argument_Fan_Song_Zhai_2024_RSEE]] — 使用耦合协调模型测度中国 30 个省份教育-科技-人才一体化发展水平，并结合[[LISA Time Path|LISA时空路径]]和[[LISA Spatiotemporal Transition|LISA时空转移]]分析时空格局演变。
