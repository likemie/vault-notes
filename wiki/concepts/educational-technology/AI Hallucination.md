---
title: AI Hallucination
aliases:
  - 人工智能幻觉
  - 大模型幻觉
  - Hallucination in AI
  - Machine Hallucination
  - Algorithmic Hallucination
  - LLM Hallucination
summary: "人工智能与教育技术学概念，指大语言模型等生成式系统输出看似连贯权威、语法高度流畅但实际上偏离客观事实、缺乏真实依据、虚构引用或逻辑自相矛盾的内容现象。"
type: concept
domain: "educational-technology"
related_count: 51
related_level: 5
related_stars: "⭐⭐⭐⭐⭐"
related_color: "#fecdd3"
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
  - "[[Scaffolding]]"
  - "[[Reliability]]"
  - "[[Epistemology]]"
  - "[[Evaluativist]]"
  - "[[Absolutist]]"
  - "[[Creativity]]"
  - "[[Brainstorming]]"
  - "[[AI Literacy]]"
  - "[[Causal Processes]]"
  - "[[Cognitive Offloading]]"
  - "[[Illusion of Competence]]"
  - "[[Self-Regulated Learning]]"
  - "[[Scientific Explanation]]"
  - "[[Alien Intelligence]]"
  - "[[Epistemic Deference]]"
  - "[[Homework]]"
  - "[[Artefact]]"
  - "[[Paradigm]]"
  - "[[Variable]]"
  - "[[Structured Teaching]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Epistemic Stances]]"
  - "[[Hypothesis]]"
  - "[[Growth]]"
  - "[[Dialogue in Education]]"
  - "[[Visible Learning]]"
  - "[[Automated Data Extraction]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Epistemic Agency]]"
related_theories:
  - "[[Formative Epistemic Injustice]]"
related_methods:
  - "[[Triangulation]]"
  - "[[Meta-analysis]]"
  - "[[Effect Size]]"
  - "[[Systematic Review]]"
  - "[[Pilot Testing]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Multimodal Discourse Analysis]]"
  - "[[Random Sampling]]"
  - "[[Correlational Research]]"
related_persons: []
related_arguments:
  - "[[Argument_Li_2026_CEAI]]"
  - "[[Argument_Zhao_2025_JIntell]]"
  - "[[Argument_Wu_2025_ER]]"
  - "[[Argument_Han_Gutierez_2026_IJSE]]"
  - "[[Argument_Smith_2026_SPE]]"
  - "[[Argument_Jansen_2026_EPR]]"
  - "[[Argument_RoyalSociety_2026_ScienceForSociety_Ch01]]"
related_instruments:
  - "[[PRISMA]]"
confidence: high
status: active
created: 2026-09-02
updated: 2026-09-24
---

# AI Hallucination
（AI 幻觉 / 大模型幻觉）

---

## 定义

> [!def] 核心定义
> AI 幻觉（AI Hallucination / Machine Hallucination）是指大语言模型（LLM）与[[Generative Artificial Intelligence\|生成式人工智能]]系统在生成文本、代码或多模态内容时，**输出在语法与语调上极具连贯性、说服力与权威感，但在客观事实上纯属虚构、缺乏真实证据支撑、编造学术[[Document\|文献]]或在逻辑上自相矛盾的内容现象**。其根源在于自回归深度神经网络基于统计概率预测下一词（Next-Token Prediction）的生成机制，而非基于对真实物理世界与逻辑真理的符号表征。[[Argument_Li_2026_CEAI\|(Ji et al., 2023; Li et al., 2026, pp. 2, 6, 11)]]

> [!concept-lens] 概念透镜
> - **含义** 区别于软件运行时的程序崩溃或逻辑报错，AI 幻觉是一种“静默且自信的错误生成”——系统以完美的自然语言包装虚假命题。
> - **用途** 在教育技术中具有“双刃剑”属性：既是诱发学生误解与学术失范的首要风险源，也是教学设计中通过“红队查错任务”激发[[Epistemological Vigilance\|认识论警觉]]与[[Critical Thinking\|批判性思维]]的核心[[Scaffolding\|认知脚手架]]。
> - **边界** 不等同于故意欺诈（AI 缺乏欺骗意图），亦不等同于单纯的训练数据偏见（幻觉常在无偏见情境下纯因概率拟合与联想泛化而凭空生成）。

