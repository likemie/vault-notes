---
title: template-metax
aliases: []
summary: "Visible Learning MetaX 卡片样式样板：以 Meta-cognition strategies 真实数据演示，勘误两条为示例"
type: template
tags: []
status: active
created: 2026-10-22
updated: 2026-10-22
---

%% 样板。正式模块由 MetaX 同步脚本生成并插入条目（map <influence_id> <条目路径>），放在 ## 实证数据 之后的独立 H2，不手写。
   卡片只写 APA 短引用、变量与数字；篇名、期刊、完整作者存于 metax/metax.json。已入库文献自动显示为链接（本例 Greene et al. 2018）。
   表头代号由 CSS 显示为中文：dom 领域｜sub 子领域｜impact 影响判定｜ma 元分析数｜k 研究数｜n 学生数｜m 效应数｜d 效应量｜rob 稳健性｜ref 文献｜var 变量｜e 勘误。
   勘误改 metax/errata.json：单篇在 e 列标 ①②…，整合在总览数值旁标 ⚑。下面两条勘误仅为样式示例。 %%

## Visible Learning MetaX

> [!metax] [Meta-cognition strategies](https://www.visiblelearningmetax.com/influences/view/meta-cognition_strategies)
> | dom | sub | impact | ma | k | n | m | d | rob |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | Student Learning Strategies | Meta-cognitive/self-regulated learning | Potential to considerably accelerate | 22 | 839 | 124,768 | 1,952 | 0.59 ⚑ | 5/5 |
>
> > [!metax-ma]- 22
> > | ref | var | k | n | m | d | e |
> > | --- | --- | --- | --- | --- | --- | --- |
> > | Haller et al. (1988) | Meta-cognitive training programs in reading | 20 | 1,553 | 20 | 0.71 |  |
> > | Chiu (1998) | Meta-cognitive interventions in reading | 43 | 3,475 | 123 | 0.67 | ① |
> > | Fan (1993) | Metacognitive training on reading comprehension | 41 | 3,219 | 223 | 0.56 |  |
> > | Jacob & Parkinson (2015) | Executive functioning | 67 | 15,879 | 67 | 0.63 |  |
> > | Baek (2018) | Metacognitive strategies | 19 | NA | 19 | 0.79 |  |
> > | Fauzan (2003) | Metacognitive strategies on comprehension | 27 | NA | 82 | 0.50 |  |
> > | [[Argument_Greene_2018_JEP\|Greene et al. (2018)]] | Epistemic knowing | 132 | 55,418 | 752 | 0.33 |  |
> > | Yeniad et al. (2013) | Shifting in Math achievement | 20 | 4,596 | 34 | 0.47 |  |
> > | Allan et al. (2014) | Inhibitory control in early years | 75 | 14,424 | 85 | 0.56 |  |
> > | Liu et al. (2021) | Meta-cognitive strategies | 54 | NA | 106 | 0.02 |  |
> > | Muncer et al. (2021) | Metacognition and math | 31 | NA | 31 | 0.80 |  |
> > | Antonio & Prudente (2022) | Metacognition in science | 10 | NA | 10 | 0.81 |  |
> > | Lei et al. (2020) | Computational thinking | 34 | 8,946 | 34 | 0.60 |  |
> > | Scionti et al. (2020) | Cognitive training in executive functioning | 27 | NA | 123 | 0.34 |  |
> > | Wongdaeng & Higgins (2023) | Metacognitive training in EFF | 29 | NA | 29 | 1.33 |  |
> > | Shirvan et al. (2016) | Strategy instruction | 26 | NA | 26 | 0.99 |  |
> > | Sercenia & Prudente (2023) | Metacognitive interventions | 23 | NA | 23 | 1.36 |  |
> > | Yan, Peng, et al. (2024) | Reducing extraneous processing in CAI | 49 | 4,700 | 53 | 0.65 |  |
> > | Eberhart et al. (2024) | Metacognitive interventions | 44 | NA | 44 | 0.34 |  |
> > | Liu (2010) | Metacognitive programs on writing | 11 | 768 | 11 | 0.77 |  |
> > | Cheng et al. (2023) | Computational thinking | 21 | 1,327 | 21 | 0.85 |  |
> > | Akpur (2024) | Metacognitive awareness | 36 | 10,463 | 36 | 0.82 |  |
>
> > [!metax-errata] 2
> > - ⚑ **整合 · 重复计数** 效应量。 示例：两项元分析的原始研究高度重叠，合并时被重复计入。正式勘误须附来源。
> > - ① **单篇 · 数值错误** Chiu (1998) 的研究数：MetaX 记为 43，应为 （核对值）。 示例。正式勘误须附来源。
