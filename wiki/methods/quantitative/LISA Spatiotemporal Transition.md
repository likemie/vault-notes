---
title: LISA Spatiotemporal Transition
aliases:
  - LISA时空转移
  - LISA Spatiotemporal Transition Matrix
  - 空间转移矩阵
  - LISA时空跃迁
summary: "一种基于Moran散点图像限转移矩阵的探索性时空数据分析方法，通过Type0-Type3四种转移类型量化空间关联格局的惯性强度和流动性，揭示空间锁定与路径依赖特征"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 4
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
tags:
  - method/spatial-analysis
  - method/panel-data
  - method/spatiotemporal
related_concepts:
  - "[[Hypothesis]]"
  - "[[Causality]]"
  - "[[Analytic Framework]]"
related_theories: []
related_methods:
  - "[[Coding in Qualitative Research]]"
  - "[[LISA Time Path]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Fan_Song_Zhai_2024_RSEE]]"
confidence: medium
status: draft
created: 2026-06-12
updated: 2026-06-12T18:30:00
---

# LISA Spatiotemporal Transition

---

## 定义

> [!info]
> LISA时空转移（LISA Spatiotemporal Transition）是探索性时空数据分析（ESTDA）的核心方法之一。它通过构建空间转移矩阵（Spatiotemporal Transition Matrix），追踪各空间单元在相邻年份之间在Moran散点图四个象限（HH、LH、LL、HL）间的转移行为，将转移分为四种类型（Type0–Type3），并通过空间凝聚度（$SC$）、时空流动度（$SF$）和相对移动率（$p$）三个汇总指标量化空间格局的惯性强度和流动性。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 68–69)]]

> [!quote]
> LISA时空转移可以更好地描述不同地理单元之间的空间关联和动态转移特征。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 72)]]
> Original: The LISA spatiotemporal transition can better describe the spatial association and dynamic transition characteristics between different geographical units.

---

## 研究程序

> [!abstract]
> LISA 时空转移分析分为四个步骤：象限[[Coding in Qualitative Research|编码]] → 构建转移频率矩阵 → 分类计数 → 计算汇总指标。

### 第一步：象限编码

> [!info]
> 对每个年份 $t$，将 $n$ 个空间单元按其 Moran 散点图坐标 $(z_{i,t}, \sum_j w_{ij} z_{j,t})$ 的符号编码为四类之一：HH（$+$, $+$）、LH（$-$, $+$）、LL（$-$, $-$）、HL（$+$, $-$）。编码后的数据为一个 $n \times T$ 的分类矩阵 $Q$，每个元素 $Q_{i,t} \in \{\text{HH}, \text{LH}, \text{LL}, \text{HL}\}$。

### 第二步：构建转移频率矩阵

> [!line-a] 一阶 Markov 转移矩阵
> 将 $n$ 个单元在连续两年 $(t, t+1)$ 之间的象限变化视为一阶 Markov 转移过程。对于全部 $T-1$ 个时间步，共产生 $n \times (T-1)$ 次转移观测。统计从状态 $a$ 转移到状态 $b$ 的频次，构成 $4 \times 4$ 转移频率矩阵 $\mathbf{M}$：
>
> | $t$ \ $t+1$ | HH | LH | LL | HL |
> |-------------|-----|-----|-----|-----|
> | **HH** | $n_{\text{HH} \to \text{HH}}$ | $n_{\text{HH} \to \text{LH}}$ | $n_{\text{HH} \to \text{LL}}$ | $n_{\text{HH} \to \text{HL}}$ |
> | **LH** | $n_{\text{LH} \to \text{HH}}$ | $n_{\text{LH} \to \text{LH}}$ | $n_{\text{LH} \to \text{LL}}$ | $n_{\text{LH} \to \text{HL}}$ |
> | **LL** | $n_{\text{LL} \to \text{HH}}$ | $n_{\text{LL} \to \text{LH}}$ | $n_{\text{LL} \to \text{LL}}$ | $n_{\text{LL} \to \text{HL}}$ |
> | **HL** | $n_{\text{HL} \to \text{HH}}$ | $n_{\text{HL} \to \text{LH}}$ | $n_{\text{HL} \to \text{LL}}$ | $n_{\text{HL} \to \text{HL}}$ |

