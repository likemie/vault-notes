---
title: Third Generation Activity Theory
aliases:
  - 第三代活动理论
  - activity theory
  - 活动理论
  - cultural-historical activity theory
  - CHAT
  - Engeström activity theory
summary: "Engeström（2001）在 Vygotsky 中介三角模型基础上发展出的第三代活动理论，聚焦多个活动系统之间的互动与边界跨越，以矛盾为变革动力，通过扩展性改造实现共享目标"
type: theory
tags:
  - theory/sociocultural
  - theory/activity-theory
  - theme/learning
  - theme/organizational-change
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
sources: []
confidence: medium
status: draft
created: 2026-05-26
updated: 2026-05-26
---

# Third Generation Activity Theory



> [!info]- 自动维护字段（对齐脚本）
> - `related_*` 与 YAML `sources` 由 `scripts/wiki_relations.py` 自动维护，AI 不手动填写。
> - 正文中的 wikilink 会同步到对应 `related_*`。
> - `## 来源` 章节中的 source wikilink 会同步到 YAML `sources`。
> - 正文自动补链由 `scripts/wiki_linker.py sync` 完成；`aliases` 是自动补链白名单。
> - Source 记录与 PDF / EPUB 阅读页面优先由 `scripts/source_record.py` 创建。
> - 处理完成后运行：
>   ```bash
>   python3 scripts/wiki_index.py
>   python3 scripts/wiki_linker.py sync
>   python3 scripts/wiki_relations.py sync
>   python3 scripts/wiki_index.py
>   python3 scripts/vault_lint.py
>   ```

> [!info]- Summary 规则（索引用，不是摘要）
> `summary` 只用于索引说明，让读者一眼看出该理论的提出者、核心命题和解释对象。
> 写法：`提出者/学派 + 核心命题 + 用来解释什么现象`。
> 好例子：`Ann Swidler (1986) 的文化社会学理论，将文化理解为提供行动策略的工具箱，而非单纯价值观系统。`
> 不要写成论文摘要；无法概括时留空：`summary: ""`。

> [!warning]- Summary YAML 安全规则
> `summary` 外层必须使用双引号包裹：`summary: "一句话索引说明"`。
> `summary` 可以正常使用中文逗号、顿号、句号、分号、括号等中文标点；内容内部只需避开英文冒号 `:`、双引号 `"`、单引号 `'`，不要用其他字符代替原本应有的标点。
> 需要断句时优先使用中文逗号，不要为了规避字符而省略标点。
> 如果英文标题原本有冒号，用自然中文改写，或使用中文标点。
> 如果内容需要引用英文著作名，不要用中文书名号、不要用 Markdown 斜体、不要加引号，直接写标题文本。



> [!info]- Frontmatter 格式规范
> - `tags` — 用方括号列表，内容 tag 建议使用英文小写连字符。
> - 推荐 tag 前缀：`level/`、`region/`、`method/`、`theory/`、`policy/`、`subject/`、`theme/`、`source/`。
> - `related_*`、`sources`、`part_of` — 若引用条目，必须写成带引号的 wikilink，如 `"[[Cultural Capital]]"`。
> - 不要在这些字段中写普通文本；不确定是否已有条目时先留空。
> - 单个值也需要引号和方括号：`related_concepts: ["[[Project-Based Learning]]"]`
> - `related_*` 与 YAML `sources` 由脚本自动同步，AI 通常不手动填写；需要建立关系时在正文使用 wikilink，需要记录来源时在 `## 来源` 列出 source wikilink。

> [!info]- Aliases 规则（用于 Automatic Linker 自动补链）
> - `aliases` 用于中英文术语映射，建议包含中文译名、英文原名、常见缩写和常见变体。
> - 文件名／标题可以保持英文；中文正文常用术语应写入 `aliases`，例如 `文化资本` → `Cultural Capital`。
> - 不要加入过于宽泛的普通词，如"资本""文化""政策""课程""能力""国家""公平"。
> - 推荐写完整术语：`文化资本`、`教育分层`、`批判话语分析`、`global competence`、`critical discourse analysis`。
> - 缩写可以写入 aliases，例如 `CDA`、`PISA`、`OECD`，但避免单个字母或过短词。

> [!warning]- 写入规则（每次写入前必须执行）
> 1. 确定新内容属于哪个 `##` 章节。
> 2. 分点 ≥ 8 条 → 按主题建 `###` 子主题，组内按时间排列。
> 3. 分点 < 8 条 → 直接按时间顺序插入正确位置，禁止追加末尾。
> 4. 写入前声明：「归属章节 > 子主题 > 插入位置」，再用 str_replace 写入。


