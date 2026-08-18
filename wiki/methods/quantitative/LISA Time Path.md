---
title: LISA Time Path
aliases:
  - LISA时空路径
  - LISA时间路径
  - Local Indicators of Spatial Association Time Path
summary: "一种将时间维度引入LISA局部空间自相关的探索性时空数据分析方法，通过相对长度和弯曲度两个几何指标追踪各空间单元在Moran散点图上的动态演化轨迹"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 5
method_related_level: 0
method_related_stars: ""
method_related_color: "#dcfce7"
tags:
  - method/spatial-analysis
  - method/panel-data
  - method/spatiotemporal
related_concepts:
  - "[[Flow]]"
  - "[[Variable]]"
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
updated: 2026-06-12T18:30:00
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
> LISA 时空路径的计算建立在传统 LISA 分析之上，核[[Flow|心流]]程为：逐年 LISA 计算 → 提取 Moran 散点坐标轨迹 → 计算几何指标（RL、D、方向）。以下逐步展开。

### 第一步：空间权重矩阵的构建

> [!info]
> 空间权重矩阵 $\mathbf{W}$ 定义了 $n$ 个空间单元之间的"邻居关系"。常见构造方式：
> - **地理距离倒数** $w_{ij} = 1/d_{ij}$（$i \neq j$），距离越近权重越大；$w_{ii} = 0$
> - **经济-地理复合权重** $\theta_{ij} = NL_j \times 1/d_{ij}$（$i \neq j$），引入经济因子 $NL$ 修正地理距离的非对称性——经济强省对弱省的影响权重大于反向。Fan 等（2024）使用此构造，以地区 GDP 衡量 $NL$。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 68)]]
>
> 权重矩阵需按行标准化（每行之和为 1），以确保空间滞后项的量纲一致。

---

### 第二步：逐年 LISA 计算与 Moran 散点图坐标提取

> [!line-a] LISA 统计量
> 对每个年份 $t$，首先计算全局 Moran's I：$I_t = \dfrac{n}{\sum_i \sum_j w_{ij}} \dfrac{\sum_i \sum_j w_{ij}(x_{i,t} - \bar{x}_t)(x_{j,t} - \bar{x}_t)}{\sum_i (x_{i,t} - \bar{x}_t)^2}$。然后计算每个单元的局部 Moran's I（LISA）：$I_{i,t} = z_{i,t} \sum_j w_{ij} z_{j,t}$，其中 $z_{i,t} = (x_{i,t} - \bar{x}_t) / \sigma_t$ 为标准化值。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 68–69)]]

> [!line-b] Moran 散点图坐标
> Moran 散点图以每个单元的标准化值 $z_{i,t}$ 为横轴、空间滞后 $\sum_j w_{ij} z_{j,t}$ 为纵轴。单元 $i$ 在第 $t$ 年的位置记为 $L_{i,t} = (z_{i,t}, \sum_j w_{ij} z_{j,t})$。根据 $(z, Wz)$ 的符号落入四个象限：
> - **HH**（$z > 0, Wz > 0$）：自身高 ─ 邻居高
> - **LH**（$z < 0, Wz > 0$）：自身低 ─ 邻居高
> - **LL**（$z < 0, Wz < 0$）：自身低 ─ 邻居低
> - **HL**（$z > 0, Wz < 0$）：自身高 ─ 邻居低

---

### 第三步：计算相对长度（$RL_i$）

> [!line-a] 公式
> $$RL_i = \dfrac{n \times \sum_{t=1}^{T-1} d(L_{i,t}, L_{i,t+1})}{\sum_{i=1}^{n} \sum_{t=1}^{T-1} d(L_{i,t}, L_{i,t+1})}$$
> 其中 $d(L_{i,t}, L_{i,t+1}) = \sqrt{(z_{i,t+1} - z_{i,t})^2 + (Wz_{i,t+1} - Wz_{i,t})^2}$ 为单元 $i$ 在 Moran 散点图上连续两年位置之间的欧氏距离，$n$ 为空间单元数，$T$ 为年份数。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, pp. 68–69)]]

> [!line-b] 含义
> $RL_i$ 将每个单元的累计移动距离与全国平均水平比较。$RL_i = 1$ 表示该单元移动幅度等于全国均值；$RL_i > 1$ 表示比全国平均更"活跃"（空间关联类型变化大）；$RL_i < 1$ 表示更"稳定"（变化小）。$RL_i$ 捕捉的是"动了多少"的量级差异。

---

### 第四步：计算弯曲度（$D_i$）

> [!line-a] 公式
> $$D_i = \dfrac{\sum_{t=1}^{T-1} d(L_{i,t}, L_{i,t+1})}{d(L_{i,1}, L_{i,T})}$$
> 分子为 22 年间的实际累计移动距离，分母为起点 $(z_{i,1}, Wz_{i,1})$ 到终点 $(z_{i,T}, Wz_{i,T})$ 的直线距离。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 69)]]

> [!line-b] 含义
> $D_i$ 衡量移动路径的"曲折程度"。$D_i \approx 1$ 表示路径近乎直线——方向高度一致（持续上升或持续下降）；$D_i \gg 1$ 表示路径大幅迂回——反复波动、方向不确定。结合 $RL_i$ 可区分四种典型模式：
>
> | $RL_i$ | $D_i$ | 模式 | 含义 |
> |--------|-------|------|------|
> | 低 | 低 | **高质量稳态** | 少动、方向一致——如东部沿海持续上升 |
> | 低 | 高 | 小范围反复 | 移动幅度小但方向来回——原地踏步 |
> | 高 | 低 | 大幅定向迁移 | 虽移动多但方向明确——快速追赶或衰退 |
> | 高 | 高 | **低质量扰动** | 大幅波动且方向反复——受政策周期冲击 |

