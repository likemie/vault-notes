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
  domain:
    displayName: Domain
  related_stars:
    displayName: Links
  related_count:
    displayName: Count
  related_color:
    displayName: Color
  tags:
    displayName: Tags
  updated:
    displayName: Updated

views:
  - type: table
    name: Concepts
    order:
      - file.name
      - domain
      - related_stars
      - related_count
      - tags
      - updated
    sort:
      - property: related_count
        direction: DESC

  - type: cards
    name: Cards
    image: related_color
    order:
      - file.name
      - domain
      - related_stars
      - related_count
    sort:
      - property: related_count
        direction: DESC
```
