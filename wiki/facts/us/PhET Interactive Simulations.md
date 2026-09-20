---
title: PhET Interactive Simulations
aliases:
  - PhET
  - PhET Simulations
  - 交互式科学仿真
  - 物理教育技术项目
summary: "诺贝尔物理学奖得主 Carl Wieman 发起、科罗拉多大学研发的开源交互式科学仿真平台，提供数百个直观可视化微观因果机制与参数操纵的虚拟微世界，全球年使用量逾亿次，权威元分析确证其显著提升科学概念理解与态度"
type: fact
subtype: program
region: us
fact_region: "us"
fact_kind: "program"
fact_related_count: 20
fact_related_level: 2
fact_related_stars: "⭐⭐"
fact_related_color: "#ede9fe"
period: "2002–至今"
initiator_organization: "科罗拉多大学博尔德分校（University of Colorado Boulder）与卡尔·威曼（Carl E. Wieman，获 NSF 等资助）"
tags:
  - region/us
  - level/k12
  - level/higher-education
  - educational-technology
  - theme/stem-education
  - computer-simulation
  - inquiry-based-learning
related_concepts:
  - "[[Corporate University]]"
  - "[[Independent Variable]]"
  - "[[Counterfactual]]"
  - "[[Hypothesis]]"
  - "[[Rote Learning]]"
  - "[[Computer Simulation]]"
  - "[[Academic Achievement]]"
  - "[[Self-Efficacy]]"
  - "[[Dependent Variable]]"
  - "[[Causality]]"
  - "[[Problem Solving]]"
  - "[[Inquiry-Based Learning]]"
  - "[[Direct Instruction]]"
  - "[[Control of Variables Strategy]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Effect Size]]"
related_instruments: []
related_persons: []
related_facts:
  - "[[National Science Foundation]]"
  - "[[Web-based Inquiry Science Environment]]"
related_arguments:
  - "[[Argument_DeJong_2023_ERR]]"
confidence: high
status: active
created: 2026-09-21
updated: 2026-09-21
---

# PhET Interactive Simulations

---

## 项目背景与立项契机

> [!claim] 项目定位
> PhET 交互式仿真平台（PhET Interactive Simulations，原名 Physics Education Technology）是由 2001 年诺贝尔物理学奖得主卡尔·威曼（Carl E. Wieman）教授于 2002 年在科罗拉多大学博尔德分校（[[Corporate University|CU]] Boulder）发起创立的开源科学与数学教育研发项目。平台提供基于网页的交互式动画微世界，被公认为全球覆盖面最广、影响力最大、实证研究最为密集的数字化科学探究工具库。（Wieman et al., 2008；Moore & Perkins, 2018；[[Argument_DeJong_2023_ERR|De Jong et al., 2023, p. 9]]）

> [!program-context] 项目背景
> - **立项时间与资助** 2002 年启动，最初由卡尔·威曼捐赠其诺贝尔奖奖金设立种子基金，随后获得[[National Science Foundation|美国国家科学基金会]]（NSF）、休利特基金会（William and Flora Hewlett Foundation）与谷歌等多方数千万美元专项资助。
> - **覆盖规模** 研发逾 160 个高保真仿真模拟单元，支持超过 115 种语言翻译，全球年运行量突破 2.5 亿次，广泛应用于从小学科学到大学进阶物理、化学、生物及数学教学。
> - **核心痛点导向** 破解传统理科教学中微观机制不可见（如电子流动、分子碰撞、光子辐射）、实体实验器材昂贵且维护困难、实验噪音遮蔽本质因果规律等顽疾，通过高交互性视觉隐喻帮助学生构建直观的心理模型。（Wieman et al., 2008）

---

## 方案设计与运行机制

> [!claim] 核心干预／机制假说
> 科学概念的本质掌握依赖于直观的因果操作与动态视觉表征。通过提供允许学生实时拖动参数滑块、即时观测动态响应、且剥离现实摩擦力干扰的虚拟微世界，能够显著降低外在认知负荷，激发探究能动性，促进概念转变与规律内化。（Moore & Perkins, 2018；[[Argument_DeJong_2023_ERR|De Jong et al., 2023, p. 5]]）

> [!policy-design]- 方案设计
> - **教学界面设计准则**
>   1. **隐性机制显性化（Making the Invisible Visible）** 直观渲染不可见的物理量（如电场线、磁力线、微观粒子碰撞速度矢量与能量条形图）；
>   2. **直观交互与低操作门槛** 摈弃复杂的菜单栏与繁琐配置，直接采用直观滑块、抓手与测量表，让学生在 10 秒内即可自主上手操纵[[Independent Variable|自变量]]；
>   3. **支持[[Counterfactual|反事实]]（What-if）与极端条件探究** 允许学生随意设定极端参数（如将重力加速度设为木星或零重力、将摩擦系数设为零），在实体实验室无法复现的情境中检验理论[[Hypothesis|假设]]；
>   4. **与显性教学时序无缝嵌合** 提倡“最小指导探索 ➔ 认知冲突暴露 ➔ 教师显性精讲 ➔ 模拟进阶验证”的混合流程。

> [!citation-card] 威曼等论 PhET 模拟对科学心理表征的重构功能
> PhET 模拟旨在促进概念理解而非[[Rote Learning|死记硬背]]。模拟使看不见的科学实体可视化，为学生操纵物理世界提供了高度动态的互动隐喻。学生不再是被动的听众，而是通过操纵滑块、观察反馈自主建构起物理学家的思维模型。（Wieman, Adams, & Perkins, 2008）
>
> *PhET simulations are designed to animate invisible physical phenomena, providing students with interactive visual mental models that support deep conceptual understanding and inquiry.*

