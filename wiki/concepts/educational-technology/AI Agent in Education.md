---
title: AI Agent in Education
aliases:
  - 教育智能体
  - 人工智能智能体
  - 智能体
  - AI Agents in Education
  - Educational AI Agent
  - AI Agent
summary: "在教育环境中具备自主交互、自适应支架与即时反馈特征的智能计算系统，涵盖智能导师系统、教育机器人、生成式智能体与对话式智能体四种核心形态并对K-12认知技能与知识建构产生中等促进效应"
type: concept
domain: "educational-technology"
related_count: 0
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
related_concepts:
  - "[[Dialogue in Education]]"
  - "[[Externalization]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Feedback]]"
  - "[[Variable]]"
  - "[[Interaction Effect]]"
  - "[[Critical Thinking]]"
  - "[[Creativity]]"
  - "[[Heterogeneity]]"
  - "[[Statistical Significance]]"
  - "[[Reflexivity]]"
  - "[[Working Memory]]"
  - "[[Document]]"
  - "[[Informationalization]]"
  - "[[Emergence]]"
  - "[[Study Population and Sample]]"
  - "[[Fade-out Effect]]"
  - "[[Prediction Interval]]"
  - "[[Effect Size]]"
related_methods:
  - "[[Meta-analysis]]"
  - "[[Experimental Research]]"
related_arguments:
  - "[[Argument_Liu_2026_CHBR]]"
confidence: high
status: draft
tags:
  - theme/educational-technology
  - theme/ai-in-education
  - cognition/learning-science
  - level/k-12
created: 2026-08-25
updated: 2026-08-25
---

# AI Agent in Education

---

## 定义

> [!def] 核心定义
> 教育智能体（AI Agent in Education）是指在教学与学习环境中，能够感知学习者输入与状态、自主执行决策并提供自适应脚手架与即时反馈的智能计算系统。与静态教育数字资源不同，教育智能体能够根据学习者的认知水平、答题表现与交互轨迹动态调整教学步调与支架强度，在基础教育中主要体现为智能导师系统（Intelligent Tutoring Systems, ITS）、人工智能教育机器人（AI Educational Robotics）、生成式智能体（Generative AI Agents）以及[[Dialogue in Education|对话]]式智能体（Conversational AI Agents）四种技术形态。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 1–3, 5)]]

> [!concept-lens] 概念透镜
> - **含义** 在人机互动学习中扮演指导者、辅导者、评估者或反思同伴角色的自适应智能中介系统。
> - **用途** 帮助教学设计者与研究者解析技术中介如何通过即时强化、自适应纠错与认知[[Externalization|外化]]促进学生的知识习得、程序技能与[[Higher-Order Thinking Skills|高阶思维]]。
> - **边界** 教育智能体不等于被动呈现内容的静态多媒体课件，亦不能在缺乏教学法设计的情况下完全替代人类教师的育人与情感支持功能。

> [!citation-card]- 关键界定
> 人工智能智能体在教育中具有辅导、答疑、评估和反馈等显著应用功能，能够通过个性化脚手架、互动学习环境与即时矫正反馈，成为主动的学习中介系统，有效促进学生的知识获取、技能发展与高阶思维潜能。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 1, 9–10)]]
>
> *AI agents have been found to have notable applications, such as coaching, tutoring, assessment, and [[Feedback]], with the potential to improve students' knowledge acquisition, skills development, and higher-order thinking skills... Unlike static digital technology, AI acts to respond to learners' inserted information, allowing for personalized scaffolding, providing interactive learning environments, and offering immediate corrective feedback.*

> [!boundary]- 概念边界
> - **不等于静态数字化学习材料** 录播视频、电子文本或静态测试软件仅单向呈现预设内容，缺乏基于学习者行为数据的动态推断、自适应支架调整与双向多轮对话能力。
> - **不等于通用基础大模型工具** 未经教育情境化微调、缺乏提示词结构化脚手架或教学评价规程的裸大模型并不具备自洽的教学智能体机能，容易引发无约束的认知卸载与信息幻觉。
> - **不等于完全自动化替代教师** 教育智能体主要承担程序性技能训练、自适应练习分流与即时语法/运算纠错，其效能深度依赖人类教师的教学法设计、情境创设与反思引导。

---

## 概念辨析

