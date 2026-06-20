---
title: 论证索引
---

从这里进入文献论证：先看连接最密的核心论证，再按出版类型、年份和期刊回到具体材料。星级与连接数由 `scripts/vault_index.py` 自动刷新。

```base
filters:
  and:
    - 'type == "argument"'
    - 'file.folder.contains("wiki/arguments")'

properties:
  argument_display_title:
    displayName: 标题
  summary:
    displayName: 摘要
  authors:
    displayName: 作者
  year:
    displayName: 年份
  journal:
    displayName: 期刊
  argument_kind:
    displayName: 类型
  argument_related_stars:
    displayName: 亮度
  argument_related_count:
    displayName: 连接
  argument_related_color:
    displayName: 色带
  updated:
    displayName: 更新

views:
  - type: cards
    name: 论证雷达
    image: argument_related_color
    order:
      - argument_display_title
      - authors
      - year
      - argument_kind
      - argument_related_stars
      - argument_related_count
    sort:
      - property: argument_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: cards
    name: 核心论证
    image: argument_related_color
    filters:
      and:
        - 'argument_related_count >= 30'
    order:
      - argument_display_title
      - authors
      - year
      - argument_kind
      - argument_related_stars
      - argument_related_count
    sort:
      - property: argument_related_count
        direction: DESC

  - type: table
    name: 完整清单
    order:
      - argument_display_title
      - summary
      - authors
      - year
      - argument_kind
      - argument_related_stars
      - argument_related_count
      - journal
      - updated
    sort:
      - property: argument_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: table
    name: 按类型分组
    groupBy:
      property: argument_kind
      direction: ASC
    order:
      - argument_display_title
      - summary
      - authors
      - year
      - argument_related_stars
      - argument_related_count
      - journal
      - updated
    sort:
      - property: argument_related_count
        direction: DESC

  - type: table
    name: 按年份分组
    groupBy:
      property: year
      direction: DESC
    order:
      - argument_display_title
      - summary
      - authors
      - argument_kind
      - argument_related_stars
      - argument_related_count
      - journal
      - updated
    sort:
      - property: argument_related_count
        direction: DESC

  - type: table
    name: 按期刊分组
    groupBy:
      property: journal
      direction: ASC
    order:
      - argument_display_title
      - summary
      - authors
      - year
      - argument_kind
      - argument_related_stars
      - argument_related_count
      - updated
    sort:
      - property: argument_related_count
        direction: DESC
```
