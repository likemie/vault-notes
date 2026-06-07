---
title: Heterogeneity
aliases:
  - 异质性
  - 研究间异质性
summary: "元分析中各研究效应量之间超出抽样误差的变异，是判断能否合理合并研究和探索调节变量的核心概念"
type: concept
tags:
- heterogeneity
- meta-analysis
- effect-size
- statistical-synthesis
- methodology
related_concepts:
  - "[[Effect Size]]"
  - "[[Variable]]"
  - "[[Research Question]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
related_persons:
  - "[[Karl Pearson]]"
  - "[[John Hattie]]"
related_arguments: []
sources:
  - "[[Argument_Higgins_2016_RE]]"
confidence: medium
status: draft
created: '2026-06-08'
updated: '2026-06-08'
---

## 定义

> [!info] 定义
> 异质性（Heterogeneity）是[[Meta-analysis|元分析]]中的核心概念，指各研究的[[Effect Size|效应量]]之间超出抽样误差预期的变异。当研究间的效果差异大于仅由样本差异所能解释的程度时，就存在异质性。它表明不同研究可能在干预实施、参与者特征、结果测量或研究设计等方面存在系统性差异（Higgins, 2016, p.32）。
>
> 异质性的存在不一定是问题——它恰恰是[[Meta-analysis|元分析]]区别于简单合并数据的关键特征。[[Karl Pearson|Pearson]]（1904）在最早的跨研究合并分析中就同时关注两个问题：合并数据能否给出更可靠的答案，以及效果变异的原因是什么（Higgins, 2016, p.33）。

---

## 核心机制

> [!abstract] 核心机制
> 异质性的判断和处理是[[Meta-analysis|元分析]]的核心步骤：
>
> **1. 检测异质性**
> - 通过统计检验（如 Q 检验）和可视化（如森林图）判断研究间变异是否超出抽样误差
> - I² 统计量描述异质性占总变异的比例
>
> **2. 探索异质性来源**
> - 调节[[Variable|变量]]分析（moderator analysis）：识别与更大或更小效应相关的研究特征，如学生年龄、干预时长、教师培训程度、特定资源的使用等（Higgins, 2016, p.32）
> - 这一功能对教育研究尤其重要——理解"什么条件下效果更好"往往比"平均效果多大"更有实践价值
>
> **3. 选择统计模型**
> - **固定效应模型（Fixed-Effect Model）**：假设所有研究估计同一个真实[[Effect Size|效应量]]，观察到的差异仅来自抽样误差。按精度（方差倒数）加权——标准误小的研究贡献更大（Higgins, 2016, p.39）
> - **随机效应模型（Random-Effects Model）**：假设每项研究有自己的随机变异，同时考虑研究内和研究间变异。由 Larry Hedges（1983）倡导，DerSimonian & Laird（1986）向医学研究者推广（Higgins, 2016, p.39）
> - 两种模型的选择直接影响汇总估计和推论

---

## 在教育研究中的意义

> [!success] 在教育研究中的意义
> - 异质性是[[Meta-analysis|元分析]]中"苹果和橙子"问题的统计体现——当研究间存在实质性异质性时，汇总的平均[[Effect Size|效应量]]可能掩盖重要差异
> - 教育干预的效果高度依赖情境：不同学生年龄、课程领域、先前成就水平、干预时长、结果测量类型都会产生系统性差异（Higgins, 2016, p.37）
> - [[John Hattie|Hattie]]（2015）对异质性的回应不是否认它，而是要求将异质性转化为[[Research Question|研究问题]]：平均效应必须继续追问调节[[Variable|变量]]（moderator）
> - 在[[Meta-meta-analysis|元-元分析]]层面，异质性问题被进一步放大——不同元分析使用不同的纳入标准、结果测量和研究设计，使跨元分析比较面临更深层的可比性挑战

---

## 局限与争议

> [!warning] 局限与争议
> - 异质性检验的统计效力通常较低——当研究数量少时，即使存在实质性异质性也可能检测不到
> - 调节[[Variable|变量]]分析往往统计效力不足（Valentine et al., 2010, cited in Higgins, 2016, p.38），难以可靠地识别异质性来源
> - 在[[Meta-meta-analysis|元-元分析]]中，每项一级[[Meta-analysis|元分析]]内部的异质性在二级聚合时信息丢失——调节变量信息在聚合过程中系统性消失（Terhart, 2011）

---

## 来源

- [[Argument_Higgins_2016_RE]]
