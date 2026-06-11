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
updated: 2026-06-12T18:30:00
---

# Coupling Coordination Model

---

## 定义

> [!info]
> 耦合协调模型（Coupling Coordination Degree Model, CCDM）是一种基于系统论的多子系统协同发展水平测度方法。它同时评估两个维度：耦合度（$C$）衡量子系统之间相互作用的强度，协调度（$D$）综合评估耦合强度与发展水平的协同演进程度。该模型的核心贡献在于避免了仅使用耦合度可能出现的"低水平高耦合"误判————当所有子系统均处于低发展水平时，耦合度仍可接近最大值。

> [!quote]
> 耦合指两个或多个子系统之间相互影响和相互作用的程度，也可以反映不同子系统之间的约束程度。耦合度可以衡量不同子系统之间的协同发展水平，并在一定程度上描述不同子系统发展水平的差异。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]
> Original: Coupling refers to the extent of mutual influence and interaction among two or more subsystems, and it can also reflect the degree of constraint between different subsystems. The degree of coupling can measure the level of collaborative development between different subsystems.

---

## 研究程序

> [!abstract] 核心公式体系
> 耦合协调模型将 $K$ 个子系统的发展水平 $e_1, e_2, \dots, e_K$ 作为输入，先后计算耦合度 $C$ 和协调度 $D$。以下以最常见的三系统情形（$K=3$）为例说明。

> [!line-a] 步骤一：指标标准化与有序度计算
> 设共有 $n$ 个空间单元、$m$ 个评价指标分布在 $K$ 个子系统中。第一步对原始指标值 $X_{ij}$ 进行 min-max 归一化：
> $$g_{ij} = \frac{X_{ij} - \min X_{ij}}{\max X_{ij} - \min X_{ij}} \quad \text{(正指标)} \qquad g_{ij} = \frac{\max X_{ij} - X_{ij}}{\max X_{ij} - \min X_{ij}} \quad \text{(负指标)}$$
> 归一化后 $g_{ij} \in [0, 1]$。然后按子系统汇总为有序度 $G_j = \sum_{i \in \text{subsystem}_j} f_i g_{ij}$，其中 $f_i$ 为综合权重（$\sum f_i = 1, f_i \geq 0$）。$G_j$ 即为子系统 $j$ 的发展水平 $e_j$。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 66–67)]]

> [!line-b] 权重确定：AHP + EWM + LSD 组合赋权
> 权重 $f_i$ 的确定直接影响 $G_j$ 的值。常用的组合赋权路径：层次分析法（AHP）通过专家两两比较获取主观权重 $v_i$；熵权法（EWM）通过 $e_i = -k\sum p_{ij}\ln p_{ij}$ 计算信息熵获取客观权重 $g_i$；最小二乘决策（LSD）模型求解 $\min H(f) = \sum_i[(g_i-f_i)X_{ij}]^2 + [(v_i-f_i)X_{ij}]^2$，约束 $\sum f_i = 1$，得到折中权重 $f_i$。详见 [[Combined Weighting AHP-EWM|AHP-熵权法组合赋权]]。

---

> [!line-a] 步骤二：计算耦合度 $C$
> 耦合度衡量 $K$ 个子系统之间的离散程度。通用公式：$C = \left[ \dfrac{\prod_{j=1}^{K} e_j}{\left(\frac{1}{K}\sum_{j=1}^{K} e_j\right)^K} \right]^{\frac{1}{K}}$。当 $K=3$ 时：$C = \left[ \dfrac{e_1 \times e_2 \times e_3}{\left(\frac{e_1+e_2+e_3}{3}\right)^3} \right]^{\frac{1}{3}}$。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]

> [!line-b] 数学直觉
> 分子是几何平均值（$\sqrt[3]{e_1 e_2 e_3}$）的立方，分母是算术平均值（$\frac{e_1+e_2+e_3}{3}$）的立方，开三次方后 $C$ 实质是几何均值与算术均值之比。由均值不等式可知几何均值 $\leq$ 算术均值，因此 $C \in [0, 1]$。当 $e_1 = e_2 = e_3$ 时两者相等，$C = 1$（完美耦合）；值差异越大，几何均值越小于算术均值，$C$ 趋近于 $0$。这一结构源自物理学中的容量耦合（Capacitive Coupling）概念——系统间的协同程度取决于它们的"对齐"程度。

> [!warning] 耦合度陷阱
> 当 $e_1 = e_2 = e_3 = 0.1$（三个子系统均处于极低水平）时，$C = 1$（完美耦合），但这显然不是研究者期望的"高协同发展"。仅用 $C$ 无法区分"共同繁荣的高水平耦合"和"共同贫困的低水平耦合"。因此必须引入协调度 $D$ 进行修正。

---

> [!line-a] 步骤三：计算协调度 $D$
> $D = \sqrt{C \times T}$，其中 $T = \sum_{j=1}^{K} \alpha_j e_j$ 为加权综合发展指数，$\alpha_j$ 为各子系统重要性权重（$\sum \alpha_j = 1$）。当各子系统同等重要时，$\alpha_1 = \alpha_2 = \alpha_3 = 1/3$。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 67–68)]]

> [!line-b] 为何用几何平均（$\sqrt{C \times T}$）而非算术平均（$(C+T)/2$）
> 几何平均具有天然的"短板惩罚"特性。假设 $C=0.9$（高耦合）但 $T=0.2$（低发展），算术平均 $(0.9+0.2)/2 = 0.55$ 会掩盖 $T$ 的严重不足；而几何平均 $\sqrt{0.9 \times 0.2} \approx 0.42$ 被拉低至接近 $T$ 的水平。反之亦然——$T=0.9$ 但 $C=0.2$ 时，几何平均同样压低得分。只有 $C$ 和 $T$ 同时达到较高水平时 $D$ 才得高分——这正是"协调发展"的数学含义：既不能偏废耦合性，也不能忽视各自的发展水平。

