---
title: Combined Weighting AHP-EWM
aliases:
  - AHP-熵权法组合赋权
  - AHP-EWM Combined Weighting Method
  - 主客观组合赋权
summary: "一种综合主观层次分析法（AHP）与客观熵权法（EWM）的指标赋权方法，通过最小二乘决策（LSD）模型最小化主客观权重偏差，平衡专家判断与数据变异两种信息来源"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 3
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
cssclasses:
  - method-manual
tags:
  - method/quantitative
  - method/model
  - method/weighting
  - method/composite-index
  - method/decision-analysis
related_concepts:
  - "[[Reliability]]"
related_theories: []
related_methods:
  - "[[Coupling Coordination Model]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Fan_Song_Zhai_2024_RSEE]]"
confidence: medium
status: draft
created: 2026-06-12
updated: 2026-11-22
---

---

> [!def] Combined Weighting AHP-EWM
> AHP-熵权法组合赋权（Combined Weighting AHP-EWM）是一种将主观赋权和客观赋权相结合的多指标权重确定方法。它分别采用层次分析法（Analytic Hierarchy Process, AHP）获取基于专家判断的主观权重，采用熵权法（Entropy Weight Method, EWM）获取基于数据变异程度的客观权重，再通过最小二乘决策（Least Square Decision, LSD）模型求解综合权重，使综合权重与两种来源权重的总偏差最小。输入为标准化后的指标数据矩阵与专家两两比较判断，输出为满足 $\sum f_j = 1, f_j \geq 0$ 的综合权重向量 $f$，可进一步用于加权合成子系统有序度。[[Argument_Fan_Song_Zhai_2024_RSEE\|(Fan et al., 2024, pp. 66–67)]]

> [!method-scope] 方法范围
> - **测量或估计对象** 综合评价指标体系中各指标的相对重要性。
> - **问题类型** 评价与测度，为综合指数或[[Coupling Coordination Model\|耦合协调模型]]提供权重输入。
> - **分析单位** 指标；被评价对象可为地区、年份或系统。
> - **输入数据** $m$ 个评价对象在 $n$ 项指标上的观测矩阵 $X_{ij}$，以及专家对指标的两两重要性判断。
> - **输出形式** 主观权重向量 $v$、客观权重向量 $g$ 与综合权重向量 $f$。

> [!citation-card] 最小二乘决策模型的作用
> 研究采用 AHP 与 EWM 计算权重，并建立最小二乘决策（LSD）模型，把指标判断决策结果的偏差控制在较小范围内。[[Argument_Fan_Song_Zhai_2024_RSEE\|(Fan et al., 2024, p. 67)]]
>
> *The AHP and EWM are used to calculate the weights. The least square decision (LSD) model is established to control the deviation of the judgment index decision results in a small range.*

---

> [!method-position] 方法定位
> - **构念效度** AHP 权重反映专家对指标重要性的判断，EWM 权重反映指标在样本中的离散程度；两者都只是指标真实重要性的近似。EWM 可能赋予实际不重要但变异大的指标过高权重，AHP 结果则依赖专家背景和判断质量。
> - **研究者判断** 专家人选与打分标度、指标正负向设定、标准化方式，以及 LSD 中对主客观偏差的惩罚设定。
> - **有效性标准** AHP 判断矩阵的一致性、权重对专家组成与样本时段的敏感性，以及综合指数结果的稳健性。
> - **不声称回答的问题** 权重只表示指标在合成时的相对贡献，不能说明指标之间的因果关系。

> [!method-stack] 方法层级
> - **上位方法** 多准则决策分析与综合评价方法。
> - **前置步骤** 指标体系构建与极差标准化。
> - **变体与扩展** 子模块可替换为其他主观赋权法或客观赋权法；LSD 也可改为对主客观偏差设置不等权重的组合模型，用于处理两类权重可靠性不等的情形。

---

> [!formula-set]- 公式链总览
> ```mermaid
> flowchart LR
>   A["原始指标矩阵 X"] --> B["极差标准化"]
>   B --> C["EWM 客观权重 g"]
>   E["专家两两比较"] --> D["AHP 主观权重 v"]
>   C --> F["LSD 综合权重 f"]
>   D --> F
>   F --> G["加权合成有序度 G"]
> ```

