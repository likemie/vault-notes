---
title: Trim and Fill Method
aliases:
  - "剪补法"
  - "剪补估计法"
  - "Duval and Tweedie's Trim and Fill"
  - "Trim and Fill"
  - "剪补技术"
summary: "由 Sue Duval 与 Richard Tweedie（2000）开发的一种用于检测和校正元分析中因发表偏倚导致漏斗图不对称的非参数统计方法。通过迭代剪除极端小样本研究以估计对称中心，随后对称填补虚拟研究并重新估计真实效应量与置信区间。"
type: method
domain: "research-methodology"
method_type: quantitative
method_family: "quantitative"
method_related_count: 22
method_related_level: 2
method_related_stars: "⭐⭐"
method_related_color: "#dcfce7"
tags:
  - "method/quantitative"
  - "statistics/meta-analysis"
  - "statistics/publication-bias"
  - "field/research-methodology"
related_concepts:
  - "[[Publication Bias]]"
  - "[[Small Study Effects]]"
  - "[[Hypothesis]]"
  - "[[Funnel Plot]]"
  - "[[Effect Size]]"
  - "[[Confidence Interval]]"
  - "[[Standard Error]]"
  - "[[Epistemology]]"
  - "[[Sampling Error]]"
  - "[[Heterogeneity]]"
  - "[[Logic Model]]"
  - "[[Cooperative Learning]]"
  - "[[Problem-Based Learning]]"
  - "[[Document]]"
related_theories: []
related_methods:
  - "[[Meta-analysis]]"
  - "[[Meta-meta-analysis]]"
  - "[[Fail-Safe N]]"
  - "[[Multilevel Egger's Test]]"
  - "[[Fixed-Effect and Random-Effects Models]]"
  - "[[Meta-regression]]"
related_instruments: []
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Gungor_2026_CP]]"
  - "[[Argument_Erdem_2026_SHE]]"
confidence: high
status: draft
created: 2026-08-24
updated: 2026-08-24
---

# Trim and Fill Method

---

## 定义

> [!def] 方法定义
> Trim and Fill Method（剪补法 / 剪除与填补法，由 Sue Duval 与 Richard Tweedie 于 2000 年提出）是一种用于诊断和校正[[Meta-analysis|元分析]]中[[Publication Bias|发表偏倚]]（及[[Small Study Effects|小研究效应]]）的经典非参数迭代统计方法。该方法[[Hypothesis|假设]]在无发表偏倚时，[[Funnel Plot|漏斗图]]中的研究[[Effect Size|效应量]]应围绕真实均值呈对称分布；当检出单侧漏斗图不对称时，该算法先迭代“剪除（Trim）”导致不对称的极端小样本研究以估计无偏的中心效应，随后在漏斗图对侧“填补（Fill）”相应数量的镜像虚拟研究，并重新拟合计算校正后的最终效应量与 95% [[Confidence Interval|置信区间]]。[[Argument_Gungor_2026_CP|(Güngör et al., 2026, pp. 6–8)]]

> [!method-scope] 方法范围
> - **研究对象** 元分析中各纳入研究的效应量及其抽样[[Standard Error|标准误]]散点分布（漏斗图空间结构）。
> - **问题类型** 检验是否存在因偏向显著阳性结果发表而缺失的阴性研究，并估计假设缺失研究被填补后的校正效应量。
> - **分析单位** 包含 $k$ 个效应量的元分析或[[Meta-meta-analysis|二阶元分析]]数据集。
> - **输出形式** 估计缺失研究的数量（$k_{\text{miss}}$）、对称填补后的漏斗图、偏倚校正后的合并效应量（Adjusted ES）及校正置信区间。

> [!citation-card]- 关键定义
> 剪补法通过基于秩次的非参数迭代算法，系统识别漏斗图中由于抑制非显著结果发表而缺失的假想研究，并在镜像位置重新补全这些研究，从而提供一种保守的敏感性校正基准（Duval & Tweedie, 2000; Borenstein et al., 2021）。[[Argument_Gungor_2026_CP|(Güngör et al., 2026, p. 8)]]
>
> *The trim and fill method is a nonparametric data-augmentation technique that estimates the number and effect sizes of missing studies from a meta-analysis, adjusting the overall effect size for publication bias (Duval & Tweedie, 2000).*

---

## 方法定位

> [!method-position] [[Epistemology|认识论]]与方法定位
> - **知识观** 认为[[Sampling Error|抽样误差]]在[[Funnel Plot|漏斗图]]中应当对称呈现，单侧截断是不完全发表机制的统计指纹。
> - **研究者角色** 运用非参数秩次检验与对称性拟合，对证据库进行压力测试与保守校正。
> - **有效性标准** 若算法估计缺失研究数 $k_{\text{miss}} = 0$ 且校正后[[Effect Size|效应量]]保持不变，表明原结论完全不受[[Publication Bias|发表偏倚]]影响。
> - **不声称回答的问题** 不能证明漏斗图不对称必然由发表偏倚引起（[[Heterogeneity|异质性]]、研究质量差异或真实[[Small Study Effects|小研究效应]]亦可导致不对称）。

