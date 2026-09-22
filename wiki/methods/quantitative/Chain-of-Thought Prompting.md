---
title: Chain-of-Thought Prompting
aliases:
  - 思维链提示
  - 思维链
  - CoT
  - Chain of Thought
  - Chain-of-Thought
summary: "通过引导大语言模型显式生成逐步推理路径以解决复杂多步认知任务的提示工程方法，在人机协同学习中充当降低理解门槛与提升推论可解释性的认知脚手架"
type: method
method_type: quantitative
method_family: "quantitative"
method_related_count: 25
method_related_level: 3
method_related_stars: "⭐⭐⭐"
method_related_color: "#dcfce7"
tags:
  - method/prompt-engineering
  - theme/ai-in-education
  - method/computational
related_concepts:
  - "[[Scaffolding]]"
  - "[[Hypothesis]]"
  - "[[Unit of Analysis]]"
  - "[[Generative Artificial Intelligence]]"
  - "[[Epistemology]]"
  - "[[Higher-Order Thinking Skills]]"
  - "[[Dialogue in Education]]"
  - "[[Paradigm]]"
  - "[[Document]]"
  - "[[Externalization]]"
  - "[[Problem Solving]]"
  - "[[Variable]]"
  - "[[Metacognition]]"
  - "[[Cognitive Offloading]]"
  - "[[Epistemic Stances]]"
  - "[[Critical Thinking]]"
related_theories: []
related_methods:
  - "[[Role-playing]]"
  - "[[Analysis of Variance]]"
  - "[[Effect Size]]"
  - "[[Correlational Research]]"
  - "[[Systematic Review]]"
related_instruments: []
related_persons:
  - "[[Socrates]]"
related_facts: []
related_arguments:
  - "[[Argument_Wu_2025_ER]]"
  - "[[Argument_Zhao_2025_JIntell]]"
  - "[[Argument_Li_2026_CEAI]]"
confidence: high
status: active
created: 2026-09-22
updated: 2026-09-22
---

# Chain-of-Thought Prompting

---

## 定义

> [!def] 方法定义
> 思维链提示（Chain-of-Thought Prompting, CoT）是一种通过在提示词（Prompts）中显式引入分步骤中间推理轨迹（Step-by-Step Reasoning Trajectories），引导大语言模型（Large Language Models, LLMs）将复杂、多步骤的认知推理任务分解为连贯推理序列的提示工程方法。在教育与人机协同学习视域下，CoT 不仅是提升算法在数学、统计学与逻辑推理准确率的技术工具，更是将模型黑盒式的直接答案输出转化为外显化、可观察、可模仿的认识[[Scaffolding\|脚手架]]（Cognitive Scaffolding）。[[Argument_Wu_2025_ER\|(Wu et al., 2025, p. 366)]]; [[Argument_Zhao_2025_JIntell\|(Zhao et al., 2025, pp. 2–4)]]

> [!method-scope] 方法范围
> - **研究对象** 大语言模型的人机交互提示语、复杂推理任务（如统计推论、算法设计、数理证明、逻辑论辩）及学习者的思维链外显记录。
> - **问题类型** 多步计算、符号推演、[[Hypothesis\|假设]]检验推导、因果链条重构、概念辨析与逻辑查错。
> - **[[Unit of Analysis\|分析单位]]** 交互轮次（Dialogue Turns）、中间推理节点（Reasoning Steps）、提示语模板与生成文本逻辑流。
> - **输出形式** 分步推理链条、中间参数推导轨迹、纠错反思文本与最终问题解答。

> [!citation-card] 人机共生中的思维链技术干预功能
> 在人机协同学习的双轨干预矩阵中，思维链策略通过指令大模型分步骤展示其推理过程，不仅能够显著减少算法偏差与事实幻觉，更为先验知识匮乏的学习者提供了清晰的思维脚手架，提升了人机交互的透明度与可解释性。[[Argument_Wu_2025_ER\|(Wu et al., 2025, p. 366)]]
>
> *Using the chain of thoughts strategy by asking the [[Generative Artificial Intelligence\|GenAI]] to reflect on its generation of output step by step, learners can enhance the GenAI's performance by generating more unbiased and accurate output... making complex concepts easier to grasp.*

