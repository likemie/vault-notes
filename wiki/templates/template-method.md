---
title: <% tp.file.title %>
aliases: []
type: method
tags: []
related_concepts: []
related_theories: []
related_methods: []
related_persons: []
related_arguments: []
sources: []
confidence: medium
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

# <% tp.file.title %>

> [!info]- 建条目的判断标准
> 论文提供该方法任意一项信息即可建条目（操作步骤、认识论立场、适用场景、局限性等）。
> 方法只被命名但无任何介绍 → 只在论证框架条目的「研究方法」一行记录，不单独建条目。

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

## 定义

> [!info]
> 写出方法的核心定义，附来源；不要只写“这是一种质性/量化方法”。

---

## 认识论立场

> [!abstract]
> 说明该方法通常属于哪个研究范式、如何理解知识、证据和研究者角色。

---

## 研究程序

> [!example]
> 说明如何执行，列出关键步骤、材料处理方式和分析逻辑。

---

## 适用场景

> [!success]
> 说明适合回答什么类型的研究问题，以及常见研究对象或材料。

---

## 局限性

> [!warning]
> 说明方法的主要限制、误用风险和适用边界，附来源。（Author, year, p.X）

---

## 相关理论

> [!tip]
> - [[建构主义]] — 一句话说明关系

---

## 使用此方法的研究

> [!example]
> - [[Argument_Lave_1991]] — 一句话说明研究内容

---

## 来源

- [[Hammersley_1983_Routledge]]