> [!line-b] 对角线与非对角线的含义
> 对角线元素 $n_{a \to a}$ 对应 Type0：单元停留在相同象限（格局锁定）。非对角元素按转移模式归入不同的 Type。转移频率矩阵可通过除以行和转换为转移概率矩阵 $\mathbf{P}$，其中 $p_{a \to b} = n_{a \to b} / \sum_{c} n_{a \to c}$。

---

### 第三步：四种转移类型的频次统计

> [!line-a] 形式化定义
> 根据自身（Local）和邻域（Neighbor）在转移前后的变化，将 $\mathbf{M}$ 的 16 个单元格归类为四种类型。设单元 $i$ 在 $t$ 年和 $t+1$ 年的象限分别为 $Q_t$ 和 $Q_{t+1}$，对应 Moran 坐标 $(z_t, Wz_t)$ 和 $(z_{t+1}, Wz_{t+1})$：
> - **Type0** = $Q_t = Q_{t+1}$：自身不变、邻域不变（对角线 4 项）
> - **Type1**：$z$ 符号变化、$Wz$ 符号不变（4 项：LH→HH, HH→LH, HL→LL, LL→HL）
> - **Type2**：$z$ 符号不变、$Wz$ 符号变化（4 项：LH→LL, LL→LH, HH→HL, HL→HH）
> - **Type3**：$z$ 和 $Wz$ 符号均变化（4 项：HL→LH, LH→HL, LL→HH, HH→LL）

> [!line-b] Type3A vs Type3B 的区分
> Type3 进一步分为两个子类。Type3A（同向）：自身和邻居的 Moran 坐标同时增大或同时减小（$z$ 和 $Wz$ 变化方向一致）——如 LL→HH（自身和邻居均转为高值）。Type3B（反向）：自身和邻居的变化方向相反——如 HH→LL 或 HL→LH。Type3A 纳入空间凝聚度（$SC$），因为同向变化意味着整体格局在移动但内部相对关系保持了一定一致性。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 69)]]

---

### 第四步：三项汇总指标

> [!line-a] 数学定义
> 设总转移次数 $m = n \times (T-1)$：
> $$SC = \frac{\text{Type0} + \text{Type3A}}{m} \qquad SF = \frac{\text{Type1} + \text{Type2}}{m} \qquad p = 1 - \frac{\sum_{i=1}^{4} p_{i,i}}{4}$$
> 其中 $p_{i,i}$ 是转移概率矩阵 $\mathbf{P}$ 的对角元素（即 $\mathbf{M}$ 各行中 Type0 的比例）。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 69)]]

> [!line-b] 解读
> - **$SC$（空间凝聚度）** $\in [0, 1]$：格局的惯性强度。$SC \to 1$ 意味着绝大多数转移属于 Type0 或 Type3A——格局高度稳定（如 Fan 等报告的 EST 整体 $SC = 0.849$）
> - **$SF$（时空流动度）** $\in [0, 1]$：格局的流动性。$SF \to 1$ 意味着频繁发生自身或邻居的单方面变化——格局处于重组的活跃期
> - **$p$（相对移动率）** $\in [0, 1]$：基于对角线概率的对照指标。$p = 0$ 表示 $\mathbf{P}$ 是单位矩阵——所有单元永远停留在同一象限（完全锁定）；$p = 1$ 表示对角元素全为 $0$——没有任何单元保持在同一象限（格局完全解体）。$p$ 值与 $SC$ 高度负相关但并非简单互补，因为 $p$ 仅用对角线信息而 $SC$ 额外计入 Type3A
>
> 通常 $SC + SF < 1$，因为 Type3B（反向双重变化）未被两者计入——Type3B 是独立的剩余类别。

### 第五步：分子系统对比

> [!info]
> LISA 时空转移的一个关键扩展是对同一面板数据按不同发展维度（如教育、科技、人才三个子系统）分别计算转移矩阵和汇总指标。通过比较各子系统的 $SC$、$SF$、$p$ 值，可识别哪一维度的空间锁定最强、哪一维度最具流动性——这为政策干预的优先级排序提供了直接的经验依据。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 73)]]

---

## 资料与分析

> [!info] 数据结构
> 输入为 $n$ 个空间单元 $\times$ $T$ 个年份的象限标签矩阵 $Q_{n \times T}$（$Q_{i,t} \in \{0,1,2,3\}$，分别对应 HH/LH/LL/HL），以及可选的子系统标签（用于分子系统分析）。标签矩阵通过对各年份 Moran 散点图坐标[[Coding in Qualitative Research|编码]]生成。

