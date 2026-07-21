---
title: Contingency Questions
aliases:
  - 条件题
  - 过滤题
  - 分支题
  - filter question
  - branching question
  - skip logic
  - contingency question
summary: "依赖于前题回答来决定后续题目是否呈现或跳转的题型，前面的问题充当过滤器，后面的问题是条件性的分支，其设计需注意位置效应、夹层效应和视觉显著性"
type: concept
domain: "research-methodology"
related_count: 5
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - method/questionnaire
  - method/survey
  - data-collection
  - source/textbook
related_concepts:
  - "[[Questionnaire]]"
  - "[[Order Effects]]"
  - "[[Variable]]"
  - "[[Content Validity]]"
related_arguments:
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch20]]"
related_methods:
  - "[[Telephone Interview]]"
confidence: medium
status: draft
created: 2026-07-21
updated: 2026-07-21
---
# Contingency Questions

## 定义

> [!def] 条件题
> 条件题（Contingency Questions）依赖于对前面问题的回答来决定后续题目是否呈现或如何跳转。前面的问题充当**过滤器（Filter）**，后面的问题是条件性的，是前面问题的**分支（Branch）**。典型形式如"如果你对第（1）题的回答是'是'，请跳至第（4）题"。一些[[Questionnaire|问卷]]用文字写明跳至的问题号，另一些用箭头指示（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch20|Cohen et al., 2011, Ch20, pp. 151–153]]）。

> [!concept-lens] 概念透镜
> - **含义** 条件题不是一种独立的题型，而是一种**问卷结构机制**——它通过在前题和后题之间建立逻辑依赖关系，使问卷能够根据不同受访者的特征或回答自适应地呈现不同路径。过滤器是入口条件，分支是跳转目标，跳转指令是连接两者的桥梁。
> - **用途** 条件题使问卷能够：(1) 跳过不适用于特定受访者的问题；(2) 根据回答深入追问特定子议题；(3) 避免强迫受访者回答无关问题而产生挫败感。它是问卷"智能化"和个性化的核心机制。
> - **边界** 条件题增加了问卷的认知复杂度和出错风险。受访者倾向于忽略、误读和错误遵循分支指令（Redline et al., 2002）。过度复杂的跳转逻辑可能比没有跳转逻辑带来更多数据质量问题。

> [!citation-card]- 条件题的三要素
> 条件题依赖于对前面问题的回答。前面的问题充当过滤器，后面的问题是条件性的，是前面问题的分支。（pp. 151–153）
>
> *A contingency question is one that depends on the response to an earlier question: the earlier question acts as a filter and the later question is contingent on it, being a branch of the earlier question.*

> [!boundary]- 与相近概念的区分
> - 不等于[[Order Effects|顺序效应]] — 顺序效应关注的是选项/题项呈现顺序对回答的无意偏差影响；条件题是研究者有意设计的逻辑跳转机制。但条件题的**位置效应**和**夹层效应**（Redline et al., 2002）与顺序效应共享"位置影响行为"的底层机制。
> - 不等于[[Questionnaire|问卷]]的题目排序（Question Sequencing） — 题目排序是线性排列原则（从无威胁到敏感）；条件题引入了非线性、有分支的路径结构。

---

## 核心要素

> [!feature] 条件题的三要素结构
> - **过滤器（Filter）** 前置问题，其回答决定后续路径是否触发。例如"你是否参加过在职培训？"——回答"是"则进入追问，回答"否"则跳过。
> - **分支（Branch）** 条件满足后呈现的后续问题。分支问题的内容依赖于过滤器问题的回答逻辑。
> - **跳转指令（Skip Instruction）** 连接过滤器与分支的导航指示，如"请跳至第 15 题"或箭头图示。指令的视觉设计和位置直接影响正确遵循率（pp. 151–153）。

> [!warning] Redline et al.（2002）的五项关键发现
> 受访者倾向于忽略、误读和错误遵循分支指令，导致不回应和跳答错误。分支指令带来的[[Questionnaire|问卷]]复杂性增加负面影响了正确完成率（pp. 151–153）：
>
> - **字数与短期记忆** 问题中字数越多，受访者忽视分支指令的可能性越大。短期记忆最多保留七项——这对[[Telephone Interview|电话访谈]]有重要含义，因为无法进行视觉回忆或检查。
> - **回答类别数量** 回答类别越多，出错可能性越大。
> - **位置效应** 受访者倾向于看到放在**末尾类别旁边**的分支指令，特别是当他们选择了那个末尾类别时。放在页面底部的问题比页面中上部的问题获得更多不回答，带分支指令的问题不应放在页面底部。
> - **夹层效应** 将分支指令夹在非分支题项之间容易导致遗漏和委托错误（回答错误的问题或遗漏应回答的问题）。
> - **视觉显著性** "改变分支指令的视觉和语言设计对受访者如何阅读、理解和执行分支指令有实质性影响"。指令应放在它们将被使用的地方和能够被看到的地方。加粗和大写可增加被关注到的机会。

> [!tip] 操作建议
> - 审慎且有限地使用过滤和分支机制。避免让参与者必须前后翻页。
> - **分区化**问卷——将概念上相近的题项保持在一起，将分支保持在同一个分区内（p. 153）。
> - 回答类别放在文本右侧可增加被回答的概率（Redline et al., 2002）。

---

## 围绕概念形成的命题

### 命题一　分支指令的视觉和位置设计本身就是影响数据质量的变量

> [!concept-lens] [[Questionnaire|问卷]]布局作为方法论[[Variable|变量]]
> 传统上问卷设计关注题项措辞和[[Content Validity|内容效度]]，但 Redline et al.（2002）的研究表明，分支指令的视觉设计和放置位置本身就是影响回答质量的独立变量——不是指令内容说了什么，而是指令放在哪里、看起来如何，决定了受访者是否遵循。

> [!claim] Redline et al.（2002）
> **视觉设计的方法论意义** 改变分支指令的视觉和语言设计对受访者如何阅读、理解和执行分支指令有实质性影响。位置效应（底部被忽略）、夹层效应（夹在非分支题之间被遗漏）和视觉显著性（加粗大写增加关注）共同表明：问卷的设计布局不是一个中性的内容容器，而是塑造数据质量的积极力量。（Redline et al., 2002; Ch20, pp. 151–153）

---

### 命题总览

> [!contrast-table] 条件题的核心命题
> | 命题类型 | 核心指向 | 方法论含义 | 代表学者 |
> |---|---|---|---|
> | **视觉设计是方法变量** | 分支指令的位置和样式决定遵循率，不只是内容问题 | 布局设计应从方法论角度审视，不能只关注措辞 | Redline et al.（2002） |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch20|Cohen et al. (2011, Ch20)]] — 在题型体系一节中定义了条件题的三要素结构（过滤器、分支、跳转指令），详细引述了 Redline et al.（2002）关于分支指令位置效应、夹层效应和视觉显著性的五项关键发现。
