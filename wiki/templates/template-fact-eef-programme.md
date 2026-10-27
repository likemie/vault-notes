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

%% EEF 具名项目专用，结构与 template-fact-program 对齐：分割线分段，不设 H2。
[!eef-programme|v3] 卡片由 eef_sync.py render-programmes 按 datasets/eef/programmes.json 的 entries 生成，不手写；
它取代 Program 模板的 [!indicators] 与 [!stat-cards]。卡片已列出的数字（影响、证据强度、成本、样本、剂量、培训、试验日期、开发机构、实施主体）正文不重复，只作解释并注明出处。
正文每项事实链接对应 Argument，或注明 EEF 网页及具体页面；网页数据只支持网页实际报告的内容，未读报告时不补写研究设计或因果解释。
学科和实施方式写入英文 tags，卡片不重复列标签。
缩写首次出现写中文（英文全称，缩写）。缺材料的段落整段删除，不填造争议或发展节点。
缺失日期写 <span class="eef-pending">待核实</span>；按周期倒推的起点须注明推算依据。 %%

---

> [!claim] 项目定位
> {{中文项目名（英文专名与缩写）面向什么对象，以什么内容或活动回应什么问题；开发方与 EEF 评估情况。}} [EEF 项目页](URL)

> [!program-context] 项目背景
> - **立项时间 / 周期** {{项目研发或启动时间；缺失时写红字待核实。}}
> - **发起方与资助机制** {{卡片未列的资助来源，如评估所属基金；开发机构不重复。}}
> - **覆盖范围与对象** {{地区、学段与参加条件；不写试验样本量。}}
> - **核心问题导向** {{项目面向的具体学习或发展问题。}}

---

> [!claim] 核心干预假说
> {{通过什么人员、形式与内容，预期改变哪项学习结果。}}

> [!policy-design] 方案设计
> - **项目目标** {{希望改变的学习结果或实践。}}
> - **覆盖对象** {{学段、年龄、筛选方式，普遍或定向实施。}}
> - **干预措施** {{实际活动、内容与资源；不写次数、时长与组别人数。}}
> - **实施控制** {{课案、监测与执行要求；随机分组等研究设计写在卡片对应试验。}}

%% 已有 Argument 引述项目方案时，可加 [!citation-card]；仅有 EEF 网页时不加。 %%

---

%% 只写卡片以外的节点（研发、试点、推广、版本更替），节点少时用 [!timeline]，演变复杂时用 [!dev-timeline]-。
试验完成时间与评估机构已在卡片中；除此之外没有可核实的节点时，删去整段。 %%

> [!timeline] 项目推进历程
> - **{{日期}}** {{研发、试点、推广、版本更替等节点；注明出处。}}

---

%% 卡片已列开发机构与实施主体。仅当评估报告另有分工细节时保留本卡，否则删除。 %%

> [!actor-grid] 实施协同矩阵
> - **开发与支持方** {{开发团队的具体职责（课程、培训、质量监控）。}}
> - **评估与资助方** {{EEF 委托、独立评估机构及其他资助者的角色。}}
> - **一线交付者** {{实际授课人员及校内协调人员的分工。}}
> - **受益对象** {{接受干预的学生及其筛选条件。}}

> [!pathways] 实施路径与管理
> - **课程内容** {{主题顺序与课次安排。}}
> - **学习活动** {{课堂活动形式。}}
> - **课前准备** {{备课与资源要求；培训时数已在卡片中。}}
> - **实施条件** {{评估报告指出的关键实施条件。}}

---

