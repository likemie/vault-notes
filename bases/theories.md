---
title: 理论索引
---

```base
filters:
  and:
    - 'type == "theory"'
    - 'file.folder.contains("wiki/theories")'

properties:
  file.name:
    displayName: Theory
  file.folder:
    displayName: Field
  tags:
    displayName: Tags
  updated:
    displayName: Updated

views:
  - type: table
    name: Theories
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
    name: By Field
    groupBy:
      property: file.folder
      direction: ASC
    order:
      - file.name
      - tags
      - updated
```
