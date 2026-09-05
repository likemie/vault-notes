---
title: AI Hallucination
aliases:
  - 人工智能幻觉
  - 大模型幻觉
  - Hallucination in AI
  - Machine Hallucination
  - Algorithmic Hallucination
  - LLM Hallucination
  - 幻觉
summary: "人工智能与教育技术学概念，指大语言模型等生成式系统输出看似连贯权威、语法高度流畅但实际上偏离客观事实、缺乏真实依据、虚构引用或逻辑自相矛盾的内容现象。"
type: concept
domain: "educational-technology"
related_count: 27
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - field/educational-technology
  - theme/artificial-intelligence
  - theme/cognitive-science
  - theme/critical-thinking
  - theme/epistemology
related_concepts:
  - "[[Generative Artificial Intelligence]]"
  - "[[Document]]"
  - "[[Epistemological Vigilance]]"
  - "[[Critical Thinking]]"
  - "[[Creativity]]"
  - "[[Brainstorming]]"
  - "[[AI Literacy]]"
  - "[[Epistemology]]"
  - "[[Cognitive Offloading]]"
  - "[[Illusion of Competence]]"
  - "[[Homework]]"
  - "[[Artefact]]"
  - "[[Reliability]]"
  - "[[Paradigm]]"
  - "[[Effect Size]]"
  - "[[Variable]]"
  - "[[Structured Teaching]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Primary and Secondary Documents]]"
related_theories: []
related_methods:
  - "[[Triangulation]]"
  - "[[Systematic Review]]"
  - "[[Pilot Testing]]"
  - "[[PRISMA]]"
  - "[[Meta-analysis]]"
related_arguments:
  - "[[Argument_Li_2026_CEAI]]"
  - "[[Argument_Zhao_2025_JIntell]]"
  - "[[Argument_RoyalSociety_2026_ScienceForSociety_Ch01]]"
confidence: high
status: active
created: 2026-09-02
updated: 2026-09-05
---

# AI Hallucination
（AI 幻觉 / 大模型幻觉）

---

## 定义

> [!def] 核心定义
> AI 幻觉（AI Hallucination / Machine Hallucination）是指大语言模型（LLM）与[[Generative Artificial Intelligence|生成式人工智能]]系统在生成文本、代码或多模态内容时，**输出在语法与语调上极具连贯性、说服力与权威感，但在客观事实上纯属虚构、缺乏真实证据支撑、编造学术[[Document|文献]]或在逻辑上自相矛盾的内容现象**。其根源在于自回归深度神经网络基于统计概率预测下一词（Next-Token Prediction）的生成机制，而非基于对真实物理世界与逻辑真理的符号表征。[[Argument_Li_2026_CEAI|(Ji et al., 2023; Li et al., 2026, pp. 2, 6, 11)]]

> [!concept-lens] 概念透镜
> - **含义** 区别于软件运行时的程序崩溃或逻辑报错，AI 幻觉是一种“静默且自信的错误生成”——系统以完美的自然语言包装虚假命题。
> - **用途** 在教育技术中具有“双刃剑”属性：既是诱发学生误解与学术失范的首要风险源，也是教学设计中通过“红队查错任务”激发[[Epistemological Vigilance|认识论警觉]]与[[Critical Thinking|批判性思维]]的核心认知脚手架。
> - **边界** 不等同于故意欺诈（AI 缺乏欺骗意图），亦不等同于单纯的训练数据偏见（幻觉常在无偏见情境下纯因概率拟合与联想泛化而凭空生成）。

> [!citation-card]- 关键表述：事实核查与去幻觉查错的教学转化（[[Argument_Li_2026_CEAI|Li et al., 2026]]）
> 事实核查与去幻觉检验（Fact-checking & Hallucination Detection）构成了生成式 AI 赋能批判性思维的核心机制之一。在 19 项实证研究中，教师通过引导学生专门针对 AI 生成的文献与数据进行对抗性审验，有效将模型的缺陷转化为培养学生认识论警觉与多源实证核查习惯的教学契机。[[Argument_Li_2026_CEAI|(Li et al., 2026, pp. 6, 11)]]
>
> *Fact-checking and error detection (n = 19) emerged as a major affordance for critical thinking... engaging students in "red-teaming" AI-generated claims turns hallucination into a pedagogical catalyst for epistemic vigilance.*

