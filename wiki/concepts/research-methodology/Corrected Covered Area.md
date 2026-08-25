---
title: Corrected Covered Area
aliases:
  - 校正覆盖面积
  - CCA
  - 校正覆盖面积矩阵
  - 覆盖面积
  - Covered Area
  - Corrected Covered Area Matrix
summary: "伞状综述与二阶元分析中用于量化系统评价间初级研究重复包含程度的标准化重叠率指标，通过排除初级文献首次计数的校正公式以 0–100% 测度文献冗余度与假阳性风险"
type: concept
domain: "research-methodology"
related_count: 18
related_level: 1
related_stars: "⭐"
related_color: "#bfdbfe"
tags:
  - statistics/meta-analysis
  - methodology/systematic-review
  - method/meta-meta-analysis
related_concepts:
  - "[[Primary and Secondary Documents]]"
  - "[[Document]]"
  - "[[Standard Error]]"
  - "[[Variable]]"
  - "[[Study Population and Sample]]"
related_theories: []
related_methods:
  - "[[Umbrella Review]]"
  - "[[Meta-meta-analysis]]"
  - "[[Meta-analysis]]"
related_instruments:
  - "[[AMSTAR]]"
  - "[[GROOVE]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Unal_2026_JECR]]"
confidence: high
status: draft
created: 2026-08-25
updated: 2026-08-25
---

# Corrected Covered Area

---

## 定义

> [!def] 核心定义
> 校正覆盖面积（Corrected Covered Area, CCA）是由 Pieper et al. (2014) 提出、用于在[[Umbrella Review|伞状综述]]（Umbrella Review）与[[Meta-meta-analysis|二阶元分析]]（Second-Order [[Meta-analysis]], SOMA）中**定量评估多个已发表系统评价或元分析之间初级实证研究重叠程度的标准化统计指标**。该指标通过从总纳入频次中扣除[[Primary and Secondary Documents|初级文献]]的基准计数值，消除了综述数量与研究总量本身对覆盖率的被动稀释或抬升效应，以 $0\%–100\%$ 的标准化比率精确测度[[Primary and Secondary Documents|初级文献]]重复被纳入的冗余强度。[[Argument_Unal_2026_JECR|(Ünal et al., 2026, pp. 1373–1375)]]

> [!concept-lens] 概念透镜
> - **测量对象** 跨多个一阶[[Meta-analysis|元分析]]或系统评价的初级研究引用矩阵（Citation Matrix）。
> - **核心功能** 揭示二阶证据库中的[[Document|文献]]重复包含程度，量化因重复计算同一批受试者样本而导致的[[Standard Error|标准误]]虚假收缩与假阳性检验膨胀风险。
> - **应用决策** 为研究者筛选、合并或剔除高重叠一阶元分析提供客观的数学门槛（通常以 $CCA > 10\%$ 作为不可接受的高重叠排除界限）。

---

## 数学原理与计算公式

> [!formula-step] 公式推导与[[Variable|变量]]界定
> 在包含 $c$ 项系统评价/[[Meta-analysis|元分析]]、共涉及 $r$ 篇不重复初级研究的伞状[[Document|文献]]集中：
>
> 1. **未校正覆盖面积（Covered Area, CA）**
>    $$CA = \frac{N}{r \cdot c}$$
>    其中 $N$ 为交叉引用矩阵中的总勾选数（即所有元分析纳入初级研究数量的总和，$\sum_{j=1}^c n_j$），$r \cdot c$ 为矩阵可能存在的最大勾选总格数。未校正指标的缺陷在于：当 $c$ 很大时，即便存在大量重复，$CA$ 也会因分母膨胀而被动呈现极低数值。
>
> 2. **校正覆盖面积（Corrected Covered Area, CCA）**
>    $$CCA = \frac{N - r}{r \cdot c - r} = \frac{N - r}{r(c - 1)}$$
>
> **公式参数含义**
> - $N$ 纳入初级研究的总频次（含重复计数，$\sum n_j$）；
> - $r$ 独立不重复初级研究的总篇数（矩阵的行数）；
> - $c$ 纳入的一阶元分析或系统评价总篇数（矩阵的列数）；
> - 分子 $N - r$ 表示扣除每篇[[Primary and Secondary Documents|初级文献]]必须出现一次的“基准出现”后，实际发生的**多余重复引用总数**；
> - 分母 $r(c - 1)$ 表示在当前矩阵规模下，所有初级文献在全部剩余元分析中均被重复引用的**理论最大可能重复总数**。

---

## 解释区间与判定阈值

> [!contrast-table] CCA 重叠程度四级判定准则（Pieper et al., 2014; Bracchiglione et al., 2022）
> | CCA 数值区间 | 重叠程度定性分级 | 证据冗余与方法学风险 | 推荐处理策略与决策规程 |
> |---|---|---|---|
> | **$0\% \le CCA < 5\%$**（$< .05$） | **轻微重叠（Slight overlap）** | 初级研究基本独立，重复计数对二阶合并效应量与方差影响极微。 | 无需剔除研究，直接采用经典加权模型进行二阶合成。 |
> | **$5\% \le CCA < 10\%$**（$.05–.09$） | **中等重叠（Moderate overlap）** | 存在局部代表性文献重合，置信区间存在微弱假阳性偏向。 | 报告重叠矩阵，实施亚组敏感性分析以验证结论稳健性。 |
> | **$10\% \le CCA < 15\%$**（$.10–.14$） | **高度重叠（High overlap）** | 核心实证证据被多次重复赋予权重，联合标准误显著虚假收缩。 | **触发剔除阈值** 优先保留方法学质量更高（如 [[AMSTAR]] 得分高）或发表时间更新的元分析，剔除冗余项。 |
> | **$CCA \ge 15\%$**（$\ge .15$） | **极高重叠（Very high overlap）** | 绝大部分[[Meta-analysis\|元分析]]共享相同的底层数据池，二阶综合退化为伪重复。 | 严禁直接进行合并计算；必须采用微观完全去重或借助 [[GROOVE]] 工具重构证据网络。 |

---

## 方法论价值与防范偏差功能

> [!warrant]- 为什么[[Meta-meta-analysis|二阶元分析]]必须报告并控制 CCA
> 1. **破除抽样独立性假定破产危机** 经典二阶固定/随机效应合并模型的数学充要条件是各一阶单元在初级样本上互不重叠（Wecker et al., 2016）。无视重叠会导致相同的经典[[Study Population and Sample|研究样本]]被赋予不成比例的双重甚至三重方差权重。
> 2. **克服主观选择偏差** 过去[[Umbrella Review|伞状综述]]常依赖研究者主观经验判断综述是否相似；CCA 提供了标准化、可复现的数学标尺。
> 3. **与可视化工具协同集成** 配合基于 Excel 与 R 语言的 [[GROOVE]]（Graphical Representation of Overlap for OVErviews）工具，CCA 不仅能计算全数据集的总体覆盖度，更能生成两两配对的 CCA 交叉热力图，精准定位重叠发生的[[Document|文献]]节点（Bracchiglione et al., 2022; [[Argument_Unal_2026_JECR|Ünal et al., 2026]]）。
