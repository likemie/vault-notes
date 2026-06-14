# Callouts

本文件定义 `wiki/templates/` 使用的 callout 语义和 CSS contract。具体视觉样式由 `.obsidian/snippets/argument-callouts.css` 提供；本文件只规定“什么时候用哪一种”。

---

## General Rules

- callout 服务阅读层次，用来区分定义、论证框架、数据、例子、争议、原文引用和结构导航。
- 普通说明段不要强行包进 callout。
- 同一节内 callout 不宜过密；内容少于 3 点时优先用散文或普通列表。
- 任何 callout 可加 `+` 或 `-` 控制折叠，例如 `[!stat-cards]-`。
- 嵌套不超过 2 层。
- 列表项内嵌套 callout 使用 `>    > [!type]`，即外层 `>` 加 3 个空格再加内层 `>`。
- Mermaid 节点标签保持单行简短，流程图默认使用 `flowchart LR`。
- `---` 分割线用于主要章节之间，以及 Argument 论证步骤之间；不要在同一小段内部频繁插入。
- 样式库只提供可复制的版式，不要求每篇 Argument 全部使用；优先服务论证清晰度。
- `[!logic-map]` 内节点标签不使用 `\n`，保持单行简短标签。
- `---` 的视觉语义：`##` 之前用于模块级切割；`###` 之前用于步骤间流程延续。

---

## Core Callouts

| Callout | 用途 |
|---|---|
| `[!info]` | 定义、背景、方法说明、前提条件 |
| `[!abstract]` | 核心主张摘要、理论框架、政策摘要、章节结构 |
| `[!question]` | 研究问题、经验谜题、核心关切 |
| `[!claim]` | 核心主张、局部命题、论证步骤中的可争辩判断 |
| `[!warrant]` | 证据与主张之间的推理桥梁、理论支撑理由 |
| `[!implication]` | 发现、命题或论证的理论、方法和实践后果 |
| `[!concept-lens]` | 概念的含义、用途和边界三联透镜 |
| `[!success]` | 主要发现、影响、效果 |
| `[!warning]` | 局限、风险、重要例外 |
| `[!tip]` | 理论提示、相关理论、可迁移经验 |
| `[!quote]` | 原文引用或双语关键引用 |
| `[!example]` | 案例、教育情境例子 |
| `[!note]-` | 可折叠补充说明 |
| `[!nav]` | 长节开头的阅读导览 |
| `[!reading-lens]` | 页面级阅读镜头或样式库导览，主要用于模板说明 |

---

## Argument Callouts

| Callout | 用途 |
|---|---|
| `[!stat-cards]` | 样本量、比例、效应量、关键数字 |
| `[!framework-table]` | 理论镜头、概念工具箱 |
| `[!method-panel]` | 研究设计、材料处理、分析步骤 |
| `[!sample-panel]` | 样本构成、材料快照、访谈信息 |
| `[!logic-map]` | Mermaid 论证图、机制图、因果链 |
| `[!step]` | 单个论证步骤容器 |
| `[!line-a]` | 并列趋势、证据链或命题线索，连续使用时自动 A、B、C |
| `[!line-b]` | 与前一个 `[!line-a]` 构成左右拼合或对照 |
| `[!chain-link]` | 独立“证据到分析结论”链节 |
| `[!evidence-grid]` | 多点并列证据 |
| `[!evidence-grid-a]` | 第一组主题证据，常与 `[!evidence-grid-b]` 对照 |
| `[!evidence-grid-b]` | 第二组主题证据，常与 `[!evidence-grid-a]` 对照 |
| `[!contrast-table]` | 两种或多种逻辑、框架、案例的多维对照 |
| `[!finding-cards]` | 不超过四条核心发现 |
| `[!pathways]` | 行动路径、实践建议、操作化方案 |
| `[!conclusion]` | 论证结论或批评裁定 |
| `[!voice]` | 边缘声音、访谈引述、立场陈述 |
| `[!case]` | 独立政策或实证案例 |
| `[!ref-table]` | 参考速查表，适合地区、案例或指标一览 |

Argument 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 研究问题 | `[!question]`、`[!stat-cards]` |
| 理论框架 | `[!framework-table]`、`[!logic-map]`、`[!frames-ref]`、`[!warrant]` |
| 研究方法 | `[!method-panel]`、`[!sample-panel]` |
| 论证结构 | 按论文实际论证综合使用 `[!logic-map]`、`[!claim]`、`[!chain-link]`、`[!warrant]`、`[!line-a]`、`[!contrast-table]`、`[!evidence-grid]` |
| 主要发现 | `[!finding-cards]`、`[!stat-cards]`、`[!evidence-grid]` |
| 自述局限 | `[!warning]` |
| 关键引用 | `[!citation-card]` |

注意：

- `[!line-a]` 连续使用时表示并列线索或证据链，序号自动递增。
- `[!line-b]` 只在需要与前一个 `[!line-a]` 构成左右拼合或对照时使用。
- `[!chain-link]` 用于完整的“证据 → 分析结论”链节，各块内容应自足。
- `[!stat-cards]` 在方法章节可写样本量；在主要发现章节应优先写结果数据，不把受访人数等样本背景混入核心发现。
- `[!finding-cards]` 适合 3–4 条核心发现；超过 4 条时改用小节或证据网格。
- `[!claim]` 必须写可争辩判断，不写材料描述。
- `[!warrant]` 必须解释“为什么证据能支持主张”，不重复证据。
- `[!implication]` 用于收束意义，避免把所有延伸讨论塞进主要发现。

