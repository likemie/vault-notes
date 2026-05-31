---
title: Solomon Four-Group Design
aliases:
  - Solomon四组设计
  - 所罗门四组设计
  - Solomon four-group
  - Solomon design
summary: "将受试者随机分配到四组的真实验设计，通过操纵前测和处理两个因素来评估前测对处理效果的潜在干扰"
type: method
method_type: quantitative
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Purpose Statement]]"
  - "[[Internal Validity]]"
related_theories: []
related_methods:
  - "[[Factorial Design]]"
  - "[[Random Assignment]]"
  - "[[Analysis of Variance]]"
related_persons: []
related_facts:
  - "[[Campbell Collaboration]]"
related_arguments: []
sources:
  - "[[Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-06-01
updated: 2026-06-01
---

# Solomon Four-Group Design

## 定义

> [!info]
> Solomon 四组设计（Solomon Four-Group Design）是一种真实验设计，是 2 × 2 [[Factorial Design|因子设计]]的特例。它将受试者[[Random Assignment|随机分配]]到四个组中，通过操纵前测（有 vs 无）和处理（有 vs 无）两个因素，来评估前测本身是否会对处理效果产生干扰效应。全部四个组均接受后测（Creswell & Creswell, 2022, Ch8, Example 8.3）。

## 研究程序

> [!example]
> 使用 [[Campbell Collaboration|Campbell]] & Stanley (1963) 符号系统表示：

```
Group A  R ——— O ——— X ——— O    (前测 + 处理 + 后测)
Group B  R ——— O —————————— O    (前测 + 无处理 + 后测)
Group C  R ——————————— X ——— O    (无前测 + 处理 + 后测)
Group D  R ———————————————— O    (无前测 + 无处理 + 后测)
```

> [!abstract] 四组的比较逻辑
> - **A vs B**：在存在前测的条件下，检验处理效果（O₂_A − O₂_B）。
> - **C vs D**：在无前测的条件下，检验处理效果（O_C − O_D）。
> - **A vs C**：检验前测效应——有前测的受试者在后测上是否与无前测的受试者表现不同？
> - 若 A vs B 的处理效果与 C vs D 的处理效果显著不同，则说明前测与处理之间存在交互效应——前测可能增强了或掩盖了处理效果（Creswell & Creswell, 2022, Ch8）。

## 适用场景

> [!success]
> - 当研究者担心前测可能使受试者对处理更加敏感（如前测让受试者意识到[[Purpose Statement|研究目的]]，从而改变其对处理的反应）时，Solomon 四组设计可以分离和评估前测效应。
> - 当研究领域存在关于前测效应的争议或理论关切时，该设计提供了强有力的[[Internal Validity|内部效度]]保障。

## 局限性

> [!warning]
> - 需要四倍的样本量（四组而非两组），资源需求显著增加。
> - 统计分析相对复杂——需要 2 × 2 [[Analysis of Variance|ANOVA]] 或更复杂的混合模型来检验前测 × 处理的交互效应。
> - 在实际教育研究中，同时运行四个组的实验在后勤和伦理上都有较高门槛，因此 Solomon 四组设计的实际使用频率远低于仅后测对照组设计。

## 方法变体与相近方法

> [!tip]
> - vs 仅后测对照组设计（Posttest-Only Control-Group Design） — 仅后测设计通过取消前测来控制前测的混淆效应，但不评估前测效应本身；Solomon 四组设计则同时评估前测的主效应和交互效应。
> - vs [[Factorial Design|因子设计]] — Solomon 四组是 2 × 2 因子设计的特例，但因子设计通常不涉及"是否有前测"作为一个因子——前测作为因子是 Solomon 四组设计的独特之处。

## 来源

- [[Creswell_2022_SAGE]]
