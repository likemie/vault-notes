---
title: Random Sampling
aliases:
  - 随机抽样
  - probability sampling
  - 概率抽样
  - random sample
  - 随机样本
  - simple random sampling
  - 简单随机抽样
  - systematic sampling
  - 系统抽样
  - stratified sampling
  - 分层抽样
  - cluster sampling
  - 整群抽样
  - stage sampling
  - 阶段抽样
  - multi-phase sampling
summary: "从总体中按均等概率选取样本的抽样策略家族，每个个体有均等概率被选中，包括简单随机抽样、系统抽样、随机分层抽样、整群抽样、阶段抽样和多阶段抽样，目的是提升样本代表性并支持统计推论"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 11
method_related_level: 1
method_related_stars: "⭐"
method_related_color: "#dcfce7"
tags:
  - method/sampling
  - quantitative-research
  - survey
related_concepts:
  - "[[Sample Size Determination]]"
  - "[[Study Population and Sample]]"
  - "[[External Validity]]"
  - "[[Causality]]"
  - "[[Internal Validity]]"
  - "[[Response Bias]]"
related_theories: []
related_methods:
  - "[[Systematic Sampling]]"
  - "[[Stratified Sampling]]"
  - "[[Random Assignment]]"
  - "[[Quantitative Research]]"
  - "[[Qualitative Research]]"
  - "[[Cluster Sampling]]"
  - "[[Stage Sampling]]"
  - "[[Multi-phase Sampling]]"
  - "[[Non-probability Sampling]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-06-01
updated: 2026-06-01
---

# Random Sampling

## 定义

> [!info]
> 随机抽样（Random Sampling）是从研究总体中选取样本的一种概率抽样方法——总体中每个个体都有均等的概率被选中。随机抽样的目标是提升样本对总体的代表性，使研究者能够将样本结果推广到更广泛的总体（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022]], Ch8）。

## 研究程序

概率抽样包含多种具体类型，均以某种形式的随机性为基础，因此都具有不同程度的推广性。以下按方法论结构逐类说明。

### 简单随机抽样

> [!step] 简单随机抽样（Simple Random Sampling）
> 总体中每个成员被选中的概率相等，且每次选择完全独立于其他选择。方法：从总体名单（抽样框）中随机抽取所需数量的受试者——可通过抽签或使用随机数表（如 Hopkins et al., 1996: 148–9）。由于概率与随机性，样本应包含与总体特征相似的受试者。局限在于需要完整的总体名单，而这并不总是容易获得（p.155）。

### 系统抽样

> [!step] [[Systematic Sampling|系统抽样]]（Systematic Sampling）
> 简单随机抽样的变体。从总体名单中以系统方式选取受试者——如从 2,000 人中抽取 100 人，每隔 20 人选取一人，起点随机选择。频率间隔公式：
>
> $$f = \frac{N}{sn}$$
>
> 其中 $f$ = 频率间隔，$N$ = 总体人数，$sn$ = 所需样本人数。例如学校有 1,400 名学生，从随机[[Sample Size Determination|样本量]]表中查得需 301 人：$f = 1400 / 301 \approx 5$，即每隔五人选取一人。
>
> **周期性问题（Periodicity）**：若名单排序存在规律性（如先列女性再列男性、或按班级从高能力到低能力排列），系统抽样可能扭曲样本。例如学校每班约 30 人，若每隔 30 人选取，可能几乎全部抽到低能力学生（Calder, 1979）。此外，系统抽样违反了概率抽样的基本前提——每个人有均等被选中的机会（因为被跳过的名字不可能被选中）。缓解方法：确保初始名单和起始点均为随机选择（pp.155–156）。

### 随机分层抽样

> [!step] [[Stratified Sampling|随机分层抽样]]（Random Stratified Sampling）
> 两步过程：（1）识别总体中必须在样本中出现的特征，将总体划分为同质的离散组（层，strata）；（2）在各组内随机抽样。各组大小由研究者判断或参照随机样本量表格确定。
>
> 分层抽样是[[Random Assignment|随机化]]与分类化的有用结合，同时支持[[Quantitative Research|定量研究]]（使用分析和推论统计）和[[Qualitative Research|质性研究]]（针对性接触特定群体）。特征选择应尽量简洁——因素越多，不仅抽样越复杂，样本往往也越大（pp.156–157）。

