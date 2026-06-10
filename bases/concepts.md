---
title: 概念索引
---

```base
filters:
  and:
    - 'type == "concept"'
    - 'file.folder.contains("wiki/concepts")'

properties:
  file.name:
    displayName: Concept
  status:
    displayName: Status
  confidence:
    displayName: Confidence
  tags:
    displayName: Tags
  updated:
    displayName: Updated

views:
  - type: table
    name: Concepts
    order:
      - file.name
      - status
      - confidence
      - tags
      - updated
    sort:
      - property: file.name
        direction: ASC

  - type: cards
    name: Cards
    order:
      - file.name
      - status
      - confidence
```
