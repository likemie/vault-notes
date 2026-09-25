---
title: Trust Calibration
aliases:
  - 信任校准
  - 人机信任校准
  - Calibrated Trust
  - 信任失调
  - Overtrust
  - 过度信任
summary: "人类操作者对自动化与智能系统赋予的主观信任水平与系统客观实际能力及情境边界相匹配的动态平衡状态，其失调（过度信任）是诱发认识论顺从与强自动化偏差的根本根源。"
type: concept
domain: "educational-technology"
related_count: 21
related_level: 2
related_stars: "⭐⭐"
related_color: "#99f6e4"
tags:
  - educational-technology
  - cognitive-science
  - human-ai-interaction
  - cognitive-bias
  - decision-making
related_concepts:
  - "[[Generative Artificial Intelligence]]"
  - "[[Construct]]"
  - "[[Automation Bias]]"
  - "[[Epistemology]]"
  - "[[Defeater]]"
  - "[[Reliability]]"
  - "[[Self-Efficacy]]"
  - "[[Reflexivity]]"
  - "[[AI Literacy]]"
  - "[[Epistemic Friction]]"
  - "[[Epistemic Deference]]"
  - "[[Scaffolding]]"
  - "[[Evaluative Judgement]]"
  - "[[Document]]"
  - "[[Variable]]"
related_theories: []
related_methods:
  - "[[Effect Size]]"
  - "[[Randomised Controlled Trials]]"
  - "[[Correlational Research]]"
related_instruments: []
related_persons:
  - "[[Socrates]]"
related_facts:
  - "[[Achieve]]"
related_arguments:
  - "[[Argument_Jovchevski_2026_PT]]"
confidence: high
status: active
created: 2026-09-22
updated: 2026-09-26
---

# Trust Calibration

---

## 定义

> [!def] 核心定义
> **人机信任校准（Trust Calibration，又称信任校准）** 指人类操作者或学习者对自动化与人工智能（[[Generative Artificial Intelligence|Artificial Intelligence]], AI）系统赋予的主观信任水平（Trust），与系统在特定任务情境中的客观真实能力（Capabilities）及有效边界相吻合的动态适应状态。在工效学、认知心理学与人机交互领域，信任校准是决定人机协同效能与安全性的核心[[Construct|构念]]；当信任水平超出系统实际能力时发生**过度信任（Overtrust）**，诱发盲目顺从与[[Automation Bias|强自动化偏差]]；当信任水平低于系统实际能力时发生**信任不足（Undertrust / Distrust）**，导致对正确建议的非理性拒绝与技术闲置。在哲学与社会[[Epistemology|认识论]]视角下，信任校准不仅是主观心理感受，更是关于信任分配是否具备客观充分理由的规范性确证机制。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 8–12)]]

> [!concept-lens] 概念透镜
> - **含义** 指人类主观信任与智能代理客观能力、训练集边界及情境极限之间的动态匹配度。
> - **用途** 帮助研究者与系统设计师识别盲目盲从与无端怀疑的失调临界点，指导交互界面构建自适应的认知防护与信任调节机制。
> - **边界** 信任校准不等于使用者的主观自信水平（Self-Confidence）；即便主体对自身能力信心不足，若其掌握了系统在当前情境不可靠的客观线索仍选择顺从，该行为在规范上依然构成失调的过度信任。

> [!citation-card] 信任校准的客观属性与自信解耦（[[Argument_Jovchevski_2026_PT|Jovchevski et al., 2026]]）
> 信任校准关注的是操作者所赋予的信任是否与其对系统当前情境极限的合理把握相吻合。即使一个操作者对自身的独立判断缺乏绝对信心（例如信贷员自评信心仅为中等），只要其明知当前案例属于系统训练集未覆盖的边缘群体，依然选择顺从算法推荐，这一决策在客观上依然构成失调的过度信任，因为操作者手中掌握了在当前具体案例中不应信任系统的充分反常理由。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 8–10)]]
>
> *Trust calibration is about whether the operator's level of trust corresponds to what they have reason to believe the system can reliably [[Achieve]] in this specific setting... even if self-confidence is low, deferring when one has [[Defeater|Defeaters]] still constitutes overtrust.*