> [!contrast-table] 教育智能体与传统教育软件及人类教师对比
> | 维度 | 教育智能体（AI Agent） | 传统静态教育软件（Static EdTech） | 人类专业教师（Human Teacher） |
> |---|---|---|---|
> | **交互机制** | 双向动态自适应交互，依学生表现实时响应 | 单向线性播放或预设分支跳转 | 深度双向言语沟通与非言语具身互动 |
> | **支架形态** | 算法驱动的认知与练习即时微支架 | 固化静态提示、参考答案解析 | 宏观教学设计、认知冲突激发与情感支持 |
> | **适用认知领域** | 程序性技能练习、规则化知识巩固与局部探索 | 事实性信息呈现与标准化选择测验 | 价值引导、复杂[[Higher-Order Thinking Skills\|高阶思维]]启发与劣构问题解决 |
> | **个性化颗粒度** | 细粒度题项级反应跟踪与自适应推送 | 班级或大组统一步调 | 受精力与师生比限制，难以实现全天候即时微追踪 |

---

## 核心要素

> [!feature] 四类核心教育智能体技术形态（Istrate, 2025; Liu et al., 2026）
> - **智能导师系统（Intelligent Tutoring Systems, ITS）** 基于领域知识图谱、学生认知模型与教学决策算法，提供结构化分步解题引导与自适应规则提示的专用系统。在数学与理科程序性问题解决中展现出最强干预效能（$g = 0.540$）。
> - **人工智能教育机器人（AI Educational Robotics）** 具备物理具身或拟人化外显形态的智能交互实体，通过多模态交互（语音、手势、动作）提供陪伴式、探究式学习体验（$g = 0.474$），多应用于低幼与小学阶段的语言认读与跨学科活动。
> - **生成式智能体（Generative AI Agents）** 基于大型语言模型（LLM）或多模态生成技术，支持开放式问答、代码辅助调试、写作支架生成与探究任务共创的智能体系统（$g = 0.421$）。
> - **[[Dialogue in Education|对话]]式智能体（Conversational AI Agents）** 依托自然语言处理驱动的聊天机器人或语音助手，支持口语对话练习、词汇问答与交互式反馈（$g = 0.468$），广泛应用于外语与第二语言口语流利度训练。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 5, 11)]]

> [!logic-map]- 教育智能体认知交互与赋能架构
> ```mermaid
> flowchart TD
>   subgraph Input["学习者输入与状态感知"]
>     A1["作答结果与解题步骤"]
>     A2["自然语言对话与提问"]
>     A3["多模态具身行为互动"]
>   end
> 
>   subgraph Engine["教育智能体自适应处理中枢"]
>     B1["认知状态评估与错误诊断"]
>     B2["最近发展区动态匹配 (ZPD)"]
>     B3["支架衰减与递进算法"]
>   end
> 
>   subgraph Output["教学反馈与赋能输出"]
>     C1["即时纠错与程序性提示"]
>     C2["启发式追问与认知反思"]
>     C3["个性化练习与多模态表征"]
>   end
> 
>   subgraph Outcomes["K-12 认知学习产出"]
>     D1["技能类认知结果 (g = 0.391, p < .001)"]
>     D2["知识类认知结果 (g = 0.344, p < .05)"]
>     D3["高阶思维技能 (g = 0.540, p = .066, 依赖支架)"]
>   end
> 
>   Input --> Engine
>   Engine --> Output
>   Output --> Outcomes
> ```

---

## 围绕概念形成的命题

---

### 命题一　教育智能体对基础教育学生认知发展具有显著中等促进效应且程序技能收益高于陈述知识

> [!concept-lens] 认知领域效应分化与技能实践机制
> 考察教育智能体如何通过即时反馈与强化练习对程序性解题技能产生高效促进，以及为什么对单纯陈述性知识的增益相对适度。

> [!claim] [[Argument_Liu_2026_CHBR|Liu et al. (2026)]]
> **程序性技能练习的优先赋能** 随机效应[[Meta-analysis|元分析]]表明，AI 智能体对 K-12 学生的整体认知表现具有统计学显著的中等促进效应（$g = 0.404, 95\%\text{ CI } [0.242, 0.567], p < .001$）。在细分认知维度上，AI 智能体对技能类认知结果（Skills-based Outcomes）表现出稳定显著的促进效应（$g = 0.391, 95\%\text{ CI } [0.197, 0.584], p < .001$），涵盖数学问题解决、口语流利度与计算思维等操作性任务；而对知识类认知结果（Knowledge-based Outcomes）的促进效应相对适度（$g = 0.344, 95\%\text{ CI } [0.040, 0.649], p = .026$）。这是因为 K-12 阶段学生认知尚在发展中，AI 智能体通过适应性重述、即时纠正反馈与分步任务引导，能极好地支持程序性策略练习与自动化技能内化；而在纯事实记忆和概念陈述层面，教科书与教师讲授依然是主导来源，技术干预的超额增益较为温和。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 6–7, 10)]]