> [!line-a] 步骤四：等级划分
> 得到每个空间单元每年的 $D$ 值后，需将其划分为便于解读的等级。常用方法：**自然断点法（Natural Breaks / Jenks）**：通过最小化组内方差、最大化组间方差自动寻找最优断点——ArcGIS 10.8 内置此功能。替代方案包括等间距法（固定间隔）和分位数法（每级等量单元）。等级数量通常取 3（低-中-高）或 5（低-较低-中等-较高-高），依据研究需要和数据分布特征确定。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 68)]]

---

## 资料与分析

> [!info] 数据结构
> 输入为面板数据：$N$ 个空间单元 $\times$ $T$ 个年份 $\times$ $m$ 个指标。每个子系统至少需要 3–6 项指标覆盖其主要维度，指标需包含正向指标（越大越好）和负向指标（越小越好）以便 min-max 归一化区分处理。所有指标必须在全样本范围内标准化而非分组标准化。

> [!info] 软件实现
> 耦合协调模型不依赖单一商业软件，以下为常用实现路径：

> [!line-a] Python（推荐 — 可复现、可扩展）
> 使用 `numpy` 和 `pandas` 即可完整实现。核心代码结构：
> ```python
> import numpy as np
> import pandas as pd
> 
> # 1. Min-max 归一化
> def minmax_normalize(X, positive=True):
>     if positive:
>         return (X - X.min()) / (X.max() - X.min())
>     return (X.max() - X) / (X.max() - X.min())
> 
> # 2. 有序度：加权求和
> G = normalized_data @ weights  # shape: (n_units, n_years, K)
> 
> # 3. 耦合度 C — K=3
> geo_mean = np.prod(G, axis=-1) ** (1/3)
> arith_mean = np.mean(G, axis=-1)
> C = (geo_mean / arith_mean)  # 等价于完整公式
> 
> # 4. 协调度 D
> T = np.average(G, axis=-1, weights=alphas)
> D = np.sqrt(C * T)
> 
> # 5. 自然断点 — 使用 jenkspy 库
> from jenkspy import JenksNaturalBreaks
> jnb = JenksNaturalBreaks(n_classes=3)
> labels = jnb.fit_predict(D.flatten())
> ```

> [!line-b] Stata / MATLAB / R 等其他工具
> - **Stata**：通过 `generate`、`egen` 和循环命令实现归一化和公式计算，适合不熟悉 Python 的研究者，缺点是循环效率低
> - **MATLAB**：矩阵运算天然适合批量计算 $C$ 和 $D$，语法与 Python/NumPy 高度相似
> - **R**：可使用 `tidyverse` + `BAMMtools`（含 `getJenksBreaks` 函数）实现 Jenks 自然断点分级
> - 论文明确使用的可视化工具为 **ArcGIS 10.8**，利用其内置的自然断点法进行地图分级渲染

> [!line-a] 计算复杂度
> 设 $N$ 个单元 $\times$ $T$ 个年份。每单元每年需计算 $K$ 个子系统有序度（$O(K \cdot m)$ 加权求和）、$C$（$O(K)$ 几何与算术均值）、$D$（$O(1)$）。总复杂度为 $O(NTKm)$。中国 30 省 $\times$ 22 年 $\times$ 15 指标 $\times$ 3 系统，全部计算在 Python 中瞬间完成（毫秒级）。自然断点分级在 $N=30$ 时计算也极快。瓶颈通常在数据清洗和指标权重确定阶段。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 66–68)]]

---

## 适用场景

> [!success]
> 适合回答"多个系统之间的协同发展程度如何？在哪些区域/时间段协同水平较高或较低？"这类综合评价问题。尤其适合以下场景：
> - 教育、科技、人才等社会子系统的耦合协调评价
> - 经济-环境-能源等可持续发展系统评价
> - 城镇化与生态环境的交互关系测度
> - 不适合回答[[Causality|因果性]]问题————高 $D$ 值不能推断因果关系，可能由第三个共同因素同时驱动

---

## 局限性

> [!warning]
> - **耦合度陷阱**：当子系统均处于低发展水平时 $C$ 可能虚高，必须结合 $D$ 综合判断。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 67)]]
> - **[[Causality|因果性]]缺失**：$D$ 是描述性指标而非因果推断工具，高耦合协调度不等于存在因果关系
> - **权重敏感性**：$T$ 中子系统权重 $\alpha$、$\beta$、$\gamma$ 的选择影响 $D$ 值，不同权重设定可能导致不同等级划分
> - **时间不变性假设**：当权重基于全时段数据计算时，未考虑指标重要性随时间的变化

---

## 相关理论

> [!tip]
> - General Systems Theory — 耦合协调模型以系统论为理论基础，将各子系统视为相互关联、相互制约的组成部分
> - [[Coupling Coordination Theory]] — 耦合协调理论为模型提供了机制层面的解释框架

---

## 使用此方法的研究

> [!example]
> - [[Argument_Fan_Song_Zhai_2024_RSEE]] — 使用耦合协调模型测度中国30个省份教育-科技-人才（EST）一体化发展水平，结合[[LISA Time Path|LISA时空路径]]和[[LISA Spatiotemporal Transition|空间转移矩阵]]分析时空格局演变
