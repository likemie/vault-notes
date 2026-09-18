---
title: Massachusetts Department of Elementary and Secondary Education
aliases:
  - 马萨诸塞州中小学教育部
  - DESE
  - Massachusetts DESE
  - 马州中小学教育部
summary: "主管美国马萨诸塞州公立学前、初等与中等教育的州级行政机关，以其先进的集中式教育数据仓库、严密的高利害问责评测系统（MCAS）及多套数据支持工具（DART、RADAR、EWIS）著称"
type: fact
subtype: organization
region: us
fact_region: "us"
fact_kind: "organization"
fact_related_count: 9
fact_related_level: 1
fact_related_stars: "⭐"
fact_related_color: "#dcfce7"
org_type: state-education-agency
headquarters: "Malden, Massachusetts, United States"
established: "1837"
tags:
  - fact/organization
  - fact/us
  - educational-governance
  - data-infrastructure
  - accountability
related_concepts:
  - "[[Data Infrastructure]]"
  - "[[Academic Achievement]]"
  - "[[Growth]]"
related_methods:
  - "[[Questionnaire]]"
related_persons:
  - "[[Horace Mann]]"
related_facts:
  - "[[Partnership Schools Kura Hourua]]"
  - "[[Elementary and Secondary Education Act of 1965]]"
  - "[[Early Warning Indicator System]]"
related_arguments:
  - "[[Argument_Hartong_Forschler_2019_BDS]]"
confidence: high
status: stable
created: 2026-09-18
updated: 2026-09-18
---

# Massachusetts Department of Elementary and Secondary Education

---

## 机构定位与宗旨

> [!claim] 核心定位
> 马萨诸塞州中小学教育部（Massachusetts Department of Elementary and Secondary Education, DESE）是负责监管与统筹指导美国马萨诸塞州全域公立 K-12 教育的州级执行部门。作为全美教育改革与高标准问责的先锋州行政机关，该机构构建了高度成熟的数字化[[Data Infrastructure|数据基础设施]]，依托集中式数据仓库与高级分析建模，推行集质量监测、学区资源优化、学生早警预警与高利害行政干预于一体的现代教育治理体系[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, pp. 2–4)]]。

> [!org-context] 机构背景
> - **成立时间 / 创设背景** 源起于 1837 年由[[Horace Mann|霍勒斯·曼]]（Horace Mann）推动创设的马萨诸塞州教育委员会（Massachusetts Board of Education），历经多次州政体制改革，于 2008 年在《公立教育重组法案》下正式重构为当前的中小学教育部。
> - **总部地点 / 业务辐射** 机构总部位于马萨诸塞州摩顿（Malden），法定管辖范围覆盖全州逾 300 个公立学区、近 2000 所公立中小学及[[Partnership Schools Kura Hourua|特许学校]]。
> - **法人属性与经费基础** 州政府内阁级公立行政机关，运作资金依托马萨诸塞州财政年度教育专项拨款及联邦[[Elementary and Secondary Education Act of 1965|初等与中等教育法]]案配套资助。
> - **核心宗旨与法定职责** 确保全州所有学生获得平等的优质公立教育机会，制定全州课程框架、教师资格认证标准，执行全州标准化学生学业评价（MCAS），并依照联邦与州法律实施学区绩效督导及低绩效学校行政托管接管[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, pp. 2, 8)]]。

---

## 数据治理与技术架构

> [!feature] 核心数据工具与治理机制
> - **集中式数据仓库与多源摄取（Data Warehouse）**
>   建立全州统一的集中式数据仓库，通过学生信息管理系统（SIMS）与教育人员信息管理系统（EPIMS）等渠道，定期自学区和学校吸纳覆盖出勤、测评、课程与师资的海量微观数据，运用自动化业务规则（Data Business Rules）执行格式与逻辑质检[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, pp. 4, 7)]]。
> - **[[Early Warning Indicator System|早期预警指标系统]]（EWIS）**
>   开发早期预警指标系统（Early Warning Indicator System, EWIS），依托纵向预测模型评估学生在不同学段面临的学术掉队或未能进入大学的风险等级，为一线教师提供针对性干预信息，但同时面临被一线错误用作学业劝退工具的技术误读张力[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 6)]]。
> - **学区分析与审查工具（DART）**
>   为全州各学区提供基于人口统计与[[Academic Achievement|学业表现]]的一览式分析工具（District Analysis and Review Tools, DART），辅助学区领导开展跨地域统计相似群体的横向对比与绩效归因[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, pp. 6–7)]]。
> - **资源配置与学区行动报告（RADAR）**
>   开发资源配置与学区行动报告系统（Resource Allocation and District Action Reports, RADAR），将学区财务支出、人员编制与学生成绩进行交叉建模，支持学区自主遴选至多 10 个地理邻近或统计特征相似的学区展开资源效益对标分析[[Argument_Hartong_Forschler_2019_BDS|(Hartong & Förschler, 2019, p. 7)]]。

---

## 实践张力与制度特征

> [!tension-table] DESE 数据实践中的制度张力
> | 实践领域 | 核心机制 | 治理挑战 | 实践应对策略 |
> |---|---|---|---|
> | **数据冻结与时效** | 设立学区法定认证截止日（Steel Door），冻结数据作为单一事实来源（Single Point of Truth） | 法定截止后发现的深层错误难以撤回修正，可能破坏已向社会公布的历史序列 | 宏观呈报保持刚性不追溯，仅对涉及学生高中毕业资格与奖学金的高利害个体数据启动司法鉴定式倒查回溯[[Argument_Hartong_Forschler_2019_BDS\|(Hartong & Förschler, 2019, pp. 7–8)]] |
> | **透明度与隐私防线** | 秉持信息公开哲学，倡导全口径向公众公开以驱动公民监督与自主问责 | 细微统计波动易引发社区恐慌、学区房市波动及对弱势生源的标签化羞辱 | 严格限制家长端统一门户权限，采用分级数据库安全角色（Security Roles）与数据假名化隔离敏感信息[[Argument_Hartong_Forschler_2019_BDS\|(Hartong & Förschler, 2019, p. 8)]] |
> | **高利害问责建模** | 将学生[[Growth\|成长]]百分位数（SGP）与毕业率等指标嵌入年度分类评价模型 | 高利害问责引发学校策略性造假（Gaming）及对主观[[Questionnaire\|问卷调查]]（如学校氛围调查）的操纵担忧 | 审慎权衡技术模型与价值规范，限制易受人为操纵的指标进入最终高利害问责体系[[Argument_Hartong_Forschler_2019_BDS\|(Hartong & Förschler, 2019, p. 9)]] |
