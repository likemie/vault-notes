---
title: 论证索引
---

```base
filters:
  and:
    - 'type == "argument"'
    - 'file.folder.contains("wiki/arguments")'

properties:
  file.name:
    displayName: Argument
  authors:
    displayName: Authors
  year:
    displayName: Year
  journal:
    displayName: Journal
  file.folder:
    displayName: Source
  updated:
    displayName: Updated

views:
  - type: table
    name: Arguments
    order:
      - file.name
      - authors
      - year
      - journal
      - file.folder
      - updated
    sort:
      - property: updated
        direction: DESC

  - type: cards
    name: Cards
    order:
      - file.name
      - authors
      - year
      - journal
    sort:
      - property: updated
        direction: DESC

  - type: table
    name: By Year
    groupBy:
      property: year
      direction: DESC
    order:
      - file.name
      - authors
      - journal
      - updated

  - type: table
    name: By Journal
    groupBy:
      property: journal
      direction: ASC
    order:
      - file.name
      - authors
      - year
      - updated
```