> [!citation-card]- 关键表述：事实核查与去幻觉查错的教学转化（[[Argument_Li_2026_CEAI\|Li et al., 2026]]）
> 事实核查与去幻觉检验（Fact-checking & Hallucination Detection）构成了生成式 AI 赋能批判性思维的核心机制之一。在 19 项实证研究中，教师通过引导学生专门针对 AI 生成的文献与数据进行对抗性审验，有效将模型的缺陷转化为培养学生认识论警觉与多源实证核查习惯的教学契机。[[Argument_Li_2026_CEAI\|(Li et al., 2026, pp. 6, 11)]]
>
> *Fact-checking and error detection (n = 19) emerged as a major affordance for critical thinking... engaging students in "red-teaming" AI-generated claims turns hallucination into a pedagogical catalyst for epistemic vigilance.*

> [!citation-card]- 关键表述：AI 幻觉对批判性思维的意外倒逼机制（[[Argument_Zhao_2025_JIntell\|Zhao et al., 2025]]）
> 生成式人工智能的固有缺陷（例如 AI 幻觉）能够有效催化批判性思维。不准确或误导性信息的生成，迫使学生主动审查输出结果的有效性与[[Reliability\|可靠性]]，从而强化其批判性评估技能，降低对生成式 AI 的盲目依赖，并显著提升有意义人机交互的实现概率。[[Argument_Zhao_2025_JIntell\|(Zhao et al., 2025, p. 14)]]
>
> *At the same time, the inherent limitations of Gen-AI, such as AI hallucinations, may catalyze critical thinking. The generation of inaccurate or misleading information compels students to scrutinize the validity and reliability of the outputs, thereby reinforcing their critical evaluation skills, reducing their reliance on Gen-AI, and increasing the likelihood of meaningful interactions with Gen-AI.*

> [!citation-card] 算法幻觉作为[[Epistemology\|认识论]]演进的扰动契机
> 在人机共生学习中，大语言模型的算法幻觉构成了促发学习者认识论扰动（Epistemic Perturbation）的关键契机。面对模型输出的破绽，绝对主义者因盲信而陷入错误扩散，而[[Evaluativist\|评价主义者]]则将幻觉转化为驱动多源交叉核验与批判性审问的认知磨刀石。[[Argument_Wu_2025_ER\|(Wu et al., 2025, pp. 364–365)]]
>
> *Algorithmic hallucination acts as an epistemic perturbation: while [[Absolutist\|absolutists]] uncritically accept erroneous fabrications, evaluativists leverage hallucinations as catalysts for multi-source [[Triangulation]] and epistemic interrogation.*