---

## 方法定位

> [!method-position] [[Epistemology\|认识论]]与方法定位
> - **知识观** 认为复杂知识的理解与构建本质上是离散逻辑命题的有序链条推进；通过将内隐心智操作显性化为外在语言符号序列，知识的有效性得以接受公开检验与评价。
> - **研究者角色** 在教学设计中，教师与研究者承担“[[Scaffolding\|认知脚手架]]架构师”角色，设计结构化思维链提示规则，引导学生从被动索要答案转向审查模型的中间推导环节。
> - **有效性标准** 逻辑推导的连贯性（Coherence）、中间推论的保真度（Step-level Faithfulness）、终结性答案准确度及对学习者[[Higher-Order Thinking Skills\|高阶思维]]的启发度。
> - **不声称回答的问题** CoT 本身不能保证每一步前提的绝对真实性（当基底模型存在事实幻觉时，可能生成“看似条理分明却从错误前提推导”的伪逻辑），因此必须与检索增强生成（RAG）和人类多源溯源核验相结合。

> [!method-stack] 方法层级
> - **研究设计** 人工智能教育应用（AIEd）、人机协同学习实验、提示工程对比研究。
> - **数据收集** 人机多轮[[Dialogue in Education\|对话]]日志、思维链提示模板、分步推理评分量规。
> - **分析方法**
>   - 零样本思维链（Zero-Shot CoT，如提示语 `"Let's think step by step"`）
>   - 少样本思维链（Few-Shot CoT，在提示中提供 2–3 个带分步推理的标准范例）
>   - 教学交互思维链（Pedagogical CoT，要求模型以[[Socrates\|苏格拉底]]追问方式引导学生补全推理链）
> - **辅助技术** 检索增强生成（RAG）、[[Role-playing\|角色扮演提示]]（Role-Playing Prompts）、自洽性采样（Self-Consistency Sampling）。

---

## 研究程序

> [!proc] 通用操作程序
> 1. **任务分解与问题表征** 明确复杂学科任务的核心目标，识别出解决该任务所必需的逻辑子步骤（如在统计[[Hypothesis\|假设]]检验中分解为：假设陈述 $\to$ 尺度诊断 $\to$ 公式选择 $\to$ 自由度与统计量计算 $\to$ 结论裁决）。
> 2. **提示词模板构建** 选择适宜的 CoT [[Paradigm\|范式]]（零样本或少样本），在提示语中显式嵌入分步要求指令（如：“请按步骤推导[[Analysis of Variance\|方差分析]][[Effect Size\|效应量]] $\omega^2$ 的公式等价性，并明确每个参数在平衡设计下的含义”）。
> 3. **人机多轮质询与中间链条审查** 学习者逐一审查大模型输出的各推导步骤，针对模糊或存疑环节发起定向追问。
> 4. **结合外部证据溯源核验** 将思维链中的推导前提与教材、期刊[[Document\|文献]]或原始数据实施交叉比对，排查逻辑跳跃或虚假假设。
> 5. **整合反思与知识内化** 总结解题图式，将[[Externalization\|外化]]的机器思维链转化为个体内在的高阶[[Problem Solving\|问题解决]]策略。

> [!formula-step] 公式步骤　思维链概率生成与分步条件依赖模型
> $$P(Y, R \mid X) = \prod_{t=1}^{|R|} P(r_t \mid X, r_{<t}) \times \prod_{k=1}^{|Y|} P(y_k \mid X, R, y_{<k})$$
>
> **这个公式在做什么** 表达大语言模型在给定输入问题 $X$ 的条件下，先联合生成由若干推理步骤构成的思维链序列 $R = (r_1, r_2, \dots, r_m)$，再基于问题与完整推理链生成最终答案 $Y$ 的概率分解。
>
> **符号说明**
> - $X$：输入的任务指令或学术问题。
> - $R = (r_1, \dots, r_m)$：中间逐步推理步骤（Reasoning Path）。
> - $Y$：最终输出的结论或解题结果。
>
> **数学直觉** 传统直接生成模式直接建模 $P(Y \mid X)$，要求大模型在极短的上下文距离内一步跨越复杂推理，极易产生逻辑断裂；CoT 通过引入显式的潜[[Variable\|变量]]路径 $R$，将复杂的非线性语义映射拆解为多个局部高概率的平滑条件转移步骤，大幅降低了每一步的搜索复杂度。
>
> **结果怎么读** 中间链条 $R$ 的生成质量直接决定了终结性答案 $Y$ 的稳健性；中间步骤越细致透明，人类学习者实施[[Metacognition\|元认知监控]]与定位错误的难度越低。

