---
title: Systematic Sampling
aliases:
  - 系统抽样
  - systematic sample
summary: "从总体名单中以固定间隔选取样本的概率抽样方法，起点随机选择，操作简便但需警惕名单排序中的周期性问题导致样本偏斜"
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
  - "[[Sample Size Determination]]"
related_theories: []
related_methods:
  - "[[Random Sampling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08]]"
confidence: medium
status: draft
created: 2026-06-22
updated: 2026-06-22
---
# Systematic Sampling

## 定义

> [!def] 方法定义
> [[Random Sampling|系统抽样]]（Systematic Sampling）是[[Random Sampling|简单随机抽样]]的变体，以系统而非随机方式从总体名单中选取受试者。从随机起点开始，按固定频率间隔依次选取，直至达到所需[[Sample Size Determination|样本量]]。频率间隔 $f = N / sn$（$N$ 为总体人数，$sn$ 为所需样本人数）。

> [!method-scope] 方法范围
> - **研究对象**：有完整名单（抽样框）的总体
> - **问题类型**：适合需要简化操作的大规模概率抽样
> - **分析单位**：个体、组织或可从名单中识别的任何单位
> - **输出形式**：概率样本，支持统计推广

## 研究程序

> [!proc] 操作步骤
> 1. 获取或构建完整的总体名单，确保名单顺序为随机排列。
> 2. 从[[Random Sampling|随机样本]]量表中确定所需样本人数 $sn$。
> 3. 计算频率间隔 $f = N / sn$。
> 4. 随机选择起始点（第 1 到第 $f$ 名之间）。
> 5. 从起始点开始，每隔 $f$ 人选取一人，直至达到[[Sample Size Determination|样本量]]。

> [!example] 数值实例
> 学校有 $N = 1400$ 名学生，随机样本量表指示需 $sn = 301$ 人，则 $f = 1400 / 301 \approx 5$，即每隔五人选取一人。

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**：有完整且随机排列的总体名单、需要简化操作的大规模[[Random Sampling|概率抽样]]。
> - **谨慎使用**：名单排序存在规律性时。
> - **不适合使用**：无法获取完整名单、名单排序有明显周期性模式且无法重新随机排列时。

## 局限性

> [!method-limits] 方法局限
> - **周期性风险（Periodicity）**（Calder, 1979）：若名单存在规律性排序——如先列全部女生再列全部男生、按班级从高能力到低能力排列——[[Random Sampling|系统抽样]]可能系统性排除某些群体，严重扭曲样本。
> - **违反等概率原则**：被跳过的名字不可能被选中，每个人不具有均等被选中的机会。
> - **缓解方式**：确保初始名单随机排列，起始点随机选择。

## 使用此方法的研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch08|Cohen, Manion & Morrison (2011, Ch. 8)]] — 系统介绍[[Random Sampling|系统抽样]]的操作程序、频率间隔公式和周期性风险。
