---
title: Early Warning Indicator System
aliases:
  - 早期预警指标系统
  - EWIS
  - Early Warning Indicator System (EWIS)
summary: "马萨诸塞州初等与中等教育厅开发的纵向算法预测系统，基于回归模型评估学生高中辍学与大学未能毕业风险，但实践中诱发指导顾问劝阻高危学生申请大学的赤字标签效应"
type: fact
subtype: program
region: "us"
fact_region: "us"
fact_kind: "program"
fact_related_count: 15
fact_related_level: 1
fact_related_stars: "⭐"
fact_related_color: "#ede9fe"
period: "2010s–至今"
initiator_organization: "[[Massachusetts Department of Elementary and Secondary Education]]"
tags:
  - fact/program
  - fact/us
  - educational-monitoring
  - algorithmic-governance
  - dropout-prevention
related_concepts:
  - "[[Data Infrastructure]]"
  - "[[Positivism]]"
  - "[[Variable]]"
  - "[[Teaching Assistant]]"
  - "[[Heterogeneity]]"
  - "[[Data Literacy]]"
  - "[[Determinism]]"
  - "[[Technical Rationality]]"
  - "[[Epistemology]]"
  - "[[Disciplina and Doctrina]]"
  - "[[Test-Based Accountability]]"
related_theories: []
related_methods:
  - "[[Fieldwork]]"
related_instruments: []
related_persons:
  - "[[Sigrid Hartong]]"
related_facts:
  - "[[Massachusetts Department of Elementary and Secondary Education]]"
related_arguments:
  - "[[Argument_Hartong_Forschler_2019_BDS]]"
confidence: high
status: stable
created: 2026-09-18
updated: 2026-09-18
---

# Early Warning Indicator System

---

## 项目背景与立项契机

> [!claim] 项目定位
> 早期预警指标系统（Early Warning Indicator System, EWIS）是美国马萨诸塞州初等与中等教育厅（[[Massachusetts Department of Elementary and Secondary Education]], DESE）依托全州纵向[[Data Infrastructure|数据基础设施]]开发的一套算法预测与学业预警系统，旨在通过对历史学业与出勤数据的回归运算，识别从学前教育直至高中阶段可能偏离学业轨道的学生，并为学校及早介入提供依据。[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 6)]]

> [!program-context] 项目背景
> - **立项时间 / 周期** 2012 年前后研发上线，历经多次算法模型迭代并作为常规数据工具整合进马萨诸塞州 Edwin 分析平台，常态化运行至今。[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 6)]]
> - **发起方与资助机制** 发起部门为马萨诸塞州初等与中等教育厅，由联邦纵向数据系统（SLDS）专项拨款与州教育预算共同资助。
> - **覆盖范围与对象** 覆盖马萨诸塞州全州所有公立学区、公立高中、初中及小学，面向全体公立学校学生进行逐年风险等级计算。
> - **核心问题导向** 回应美国各州长期面临的高中辍学率隐患、大学按期毕业率滞后以及学业援助行动过晚的结构性治理危机。

---

## 方案设计与运行机制

> [!claim] 核心干预／机制假说
> EWIS 建立在[[Positivism|实证主义]]的预防性干预假说之上：假定通过整合历史多维行为数据（出勤、违纪、考试成绩、挂科数），能够建立高精度的纵向统计回归模型，先验地测算出个体学生偏离正常升学轨道的概率并赋予红黄绿风险标签，从而促使学校教辅人员在危机显现前精准投放补救资源。[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 6)]]

> [!policy-design]- 方案设计
> - **项目目标** 识别学生在关键学业过渡节点（如初升高、高中毕业、大学入学及持续就读）的脱轨风险，实现教育资源的预防性精准滴灌。
> - **覆盖对象** 幼儿园至 12 年级所有在册学生，重点聚焦 8–9 年级过渡期与高中阶段升学冲刺期。
> - **算法模型与指标选取** 借鉴 Neild 等人（2007）提出的辍学预警核心指标，构建多[[Variable|变量]]概率回归模型；输入变量涵盖学生出勤率（Attendance）、停课违纪记录（Discipline）、马萨诸塞州综合评估系统（Massachusetts Comprehensive Assessment System, MCAS）标准化测试分数门槛、核心学科不及格科目数等。
> - **输出形式与风险分级** 系统后台运算后将学生自动划分为三类风险等级：低风险（Low Risk，有望达标）、中风险（Moderate Risk，需持续观察）以及高风险（High Risk，高度可能辍学或大学无法毕业），并在州端与校端仪表盘中予以可视化标色呈现。[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 6)]]

> [!citation-card] [[Massachusetts Department of Elementary and Secondary Education|DESE]] 官方关于 EWIS 预测逻辑与应用初衷的阐述
> 早期预警指标系统是一套系统性的全州数据工具，用于探索学生历史轨迹与未来学业成果之间的关联，旨在帮[[Teaching Assistant|助教]]育工作者识别那些若无额外干预则可能无法达成学业里程碑的学生，从而提前规划个性化支持策略。[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 6)]]
>
> *EWIS is designed to identify students who are at risk of missing key educational milestones, helping educators target resources and interventions early to get students back on track.*

---

## 推进历程与阶段演进

