---
title: LISA Time Path
aliases:
  - LISA时空路径
  - LISA时间路径
  - Local Indicators of Spatial Association Time Path
summary: "一种将时间维度引入LISA局部空间自相关的探索性时空数据分析方法，通过相对长度和弯曲度两个几何指标追踪各空间单元在Moran散点图上的动态演化轨迹"
type: method
method_type: quantitative
tags:
  - method/spatial-analysis
  - method/panel-data
  - method/spatiotemporal
related_concepts: []
related_theories: []
related_methods:
  - "[[LISA Spatiotemporal Transition]]"
  - "[[Coupling Coordination Model]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Fan_Song_Zhai_2024_RSEE]]"
confidence: medium
status: draft
created: 2026-06-12
updated: 2026-06-12
---

# LISA Time Path

---

## 定义

> [!info]
> LISA时空路径（LISA Time Path）是探索性时空数据分析（Exploratory Spatiotemporal Data Analysis, ESTDA）的核心方法之一。它将时间维度引入传统的LISA（局部空间自相关指标），追踪每个空间单元在Moran散点图上多年的移动轨迹，通过相对长度和弯曲度两个几何指标刻画局部空间关联格局的动态演化特征。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 68)]]

> [!quote]
> 基于ESTDA模型，LISA时空路径将时间维度纳入LISA以实现动态交互。LISA时空路径可以通过相对长度和弯曲度来计算。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 68)]]
> Original: Based on the ESTDA model, the LISA time path incorporates the temporal dimension into the LISA to realize dynamic interaction. The LISA time path can be calculated by relative length and tortuosity.

---

## 研究程序

> [!abstract]
> LISA时空路径的计算建立在传统的LISA分析基础之上，增加了时间维度的追踪。

> [!line-a] 基础步骤：LISA分析
> 对每个年份计算全局Moran's I和局部LISA值，将每个空间单元映射到Moran散点图的四个象限之一：HH（自身高-邻居高）、LH（自身低-邻居高）、LL（自身低-邻居低）、HL（自身高-邻居低）。

> [!line-b] 核心指标一：相对长度（Relative Length, $RL_i$）
> $RL_i = \dfrac{n \times \sum_{t=1}^{T-1} d(L_{i,t}, L_{i,t+1})}{\sum_{i=1}^{n} \sum_{t=1}^{T-1} d(L_{i,t}, L_{i,t+1})}$，其中 $n$ 为空间单元数、$T$ 为时间跨度、$d(L_{i,t}, L_{i,t+1})$ 为单元 $i$ 从 $t$ 年到 $t+1$ 年在Moran散点图上的移动距离。$RL_i > 1$ 表示该单元的空间关联类型比全国平均更活跃，$RL_i < 1$ 表示更稳定。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 68–69)]]

> [!line-b] 核心指标二：弯曲度（Tortuosity, $D_i$）
> $D_i = \dfrac{\sum_{t=1}^{T-1} d(L_{i,t}, L_{i,t+1})}{d(L_{i,t_1}, L_{i,T})}$，即实际移动总路径长度与起点-终点直线距离的比值。$D_i$ 越接近 $1$ 表示移动方向越一致（持续上升或持续下降），$D_i$ 越大表示路径越曲折（反复波动、方向不确定）。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 69)]]

> [!line-b] 辅助指标：移动方向
> 通过象限法划分移动方向：$0^\circ$–$90^\circ$ 为本地与邻域协同正向增长，$90^\circ$–$180^\circ$ 和 $270^\circ$–$360^\circ$ 为非协同增长，$180^\circ$–$270^\circ$ 为协同负向增长。

---

## 资料与分析

> [!info]
> - **资料类型**：面板数据，需包含各空间单元多年的指标值，以及空间权重矩阵（地理距离或经济-地理复合距离）
> - **分析策略**：先逐年计算LISA值 → 提取每个单元在Moran散点图上的坐标序列 → 计算RL和D → 按自然断点法分为高、中、低三级进行可视化
> - **软件工具**：GeoDa、PySAL（Python空间分析库）、ArcGIS

---

## 适用场景

> [!success]
> 适合回答"空间格局的稳定性和演化方向如何？哪些区域的空间关联类型变化最活跃？"等问题。尤其适用于：
> - 长期面板数据的空间格局演化分析
> - 区域发展收敛/发散趋势的识别
> - 区分"稳健进步"（低RL + 低D）和"无效波动"（高RL + 高D）两种增长模式

---

## 局限性

> [!warning]
> - **描述性工具**：RL和D是描述性几何指标，提供了格局变化的量化证据，但不能直接解释变化的原因
> - **对空间权重矩阵敏感**：RL和D的值依赖于空间权重矩阵的设定，不同权重构造方式可能导致不同结论
> - **象限坐标的精度损失**：将Moran散点图连续坐标压缩为四个象限再追踪，丢失了连续变化信息

---

## 相关方法

> [!tip]
> - [[LISA Spatiotemporal Transition]] — LISA时空路径关注连续轨迹的几何特征，LISA时空转移关注离散状态间的跳转概率，两者互补
> - Moran's I — 全局和局部Moran's I是LISA时空路径的基础分析层
> - [[Coupling Coordination Model]] — 耦合协调模型提供可被LISA时空路径追踪的综合发展指标

---

## 使用此方法的研究

> [!example]
> - [[Argument_Fan_Song_Zhai_2024_RSEE]] — 使用LISA时空路径追踪中国30个省份EST耦合协调度的22年空间关联演化，计算RL和D揭示东部"高质量稳态"与西部"低质量扰动"的稳定性分化
