---
title: Learning Analytics
aliases:
  - 学习分析
  - 学习分析学
  - LA
  - Educational Data Mining
  - EDM
summary: 通过对学习过程中产生的数字痕迹进行收集、分析与报告以理解和优化学习的技术实践
type: concept
tags:
  - learning-analytics
  - educational-data-mining
  - personalized-learning
  - edtech
  - digitalization
  - data-science
  - region/global
  - level/higher-ed
  - theme/subjectification
related_concepts:
  - "[[Online Self-Assessment]]"
  - "[[Promising Student]]"
  - "[[Educational Technology Industry]]"
  - "[[Knowledge-Based Economy]]"
  - "[[Transhumanism]]"
  - "[[Performativity of Measurement]]"
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Thompson_2022_Promising_Student]]"
  - "[[Argument_Amos_2022_Springer]]"
sources:
  - "[[Ch4_Amos_2022]]"
  - "[[Ch13_Thompson_2022]]"
confidence: medium
status: draft
created: 2026-05-08
updated: 2026-05-19
---

# Learning Analytics

## 定义

> [!info]
> 学习分析（Learning Analytics，简称 LA）是指通过对学习过程中产生的数字痕迹——点击流、提交时间、测验成绩、讨论参与度等——进行收集、测量、分析和报告，以理解和优化学习及其发生环境的技术实践。与之密切相关的还有教育数据挖掘（Educational Data Mining, EDM），后者侧重从教育数据中自动发现模式和构建预测模型（Thompson et al., 2022, p.224）。

从量化社会学的角度看，学习分析的量化过程伴随着"价值化"（valorization）——不仅仅表征世界（如学生的某种能力），还创造了带有等级不平等的新现实（Mau, 2019, pp.40–59; Thompson et al., 2022, p.225）。这与 [[Performativity of Measurement|测量的生产性]] 一脉相承：学习分析的数据不只是"反映"学习，更是重塑学习行为和主体性的生产性力量。

> [!example]
> 传统课堂中，教师通过观察学生的面部表情、提问频率和作业表现来判断谁在挣扎、谁需要额外挑战。学习分析将这些"教师直觉"转化为数据仪表盘——每个学生的参与度被量化为数字、学习进度被可视化为进度条、薄弱知识点被算法自动标记。教师角色从"观察者-判断者"转变为"数据读取者-响应者"（Amos, 2022, p.57）。

## 核心要素

> [!abstract]

### 数据收集与追踪

Behrens 和 DiCerbo（2014, pp.39–40）将教育数据的增长描述为从"数字荒漠"（digital desert）到"数字海洋"（digital ocean）的转变——数字痕迹的丰富性使得对学习过程的全面追踪成为可能。Bächle（2016, p.172）指出，这种数据丰富性同时承诺了"通过数据实现对自我的完全可读性"（Thompson et al., 2022, p.224）。

### 学习者建模与预测

学习分析的核心技术产出是"学习者模型"（learner models）——通过收集和分析学生的兴趣、动机、认知技能和行为数据，识别学业成功的预测因子（Pea, 2014; Thompson et al., 2022, p.224）。Antunes（2010, pp.353–363）提出的"ASAP 分类器"（ASAP classifiers）是一个典型例子：能够自动预测学生成功或失败概率的算法，以便在最早阶段实施对策（Thompson et al., 2022, p.224）。

### 反馈与适应循环

学习分析与个性化学习构成"测量-反馈-适应"循环：学习分析负责数据的收集和建模，个性化推荐引擎根据分析结果推送学习内容（Amos, 2022, pp.56–57）。这个闭环承诺了一种"无摩擦学习"（frictionless learning）——学生在不需要主动求助的情况下，系统自动从表现数据中"读取"需求并响应。

## 主要应用场景

### 个性化学习与自适应系统

> [!abstract]
> Amos（2022, pp.56–57）将学习分析定位为 [[Educational Technology Industry|教育技术产业]]三重驱动力中"教师专业发展"维度的核心技术：

- **宣称的教育价值**：通过精确追踪每个学生的强项和弱项，提供"恰到好处"的学习内容和难度
- **创造的新劳动力市场**：催生了数据科学家、学习设计师、教育技术开发者等新职业类别
- **与利润动机的关联**：学习分析的技术基础设施（数据平台、分析算法、可视化工具）主要由 EdTech 公司提供，使"专业发展"动机与利润动机在实践中难以分离