> [!info] 软件实现

> [!line-a] Python 实现
> ```python
> import numpy as np
> 
> # Q: (n, T) 整数矩阵, 0=HH, 1=LH, 2=LL, 3=HL
> n, T = Q.shape
> 
> # 构建 4×4 转移频率矩阵
> M = np.zeros((4, 4), dtype=int)
> for t in range(T - 1):
>     for a in range(4):
>         for b in range(4):
>             M[a, b] += np.sum((Q[:, t] == a) & (Q[:, t+1] == b))
> 
> # Type 计数
> Type0 = np.trace(M)  # 对角元素之和
> 
> # Type1: z变 Wz不变
> Type1 = (M[1,0] + M[0,1] +   # LH↔HH
>          M[3,2] + M[2,3])    # HL↔LL
> 
> # Type2: z不变 Wz变
> Type2 = (M[1,2] + M[2,1] +   # LH↔LL
>          M[0,3] + M[3,0])    # HH↔HL
> 
> # Type3: 双重变化
> Type3 = (M[3,1] + M[1,3] +   # HL↔LH
>          M[2,0] + M[0,2])    # LL↔HH
> 
> # 汇总指标
> total = n * (T - 1)
> SC = (Type0 + Type3A) / total   # Type3A需根据具体转移方向判定
> SF = (Type1 + Type2) / total
> P = M / M.sum(axis=1, keepdims=True)  # 转移概率矩阵
> p = 1 - np.trace(P) / 4
> 
> print(f"Type0={Type0/total:.3f} Type1={Type1/total:.3f} "
>       f"Type2={Type2/total:.3f} Type3={Type3/total:.3f}")
> print(f"SC={SC:.3f} SF={SF:.3f} p={p:.3f}")
> ```

> [!line-b] 实现注意事项
> - **Type3A vs Type3B**：需根据转移方向手动判定——LL→HH（同向好）和 HH→LL（同向差）均为 Type3A，HL→LH 和 LH→HL 为 Type3B
> - **分子系统对比**：对外层循环包装——对每个子系统分别运行为 Q 赋值，独立构造 M 并计算指标
> - **零行处理**：如果某行之和为 0（某象限从未出现），需在计算 P 时跳过该行（或填充 NaN）
> - **统计检验**：可对转移矩阵做 $\chi^2$ 独立性检验（原[[Hypothesis|假设]]：转移与起始象限无关），以判断转移是否显著偏离随机期望。同样可检验不同子系统之间的转移概率差异

---

## 适用场景

> [!success]
> 适合回答"空间格局的惯性有多强？是否存在路径依赖和空间锁定？不同子系统（如教育、科技、人才）的空间锁定强度有何差异？"等问题。尤其适用于：
> - 检验区域发展是否存在"富者愈富、穷者愈穷"的马太效应
> - 评估政策干预是否改变了既有的空间格局
> - 比较不同发展维度的空间流动性和固化程度

---

## 局限性

> [!warning]
> - **离散化信息损失**：将空间关联信息压缩为四个象限的离散状态，忽略了连续坐标的渐变信息
> - **对空间权重矩阵敏感**：象限归属依赖于空间权重矩阵的构造方式，不同权重设定可能导致不同转移矩阵结果
> - **短时波动与长期趋势的混淆**：Type1或Type2的单次转移是短期波动还是长期趋势的起点，转移矩阵本身无法区分
> - **不提供[[Causality|因果]]解释**：转移矩阵揭示格局稳定性，但不解释稳定或变化的原因

---

## 相关方法

> [!tip]-
> - [[LISA Time Path]] — LISA时空路径从连续几何维度追踪轨迹，LISA时空转移从离散概率维度量化状态变化，两者互补构成ESTDA的完整[[Analytic Framework|分析框架]]
> - Moran's I — 全局和局部Moran's I是LISA时空转移的基础分析层
> - Markov Chain — 空间转移矩阵本质上是一阶Markov转移矩阵在空间分析中的应用

---

## 使用此方法的研究

> [!example]
> - [[Argument_Fan_Song_Zhai_2024_RSEE]] — 使用LISA时空转移分析中国EST耦合协调度的空间格局稳定性，发现Type0占80.2%（$SC = 0.849$，$p = 0.089$），证明存在显著的空间锁定效应；进一步分教育、科技、人才三个子系统对比，发现科技子系统锁定最强（Type0 = 0.814）、人才最弱（Type0 = 0.743）
