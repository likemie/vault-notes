---
title: <% tp.file.title %>
authors:
  - "[[Author, A. A.]]"
summary: ""
type: argument
subtype: monograph
publication_type: book
book_title: ""
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
related_persons: []
related_facts: []
related_arguments: []
sources:
  - "[[Source_Name]]"
part_of:
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

---

## 全书定位

> [!monograph-profile] 专著档案
> - **核心对象**：这本书研究什么对象、场域、案例、理论问题或政策问题。
> - **论证类型**：说明它是经验研究、理论建构、方法论著作、政策分析、历史叙事、教材型专著还是批判性著作。
> - **处理粒度**：`single-argument` 或 `chapter-arguments`。说明章节细节是累积在本页，还是另建章节 Argument。
> - **材料边界**：说明当前整合依据是全书、部分章节、导论/结论，还是已处理章节。

---

## 研究问题与核心主张

> [!question] 全书问题
> 直接陈述全书要回答的核心问题，综合各章提炼；不要只复述书名，也不要以“本书/作者/研究者”作为常规句子主语。

> [!monograph-thesis] 全书核心主张
> - **问题起点**：全书从什么经验、理论、历史、方法或政策困境出发。
> - **核心解释**：作者提出什么主要解释、模型、机制、类型或批判。
> - **最终贡献**：读完全书后，读者对该问题的理解应发生什么改变。

> [!citation-card]- 核心表述
> 中文译文或中文原文。（第X章，p.X）
>
> *Original text or English translation.*

---

## 理论、概念与方法工具

> [!monograph-tools] 理论与概念工具
> - **[[Theory]] / [[Concept]]**：说明该理论或概念如何贯穿全书，是问题框架、解释机制、类型工具还是批判视角。（p.X）
> - **[[Theory]] / [[Concept]]**：说明它与其他理论工具的关系。

> [!monograph-method] 研究方法与材料
> - **研究设计**：说明全书的研究设计、材料类型或论证方式。
> - **资料来源**：访谈、档案、统计数据、案例、文本、图像、政策文件或二手文献。
> - **分析策略**：编码、比较、历史追踪、机制分析、模型建构、理论阐释或批判分析。
> - **方法边界**：说明这些材料和方法不能支持什么推断。

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

> [!argument-steps] 论证步骤
> - **1. 问题起点**：全书从什么经验、理论或政策问题出发。
> - **2. 理论／概念工具**：哪些概念、理论或方法组织全书解释。
> - **3. 关键前提**：作者依赖什么历史、制度、方法或价值判断。
> - **4. 证据支撑**：哪些章节、案例、数据或材料提供主要证据。
> - **5. 中间推论**：从材料到结论之间有哪些推理步骤。
> - **6. 结论**：全书最终改变了什么理解。
> - **7. 谨慎处理处**：只记录原书论证中需要谨慎处理的跳跃、边界或未充分说明处，不补写外部批评。

---

## 章节推进

> [!chapter-arc] 章节推进线
> - **导论 / Ch. 1 — 章节标题**：说明该章在全书论证中的功能，例如提出谜题、建立背景、界定对象或搭建理论。
> - **Ch. <N> — <章节标题>**：说明该章如何推进上一章，提供什么证据、机制、类型或案例。
> - **结论章 — 章节标题**：说明如何收束全书论证、提出边界、政策含义或后续问题。

> [!chapter-index] 章节索引
> - **Ch. X — 章节标题**：[[Argument_BookFolder_ChXX]] — 若采用 chapter-arguments，链接章节 Argument；若采用 single-argument，用一句话说明该章位置。
> - **Ch. Y — 章节标题**：待处理 — 说明候选章节功能和优先级。

%% single-argument 时，可在章节索引后为已处理章节增加简短 `### 第X章` 小节；chapter-arguments 时，不在本页展开完整章节论证链。 %%

---

## 跨章综合

> [!book-synthesis] 跨章综合
> - **主题线索一**：哪些章节共同处理同一概念、机制、案例、类型或争议；综合后形成什么判断。
> - **主题线索二**：哪些章节之间形成递进、对照、修正或反例关系。
> - **方法／材料线索**：不同章节的材料如何互相支撑或限制。

> [!finding-cards] 综合发现
> - **发现一** 综合各章提炼的核心发现，附章节或页码来源。
> - **发现二** 说明该发现来自哪些章节，不机械搬运所有小发现。

> [!stat-cards]- 核心数据
> 有具体数字、样本量、效应量或比例时，单独放在这里。（第X章，p.X）

---

## 关键引用

> [!citation-card]- 关键引用
> 中文译文或中文原文。（第X章，p.X）
>
> *Original text or English translation.*

---

## 自述局限与使用边界

> [!book-limits] 自述局限与使用边界
> - **作者自述局限**：只写书中明确自述的局限、边界条件或未来研究方向。
> - **材料边界**：说明样本、案例、时期、地区、文本或资料来源的边界。
> - **推断边界**：说明哪些结论不能由本书材料直接推出。
> - **引用提醒**：说明引用全书 Argument 还是应回到具体章节、页码或章节 Argument。

---

## 来源

%% 只列整本书 source record wikilink。章节 source 写入对应章节 Argument。 %%

- [[Source_Name]]