> [!example]
> 一个学生在 Coursera 上学习机器学习课程。学习分析系统追踪她观看视频的时长、暂停和回放的频率、测验的答题时间和错误模式。个性化推荐引擎根据这些分析结果，在她卡住的概率概念上推送补充材料，在她已掌握的内容上跳过练习。整个过程不需要学生主动"寻求帮助"（Amos, 2022, p.57）。

### 先发制人的学生治理

> [!abstract]
> 在高等教育入学环节，学习分析的技术能力被用于入学前的"先发制人"（preemptive）治理。Thompson 等人（2022, pp.224–226）以 [[Online Self-Assessment]] 为分析对象展示了这一机制。

在 [[Online Self-Assessment|OSA]] 场景中，学习分析将干预窗口从学习过程中提前到了入学之前——通过收集潜在学生的兴趣、期望、动机和认知技能数据，构建数字自我（digital self），并生成数字最优（digital optimum）作为参照标准。数字自我与数字最优之间的差距驱动着算法治理——学生被引导主动管理自己的"学习组合"、弥补不足（Thompson et al., 2022, p.226）。详见 [[Online Self-Assessment#数据化与主体化效应]]。

这一治理模式的运作基础是将学生特征转化为可被归因于该个体的数字指标——即 Bächle（2016, p.194）所说的"统计人造物"（statistical artefact）。被建构的数字自我成为后续治理决策的依据：哪些学生需要额外关注、哪些学生适合特定项目、哪些学生面临着高风险（Thompson et al., 2022, pp.224–225）。

> [!example]
> 亚利桑那大学的 e-advice 系统是学习分析与先发制人治理结合的典型案例：当算法自动追踪记录到一系列"问题学生行为"（如未按时完成课程作业、花在健身房的时间多于图书馆）时，辅导员被自动通知并介入（Amos, 2019, p.238; Thompson et al., 2022, p.225）。学生的日常行为被转化为持续的调制信号，干预从反应性（学生主动求助）转变为预判性（系统在学生意识到问题之前就标记风险）。这表明学习分析不仅是"描述学习"的工具，更是"治理学习"的机制——它与 [[Promising Student|"有前景的学生"]] 的主体建构互为表里。

### 教育劳动市场重塑

> [!success]
> Amos（2022, p.57）指出学习分析对教师角色的根本性重塑：

- **角色转变**：教师从知识传递者和学习设计者，部分转变为算法的执行者和数据的提供者——学习分析系统设计学习路径，教师负责监督和干预
- **劳动市场分层**：学习分析同时创造高端技术岗位（数据科学家）和"执行层"教学岗位（按仪表盘指示行动的教师），可能加剧教育劳动市场的两极分化
- **去专业化风险**：当教学决策越来越多地由算法驱动，"教师的专业判断"空间可能被压缩

## 争议与批评

> [!warning]

- **"改善学习质量"的证据不足**：学习分析的宣称效果——提高学习成绩、降低辍学率——缺乏大规模、独立评估的经验支持（Amos, 2022, p.57）
- **数据化 ≠ 理解学习**：将学习过程简化为可追踪的数字痕迹，可能遗漏学习中最关键的维度——困惑的质量、创造性的酝酿、同伴之间的非正式互动——这些难以量化但对学习至关重要的过程（Thompson et al., 2022, p.227）
- **与超人类主义的亲和性**：学习分析的核心逻辑——通过数据追踪和算法优化来"增强"学习——与 [[Transhumanism]] 的效率最大化逻辑高度兼容（Amos, 2022, pp.58–59）
- **可预测性的幻觉**：学习分析的逻辑预设学生的学业成功可以被入场数据预测，但这排除了教育的根本开放性——[[Bildung]] 指向的是一个超越数据相关性的、开放且不可预测的未来（Thompson et al., 2022, p.227）
- **先发制人治理的伦理风险**：在 OSA 场景中，学习分析在入学前就对"问题学生"进行预判和预管理——这引发了对数据驱动的"预判性身份"（preemptive identity）的伦理担忧：一个人可能在被给予机会证明自己之前，就已经被算法标记为"高风险"（Thompson et al., 2022, pp.224–225）

## 来源

- [[Ch4_Amos_2022]]
- [[Ch13_Thompson_2022]]
