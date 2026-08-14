---
summary: "中学生至研究生（740名）的量化研究 + 因子混合模型 + 验证了将信念维度与发展阶段整合的认识论与本体论认知（EOC）模型，指出认识论认知具有领域特殊性且多维分布刻画优于独立维度。"
type: argument
authors:
  - "[[Greene, J. A.]]"
  - "[[Torney-Purta, J.]]"
  - "[[Azevedo, R.]]"
source_language: en
citation: "Greene, J. A., Torney-Purta, J., & Azevedo, R. (2010). Empirical Evidence Regarding Relations Among a Model of Epistemic and Ontological Cognition, Academic Performance, and Educational Level. Journal of Educational Psychology, 102(1), 234–255."
year: 2010
doi: "10.1037/a0017998"
citation_aliases:
  - "Greene et al., 2010"
  - "Greene et al. (2010)"
isbn: ""
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments: []
sources:
  - "[[sources/Greene_2010_JEP/Greene_2010_JEP|Greene_2010_JEP]]"
part_of: 
status: draft
created: 2026-08-15
updated: 2026-08-15
subtype: journal-article
publication_type: journal-article
title: "Argument_Greene_2010_JEP"
argument_key: "Argument_Greene_2010_JEP"
argument_display_title: "Empirical Evidence Regarding Relations Among a Model of Epistemic and Ontological Cognition, Academic Performance, and Educational Level"
argument_kind: "journal-article"
argument_related_count: 0
argument_related_level: 0
argument_related_stars: "☆"
argument_related_color: "#dbeafe"
journal: "Journal of Educational Psychology"
book_title: ""
publication_place: ""
publisher: ""
issuing_organization: ""
---
# Argument_Greene_2010_JEP

---

## 研究问题

> [!question]
> 以往研究主要分为发展阶段论（如 Kuhn 等）与多维信念系统论（如 Schommer），但两者整合不足，且量化测量工具的信效度往往不佳。本文试图回答：能否构建一个同时容纳多维度和发展阶段，且区分领域特殊性（数学与历史）的认识论与本体论认知（Epistemic and Ontological Cognition, EOC）模型？

> [!claim] 核心主张
> 作者提出了整合性的 EOC 模型，并通过因子混合模型（Factor mixture modeling）证明：将个体在多维度（简单与确定知识、权威辩护、个人辩护）上的信念组合成轮廓特征（profile），可以更好地识别其所处的发展阶段（现实主义者、教条主义者、怀疑论者、理性主义者）；此外，EOC 具有领域特殊性（历史领域的发展通常优于数学领域），并与受教育程度、学业成绩存在预测关系。

> [!concept-lens] 阅读透镜
> - **对象** 740 名中学生至研究生的认识论信念问卷数据。
> - **张力** 独立维度的信念测量 vs 基于轮廓的整合阶段模型；领域一般性 vs 领域特殊性。
> - **贡献** 提供了一种利用定量工具（EOCQ）结合因子混合模型来实证检验“多维阶段融合模型”的方法路径，并将“知识的本质”重新界定为“本体论认知”。

---

## 理论框架

> [!framework-table] 理论工具箱
> | 理论工具 | 解释功能 |
> |----------|----------|
> | **认识论与本体论认知（EOC）模型**<br>[[Epistemic and Ontological Cognition]] | 将知识的本质重新界定为本体论认知，将认知的本质（辩护）保留为认识论认知。该模型预设了四个发展阶段：现实主义、教条主义、怀疑论、理性主义。 |

> [!warrant]- 理论如何支撑论证
> 作者通过 EOC 模型提出假设，即个体的认知发展表现为在三大维度的强弱组合特征档案（profile）。通过因子混合模型，可以验证多维度的量化得分能否聚合成理论预设的这四个阶段，从而证实该模型的结构合理性。

---

## 研究方法

> [!method-panel] 研究设计
> | 模块 | 材料与处理方式 |
> |------|----------------|
> | **调查测量**<br>Quantitative Survey | 采用认识论与本体论认知问卷（[[Epistemic and Ontological Cognition Questionnaire\|EOCQ]]），测量简单与确定知识、权威辩护、个人辩护三大维度。 |
> | **分析策略**<br>[[Factor Mixture Modeling]] | 使用验证性因子分析（CFA）检验问卷结构的建构效度；使用因子混合模型（Factor mixture modeling）将参与者划分到不同的潜在类别中，并验证领域特殊性及协变量（教育水平、成绩）的作用。 |

> [!sample-panel]- 样本与材料快照
> | 样本层面 | 构成 |
> |----------|------|
> | **调查样本** | 740 名学生（127 名中学生、173 名高中生、305 名本科生、135 名研究生）。 |

---

## 论证结构