---

## 方法变体与提示范式辨析

> [!tension-table] 思维链提示及相近技术提示策略对比
> | 提示[[Paradigm\|范式]] | 输入构造特征 | 认知负荷要求 | 典型适用情境 | 优势与局限 |
> |---|---|---|---|---|
> | **零样本思维链（Zero-Shot CoT）** | 在指令后附加启发词（如 `"Let's think step by step"`） | 极低（无需准备范例） | 初步探究、开放性概念推演 | 简便高效，但复杂统计计算中稳定性弱于少样本 |
> | **少样本思维链（Few-Shot CoT）** | 在 Prompt 中提供 2–3 个包含输入、分步推理与答案的高质量示范 | 中等（需人工设计范例） | 格式化数理证明、公式推导与代码编写 | 准确率极高，但受提示词上下文窗口与示范偏差限制 |
> | **[[Role-playing\|角色扮演]]思维链（Role-Playing CoT）** | 设定大模型特定身份（如“统计学导师”）并要求按步引导 | 低至中等 | 先验知识薄弱学生的渐进式辅导 | 语言风格亲和、降低焦虑，但需防范角色泛化偏差 |
> | **检索增强思维链（RAG-CoT）** | 将分步推理与外部知识库动态检索深度绑定 | 高（需外挂数据库支持） | 高利害学术核验、防算法幻觉 | 事实准确度最高，能有效阻断伪逻辑链条 |

---

## 适用场景与局限性

> [!method-fit] 适用判断
> - **适合使用**
>   - 包含多层逻辑推理、参数转换与跨概念整合的复杂学术问题（如[[Analysis of Variance\|单因素方差分析]][[Effect Size\|效应量]] $\omega^2$ 推导、列联表卡方统计量计算）。[[Argument_Wu_2025_ER\|(Wu et al., 2025, p. 366)]]
>   - 面向先验知识薄弱学生的阶梯式概念教学与启发式解题训练。
>   - 计算机编程中的算法逻辑设计、代码审查与排错反思。
> - **谨慎使用**
>   - 纯粹的事实性检索（使用 CoT 会增加不必要的计算开销与冗长文本）。
>   - 学习者完全缺乏学科基础时：模型可能生成表面看似严密但关键前提错误的伪思维链，诱发学习者的“逻辑流畅性错觉”。

> [!method-limits] 方法局限
> - **虚假推理链（Faithfulness Issue）** 大模型生成的思维链有时属于后验合理化（Post-hoc Rationalization），即模型可能内部已按错误路径生成结论，但为迎合指令编造出看似合理的中间步骤。
> - **[[Cognitive Offloading\|认知外包]]与思维惰性风险** 若学生仅将思维链作为阅读材料而非主动批判的对象，仍可能引发认知卸载，无法真正内化[[Higher-Order Thinking Skills\|高阶思维]]能力。

---

## 使用此方法的研究

> [!evidence-grid-a] [[Correlational Research\|相关研究]]索引
> - [[Argument_Wu_2025_ER\|Wu et al. (2025)]] — 将思维链提示与[[Role-playing\|角色扮演]]、检索增强生成共同确立为促进自适应[[Epistemic Stances\|认识立场]]演进的技术干预支架，阐述其对低先验知识者推导统计原理的[[Scaffolding\|脚手架]]功能。（p. 366）
> - [[Argument_Li_2026_CEAI\|Li et al. (2026)]] — [[Systematic Review\|系统综述]]生成式 AI 在高等教育中的应用，指出结构化分步追问是防范认知侵蚀与维持[[Critical Thinking\|批判性思维]]的关键教学干预规制。（pp. 10–12）
