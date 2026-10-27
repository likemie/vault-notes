---
title: <% tp.file.title %>
aliases: []
summary: ""
type: fact
subtype: program
region: uk
period: ""
initiator_organization: ""
tags: [eef, eef-programme]
related_concepts: []
related_theories: []
related_methods: []
related_instruments: []
related_persons: []
related_facts: []
related_arguments: []
confidence: medium
status: draft
created: <% tp.date.now("YYYY-MM-DD") %>
updated: <% tp.date.now("YYYY-MM-DD") %>
---

%% EEF 具名项目专用 Program 模板。占位字段在建条时替换；相关字段由脚本维护。
正文的每项事实须链接对应 Argument，或明确标注 EEF 网页快照及具体页面。
网页数据只能支持网页实际报告的内容。未读报告时不能补写研究设计或因果解释。
本骨架保留 Program 的五部分；辅助章节缺材料时删除，不填造争议或发展节点。
缩写首次出现写中文（英文全称，缩写）。卡片已列出的数字（影响、证据强度、成本、样本、剂量、培训、试验日期）正文不重复，只补充解释与来源。
不输出记录方式的自我说明、泛化核验提醒或阅读指引；缺失信息只在对应字段标记待核实，保留具体证据限制。
缺失日期写 <span class="eef-pending">待核实</span>；按周期倒推的项目起点须注明推算依据，实际授课日期另核。 %%

## 项目背景与目标

> [!claim] 项目定位
> {{中文项目名（英文专名与缩写）面向什么对象，以什么内容或活动回应什么问题。}}

> [!program-context] 项目背景
> - **立项时间** {{项目研发或启动时间；缺失时写红字待核实。}}
> - **发起与资助主体** {{区分项目开发、交付、评估资助和独立评估的主体。}}
> - **覆盖范围** {{地区与推广规模；试验样本见卡片。}}
> - **核心问题导向** {{项目面向的具体学习或发展问题。}}

## 方案设计

> [!policy-design] 干预方案
> - **项目目标** {{希望改变的学习结果或实践。}}
> - **干预措施** {{实际活动、内容与资源。}}
> - **实施控制** {{执行要求与实施监测；剂量、培训、成本见卡片。}}

### 实施安排

> [!pathways] 交付安排
> - **人员与分工** {{实际交付人员、校内负责人及外部支持者。}}
> - **实施条件** {{页面或报告明确记载的支持条件。}}

## 推进历程

> [!timeline] 项目与评估节点
> - **{{日期}}** {{研发、试点、推广等卡片以外的节点；试验完成时间已在卡片中，不重复。}}

%% 日期不足以确认先后时不强排阶段。试验完成日期、报告上传日期分别标识。
项目网页没有研发或立项年份时，保留已知评估节点，并写明立项时间待核。 %%

## 成效评估

%% 项目在 datasets/eef/programmes.json 的 entries 中显式登记；
运行 python3 scripts/eef_sync.py render-programmes 生成下方模块，不手写卡片数据。
只导入单项目时用 import-programmes --raw <原始 JSON> --slug <项目键>。
下方为 1stClass@Number 1 的真实样板（template-programme 1stclass-number-1 刷新）：
标题与简介 → 四项要点 → 项目信息 → 每次试验一个折叠块（信息表 + 结果表，亚组以 ↳ 标示）→ 待核实事项。 %%