> [!logic-map]- 核心论证逻辑链
> ```mermaid
> flowchart LR
>     A["传统模型分离维度与阶段"] --> B["建立EOCD整合模型"]
>     B --> C["EOCQ问卷开发"]
>     C --> D["CFA验证测量模型"]
>     C --> E["因子混合模型聚类"]
>     D --> F["因子具备一定建构效度与领域特殊性"]
>     E --> G["多维信念聚合出预设的四类阶段特征"]
>     F & G --> H["证明量化模型可同时刻画多维与发展特征"]
> ```

---

### 第一步：验证测量模型与领域特殊性

> [!claim] 测量模型主张
> EOCQ 问卷分数在大部分因子上具有可接受的建构效度，且认识论与本体论认知具有领域特殊性。

> [!chain-link] 证据到判断
> 验证性因子分析（CFA）显示，区分数学与历史两个具体领域的测量模型在数据拟合度上显著优于领域一般性模型（将两学科题目归为同一因子）。多数维度的建构信度可接受。

> [!warrant]- 推理桥梁
> 领域特定模型拟合更优，反驳了领域一般性假设，说明学生对良构领域与劣构领域的认知本质持有不同的信念结构。

---

### 第二步：利用因子混合模型验证阶段融合

> [!claim] 混合模型主张
> 通过因子混合模型找出的潜在类别多数能匹配 EOC 模型预设的发展阶段，证明信念的定量维度可以整合为定性的发展阶段。

> [!chain-link] 证据到判断
> 六分类的因子混合模型拟合最佳。在得出的类别中，多数轮廓匹配了预设阶段。在各类别中，历史领域的信念发展水平都至少与数学域持平或更高。

> [!warrant]- 推理桥梁
> 多维信念在聚类后呈现出与阶段论相符的组合模式，证明将维度分数整合成潜在特征档案更能反映个人的真实发展位置。

---

### 第三步：探讨学术结果的预测效度

> [!claim] 预测效度主张
> 教育水平和学业成绩是 EOC 模型阶段的重要预测指标。

> [!chain-link] 证据到判断
> 多项逻辑回归表明，受教育年限越长，个体越有可能处于更高级的认识论阶段（如怀疑论或理性主义）；而数学或历史成绩较差的学生，更可能停留在现实主义阶段。

---

## 主要发现

> [!finding-cards] 核心发现
> 1. **发现一** 学生的认识论与本体论信念具有显著的领域特殊性，通常在劣构领域（历史）的认知发展早于良构领域（数学）。（p. 242）
> 2. **发现二** 定量的多维信念评分可通过因子混合模型有效聚类为定性的发展阶段类别，较好地吻合了现实主义者、怀疑论者和理性主义者等阶段预设。（p. 245）
> 3. **发现三** 维度的特征档案（profiles）能更有效地反映个人认识论水平，且与受教育年限和学业成绩存在明确的预测关系。（p. 246）

> [!stat-cards]- 核心数据
> - **740** 参与问卷调查的总样本数。（p. 240）
> - **6分类** 选定为最佳拟合的因子混合模型类别数。（p. 243）

> [!example]- 图1：Range of differences regarding the domain generality or specificity of epistemic cognition.
> ![](https://img.mylikemie.icu/sources/Greene_2010_JEP/figures/Greene_2010_JEP_Fig1_Range_of_differences_regarding_domain_generality.jpg)

> [!example]- 图2：Hypothesized domain-specific measurement model.
> ![](https://img.mylikemie.icu/sources/Greene_2010_JEP/figures/Greene_2010_JEP_Fig2_Hypothesized_domain-specific_measurement_model.jpg)

> [!example]- 图3：Factor mixture model.
> ![](https://img.mylikemie.icu/sources/Greene_2010_JEP/figures/Greene_2010_JEP_Fig3_Factor_mixture_model.jpg)

> [!example]- 图4：Latent class factor means.
> ![](https://img.mylikemie.icu/sources/Greene_2010_JEP/figures/Greene_2010_JEP_Fig4_Latent_class_factor_means.jpg)

---

## 关键引用

> [!citation-card]- EOC 模型构建理由
> Hofer (2001) suggested that personal epistemology research may be moving toward “an integration of ideas from multiple models: an identifiable set of dimensions of beliefs, organized as theories, progressing in reasonably predictable directions, activated in context, operating as epistemic cognition” (p. 377).（p. 234）
>
> *Hofer (2001) suggested that personal epistemology research may be moving toward “an integration of ideas from multiple models: an identifiable set of dimensions of beliefs, organized as theories, progressing in reasonably predictable directions, activated in context, operating as epistemic cognition” (p. 377).*

---

## 自述局限

> [!warning]
> 作者自述：因子混合模型需要大样本量，740 人的样本仍然偏小；“简单与确定知识”个别题目表现不佳；横截面数据限制了因果或纵向发展推论。（p. 247）

---

## 来源

- [[sources/Greene_2010_JEP/Greene_2010_JEP|Greene_2010_JEP]]
