---
title: 事实索引
---

从这里进入政策、事件、组织与制度场景：先看连接最密的事实枢纽，再按地区和事实类型分流。

```base
filters:
  and:
    - 'type == "fact"'
    - 'file.folder.contains("wiki/facts")'

properties:
  file.name:
    displayName: 事实
  summary:
    displayName: 摘要
  fact_region:
    displayName: 地区
  fact_kind:
    displayName: 类型
  fact_related_stars:
    displayName: 亮度
  fact_related_count:
    displayName: 连接
  fact_related_color:
    displayName: 色带
  tags:
    displayName: 标签
  updated:
    displayName: 更新

views:
  - type: cards
    name: 事实图谱
    image: fact_related_color
    order:
      - file.name
      - summary
      - fact_region
      - fact_kind
      - fact_related_stars
      - fact_related_count
    sort:
      - property: fact_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: cards
    name: 事实枢纽
    image: fact_related_color
    filters:
      and:
        - 'fact_related_count >= 20'
    order:
      - file.name
      - summary
      - fact_region
      - fact_kind
      - fact_related_stars
      - fact_related_count
    sort:
      - property: fact_related_count
        direction: DESC

  - type: table
    name: 完整清单
    order:
      - file.name
      - summary
      - fact_region
      - fact_kind
      - fact_related_stars
      - fact_related_count
      - tags
      - updated
    sort:
      - property: fact_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: table
    name: 按地区分组
    groupBy:
      property: fact_region
      direction: ASC
    order:
      - file.name
      - summary
      - fact_kind
      - fact_related_stars
      - fact_related_count
      - tags
      - updated
    sort:
      - property: fact_related_count
        direction: DESC

  - type: table
    name: 按类型分组
    groupBy:
      property: fact_kind
      direction: ASC
    order:
      - file.name
      - summary
      - fact_region
      - fact_related_stars
      - fact_related_count
      - tags
      - updated
    sort:
      - property: fact_related_count
        direction: DESC

  - type: table
    name: 证据线索
    filters:
      and:
        - 'tags.contains("theme/evidence-based-education") || tags.contains("evidence-based-reform") || tags.contains("evidence-standards")'
    order:
      - file.name
      - summary
      - fact_region
      - fact_kind
      - fact_related_stars
      - fact_related_count
      - tags
      - updated
    sort:
      - property: fact_related_count
        direction: DESC
```