> [!boundary]- 概念边界
> - 不等于 用户满意度（User Satisfaction）— 满意度是基于交互体验与输出流畅感的情感偏好；信任校准是对系统因果效能与[[Reliability|可靠性]]边界的理性认知匹配。
> - 不等于 系统可解释性（Explainability）— 可解释性是技术界面呈现特征；可解释性若只提供表面流畅的伪因果包装，反而可能诱发虚假的过度信任与校准恶化。
> - 不等于 主观自信（Self-Confidence）— 自信反映操作者对自身独立判断的[[Self-Efficacy|自我效能]]评估，而信任校准反映对系统能力合理边界的客观认知。

---

## 概念辨析

> [!contrast-table] 人机信任状态三元象限辨析
> | 比较维度 | 信任不足 / 怀疑（Undertrust / Distrust） | **校准信任（Calibrated Trust）** | 过度信任（Overtrust / Strong Bias） |
> |---|---|---|---|
> | **信任与能力关系** | 主观信任 **$<$** 系统实际客观能力 | 主观信任 **$=$** 系统实际客观能力 | 主观信任 **$>$** 系统实际客观能力 |
> | **典型决策行为** | 即使系统给出最优解仍固执拒绝，坚持低效手动操作 | 适度依赖系统优势，在系统盲区与反常情境主动接管介入 | 盲目顺从错误建议，放弃独立核验与[[Reflexivity\|反思性]]证据修正 |
> | **核心认知根源** | 算法厌恶（Algorithm Aversion）或早期偶发错误泛化 | 深刻理解系统训练集极限与边界条件，具备[[AI Literacy\|AI素养]] | 流畅权威性错觉、认知吝啬、算法客观性迷信 |
> | **治理干预方向** | 提升系统可解释性与展示历史基线成功率 | 维持动态反馈与常态化双向协同 | 引入[[Epistemic Friction\|认识论摩擦]]、反思机器与[[Defeater\|反驳型击败者]] |

---

## 核心要素

> [!feature] 人机信任校准的核心维度与机制
> - **能力与边界感知（Capability & Boundary Awareness）** 操作者对系统算法架构、训练语料分布及适用情境极限的清晰认知，是实现精准信任校准的认知基石。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 8–10)]]
> - **信任动态调节性（Dynamic Adjustability）** 信任不是静态常量，必须随任务复杂度、传感器数据噪声及现场反常信号的出现而实时动态升降。
> - **自信与校准解耦（Decoupling of Confidence & Calibration）** 信任校准取决于信任分配是否具备情境合理性，不能简单还原为操作者个人自信心高低的心理博弈。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 9–10)]]
> - **过度信任向[[Epistemic Deference\|认识论顺从]]的转化阈值（Overtrust to Deference Threshold）** 当过度信任越过临界点，操作者不仅在行为上顺从，更在[[Epistemology|认识论]]上将最终裁决权威让渡给机器，导致理性信念修正机能陷入瘫痪。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 10–12)]]
> - **批判性校准[[Scaffolding|脚手架]]（Calibration Scaffolding）** 利用反思机器（Reflection Machines）的[[Socrates|苏格拉底]]追问与[[Defeater|反驳型击败者]]（Rebutting Defeaters）的主动介入，为操作者提供重新校准信任的认知支架。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 20–24)]]

---

## 围绕概念形成的命题

---

### 命题一　过度信任是强自动化偏差的实质根源，其本质是向技术代理让渡合法认识权威

> [!concept-lens] 信任失调与权威让渡
> 探讨信任失调如何从一般的行为顺从演化为深层的哲学与[[Epistemology|认识论]]让渡。

