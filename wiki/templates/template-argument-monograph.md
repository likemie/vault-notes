---
title: <% tp.file.title %>
authors:
  - "[[Author, A. A.]]"
source_language: en
summary: ""
type: argument
subtype: monograph
publication_type: book
book_title: ""
publication_place: ""
publisher: ""
year:
doi: ""
isbn: ""
citation_aliases: []
citation: ""
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments: []
sources:
  - "[[books/<book-folder>/Source_Name|Source_Name]]"
part_of:
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

---

## 全书定位

> [!monograph-profile] 专著档案
> - **核心对象** 这本书研究什么对象、场域、案例、理论问题或政策问题。
> - **论证类型** 说明它是经验研究、理论建构、方法论著作、政策分析、历史叙事、教材型专著还是批判性著作。
> - **处理粒度** `single-argument` 或 `chapter-arguments`。说明章节细节是累积在本页，还是另建章节 Argument。
> - **材料边界** 说明当前整合依据是全书、部分章节、导论/结论，还是已处理章节。

---

## 研究问题与核心主张

> [!question] 全书问题
> 直接陈述全书要回答的核心问题，综合各章提炼；不要只复述书名，也不要以“本书/作者/研究者”作为常规句子主语。

> [!monograph-thesis] 全书核心主张
> 用一至三句话给出全书对上述问题的核心答案与解释，不在此展开逐章证据。（相关章节，pp. X–Y）

%% 每条信息由一个主模块承载。全书定位写档案；核心主张写答案；工具写分析资源；地图写路径；章节表写导航；跨章综合写章节间的关系与解释；末节写完整证据边界。少量核心引文集中到后部关键引用，不在此重复。 %%

---

## 理论、概念与方法工具

> [!monograph-tools] 理论与概念工具
> - **[[<理论名>]] / [[<概念名>]]** 说明该理论或概念如何贯穿全书，是问题框架、解释机制、类型工具还是批判视角。（p.X）
> - **[[<理论名>]] / [[<概念名>]]** 说明它与其他理论工具的关系。

> [!monograph-method] 研究方法与材料
> - **研究设计** 说明全书的研究设计、材料类型或论证方式。
> - **资料来源** 访谈、档案、统计数据、案例、文本、图像、政策文件或二手文献。
> - **分析策略** 编码、比较、历史追踪、机制分析、模型建构、理论阐释或批判分析。
> - **证据类型** 说明材料适合支持哪一类判断；完整推断边界放在末节。

---

## 全书论证地图

> [!book-argument-map] 全书论证图
> ```mermaid
> flowchart LR
>   A["问题起点"] --> B["理论/概念工具"]
>   B --> C["关键材料"]
>   C --> D["中间机制"]
>   D --> E["核心结论"]
>   D -.边界.-> F["需谨慎处"]
> ```

%% 论证图与 argument-steps 默认择一。若改用步骤，移除上面的图；保留关键前提、证据到结论的中间推论。图已经表达的信息不再另列步骤。 %%

---

## 章节推进

%% chapter-arguments 默认使用以下表格。章节链接骨架由 vault_index.py 维护；填写内容概要和主要关联条目。概述写该章独有内容及在全书中的论证功能，不另设同义的推进线或章节索引。single-argument 第一列可写普通章节名，并在表后保留章节记录。 %%

> [!textbook-overview] 章节导航与论证功能
> | 章节 | 内容概要 | 主要关联条目 |
> |---|---|---|
> | [[Argument_BookFolder_Ch01\|第1章 章节标题]] | 该章独有内容，以及它提出、支持、修正或收束什么问题。 | [[相关条目]] |
> | [[Argument_BookFolder_Ch02\|第2章 章节标题]] | 相对前章新增的证据、机制或解释。 | [[相关条目]] |

%% 缺少内容的占位行在成稿时删除；尚未处理章节只标阅读状态，不猜测其结论。single-argument 可在表后增加简短 ### 第X章；chapter-arguments 将完整章节论证写入独立 Argument。 %%

---

## 跨章综合

%% book-synthesis 与 finding-cards 默认择一。跨章综合必须解释递进、对照、修正或共同机制，不再逐章总结，也不在后面再附同义的综合发现。主题多时用 ### 按问题分组，数量与材料相称。跨章数据确有比较意义时制表；单章数值与完整案例链接主条目。 %%

### <跨章主题的完整判断>

> [!book-synthesis] <章节之间的解释关系>
> - **递进或修正** 说明哪些章节共同支持一个判断，以及后续章节增加、限制或改变了什么。（相关章节，pp. X–Y）
> - **成立条件** 说明哪些材料支持这一解释、在哪些情境下成立；此处保留理解结论必需的限定，完整证据边界统一放在末节。（相关章节，pp. X–Y）

---

## 关键引用

> [!citation-card]- 关键引用
> 中文译文或中文原文。（第X章，p.X）
>
> *Original text or English translation.*

---

## 自述局限与使用边界

> [!book-limits] 自述局限与使用边界
> - **作者自述局限** 只写书中明确自述的局限、边界条件或未来研究方向。
> - **材料边界** 说明样本、案例、时期、地区、文本或资料来源的边界。
> - **推断边界** 说明哪些结论不能由本书材料直接推出。
> - **引用提醒** 说明引用全书 Argument 还是应回到具体章节、页码或章节 Argument。

---

## 来源

%% 只列整本书 source record wikilink。章节 source 写入对应章节 Argument。 %%

- [[books/<book-folder>/Source_Name|Source_Name]]
