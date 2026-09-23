---
title: Automation Bias
aliases:
  - 自动化偏差
  - 自动化偏见
  - 弱自动化偏差与强自动化偏差
  - 弱自动化偏差
  - 强自动化偏差
  - Weak and Strong Automation Bias
  - Weak Automation Bias
  - Strong Automation Bias
  - Commission and Omission Errors
summary: "人机交互、认知心理学与人工智能伦理核心构念，指人类操作者过度依赖自动化或人工智能决策支持系统的提示（或沉默），甚至在面对相左证据时仍放弃自主判断或忽视矛盾线索的系统性决策偏差。"
type: concept
domain: "educational-technology"
related_count: 24
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - concept/educational-technology
  - theme/artificial-intelligence
  - theme/ai-ethics
  - theme/human-ai-interaction
  - theme/cognitive-bias
related_concepts:
  - "[[Generative Artificial Intelligence]]"
  - "[[Trust Calibration]]"
  - "[[Epistemology]]"
  - "[[Epistemic Deference]]"
  - "[[Epistemic Friction]]"
  - "[[Cognitive Deskilling]]"
  - "[[Meaningful Human Control]]"
  - "[[AI Agent in Education]]"
  - "[[Defeater]]"
  - "[[Necessary and Sufficient Conditions]]"
  - "[[Reliability]]"
  - "[[Façade of Rationality]]"
  - "[[Illusion of Competence]]"
  - "[[Variable]]"
  - "[[Evaluative Judgement]]"
  - "[[Metacognition]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Correlational Research]]"
  - "[[Systematic Review]]"
related_instruments: []
related_persons:
  - "[[Socrates]]"
related_facts: []
related_arguments:
  - "[[Argument_Jovchevski_2026_PT]]"
  - "[[Argument_Jansen_2026_EPR]]"
  - "[[Argument_Li_2026_CEAI]]"
  - "[[Argument_Du_Yuan_2026_AIS]]"
confidence: high
status: draft
created: 2026-09-22
updated: 2026-09-22
---

# Automation Bias
（自动化偏差 / 弱自动化偏差与强自动化偏差）

---

## 定义

> [!def] 核心定义
> 自动化偏差（Automation Bias）是指人类操作者在人机协同决策情境中，将自动化或人工智能（[[Generative Artificial Intelligence|Artificial Intelligence]], AI）决策支持系统的提示（或其沉默）作为替代自主信息搜集与审思的启发式替代品，过度依赖系统线索而产生执行错误（Commission Errors）或遗漏错误（Omission Errors）的系统性决策倾向。[[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026, pp. 2–5)]] 根据操作者对矛盾证据的接触与认知卷入程度，可进一步划分为两类形态：
> 1. **弱自动化偏差（Weak Automation Bias）** 操作者在未主动查阅或忽略唾手可得的相左证据的情况下，盲目追随系统的提示或沉默，其认知机制源于认知吝啬与警觉性替代，在伦理上构成应知而未注意的过失疏忽（Culpable Negligence）；
> 2. **强自动化偏差（Strong Automation Bias）** 操作者在已经察觉、记录或权衡了矛盾证据，甚至自身已形成相反判断的情况下，依然顺从系统的提示或沉默，其根源在于[[Trust Calibration|信任失调]]（Miscalibrated Trust）与过度信任（Overtrust），并在[[Epistemology|认识论]]上构成了对技术系统的[[Epistemic Deference|认识论顺从]]（[[Epistemic Deference]]）。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 1–2, 6–11)]]

> [!concept-lens] 概念透镜
> - **含义** 揭示人类在面对自动化与智能决策支持系统时，注意力分配、证据权衡与最终裁决权发生扭曲的认知与规范失调机制。
> - **用途** 解释航空、医疗、司法及军事等高风险情境中人机协同决策为何频繁出现系统性失效，指导人机交互界面通过注入[[Epistemic Friction|认知摩擦]]与反思机制来校准信任。
> - **边界** 区别于纯粹的技术故障或算法本身的统计偏差；自动化偏差特指人类对系统输出的解释、评估与过度顺从行为，且必须在存在矛盾证据或系统未提示应有警报的背景下才能被诊断。