> [!claim] Muir (1987); Lee & See (2004); [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]]
> **过度信任驱动的[[Epistemic Deference|认识论顺从]]** 传统工效学将[[Automation Bias|自动化偏差]]定性为有限注意力的认知节省策略；规范研究指出，当操作者在已接触到反常冲突证据的情境下依然顺从系统时（强自动化偏差），其根本驱动力是过度信任（Overtrust）。操作者单凭系统以往的高准确率或算法客观性光环，预先假定机器比自身拥有更高的认识特权，从而将最终[[Evaluative Judgement|评价性判断]]权威让渡给算法黑箱，发生了深层的[[Epistemic Deference|认识论顺从]]。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 10–12)]]

---

### 命题二　信任校准独立于操作者主观自信，其评价基准在于信任分配是否具备客观情境理由

> [!concept-lens] 规范理性与客观理由
> 澄清将信任校准还原为主观自信高低所带来的理论混淆。

> [!claim] [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]]
> **客观理由对主观自信的规范优先性** 针对“操作者自信心低因而顺从高准确率算法属于合理论据”的辩护，规范认识论论证了信任校准的客观规范属性。信任校准不是主体主观信心与算法标称准确率的简单机械相减，而是操作者是否依据现场反常证据做出了符合情境极限的合理判断。只要操作者掌握了当前案例超出模型训练边界的充分证据（[[Defeater|击败者]]），无论其自身信心高低，盲目顺从均构成失调的过度信任。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 8–10)]]

---

### 命题三　注入认识论摩擦与击败者机制是实现人机批判性信任动态校准的关键路径

> [!concept-lens] 交互干预与动态校准
> 探讨如何通过界面工程主动重构操作者的信任分配。

> [!claim] Hoff & Bashir (2015); [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]]
> **[[Epistemic Friction|认识论摩擦]]对信任失调的动态阻断** 静态警示与单向解释无法从根本上遏制过度信任；唯有在人机决策回路中注入生产性[[Epistemic Friction|认识论摩擦]]（如反思机器的[[Socrates|苏格拉底]]式追问与反驳型击败者的反例呈现），才能打破无反思的自动顺从惯性，促使操作者从被动接受转向主动审议，实现信任水平与系统客观能力的精准校准。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 20–25)]]

---

### 命题总览

> [!contrast-table] 所有命题归纳
> | 命题类型 | 核心指向 | 适用情境 | 代表学者 |
> |---|---|---|---|
> | **过度信任实质命题** | 过度信任驱动强自动化偏差并演化为深层认识论顺从 | 高风险人机协同、临床医疗AI诊断、智能风控审批 | Muir (1987); Lee & See (2004); [[Argument_Jovchevski_2026_PT\|Jovchevski et al. (2026)]] |
> | **客观理由解耦命题** | 信任校准独立于主观自信，取决于是否掌握情境反常理由 | 复杂专业决策、非标准数据场景、专家与AI冲突分析 | Jovchevski 等（2026） |
> | **认知摩擦校准命题** | 依托反思机器与击败者注入认知摩擦以实现动态信任校准 | 智能交互界面设计、人机回路安全规程、可抗辩AI系统 | Hoff & Bashir (2015); Jovchevski et al. |

---

## 概念演变

> [!dev-timeline] 信任校准概念的演变历程
> - **1980s–1990s — 工效学与自动化信任奠基** Bonnie Muir (1987) 首次将社会心理学信任理论引入人机系统，界定信任校准为操作者主观信任与机器客观[[Reliability|可靠性]]（Reliability）的吻合度。
> - **2004 — 动态信任框架与适当依赖模型** John D. Lee & Katrina A. See (2004) 在 *Human Factors* 发表里程碑综述，构建“信息—信念—信任—依赖”动态回路，系统辨析过度信任（Overtrust）与信任不足（Distrust）的促发机制。
> - **2015 — 信任影响因素的多层三元整合** Kevin Anthony Hoff & Masooda Bashir (2015) 整合实证[[Document|文献]]，提出倾向性信任（Dispositional）、情境性信任（Situational）与习得性信任（Learned）的三层分析模型。
> - **2026 — 社会[[Epistemology|认识论]]转向与客观理由确证** [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]] 将信任校准从心理测量与行为工效学拓展至规范认识论，论证过度信任向[[Epistemic Deference|认识论顺从]]转化的因果路径，确立自信解耦机制，并提出利用[[Defeater|击败者]]与反思机器校准批判性信任的交互架构。

