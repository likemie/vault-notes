import test from 'node:test';
import assert from 'node:assert/strict';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import {
  buildQuartzUrl,
  getIndexStats,
  loadWikiIndex,
  resolveIndexPath,
  searchWikiIndex,
} from './wikiIndex.ts';

const __filename = fileURLToPath(import.meta.url);
const APP_DIR = path.resolve(path.dirname(__filename), '..');

test('loads bundled wiki-index.json and computes stats', () => {
  const indexPath = resolveIndexPath(APP_DIR);
  const entries = loadWikiIndex(indexPath);
  assert.ok(entries.length > 5000, `Expected >5000 entries, got ${entries.length}`);
  const stats = getIndexStats(entries);
  assert.ok(stats.concept > 0);
  assert.ok(stats.argument > 0);
});

test('searchWikiIndex matches English title, Chinese alias, and type filter', () => {
  const sample = [
    {
      title: 'Recontextualization',
      type: 'concept',
      path: 'wiki/concepts/sociology-of-education/Recontextualization.md',
      aliases: ['再情境化', 'recontextualisation'],
    },
    {
      title: 'APA Style',
      type: 'concept',
      path: 'wiki/concepts/academic-writing/APA Style.md',
      aliases: ['美国心理学会出版手册'],
    },
    {
      title: 'Bernstein_2000_Pedagogy',
      type: 'argument',
      path: 'wiki/arguments/books/Bernstein_2000_Pedagogy.md',
      aliases: ['再情境化规则'],
    },
  ];

  const byAlias = searchWikiIndex(sample, { query: '再情境化' });
  assert.equal(byAlias[0].title, 'Recontextualization');

  const onlyArgs = searchWikiIndex(sample, { query: '再情境化', type: 'argument' });
  assert.equal(onlyArgs.length, 1);
  assert.equal(onlyArgs[0].type, 'argument');
});

test('buildQuartzUrl encodes path cleanly', () => {
  const url = buildQuartzUrl(
    'wiki/concepts/academic-writing/APA Style.md',
    'https://likemie.github.io/',
  );
  assert.equal(url, 'https://likemie.github.io/wiki/concepts/academic-writing/APA-Style');
});