> [!citation-card]- 关键表述：AI 幻觉对批判性思维的意外倒逼机制（[[Argument_Zhao_2025_JIntell|Zhao et al., 2025]]）
> 生成式人工智能的固有缺陷（例如 AI 幻觉）能够有效催化批判性思维。不准确或误导性信息的生成，迫使学生主动审查输出结果的有效性与可靠性，从而强化其批判性评估技能，降低对生成式 AI 的盲目依赖，并显著提升有意义人机交互的实现概率。[[Argument_Zhao_2025_JIntell|(Zhao et al., 2025, p. 14)]]
>
> *At the same time, the inherent limitations of Gen-AI, such as AI hallucinations, may catalyze critical thinking. The generation of inaccurate or misleading information compels students to scrutinize the validity and reliability of the outputs, thereby reinforcing their critical evaluation skills, reducing their reliance on Gen-AI, and increasing the likelihood of meaningful interactions with Gen-AI.*

> [!boundary]- 概念边界
> - **不等于 算法偏见（Algorithmic Bias）** 算法偏见反映的是训练数据分布不均或历史歧视的系统性再现（如性别或种族刻板印象）；AI 幻觉则是模型在缺失确定信息时进行的概率性“无中生有（Confabulation）”。
> - **不等于 [[Creativity|创造性]]联想（Creative Ideation）** 在小说构思与[[Brainstorming|头脑风暴]]中，虚构情节属于有益的创造性发散；但当任务情境切换为科学研究、学术论文或事实问答时，未经标记的虚构即构成有害的“幻觉”。

---

## 概念辨析

> [!contrast-table] 概念辨析
> | 比较维度 | **AI 幻觉（AI Hallucination）** | **算法偏见（Algorithmic Bias）** | **程序语法错误（Syntax/Runtime Error）** | **[[Creativity\|创造性]]虚构（Creative Confabulation）** |
> |---|---|---|---|---|
> | **本质特征** | 表层顺滑但事实虚构或逻辑断裂 | 统计样本偏差引发的系统性刻板印象 | 代码逻辑错误导致程序无法运行或崩溃 | 艺术与故事创作中的有意观念重组 |
> | **表现形式** | 捏造期刊论文、杜撰实验数据、伪造引文 | 输出带有性别/种族歧视倾向的结论 | 抛出错误代码（如 NullPointer、SyntaxError） | 虚构角色、情节、比喻与科幻场景 |
> | **感知难度** | **极高**（语调权威顺畅，极具欺骗性） | **中等**（需结合社会学与统计分布识别） | **极低**（系统直接报错并中断运行） | **低**（使用者预先知道是艺术创作） |
> | **教育应对策略** | 训练[[Epistemological Vigilance\|认识论警觉]]、多源[[Triangulation\|三角互证]]与一手核查 | 开设 [[AI Literacy\|AI 素养]]与伦理审查课程 | 讲授代码调试与编译器使用方法 | 引导发散构想并进入后期二次收敛审订 |

---

## 核心要素

> [!feature] 核心要素
> - **事实性虚构（Factual Hallucination）** 捏造历史事件、科学原理、地理常识或统计数据（如杜撰不存在的化学反应方程式）。[[Argument_Li_2026_CEAI|(Li et al., 2026, p. 6)]]
> - **引用性虚构（Source & Reference Fabrication）** 捏造格式极其规范但完全不存在的学术论文作者、DOI、期刊名与卷期号（学术写作中最普遍的幻觉形态）。[[Argument_Li_2026_CEAI|(Archila et al., 2024; Li et al., 2026, p. 11)]]
> - **逻辑推理断裂（Logical & Deductive Inconsistency）** 在长文本推导或数学证明中，前言不搭后语，每一步看似合理但整体推论存在致命逻辑跳跃。[[Argument_Li_2026_CEAI|(Urhan et al., 2024; Li et al., 2026, p. 7)]]
> - **顺应性误导（Sycophancy / User-Induced Bias）** 随着用户提问的诱导性倾向而顺应生成虚假支持理由，强化用户的确认偏误（Confirmation Bias）。

