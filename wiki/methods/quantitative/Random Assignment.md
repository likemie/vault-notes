---
title: Random Assignment
aliases:
  - 随机分配
  - 随机分组
  - randomisation
  - randomized assignment
  - 随机化
  - randomization
summary: 将受试者按概率均等原则分配到实验处理条件中，以消除系统性偏差并支持因果推断的实验技术，在教育研究中受到开放系统和能动性视角的哲学反思
type: method
method_type: quantitative
tags:
  - method/experimental
  - quantitative-research
  - causal-inference
related_concepts:
  - "[[Causality]]"
  - "[[Effect Size]]"
  - "[[Epistemology]]"
  - "[[Positivism]]"
  - "[[Variable]]"
  - "[[Internal Validity]]"
  - "[[External Validity]]"
  - "[[Purpose Statement]]"
  - "[[School Leadership]]"
  - "[[Student-Teacher Relationship]]"
  - "[[Emergence]]"
  - "[[Paradigm]]"
related_theories:
  - "[[Critical Realism]]"
  - "[[Realist Evaluation]]"
related_methods:
  - "[[Experimental Research]]"
  - "[[Random Sampling]]"
  - "[[Quasi-Experimental Designs]]"
  - "[[Case Study]]"
  - "[[Randomised Controlled Trials]]"
related_persons: []
related_facts:
  - "[[Education Endowment Foundation]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Wrigley_2018_BERJ]]"
confidence: medium
status: draft
created: 2026-05-31
updated: 2026-06-19
---

# Random Assignment

---

## 定义

> [!def] 方法定义
> 随机分配（Random Assignment）是[[Experimental Research|实验研究]]中将受试者按概率均等原则分配到不同实验处理条件中的技术，是区分真实验与准实验的核心特征。当每个受试者被随机分配到某一处理条件——例如受试者 1 进入治疗组，受试者 2 进入控制组——意味着各组的受试者特征在概率上不存在系统性偏差，从而消除了受试者基线特征差异对结果的潜在影响。([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8; Keppel & Wickens, 2003]])

> [!method-scope] 方法范围
> - **研究对象**：被随机分派到不同实验处理条件（干预组与对照组）的受试者个体或单位。
> - **问题类型**：[[Causality|因果推断]]（Causal Inference）与干预净效应估计问题。
> - **分析单位**：个体（如学生）、群体（如班级、学校）。
> - **输出形式**：组间基线平衡检验、干预后[[Effect Size|效应量]]（Effect Size）的无偏估计。

> [!citation-card] 关键定义
> 当个体被随机分配到组别中时，该程序被称为真实验。([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]])
>
> When individuals are randomly assigned to groups, the procedure is called a true experiment.

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观**：基于[[Positivism|实证主义]]与经验主义因果观。假定通过控制和消除混杂[[Variable|变量]]，可以直接从因果事件的恒常规则性（X 导致 Y）推导出[[Causality|因果关系]]。
> - **研究者角色**：作为客观的操控者和观察者，设计随机程序以隔离混杂变量，排除主观判断干扰。
> - **有效性标准**：主要服务于[[Internal Validity|内部效度]]（Internal Validity）。高信度的随机分配能最大限度排除选择偏误（Selection Bias）。
> - **不声称回答的问题**：不能回答干预“为什么”起作用的深层因果机制，也不能回答干预在未经随机化控制的现实“开放社会系统”中如何运作。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 6, 8]])

> [!method-stack] 方法层级
> - **研究设计**：真实验设计（True Experimental Designs，如前测-后测控制组设计、仅后测控制组设计）。
> - **辅助技术**：随机数生成器、分层随机化（Stratified Randomisation）、匹配随机化（Matched Randomisation）。

---

## 研究程序

> [!proc] 随机分配实施步骤
> 1. **确定实验处理条件**：界定独立[[Variable|变量]]的各个水平（如：使用新软件的干预组 vs. 一切照旧的控制组）。
> 2. **生成随机分配序列**：使用随机数生成器、计算机算法或随机数表，为每个进入实验的受试者（或学校）生成概率均等的分配指令。
> 3. **隐蔽分配与实施**：确保分配序列对受试者和一线执行人员隐蔽（如可能，实施单盲或双盲），将受试者依次分派入组。
> 4. **基线平衡检验 (Baseline Balance Test)**：在实验开始前测量并比对干预组与控制组的前测成绩（Pre-test）及关键特征，检验随机化是否成功消除组间系统性差异。
> 5. **净效应估计**：在干预结束后测量后测成绩（Post-test），计算[[Effect Size|效应量]]。
>
> > [!tip] 随机分配 vs. [[Random Sampling|随机抽样]]
> > 随机分配（Random Assignment）和[[Random Sampling|随机抽样]]（Random Sampling）是两个不同的概念。随机抽样涉及如何从总体中抽取样本，目的是提升样本对总体的代表性（保障[[External Validity|外部效度]]）。随机分配涉及如何将已选取的样本分派到实验条件中，目的是消除组间系统性偏差以确立[[Causality|因果关系]]（保障[[Internal Validity|内部效度]]）。([[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]])