### 整群抽样

> [!step] [[Cluster Sampling|整群抽样]]（Cluster Sampling）
> 当总体大且广泛分散时，简单随机抽样在行政上不可行。例如要调查全国学生的体能水平——随机选取学生并四处奔波测试完全不切实际。整群抽样选择特定数量的学校（或地理上接近的"群"），测试这些学校中的所有学生。
>
> 需注意整群抽样可能引入偏差——来自重工业区或贫困区的城市整群样本可能不代表所有类型的城市或社会经济群体。因此宁可多取几个群并在每个群内轻度抽样，而非少取群并在每个群内深度抽样（p.157）。

### 阶段抽样

> [!step] [[Stage Sampling|阶段抽样]]（Stage Sampling）
> 整群抽样的延伸——从样本中再抽取样本。例如：随机选择若干学校 → 从各校随机选择若干班级 → 从各班随机选择若干学生。
>
> Morrison（1993: 121–2）提供了一例：某研究者需从 11 所学校 2,000 名 16 岁学生中抽取 322 名。第一阶段：将 11 所学校名称放入帽中抽取 322 次（放回）；第二阶段：要求各校随机选择各自所需人数。随机性在两个阶段中得以保持，大量案例被有效管理。注意此策略假定各校规模相等且足够大，实践中未必成立（pp.157–158）。

### 多阶段抽样

> [!step] [[Multi-phase Sampling|多阶段抽样]]（Multi-phase Sampling）
> 与阶段抽样的关键区别在于各阶段目的不同。阶段抽样全程贯穿着单一的统一目的（如接触特定区域的特定学生群体）；多阶段抽样中每个阶段的目的发生变化——如第一阶段基于地理标准，第二阶段基于经济标准，第三阶段基于政治标准。每个阶段的样本总体都会随之变化（p.158）。

## 概念辨析

> [!example]
> - vs [[Random Assignment|随机分配]]（Random Assignment） — 这是两个经常混淆的概念。随机抽样是关于**谁**进入[[Study Population and Sample|研究样本]]——目标是将样本推广到总体（[[External Validity|外部效度]]）。随机分配是关于已进入样本的受试者**如何**被分配到各实验条件——目标是消除组间系统性偏差并支持[[Causality|因果推断]]（[[Internal Validity|内部效度]]）。一项研究可以同时使用随机抽样和随机分配，也可以只使用其中之一或都不使用（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022]], Ch8）。

## 适用场景

> [!success]
> - 研究目标是从样本结果推广到更广泛的总体时，概率抽样是最理想的选择。
> - 简单随机抽样适合总体名单完整且规模适中的情境。
> - [[Systematic Sampling|系统抽样]]适合有完整名单且需简化操作的大规模抽样。
> - [[Stratified Sampling|随机分层抽样]]适合已知总体关键特征（如性别、社会经济地位）且希望对关键子组进行均衡比较的研究。
> - [[Cluster Sampling|整群抽样]]和[[Stage Sampling|阶段抽样]]适合总体大且广泛分散、行政上难以逐一接触的情境。
> - [[Multi-phase Sampling|多阶段抽样]]适合各研究阶段有不同目的和不同[[Study Population and Sample|目标总体]]的复杂研究设计。

## 局限性

> [!warning]
> - 在实际研究中，获取总体的完整名单往往不可行或成本极高，使真正的简单随机抽样难以实现。
> - [[Systematic Sampling|系统抽样]]的核心风险是周期性（periodicity）——若名单排序存在规律性（如按能力高低排列），系统抽样可能系统性排除某些群体。
> - [[Stratified Sampling|随机分层抽样]]中，层数越多样本越快膨胀；特征选择应尽量简洁。
> - [[Cluster Sampling|整群抽样]]中，少数群落内的同质性可能导致样本不代表总体的多样性——应多取群并在群内轻度抽样。
> - [[Stage Sampling|阶段抽样]]假定各阶段单位（如学校）规模大致相等，实践中未必成立。
> - 即使抽样设计是随机的，低回应率仍可能导致最终样本丧失随机性——拒绝参与者与参与者之间可能存在系统性差异（[[Response Bias|回应偏差]]）。
> - 在教育研究中，[[Non-probability Sampling|便利抽样]]是最常见的选择——需诚实讨论样本对总体的代表性局限。

