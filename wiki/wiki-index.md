# Wiki Index

> 本页由 Dataview 自动生成索引。  
> 不再手动维护全量条目清单。新建或修改条目后，Dataview 会根据 frontmatter 自动刷新。

---

## 最近更新

```dataview
TABLE type, subtype, status, confidence, file.folder
FROM "wiki"
WHERE file.name != "index"
  AND !contains(file.folder, "templates")
  AND !contains(file.folder, "indexes")
SORT file.mtime DESC
LIMIT 30
```

---

## 草稿条目

```dataview
TABLE type, subtype, aliases, tags, sources
FROM "wiki"
WHERE status = "draft"
  AND file.name != "index"
  AND !contains(file.folder, "templates")
  AND !contains(file.folder, "indexes")
SORT file.mtime DESC
```

---

## Concepts

```dataview
TABLE aliases, tags, related_theories, related_persons, confidence, status
FROM "wiki"
WHERE type = "concept"
SORT file.name ASC
```

---

## Theories

```dataview
TABLE aliases, tags, related_concepts, related_persons, related_methods, confidence, status
FROM "wiki"
WHERE type = "theory"
SORT file.name ASC
```

---

## Methods

```dataview
TABLE aliases, tags, related_theories, related_concepts, confidence, status
FROM "wiki"
WHERE type = "method"
SORT file.name ASC
```

---

## Persons

```dataview
TABLE aliases, tags, related_theories, related_concepts, related_methods, confidence, status
FROM "wiki"
WHERE type = "person"
SORT file.name ASC
```

---

## Facts

```dataview
TABLE subtype, aliases, tags, related_concepts, related_theories, related_persons, confidence, status
FROM "wiki"
WHERE type = "fact"
SORT subtype ASC, file.name ASC
```

---

## Arguments

```dataview
TABLE subtype, citation, tags, related_concepts, related_theories, related_methods, sources, status
FROM "wiki"
WHERE type = "argument"
SORT file.name ASC
```

---

## By Status

### Draft

```dataview
LIST
FROM "wiki"
WHERE status = "draft"
  AND file.name != "index"
  AND !contains(file.folder, "templates")
  AND !contains(file.folder, "indexes")
SORT file.name ASC
```

### Review

```dataview
LIST
FROM "wiki"
WHERE status = "review"
  AND file.name != "index"
  AND !contains(file.folder, "templates")
  AND !contains(file.folder, "indexes")
SORT file.name ASC
```

### Published

```dataview
LIST
FROM "wiki"
WHERE status = "published"
  AND file.name != "index"
  AND !contains(file.folder, "templates")
  AND !contains(file.folder, "indexes")
SORT file.name ASC
```

---

## By Type

```dataview
TABLE rows.file.link AS Entries
FROM "wiki"
WHERE type
  AND file.name != "index"
  AND !contains(file.folder, "templates")
  AND !contains(file.folder, "indexes")
GROUP BY type
SORT type ASC
```

---

## Without Status

```dataview
TABLE type, subtype, tags, file.folder
FROM "wiki"
WHERE !status
  AND file.name != "index"
  AND !contains(file.folder, "templates")
  AND !contains(file.folder, "indexes")
SORT file.folder ASC, file.name ASC
```

---

## Without Sources

```dataview
TABLE type, subtype, tags, status
FROM "wiki"
WHERE !sources
  AND file.name != "index"
  AND !contains(file.folder, "templates")
  AND !contains(file.folder, "indexes")
SORT type ASC, file.name ASC
```