> [!boundary]- 概念边界
> - **不等于 算法偏见（Algorithmic Bias）** 算法偏见反映的是训练数据分布不均或历史歧视的系统性再现（如性别或种族刻板印象）；AI 幻觉则是模型在缺失确定信息时进行的概率性“无中生有（Confabulation）”。
> - **不等于 [[Creativity\|创造性]]联想（Creative Ideation）** 在小说构思与[[Brainstorming\|头脑风暴]]中，虚构情节属于有益的创造性发散；但当任务情境切换为科学研究、学术论文或事实问答时，未经标记的虚构即构成有害的“幻觉”。

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
> - **事实性虚构（Factual Hallucination）** 捏造历史事件、科学原理、地理常识或统计数据（如杜撰不存在的化学反应方程式）。[[Argument_Li_2026_CEAI\|(Li et al., 2026, p. 6)]]
> - **引用性虚构（Source & Reference Fabrication）** 捏造格式极其规范但完全不存在的学术论文作者、DOI、期刊名与卷期号（学术写作中最普遍的幻觉形态）。[[Argument_Li_2026_CEAI\|(Archila et al., 2024; Li et al., 2026, p. 11)]]
> - **逻辑推理断裂（Logical & Deductive Inconsistency）** 在长文本推导或数学证明中，前言不搭后语，每一步看似合理但整体推论存在致命逻辑跳跃。[[Argument_Li_2026_CEAI\|(Urhan et al., 2024; Li et al., 2026, p. 7)]]
> - **顺应性误导（Sycophancy / User-Induced Bias）** 随着用户提问的诱导性倾向而顺应生成虚假支持理由，强化用户的确认偏误（Confirmation Bias）。
> - **伪完整性机制遗漏（Pseudo-completeness & Mechanistic Omission）** 生成式模型生成表层语法极其流畅、情节生动（如四季豆生长的童话拟人化叙述），但实质上省略了关键物理/生物微观因果机制（如根茎水分输运或分类学上位界定）的“隐蔽性不完整”，造成对科学原理的伪表征。[[Argument_Han_Gutierez_2026_IJSE\|(Han & Gutierez, 2026, pp. 11–16)]]
> - **多模态静态表征偏差（Multimodal Static Representation Bias）** 图像生成模型倾向于生成具象但静态的宏观外貌插图（如仅画出根部插入泥土），缺乏反映动态流动、因果方向与微观解剖特征（如吸水根毛与渗透流动箭头）的科学表征，容易诱发学生对动态[[Causal Processes|因果过程]]的错误感知。[[Argument_Han_Gutierez_2026_IJSE\|(Han & Gutierez, 2026, pp. 16–18)]]
> - **权威自信表象与非具身盲视（Confident Fallibility & Disembodied Blindness）** 大模型在出现事实性与常识性谬误时，依然以极端流畅、权威和自信的语调进行论述（confidently gets something wrong）；且由于缺乏人类具身生活世界（dis-embodied existence）与现实物理经验，模型无法凭借直觉常识辨识脱离现实的荒谬空想。[[Argument_Smith_2026_SPE\|(Smith, 2026, pp. 7, 10)]]

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

> [!concept-lens] 技术底层逻辑与[[Epistemology\|认识论]]局限
> 解构大模型的运作本质，破除“AI 只是偶尔犯错、未来会很快彻底无错误”的技术乌托邦幻想。

> [!claim] Ji et al.; Li et al.
> **概率生成的内在幻觉性** 大语言模型不是事实检索数据库，而是基于高维向量空间进行概率采样的“词语预测引擎”。模型为了维持文本的自然流畅与语义连贯，在遇到知识盲区时天然倾向于基于统计联想填补空白，因而生成幻觉并非外部偶发 bug，而是生成式模型赖以运行的内在计算特性。[[Argument_Li_2026_CEAI\|(Ji et al., 2023; Li et al., 2026, pp. 2, 10–11)]]

---

### 命题二　在非结构化学习中，AI 幻觉是诱发学术失范与心智惰性的核心风险源

> [!concept-lens] [[Cognitive Offloading\|认知卸载]]与学术诚信危机
> 揭示学生在缺乏批判意识与自主调节能力时直接采纳幻觉内容的严重后果。

> [!claim] Li et al.; Zhao et al.
> **幻觉诱发的心智风险与自律脆弱性** 在缺乏显性指导的自由使用环境中，学生由于存在[[Illusion of Competence\|能力错觉]]与惰性心理，极易将虚构引用与伪事实直接吸收到学术论文中，导致严重的论证漏洞与学术合规焦虑[[Argument_Li_2026_CEAI\|(Li et al., 2026, pp. 6–8)]]。[[Meta-analysis\|元分析]]进一步证实，[[Self-Regulated Learning\|自主调节学习]]（SRL）薄弱的学生缺乏对生成内容真实性与相关性的审验判断能力，更容易不加甄别地顺从和采纳包括幻觉在内的错误信息，导致人机交互难以转化为有意义的认知建构[[Argument_Zhao_2025_JIntell\|(Zhao et al., 2025, pp. 11, 16)]]。

---

### 命题三　在结构化探究中，AI 幻觉可被教学化转化为激发批判性思维与认识论演进的认知靶子

> [!concept-lens] 教学转化与[[Epistemological Vigilance\|认识论警觉]]培养
> 阐明教师与人机协同机制如何将技术缺陷转化为培养批判反思与促成[[Evaluativist\|评价主义认识立场]]跃迁的[[Scaffolding\|脚手架]]。