---

## 核心主张

> [!info]
> 活动理论（activity theory）从社会文化视角理解人类行为与社会历史转型。其核心主张是：人类认知发展源于心理表征与外部影响之间的互动，且人类行为应作为集体活动来理解，而非个体行为的简单加总。第三代活动理论进一步主张：不同活动系统之间的互动与边界跨越是变革的来源——当系统之间的矛盾被识别和解决时，原有系统可能经历"扩展性改造"（expansive transformation）。

> "活动理论将人类实践概念化为集体活动，'活动'——定义为'一个有对象导向和文化形塑的结构'——成为分析单元"（Engeström, 1999, p.21，引自 Wang & McLaughlin, 2025, p.590）

---

## 核心命题

> [!abstract]

### 第一代：Vygotsky 的中介三角模型

Vygotsky（1978）提出认知发展源于个体（主体，Subject）与外部影响之间的互动。在这一原始模型中，个体追求发展目标（客体，Object）的过程由社会文化工具（中介工具，Mediating artefacts）——如语言、符号、概念——所中介（Wang & McLaughlin, 2025, p.590）。

> 举例：一个学生学习数学（主体追求客体），所使用的教科书、教师语言和课堂符号系统就是中介工具——这些工具不仅传递知识，也塑造学生如何理解数学。

### 第二代：Engeström 的集体活动系统

Engeström（1987）认识到人类行为与所处社群之间的复杂交互关系，在 Vygotsky 模型基础上增加了三个社会维度，将分析单元扩展为集体活动系统（Wang & McLaughlin, 2025, p.590）：

- **主体（Subject）**：参与活动的个体或群体
- **客体（Object）**：活动的目标
- **中介工具（Mediating artefacts）**：主体为实现客体所使用的工具
- **共同体（Community）**：活动所嵌入的社会情境
- **规则（Rules）**：活动的显性或隐性规范
- **劳动分工（Division of labour）**：不同层级行动者之间的责任分配

> 举例：一个学校的考试问责系统构成一个活动系统——教师（主体）追求提升考试成绩（客体），通过教师主导的教学法（中介工具），在学校评价制度（规则）、家长支持（共同体）和自上而下的目标分解（劳动分工）的共同作用下运作。

### 第三代：多系统互动与边界跨越

Engeström（2001）的第三代活动理论聚焦于跨越不同活动系统边界的过程。核心假设（Wang & McLaughlin, 2025, pp.590-591）：

1. 活动系统是开放的、动态的——一个活动系统可以与其他系统互动并吸收新元素
2. 当不同系统互动时，矛盾（contradictions）和变化会出现——例如 LCE 改革的目标与考试问责的目标之间的冲突
3. 解决矛盾需要每个系统打破自身边界，朝向集体有意义的目标移动
4. 这可以促成"扩展性改造"（expansive transformation）——原有系统的关键元素被重构（Engeström, 2001, p.137）

---

## 发展脉络

> [!note]
> - **Vygotsky（1978）** — 提出第一代中介三角模型：主体—中介工具—客体。认知发展源于人通过文化工具与外部世界的互动
> - **Engeström（1987）** — 发展为第二代活动理论，增加共同体、规则和劳动分工三个社会维度，将活动概念化为集体性、对象导向的文化形构。著作 Learning by Expanding
> - **Engeström（2001）** — 提出第三代活动理论，聚焦多个活动系统之间的互动与边界跨越。提出"扩展性学习"（expansive learning）和"扩展性改造"概念，认为矛盾可以是变革的来源

---

## 认识论立场

> [!info]
> - **本体论与认识论**：社会文化建构主义——人类认知和行为由社会文化情境塑造，不能脱离具体活动系统来理解
> - **分析单元**：集体活动系统，而非个体行为
> - **常用方法**：质性案例研究、民族志、发展性工作研究（developmental work research）；关注系统层面的互动、矛盾和转型，而非个体层面的变量关系

---

## 相关研究

> [!example]
> - [[Argument_Wang_2025_CE]] — 以第三代活动理论为框架，分析中国学校中考试问责系统与 LCE 改革系统之间的互动、矛盾与共享目标的建立

---

## 应用领域

> [!success]
> - **教育改革分析**：用于理解不同教育目标系统之间的张力与可能的协同——如考试问责与 LCE 的关系（Wang & McLaughlin, 2025）
> - **组织学习与变革**：Engeström 最初将活动理论应用于工作场所的学习和创新，分析不同专业团队之间的边界跨越
> - **教师专业发展**：分析教师学习如何在个人信念、学校制度和外部改革压力之间的互动中发生

---

## 来源

- [[Wang_2025_CE]]