---

### 命题二　教育智能体的干预成效受学段认知成熟度与学科知识结构显著调节且高小学段与语言艺术学科获益最强

> [!concept-lens] 学段认知转型与学科情境适配机制
> 探讨学习者认知发展阶段与学科教学内容特性如何共同决定人机自适应交互的促学效能。

> [!claim] [[Argument_Liu_2026_CHBR|Liu et al. (2026)]]
> **高小学段抽象思维转型的干预敏感窗口** 亚组调节分析证实学段[[Variable|变量]]具有高度显著的[[Interaction Effect|调节效应]]（$Q_B = 12.97, p = .005$）。高小学段（4–6 年级）获得的促进效应最为强劲（$g = 0.877, 95\%\text{ CI } [0.502, 1.253], p < .001$），显著高于初中阶段（$g = 0.195, p < .05$）与低小学段（$g = 0.237, p < .05$），而高中阶段则未达显著水平（$g = 0.037, p > .05$）。这一分化表明，高小学段学生正处于从具体运算向形式运算与抽象逻辑推理过渡的关键窗口期，既具备了独立操作技术界面的数字素养，又高度渴望个性化认知支架；相比之下，低小儿童自我调节不足，高中生学习内容抽象度极高且应试结构固化，单纯技术接入收益减弱。
>
> **语言与艺术学科交互契合度** 学科领域同样显著调节干预效应（$Q_B = 7.61, p = .006$）。语言与读写能力（$g = 0.830, 95\%\text{ CI } [0.384, 1.127], p < .001$）以及艺术与创造力（$g = 0.755, 95\%\text{ CI } [0.112, 1.548], p < .05$）成效最为突出，数学与技术领域次之（$g = 0.230, p < .01$），而自然科学领域未显现统计显著效应（$g = -0.065, p > .05$）。这表明基于[[Dialogue in Education|对话]]、多轮表达与发散生成的文科和艺术任务与教育智能体的交互特性天然契合。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 7, 12)]]

---

### 命题三　生成式与对话式智能体对高阶思维的促进具有高度变异性并取决于显性教学脚手架与反思设计

> [!concept-lens] 技术[[Externalization|外化]]与[[Higher-Order Thinking Skills|高阶思维]]引导的结构依赖性
> 阐明 AI 智能体促进[[Critical Thinking|批判性思维]]、探究推理与[[Creativity|创造力]]等高阶认知表现时面临的高[[Heterogeneity|异质性]]与教学法条件。

> [!claim] [[Argument_Liu_2026_CHBR|Liu et al. (2026)]]
> **高阶思维赋能的不确定性与支架依赖** 元分析数据显示，AI 智能体对高阶思维技能（Higher-Order Thinking Skills）的汇总效应点估计值虽大（$g = 0.540$），但未达到[[Statistical Significance|统计显著性]]门槛（$95\%\text{ CI } [-0.036, 1.117], p = .066$），且存在极高的跨研究异质性（$Q = 259.62, I^2 = 95.4\%$）。这一结果揭示出 AI 赋能高阶认知的双重属性：当生成式智能体与探究式学习、项目驱动或[[Reflexivity|反思性]]调试策略（如教师指导脚手架与结构化反思量规）紧密结合时，能够有效释放[[Working Memory|工作记忆]]、激活深层推理；但若缺乏教学法约束与思维导引，学生容易陷入低水平机械互动或认知卸载，难以自发实现高阶认知进阶。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 7, 10–11)]]

---

### 命题总览

