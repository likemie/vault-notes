---
title: Stage Sampling
aliases:
  - 阶段抽样
  - stage sample
  - multi-stage sampling
summary: "整群抽样的延伸，从样本中再抽取样本的多层概率抽样方法，每阶段保持随机性，从一般走向具体、从广走向窄"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 0
method_related_level: 0
method_related_stars: "☆"
method_related_color: "#dcfce7"
tags:
  - method/sampling
  - quantitative-research
related_concepts:
  - "[[Sampling Error]]"
related_theories: []
related_methods:
  - "[[Random Sampling]]"
  - "[[Cluster Sampling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
confidence: medium
status: draft
created: 2026-06-22
updated: 2026-06-22
---
# Stage Sampling

## 定义

> [!def] 方法定义
> [[Random Sampling|阶段抽样]]（Stage Sampling）是[[Cluster Sampling|整群抽样]]的延伸，从样本中再抽取样本。例如随机选择若干学校（第一阶），从各校随机选择若干班级（第二阶），从各班随机选择若干学生（第三阶）。每阶段均保持随机性，全程贯穿单一的统一目的。核心逻辑是从一般走向具体、从广走向窄、从大走向小。

> [!method-scope] 方法范围
> - **研究对象**：嵌套在多层组织中的个体（如学生嵌套于班级、班级嵌套于学校）
> - **问题类型**：需要从大规模、多层总体中抽取概率样本的研究
> - **分析单位**：各阶段单位不同（学校、班级、个体）
> - **输出形式**：多阶段概率样本

## 研究程序

> [!proc] 操作步骤
> 1. 列出第一阶单位（如所有学校），随机抽取所需数量。
> 2. 在每个被抽中的第一阶单位内，列出第二阶单位（如班级），随机抽取。
> 3. 继续向下直至达到目标个体层面。
> 4. 每阶段均采用随机选择（如抽签、随机数表）。

> [!example] Morrison（1993: 121–2）的实例
> 某研究者需从 11 所中学的 2,000 名 16 岁学生中抽取 322 名。第一阶段：将 11 所学校名称放入帽中抽取 322 次（放回）；第二阶段：各校按被抽中次数随机选择相应数量的学生。随机性在两个阶段均得以保持，2,000 人的大规模被有效管理。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**：总体嵌套在多层组织结构中、无法获取完整的个体层面名单。
> - **谨慎使用**：假定各阶段单位规模大致相等且足够大——实践中未必成立。
> - **不适合使用**：各阶段单位规模差异极大且无合适校正方法时。

## 局限性

> [!method-limits] 方法局限
> - **规模假定**：假定各阶段单位（如学校）规模大致相等，实践中未必成立。
> - **累积误差**：每[[Random Sampling|阶段抽样]]均引入[[Sampling Error|抽样误差]]，多阶段累积可能使最终标准误增大。
> - **缓解方式**：在分析中使用多水平模型或调查加权方法校正。

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 介绍阶段抽样与 Morrison（1993）的操作实例。