> [!method-stack] 方法层级
> - **研究设计** [[Meta-analysis|元分析]]偏倚诊断与敏感性分析
> - **数据输入** 各独立研究效应量 $y_i$ 及其抽样方差 $v_i$
> - **分析方法** 非参数迭代算法（$L_0, R_0, Q_0$ 估计量）
> - **辅助技术** 漏斗图绘制、与 [[Fail-Safe N]] 及 [[Multilevel Egger's Test]] 交叉检验

---

## 研究程序与算法步骤

> [!proc] 剪补法的标准三阶段算法操作规程
> 1. **初始中心估计与排序** 计算当前所有研究的加权合并[[Effect Size|效应量]]，计算各研究相对于均值的残差并按绝对值排序。
> 2. **迭代剪除（Trim）** 运用 Duval & Tweedie 的非参数估计量（如 $L_0$ 或 $R_0$），迭代识别并暂时剔除对侧缺乏配对支持的极端不对称小样本研究，直到剩余研究呈现对称形态，由此锁定无偏的真实中心。
> 3. **对称填补与重新合成（Fill）** 将先前剪除的研究沿新确定的真实中心做镜像翻转，生成相应数量的虚拟镜像研究（Imputed Studies）补回数据集；运用固定效应或[[Fixed-Effect and Random-Effects Models|随机效应模型]]对“原始研究 + 虚拟研究”的全集重新进行加权合成，输出偏倚校正后的效应量。

> [!logic-map]- 剪补法迭代运算[[Logic Model|逻辑模型]]
> ```mermaid
> flowchart TD
>     A["原始漏斗图数据 (存在单侧不对称)"] --> B["阶段一：Trim 迭代剪除极端小样本研究"]
>     B --> C["锁定对称的无偏中心基准"]
>     C --> D["阶段二：Fill 在对侧对称填补虚拟镜像研究"]
>     D --> E["对完整数据集重新加权合成"]
>     E --> F["输出偏倚校正效应量及置信区间"]
> ```

---

## 经典应用案例

> [!example] [[Argument_Gungor_2026_CP|Güngör et al. (2026)]] [[Cooperative Learning|合作学习]][[Meta-meta-analysis|二阶元分析]]偏倚检验
> 在合作学习二阶[[Meta-analysis|元分析]]中，作者综合运用剪补法对 23 个[[Effect Size|效应量]]进行偏倚检验：
> - **剪补检验结果** 剪补算法估计缺失研究数为 **$k_{\text{miss}} = 0$**（未识别到任何需剪除或填补的不对称研究）；
> - **校正效应量对比** 填补前后二阶效应量点估计值与 95% [[Confidence Interval|置信区间]]完全一致（$ES = 0.71, 95\%\text{ CI} = [0.55, 0.87]$）；
> - **结论推导** 与经典[[Fail-Safe N|失安全系数]]（$N_{\text{fs}} = 4954$）及 Egger 线性回归（$t = 2.08, p = .05$）相互印证，确凿证实合作学习对学生学习产出的中等促进效应具有高度稳健性，不存在[[Publication Bias|发表偏倚]]威胁。[[Argument_Gungor_2026_CP|(Güngör et al., 2026, pp. 6–8)]]
> [!example] [[Argument_Erdem_2026_SHE|Erdem et al. (2026)]] 高等教育[[Problem-Based Learning|问题本位学习]]二阶元分析偏倚检验
> 在问题本位学习高等教育二阶[[Meta-analysis|元分析]]中，作者综合运用剪补法对 47 个[[Effect Size|效应量]]进行偏倚检验：
> - **剪补检验结果** 剪补算法估计需在均值左侧补入 **$k_{\text{miss}} = 6$** 个负或小效应研究；
> - **校正效应量对比** 观测效应量 $ES = 0.68$ 经剪补调整后降至 $ES = 0.60$（$95\%\text{ CI} = [0.49, 0.71]$），差异约 $\Delta ES = 0.08$；
> - **结论推导** 与Egger 回归（$t(45) = 5.53, p < .001$）相互印证，提示存在轻微[[Publication Bias|发表偏倚]]，但校正后 PBL 仍呈显著正效应。[[Argument_Erdem_2026_SHE|(Erdem et al., 2026, pp. 960–961)]]

---

## 优缺点与方法局限

> [!contrast-table] 剪补法的优势与局限对比
> | 优势 (Strengths) | 局限 (Limitations) |
> |---|---|
> | 能够直接给出**偏倚校正后的具体[[Effect Size|效应量]]与[[Confidence Interval|置信区间]]**，突破了失安全数只能检验[[Hypothesis|假设]]的缺陷 | 严重依赖“漏斗图不对称必然源于[[Publication Bias|发表偏倚]]”的前提假定 |
> | 非参数估计，无需对未发表研究的效应分布做过于严苛的参数先验设定 | 在研究间存在高度真实[[Heterogeneity|异质性]]时容易误判，导致过度填补并产生保守偏倚 |
> | 结果直观，可通过[[Funnel Plot|漏斗图]]可视化呈现填补后的完整证据图景 | 在多水平嵌套或[[Document|文献]]重叠复杂数据中需结合多水平[[Meta-regression|元回归]]谨慎解释 |

---

## 相关研究

> [!evidence-grid-a] 相关研究索引
> - [[Argument_Gungor_2026_CP|Güngör et al. (2026)]] — [[Meta-meta-analysis|二阶元分析]]，运用剪补法对跨学科 23 个一阶[[Meta-analysis|元分析]][[Effect Size|效应量]]进行[[Publication Bias|发表偏倚]]敏感性检验，确证 $k_{\text{miss}} = 0$ 且校正效应量保持 $ES = 0.71$ 稳健不变。
> - [[Argument_Erdem_2026_SHE|Erdem et al. (2026)]] — [[Meta-meta-analysis|二阶元分析]]，运用剪补法对高等教育[[Problem-Based Learning|问题本位学习]]的 47 个[[Effect Size|效应量]]进行[[Publication Bias|发表偏倚]]检验，估计缺失研究 $k_{\text{miss}} = 6$，校正后效应量由 $0.68$ 调整为 $0.60$，提示轻微偏倚。