> [!contrast-table] 教育智能体核心命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表[[Document\|文献]] |
> |---|---|---|---|
> | **程序技能优先** | 即时自适应反馈与分步演练对程序性解题与技能熟练度产生中等显著赋能（$g = 0.391$），优于陈述性事实记忆（$g = 0.344$）。 | K-12 阶段数学解题、外语听说训练与计算思维基础教学 | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]]; Holmes et al. (2019) |
> | **学段学科适配** | 高小学段（$g = 0.877$）与语言读写（$g = 0.830$）、艺术创造（$g = 0.755$）是教育智能体介入的最优效能区。 | 基础教育[[Informationalization\|信息化]]课程设计、智慧课堂部署与学段资源配置 | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]]; Wang et al. (2024) |
> | **高阶思维支架依赖** | 高阶思维点估计较高（$g = 0.540$）但异质性极大（$I^2 = 95.4\%$），必须依赖探究教学与反思脚手架。 | 复杂科学问题解决、开放式写作与高阶计算思维培养 | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]]; Du et al. (2025); Fang et al. (2025) |

---

## 概念演变

> [!dev-timeline] 教育智能体的发展演变脉络
> - **1970s–1980s 规则型计算机辅助教学与早期 ITS 萌芽** 基于行为主义与早期认知心理学，开发出 SCHOLAR、GUIDON 等基于产生式规则与专家系统的早期智能导师系统，实现单向规则分流。
> - **1990s–2000s 认知模型成熟与贝叶斯知识追踪** Anderson 等人开发认知导师（Cognitive Tutor），结合贝叶斯知识追踪（BKT）与产生式规则，实现精细化的学生技能掌握度建模与步调自适应。
> - **2010s 具身教育机器人与[[Dialogue in Education|对话]]智能体普及** 随着自然语言处理与传感器硬件发展，NAO 等实体教育机器人和基于检索/规则的教学聊天机器人进入中小学课堂，探索情感陪伴与外语会话互动。
> - **2020s 生成式智能体与大模型驱动的自适应生态** 基于大语言模型与多模态架构的生成式智能体（如 ChatGPT、个性化 Agent 助手）广泛[[Emergence|涌现]]，具备开放式上下文理解、代码实时调试与自适应支架生成能力，并在全球基础教育中开展大规模准实验干预评估。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 1–3)]]

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 技术工具形态分化与促学效能争议
> > 学界对哪类智能体在 K-12 课堂中最具成效存在不同观察。
> >
> > - **结构化优先立场** 强调智能导师系统（ITS）与教育机器人因具备严密的领域知识结构和拟人化支架，在基础教育中效能最为稳健可靠（$g = 0.540$ 与 $g = 0.474$）。
> > - **开放生成优先立场** 认为生成式智能体能够激发自主探究与多元表征，但在缺乏教师引导时可能因自主调节负担过重而削弱低幼学生的专注度。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, p. 11)]]

> [!warning] 适用局限与警示
> - **区域代表性局限** 现有[[Meta-analysis|元分析]]证据中有超过 67% 的初级研究来自亚洲教育情境（中国大陆、中国台湾、韩国等），其高结构化的课堂文化可能放大了技术干预的受控效应，向欧美或其他教育体制外推时需保持审慎。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, p. 13)]]
> - **长期干预的可持续性挑战** 干预周期超过 3 个月的[[Study Population and Sample|研究样本]]量较少且效应不稳定（$g = 0.650, p > .05$），长期使用中可能面临技术新奇[[Fade-out Effect|效应消退]]、软硬件维护成本及学生持续投入度衰减等现实挑战。[[Argument_Liu_2026_CHBR|(Liu et al., 2026, pp. 7, 13)]]

---

## 实证数据

> [!ma-table]- 一阶[[Meta-analysis|元分析]]总体结果
> <span class="concept-meta-analysis-table-marker" aria-hidden="true"></span>
>
> | 一阶元分析 | 当前概念角色与总体结果 | $k$ / $N$ | 效应指标与模型 | 汇总效应与 95% CI | [[Heterogeneity\|异质性]]与[[Prediction Interval\|预测区间]] | 关键解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素：AI 智能体对 K-12 学生认知学习成果的总体促进效应 | $k = 73$ / $N = 3{,}042$（34 项独立研究） | Hedges' $g$ / 随机效应模型 | $g = 0.404$ $[0.242, 0.567]$ | $Q(72) = 813.56, p < .001, I^2 = 91.2\%, \tau^2 = 0.448$ | 仅纳入 2020–2025 年实验与准实验研究；67.65% 样本来自亚洲，未作个别研究偏倚风险工具质评 |