> [!formula-step] 步骤一　指标极差标准化
> $$x'_{ij} = \frac{X_{ij} - \min X_{ij}}{\max X_{ij} - \min X_{ij}}\ (\text{正向}), \qquad x'_{ij} = \frac{\max X_{ij} - X_{ij}}{\max X_{ij} - \min X_{ij}}\ (\text{负向})$$
>
> **这个公式在做什么** 把量纲不同的原始指标值转换为 $[0, 1]$ 区间内的无量纲值，消除测量方法和单位的影响。[[Argument_Fan_Song_Zhai_2024_RSEE\|(Fan et al., 2024, p. 66)]]
>
> **符号说明**
> - $X_{ij}$：第 $i$ 个评价对象在第 $j$ 项指标上的原始值。
> - $x'_{ij}$：标准化后的指标值。
>
> **数学直觉** 以该指标的最小值为起点、极差为单位重新度量；负向指标（如失业率）先反转方向，使数值越大始终代表表现越好。
>
> > [!example]- 手算示例
> > 示例：某正向指标在 3 个地区的取值为 10、20、30，则标准化值为 $0$、$0.5$、$1$。若为负向指标，标准化值为 $1$、$0.5$、$0$。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | 取值 0 与 1 | 分别对应该指标在样本中表现最差和最好的对象。 |
> > | 注意 | 零值与熵权计算 | 标准化后出现 0 时，熵权法中的 $p \ln p$ 需按 $0$ 处理或做平移，否则对数无定义。 |

> [!formula-step] 步骤二　AHP 主观权重
> $$A v = \lambda_{\max} v$$
>
> **这个公式在做什么** 专家对 $n$ 项指标两两比较重要性（通常使用 1–9 标度法）构造判断矩阵 $A$，取其最大特征值对应的特征向量并归一化，得到主观权重向量 $v$。
>
> **符号说明**
> - $A$：判断矩阵，元素 $a_{jk}$ 表示指标 $j$ 相对指标 $k$ 的重要程度，且 $a_{kj} = 1/a_{jk}$。
> - $\lambda_{\max}$：判断矩阵的最大特征值。
> - $v$：归一化后的主观权重向量。
>
> **数学直觉** 若专家判断完全一致，$a_{jk} = v_j / v_k$，此时权重向量恰为判断矩阵的特征向量；特征向量法从带有判断误差的矩阵中提取最接近这一比例结构的权重。
>
> > [!example]- 手算示例
> > 示例：两项指标，专家认为指标 1 比指标 2 稍重要，记 $a_{12} = 3$，则 $A = \begin{pmatrix} 1 & 3 \\ 1/3 & 1 \end{pmatrix}$。最大特征值 $\lambda_{\max} = 2$，对应特征向量归一化后 $v = (0.75, 0.25)$。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $v_j$ 较大 | 专家整体认为该指标更重要。 |
> > | 注意 | 过程透明度 | 需报告专家数量、背景及评判过程，否则 AHP 部分的严谨性无法评估。[[Argument_Fan_Song_Zhai_2024_RSEE\|(Fan et al., 2024, p. 71)]] |

> [!formula-step] 步骤三　EWM 客观权重
> $$p_{ij} = \frac{x'_{ij}}{\sum_{i=1}^{m} x'_{ij}}, \quad e_j = -\frac{1}{\ln m} \sum_{i=1}^{m} p_{ij} \ln p_{ij}, \quad g_j = \frac{1 - e_j}{\sum_{k=1}^{n} (1 - e_k)}$$
>
> **这个公式在做什么** 计算每项指标在样本中的信息熵 $e_j$，以信息效用值 $1 - e_j$ 归一化得到客观权重向量 $g$。
>
> **符号说明**
> - $p_{ij}$：对象 $i$ 在指标 $j$ 上的取值占比。
> - $e_j$：指标 $j$ 的熵值，系数 $1/\ln m$ 使其落在 $[0, 1]$。
> - $g_j$：指标 $j$ 的客观权重。
>
> **数学直觉** 各对象取值越接近，熵值越接近 1，指标提供的区分信息越少；取值差异越大，熵值越低，信息效用值越高，权重越大。
>
> > [!example]- 手算示例
> > 示例：3 个对象在某指标上的占比为 $p = (0.2, 0.3, 0.5)$。
> > $e = -\frac{1}{\ln 3}(0.2 \ln 0.2 + 0.3 \ln 0.3 + 0.5 \ln 0.5) \approx 0.937$，信息效用值 $1 - e \approx 0.063$。
> > 再与其余指标的信息效用值一起归一化，即得该指标的客观权重。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $g_j$ 较大 | 该指标在样本中离散程度高，对区分评价对象贡献大。 |
> > | 注意 | 变异不等于重要 | 变异大但实质意义有限的指标可能被赋予过高权重；权重也会随样本范围和时段改变。 |