> [!eef-programme|v3] [1stClass@Number 1](https://educationendowmentfoundation.org.uk/projects-and-evaluation/promising-programmes/1stclass-number-1)
> 为二年级数学困难学生设计的 10 周小组数学干预。
>
> | imp | stage | sec | cost |
> | --- | --- | --- | --- |
> | +2 个月 | 成效试验 | ●●●●○ | <span class="eef-cost">●●○○○ 低</span><br><small>£93/生/年</small> |
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
> > | 样本 | 页面学校数 130 所<br>130 所学校中，107 所被评为 Good 或 Outstanding。<br>学生中享有 pupil premium 资格的比例为 28%。 |
> > | 剂量 | 每周 3 次 × 30 分钟，每组 4 人；项目方案；首次试验适用性<span class="eef-pending">待核实</span> |
> > | 培训 | 助教六个半天；课堂教师两个半天。 |
> > | 经费 | 成本评级 <span class="eef-cost">●○○○○ 极低</span>；研究拨款 £287,500；交付 £77/生/年（3 年摊销）；学校首年 £1,612；不含课堂教师及助教的替岗费用。 |
> > | 资料 | [研究方案](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/Round_8_-_1st_Class_at_Number.pdf?v=1793056918) · [统计分析计划](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/Round_8_-_1st_class_at_number_SAP.pdf?v=1793056918) · [评估报告](https://d2tic4wvo1iusb.cloudfront.net/production/documents/projects/1stClass%40Number_evaluation_report.pdf?v=1793056918) |
> >
> > | out | grp | imp | es | sec | sig |
> > | --- | --- | --- | --- | --- | --- |
> > | 数量推理 | 全体学生 | +2 | 未提供 | ●●●●○ | 未达统计显著 |
> > | 数量推理 | ↳ 免费校餐资格学生 | 0 | 未提供 | 不适用 | 未报告 |
>
> > [!eef-trial]- [第二次试验](https://educationendowmentfoundation.org.uk/projects-and-evaluation/projects/1stclass-number1-second-trial) · 成效试验 · 完成 2026-10 · 1,880 名学生 · +2 个月
> > | k | v |
> > | --- | --- |
> > | 时间 | 试验 <span class="eef-pending">待核实</span>；干预 <span class="eef-pending">待核实</span>，共 10 周 |
> > | 评估 | [英国国家教育研究基金会（National Foundation for Educational Research，NFER）](https://www.nfer.ac.uk/about-nfer/)；随机分配程序与分析方法<span class="eef-pending">待核实</span>。 |
> > | 样本 | 页面学校数 235 所；随机分配学校 226 所<br>73% 的试验学校属于全国免费校餐资格比例最高的 40% 学校。<br>91% 位于城市，全国对应比例为 70%。<br>学校 第二关键阶段（Key Stage 2，KS2） 数学达标率均值为 70.4，全国为 73.1。 |
> > | 剂量 | 每周 3 次 × 30 分钟，每组 4 人 |
> > | 培训 | 导言写一个整天和四个半天；实施段另写六次培训，计数待核。 |
> > | 经费 | 成本评级 <span class="eef-cost">●●○○○ 低</span>；研究拨款 £386,457.59；交付 £93/生/年（3 年摊销）；学校年均 £745 |
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

> [!finding-cards] 核心实证结论
> - **主要效应** {{按实际测量的指标解释结果，区分时点与版本，保留显著性与不确定性。}}
> - **异质性效应** {{亚组结果的解读；不据两行点估计推断亚组差异显著。}}
> - **边界条件** {{样本与目标场景的差别、测验敏感度等限制。}}

---

%% 争议材料充足时加 [!debates]；实施者满意或反馈不能直接写成学生因果收益。 %%

> [!lessons] 经验教训与启示
> - **实施教训** {{评估报告记载的实施困难与偏差。}}
> - **证据局限与推广启示** {{测量、实施与数据限制，以及对推广的含义。网页与报告的结论分别注明出处。}}

---

> [!entry-map] 相关条目网络
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | {{教学策略概念}} | Concept | {{该项目实际采用的措施。}} |
> | {{开发、交付、资助或评估机构}} | Fact (Organization) | {{具体角色。}} |
> | {{EEF 因素条目}} | Concept | {{对应的 Toolkit 主题。}} |
> | {{读完报告后建立的 Argument}} | Argument | {{对应哪次试验与哪项结果。}} |