---

### 第五步：移动方向

> [!line-a] 计算方式
> 对每个单元计算起点到终点的向量 $\vec{v}_i = (z_{i,T} - z_{i,1}, Wz_{i,T} - Wz_{i,1})$，求其方向角 $\theta_i = \arctan2(\Delta Wz, \Delta z)$，$\theta_i \in [-180^\circ, 180^\circ]$。[[Argument_Fan_Song_Zhai_2024_RSEE|(Fan et al., 2024, p. 72)]]

> [!line-b] 解读
> - $0^\circ$–$90^\circ$：自身与邻居协同正向增长（双方均进步）
> - $90^\circ$–$180^\circ$ 和 $270^\circ$–$360^\circ$（即 $-90^\circ$–$0^\circ$）：非协同增长（自身与邻居方向背离）
> - $180^\circ$–$270^\circ$（即 $-180^\circ$–$-90^\circ$）：自身与邻居协同负向增长（双方均退步）

---

## 资料与分析

> [!info] 数据结构
> 输入为面板数据，$n$ 个空间单元 $\times$ $T$ 个年份，含一个综合指标（如耦合协调度 $D$）和空间权重矩阵 $\mathbf{W}_{n \times n}$。权重矩阵的构造是决定 LISA 结果的"隐[[Variable|变量]]"——不同的距离度量和经济因子会导致不同的邻居定义和 LISA 坐标。

> [!info] 软件实现

> [!line-a] GeoDa（推荐 — 图形界面，零代码）
> GeoDa 是 Luc Anselin 团队开发的免费开源空间分析软件，内置 LISA and Moran 散点图功能。操作流程：
> 1. 导入 shapefile 或 GeoJSON 格式的空间数据
> 2. 创建空间权重矩阵（Tools → Weights Manager → 选距离倒数或邻接）
> 3. 对每个截面年份运行 Univariate Local Moran's I → 导出散点图坐标
> 4. 在外部（Python/Excel）整理 22 年的坐标序列，计算 RL 和 D
> 5. 将 RL 和 D 合并回 GeoDa 进行空间可视化
>
> 缺点：需逐年份手动操作，$T$ 大时效率低；RL 和 D 需外部计算。

> [!line-b] PySAL / Python（可编程，批量处理）
> Python 空间分析库 PySAL（`libpysal` + `esda`）可批量计算多截面 LISA：
> ```python
> import libpysal, esda, numpy as np
> 
> # 读取空间权重（Gal/GWT 格式或手动构造）
> w = libpysal.weights.DistanceBand.from_shapefile(
>     "provinces.shp", threshold=1000
> )
> w.transform = 'r'  # 行标准化
> 
> # 逐年计算 LISA
> coords = np.zeros((n, T, 2))  # (单元, 年份, [z, Wz])
> for t in range(T):
>     y = panel_data[:, t]
>     yi = (y - y.mean()) / y.std()  # 标准化 z
>     wy = libpysal.weights.lag_spatial(w, yi)  # 空间滞后 Wz
>     coords[:, t, 0] = yi
>     coords[:, t, 1] = wy
> 
> # 计算 RL 和 D
> steps = np.sqrt(np.diff(coords[:,:,0], axis=1)**2
>               + np.diff(coords[:,:,1], axis=1)**2)
> RL = n * steps.sum(axis=1) / steps.sum()  # shape (n,)
> D = steps.sum(axis=1) / np.sqrt(
>     (coords[:, -1, 0] - coords[:, 0, 0])**2
>   + (coords[:, -1, 1] - coords[:, 0, 1])**2
> )
> ```
>
> - **ArcGIS** 论文明确使用 ArcGIS 10.8 进行 RL、D、移动方向的空间分布图渲染（自然断点法）
> - **R**`spdep` 包提供 `localmoran()` 函数，可配合 `ggplot2` 可视化

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
> - **描述性工具** RL和D是描述性几何指标，提供了格局变化的量化证据，但不能直接解释变化的原因
> - **对空间权重矩阵敏感** RL和D的值依赖于空间权重矩阵的设定，不同权重构造方式可能导致不同结论
> - **象限坐标的精度损失** 将Moran散点图连续坐标压缩为四个象限再追踪，丢失了连续变化信息

---

## 相关方法

> [!tip]-
> - [[LISA Spatiotemporal Transition]] — LISA时空路径关注连续轨迹的几何特征，LISA时空转移关注离散状态间的跳转概率，两者互补
> - Moran's I — 全局和局部Moran's I是LISA时空路径的基础分析层
> - [[Coupling Coordination Model]] — 耦合协调模型提供可被LISA时空路径追踪的综合发展指标

---

## 使用此方法的研究

> [!example]
> - [[Argument_Fan_Song_Zhai_2024_RSEE]] — 使用LISA时空路径追踪中国30个省份EST耦合协调度的22年空间关联演化，计算RL和D揭示东部"高质量稳态"与西部"低质量扰动"的稳定性分化