> [!formula-step] 步骤四　LSD 综合权重与加权合成
> $$\min H(f) = \sum_{i=1}^{m} \sum_{j=1}^{n} \left\{ \left[(g_j - f_j) X_{ij}\right]^2 + \left[(v_j - f_j) X_{ij}\right]^2 \right\}, \quad \text{s.t.}\ \sum_{j=1}^{n} f_j = 1,\ f_j \geq 0$$
>
> **这个公式在做什么** 在权重和为 1 的约束下，求使综合权重 $f$ 与客观权重 $g$、主观权重 $v$ 的加权偏差平方和最小的解；所得 $f$ 再用于合成子系统有序度 $G = \sum_j f_j x'_{j}$。[[Argument_Fan_Song_Zhai_2024_RSEE\|(Fan et al., 2024, pp. 66–67)]]
>
> **符号说明**
> - $v$、$g$、$f$：主观、客观与综合权重向量。
> - $X_{ij}$：指标数据，作为偏差的放大系数。
> - $H(f)$：主客观偏差平方和。
>
> **数学直觉** 记 $S_j = \sum_i X_{ij}^2$，目标函数可写为 $\sum_j S_j[(g_j - f_j)^2 + (v_j - f_j)^2]$。对 $f_j$ 求导并引入约束的拉格朗日乘子，由 $\sum v_j = \sum g_j = 1$ 可推出乘子为 0，最优解为 $f_j^* = (v_j + g_j)/2$。在这一目标函数设定下，数据 $X_{ij}$ 只改变 $H$ 的大小，不改变最优权重的位置；LSD 结果等价于主客观权重的算术平均，这也是该模型对两类权重施以同等惩罚的直接体现。
>
> > [!example]- 手算示例
> > 示例：3 项指标，$v = (0.5, 0.3, 0.2)$，$g = (0.2, 0.5, 0.3)$。
> > 综合权重 $f^* = (0.35, 0.40, 0.25)$。
> > 若 $S = (8, 6, 7)$，则 $H(f^*) = 0.5 \times [8 \times 0.3^2 + 6 \times 0.2^2 + 7 \times 0.1^2] = 0.515$；改用纯 AHP 或纯 EWM 权重时 $H = 1.03$。
>
> > [!formula-reading] 结果解读与注意事项
> > | 类型 | 要点 | 说明 |
> > |---|---|---|
> > | 读法 | $f_j$ 位于 $v_j$ 与 $g_j$ 之间 | 主客观权重分歧越大，综合权重相对任一来源的偏离越大，$H$ 的最小值也越高。 |
> > | 注意 | 对称惩罚 | 模型对主观与客观偏差施以同等惩罚，未考虑两者[[Reliability\|可靠性]]可能不等；需要偏向某一来源时应改用加权组合。 |
>
> > [!geogebra] LSD 偏差平方和最小化动态模拟
> > - **上方柱状图** 3 项指标的 AHP 主观权重 $v$（蓝）、EWM 客观权重 $g$（绿）与试探权重 $f(t)$（橙），黑色横线为 LSD 最优权重 $f^* = (v + g)/2$。
> > - **下方曲线** 横轴为试探系数 $t$（$t = 0$ 为纯 EWM，$t = 1$ 为纯 AHP），纵轴为偏差平方和 $H(t)$，橙点为当前位置。
> > - **滑块 AHP 权重 v₁** 调整指标 1 的主观权重（0.10–0.80），$v_2 : v_3$ 固定为 3 : 2；客观权重与 $S_j$ 为示例值。
> > - **滑块 试探系数 t** 沿 $f(t) = t v + (1 - t) g$ 移动试探权重。
> > - **右侧面板** 显示 $v$、$g$、$f(t)$、$f^*$ 与 $H$ 的读数。
> >
> > 拖动 $t$ 观察 $H$ 在 $t = 0.5$ 处取得最小值，橙色柱与黑色横线重合；再拖动 $v_1$ 观察主客观分歧扩大时曲线整体抬升，但最小值位置不变。
> >
> > ![[wiki/assets/geogebra/combined_weighting_ahp_ewm.ggb]]

