---
title: template-metax
aliases: []
summary: "Visible Learning MetaX 模块样式：由 scripts/metax_sync.py 生成并插入条目，不手写"
type: template
tags: []
status: active
created: 2026-10-22
updated: 2026-10-22
---

%% 本模块由 `scripts/metax_sync.py map <influence_id> <条目路径>` 生成，放在 `## 实证数据` 之后的独立 H2。
   卡片只写 APA 短引用、变量与数字；篇名、期刊、完整作者存于 metax/metax.json。
   表头代号由 CSS 显示为中文：dom 领域｜sub 子领域｜impact 影响判定｜ma 元分析数｜k 研究数｜n 学生数｜m 效应数｜d 效应量｜rob 稳健性｜ref 文献｜var 变量｜e 勘误。
   勘误改 metax/errata.json：单篇在 e 列标 ①②…，整合在总览数值旁标 ⚑。 %%

## Visible Learning MetaX

> [!metax] [<Influence>](https://www.visiblelearningmetax.com/influences/view/<influence_id>)
> | dom | sub | impact | ma | k | n | m | d | rob |
> | --- | --- | --- | --- | --- | --- | --- | --- | --- |
> | <Domain> | <Sub-Domain> | <Impact on Student Achievement> | 0 | 0 | 0 | 0 | 0.00 ⚑ | 0/5 |
>
> > [!metax-ma]- <元分析行数>
> > | ref | var | k | n | m | d | e |
> > | --- | --- | --- | --- | --- | --- | --- |
> > | [[Argument_Author_Year_Journal\|Author et al. (Year)]] | <Variable> | 0 | NA | 0 | 0.00 |  |
> > | Author & Author (Year) | <Variable> | 0 | 0 | 0 | 0.00 | ① |
>
> > [!metax-errata] <勘误条数>
> > - ⚑ **整合 · <类型>** <字段>：MetaX 记为 <值>，应为 <值>。<说明>（[[Argument_Author_Year_Journal|Author, Year, p. X]]）
> > - ① **单篇 · <类型>** Author & Author (Year) 的<字段>：MetaX 记为 <值>，应为 <值>。（[[Argument_Author_Year_Journal|Author, Year, p. X]]）
