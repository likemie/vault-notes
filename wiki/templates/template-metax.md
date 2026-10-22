---
title: template-metax
aliases: []
summary: "Visible Learning MetaX 卡片样式样板：以 Meta-cognition strategies 与 Boredom 真实数据演示（后者含自动核算勘误）"
type: template
tags: []
status: active
created: 2026-10-22
updated: 2026-10-22
---

%% 样板。正式模块由 MetaX 同步脚本生成并插入条目（map <influence_id> <条目路径>），条目中不设标题，放在实证数据表格之后（无实证表格时放在“相关研究”证据卡之前），不手写。
   卡片只写 APA 短引用、变量与数字；篇名、期刊、完整作者存于 metax/metax.json。已入库文献自动显示为链接（本例 Greene et al. 2018）。
   表头代号由 CSS 显示为中文：rate 评级｜ma 元分析数｜k 研究数｜n 学生数｜m 效应数｜d 效应量（按研究数加权，Σkd/Σk）｜du 效应量（未加权）｜rob 稳健性（●×5）｜ref 文献｜var 变量｜e 勘误。
   勘误改 metax/errata.json：单篇在 e 列标 ①②…，整合在总览数值旁标 ⚑。勘误框仅在两种情况下出现：errata.json 有该因素的有来源勘误；或脚本重算总览（元分析数、研究数、学生数、效应数、按研究数加权的 d）与列表不符、发现疑似重复行，即单项相加不等于总览或合计行、加权或未加权平均数重算不符、元分析数与列表行数不符、发现疑似重复行时，此类以 ∑ 标记，每次同步自动重算，不写入 errata.json。 %%

> [!metax] [元认知策略 · Meta-cognition strategies](https://www.visiblelearningmetax.com/influences/view/meta-cognition_strategies)
> 学生学习策略 › 元认知／自我调节学习
>
> | rate | ma | k | n | m | d | du | rob |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | ★★★★ 显著加速 | 22 | 839 | 124,768 | 1,952 | 0.59 | 0.68 | ●●●●● |
>
> > [!metax-ma]- 22 项
> > | ref | var | k | n | m | d | e |
> > | --- | --- | --- | --- | --- | --- | --- |
> > | Haller et al. (1988) | Meta-cognitive training programs in reading | 20 | 1,553 | 20 | 0.71 |  |
> > | Chiu (1998) | Meta-cognitive interventions in reading | 43 | 3,475 | 123 | 0.67 |  |
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

> [!metax] [厌倦 · Boredom](https://www.visiblelearningmetax.com/influences/view/boredom)
> 学生 › 情绪
>
> | rate | ma | k | n | m | d | du | rob |
> | --- | --- | --- | --- | --- | --- | --- | --- |
> | ▼ 负向影响 | 6 | 257 | 116,038 | 1,254 | -0.45 | -0.43 | ●●●●○ |
>
> > [!metax-ma]- 6 项
> > | ref | var | k | n | m | d | e |
> > | --- | --- | --- | --- | --- | --- | --- |
> > | Tze et al. (2016) | Boredom on achievement | 21 | 14,535 | 29 | -0.32 |  |
> > | Trimble et al. (2007) | Boredom on achievement | 27 | NA | 30 | -0.45 | ∑ |
> > | Camacho-Morles et al. (2021) | Boredom on achievement | 25 | 28,410 | 66 | -0.45 |  |
> > | Loderer et al. (2020) | Boredom on achievement | 8 | 1,181 | 14 | -0.43 |  |
> > | Stempfer et al. (2023) | Boredom on achievement | 149 | 71,912 | 1,085 | -0.47 |  |
> > | Trickey & Topping (2007) | Boredom on achievement | 27 | NA | 30 | -0.45 | ∑ |
>
> > [!metax-errata] 2 条
> > - ∑ **自动核算 · 疑似重复** Trimble et al. (2007) 与 Trickey & Topping (2007) 的研究数、效应数与效应量完全相同，疑为同一项元分析重复收录。
> > - ∑ **自动核算 · 剔除重复后** 元分析 5 项，研究数 230，加权平均效应量 -0.45，未加权平均效应量 -0.42（仅供参考，尚未经文献核实）。
