---
title: 人物索引
---

```base
filters:
  and:
    - 'type == "person"'
    - 'file.folder.contains("wiki/persons")'

properties:
  file.name:
    displayName: Person
  file.folder:
    displayName: Region
  tags:
    displayName: Tags
  updated:
    displayName: Updated

views:
  - type: table
    name: Persons
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
    name: By Region
    groupBy:
      property: file.folder
      direction: ASC
    order:
      - file.name
      - tags
      - updated
```