> [!logic-map]- 教育情境中 AI 幻觉的二元分化路径图
> ```mermaid
> flowchart TD
>     A["大语言模型生成包含幻觉 (Hallucination) 的内容"] --> B{"学习者的处理方式与教学支架"}
>     
>     subgraph 盲从与心智侵蚀路径["盲从与心智侵蚀路径 (Uncritical Acceptance)"]
>         B -->|"缺乏 AI 素养 / 无反思支架"| N1["被表面语义流畅性蒙蔽 (能力错觉)"]
>         N1 --> N2["直接复制粘贴至课程作业或论文中"]
>         N2 --> N3["引发学术不端、事实谬误与批判性思维萎缩"]
>     end
>     
>     subgraph 教学化转化路径["教学化转化路径 (Pedagogical Red-Teaming)"]
>         B -->|"嵌入红队查错任务 / 显性素养指引"| P1["激活认识论警觉与生产性认识论摩擦"]
>         P1 --> P2["开展一手文献核查与多源三角互证"]
>         P2 --> P3["成功识别模型盲区，实现批判性思维深化 (CT ↑)"]
>     end
>     
>     style N3 fill:#fee2e2,stroke:#ef4444,stroke-width:2px
>     style P3 fill:#dbeafe,stroke:#3b82f6,stroke-width:2px
> ```

---

## 围绕概念形成的命题

---

### 命题一　AI 幻觉是自回归大语言模型概率生成机制的内在副产物而非偶发故障

> [!concept-lens] 技术底层逻辑与[[Epistemology|认识论]]局限
> 解构大模型的运作本质，破除“AI 只是偶尔犯错、未来会很快彻底无错误”的技术乌托邦幻想。

> [!claim] Ji et al.; Li et al.
> **概率生成的内在幻觉性** 大语言模型不是事实检索数据库，而是基于高维向量空间进行概率采样的“词语预测引擎”。模型为了维持文本的自然流畅与语义连贯，在遇到知识盲区时天然倾向于基于统计联想填补空白，因而生成幻觉并非外部偶发 bug，而是生成式模型赖以运行的内在计算特性。[[Argument_Li_2026_CEAI|(Ji et al., 2023; Li et al., 2026, pp. 2, 10–11)]]

---

### 命题二　在非结构化学习中，AI 幻觉是诱发学术失范与心智惰性的核心风险源

> [!concept-lens] [[Cognitive Offloading|认知卸载]]与学术诚信危机
> 揭示学生在缺乏批判意识与自主调节能力时直接采纳幻觉内容的严重后果。

> [!claim] Li et al.; Zhao et al.
> **幻觉诱发的心智风险与自律脆弱性** 在缺乏显性指导的自由使用环境中，学生由于存在[[Illusion of Competence|能力错觉]]与惰性心理，极易将虚构引用与伪事实直接吸收到学术论文中，导致严重的论证漏洞与学术合规焦虑[[Argument_Li_2026_CEAI|(Li et al., 2026, pp. 6–8)]]。元分析进一步证实，自主调节学习（SRL）薄弱的学生缺乏对生成内容真实性与相关性的审验判断能力，更容易不加甄别地顺从和采纳包括幻觉在内的错误信息，导致人机交互难以转化为有意义的认知建构[[Argument_Zhao_2025_JIntell|(Zhao et al., 2025, pp. 11, 16)]]。

---

### 命题三　在结构化探究中，AI 幻觉可被教学化转化为激发批判性思维的认知靶子

> [!concept-lens] 教学转化与[[Epistemological Vigilance|认识论警觉]]培养
> 阐明教师与人机协同机制如何将技术缺陷转化为培养批判反思的脚手架。

