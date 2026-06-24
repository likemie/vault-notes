---
title: 概念索引
---

从这里进入概念网络：先看连接最密的核心概念，再按知识领域分流。

```base
filters:
  and:
    - 'type == "concept"'
    - 'file.folder.contains("wiki/concepts")'

properties:
  file.name:
    displayName: 概念
  summary:
    displayName: 摘要
  domain:
    displayName: 领域
  related_stars:
    displayName: 亮度
  related_count:
    displayName: 连接
  related_color:
    displayName: 色带
  tags:
    displayName: 标签
  updated:
    displayName: 更新

views:
  - type: cards
    name: 概念图谱
    image: related_color
    order:
      - file.name
      - summary
      - domain
      - related_stars
      - related_count
    sort:
      - property: related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: cards
    name: 概念枢纽
    image: related_color
    filters:
      and:
        - 'related_count >= 50'
    order:
      - file.name
      - summary
      - domain
      - related_stars
      - related_count
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 完整清单
    order:
      - file.name
      - summary
      - domain
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: table
    name: 按领域分组
    groupBy:
      property: domain
      direction: ASC
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 研究方法
    filters:
      and:
        - 'domain == "research-methodology"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 高等教育
    filters:
      and:
        - 'domain == "higher-education"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 政治经济
    filters:
      and:
        - 'domain == "political-economy-geopolitics"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 教育社会学
    filters:
      and:
        - 'domain == "sociology-of-education"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 政策改革
    filters:
      and:
        - 'domain == "educational-policy-reform"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 比较教育
    filters:
      and:
        - 'domain == "comparative-education"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 教育哲学
    filters:
      and:
        - 'domain == "educational-philosophy"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 学习科学
    filters:
      and:
        - 'domain == "learning-science-cognitive-science"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 中国哲学
    filters:
      and:
        - 'domain == "chinese-philosophy"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: table
    name: 领域 / 教学法
    filters:
      and:
        - 'domain == "instruction-pedagogy"'
    order:
      - file.name
      - summary
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC
```