> [!citation-card] 弱自动化偏差与强自动化偏差的实质分野（[[Argument_Jovchevski_2026_PT|Jovchevski et al., 2026]]）
> 我们区分了弱自动化偏差与强自动化偏差：在弱自动化偏差中，用户在未查阅与之相矛盾且唾手可得的证据的情况下追随系统的自动化提示（或其沉默）；而在强自动化偏差中，用户即使已经意识到这些矛盾证据，却仍然追随系统的提示（或其沉默）。弱自动化偏差类似于基于自动化的自满，可合理地与人类操作者的过失相联系；而强自动化偏差则揭示了操作者对自动化系统过度且无根据的信任转移，导致前者对后者的提示产生认识论顺从。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, p. 1)]]
>
> *We distinguish between weak automation bias, where users follow system's automated cues (or its silence) without consulting readily accessible evidence that contradicts them, and strong automation bias, where users follow such cues (or their absence) even when they are aware of such evidence. While weak automation bias, in our view, resembles automation-based complacency and is plausibly associated with negligence on the part of the human operator, strong automation bias reveals an excessive and unwarranted transfer of trust from operators to automated systems which results in epistemic deference of the former to the prompts of the latter.*

> [!boundary]- 概念边界辨析
> - **区别于 自动化自满（Automation Complacency）** 自动化自满通常指多任务监控负荷下对系统状态的注意力分配不足与全面懈怠；自动化偏差特指决策情境中，启发式规则或过度信任直接扭曲对特定线索的权衡与裁决动作。弱自动化偏差在表现上与自满高度重叠，而强自动化偏差则发生在注意力已经投入且证据已被注意的深层认知加工阶段。
> - **区别于 算法偏差（Algorithmic Bias）** 算法偏差指模型内部训练数据代表性不足或算法逻辑造成的统计偏误；自动化偏差则是人类操作者在面对算法输出时的社会认知与心理评价偏差。
> - **区别于 理性认识顺从（Rational Epistemic Deference）** 当智能系统在客观能力、计算速度与验证复杂度上显著超越人类且不可验证时，向系统让渡判断属于工具理性；而强自动化偏差特指在人类拥有反常证据且具备反思能力的情境下，仍做出无根据的非理性顺从。

---

## 概念辨析

> [!contrast-table] 自动化偏差、自动化自满与算法偏差对比
> | 维度 | 弱自动化偏差 | 强自动化偏差 | 自动化自满（Complacency） | 算法偏差（Algorithmic Bias） |
> |---|---|---|---|---|
> | **核心机制** | 认知吝啬，将系统线索作为警觉性的启发式替代 | 信任过度与失调，向算法让渡权威形成[[Epistemic Deference\|认识论顺从]] | 监控负荷下注意力衰退与依赖性懈怠 | 模型数据采样偏差或算法损失函数失衡 |
> | **证据接触状态** | 存在可用反常证据但**未主动查阅** | 已**察觉并权衡**反常证据但仍推翻自身判断 | 遗漏对多路监控仪表的主动扫描 | 算法内部机制，与操作者即时认知无关 |
> | **主要错误类型** | 执行错误与遗漏错误并存（偏向疏忽） | 执行错误与遗漏错误并存（偏向顺从） | 主要是未及时发现异常的遗漏错误 | 系统性预测偏向或分类不公 |
> | **规范性伦理性质** | 应知而未注意的过失疏忽（Negligence） | 侵蚀自主能动性并放弃道德判断义务 | 角色职责层面的注意力失职 | 技术正义与算法公平缺陷 |

---

## 核心要素与表现形态

