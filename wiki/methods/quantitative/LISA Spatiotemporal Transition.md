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
tags:
  - method/spatial-analysis
  - method/panel-data
  - method/spatiotemporal
related_concepts:
  - "[[Analytic Framework]]"
related_theories: []
related_methods:
  - "[[LISA Time Path]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Fan_Song_Zhai_2024_RSEE]]"
confidence: medium
status: draft
created: 2026-06-12
updated: 2026-06-12
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
> LISA时空转移分析分为转移类型划分和汇总指标计算两个层面。

> [!line-a] 层面一：四种转移类型
> 以相邻两期（$t \rightarrow t+1$）为单位，追踪每个空间单元的象限变化：
> - **Type0**（自身不变-邻域不变）：$LH_t \rightarrow LH_{t+1}$、$HL_t \rightarrow HL_{t+1}$、$HH_t \rightarrow HH_{t+1}$、$LL_t \rightarrow LL_{t+1}$————完全稳定，格局锁定
> - **Type1**（自身变-邻域不变）：$LH_t \rightarrow HH_{t+1}$、$HL_t \rightarrow LL_{t+1}$、$HH_t \rightarrow LH_{t+1}$、$LL_t \rightarrow HL_{t+1}$————仅自身升级或降级
> - **Type2**（自身不变-邻域变）：$LH_t \rightarrow LL_{t+1}$、$HL_t \rightarrow HH_{t+1}$、$HH_t \rightarrow HL_{t+1}$、$LL_t \rightarrow LH_{t+1}$————仅邻居变化
> - **Type3**（自身变-邻域变）：$HL_t \rightarrow LH_{t+1}$、$LH_t \rightarrow HL_{t+1}$、$LL_t \rightarrow HH_{t+1}$、$HH_t \rightarrow LL_{t+1}$————双重变化，进一步分为同向Type3A和反向Type3B
>
> Type3A和Type3B的区分关键在于转移方向是否一致：自身和邻居同时向好（或同时向差）为Type3A；自身向好但邻居向差（或反之）为Type3B。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 69)]]

> [!line-b] 层面二：三项汇总指标
> - **空间凝聚度** $SC = \dfrac{Type0 + Type3A}{m}$：衡量格局的惯性强度，$SC$ 越大格局越稳定
> - **时空流动度** $SF = \dfrac{Type1 + Type2}{m}$：衡量格局的流动性，$SF$ 越大格局越活跃
> - **相对移动率** $p = 1 - \dfrac{\sum p_{i,i}}{k}$：$p = 0$ 表示无任何转移（完全锁定），$p = 1$ 表示所有单元均发生转移（格局解体）。$k = 4$ 为转移矩阵的维度。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 69)]]

---

## 资料与分析

> [!info]
> - **资料类型**：面板数据，需逐年计算LISA值并确定每个空间单元的象限归属
> - **分析策略**：逐年配对构建转移矩阵 → 统计四种转移类型的频次和比例 → 计算SC、SF和p → 可进一步按子系统分别构建转移矩阵以比较不同维度的锁定强度差异
> - **软件工具**：转移矩阵的构建需自行编程（Python/R），LISA值的计算可使用GeoDa或PySAL

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
> - **不提供因果解释**：转移矩阵揭示格局稳定性，但不解释稳定或变化的原因

---

## 相关方法

> [!tip]
> - [[LISA Time Path]] — LISA时空路径从连续几何维度追踪轨迹，LISA时空转移从离散概率维度量化状态变化，两者互补构成ESTDA的完整[[Analytic Framework|分析框架]]
> - Moran's I — 全局和局部Moran's I是LISA时空转移的基础分析层
> - Markov Chain — 空间转移矩阵本质上是一阶Markov转移矩阵在空间分析中的应用

---

## 使用此方法的研究

> [!example]
> - [[Argument_Fan_Song_Zhai_2024_RSEE]] — 使用LISA时空转移分析中国EST耦合协调度的空间格局稳定性，发现Type0占80.2%（$SC = 0.849$，$p = 0.089$），证明存在显著的空间锁定效应；进一步分教育、科技、人才三个子系统对比，发现科技子系统锁定最强（Type0 = 0.814）、人才最弱（Type0 = 0.743）
