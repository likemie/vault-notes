import test from 'node:test';
import assert from 'node:assert/strict';
import { compactMessagesForStorage, selectIdsToPrune } from './conversations.ts';

test('compactMessagesForStorage drops bulky alias arrays and truncates snippets', () => {
  const input = [
    {
      id: 'm1',
      role: 'model',
      text: 'Answer text',
      indexMatches: [
        {
          title: 'Recontextualization',
          type: 'concept',
          path: 'wiki/concepts/Recontextualization.md',
          aliases: ['a1', 'a2', 'a3', 'a4'],
          score: 110,
        },
      ],
      citations: [
        {
          title: 'Doc 1',
          entryPath: 'wiki/concepts/Doc1.md',
          textSnippet: 'x'.repeat(300),
        },
      ],
    },
  ];

  const out = compactMessagesForStorage(input);
  const match = out[0].indexMatches[0];
  const citation = out[0].citations[0];
  assert.equal('aliases' in match, false);
  assert.equal(citation.textSnippet.length, 120);
});

test('selectIdsToPrune enforces both maxCount and maxBytes budget', () => {
  const docs = [
    { id: 'c1', approxBytes: 300 },
    { id: 'c2', approxBytes: 300 },
    { id: 'c3', approxBytes: 300 },
    { id: 'c4', approxBytes: 300 },
  ];

  assert.deepEqual(selectIdsToPrune(docs, 3, 10000), ['c4']);
  assert.deepEqual(selectIdsToPrune(docs, 10, 650), ['c3', 'c4']);
});