> [!feature] 自动化偏差的核心要素与表现形式
> - **执行错误（Commission Errors）** 操作者直接遵循系统给出的错误指令或误报警报（False Alarms），即使现场存在其他指示系统错误的物理读数或环境线索。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, p. 4)]]
> - **遗漏错误（Omission Errors）** 当真实危险或关键事件发生而自动化系统未发出警报时，操作者因系统未提示而未能采取必要行动。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, p. 5)]]
> - **警觉性替代（Replacement of Vigilance）** 认知主体以系统状态作为判断环境的代理指标，终止自主多源交叉验证。
> - **[[Trust Calibration|信任失调]]与过度信任（Miscalibrated Overtrust）** 操作者赋予系统的信任程度严重超出该系统在特定情境下的客观能力与适用极限。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 6–9)]]

> [!logic-map]- 自动化偏差的两类路径与伦理危害推导图
> ```mermaid
> flowchart TD
>     A["人机协同决策情境（存在相左证据）"] --> B{"操作者对证据的认知卷入"}
>     B -->|"未主动查阅 / 忽略证据"| C["弱自动化偏差（Weak Automation Bias）"]
>     B -->|"已察觉 / 权衡矛盾证据"| D["强自动化偏差（Strong Automation Bias）"]
>     
>     C --> C1["认知吝啬与警觉性启发替代"]
>     C1 --> C2["过失疏忽（Culpable Negligence）"]
>     
>     D --> D1["信任失调与过度信任（Overtrust）"]
>     D1 --> D2["认识论顺从（Epistemic Deference）"]
>     D2 --> E1["程序主义：信念修正能力失效，削弱自主能动性"]
>     D2 --> E2["实质主义：制度性抗辩成本与去技能化削弱权威"]
>     D2 --> E3["伦理维度：架空有意义人类控制，违背道德裁决义务"]
>     
>     E1 & E2 & E3 --> F["高风险决策严重后果（如误击、误诊、误判）"]
> ```

---

## 围绕概念形成的命题

---

### 命题一　弱自动化偏差根植于认知吝啬，强自动化偏差由过度信任与认识论顺从驱动

> [!concept-lens] 认知启发式视角与[[Trust Calibration|过度信任]]视角的整合
> 辨析自动化偏差在认知心理学与社会[[Epistemology|认识论]]中的双重机制基础。

> [!claim] Mosier et al. (1998); Skitka et al. (2000); [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]]
> **启发式替代与过度信任的分流** 传统的认知启发式视角将自动化偏差定义为在决策中以系统线索替代警觉性信息搜索的启发式偏误，基于认知吝啬（Cognitive Miser）假说解释了弱自动化偏差；然而，当操作者在已明确感知反常证据的情况下依然放弃自身立场追随系统时，启发式模型无法提供充分解释。强自动化偏差的实质是操作者对系统能力的信任严重超出其客观边界（过度信任），从而在社会认识论层面将系统视作更高权威，发生深层的[[Epistemic Deference|认识论顺从]]（[[Epistemic Deference]]）。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 4–11)]]

---

### 命题二　强自动化偏差从程序与实质双重维度侵蚀人类操作者的自主能动性

> [!concept-lens] 自主行动能力与社会技术制度架构
> 解构强自动化偏差如何破坏人类作为独立自主行动者的核心条件。

> [!claim] [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]]
> **信念修正失效与关系性权威削弱** 在程序主义视角下，理性自主要求行动者具备根据新证据修正信念的能力；操作者在面对累积的反向证据时持续顺从系统错误输出，表明其信念修正能力受到系统性抑制，构成了程序性自主的瓦解。在实质主义与关系自主视角下，自动化偏差不仅是个人认知偏差，更是由社会技术系统结构性诱发的：对算法客观中立的社会预设、组织要求偏离系统建议时承担极高举证成本的制度惯性，以及长期依赖导致的人类专业[[Cognitive Deskilling|去技能化]]（Deskilling），共同削弱了操作者将自身视为合法决策权威的自我评价态度，使自主能动性在制度层面受到削弱。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 11–17)]]