> [!claim] Archila et al.; Li et al.; Zhao et al.
> **算法缺陷对批判性思维的倒逼与磨刀石效应** 当教师明确将 AI 输出设定为“包含潜在错误的初级素材”并设计对抗性查错（Red-teaming）任务时，AI 幻觉构成了极佳的反思磨刀石[[Argument_Li_2026_CEAI|(Archila et al., 2024; Li et al., 2026, pp. 6, 11–12)]]。元分析从实证层面阐明了这种反向催化机制：生成式 AI 固有的幻觉与不准确信息，在客观上倒逼学生放弃盲从顺从，主动审查输出结果的有效性与可靠性，从而显著强化了批判性评估技能（$g = 0.691$），降低了技术依赖并大幅提升了有意义人机交互的实现概率[[Argument_Zhao_2025_JIntell|(Zhao et al., 2025, pp. 10–11, 14)]]。

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心主张 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **技术机制命题** | 概率预测本质决定幻觉是生成式系统的内在属性 | 计算机科学、大模型原理与 AI 素养基础 | Ji et al.; Li et al. |
> | **风险侵蚀命题** | 无支架使用与低自律状态下幻觉诱发虚假掌握与认知顺从 | 开放性课后[[Homework\|作业]]、无监管学术写作 | Li et al.; Xu et al.; Zhao et al. |
> | **教学转化命题** | 结构化红队查错将幻觉转化为倒逼批判性思维深化的认知脚手架 | 科学写作探究、高校专业课程评估改革 | Archila et al.; Li et al.; Zhao et al. |

---

## 概念演变

> [!dev-timeline] 概念演变脉络
> - **2010 年代末 — 计算机视觉与自然语言初现** 幻觉概念最早用于描述深度神经网络在图像生成中出现的无意义伪影（[[Artefact|artifacts]]）及神经机器翻译中的凭空添词。
> - **2022–2023 年 — ChatGPT 爆发与大模型幻觉泛化** 随着生成式 AI 普及，幻觉特异性指向 LLMs 编造虚假事实与虚构学术引文的普遍现象，引发全球学术界关于研究可[[Reliability|信度]]的争论。
> - **2024–2026 年 — 学习科学与教育学教学化转向** 教育研究从单纯的“技术除错/封禁”转向“教学转化”，[[Argument_Li_2026_CEAI|Li et al. (2026)]]、Archila et al. (2024) 与 [[Argument_Zhao_2025_JIntell|Zhao et al. (2025)]] 系统确立了基于 AI 幻觉识别的[[Critical Thinking|批判性思维]]与[[Epistemological Vigilance|认识论警觉]]培养[[Paradigm|范式]]。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 技术解决论（RAG/检索增强） vs [[Epistemology|认识论]]防御论
> > 争论是否能通过检索增强生成（RAG）、知识图谱绑定或强化学习彻底消除幻觉。
> >
> > - **技术实在论** 认为随算法演进，事实幻觉将降至忽略不计水平。
> > - **认识论审视论（[[Argument_Li_2026_CEAI|Li et al., 2026]]）** 强调只要是基于概率采样的自回归架构，幻觉就不可能完全为零，人类学习者的[[Epistemological Vigilance|认识论警觉]]永远是不可替代的最后一道防线。
>
> > [!axis] 幻觉容忍度：发散创意（Affordance） vs 科学严谨（Hazard）
> > 在艺术创作与隐喻生成中，幻觉被视为[[Creativity|创造力]]的催化剂；而在 STEM 与学术研究中，幻觉则是必须严厉剔除的毒素。

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Li_2026_CEAI\|Li et al. (2026, p. 6)]] | 全球 67 项高等教育实证研究（2022–2025） | [[Systematic Review\|系统综述]]与主题综合（PRISMA 2020 框架） | 事实核查与查错机制主题（Fact-checking & Error Detection） | 19 项实证研究明确报告将 AI 幻觉识别设计为课堂核查任务，显著促进了学生的[[Critical Thinking\|批判性思维]]与多源验证习惯 | 87% 研究 MMAT $\ge 80\%$ | 确立 AI 幻觉在[[Structured Teaching\|结构化教学]]中作为[[Higher-Order Thinking Skills\|高阶思维]]训练载体的有效性 |
> | [[Argument_Li_2026_CEAI\|Li et al. (2026, p. 11)]] (引述 Archila et al., 2024) | 大学本科生科学写作课堂 | 教学干[[Pilot Testing\|预实验]]与文本分析 | 对抗性红队查错（Red-teaming）表现 | 学生在教师布置的去幻觉任务中，主动核查并成功标定出 14 处 ChatGPT 编造的虚假[[Document\|文献]]与错误科学论断 | — | 证实具体的查错量规能有效将对 AI 幻觉的警惕转化为可操作的实证探究行为 |
> | [[Argument_Li_2026_CEAI\|Li et al. (2026, p. 7)]] | 全球 67 项高等教育实证研究（2022–2025） | [[PRISMA]] 系统综述 | 缺乏幻觉核查导致的学术风险 | 14 项实证研究报告学生因未辨别 AI 幻觉而直接采纳错误引文，导致[[Homework\|作业]]论证逻辑破裂并面临学术诚信风险 | — | 揭示缺乏 AI 素养与幻觉防范规程时的普遍认知风险 |
> | [[Argument_Zhao_2025_JIntell\|Zhao et al. (2025, pp. 10–11, 14, 16)]] | 纳入全球 59 项独立实证研究（批判性思维子维度 $k = 20$） | 随机效应一阶[[Meta-analysis\|元分析]]与调节效应模型 | 批判性思维（$g = 0.691$）机制解释与自主调节能力（低 SRL 易感性） | 确立批判性思维在中等偏大水平显著提升（$g = 0.691$），理论机制模型证实 AI 幻觉具有倒逼审验的催化作用；同时亚组检验显示低 SRL 组促学效应微弱（$g = 0.284$），证实缺乏自律调控易深陷幻觉误导 | 组内 $Z = 5.973, p < 0.001$；SRL 组间 $Q_b = 40.962, p < 0.001$ | 实证表明 AI 幻觉转化为批判性思维动力高度依存于学习者的自我调节水平与显性查错支架 |

