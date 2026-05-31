---
title: Pre-Experimental Designs
aliases:
  - 前实验设计
  - pre-experiments
  - one-shot case study
  - 单组后测设计
  - one-group pretest-posttest design
  - 单组前后测设计
  - static group comparison
summary: "研究单一组并实施干预的实验设计类型，不设对照组或对照组不等价，内部效度最低"
type: method
method_type: quantitative
tags:
  - method/experimental
  - quantitative-research
  - design-type
related_concepts:
  - "[[Internal Validity]]"
  - "[[Causality]]"
related_theories: []
related_methods:
  - "[[Experimental Research]]"
  - "[[Random Assignment]]"
  - "[[Quasi-Experimental Designs]]"
related_persons: []
related_facts:
  - "[[Campbell Collaboration]]"
related_arguments: []
sources:
  - "[[Creswell_2022_SAGE]]"
confidence: medium
status: draft
created: 2026-05-31
updated: 2026-05-31
---

# Pre-Experimental Designs

## 定义

> [!info]
> 前实验设计（Pre-Experimental Designs）是[[Experimental Research|实验研究]]中[[Internal Validity|内部效度]]最低的一类设计。这类设计研究单一组并实施干预，不设对照组与实验组进行比较，或使用的比较组不等价（Creswell & Creswell, 2022, Ch8）。

## 方法变体

> [!example]
> 前实验设计包含以下四种主要变体（Creswell & Creswell, 2022, Ch8, Example 8.1），使用 [[Campbell Collaboration|Campbell]] & Stanley (1963) 的经典符号系统（X = 处理暴露，O = 观察或测量）：

### 一次性个案研究（One-Shot Case Study）

一组接受处理后进行测量：

```
Group A  X ———————————————— O
```

这是最弱的设计，无前测、无对照组，无法判断变化是否由处理引起。

### 单组前后测设计（One-Group Pretest–Posttest Design）

一组在前后测之间接受处理：

```
Group A  O1 ——— X ——— O2
```

有前后比较，但无对照组，无法排除历史、成熟等[[Internal Validity|内部效度]]威胁。

### 静态组比较（Static Group Comparison）

处理后选取比较组，两组均接受后测：

```
Group A  X ———————————————— O
Group B  ——————————————————— O
```

增加比较组，但两组不等价（非[[Random Assignment|随机分配]]），无法确定前测等价性。

### 替代处理非等价组后测设计（Alternative Treatment Posttest-Only With Nonequivalent Groups）

与静态组比较类似，但比较组接受不同的处理：

```
Group A  X1 ———————————————— O
Group B  X2 ———————————————— O
```

可以比较两种处理，但因缺乏随机分配和基线测量，因果解释非常受限。

## 适用场景

> [!success]
> - 初步探索性研究中，当资源和条件不足以实施真实验时。
> - 教学情境中用于初步评估教学干预的效果。
> - 作为更严格实验设计的预备阶段（Creswell & Creswell, 2022, Ch8）。

## 局限性

> [!warning]
> - [[Internal Validity|内部效度]]极低：缺乏[[Random Assignment|随机分配]]、对照组和／或前测，几乎无法排除替代性因果解释。
> - 单组设计无法区分处理效果与自然成熟、历史事件、回归均值等威胁。
> - 不适合做出[[Causality|因果推断]]（[[Campbell Collaboration|Campbell]] & Stanley, 1963; 引自 Creswell & Creswell, 2022, Ch8）。

## 方法变体与相近方法

> [!tip]
> - [[Quasi-Experimental Designs]] — 准实验设计增加了对照组和时间序列观测，[[Internal Validity|内部效度]]高于前实验设计。
> - [[Experimental Research]] — 真实验通过[[Random Assignment|随机分配]]获得最高的内部效度。

## 来源

- [[Creswell_2022_SAGE]]
