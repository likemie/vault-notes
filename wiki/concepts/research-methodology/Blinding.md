---
title: Blinding
aliases:
  - 盲法
  - 盲态
  - single-blind
  - double-blind
  - masked design
summary: "实验研究中使实验者或受试者不知道受试者所属研究条件的技术，用于降低实验者偏差和需求特征等系统性偏差"
type: concept
domain: "research-methodology"
related_count: 8
related_level: 0
related_stars: "☆"
related_color: "#e5e7eb"
tags:
  - method/experimental
  - quantitative-research
  - bias-control
related_concepts:
  - "[[Internal Validity]]"
  - "[[Hawthorne Effect]]"
  - "[[Experimenter Bias]]"
  - "[[Informed Consent]]"
related_methods:
  - "[[Experimental Research]]"
  - "[[Random Assignment]]"
related_arguments:
  - "[[Argument_Creswell_2022_SAGE]]"
  - "[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16]]"
status: draft
created: 2026-05-31
updated: 2026-07-13
---
# Blinding

## 定义

> [!def] 核心定义
> 盲法（Blinding）是[[Experimental Research|实验研究]]中用于降低系统性偏差的技术——在完成所有结果测量评估之前，使实验者和／或受试者不知道受试者所属的研究条件。盲法的核心目的是防止知晓条件分配后产生的期望或行为偏差影响实验结果（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。

> [!concept-lens] 盲法在偏差控制中的位置
> - **含义** 盲法通过切断"谁在哪一组"这一信息的传播路径来消除偏差源。它控制的是**知晓条件分配后的人为反应**——而非干预本身的效应、也非[[Random Assignment|随机化]]控制的组间初始差异。
> - **用途** 盲法保护的是[[Internal Validity|内部效度]]——确保观察到的组间差异来自干预而非来自研究者或参与者的期望。在医学实验中，盲法与安慰剂共同构成了偏差控制的双重防线。
> - **边界** 盲法不等于[[Random Assignment|随机分配]]——随机化控制组间初始差异，盲法控制实验过程中的期望偏差。盲法也不等于安慰剂——安慰剂是让参与者相信自己在接受处理，盲法是让参与者不知道自己接受的是什么。

> [!quote]
> "Blinding in experimental research is when the experimenter (and/or the participant) is kept unaware of the participant's assigned study condition."（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）

---

## 概念辨析

> [!contrast-table] 单盲 vs 双盲 vs 无盲法
> | 类型 | 参与者知情 | 研究者知情 | 控制哪些偏差 | 教育研究中的可行性 |
> |---|---|---|---|---|
> | **单盲（Single-Blind）** | 否——不知道自己在哪一组 | 是——知道每个参与者的组别 | 参与者预期效应、[[Hawthorne Effect\|霍桑效应]] | 较高——无需对教师隐瞒教学方法 |
> | **双盲（Double-Blind）** | 否 | 否——由第三方持有组别信息 | 参与者预期效应 + [[Experimenter Bias\|实验者偏差]] | 较低——教师通常知道自己使用的教学方法 |
> | **无盲法（Open-Label）** | 是 | 是 | 无 | 最高——但偏差风险最大 |

教育研究中单盲比双盲更容易实施。在比较计算机辅助教学与传统面授时，教师和学生不可能不知道该组使用的是哪种教学方式——此时双盲在操作上不可行。替代策略包括使用客观的结果测量（如标准化测试而非教师主观评分）来降低偏差风险（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。

---

## 核心要素

> [!feature] 盲法的四个运作条件
> - **知情路径的切断** 盲法控制的是"知道条件分配后产生的人为反应"——如果施测结果测量的实验者知道某受试者在"有益"处理组，可能以更积极、更具暗示性或更鼓励的方式施测，从而人为放大处理效应（[[Argument_Creswell_2022_SAGE|Creswell & Creswell, 2022, Ch8]]）。
> - **第三方信息持有** 在双盲实验中，组别信息由独立第三方持有，直到所有结果测量完成——研究者和参与者都不知情。
> - **盲法不可行时的替代** 当完全盲法在操作上无法实现时，应在方法部分诚实说明并将其作为研究局限。替代策略包括使用客观结果测量降低偏差风险。
> - **教育研究中的特殊策略** 可以不让参与者知道自己在实验中，或告诉他们实验是关于 X 而实际是关于 Y——即**误导参与者（put them off the scent）**。这种欺骗的正当理由是使实验在更自然的条件下进行（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 315]]）。

---

## 围绕概念形成的命题

### 知情本身就是偏差源

> [!claim] 研究者知情会通过施测行为传导偏差
> 若施测结果测量的实验者知道某受试者接受的是有益的处理条件，实验者可能以更积极、更有暗示性或更鼓励的方式施测结果测量，从而人为放大处理效应。盲法通过切断这一知情路径来消除偏差——即使研究者的期望是无意识的，它们仍然可以通过微妙的互动线索（语气、肢体语言、提问方式）影响参与者的表现。

### 教育研究中的盲法需要创造性策略

> [!claim] 当双盲不可行时，替代策略比放弃控制更有价值
> 在教育实验中，许多干预本质上无法对实施者隐瞒（如比较两种不同的教学方法），双盲在操作上不可行。但单盲仍然可以实施——至少让参与者不知道自己属于哪一组。更进一步的策略是"误导"：告诉所有参与者实验是关于 A，实际测量的是 B，使参与者的被研究意识指向错误方向，从而降低需求特征。这种做法需要满足伦理上的正当性论证（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, pp. 314–315]]）。

---

## 争议与批评

> [!warning] 盲法的操作边界
> - 在比较计算机辅助教学与传统面授等有明显物理差异的干预时，完全盲法在操作上难以实现——受试者和教师不可能不知道自己使用的是计算机还是面对面授课。
> - 当盲法不可行时，研究者应在方法部分诚实说明其局限，替代策略包括使用客观结果测量（如标准化测试）来降低偏差风险。
> - "误导"策略虽然有效，但引发伦理争议——故意欺骗参与者与[[Informed Consent|知情同意]]原则存在张力，需要满足严格的正当性条件。

---

## 应用案例

> [!case] 医学实验中的双盲与安慰剂
> 在药物实验中，参与者被[[Random Assignment|随机分配]]至实验组（接受新药）或控制组（接受外观相同的安慰剂）。不仅参与者不知道自己在哪一组（单盲），连施药和评估结果的医生也不知道（双盲）——组别信息由第三方持有。这种设计同时控制了：参与者的安慰剂效应（对"接受治疗"的信念）、参与者的[[Hawthorne Effect|霍桑效应]]（对"被研究"的反应）、以及医生的[[Experimenter Bias|实验者偏差]]（对"有益"处理组更积极的观察和记录）。

> [!case] 教育实验中的"误导"策略
> 在检验一种新的阅读教学方法时，如果直接告知学生"你们在参与实验"，学生可能因被选中而格外努力，混淆教学方法的真实效果。一种策略是告知所有学生这是常规课堂活动，实际测量的是阅读能力——但研究真正关注的是教学方法的效果。学生因被研究而产生的额外努力被引导到了错误的方向，不会系统地偏向某一组（[[Argument_Cohen_Manion_Morrison_2011_Routledge_Ch16|Cohen et al., 2011, Ch16, p. 315]]）。