---

## 适用场景

> [!method-fit] 适用判断
> - **适合使用**：当[[Purpose Statement|研究目的]]在于评估某项标准化干预（如某种教学软件、标准化测试）对学业成绩的纯粹因果净效应，且样本量足够大、环境相对封闭时。
> - **谨慎使用**：在复杂的教育生态中，受试者（如[[School Leadership|学校领导]]、教师）的态度和信念在随机分配前已高度分化。由于无法实施双盲，教师的热情与主动施为（Agency）会污染实验过程，导致[[Effect Size|效应量]]难以归因。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 6]])
> - **不适合使用**：许多教育研究情境中，由于行政限制、伦理冲突（如不能随机剥夺一部分学生接受优质教学的机会），随机分配在实践上不可行，此时应使用[[Quasi-Experimental Designs|准实验设计]]或质性[[Case Study|个案研究]]。

---

## 局限性与学术批评

> [!method-limits] 方法局限与批判
> - **“糟糕随机化”导致的统计偏误风险**：当实验样本量较小或学校自主选择性退出时，随机分配极易失衡，造成“糟糕的随机化”（Bad Randomisation）。此时干预组和控制组在前测阶段就存在显著的基线差异。如果简单采用平均后测得分差计算[[Effect Size|效应量]]，会产生严重的“数据包装”偏误。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 5]])
> - **因果归因的“黑箱化”**：随机分配将复杂的教学过程简化为输入（干预项目）和输出（效应量）的对比，却无法诊断“为什么”学生会产生困难，也过滤掉了教师的推理和情境脉络，将因果机制置于统计黑箱之中。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 6]])
> - **实验室“封闭系统”假设与教育“开放系统”现实的冲突**：随机分配的哲学前提是能像物理实验室那样隔离外界干扰（封闭系统）。但在现实教育系统（开放系统）中，外部政策、学校文化、[[Student-Teacher Relationship|师生关系]]的[[Emergence|涌现]]性因果力量无处不在。完美的随机分配只是一个无法在现实中完整复制的“休谟式规则性”幻象。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 8]])

> [!critique-method] Fresh Start 案例解构：随机化失败的实证证据
> 英国教育 Endowment Foundation ([[Education Endowment Foundation|EEF]]) 曾对一项针对中一阅读困难学生的拼读干预项目（Fresh Start）进行 [[Randomised Controlled Trials|RCT]] 评估，其行政摘要宣称项目带来了 $+0.24SD$ 的效应量（相当于 3 个月额外进步），并将该项目奉为循证黄金标准。
> 
> 然而，通过对技术报告的解构发现：
> 1. **前测失衡**：由于分配失控，干预组的前测均值远低于控制组的前测均值。干预组的后测均值甚至仅略高于控制组的前测均值。
> 2. **匹配子集拆解的幻灭**：当研究者从中筛选出前测成绩完全相同的低分学生子集进行重新分析时，干预组和控制组的平均进步幅度和后测成绩**几乎完全相同**（净效应量变为 $+0.00SD$）。
> 所谓的 $+0.24SD$ 效应量纯粹是糟糕随机化和前测失衡带来的统计伪像，这一案例生动展示了过度迷信随机分配而不进行基线细分核验的科学风险。([[Argument_Wrigley_2018_BERJ|Wrigley, 2018, p. 5]])

---

## 相关理论与方法

> [!frames-ref] 相关理论
> - [[Critical Realism]] — 批判实在论指出社会系统是分层的、开放的，[[Causality|因果关系]]取决于机制与背景的交互，因而对随机分配所基于的封闭系统恒常规则因果观提出了根本质疑。
> - [[Realist Evaluation]] — 实在论评估主张社会项目是通过激发受试者的推理而起作用，从而打破了随机分配将人的能动性视为污染源的黑箱[[Paradigm|范式]]。

---

## 使用此方法的研究

> [!evidence-grid-a] 实证研究与批判案例索引
> - [[Argument_Creswell_2022_SAGE|Creswell & Creswell (2022)]] — 介绍了在 2 × 4 混合实验设计中使用随机数生成器将受试者随机分配到价值肯定条件或控制条件中的标准流程。（Ch8, Example 8.5）
> - [[Argument_Wrigley_2018_BERJ|Wrigley (2018)]] — 对 [[Education Endowment Foundation|EEF]] Fresh Start 等 [[Randomised Controlled Trials|RCT]] 实验报告进行了高精度的技术解构，作为“随机分配失败与基线失衡导致[[Effect Size|效应量]]伪像”的经典批判案例。
