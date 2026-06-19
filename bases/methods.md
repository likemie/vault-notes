---
title: 方法索引
---

```base
filters:
  and:
    - 'type == "method"'
    - 'file.folder.contains("wiki/methods")'

properties:
  file.name:
    displayName: Method
  method_type:
    displayName: Type
  file.folder:
    displayName: Folder
  tags:
    displayName: Tags
  updated:
    displayName: Updated

views:
  - type: table
    name: Methods
    order:
      - file.name
      - method_type
      - file.folder
      - tags
      - updated
    sort:
      - property: method_type
        direction: ASC
      - property: updated
        direction: DESC

  - type: cards
    name: Cards
    order:
      - file.name
      - method_type
      - updated
    sort:
      - property: updated
        direction: DESC

  - type: table
    name: By Type
    groupBy:
      property: method_type
      direction: ASC
    order:
      - file.name
      - file.folder
      - tags
      - updated
```
