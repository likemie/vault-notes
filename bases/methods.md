---
title: 方法索引
---

从这里进入研究方法：先看连接最密的方法枢纽，再按质性、量化、混合方法分流。

```base
filters:
  and:
    - 'type == "method"'
    - 'file.folder.contains("wiki/methods")'

properties:
  file.name:
    displayName: 方法
  summary:
    displayName: 摘要
  method_type:
    displayName: 类型
  method_family:
    displayName: 路径
  method_related_stars:
    displayName: 亮度
  method_related_count:
    displayName: 连接
  method_related_color:
    displayName: 色带
  tags:
    displayName: 标签
  updated:
    displayName: 更新

views:
  - type: cards
    name: 方法地图
    image: method_related_color
    order:
      - file.name
      - summary
      - method_family
      - method_related_stars
      - method_related_count
    sort:
      - property: method_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: cards
    name: 方法枢纽
    image: method_related_color
    filters:
      and:
        - 'method_related_count >= 20'
    order:
      - file.name
      - summary
      - method_family
      - method_related_stars
      - method_related_count
    sort:
      - property: method_related_count
        direction: DESC

  - type: table
    name: 完整清单
    order:
      - file.name
      - summary
      - method_type
      - method_related_stars
      - method_related_count
      - tags
      - updated
    sort:
      - property: method_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: cards
    name: 质性方法
    image: method_related_color
    filters:
      and:
        - 'method_family == "qualitative"'
    order:
      - file.name
      - summary
      - method_related_stars
      - method_related_count
    sort:
      - property: method_related_count
        direction: DESC

  - type: cards
    name: 量化方法
    image: method_related_color
    filters:
      and:
        - 'method_family == "quantitative"'
    order:
      - file.name
      - summary
      - method_related_stars
      - method_related_count
    sort:
      - property: method_related_count
        direction: DESC

  - type: cards
    name: 混合方法
    image: method_related_color
    filters:
      and:
        - 'method_family == "mixed"'
    order:
      - file.name
      - summary
      - method_related_stars
      - method_related_count
    sort:
      - property: method_related_count
        direction: DESC

  - type: table
    name: 按路径分组
    groupBy:
      property: method_family
      direction: ASC
    order:
      - file.name
      - summary
      - method_related_stars
      - method_related_count
      - tags
      - updated
    sort:
      - property: method_related_count
        direction: DESC
```