> [!ma-table]- 一阶元分析互补维度亚组
> <span class="concept-meta-moderator-table-marker" aria-hidden="true"></span>
>
> | 一阶元分析 | 当前概念角色 | 对应亚组 | 证据规模 $k$ / $N$ | 亚组汇总效应与 95% CI | 正式组间检验 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（认知结果分类） | 技能类认知结果（Skill-Based Outcomes） | $k = 42$ / — | $g = 0.391$ $[0.197, 0.584]$ | $Q = 409.56, I^2 = 90.0\%, p < .001$ | 涵盖数学解题、编程、读写技能，效应高度稳定显著 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（认知结果分类） | 知识类认知结果（Knowledge-Based Outcomes） | $k = 18$ / — | $g = 0.344$ $[0.040, 0.649]$ | $Q = 143.82, I^2 = 88.2\%, p = .026$ | 概念与事实记忆，效应相对适度 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（认知结果分类） | [[Higher-Order Thinking Skills\|高阶思维技能]]（Higher-Order Thinking） | $k = 13$ / — | $g = 0.540$ $[-0.036, 1.117]$ | $Q = 259.62, I^2 = 95.4\%, p = .066$ | 点估计大但未达统计显著，异质性极高 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（智能体技术类型） | 智能导师系统（ITS） | $k = 10$ / — | $g = 0.540$ $[0.241, 0.839]$ | 智能体类型间检验 $Q_B = 0.069, p = .793$ | 点估计最高，分步规则引导能力强 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（智能体技术类型） | 人工智能教育机器人（Robotics） | $k = 16$ / — | $g = 0.474$ $[0.150, 0.799]$ | $p < .001$ | 具身多模态互动，适合低龄与语言学习 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（智能体技术类型） | [[Dialogue in Education\|对话]]式智能体（Conversational AI） | $k = 30$ / — | $g = 0.468$ $[0.008, 0.645]$ | $p < .05$ | 语言问答与即时互动 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（智能体技术类型） | 生成式智能体（GenAI Agent） | $k = 17$ / — | $g = 0.421$ $[0.198, 0.645]$ | $p < .001$ | 依赖支架引导与任务约束 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（学段分类） | 高小学段（Upper-primary, 4–6年级） | $k = 28$ / — | $g = 0.877$ $[0.502, 1.253]$ | 学段间检验 $Q_B = 12.97, p = .005$ | 处于抽象推理过渡期，获益极显著且最为突出 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（学段分类） | 低小学段（Lower-primary, 1–3年级） | $k = 8$ / — | $g = 0.237$ $[0.044, 0.431]$ | $p < .05$ | 基础概念习得 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（学段分类） | 初中阶段（Lower-secondary, 7–9年级） | $k = 17$ / — | $g = 0.195$ $[0.012, 0.402]$ | $p < .05$ | 学科进阶技能练习 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（学段分类） | 高中阶段（Upper-secondary, 10–12年级） | $k = 19$ / — | $g = 0.037$ $[-0.217, 0.290]$ | $p > .05$ | 未达统计显著 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（学科分类） | 语言与读写（Language and Literacy） | $k = 28$ / — | $g = 0.830$ $[0.384, 1.127]$ | 学科间检验 $Q_B = 7.61, p = .006$ | 对话与生成特性高度匹配语言学习 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（学科分类） | 艺术与[[Creativity\|创造力]]（Arts and Creativity） | $k = 4$ / — | $g = 0.755$ $[0.112, 1.548]$ | $p < .05$ | 激发发散思维与创新设计 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（学科分类） | 数学与技术（Mathematics and Technology） | $k = 28$ / — | $g = 0.230$ $[0.067, 0.393]$ | $p < .01$ | 程序性运算与代码调试 |
> | [[Argument_Liu_2026_CHBR\|Liu et al. (2026)]] | 干预因素（学科分类） | 自然科学（Natural Science） | $k = 11$ / — | $g = -0.065$ $[-0.454, 0.324]$ | $p > .05$ | 未显现显著促学效果 |

---

## 应用案例

> [!evidence-grid-a] 应用案例索引
> - [[Argument_Liu_2026_CHBR|Liu et al. (2026)]] — 运用随机效应[[Meta-analysis|元分析]]综合 34 项实验与准[[Experimental Research|实验研究]]（73 个[[Effect Size|效应量]]，$N = 3{,}042$），系统确立了 AI 智能体在 K-12 阶段对技能类认知结果（$g = 0.391$）与知识类认知结果（$g = 0.344$）的显著促进效应，并揭示出高小学段（$g = 0.877$）与语言读写学科（$g = 0.830$）的突出干预敏感性。
