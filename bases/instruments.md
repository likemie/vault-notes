---
title: 测量工具索引
---

从这里进入测量工具库：先看全部工具，再按测验、量表、问卷以及观察、访谈与量规分流。

```base
filters:
  and:
    - 'type == "instrument"'
    - 'file.folder.contains("wiki/instruments")'

properties:
  file.name:
    displayName: 工具
  summary:
    displayName: 摘要
  instrument_type:
    displayName: 类型
  developers:
    displayName: 开发者
  original_year:
    displayName: 年份
  item_count:
    displayName: 题项
  administration_mode:
    displayName: 施测方式
  response_format:
    displayName: 作答格式
  languages:
    displayName: 语言
  status:
    displayName: 状态
  tags:
    displayName: 标签
  updated:
    displayName: 更新

views:
  - type: cards
    name: 工具总览
    order:
      - file.name
      - summary
      - instrument_type
      - developers
      - original_year
    sort:
      - property: updated
        direction: DESC

  - type: table
    name: 完整清单
    order:
      - file.name
      - summary
      - instrument_type
      - developers
      - original_year
      - item_count
      - administration_mode
      - response_format
      - languages
      - status
      - tags
      - updated
    sort:
      - property: instrument_type
        direction: ASC
      - property: updated
        direction: DESC

  - type: cards
    name: 测验
    filters:
      and:
        - 'instrument_type == "test"'
    order:
      - file.name
      - summary
      - developers
      - original_year
      - item_count
    sort:
      - property: updated
        direction: DESC

  - type: cards
    name: 量表、问卷与清单
    filters:
      or:
        - 'instrument_type == "scale"'
        - 'instrument_type == "questionnaire"'
        - 'instrument_type == "inventory"'
    order:
      - file.name
      - summary
      - instrument_type
      - developers
      - item_count
    sort:
      - property: instrument_type
        direction: ASC
      - property: updated
        direction: DESC

  - type: table
    name: 观察、访谈与量规
    filters:
      or:
        - 'instrument_type == "observation-tool"'
        - 'instrument_type == "interview-tool"'
        - 'instrument_type == "rubric"'
    order:
      - file.name
      - summary
      - instrument_type
      - developers
      - administration_mode
      - status
      - updated
    sort:
      - property: instrument_type
        direction: ASC
      - property: updated
        direction: DESC

  - type: table
    name: 按类型分组
    groupBy:
      property: instrument_type
      direction: ASC
    order:
      - file.name
      - summary
      - developers
      - original_year
      - item_count
      - status
      - updated
    sort:
      - property: updated
        direction: DESC
```
