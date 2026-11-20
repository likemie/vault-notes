const { deepEqual, equal } = require("node:assert/strict");
const { test } = require("node:test");
const { transformSync } = require("esbuild");
const { readFileSync } = require("node:fs");
const { join } = require("node:path");

function importPureModule(filename) {
  const input = readFileSync(join(__dirname, filename), "utf8");
  const { code } = transformSync(input, { loader: "ts", format: "cjs" });
  const module = { exports: {} };
  new Function("module", code)(module);
  return module.exports;
}

const { TitleIndex } = importPureModule("../src/title-index.ts");
const { searchTitles, titleRange } = importPureModule("../src/search.ts");

test("matches the uninterrupted title case-insensitively and ranks complete titles first", () => {
  const index = new TitleIndex();
  index.set("notes/new.md", 8, { title: "芬兰教育改革" });
  index.set("notes/exact.md", 2, { title: "芬兰教育" });
  index.set("notes/spaced.md", 100, { title: "芬兰 教育" });
  index.set("notes/another.md", 100, { title: "芬兰的教育" });
  index.set("notes/english.md", 1, { title: "Case Study" });
  index.set("notes/芬兰教育.md", 100, { title: "Other" });
  equal(searchTitles(index.entries(), "   ", false).total, 0);
  deepEqual(searchTitles(index.entries(), " 芬兰教育 ", false).rows.map(r => r.entry.path), ["notes/exact.md", "notes/new.md"]);
  deepEqual(searchTitles(index.entries(), "芬兰 教育", false).rows.map(r => r.entry.path), ["notes/spaced.md"]);
  equal(searchTitles(index.entries(), "cAsE StUDy", false).rows[0].tier, 0);
});

test("aliases are opt-in, only whole aliases match, and invalid titles are omitted", () => {
  const index = new TitleIndex();
  index.set("notes/fact.md", 3, { title: "Knowledge Diplomacy", aliases: ["知识外交", "KD"] });
  index.set("notes/invalid.md", 5, { title: [1], aliases: "知识外交" });
  index.set("notes/alias-only.md", 5, { aliases: "知识外交" });
  equal(searchTitles(index.entries(), "知识外交", false).total, 0);
  equal(searchTitles(index.entries(), "知识外", true).total, 0);
  equal(searchTitles(index.entries(), " kd ", true).rows[0].alias, "KD");
  equal(searchTitles(index.entries(), "知识外交", true).total, 1);
});

test("updates, renames, and folder removal keep the index current and cap rendered hits", () => {
  const index = new TitleIndex();
  for (let i = 0; i < 35; i++) index.set("notes/Case " + i + ".md", i, { title: "Case " + i });
  const broad = searchTitles(index.entries(), "case", false);
  equal(broad.total, 35);
  equal(broad.rows.length, 30);
  equal(broad.rows[0].entry.title, "Case 34");
  index.move("notes/Case 34.md", "archive/saved.md", 36);
  equal(searchTitles(index.entries(), "Case 34", false).rows[0].entry.path, "archive/saved.md");
  index.set("archive/saved.md", 37, { title: "Renamed title" });
  index.remove("notes", true);
  equal(searchTitles(index.entries(), "case", false).total, 0);
  equal(searchTitles(index.entries(), "renamed", false).total, 1);
});

test("highlights displayed character boundaries when lowercasing expands a letter", () => {
  const title = "İstanbul";
  const folded = title.toLowerCase();
  deepEqual(titleRange(title, folded, 0, 2), [0, 1]);
  deepEqual(titleRange(title, folded, folded.indexOf("stan"), 4), [1, 5]);
});

test("excludes backup folders from title and alias search and removes notes moved into them", () => {
  const index = new TitleIndex();
  const properties = { title: "Knowledge Diplomacy", aliases: ["知识外交"] };
  const original = "wiki/Knowledge Diplomacy.md";
  const backup = "tmp/proposition-migration/backup/wiki/Knowledge Diplomacy.md";
  index.set(original, 1, properties);
  index.set(backup, 2, properties);
  index.set("tmp/callout-design-backup-v4/Knowledge Diplomacy.md", 3, properties);
  index.set("Backups/Knowledge Diplomacy.md", 3, properties);
  index.set("备份/Knowledge Diplomacy.md", 3, properties);
  equal(searchTitles(index.entries(), "Knowledge Diplomacy", false).total, 1);
  equal(searchTitles(index.entries(), "知识外交", true).rows[0].entry.path, original);
  equal(searchTitles(index.entries(), "知识外交", true).total, 1);
  equal(index.move(original, backup, 4), true);
  equal(searchTitles(index.entries(), "Knowledge Diplomacy", false).total, 0);
  index.set("wiki/backup policy.md", 5, { title: "Backup policy" });
  equal(searchTitles(index.entries(), "backup policy", false).total, 1);
});