> [!software-impl] 软件实现
> - **数据来源** 统计年鉴或统计公报等面板数据，需统一指标口径与正负向。
> - **核心包或命令** Python 的 `numpy` 完成标准化、熵权与特征向量计算，`scipy.optimize.minimize` 可用于数值求解 LSD 并核对闭式解。
> - **实现流程** 标准化 → AHP 判断矩阵求特征向量 → 熵权计算 → LSD 求综合权重 → 加权合成有序度。
> - **报告标准** 报告专家数量与背景、判断矩阵及其一致性检验、指标正负向设定、主观权重、客观权重与综合权重的完整列表。

> [!formula] Python 计算骨架
> ```python
> import numpy as np
>
> def minmax(X, positive):
>     """极差标准化；positive 为布尔数组，False 表示负向指标"""
>     lo, hi = X.min(axis=0), X.max(axis=0)
>     return np.where(positive, (X - lo) / (hi - lo), (hi - X) / (hi - lo))
>
> def entropy_weights(Z, eps=1e-12):
>     """熵权法客观权重 g"""
>     m = Z.shape[0]
>     P = Z / Z.sum(axis=0)
>     e = -np.sum(P * np.log(P + eps), axis=0) / np.log(m)
>     d = 1 - e
>     return d / d.sum()
>
> def ahp_weights(A):
>     """AHP 主观权重 v：最大特征值对应的特征向量"""
>     vals, vecs = np.linalg.eig(A)
>     w = np.abs(vecs[:, np.argmax(vals.real)].real)
>     return w / w.sum()
>
> def lsd_weights(v, g):
>     """LSD 目标函数 sum_j S_j[(g_j-f_j)^2+(v_j-f_j)^2] 在 sum f = 1 下的闭式解"""
>     return (v + g) / 2
>
> # 示例
> v = np.array([0.5, 0.3, 0.2])
> g = np.array([0.2, 0.5, 0.3])
> print(lsd_weights(v, g))  # [0.35 0.4  0.25]
> ```

> [!method-stack] 变量与诊断
> - **数据结构** 横截面或面板指标矩阵（$m$ 个对象 × $n$ 项指标）。
> - **变量** 正向与负向评价指标；输出为指标权重与加权合成的有序度。
> - **识别假设** 指标体系完整覆盖评价对象；指标重要性在研究时段内不变；主客观两类权重同等可靠。
> - **诊断与检验** AHP 一致性检验、权重对专家组成与样本时段的敏感性分析、替换赋权方法后的排序稳健性。

---

> [!method-fit] 适用判断
> - **适合使用** 构建综合评价指标体系时需要确定指标权重，且领域专家知识与充分数据同时可用；单一赋权方法难以令人信服；指标体系中同时包含易于量化的硬指标和难以量化的软指标（如教育关注度、技术复杂度）。[[Argument_Fan_Song_Zhai_2024_RSEE\|(Fan et al., 2024, pp. 66–67)]]
> - **谨慎使用** AHP 专家过程和评判质量不透明时，组合赋权可能实际退化为以 EWM 为主的客观驱动模式，组合的方法论意义随之减弱。
> - **不适合使用** 推断指标之间的因果关系，或在指标重要性随时间明显变化的长时段中套用单一固定权重。

---

> [!method-limits] 方法局限
> - **测量偏误** 若未报告专家数量、背景及评判过程，AHP 方法论的严谨性无法评估。[[Argument_Fan_Song_Zhai_2024_RSEE\|(Fan et al., 2024, p. 71)]]
> - **可比边界** 组合权重基于全时段数据计算，未考虑指标重要性随时间推移的变化；EWM 权重随样本范围改变，跨研究的权重不可直接比较。
> - **误用风险** LSD 对主观和客观权重偏差施以同等惩罚，但两者的[[Reliability\|可靠性]]在实际中可能不等；按上述目标函数，其解等于两类权重的算术平均，容易被误读为经过数据优化的独立结果。
> - **补救方式** 公开专家判断过程与一致性检验，进行分时段权重估计与敏感性分析，或按可靠性差异为主客观偏差设置不同权重。

---

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Coupling Coordination Model]] | 下游方法 | 组合赋权常与耦合协调模型配合使用，前者确定指标权重，后者计算系统协同水平。 |
> | [[Reliability]] | 相关概念 | LSD 对两类权重同等惩罚，隐含主客观信息来源可靠性相等的假设。 |

---

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Fan_Song_Zhai_2024_RSEE|Fan et al. (2024)]] — 使用 AHP-EWM-LSD 组合赋权确定 15 项教育、科技与人才评价指标的权重，为[[Coupling Coordination Model\|耦合协调模型]]提供综合权重输入。