> [!claim] Archila et al.; Li et al.; Zhao et al.; Wu et al.
> **算法缺陷对[[Critical Thinking\|批判性思维]]的倒逼与认识论重塑效应** 当教师明确将 AI 输出设定为“包含潜在错误的初级素材”并设计对抗性查错（Red-teaming）任务时，AI 幻觉构成了极佳的反思磨刀石[[Argument_Li_2026_CEAI\|(Archila et al., 2024; Li et al., 2026, pp. 6, 11–12)]]。元分析证实，生成式 AI 固有的幻觉与不准确信息，在客观上倒逼学生放弃盲从，显著强化批判性评估技能（$g = 0.691$）[[Argument_Zhao_2025_JIntell\|(Zhao et al., 2025, pp. 10–11, 14)]]。实证研究进一步从认识论视角揭示，算法幻觉构成了促发认识论扰动（Epistemic Perturbation）的教学契机：绝对主义者盲信幻觉导致错误扩散，而结合提示词与同行评议支架，能够引导学生直面算法破绽，激发出多源实证核验动机，促成向[[Evaluativist\|评价主义认识立场]]的跨越。[[Argument_Wu_2025_ER\|(Wu et al., 2025, pp. 364–366)]]

> [!claim] Han, J., & Gutierez, S. B.
> **学科评价标准驱动中学生穿透 AI 幻觉与机制遗漏** 在人机协同[[Scientific Explanation|科学解释建构]]中，初中生面对生成式 AI（Canva 与 ChatGPT）产出的流畅童话故事与静态图解时，依托显性学科解释标准（相关性、因果叙事、概念框架、适切表征水平）实施对抗性审问：不仅识别出关于植物器官功能的碎片化罗列，更精准捕获了因果链条断裂与真菌界分类遗漏，通过针对性重构提示词与多模态补充促使 AI 生成更严谨的科学机制模型。[[Argument_Han_Gutierez_2026_IJSE\|(Han & Gutierez, 2026, pp. 11–18)]]

