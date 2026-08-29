---
title: GROOVE
aliases:
  - 系统评价重叠图形表征工具
  - Graphical Representation of Overlap for OVErviews
  - GROOVE Tool
  - 重叠图形表征工具
summary: "用于伞状综述与二阶元分析中量化、探索与可视化初级研究重叠的图形表征工具，基于校正覆盖面积（CCA）矩阵生成结构化热力图与成对重叠诊断"
type: instrument
instrument_type: rubric
part_of: ""
developers:
  - "Bracchiglione, J."
  - "Meza, N."
  - "Revuelta-Zamorano, M."
  - "Solis-García, G."
  - "Garrido, D."
  - "Bravo-Soto, I."
  - "Pantoja, T."
  - "Madrid, E."
original_year: "2022"
languages:
  - en
item_count: ""
administration_mode: observer-rating
response_format: quantitative-matrix
tags:
  - instrument/rubric
  - method/meta-meta-analysis
  - methodology/systematic-review
  - overlap-analysis
related_concepts:
  - "[[Standard Error]]"
  - "[[Primary and Secondary Documents]]"
  - "[[Corrected Covered Area]]"
  - "[[Document]]"
  - "[[Chain of Evidence]]"
  - "[[Effect Size]]"
  - "[[Internal Validity]]"
related_theories: []
related_methods:
  - "[[Umbrella Review]]"
  - "[[Meta-meta-analysis]]"
  - "[[Meta-analysis]]"
  - "[[Coding in Qualitative Research]]"
related_instruments:
  - "[[AMSTAR]]"
related_persons: []
related_facts: []
related_arguments:
  - "[[Argument_Unal_2026_JECR]]"
confidence: high
status: draft
created: 2026-08-25
updated: 2026-08-25
---

# GROOVE

---

## 工具定位

> [!instrument-profile] GROOVE
> - **工具类型** [[Umbrella Review|伞状综述]]与[[Meta-meta-analysis|二阶元分析]]初级研究重叠定量审计与可视化分析工具（Overlap Quantification & Graphical Representation Tool）。
> - **开发者与年份** Bracchiglione et al. (2022)。
> - **测量目的** 用于在[[Umbrella Review|伞状综述]]（Overview of Reviews）与二阶[[Meta-analysis|元分析]]中，系统量化、探索并可视化不同系统评价与一阶[[Meta-analysis|元分析]]之间初级实证研究（Primary Studies）的重复包含程度，避免由于重复计数相同受试者而导致的[[Standard Error|标准误]]假性收缩与假阳性推断。
> - **实施方式** 基于 Excel 宏算法及结构化脚本，通过导入[[Primary and Secondary Documents|初级文献]]交叉引用矩阵自动计算节点重叠并生成分级色彩热力图。

---

## 核心构念与分析维度

> [!construct-table] [[Corrected Covered Area]]
> <span class="instrument-dimension-table-marker" aria-hidden="true"></span>
>
> | 分析维度 | 统计算法 / 呈现形式 | 测量与诊断功能 | 决策判定规则 |
> |---|---|---|---|
> | **总体校正覆盖面积（Overall CCA）** | $$CCA = \frac{N - r}{r(c - 1)}$$ | 衡量全数据集内所有纳入[[Meta-analysis|元分析]]作为一个整体时的总体重复包含水平。 | $< 5\%$ 轻微；$5\%–10\%$ 中等；$10\%–15\%$ 高度；$\ge 15\%$ 极高重叠（通常以 $10\%$ 为排除警戒线）。 |
> | **成对重叠矩阵（Pairwise CCA Matrix）** | 两两综述间独立的 $2 \times r_{ij}$ 交叉子矩阵计算 | 定位具体哪两项元分析之间存在高度重复，识别关键重叠源头。 | 若特定两项元分析间 $CCA > 10\%$，触发成对剔除或亚组敏感性合并。 |
> | **初级研究结构分布热力图（Heatmap Display）** | 红/橙/黄/绿四色[[Coding in Qualitative Research|编码]]的矩阵色块图 | 直观呈现各一阶元分析对初级研究的覆盖广度与聚集重叠区域。 | 绿色表示轻微重叠，黄色表示中等重叠，橙色与红色警示高度与极高重叠。 |
> | **[[Document|文献]]筛选与敏感性决策节点** | 逐步剔除模拟与重新计算模块 | 模拟剔除重叠元分析后全数据集 CCA 的变动轨迹，辅助制定排除策略。 | 优先剔除研究范围狭窄、发表年份陈旧或 [[AMSTAR]] 方法学质量评分较低的元分析。 |

---

## 操作规程与实施步骤

> [!proc] GROOVE 工具四步操作规程
> 1. **提取与清洗[[Primary and Secondary Documents|初级文献]]清单** 逐篇提取所有初筛纳入的一阶[[Meta-analysis|元分析]]所引用的全部初级研究参考[[Document|文献]]，标准化作者姓名与发表年份，消除格式异构。
> 2. **构建二元交叉引用矩阵（Citation Matrix）** 建立 $r$ 行（不重复初级研究）$\times$ $c$ 列（一阶元分析）的电子表格，填入 0 与 1（或打勾标记），统计总勾选数 $N$。
> 3. **运行 GROOVE 自动化宏程序** 启动 GROOVE 工具，自动计算整体 $[[Corrected Covered Area|CCA]]$ 与所有成对组合的 $CCA_{ij}$ 指数，并生成四色重叠热力图。
> 4. **执行重叠剔除与[[Chain of Evidence|证据链]]合规化** 对成对或总体 $CCA > 10\%$ 的高重叠元分析实施逐一剔除，直至剩余数据集满足抽样独立性标准（[[Argument_Unal_2026_JECR|Ünal et al., 2026]]）。

---

## 方法学贡献与应用典范

> [!warrant]- 方法学定位
> 在第一代粗放[[Meta-meta-analysis|元综合]]（如 Hattie, 2009）中，[[Document|文献]]重叠常被完全忽视，导致高达 80%–90% 的底层数据被重复加权。GROOVE 工具为第二代与第三代[[Umbrella Review|伞状综述]]提供了标准化、可复现的去重操作方案：
> - **透明度与可追溯性** 替代了传统综述凭借主观印象判定“文献相似”的模糊做法，输出标准矩阵；
> - **典型实证案例** [[Argument_Unal_2026_JECR|Ünal et al. (2026)]] 在对 35 项 AI 教育效果[[Meta-analysis|元分析]]实施二阶综合时，运用 GROOVE 工具计算各 FOM 之间的 [[Corrected Covered Area|CCA]] 矩阵，果断排除了 6 项 $CCA > 10\%$ 的重叠元分析，确保了最终 19 项元分析合成[[Effect Size|效应量]]（$ES = .67$）的高[[Internal Validity|内部效度]]与数学稳健性。