> [!dev-timeline] 项目推进历程
> - **2007–2011 — 预警指标理论验证与指标确立** 全美学界与非营利机构（如约翰斯·霍普金斯大学团队）确立以缺勤率与不及格课程为核心的预警指标模型；马萨诸塞州立项论证将全州纵向数据库转变为预测性决策平台的可行性。
> - **2012–2016 — 算法系统上线与全州学区接入** [[Massachusetts Department of Elementary and Secondary Education|DESE]] 正式向全州学区推送 EWIS 报告，嵌入州级统一商业智能与数据报告平台（Edwin Analytics），提供从早期儿童阶段到高中毕业的全链条风险评分。
> - **2017–至今 — 预测向大学升学扩展与微观实践反思** 预测模型进一步向高等教育延伸，纳入预测学生在高中毕业后是否能在六年内完成大学学业的预测概率；与此同时，学界与实地调研揭示出基层顾问对风险标签的扭曲使用等意外后果。[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 6)]]

---

## 实施架构与角色分工

> [!actor-grid] 实施协同矩阵
> - **发起与监管方** 马萨诸塞州初等与中等教育厅（[[Massachusetts Department of Elementary and Secondary Education|DESE]]）：负责全州模型开发、数据库集成、算法参数校准及全州访问权限管控。
> - **技术与平台支持** 州数据管理办公室与第三方软件供应商（如 Edwin Analytics 承建商），负责数据清洗、自动化批处理计算与交互界面交付。
> - **一线执行机构** 各学区督学办公室、公立高中行政团队、指导顾问（School Counselors）以及班主任教师：负责查阅预警清单、解释指标并落实微观学生干预。
> - **目标受试对象** 州内普通中小学学生及其家庭，处于被数据流追踪、标色与分类的接收终端。

---

## 成效评估与实证发现

> [!finding-cards] 核心实证结论
> - **预测准确性与宏观识别效能** 在纯统计预测维度上，多指标回归模型对群体层面的高中辍学与按期毕业表现出较高的统计预测力，帮助州教育厅精准定位了高辍学风险的薄弱学区与群体分布。
> - **微观实践[[Heterogeneity|异质性]]与赤字标签陷阱** 实地定性调研揭示，在缺乏配套个别化辅导资源与正确[[Data Literacy|数据素养]]指引下，基层行政与指导顾问并未将高风险评级转化为帮扶干预，而是将其直接异化为否定学生发展潜力的[[Determinism|决定论]]标签。[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 6)]]

---

## 争议、局限与经验教训

> [!debates] 核心争议
>
> > [!axis] 赤字标签效应与自我实现预言的伦理危机
> > 预测性算法将复杂的学生生存状态还原为孤立的概率数字，在微观实践中直接诱发了教育工作者将系统警告作为劝退或降低期望的理由。
> >
> > - **[[Fieldwork|实地调查]]发现（[[Argument_Hartong_Forschler_2019_BDS|Hartong & Förschler, 2019]]）** 一位高中指导顾问在接受访谈时直言，当系统预测某一学生完成大学学业的概率极低（被划入高风险红区）时，顾问的工作并非为该生提供强化的大学准备支持，而是建议学生“根本不要申请大学，去另寻出路”，将预测工具变成了合法化排斥边缘群体的冷酷守门工具。[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 6)]]
> > - **批判数据学者立场** 这种实践不仅未能实现系统宣称的扶持初衷，反而通过数据权威强化了对处境不利学生的结构性歧视，使预测沦为残酷的“自我实现预言”（Self-fulfilling Prophecy）。
>
> > [!axis] [[Technical Rationality|技术理性]]与行政资源的脱节
> > 州级行政部门过分迷信算法预测的自动化与科学性，误以为部署预测系统便等同于解决了辍学危机，却忽视了一线学校根本缺乏配套干预师资、心理支持网络与充裕预算的现实困境。

> [!lessons] 经验教训与启示
> - **[[Data Infrastructure|数据基础设施]]素养不可或缺** 数据治理绝非单纯的算法部署；若不全面重构一线教育工作者对数据生成逻辑、算法偏误及其[[Epistemology|认识论]]边界的理解（即提高数据基础设施素养），越是精密的预测模型越容易演变为[[Disciplina and Doctrina|规训]]与推卸责任的行政利器。
> - **警惕从发展性评估向惩罚性分流的滑坡** 预警系统必须建立严格的伦理护栏，禁止将风险评分直接作为剥夺学生学习机会、关闭高阶升学通道的行政依据。

---

## 相关条目网络

> [!entry-map]
>
> | 条目 | 类型 | 关系 |
> |:-----|:-----|:-----|
> | [[Data Infrastructure]] | Concept | EWIS 所依托的全州纵向综合数据系统与分析平台。 |
> | [[Technical Rationality]] | Concept | 驱使开发团队将辍学治理简化为概率风险计算的技术理性信念。 |
> | [[Test-Based Accountability]] | Concept | EWIS 的核心输入[[Variable\|变量]]重度依赖全州统考标准化测试成绩。 |
> | [[Massachusetts Department of Elementary and Secondary Education]] | Fact (Org) | 系统的立项、开发、维护与推广实施主体。 |
> | [[Sigrid Hartong]] | Person | 深度调研 EWIS 在公立高中基层实践中的扭曲与异化后果。 |