> [!eef-programme|v3] [1stClass@Number 1](https://educationendowmentfoundation.org.uk/projects-and-evaluation/promising-programmes/1stclass-number-1)
> 为二年级数学困难学生设计的 10 周小组数学干预。
>
> | imp | stage | sec | cost |
> | --- | --- | --- | --- |
> | +2 个月 | 成效试验 | ●●●●○ | £93 /生/年 |
>
> | k | v |
> | --- | --- |
> | 开发机构 | 边山大学（Edge Hill University）的 Every Child Counts 团队 |
> | 实施主体 | 参与学校，由受训助教交付，校内联络教师协调 |
> | 成本口径 | 最近试验条件下的估算；假定每年实施两组，每组四名学生。现行价格<span class="eef-pending">待核实</span>。 |
>
> > [!eef-trial]- [第一次试验](https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/1stclassnumber) · 成效试验 · 完成 2018-07 · 532 名学生 · +2 个月
> > | k | v |
> > | --- | --- |
> > | 时间 | 项目周期 2015-11 至 2018-07（2 年 8 个月；起点按周期倒推，<span class="eef-pending">待核实</span>）；干预 <span class="eef-pending">待核实</span>，共 10 周 |
> > | 评估 | 牛津大学（University of Oxford）；设有对照组；随机分配程序与具体比较安排<span class="eef-pending">待核实</span>。 |
> > | 样本 | 学生 532 人；学校 130 所<br>130 所学校中，107 所被评为 Good 或 Outstanding。<br>学生中享有 pupil premium 资格的比例为 28%。 |
> > | 剂量 | 每周 3 次 × 30 分钟，每组 4 人；项目方案；首次试验适用性<span class="eef-pending">待核实</span> |
> > | 培训 | 助教六个半天；课堂教师两个半天。 |
> > | 经费 | 研究拨款 £287,500；交付 £77/生/年（3 年摊销）；学校首年 £1,612；不含课堂教师及助教的替岗费用。 |
> > | 资料 | [研究方案](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/Round_8_-_1st_Class_at_Number.pdf?v=1793056918) · [统计分析计划](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/Round_8_-_1st_class_at_number_SAP.pdf?v=1793056918) · [评估报告](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/1stClass%40Number_evaluation_report.pdf?v=1793056918) |
> >
> > | out | grp | imp | es | sec | sig |
> > | --- | --- | --- | --- | --- | --- |
> > | 数量推理 | 全体学生 | +2 | — | ●●●●○ | 未达统计显著 |
> > | 数量推理 | ↳ 免费校餐资格学生 | 0 | — | 不适用 | 未报告 |
>
> > [!eef-trial]- [第二次试验](https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/1stclass-number1-second-trial) · 成效试验 · 完成 2026-10 · 1,880 名学生 · +2 个月
> > | k | v |
> > | --- | --- |
> > | 时间 | 试验 <span class="eef-pending">待核实</span>；干预 <span class="eef-pending">待核实</span>，共 10 周 |
> > | 评估 | [英国国家教育研究基金会（National Foundation for Educational Research，NFER）](https://www.nfer.ac.uk/about-nfer/)；随机分配程序与分析方法<span class="eef-pending">待核实</span>。 |
> > | 样本 | 学生 1,880 人；学校 235 所；随机分配学校 226 所<br>73% 的试验学校属于全国免费校餐资格比例最高的 40% 学校。<br>91% 位于城市，全国对应比例为 70%。<br>学校 第二关键阶段（Key Stage 2，KS2） 数学达标率均值为 70.4，全国为 73.1。 |
> > | 剂量 | 每周 3 次 × 30 分钟，每组 4 人 |
> > | 培训 | 导言写一个整天和四个半天；实施段另写六次培训，计数待核。 |
> > | 经费 | 研究拨款 £386,457.59；交付 £93/生/年（3 年摊销）；学校年均 £745 |
> > | 资料 | [评估报告](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/1stClassNo.1_evaluation-report_v.1.0.0_2025-06-25-173138_pttn.pdf?v=1793026194) · [研究方案（修订版）](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/EECN_Study_Protocol_OnlineTrainingUpdate_V2.pdf?v=1793026194) · [研究方案](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/1stClass%40Number1_Evaluation-Protocol.pdf?v=1793026194) · [统计分析计划](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/1stClass%40Number1_Statistical-Analysis-Plan.pdf?v=1793026194) · [补充附录](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/1st%40ClassNo.1_further-appendices_v.1.0.0_2025-06-25-173129_zjgf.pdf?v=1793026194) |
> >
> > | out | grp | imp | es | sec | sig |
> > | --- | --- | --- | --- | --- | --- |
> > | 数学成绩 | 全体学生 | +2 | 0.12 | ●●●●○ | 未报告 |
> > | 数学成绩 | ↳ 免费校餐资格学生 | +2 | 0.11 | 不适用 | 未报告 |
>
> > [!eef-errata]- 3 项待核实
> > - **第一次试验** 免费校餐资格亚组的结构化评级为不适用，评估结论称其证据安全性低于全样本。
> > - **第二次试验** 页面登记学校数与随机分配学校数的差额原因不明。
> > - **第二次试验** 页面完成时间晚于评估报告附件上传日期。

### 结果解释与适用范围

{{按实际测量的指标解释结果。区分不同人群、时点及版本；保留显著性与不确定性。}}

### 实施条件与证据局限

{{说明样本与目标场景的差别，列出确有依据的测量、实施与数据限制。网页和报告的结论分别注明出处。}}

%% 项目页和评估页字段冲突时，保留两个值及各自出处，标记待核；不代替来源作纠正。
争议材料充足时可增加独立章节；实施者满意或反馈不能直接写成学生因果收益。 %%

> [!entry-map] 相关条目
>
> | 条目 | 类型 | 关系 |
> | --- | --- | --- |
> | {{已有的具名项目或项目版本}} | Fact | {{明确的版本或实施关系}} |
> | {{已有的教学策略概念}} | Concept | {{该项目实际采用的措施}} |
> | {{已核实的机构}} | Fact | {{开发、交付、资助或评估的具体角色}} |
> | {{已读完报告后建立的 Argument}} | Argument | {{对应哪次试验与哪项结果}} |
