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
  subtype:
    displayName: Type
  region:
    displayName: Region
  summary:
    displayName: Why it matters
  file.folder:
    displayName: Context
  status:
    displayName: Status
  tags:
    displayName: Tags
  updated:
    displayName: Updated

views:
  - type: table
    name: Map
    order:
      - file.name
      - subtype
      - region
      - summary
      - file.folder
      - updated
    sort:
      - property: updated
        direction: DESC

  - type: cards
    name: Cards
    order:
      - file.name
      - subtype
      - region
      - summary
      - status
    sort:
      - property: updated
        direction: DESC

  - type: table
    name: By Region
    groupBy:
      property: region
      direction: ASC
    order:
      - file.name
      - subtype
      - summary
      - tags
      - updated
    sort:
      - property: region
        direction: ASC
      - property: updated
        direction: DESC

  - type: table
    name: By Type
    groupBy:
      property: subtype
      direction: ASC
    order:
      - file.name
      - region
      - summary
      - tags
      - updated
    sort:
      - property: subtype
        direction: ASC
      - property: updated
        direction: DESC

  - type: table
    name: Policies
    filters:
      and:
        - 'subtype == "policy"'
    order:
      - file.name
      - region
      - summary
      - tags
      - updated
    sort:
      - property: region
        direction: ASC
      - property: updated
        direction: DESC

  - type: table
    name: Organizations
    filters:
      and:
        - 'subtype == "organization"'
    order:
      - file.name
      - region
      - summary
      - tags
      - updated
    sort:
      - property: region
        direction: ASC
      - property: updated
        direction: DESC

  - type: table
    name: Events
    filters:
      and:
        - 'subtype == "event"'
    order:
      - file.name
      - region
      - summary
      - tags
      - updated
    sort:
      - property: region
        direction: ASC
      - property: updated
        direction: DESC

  - type: table
    name: Evidence Trail
    filters:
      and:
        - 'tags.contains("theme/evidence-based-education") || tags.contains("evidence-based-reform") || tags.contains("evidence-standards")'
    order:
      - file.name
      - subtype
      - region
      - summary
      - tags
      - updated
    sort:
      - property: updated
        direction: DESC
```
