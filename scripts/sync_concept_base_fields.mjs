import fs from "node:fs"
import path from "node:path"
import { fileURLToPath } from "node:url"
import YAML from "/Users/shaoyangwu/quartz/node_modules/yaml/dist/index.js"

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "..")
const conceptsDir = path.join(root, "wiki", "concepts")

const generatedKeys = ["domain", "related_count", "related_level", "related_stars", "related_color"]

const colors = [
  "#e5e7eb",
  "#bfdbfe",
  "#99f6e4",
  "#fde68a",
  "#fdba74",
  "#fecdd3",
  "#ddd6fe",
]

function walk(dir) {
  const entries = fs.readdirSync(dir, { withFileTypes: true })
  return entries.flatMap((entry) => {
    const fullPath = path.join(dir, entry.name)
    if (entry.isDirectory()) return walk(fullPath)
    return entry.isFile() && entry.name.endsWith(".md") ? [fullPath] : []
  })
}

function splitFrontmatter(content) {
  if (!content.startsWith("---\n")) return null
  const end = content.indexOf("\n---", 4)
  if (end === -1) return null
  return {
    yaml: content.slice(4, end),
    body: content.slice(end + 1),
  }
}

function countRelated(data) {
  return Object.entries(data)
    .filter(([key]) => key.startsWith("related_") && !generatedKeys.includes(key))
    .reduce((total, [, value]) => {
      if (Array.isArray(value)) return total + value.filter((item) => item != null && String(item).trim() !== "").length
      if (value == null) return total
      if (typeof value === "string") return total + (value.trim() === "" ? 0 : 1)
      return total + 1
    }, 0)
}

function starsFor(count) {
  if (count <= 5) return { level: 0, stars: "☆" }
  if (count > 50) return { level: 6, stars: "★★★★★★" }
  const level = Math.min(5, Math.ceil((count - 5) / 5))
  return { level, stars: "★".repeat(level) }
}

function quoteYamlString(value) {
  return JSON.stringify(value)
}

function upsertGeneratedFields(yamlText, fields) {
  const lines = yamlText.replace(/\n+$/, "").split("\n")
  const filtered = []

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i]
    const match = /^([A-Za-z0-9_-]+):/.exec(line)
    if (match && generatedKeys.includes(match[1])) {
      while (i + 1 < lines.length && /^(?:\s+|-\s)/.test(lines[i + 1])) i++
      continue
    }
    filtered.push(line)
  }

  const insertAt = Math.max(
    filtered.findIndex((line) => /^type:\s*/.test(line)) + 1,
    0,
  )
  const generated = [
    `domain: ${quoteYamlString(fields.domain)}`,
    `related_count: ${fields.related_count}`,
    `related_level: ${fields.related_level}`,
    `related_stars: ${quoteYamlString(fields.related_stars)}`,
    `related_color: ${quoteYamlString(fields.related_color)}`,
  ]

  filtered.splice(insertAt, 0, ...generated)
  return `${filtered.join("\n")}\n`
}

let changed = 0
const summaries = []

for (const file of walk(conceptsDir)) {
  const rel = path.relative(root, file)
  const parts = rel.split(path.sep)
  const domain = parts[2]
  const content = fs.readFileSync(file, "utf8")
  const frontmatter = splitFrontmatter(content)
  if (!frontmatter) continue

  const data = YAML.parse(frontmatter.yaml) ?? {}
  if (data.type !== "concept") continue

  const related_count = countRelated(data)
  const { level: related_level, stars: related_stars } = starsFor(related_count)
  const related_color = colors[related_level]
  const nextYaml = upsertGeneratedFields(frontmatter.yaml, {
    domain,
    related_count,
    related_level,
    related_stars,
    related_color,
  })
  const nextContent = `---\n${nextYaml}${frontmatter.body}`

  if (nextContent !== content) {
    fs.writeFileSync(file, nextContent)
    changed++
  }

  summaries.push({ rel, domain, related_count, related_stars })
}

summaries.sort((a, b) => b.related_count - a.related_count)

console.log(`Updated ${changed} concept files.`)
for (const item of summaries.slice(0, 10)) {
  console.log(`${item.related_count.toString().padStart(3)} ${item.related_stars.padEnd(5)} ${item.domain} / ${path.basename(item.rel, ".md")}`)
}