---

## 争议与批评

> [!debates] 学术争议
>
> > [!axis] 信任最大化 vs 批判性信任校准
> > 商业算法开发常追求“提升用户信任与粘性”，而人机工效学与认知安全学界强调“盲目高信任极其危险，唯有与能力精准校准的批判性信任才具正当性”。
> >
> > - **商业推广取向** 倾向于通过拟人化语气和流畅文本消除一切使用摩擦以最大化采纳率。
> > - **认知安全取向** 强调必须保留适度怀疑与审查阻力，防止操作者陷入过度信任。[[Argument_Jovchevski_2026_PT|(Jovchevski et al., 2026, pp. 20–22)]]
>
> > [!axis] 可解释性是校准工具还是过度信任诱因
> > 探讨向用户呈现特征权重或生成式解释究竟能促进校准，还是会加剧盲目信任。
> >
> > - **解释促进校准论** 主张白箱透明度能帮助用户看清模型短板。
> > - **虚假安全感警示** 批判研究指出表面流畅的解释往往充当了欺骗性的“合理化修饰”，反而显著加剧了非专家的过度信任。

> [!warning] 适用局限
> 信任校准依赖于系统行为的可观察性与任务环境反馈的及时性；在高度动态、信息极度不完全且无法事后快速检验真伪的黑天鹅极端情境中，人类往往难以在短时间内完成有效的信任校准。

---

## 实证数据

> [!ref-table]- 信任失调与[[Automation Bias|自动化偏差]]实证结果
> <span class="concept-other-empirical-table-marker" aria-hidden="true"></span>
>
> | 研究 | 样本与情境 | 研究设计 | [[Variable\|变量]]或指标 | 原始统计结果（无[[Effect Size\|效应量]]） | 不确定性或显著性 | 解释边界 |
> |---|---|---|---|---|---|---|
> | Klingbeil et al. (2024) (引自 [[Argument_Jovchevski_2026_PT\|Jovchevski et al., 2026, p. 10]]) | 行为经济学匿名陌生人信任博弈实验 | [[Randomised Controlled Trials\|随机对照实验]]室实验 | AI 标签建议与操作者合作率（过度信任测量） | 控制组历史违约率高时合作率仅 6%；引入 AI 标签建议后合作率激增至 44%（专家标签无此显著上升） | $p < .05$ | 证实仅“AI 系统”标签本身即足以触发显著的先验过度信任与强顺从 |
> | Rosbach et al. (2025) (引自 [[Argument_Jovchevski_2026_PT\|Jovchevski et al., 2026, pp. 7–8]]) | 28 名病理学临床专家，肿瘤细胞占比（TCP）评估 | 临床辅助诊断时间压力实验 | 专家推翻正确独立判断顺从错误 AI 提示的比率 | 在 67 次人机冲突评估中，专家有 38 次放弃自身原本正确的判断，改为顺从错误 AI 提示 | 38 / 67 (56.7%) | 实证确证专业领域中过度信任导致的强自动化偏差能直接摧毁专家的独立判断力 |

---

## 相关研究

> [!evidence-grid-a] [[Correlational Research|相关研究]]索引
> - [[Argument_Jovchevski_2026_PT|Jovchevski et al. (2026)]] — 从规范[[Epistemology|认识论]]视角系统阐述信任校准与过度信任，澄清其与主观自信的本质区别，提出利用[[Defeater|反驳型击败者]]（Defeaters）与反思机器（Reflection Machines）校准批判性信任并防范[[Automation Bias|自动化偏差]]。