> [!claim] Smith; Braun & Meacham
> **[[Alien Intelligence|异己智能]]定位、事实核查规程与离散步骤防御** 面对大语言模型“极其自信地输出事实错误”（confidently gets something wrong）的固有幻觉特性，防范成长性认识伤害的关键在于打破将大模型视为全知私厨或人类伙伴的拟人化幻想，将其概念化为缺乏人类道德关怀与物理生活经验的[[Alien Intelligence|异己智能]]（Alien Intelligence；Braun & Meacham, 2024）。在具体教学中，教师强制推行两重操作性防御规程：一是**独立事实核查规程（Confirming Factual Information）**，严格要求学生核实 AI 给出的任何事实性数据，将排查幻觉常态化；二是**推行思维步骤全外显（Showing Steps）**，要求学生将复杂问题分解为离散步骤并写出推导痕迹，确保学生即使借助 AI 亦能清晰把握完整的解题认知地图，在对抗性查错中牢固捍卫主体的认识自主权。[[Argument_Smith_2026_SPE\|(Smith, 2026, pp. 10–11)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心主张 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **技术机制命题** | 概率预测本质决定幻觉是生成式系统的内在属性 | 计算机科学、大模型原理与 AI 素养基础 | Ji et al.; Li et al. |
> | **风险侵蚀命题** | 无支架使用与低自律状态下幻觉诱发虚假掌握与[[Epistemic Deference\|认知顺从]] | 开放性课后[[Homework\|作业]]、无监管学术写作 | Li et al.; Xu et al.; Zhao et al. |
> | **教学转化与认识跃迁** | 结构化查错与异己智能定位将幻觉转化为倒逼批判性思维与评价论演进的认知靶子 | 科学写作探究、统计推论决策、人文学科批判性读写 | Archila et al.; Li et al.; Zhao et al.; [[Argument_Wu_2025_ER\|Wu et al. (2025)]]; [[Argument_Han_Gutierez_2026_IJSE\|Han & Gutierez (2026)]]; [[Argument_Smith_2026_SPE\|Smith (2026)]] |

---

## 概念演变

> [!dev-timeline] 概念演变脉络
> - **2010 年代末 — 计算机视觉与自然语言初现** 幻觉概念最早用于描述深度神经网络在图像生成中出现的无意义伪影（[[Artefact\|artifacts]]）及神经机器翻译中的凭空添词。
> - **2022–2023 年 — ChatGPT 爆发与大模型幻觉泛化** 随着生成式 AI 普及，幻觉特异性指向 LLMs 编造虚假事实与虚构学术引文的普遍现象，引发全球学术界关于研究可[[Reliability\|信度]]的争论。
> - **2024–2026 年 — 学习科学与教育学教学化转向** 教育研究从单纯的“技术除错/封禁”转向“教学转化”，[[Argument_Li_2026_CEAI\|Li et al. (2026)]]、Archila et al. (2024) 与 [[Argument_Zhao_2025_JIntell\|Zhao et al. (2025)]] 系统确立了基于 AI 幻觉识别的[[Critical Thinking\|批判性思维]]与[[Epistemological Vigilance\|认识论警觉]]培养[[Paradigm\|范式]]。
> - **2025 年 — 人机共生[[Epistemology\|认识论]]扰动机制确立** [[Argument_Wu_2025_ER\|Wu et al. (2025)]] 实证揭示算法幻觉作为诱发认识论扰动的核心催化剂，确立了通过双轨支架将幻觉转化为评价主义立场跃迁的干预机制。
> - **2026 年 — 多模态伪完整性审验与学科标准支架** [[Argument_Han_Gutierez_2026_IJSE\|Han & Gutierez (2026)]] 揭示生成式 AI 在[[Scientific Explanation|科学解释]]中的伪完整性与静态图解表征偏差，实证确立学科四维标准在初中生识别机制断裂与图解纠偏中的支架效能。
> - **2026 年 — [[Alien Intelligence|异己智能]]定位与批判性防御规程确立** [[Argument_Smith_2026_SPE\|Smith (2026)]] 揭示大模型自信输出事实谬误的幻觉特征，提出将 AI 概念化为缺乏人类具身生活经验的“异己智能”，通过独立事实核查规程与思维步骤全外显构建防范成长性认识伤害的教学防线。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 技术解决论（RAG/检索增强） vs [[Epistemology\|认识论]]防御论
> > 争论是否能通过检索增强生成（RAG）、知识图谱绑定或强化学习彻底消除幻觉。
> >
> > - **技术实在论** 认为随算法演进，事实幻觉将降至忽略不计水平。
> > - **认识论审视论（[[Argument_Li_2026_CEAI\|Li et al., 2026]]; [[Argument_Wu_2025_ER\|Wu et al., 2025]]）** 强调只要是基于统计概率采样的自回归架构，幻觉就不可能完全为零；大模型经常极其自信地输出事实错误，人类学习者的[[Epistemological Vigilance\|认识论警觉]]与事实核查责任永远是不可替代的最后防线。
>
> > [!axis] 幻觉容忍度：发散创意（Affordance） vs 事实严谨与求知发展（Hazard）
> > 在艺术创作与隐喻生成中，幻觉被视为[[Creativity\|创造力]]的催化剂；而在学术写作与育人情境中，自信的幻觉被视为心智侵蚀源。
> >
> > - **创意宽容论** 认为在[[Brainstorming|头脑风暴]]与虚构叙事中，无序幻觉有助于打破常规联想定势。
> > - **求知伤害警示论（[[Argument_Smith_2026_SPE\|Smith, 2026]]）** 警示在未成年人学习期，AI 幻觉的隐蔽性在于其语言表层的权威流畅性，缺乏事实核查与[[Alien Intelligence|异己智能]]警觉的学生极易把虚构当作真理直接内化，诱发深层的[[Formative Epistemic Injustice|成长性认识不正义]]。

---

## 实证数据

> [!ref-table]- 其他实证结果（无[[Effect Size\|效应量]]）
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无效应量） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Li_2026_CEAI\|Li et al. (2026, p. 6)]] | 全球 67 项高等教育实证研究（2022–2025） | [[Systematic Review\|系统综述]]与主题综合（PRISMA 2020 框架） | 事实核查与查错机制主题（Fact-checking & Error Detection） | 19 项实证研究明确报告将 AI 幻觉识别设计为课堂核查任务，显著促进了学生的[[Critical Thinking\|批判性思维]]与多源验证习惯 | 87% 研究 MMAT $\ge 80\%$ | 确立 AI 幻觉在[[Structured Teaching\|结构化教学]]中作为[[Higher-Order Thinking Skills\|高阶思维]]训练载体的有效性 |
> | [[Argument_Li_2026_CEAI\|Li et al. (2026, p. 11)]] (引述 Archila et al., 2024) | 大学本科生科学写作课堂 | 教学干[[Pilot Testing\|预实验]]与文本分析 | 对抗性红队查错（Red-teaming）表现 | 学生在教师布置的去幻觉任务中，主动核查并成功标定出 14 处 ChatGPT 编造的虚假[[Document\|文献]]与错误科学论断 | — | 证实具体的查错量规能有效将对 AI 幻觉的警惕转化为可操作的实证探究行为 |
> | [[Argument_Li_2026_CEAI\|Li et al. (2026, p. 7)]] | 全球 67 项高等教育实证研究（2022–2025） | [[PRISMA]] 系统综述 | 缺乏幻觉核查导致的学术风险 | 14 项实证研究报告学生因未辨别 AI 幻觉而直接采纳错误引文，导致[[Homework\|作业]]论证逻辑破裂并面临学术诚信风险 | — | 揭示缺乏 AI 素养与幻觉防范规程时的普遍认知风险 |
> | [[Argument_Zhao_2025_JIntell\|Zhao et al. (2025, pp. 10–11, 14, 16)]] | 纳入全球 59 项独立实证研究（批判性思维子维度 $k = 20$） | 随机效应一阶[[Meta-analysis\|元分析]]与调节效应模型 | 批判性思维（$g = 0.691$）机制解释与自主调节能力（低 SRL 易感性） | 确立批判性思维在中等偏大水平显著提升（$g = 0.691$），理论机制模型证实 AI 幻觉具有倒逼审验的催化作用；同时亚组检验显示低 SRL 组促学效应微弱（$g = 0.284$），证实缺乏自律调控易深陷幻觉误导 | 组内 $Z = 5.973, p < 0.001$；SRL 组间 $Q_b = 40.962, p < 0.001$ | 实证表明 AI 幻觉转化为批判性思维动力高度依存于学习者的自我调节水平与显性查错支架 |
> | [[Argument_Wu_2025_ER\|Wu et al. (2025, pp. 363–366)]] | N=124 师范生统计分析任务 | 2x2 [[Randomised Controlled Trials\|随机对照实验]]与人机交互追踪 | 算法幻觉识别率与[[Epistemic Stances\|认识立场]]演进 | 实验组通过提示词约束使大模型显式输出前提[[Hypothesis\|假设]]，学生成功识别出 ChatGPT 在正态性假设上的算法幻觉，多源验证行为显著增加，评价论达成率显著提升 | $p < .01$ | 证实幻觉在双轨支架下能有效转化为认识论进阶的催化剂 |
> | [[Argument_Han_Gutierez_2026_IJSE\|Han & Gutierez (2026, pp. 11–18)]] | 韩国 8 名初中生，两节人机协同科学课（植物[[Growth\|生长]]与真菌分类） | 质性多层[[Multimodal Discourse Analysis\|多模态话语分析]]（录像转录、数字生成物、访谈） | AI 伪完整性识别与多模态图表纠偏表现 | 初中生在 4 组[[Dialogue in Education\|对话]]中敏锐指出 AI 叙事性童话掩盖了水分运输机制，并识别出静态插图缺乏水流渗透箭头，通过迭代提示词促使 AI 补全机制与微观结构 | 质性微观对话与制品分析 | 确立学科标准在初中生识破 AI 伪完整性与多模态表征偏差中的有效支架功能 |
> | [[Argument_Jansen_2026_EPR\|Jansen et al. (2026, pp. 16–18)]] | 156 项教育元分析（[[Visible Learning\|可见的学习]]数据库[[Random Sampling\|随机抽样]]，468 个数据点） | 大模型提取准确性与金标准仲裁评测（Gemini 2.5 Pro、GPT-4.1、GPT-o3） | [[Automated Data Extraction\|自动化数据提取]]中的事实幻觉与信息遗漏 | 在 55 项原文缺失对应统计量的元分析中，三大前沿 LLM 仅产生 3–4 例事实性幻觉（与人类专家的 3–4 例完全持平）；而信息遗漏更为普遍（LLM 遗漏 21–36 例 vs 专家 12–31 例） | $\text{ICC} = 0.96–0.97$（模型 vs 金标准） | 证实前沿 LLM 在严格提示词下事实性幻觉发生率极低，误差主要由长文本信息遗漏与多表累加疏漏驱动 |

