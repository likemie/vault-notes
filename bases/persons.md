---
title: 人物索引
---

从这里进入人物网络：先看连接最密的理论家、研究者与政策行动者，再按地区分流。

```base
filters:
  and:
    - 'type == "person"'
    - 'file.folder.contains("wiki/persons")'

properties:
  file.name:
    displayName: 人物
  summary:
    displayName: 摘要
  person_region:
    displayName: 地区
  person_related_stars:
    displayName: 亮度
  person_related_count:
    displayName: 连接
  person_related_color:
    displayName: 色带
  tags:
    displayName: 标签
  updated:
    displayName: 更新

views:
  - type: cards
    name: 人物图谱
    image: person_related_color
    order:
      - file.name
      - summary
      - person_region
      - person_related_stars
      - person_related_count
    sort:
      - property: person_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: cards
    name: 人物枢纽
    image: person_related_color
    filters:
      and:
        - 'person_related_count >= 20'
    order:
      - file.name
      - summary
      - person_region
      - person_related_stars
      - person_related_count
    sort:
      - property: person_related_count
        direction: DESC

  - type: table
    name: 完整清单
    order:
      - file.name
      - summary
      - person_region
      - person_related_stars
      - person_related_count
      - tags
      - updated
    sort:
      - property: person_related_count
        direction: DESC
      - property: updated
        direction: DESC

  - type: table
    name: 按地区分组
    groupBy:
      property: person_region
      direction: ASC
    order:
      - file.name
      - summary
      - person_related_stars
      - person_related_count
      - tags
      - updated
    sort:
      - property: person_related_count
        direction: DESC

  - type: table
    name: 地区 / 英国
    filters:
      and:
        - 'person_region == "uk" || person_region == "UK"'
    order:
      - file.name
      - summary
      - person_related_stars
      - person_related_count
      - tags
      - updated
    sort:
      - property: person_related_count
        direction: DESC

  - type: table
    name: 地区 / 美国
    filters:
      and:
        - 'person_region == "us" || person_region == "US" || person_region == "usa" || person_region == "USA" || person_region == "united-states"'
    order:
      - file.name
      - summary
      - person_related_stars
      - person_related_count
      - tags
      - updated
    sort:
      - property: person_related_count
        direction: DESC

  - type: table
    name: 地区 / 中国
    filters:
      and:
        - 'person_region == "china" || person_region == "China"'
    order:
      - file.name
      - summary
      - person_related_stars
      - person_related_count
      - tags
      - updated
    sort:
      - property: person_related_count
        direction: DESC

  - type: table
    name: 地区 / 德法
    filters:
      and:
        - 'person_region == "germany" || person_region == "Germany" || person_region == "德国" || person_region == "france" || person_region == "France"'
    order:
      - file.name
      - summary
      - person_related_stars
      - person_related_count
      - tags
      - updated
    sort:
      - property: person_related_count
        direction: DESC

  - type: table
    name: 地区 / 澳新加
    filters:
      and:
        - 'person_region == "australia" || person_region == "new-zealand" || person_region == "New Zealand" || person_region == "newzealand" || person_region == "canada"'
    order:
      - file.name
      - summary
      - person_related_stars
      - person_related_count
      - tags
      - updated
    sort:
      - property: person_related_count
        direction: DESC
```
