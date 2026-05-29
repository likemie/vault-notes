# Schema：Figures and Attachments

触发标识：用户要求提取、整理、移动、删除、重画或引用文献中的图片、图表、figure、截图、示意图。

只有在任务涉及 figure 时读取本文件；普通文献处理、补链、关系同步不需要读取。

---

## 适用范围

Figure 指从文献中截取、导出或重画的图表图片，包括 `.png`、`.jpg`、`.jpeg`、`.webp`、`.svg`。

常见任务：

- 将已有散放图片整理到 `figures/`。
- 从 PDF / EPUB / source 文件中提取图表。
- 生成或重画论证结构图、概念图、流程图。
- 更新 wiki 条目中的图片嵌入路径。
- 删除确认未引用的多余图片。

---

## 放置规则

### 普通论文／报告 source

一旦普通论文／报告需要提取、整理或引用 figure，就必须把原本扁平放置的 source 记录和源文件一起移动进独立 source 文件夹；figure 任务不是只新增图片文件。

目标结构：

```text
sources/<source-id>/
  <source-id>.md
  <source-id>.pdf
  figures/
    <source-id>_Fig1_Descriptive_Name.png
```

若开始前文件仍在扁平结构：

```text
sources/<source-id>.md
sources/<source-id>.pdf
sources/<source-id>_Fig1_Descriptive_Name.png
```

必须整理为上面的独立文件夹结构，并同步更新所有图片引用路径。source 记录中的 PDF 嵌入可以继续使用同文件夹本地文件名：`![[<source-id>.pdf]]`。

没有配套 figure 的普通论文／报告可以继续使用扁平结构：

```text
sources/<source-id>.md
sources/<source-id>.pdf
```

### 书籍 source

书籍 figure 统一放在书籍工作区内：

```text
books/<book-folder>/
  <book-folder>.md
  BookName.pdf 或 BookName.epub
  figures/
    Figure_2-1_Descriptive_Name.png
```

论文集章节若有 figure，也放在同一 `books/<book-folder>/figures/` 下；文件名应包含章节或作者信息以避免冲突。

---

## 命名规则

- 优先保留来源信息和图号：`Rappleye_2006_Fig3_Conceptual_Map.png`、`Figure_2-1_Western_Learner.png`。
- 重画或自制图应使用可读英文文件名，如 `Argument_Li_2012_Chapter_Relation_Map.svg`。
- 文件名可以保留原书中文图名；若后续需要跨平台发布，再逐步改为英文。
- 同一来源内不要出现含义不明的文件名，如 `image1.png`、`截图.jpeg`、`图.jpeg`。

---

## 引用规则

wiki 正文中嵌入 figure 时，使用从 vault root 开始的完整路径，避免移动条目后断链：

```markdown
![[sources/<source-id>/figures/<figure-file>.png]]
![[books/<book-folder>/figures/<figure-file>.png]]
```

source 记录嵌入同文件夹 PDF / EPUB 时，可以使用本地文件名：

```markdown
![[<source-id>.pdf]]
```

不要在 wiki 条目中使用只含文件名的 figure 嵌入，除非图片与条目在同一文件夹且不会移动。

---

## 移动与删除流程

移动 source 记录、PDF 或 figure 时：

1. 先用 `rg` 找出所有旧路径、裸文件名和相关 source-id。
2. 新建目标 `figures/` 文件夹。
3. 移动文件。
4. 更新所有 `![[...]]` 嵌入路径。
5. 再用 `rg` 确认没有旧路径残留。
6. 跑相关条目的 `vault_lint.py --path ...`。
7. 若移动了 source 记录，运行定向 `wiki_relations.py sync <wiki-argument-path>`；若反向关系明显不完整，再运行 `wiki_relations.py sync --full`。

删除 figure 前必须先用 `rg` 全库确认没有引用；只删除确认未引用的多余图片。

---

## 与其他 schema 的关系

- 书籍任务仍按 `schema/schema-monograph-pdf.md`、`schema/schema-monograph-epub.md` 或 `schema/schema-edited-volume.md` 处理。
- 只有当书籍任务需要处理 figure 时，额外读取本 schema。
- 普通论文／报告只有在存在 figure 或用户要求整理图片时，才读取本 schema。