---

### 命题三　强自动化偏差将人在回路退化为形式化橡皮图章，违背高风险情境下的道德能动性义务

> [!concept-lens] 尊严关切与有意义人类控制的捍卫
> 论证在高风险甚至关乎生死存亡的决策情境中，放弃人类独立道德判断构成了根本性的伦理失职。

> [!claim] [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]]
> **道德判断的不可让渡性与控制架空** 基于人类尊严的伦理立场，关乎人的生命安全与重大利益的决策必须包含对生命内在价值的道德审思与敬畏，而自动化与人工智能系统天然缺乏这种道德关切与理解能力。在自主武器系统、重症医疗诊断或司法风控中保留[[Meaningful Human Control|人在回路]]（Human-in-the-Loop, HITL），核心目的在于注入真实的人类道德能动性（Moral Agency）与[[Meaningful Human Control|有意义的人类控制]]；强自动化偏差使人类操作者退化为被动的橡皮图章（Rubber Stamp），实质上将杀伤或处置裁决权全盘让渡给无道德能力的机器，造成了对人类尊严与道德受托义务的严重背弃。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 17–20)]]

---

### 命题四　通过反思机器与击败者机制引入认识论摩擦是校准批判性信任的核心路径

> [!concept-lens] 设计干预与人机交互重构
> 探讨如何利用交互机制打破自动化偏差，培育批判性信任。

> [!claim] Veluwenkamp & Buijsman (2025); [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]]
> **生产性[[Epistemic Friction|认知摩擦]]对盲从的解构** 克服强自动化偏差不能仅依赖道德说教或增加事后问责，而必须在人机交互节点主动注入[[Epistemic Friction|认识论摩擦]]。主要技术方案包括：
> 1. **反思机器（Reflection Machines, RMs）** 嵌入关键决策节点的对话式反思[[AI Agent in Education|智能体]]，通过[[Socrates|苏格拉底]]式追问与对抗性质询，促使操作者阐明决策理由并重构审思投入；
> 2. **[[Defeater|反驳型击败者]]（Rebutting Defeaters）** 在系统给出推荐的同时，自动凸显支持对立诊断或互斥解释的反常证据指标，直接赋予操作者质疑与抗辩算法的认知杠杆，从而维持操作者的认识权威与批判性信任（Critical Trust）。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 20–25)]]

---

### 命题总览

> [!contrast-table] 自动化偏差核心命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **认知机制分流命题** | 弱偏差源于认知吝啬与启发替代，强偏差源于过度信任与认识顺从 | 人机协同决策、航空驾驶、医疗辅助诊断 | Mosier et al. (1998); Skitka et al. (2000); [[Argument_Jovchevski_2026_PT\|Jovchevski et al. (2026)]] |
> | **自主侵蚀命题** | 强偏差通过抑制信念修正能力与剥落制度性权威双向削弱自主性 | 算法审计、高阶专业工作流、人工智能辅助办公 | [[Argument_Jovchevski_2026_PT\|Jovchevski et al. (2026)]]; Mackenzie (2008); Stoljar (2000) |
> | **道德失职命题** | 强偏差架空人在回路与有意义人类控制，违背人类尊严与道德审思义务 | 军事自主武器、临床急救、司法刑罚评估 | [[Argument_Jovchevski_2026_PT\|Jovchevski et al. (2026)]]; Sparrow (2016); Santoni de Sio & van den Hoven (2018) |
> | **摩擦干预命题** | 借助反思机器与反驳型击败者注入认知摩擦，重建批判性信任与可质询性 | 智能界面交互设计、人机团队安全架构 | Veluwenkamp & Buijsman (2025); [[Argument_Jovchevski_2026_PT\|Jovchevski et al. (2026)]] |

---

## 概念演变

