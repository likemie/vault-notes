import crypto from 'node:crypto';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import dotenv from 'dotenv';
import { GoogleGenAI } from '@google/genai';

interface SyncRecord {
  hash: string;
  documentName?: string;
  updatedAt: string;
}

interface SyncState {
  storeName: string;
  files: Record<string, SyncRecord>;
}

interface WikiIndexItem {
  title: string;
  type: string;
  path: string;
  aliases?: string[];
}

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
const APP_DIR = path.resolve(__dirname, '..');
const VAULT_ROOT = path.resolve(APP_DIR, '..');
const WIKI_DIR = path.join(VAULT_ROOT, 'wiki');
const SOURCE_INDEX_JSON = path.join(WIKI_DIR, 'index.json');
const BUNDLED_INDEX_JSON = path.join(APP_DIR, 'data', 'wiki-index.json');
const STATE_PATH = path.join(APP_DIR, 'data', 'sync-state.json');

dotenv.config({ path: path.join(APP_DIR, '.env') });

function parseArgs(argv: string[]) {
  const args = {
    dryRun: false,
    reset: false,
    limit: Infinity,
    concurrency: 3,
    storeName: process.env.FILE_SEARCH_STORE_NAME || '',
    displayName: 'mynotes-academic-wiki',
  };

  for (let i = 0; i < argv.length; i++) {
    const token = argv[i];
    if (token === '--dry-run') args.dryRun = true;
    else if (token === '--reset') args.reset = true;
    else if (token === '--limit' && argv[i + 1]) args.limit = Number(argv[++i]);
    else if (token === '--concurrency' && argv[i + 1]) args.concurrency = Math.max(1, Number(argv[++i]));
    else if (token === '--store-name' && argv[i + 1]) args.storeName = argv[++i];
    else if (token === '--display-name' && argv[i + 1]) args.displayName = argv[++i];
  }
  return args;
}

function collectMarkdownFiles(dir: string, out: string[] = []): string[] {
  for (const entry of fs.readdirSync(dir, { withFileTypes: true })) {
    if (entry.name.startsWith('.') || entry.name === 'templates' || entry.name === 'assets') {
      continue;
    }
    const full = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      collectMarkdownFiles(full, out);
    } else if (entry.isFile() && entry.name.toLowerCase().endsWith('.md')) {
      out.push(full);
    }
  }
  return out;
}

function sha256(filePath: string): string {
  const buf = fs.readFileSync(filePath);
  return crypto.createHash('sha256').update(buf).digest('hex');
}

function loadState(storeName: string, reset: boolean): SyncState {
  if (!reset && fs.existsSync(STATE_PATH)) {
    const parsed = JSON.parse(fs.readFileSync(STATE_PATH, 'utf-8')) as SyncState;
    return {
      storeName: storeName || parsed.storeName || '',
      files: parsed.files || {},
    };
  }
  return { storeName, files: {} };
}

function saveState(state: SyncState) {
  fs.mkdirSync(path.dirname(STATE_PATH), { recursive: true });
  fs.writeFileSync(STATE_PATH, JSON.stringify(state, null, 2), 'utf-8');
}