---

## 应用案例

> [!example] 典型教学应用案例
> - **科学论文写作中的“AI 幻觉红队对抗测试”（Archila et al., 2024; [[Argument_Li_2026_CEAI\|Li et al., 2026]]）**
>   教师让 ChatGPT 针对某个争议性科学议题生成一篇包含 5 篇参考[[Document\|文献]]的微综述，然后要求学生作为“学术审稿人（Reviewer）”，逐一检索 Web of Science 与 PubMed 数据库核对引文是否存在、引述结论是否被歪曲。该任务极大地锻炼了学生的[[Primary and Secondary Documents\|一手文献]]溯源与实证辨析能力。
> - **“提示词去幻觉迭代与辩护答辩”考核规程（[[Argument_Wu_2025_ER\|Wu et al., 2025]]）**
>   在统计决策与研究设计课中，要求学生利用提示词迫使模型暴露其潜在的逻辑幻觉与适用边界，并将去幻觉的多源核验记录与同行评议辩护作为核心考核依据。
> - **中学生多模态[[Scientific Explanation|科学解释]]“去伪存真与机制补全”探究（[[Argument_Han_Gutierez_2026_IJSE\|Han & Gutierez, 2026]]）**
>   初中科学课上引导学生运用四维科学解释标准审查 AI 生成的四季豆生长童话与植物根部插图，自主发现机制断裂与图解表征失真，并重构提示词以补全因果微观机制。
> - **随堂低利害对比与事实核查微实验（[[Argument_Smith_2026_SPE\|Smith, 2026]]）**
>   教师在课堂上设计低利害任务（如撰写感谢信），引导学生将自主完成的初稿与大模型版本并置对比，逐句排查 AI 生成的事实细节并反向审问修辞理由，使学生在无高压考核的情境下固化对 AI 自信幻觉的事实核查习惯。

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research\|相关研究]]索引
> - [[Argument_Wu_2025_ER\|Wu et al. (2025)]] — 提出人机共生自适应[[Epistemic Stances\|认识立场]]框架，实证揭示算法幻觉作为[[Epistemology\|认识论]]扰动契机如何通过双轨支架驱动学生向评价主义演进。
> - [[Argument_Zhao_2025_JIntell\|Zhao et al. (2025)]] — 运用一阶[[Meta-analysis\|元分析]]实证揭示生成式 AI 对[[Critical Thinking\|批判性思维]]的显著促学效应（$g = 0.691$），从认知机理上提出 AI 幻觉对批判审验的倒逼催化机制，同时发现低[[Self-Regulated Learning\|自主调节学习]]能力者更容易受到幻觉误导。
> - [[Argument_Li_2026_CEAI\|Li et al. (2026)]] — [[Systematic Review\|系统综述]] 67 项高等教育 ChatGPT 实证研究，将 AI 幻觉识别与去幻觉查错确立为驱动[[Critical Thinking\|批判性思维]]发展的核心教学机制。
> - [[Argument_Han_Gutierez_2026_IJSE\|Han & Gutierez (2026)]] — 揭示中学生如何运用学科四维解释标准识别并纠正生成式 AI 在文本叙事中的因果机制遗漏与多模态图像中的静态表征偏差。
> - [[Argument_Jansen_2026_EPR\|Jansen et al. (2026)]] — 在 156 项教育元分析的[[Automated Data Extraction\|自动化数据提取]]中系统评测大模型幻觉与遗漏率，证实模型事实性幻觉发生率极低且与人类专家持平。
> - [[Argument_RoyalSociety_2026_ScienceForSociety_Ch01\|The Royal Society (2026)]] — 强调基础教育科学课程必须培养学生识别大模型幻觉与算法偏见的批判性数字素养。
> - [[Argument_Smith_2026_SPE\|Smith (2026)]] — 揭示大语言模型自信输出事实谬误的幻觉特征，提出将 AI 概念化为缺乏具身生命的“[[Alien Intelligence|异己智能]]”，推行事实核查规程与思维步骤全外显以捍卫求知者的[[Epistemic Agency|认识主体性]]。
