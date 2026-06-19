---
title: 事实索引
---

```base
filters:
  and:
    - 'type == "fact"'
    - 'file.folder.contains("wiki/facts")'

properties:
  file.name:
    displayName: Fact
  file.folder:
    displayName: Context
  tags:
    displayName: Tags
  updated:
    displayName: Updated

views:
  - type: table
    name: Facts
    order:
      - file.name
      - file.folder
      - tags
      - updated
    sort:
      - property: updated
        direction: DESC

  - type: cards
    name: Cards
    order:
      - file.name
      - file.folder
      - updated
    sort:
      - property: updated
        direction: DESC

  - type: table
    name: By Context
    groupBy:
      property: file.folder
      direction: ASC
    order:
      - file.name
      - tags
      - updated
```