---

## 推进历程与阶段演进

> [!dev-timeline] 项目推进历程
> - **2002–2007 — 物理模拟雏形与设计原则确立** 创立初期基于 Java 与 Flash 研发首批核心物理力学与光学仿真，在《Science》发表里程碑论文确立基于学习科学的设计原则（Wieman et al., 2008）。
> - **2008–2014 — 跨学科横向扩张与全球普及** 拓展至化学、生物、地球科学与纯数学，成为全美乃至全球理科教师教学大纲的标准配置；大规模[[Meta-analysis|元分析]]证实其在概念理解上的普遍优势（d'Angelo et al., 2014）。
> - **2015–至今 — 全面迁移至 HTML5 与全平台无障碍可访问性** 彻底摆脱插件限制，实现手机、平板跨平台免安装运行；研发支持视障儿童的动态声音反馈与触觉辅助技术，推进全球教育公平（Moore & Perkins, 2018；[[Argument_DeJong_2023_ERR|De Jong et al., 2023, p. 9]]）。

---

## 成效评估与实证发现

> [!finding-cards] 核心实证结论
> - **跨学科概念理解与科学推理的全面领先** 权威[[Meta-analysis|元分析]]与系列对照实验（d'Angelo et al., 2014；Wieman et al., 2008）表明，在相同教学时长下，使用 PhET 开展探究的学生在定性概念测试与因果推理能力上显著超越仅听讲传统课件或观看教师板书的学生（$p < .05$）。
> - **实体实验与[[Computer Simulation|虚拟仿真]]的协同增效** 对比研究发现，纯实体实验因器材接触不良或读数误差常导致学生忽视核心规律；而“先用 PhET 探索纯净因果规律、再开展实体实验连接现实噪音”的组合，取得了最高的[[Academic Achievement|学业成就]]与动手技能。（Moore & Perkins, 2018）
> - **显著提升情意态度与科学兴趣** 视觉化与高交互性显著改善了学生对物理化学的恐惧心理，提升了学习[[Self-Efficacy|自我效能感]]。

---

## 实证数据

> [!effect-table]- 原始研究实证数据
> <span class="concept-effect-table-marker" aria-hidden="true"></span>
>
> | 研究 | 比较或干预 | [[Dependent Variable\|结果变量]] | 分析样本 | 组别统计 | [[Effect Size\|效应量]] | 显著性或不确定性 | 设计与解释边界 |
> |---|---|---|---|---|---|---|---|
> | Wieman, Adams, & Perkins (2008)（引自 [[Argument_DeJong_2023_ERR\|De Jong et al., 2023, p. 9]]） | PhET 模拟探究教学 vs 传统名师课堂演示与讲授 | 大学物理电路与电磁学概念掌握 | 大学普通物理学本科生对照实验 | PhET 探究组在定性概念理解与非计算[[Causality\|因果推断]]题上显著优于名师讲授组 | — | 概念测验显著（$p < .05$） | 标杆实验；证实高交互性可视化微世界在打破前概念迷思上显著优于单纯视听讲解 |
> | Moore & Perkins (2018)（同上引文） | HTML5 跨平台 PhET 模拟嵌入自适应探究工作单 vs 纯文本学习 | K-12 与大学 STEM 概念掌握与态度 | 大规模跨校多学期实证追踪 | 嵌入仿真组在各年级概念保持与[[Problem Solving\|问题解决]]技能上保持系统性优势 | — | $p < .01$ | 规模化课程实践分析；确立交互微世界作为现代[[Inquiry-Based Learning\|指导式探究]]标配基础设施的实效 |

---

## 争议、局限与经验教训

> [!debates] 核心争议
>
> > [!axis] 完美仿真 vs 真实实验误差感知
> > 争论焦点在于纯虚拟模拟是否会导致学生丧失对真实科学误差的敬畏。
> >
> > - **误差缺失论** 批评者担忧学生习惯了理想无摩擦的物理世界，在面对真实仪器的接触电阻或测量浮动时无所适从。
> > - **分工协同论** PhET 团队指出，模拟定位并非彻底消灭实体实验，而是在概念初建期剥离无关噪音，使学生先建立牢固的认知因果锚点，再进入实体实验学习误差处理（Wieman et al., 2008）。

---

## 相关条目网络

> [!entry-map]
> 
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Computer Simulation]] | 概念 | PhET 是全球教育领域最具代表性、应用最广的计算机模拟微世界库。 |
> | [[Inquiry-Based Learning]] | 概念 | PhET 构成了现代 STEM 开展技术增强指导式探究学习的核心基础设施。 |
> | [[Direct Instruction]] | 概念 | 课堂实践广泛将 PhET 模拟探索与后续显性直接讲授相结合。 |
> | [[Control of Variables Strategy]] | 概念 | PhET 界面中的多[[Variable\|变量]]独立滑块设计是训练变量控制策略的最优场景。 |
> | [[Web-based Inquiry Science Environment]] | 事实 | 与 WISE 类似，均为经受大规模实证检验的标杆数字化科学教育项目。 |
> | [[Argument_DeJong_2023_ERR\|De Jong et al. (2023)]] | 论证 | 权威综述将 PhET 作为确立数字化仿真探究显著优于传统教学的标杆证据。 |
