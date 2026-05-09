---
title: <% tp.file.title %>
aliases: []
type: theory
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_facts: []
related_arguments: []
sources: []
confidence: medium
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

> [!info]- Frontmatter 格式规范
> - `tags` — 用方括号列表，内容 tag 建议使用英文小写连字符。
> - 推荐 tag 前缀：`level/`、`region/`、`method/`、`theory/`、`policy/`、`subject/`、`theme/`、`source/`。
> - `related_*` 和 `sources` — 所有值必须加引号。
> - wikilink 必须包在引号内，否则 Obsidian 无法解析 frontmatter。
> - 单个值也需要引号和方括号：`related_concepts: ["[[项目式学习]]"]`

> [!info]- Aliases 规则（用于 Automatic Linker 自动补链）
> - `aliases` 用于中英文术语映射，建议包含中文译名、英文原名、常见缩写和常见变体。
> - 文件名／标题可以保持英文；中文正文常用术语应写入 `aliases`，例如 `文化资本` → `Cultural Capital`。
> - 不要加入过于宽泛的普通词，如“资本”“文化”“政策”“课程”“能力”“国家”“公平”。
> - 推荐写完整术语：`文化资本`、`教育分层`、`批判话语分析`、`global competence`、`critical discourse analysis`。
> - 缩写可以写入 aliases，例如 `CDA`、`PISA`、`OECD`，但避免单个字母或过短词。

> [!warning]- 写入规则（每次写入前必须执行）
> 1. 确定新内容属于哪个 `##` 章节。
> 2. 分点 ≥ 8 条 → 按主题建 `###` 子主题，组内按时间排列。
> 3. 分点 < 8 条 → 直接按时间顺序插入正确位置，禁止追加末尾。
> 4. 写入前声明：「归属章节 > 子主题 > 插入位置」，再用 str_replace 写入。


---

## 核心主张

> [!tip]
> 写出理论的基本立场和最核心主张，避免把应用案例当成理论主张。

> [!quote]
> "原文引用"（Author, year, p.X）

---

## 核心命题

> [!abstract]
> 主要命题或子理论，逐条列出并附来源；每条说明其逻辑含义。

---

## 发展脉络

> [!note]
> 说明理论如何形成、演变和分化，按时间顺序排列。
> - 1920s [[Vygotsky]] 提出社会建构主义
> - 1950s [[Piaget]] 发展认知建构主义

> [!note]- 分期示例
> - 1920s [[Vygotsky]] 提出社会建构主义（p.X）
> - 1936s [[Piaget]] 发展认知建构主义（p.X）

---

## 认识论立场

> [!info]
> - 本体论与认识论立场：简述
> - 常用研究方法：[[质性研究]]、[[民族志]]

---

## 争议与批评

> [!warning]
> 记录理论受到的主要批评、争议和适用边界。
> - 批评描述，附来源和立场。（Author, year, p.X）

---

## 相关研究

> [!example]
> 链接到以此理论为框架的论证框架条目：
> - [[Argument_Thomas_2000]] — 一句话说明如何使用此理论

---

## 应用领域

> [!success]
> - [[项目式学习]] — 以建构主义为核心理论依据

---

## 来源

- [[Vygotsky_1978_HUP]]
