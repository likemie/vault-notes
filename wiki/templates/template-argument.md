---
title: <% tp.file.title %>
summary: ""
type: argument
authors: []
citation: ""
year:
doi: ""
isbn: ""
citation_aliases: []
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
sources:
  - "[[Source_Name]]"
part_of:
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
subtype: journal-article
publication_type: journal-article
journal: ""
book_title: ""
issuing_organization: ""
---

# <% tp.file.title %>

---

## 研究问题

%% [!question] 标题栏由 CSS 自动显示"研究问题"，无需手动添加。 %%
> [!question]
> 直接陈述问题意识，说明要解释的教育现象、理论问题或政策问题；不要只复述标题。

> [!claim] 核心主张
> 用一两句话写出本文最重要的论证判断。说明作者最终要让读者接受什么，而不是复述研究主题。

> [!concept-lens] 阅读透镜
> - **对象** 研究对象、材料范围或经验场景。
> - **张力** 核心比较关系、理论冲突或证据缺口。
> - **贡献** 本文改变了什么理解、分类或解释路径。

---

## 理论框架

> [!framework-table] 理论工具箱
> | 理论工具 | 解释功能 |
> |----------|----------|
> | **<理论名>**<br>[[<理论名>]] | 简短定义或核心命题。说明它如何帮助解释问题、组织证据或推出判断。 |
> | **<理论名>**<br>[[<理论名>]] | 简短定义或核心命题。说明它如何帮助解释问题、组织证据或推出判断。 |

> [!warrant]- 理论如何支撑论证
> 说明理论工具如何把研究问题、材料证据和核心主张连接起来。不要只列理论名，要写出推理桥梁。

---

## 研究方法

> [!method-panel] 研究设计
> | 模块 | 材料与处理方式 |
> |------|----------------|
> | **材料分析／具体方法**<br><English Method Name> | 描述材料类型、处理方式、检索词、编码或分析路径。样本构成另放到下方样本面板。 |
> | **访谈／具体方法**<br><English Method Name> | 描述访谈形式、执行时间、问题范围、抽样逻辑。人数和身份构成另放到下方样本面板。 |
> | **分析策略／具体方法**<br><English Method Name> | 描述编码、比较、模型、解释路径或验证方式。 |

> [!sample-panel]- 样本与材料快照
> | 样本层面 | 构成 |
> |----------|------|
> | **文本样本** | 文本数量、出版社、年份、科目、语料重心。 |
> | **访谈样本** | 人数、身份构成、地域、信仰、教育背景。 |
> | **材料情境** | 访谈语言、转录翻译、田野地点、材料限制。 |

---

## 论证结构

%% 根据论文实际论证方式，综合运用 [!claim]、[!chain-link]、[!warrant]、[!line-a]、[!contrast-table]、[!evidence-grid]、[!logic-map] 等 callout。下面只是最小骨架，不要求每篇都保留同样组合。 %%

> [!logic-map]- 核心论证逻辑链
> ```mermaid
> flowchart LR
>     A["问题起点"]
>     B["概念工具"]
>     C["证据一"]
>     D["证据二"]
>     E{"结构断裂"}
>     F["结论"]
>
>     A --> B
>     B --> C
>     B --> D
>     C --> E
>     D --> E
>     E --> F
> ```

---

### 论证步骤一

%% 本步骤可按需扩充：[!exegesis]- 加具体例子；[!contrast-table] 或 [!tension-table] 做横向比较；[!evidence-grid] 列证据索引；[!line-a]/[!line-b] 标注并置材料；[!logic-map]- 可视化局部论证链。 %%

> [!claim] 步骤一主张
> 写出这一论证步骤的局部主张。

> [!chain-link] 证据到判断
> 说明关键材料、数据或文本如何支持这一步主张。抽象处加入原文例子或简短教育情境说明。

> [!warrant]- 推理桥梁
> 说明为什么这组证据足以推出上述判断，指出中间假设、分类标准或解释规则。

---

### 论证步骤二

%% 本步骤可按需扩充：[!proposition-chain] 列递进命题；[!feature] 做要素拆解；[!framework-table] 展示理论工具如何转化为分析维度；[!effect-table]- 或 [!ma-table]- 记录量化数据。 %%

> [!claim] 步骤二主张
> 写出第二步如何推进、修正或限定第一步。

> [!chain-link] 证据到判断
> 说明这一组证据如何推动论证进入下一层。

---

### 论证步骤三

%% 本步骤可按需扩充：[!implication]- 展开推论后果；[!finding-cards] 提前列核心发现；[!debates] 记录多方学术争论；[!tension] 仅用于两方正面对立；[!critique]- 记录外部批评。 %%

> [!claim] 步骤三主张
> 写出最终论证收束。

> [!warrant]- 最终推理桥梁
> 说明作者如何从前面材料收束到最终判断，避免只写结论。

---

## 主要发现

> [!finding-cards] 核心发现
> 1. **发现一** 一句话说明第一个核心判断，尽量标注页码。
> 2. **发现二** 一句话说明第二个核心判断，尽量标注页码。
> 3. **发现三** 一句话说明作为收束的核心判断，尽量标注页码。
> 4. **可选发现** 只有确实需要第四点时才保留。

> [!stat-cards]- 核心数据
> - **数字** 含义。（p.X）
> - **数字** 含义。（p.X）

---

## 关键引用

%% 可按引用数量重复 [!citation-card]-，每张对应一个主题或论证节点。 %%

> [!citation-card]- 引用主题
> 中文译文。（p.X）
>
> *Original text or English translation.*

---

## 自述局限

> [!warning]
> 只写原文明确自述的局限、边界条件或未来研究方向，并附页码。不要补写外部批评、外部评价或原文没有说明的缺陷。

---

## 来源

- [[Source_Name]]
