---
title: Item Analysis
aliases:
  - 项目分析
  - 试题分析
  - item discriminability
  - 项目区分度
  - item difficulty
  - 项目难度
  - distractor analysis
  - 干扰项分析
summary: "测验编制过程中对每个项目进行统计分析的方法，包括项目区分度指数、项目难度指数和干扰项效果三项核心分析，是优化测验质量、筛选有效项目的关键技术"
type: concept
domain: "research-methodology"
related_count: 5
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - theme/measurement
  - theme/assessment
  - method/quantitative
related_concepts:
  - "[[Norm-Referenced, Criterion-Referenced, and Domain-Referenced Tests]]"
  - "[[Professional Judgment]]"
related_theories:
  - "[[Item Response Theory]]"
related_methods:
  - "[[Pilot Testing]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]]"
confidence: medium
status: draft
created: 2026-07-24
updated: 2026-07-24
---

# Item Analysis

---

## 定义

> [!def] 核心定义
> 项目分析（item analysis）是在测验编制和[[Pilot Testing|预测试]]阶段对每个测验项目进行的统计分析，目的是确保：（1）项目如预期般运作（标准参照项目合理覆盖领域和标准，常模参照项目展示项目区分度）；（2）项目难度适当；（3）测验可靠（排除不必要的干扰信息和无关线索）（Gronlund & Linn, 1990; Millman & Greene, 1993）。项目分析的理论基础是[[Item Response Theory|项目反应理论]]（IRT）。

> [!concept-lens] 概念透镜
> - **含义** 项目分析不是单一指标，而是对每个项目从区分度、难度和干扰项三个维度进行的多角度质量审查。
> - **用途** 在预测试后帮助研究者淘汰区分度不足、难度不当或干扰项失效的项目，保留质量最好的项目进入正式测验。
> - **边界** 区分度和难度在[[Norm-Referenced, Criterion-Referenced, and Domain-Referenced Tests|常模参照测验]]和标准参照测验中的意义不同——常模参照追求高区分度和中等难度，标准参照不以区分度为核心关注。

---

## 核心要素

### 项目区分度

> [!def] 项目区分度
> 项目区分度（item discriminability）指该项目被高分组学生答对、同时被低分组学生答错的潜力——即项目在多大程度上能有效显示一组学生之间的差异。

**计算公式** 将[[Pilot Testing|预测试]]学生的分数分为高分、中分、低分三组（各 10 人），取高分组和低分组：

$$\text{区分度指数} = \frac{A - B}{N}$$

其中 $A$ = 高分组答对人数，$B$ = 低分组答对人数，$N$ = 两组总人数（通常为 20）。

**判断标准**
- 区分度指数最大值 = 1.00
- 小于 0.67 的项目应首先检查是否存在措辞歧义或暗示线索
- 是否使用低于 0.67 的项目取决于研究者的[[Professional Judgment|专业判断]]
- 在[[Norm-Referenced, Criterion-Referenced, and Domain-Referenced Tests|常模参照测验]]中，区分度至关重要；在标准参照测验中，低区分度不一定意味着项目质量差（可能所有学生都学会了）

> [!example] 区分度计算示例
> 高分组 10 人全部答对（A = 10），低分组 2 人答对（B = 2），N = 20：
>
> 区分度指数 $= \frac{10 - 2}{20} = 0.40$
>
> 该项目的区分度尚可，但低于 0.67 的理想值。

### 项目难度

> [!def] 项目难度
> 项目难度（item difficulty）是答对该项目的学生比例。

**计算公式**

$$\text{难度指数} = \frac{A}{N} \times 100\%$$

其中 $A$ = 答对学生人数，$N$ = 尝试该项目的学生总数。

**判断标准**
- 最大值 = 100%
- 低于 33% 的项目可能过难，高于 67% 的项目可能过易
- 常模参照测验的理想难度约为 50%（Frisbie, 1981）
- 标准参照测验中，难度应与任务或目标匹配：容易的目标应有高难度指数，困难的目标应有低难度指数
- 教学有效的标准参照测验，难度指数可能普遍偏高（Gronlund & Linn, 1990, p. 265）

> [!example] 难度计算示例
> 20 名学生中 12 人答对：难度指数 $= \frac{12}{20} \times 100\% = 60\%$，在 33%–67% 的合理范围内。

### 干扰项分析

> [!def] 干扰项分析
> 干扰项（distractor）是多项选择题中的错误选项。有效干扰项应吸引更多低分组学生而非高分组学生。如果一个选项没有人选择（高低分组均为 0），则该干扰项完全失效。

> [!example] 干扰项效果判断
> | 选项 | 高分组 10 人 | 低分组 10 人 | 结论 |
> |------|-------------|-------------|------|
> | A（正确答案） | 10 | 2 | 正确区分 |
> | B（干扰项） | 0 | 0 | 无效干扰——无人选择 |
> | C（干扰项） | 2 | 10 | 有效干扰——吸引更多低分者 |

---

## 争议与批评

> [!warning] 小样本的限制
> 在小样本上计算区分度和难度指数时，应谨慎对待这些指数，不宜过分信任。项目分析只有在足够大的[[Pilot Testing|预测试]]样本中才能稳定反映项目的真实质量。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch24]] — 教材 24.5 节详细介绍了项目分析的三个核心维度（区分度、难度和干扰项分析），给出计算公式、判断标准和常模参照与[[Norm-Referenced, Criterion-Referenced, and Domain-Referenced Tests|标准参照测验]]中的不同应用原则。