---

## 应用案例

> [!example] 典型教学应用案例
> - **科学论文写作中的“AI 幻觉红队对抗测试”（Archila et al., 2024; [[Argument_Li_2026_CEAI|Li et al., 2026]]）**
>   教师让 ChatGPT 针对某个争议性科学议题生成一篇包含 5 篇参考[[Document|文献]]的微综述，然后要求学生作为“学术审稿人（Reviewer）”，逐一检索 Web of Science 与 PubMed 数据库核对引文是否存在、引述结论是否被歪曲。该任务极大地锻炼了学生的[[Primary and Secondary Documents|一手文献]]溯源与实证辨析能力。
> - **“提示词去幻觉迭代与辩护答辩”考核规程**
>   在计算机编程与工程设计课中，教师允许使用 AI 辅助编写代码，但要求学生在答辩时必须展示：如何通过设计对比性提示词（Prompting）迫使模型暴露其潜在的逻辑幻觉与漏洞，并将去幻觉的过程性记录作为核心给分点。

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Zhao_2025_JIntell|Zhao et al. (2025)]] — 运用一阶元分析实证揭示生成式 AI 对批判性思维的显著促学效应（$g = 0.691$），从认知机理上提出 AI 幻觉对批判审验的倒逼催化机制，同时发现低自主调节学习能力者更容易受到幻觉误导。
> - [[Argument_Li_2026_CEAI|Li et al. (2026)]] — [[Systematic Review|系统综述]] 67 项高等教育 ChatGPT 实证研究，将 AI 幻觉识别与去幻觉查错确立为驱动[[Critical Thinking|批判性思维]]发展的核心教学机制。
> - [[Argument_RoyalSociety_2026_ScienceForSociety_Ch01|The Royal Society (2026)]] — 强调基础教育科学课程必须培养学生识别大模型幻觉与算法偏见的批判性数字素养。