---

## Concept and Theory Callouts

| Callout | 用途 |
|---|---|
| `[!boundary]` | 概念边界、适用范围、排除条件 |
| `[!def]` | 概念定义，适合突出核心定义和边界 |
| `[!term]` | 术语说明，适合短定义或名称辨析 |
| `[!tension]` | 理论张力、对立立场、规范冲突 |
| `[!feature]` | 并列特征或属性卡片 |
| `[!features]` | 紧凑特征列表，常嵌套在父 callout 中 |
| `[!taxonomy]` | 分类或层级体系 |
| `[!assumptions]` | 一组层层递进的理论假设或前提 |
| `[!axioms]` | 公理化前提或不可再拆的基础命题 |
| `[!designs]` | 设计类型、研究设计或制度设计方案 |
| `[!decisions]` | 决策点、判断路径或选择标准 |
| `[!exegesis]` | 抽象概念或论证步骤的解释性补充，常配教育例子 |
| `[!timeline]` | 年代里程碑列表，每项一行 |
| `[!phase]` | 有明确起止年代的历史阶段叙事 |
| `[!dev-timeline]` | 大型分阶段时间轴，含子事件和散文详情 |
| `[!frames-ref]` | 固定数量的框架、原则或要点，适合 6–12 项 |
| `[!quad-grid]` | 恰好 4 项且权重相当的类型、案例或框架 |
| `[!actor-grid]` | 行动者或利益相关者类型网格 |
| `[!col-l]` + `[!col-r]` | 父 callout 内两个并列子主题 |

Concept 页面常用位置：

| 位置 | 推荐 callout |
|---|---|
| 定义 | `[!def]`、`[!concept-lens]`、`[!boundary]`、`[!quote]` |
| 概念辨析 | `[!contrast-table]` |
| 核心要素 | `[!feature]`、`[!logic-map]`、`[!taxonomy]`、`[!frames-ref]`、`[!contrast-table]` |
| 核心命题 | `[!claim]`、`[!warrant]`、`[!implication]`、`[!line-a]`、`[!logic-map]`、`[!finding-cards]` |
| 概念演变 | `[!timeline]`、`[!phase]`、`[!dev-timeline]` |
| 理论语境 | `[!logic-map]`、`[!frames-ref]`、`[!quad-grid]`、`[!col-l]` + `[!col-r]` |
| 实证发现 | 默认一句话索引；材料丰富时可选 `[!stat-cards]`、`[!finding-cards]`、`[!evidence-grid-a]`、`[!evidence-grid-b]` |
| 争议与批评 | 根据实际材料选用 `[!tension]`、`[!warning]`、`[!critique]`、`[!critique-method]`、`[!critique-logic]`、`[!critique-data]`、`[!critique-fatal]` |
| 应用案例 | 默认一句话索引；材料丰富时可选 `[!case]`、`[!evidence-grid-a]`、`[!evidence-grid-b]` |
| 关键引用 | `[!citation-card]` |

注意：

- `[!line-a]` + `[!line-b]` 适合概念对或命题与延伸的层级关系；内容简短时改用 `[!finding-cards]`。
- `[!frames-ref]` 适合 6–12 个固定并列条目；有层级或需要散文延伸时改用 `[!finding-cards]`。
- `[!dev-timeline]+` 适合有丰富子事件的概念发展；内容少时降级为 `[!timeline]` 或 `[!phase]`。
- `[!citation-card]` 每节最多 1–2 个，优先集中到页面后部。
- `[!contrast-table]` 是 `## 概念辨析` 的首选样式。
- `[!concept-lens]` 适合定义章节开头，用三点快速说明“含义、用途、边界”。

---

## Method and Critique Callouts

| Callout | 用途 |
|---|---|
| `[!formula]` | 单个公式与变量说明 |
| `[!formula-set]` | 多公式对比 |
| `[!critique]` | 通用学术批评 |
| `[!critique-method]` | 方法论或统计错误 |
| `[!critique-logic]` | 逻辑或概念矛盾 |
| `[!critique-data]` | 实证或数据反例 |
| `[!critique-fatal]` | 根本性缺陷 |

---

## Book and Evaluation Callouts

| Callout | 用途 |
|---|---|
| `[!chapter-question]` | 章节研究问题或章节在全书论证中的位置 |
| `[!strength]` | SWOT 或评价中的优势 |
| `[!weakness]` | SWOT 或评价中的劣势 |
| `[!opportunity]` | SWOT 或评价中的机会 |
| `[!threat]` | SWOT 或评价中的威胁 |
| `[!indicators]` | 评价指标体系或分层指标 |
| `[!lessons]` | 案例分析后的经验、启示或教训 |

---

## Citation Cards

关键引用优先使用 `[!citation-card]` 或 `[!quote]`。

外文材料：

```markdown
> [!citation-card] 引用标题
> 中文译文。[[Argument_Author_Year_Journal|(Author, Year, p. X)]]
>
> Original: Original text.
```

中文材料：

```markdown
> [!citation-card] 引用标题
> 中文原文。[[Argument_Author_Year_Journal|(作者, 年份, p. X)]]
>
> English: English translation.
```

不要只写中文意译；重要逐字引用必须保留原文。
