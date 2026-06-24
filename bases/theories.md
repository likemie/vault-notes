---
title: 理论索引
---

从这里进入理论谱系：先看连接最密的理论枢纽，再按研究领域分流。

```base
filters:
  and:
    - 'type == "theory"'
    - 'file.folder.contains("wiki/theories")'

properties:
  file.name:
    displayName: 理论
  summary:
    displayName: 摘要
  theory_field:
    displayName: 领域
  theory_related_stars:
    displayName: 亮度
  theory_related_count:
    displayName: 连接
  theory_related_color:
    displayName: 色带
  tags:
    displayName: 标签
  updated:
    displayName: 更新

views:
  - type: cards
    name: 理论谱系
    image: theory_related_color
    order:
      - file.name
      - summary
      - theory_field
      - theory_related_stars
      - theory_related_count
    sort:
      - property: theory_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: cards
    name: 理论枢纽
    image: theory_related_color
    filters:
      and:
        - 'theory_related_count >= 20'
    order:
      - file.name
      - summary
      - theory_field
      - theory_related_stars
      - theory_related_count
    sort:
      - property: theory_related_count
        direction: DESC

  - type: table
    name: 完整清单
    order:
      - file.name
      - summary
      - theory_field
      - theory_related_stars
      - theory_related_count
      - tags
      - updated
    sort:
      - property: theory_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: table
    name: 按领域分组
    groupBy:
      property: theory_field
      direction: ASC
    order:
      - file.name
      - summary
      - theory_related_stars
      - theory_related_count
      - tags
      - updated
    sort:
      - property: theory_related_count
        direction: DESC

  - type: table
    name: 领域 / 教育哲学
    filters:
      and:
        - 'theory_field == "educational-philosophy"'
    order:
      - file.name
      - summary
      - theory_related_stars
      - theory_related_count
      - tags
      - updated
    sort:
      - property: theory_related_count
        direction: DESC

  - type: table
    name: 领域 / 教育社会学
    filters:
      and:
        - 'theory_field == "sociology-of-education"'
    order:
      - file.name
      - summary
      - theory_related_stars
      - theory_related_count
      - tags
      - updated
    sort:
      - property: theory_related_count
        direction: DESC

  - type: table
    name: 领域 / 研究方法
    filters:
      and:
        - 'theory_field == "research-methodology"'
    order:
      - file.name
      - summary
      - theory_related_stars
      - theory_related_count
      - tags
      - updated
    sort:
      - property: theory_related_count
        direction: DESC

  - type: table
    name: 领域 / 高等教育
    filters:
      and:
        - 'theory_field == "higher-education"'
    order:
      - file.name
      - summary
      - theory_related_stars
      - theory_related_count
      - tags
      - updated
    sort:
      - property: theory_related_count
        direction: DESC

  - type: table
    name: 领域 / 政治经济
    filters:
      and:
        - 'theory_field == "political-economy-geopolitics"'
    order:
      - file.name
      - summary
      - theory_related_stars
      - theory_related_count
      - tags
      - updated
    sort:
      - property: theory_related_count
        direction: DESC

  - type: table
    name: 领域 / 学习科学
    filters:
      and:
        - 'theory_field == "learning-science-cognitive-science"'
    order:
      - file.name
      - summary
      - theory_related_stars
      - theory_related_count
      - tags
      - updated
    sort:
      - property: theory_related_count
        direction: DESC

  - type: table
    name: 领域 / 比较教育
    filters:
      and:
        - 'theory_field == "comparative-education"'
    order:
      - file.name
      - summary
      - theory_related_stars
      - theory_related_count
      - tags
      - updated
    sort:
      - property: theory_related_count
        direction: DESC
```