async function main() {
  const opts = parseArgs(process.argv.slice(2));

  if (!fs.existsSync(WIKI_DIR) || !fs.existsSync(SOURCE_INDEX_JSON)) {
    throw new Error(`Cannot find wiki directory or wiki/index.json at ${WIKI_DIR}`);
  }

  // Always refresh qa-app/data/wiki-index.json from vault's wiki/index.json
  fs.mkdirSync(path.dirname(BUNDLED_INDEX_JSON), { recursive: true });
  fs.copyFileSync(SOURCE_INDEX_JSON, BUNDLED_INDEX_JSON);
  console.log(`[sync] Copied ${SOURCE_INDEX_JSON} -> ${BUNDLED_INDEX_JSON}`);

  const indexItems = JSON.parse(fs.readFileSync(SOURCE_INDEX_JSON, 'utf-8')) as WikiIndexItem[];
  const indexByPath = new Map(indexItems.map((item) => [item.path, item]));

  const allMdFiles = collectMarkdownFiles(WIKI_DIR).sort();
  const state = loadState(opts.storeName, opts.reset);

  const currentRelSet = new Set<string>();
  const toUpload: Array<{ relPath: string; fullPath: string; hash: string }> = [];

  for (const fullPath of allMdFiles) {
    const relPath = path.relative(VAULT_ROOT, fullPath).replace(/\\/g, '/');
    currentRelSet.add(relPath);
    const hash = sha256(fullPath);
    if (state.files[relPath]?.hash !== hash) {
      toUpload.push({ relPath, fullPath, hash });
    }
  }

  const toDelete = Object.keys(state.files).filter((relPath) => !currentRelSet.has(relPath));

  console.log(
    `[sync] Scanned ${allMdFiles.length} wiki markdown files: ${toUpload.length} new/changed, ${toDelete.length} deleted.`,
  );

  if (opts.dryRun) {
    console.log('[sync] Dry run enabled. Sample pending uploads:');
    for (const item of toUpload.slice(0, 10)) {
      console.log(`  + ${item.relPath}`);
    }
    return;
  }

  const apiKey = process.env.GEMINI_API_KEY;
  if (!apiKey) {
    throw new Error('Missing GEMINI_API_KEY in qa-app/.env or environment');
  }

  const ai = new GoogleGenAI({ apiKey });

  if (!state.storeName) {
    console.log(`[sync] Creating File Search Store "${opts.displayName}"...`);
    const store = await ai.fileSearchStores.create({
      config: { displayName: opts.displayName },
    });
    if (!store.name) {
      throw new Error('File Search Store creation returned empty store.name');
    }
    state.storeName = store.name;
    saveState(state);
    console.log(`[sync] Created store: ${state.storeName}`);
    console.log(`[sync] Remember to put FILE_SEARCH_STORE_NAME=${state.storeName} in qa-app/.env`);
  }

  // Delete removed files from File Search Store
  for (const relPath of toDelete) {
    const docName = state.files[relPath]?.documentName;
    if (docName) {
      try {
        await ai.fileSearchStores.documents.delete({ name: docName });
        console.log(`[sync] Deleted remote doc: ${relPath}`);
      } catch (err) {
        console.warn(`[sync] Failed to delete ${docName}:`, err instanceof Error ? err.message : err);
      }
    }
    delete state.files[relPath];
    saveState(state);
  }

  const batch = toUpload.slice(0, opts.limit);
  let completed = 0;
  let cursor = 0;

  async function worker() {
    while (cursor < batch.length) {
      const idx = cursor++;
      const item = batch[idx];
      const meta = indexByPath.get(item.relPath);

      // Remove stale remote version before re-uploading changed file
      const prevDoc = state.files[item.relPath]?.documentName;
      if (prevDoc) {
        try {
          await withRetry(() => ai.fileSearchStores.documents.delete({ name: prevDoc }), `delete ${item.relPath}`, 3);
        } catch {
          // Ignore if already absent
        }
      }

      const customMetadata = [
        { key: 'vault_path', stringValue: item.relPath },
        { key: 'type', stringValue: meta?.type ?? inferTypeFromPath(item.relPath) },
        { key: 'title', stringValue: meta?.title ?? path.basename(item.relPath, '.md') },
      ];

      let op = await withRetry(
        () =>
          ai.fileSearchStores.uploadToFileSearchStore({
            fileSearchStoreName: state.storeName,
            file: item.fullPath,
            config: {
              mimeType: 'text/markdown',
              displayName: meta?.title ?? item.relPath,
              customMetadata,
            },
          }),
        `upload ${item.relPath}`,
      );

      while (!op.done) {
        await new Promise((r) => setTimeout(r, 1500));
        op = await withRetry(() => ai.operations.get({ operation: op }), `poll ${item.relPath}`);
      }

      if (op.error) {
        throw new Error(`Upload operation failed for ${item.relPath}: ${JSON.stringify(op.error)}`);
      }

      const docName = normalizeDocumentName(
        op.response?.parent,
        op.response?.documentName,
        state.storeName,
      );
      state.files[item.relPath] = {
        hash: item.hash,
        documentName: docName,
        updatedAt: new Date().toISOString(),
      };
      completed++;
      if (completed % 25 === 0 || completed === batch.length) {
        saveState(state);
        console.log(`[sync] Progress: ${completed}/${batch.length}`);
      }
    }
  }

  const workers = Array.from({ length: opts.concurrency }, () => worker());
  await Promise.all(workers);
  saveState(state);
  console.log(`[sync] Done. Store=${state.storeName}, tracked=${Object.keys(state.files).length} files.`);
}

async function withRetry<T>(fn: () => Promise<T>, label: string, maxAttempts = 5): Promise<T> {
  let delayMs = 2000;
  for (let attempt = 1; attempt <= maxAttempts; attempt++) {
    try {
      return await fn();
    } catch (err) {
      const msg = err instanceof Error ? err.message : String(err);
      const retryable = /429|503|500|rate|quota|ECONNRESET|ETIMEDOUT|fetch failed/i.test(msg);
      if (!retryable || attempt === maxAttempts) {
        throw err;
      }
      console.warn(`[sync] Retry ${attempt}/${maxAttempts} for ${label} after ${delayMs}ms (${msg})`);
      await new Promise((r) => setTimeout(r, delayMs));
      delayMs *= 2;
    }
  }
  throw new Error(`Unreachable retry failure for ${label}`);
}

function normalizeDocumentName(
  parent: string | undefined,
  docName: string | undefined,
  storeName: string,
): string | undefined {
  if (!docName) return undefined;
  if (docName.startsWith('fileSearchStores/')) return docName;
  const baseStore = parent || storeName;
  return `${baseStore}/documents/${docName}`;
}

function inferTypeFromPath(relPath: string): string {
  const seg = relPath.split('/')[1] || '';
  const map: Record<string, string> = {
    concepts: 'concept',
    theories: 'theory',
    arguments: 'argument',
    facts: 'fact',
    methods: 'method',
    instruments: 'instrument',
    persons: 'person',
  };
  return map[seg] ?? 'other';
}

main().catch((err) => {
  console.error('[sync] Fatal:', err);
  process.exit(1);
});