> [!dev-timeline] 自动化偏差的概念演变脉络
> - **1992–1998 年 — 航空驾驶舱中的启发式偏误奠基** 凯瑟琳·莫西尔（Kathleen Mosier）等学者在飞行模拟实验中发现飞行员因盲从电子清单而关闭正常引擎，首次正式界定自动化偏差，并提出执行错误与遗漏错误的分类。
> - **2000 年 — 认知吝啬假说与问责机制检验** 琳达·斯基特卡（Linda Skitka）等进一步将自动化偏差解释为人类为最小化心智努力而采取的认知启发策略，并检验了社会问责对缓解偏差的有限效果。
> - **2004–2010 年 — [[Trust Calibration|过度信任]]与自满注意力的整合** 玛丽·卡明斯（Mary Cummings）分析爱国者导弹误击友机惨剧，揭示操作者在明知系统显示异常时依然盲从；拉贾·帕拉苏拉曼（Raja Parasuraman）等将信任校准、过度信任与注意力分配模型全面引入自动化偏差研究。
> - **2026 年 — 弱/强偏差哲学界定与伦理规范转向** [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]] 提出弱自动化偏差与强自动化偏差的严格二元区分，确立过度信任—[[Epistemic Deference|认识论顺从]]解释模型，系统论证其对自主能动性与道德代理义务的侵蚀，并提出基于[[Epistemic Friction|认识论摩擦]]（反思机器与[[Defeater|击败者]]）的交互设计干预体系。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 自信程度是否为诊断强自动化偏差与[[Trust Calibration|过度信任]]的[[Necessary and Sufficient Conditions|必要条件]]
> > 争论当操作者自身信心不足而顺从人工智能系统时，是否属于理性的信任分配而非认知偏差。
> >
> > - **怀疑论立场** 若操作者自身判断的置[[Reliability|信度]]极低（如 2/4），选择信任长期准确率更高的系统属于理性贝叶斯更新，不应被斥为非理性的强偏差。
> > - **规范哲学立场（[[Argument_Jovchevski_2026_PT|Jovchevski et al., 2026]]）** 自信水平只是影响信任倾向的因果因素，而非信任校准的构成性条件。如果操作者明知当前案例属于系统训练集的盲区或局限，依然因整体信任而顺从系统推翻自身依据充分的观察，该决策依然构成强自动化偏差。
>
> > [!axis] 可解释人工智能（Explainable [[Generative Artificial Intelligence|Artificial Intelligence]], XAI）究竟是缓解还是加剧自动化偏差
> > 争论为算法决策提供因果解释与置信度展示能否促进信任校准。
> >
> > - **透明度促进论** 详尽的特征归因与推理链条有助于操作者发现模型错误并主动介入。
> > - **解释性诱导论（Schemmer et al., 2022; Vered et al., 2023）** 表面看似严密的自然语言解释极易营造[[Façade of Rationality|理性表象]]，反而诱导人类产生更深层的[[Illusion of Competence|能力错觉]]与过度信任，加剧执行错误。

> [!warning] 适用与干预局限
> 引入反思机器与[[Defeater|击败者机制]]虽能制造[[Epistemic Friction|认知摩擦]]，但在时间极度紧迫的高压操作情境（如战机空战或急性心梗抢救）中，过多的质询可能诱发严重的认知过载或致灾性决策延误；且强制性的反思交互在长期运行中存在退化为形式化例行公事（Routinization）的风险。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 22–24)]]

---

## 实证数据

> [!ref-table]- 自动化偏差相关实证基准与实验数据
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无[[Effect Size\|效应量]]） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | [[Argument_Jovchevski_2026_PT\|Klingbeil et al. (2024; cited in Jovchevski et al., 2026)]] | 陌生匹配博弈实验 | 六轮修改版信任博弈，第四轮引入人工智能或专家建议 | 参与者独立判断为极可能退出（OUT）情境下的合作（IN）顺从率 | 控制组合作率为 6%；在收到鼓励合作的建议时，标记为专家建议组无显著变化，而标记为人工智能建议组合作率上升至 44% | $p < .01$ | 证实仅将建议贴上人工智能标签即可显著诱发强自动化偏差，推翻参与者基于历史上下文的独立判断 |
> | [[Argument_Jovchevski_2026_PT\|Dijkstra et al. (1998; cited in Jovchevski et al., 2026)]] | 84 名大学生法律咨询任务 | 2（专家系统 vs 人类顾问）被试间实验设计 | 对完全相同推理逻辑建议的客观性与理性程度评定 | 呈现完全相同推理内容时，被试评定归属于专家系统的建议显著比归属于人类专家的建议更具客观性与理性 | $p < .05$ | 证实社会对机器客观中立的刻板印象为技术系统赋予了不对称的先验认识权威 |
> | [[Argument_Jovchevski_2026_PT\|Rosbach et al. (2025; cited in Jovchevski et al., 2026)]] | 28 名计算病理学医生 | 人工智能辅助肿瘤细胞占比（Tumor-Cell Percentages, TCP）估算，设时间压力条件 | 冲突咨询中专家顺从错误系统建议（改对为错）的案例频数 | 在 560 次评估中发生 67 次冲突决策；其中 38 次为专家原本正确但改从错误系统提示 | 原文报告频数 | 证实高阶专业人士在面对显微切片明确证据时依然会发生强自动化偏差 |
> | [[Argument_Jovchevski_2026_PT\|Mosier et al. (1998; cited in Jovchevski et al., 2026)]] | 航线执飞飞行员模拟舱测试 | 高保真飞行模拟实验 | 出现虚假仪表指示时关闭健康引擎的执行错误率 | 即使仪表盘其他多处物理参数均显示正常，绝大多数飞行员依然顺从计算机虚假指示执行了关车动作 | $p < .001$ | 奠定高技术驾驶舱中警觉性替代与执行错误的基础实证证据 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]] — 系统构建弱/强自动化偏差理论模型，论证强自动化偏差作为[[Epistemic Deference|认识论顺从]]对自主能动性与道德责任的伦理侵蚀，并提出反思机器与[[Defeater|击败者设计]]框架。
> - [[Argument_Jansen_2026_EPR|Jansen et al. (2026)]] — 在教育证据综合中探讨自动化偏差风险，提出通过多模型背对背提取与专家仲裁落实[[Meaningful Human Control|有意义的人类控制]]。
> - [[Argument_Li_2026_CEAI|Li et al. (2026)]] — [[Systematic Review|系统综述]]高等教育[[Generative Artificial Intelligence|生成式人工智能]]交互中的心智惰性，强调通过结构化支架注入[[Epistemic Friction|认识论摩擦]]以避免学生被动盲从。
> - [[Argument_Du_Yuan_2026_AIS|Du & Yuan (2026)]] — 诊断大语言模型（Large Language Models, LLMs）无摩擦委派对中间认识动作与[[Evaluative Judgement|评价性判断]]的剥离危害。

---

## 条目关联

> [!entry-map] 相关概念与理论关系总览
> | 概念/理论 | 维度/关系类型 | 核心关联说明 |
> |---|---|---|
> | [[Epistemic Deference]] | 核心机制 | 强自动化偏差在[[Epistemology\|认识论]]上的本质体现为人类操作者对算法系统的不当认知顺从。 |
> | [[Epistemic Friction]] | 应对机制 | 克服自动化偏差的核心设计原则是在人机交互回路中按需引入生产性认知阻力。 |
> | [[Meaningful Human Control]] | 伦理目标 | 自动化偏差直接架空实质性监督，使有意义人类控制退化为形式化橡皮图章。 |
> | [[Generative Artificial Intelligence]] | 诱发环境 | 生成式 AI 高度流畅的语言表达与权威语调极易诱发强自动化偏差。 |
> | [[Metacognition]] | 认知机理 | 自动化偏差本质上是外在技术线索抑制了人类内部的元认知监控与慢思考反思。 |
