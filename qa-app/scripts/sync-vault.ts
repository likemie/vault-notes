import { execFileSync } from 'node:child_process';
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
const APP_CONFIG_JSON = path.join(APP_DIR, 'data', 'app-config.json');
const STATE_PATH = path.join(APP_DIR, 'data', 'sync-state.json');

dotenv.config({ path: path.join(APP_DIR, '.env') });

function readDefaultStoreName(): string {
  if (process.env.FILE_SEARCH_STORE_NAME) {
    return process.env.FILE_SEARCH_STORE_NAME;
  }
  if (fs.existsSync(APP_CONFIG_JSON)) {
    try {
      const cfg = JSON.parse(fs.readFileSync(APP_CONFIG_JSON, 'utf-8')) as {
        fileSearchStoreName?: string;
      };
      if (cfg.fileSearchStoreName) return cfg.fileSearchStoreName;
    } catch {
      // Ignore malformed config
    }
  }
  return '';
}

function parseArgs(argv: string[]) {
  const args = {
    dryRun: false,
    reset: false,
    limit: Infinity,
    concurrency: 3,
    match: '',
    gitBase: '',
    gitHead: 'HEAD',
    storeName: readDefaultStoreName(),
    displayName: 'mynotes-academic-wiki',
  };

  for (let i = 0; i < argv.length; i++) {
    const token = argv[i];
    if (token === '--dry-run') args.dryRun = true;
    else if (token === '--reset') args.reset = true;
    else if (token === '--limit' && argv[i + 1]) args.limit = Number(argv[++i]);
    else if (token === '--concurrency' && argv[i + 1]) args.concurrency = Math.max(1, Number(argv[++i]));
    else if (token === '--match' && argv[i + 1]) args.match = argv[++i];
    else if (token === '--git-diff' && argv[i + 1]) {
      args.gitBase = argv[++i];
      if (argv[i + 1] && !argv[i + 1].startsWith('--')) {
        args.gitHead = argv[++i];
      }
    }
    else if (token === '--store-name' && argv[i + 1]) args.storeName = argv[++i];
    else if (token === '--display-name' && argv[i + 1]) args.displayName = argv[++i];
  }
  return args;
}

function isSyncableWikiMarkdown(relPath: string): boolean {
  const norm = relPath.replace(/\\/g, '/');
  if (!norm.startsWith('wiki/') || !norm.toLowerCase().endsWith('.md')) return false;
  const parts = norm.split('/');
  return !parts.some((p) => p.startsWith('.') || p === 'templates' || p === 'assets');
}

function getGitDiffChanges(baseSha: string, headSha: string): {
  toUploadPaths: string[];
  toReplacePaths: Set<string>;
  toDeletePaths: string[];
} {
  const raw = execFileSync(
    'git',
    ['-C', VAULT_ROOT, '-c', 'core.quotepath=false', 'diff', '--name-status', '-z', baseSha, headSha, '--', 'wiki'],
    { encoding: 'utf8', maxBuffer: 32 * 1024 * 1024 },
  );

  const tokens = raw.split('\0').filter(Boolean);
  const uploadSet = new Set<string>();
  const replaceSet = new Set<string>();
  const deleteSet = new Set<string>();

  for (let i = 0; i < tokens.length; i++) {
    const status = tokens[i];
    if (status.startsWith('R') || status.startsWith('C')) {
      const oldPath = tokens[++i] ?? '';
      const newPath = tokens[++i] ?? '';
      if (status.startsWith('R') && isSyncableWikiMarkdown(oldPath)) {
        deleteSet.add(oldPath);
      }
      if (isSyncableWikiMarkdown(newPath)) {
        uploadSet.add(newPath);
        replaceSet.add(newPath);
      }
    } else {
      const filePath = tokens[++i] ?? '';
      if (!isSyncableWikiMarkdown(filePath)) continue;
      if (status === 'D') {
        deleteSet.add(filePath);
      } else {
        uploadSet.add(filePath);
        if (status === 'M') {
          replaceSet.add(filePath);
        }
      }
    }
  }

  for (const p of uploadSet) {
    deleteSet.delete(p);
  }

  return {
    toUploadPaths: Array.from(uploadSet).sort(),
    toReplacePaths: replaceSet,
    toDeletePaths: Array.from(deleteSet).sort(),
  };
}

async function lookupRemoteDocumentsByVaultPath(
  ai: GoogleGenAI,
  storeName: string,
  targetPaths: Set<string>,
): Promise<Map<string, string[]>> {
  const found = new Map<string, string[]>();
  if (targetPaths.size === 0) return found;

  const pager = await withRetry(
    () => ai.fileSearchStores.documents.list({ parent: storeName, config: { pageSize: 20 } }),
    'list store documents',
  );

  for await (const doc of pager) {
    const meta = doc.customMetadata?.find((m) => m.key === 'vault_path');
    const vaultPath = meta?.stringValue;
    if (vaultPath && targetPaths.has(vaultPath) && doc.name) {
      const list = found.get(vaultPath) ?? [];
      list.push(doc.name);
      found.set(vaultPath, list);
    }
  }
  return found;
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

  const state = loadState(opts.storeName, opts.reset);
  const toUpload: Array<{ relPath: string; fullPath: string; hash: string }> = [];
  let toDelete: string[] = [];
  let remoteCleanupTargets = new Set<string>();

  if (opts.gitBase) {
    const diff = getGitDiffChanges(opts.gitBase, opts.gitHead);
    for (const relPath of diff.toUploadPaths) {
      const fullPath = path.join(VAULT_ROOT, relPath);
      if (fs.existsSync(fullPath)) {
        toUpload.push({ relPath, fullPath, hash: sha256(fullPath) });
      }
    }
    toDelete = diff.toDeletePaths;
    remoteCleanupTargets = new Set([...diff.toDeletePaths, ...diff.toReplacePaths]);
    console.log(
      `[sync] Git diff (${opts.gitBase}..${opts.gitHead}): ${toUpload.length} to upload, ${toDelete.length} to delete.`,
    );
  } else {
    const allMdFiles = collectMarkdownFiles(WIKI_DIR).sort();
    const currentRelSet = new Set<string>();

    for (const fullPath of allMdFiles) {
      const relPath = path.relative(VAULT_ROOT, fullPath).replace(/\\/g, '/');
      currentRelSet.add(relPath);
      const hash = sha256(fullPath);
      if (state.files[relPath]?.hash !== hash) {
        toUpload.push({ relPath, fullPath, hash });
      }
    }

    toDelete = Object.keys(state.files).filter((relPath) => !currentRelSet.has(relPath));
    console.log(
      `[sync] Scanned ${allMdFiles.length} wiki markdown files: ${toUpload.length} new/changed, ${toDelete.length} deleted.`,
    );
  }

  if (opts.dryRun) {
    console.log('[sync] Dry run enabled. Sample pending uploads:');
    for (const item of toUpload.slice(0, 10)) {
      console.log(`  + ${item.relPath}`);
    }
    return;
  }

  if (opts.gitBase && toUpload.length === 0 && toDelete.length === 0) {
    console.log('[sync] No wiki markdown changes in git diff. Index refreshed only.');
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

  // In CI (--git-diff) mode without local sync-state.json, resolve remote documentNames for modified/deleted files
  const remoteDocsMap = new Map<string, string[]>();
  const unresolvedTargets = new Set(
    Array.from(remoteCleanupTargets).filter((p) => !state.files[p]?.documentName),
  );
  if (unresolvedTargets.size > 0) {
    console.log(`[sync] Looking up ${unresolvedTargets.size} modified/deleted paths in remote store...`);
    const resolved = await lookupRemoteDocumentsByVaultPath(ai, state.storeName, unresolvedTargets);
    for (const [k, v] of resolved.entries()) {
      remoteDocsMap.set(k, v);
    }
  }

  // Delete removed files from File Search Store
  for (const relPath of toDelete) {
    const docNames = new Set<string>();
    if (state.files[relPath]?.documentName) docNames.add(state.files[relPath].documentName!);
    for (const d of remoteDocsMap.get(relPath) ?? []) docNames.add(d);

    for (const docName of docNames) {
      try {
        await withRetry(
          () => ai.fileSearchStores.documents.delete({ name: docName, config: { force: true } }),
          `delete ${relPath}`,
          3,
        );
        console.log(`[sync] Deleted remote doc: ${relPath}`);
      } catch (err) {
        console.warn(`[sync] Failed to delete ${docName}:`, err instanceof Error ? err.message : err);
      }
    }
    delete state.files[relPath];
    saveState(state);
  }

  const filtered = opts.match
    ? toUpload.filter((item) => item.relPath.toLowerCase().includes(opts.match.toLowerCase()))
    : toUpload;
  const batch = filtered.slice(0, opts.limit);
  let completed = 0;
  let cursor = 0;

  async function worker() {
    while (cursor < batch.length) {
      const idx = cursor++;
      const item = batch[idx];
      const meta = indexByPath.get(item.relPath);

      // Remove stale remote version before re-uploading changed file
      const staleDocs = new Set<string>();
      if (state.files[item.relPath]?.documentName) staleDocs.add(state.files[item.relPath].documentName!);
      for (const d of remoteDocsMap.get(item.relPath) ?? []) staleDocs.add(d);

      for (const prevDoc of staleDocs) {
        try {
          await withRetry(
            () => ai.fileSearchStores.documents.delete({ name: prevDoc, config: { force: true } }),
            `delete ${item.relPath}`,
            3,
          );
        } catch {
          // Ignore if already absent
        }
      }

      const customMetadata = [
        { key: 'vault_path', stringValue: item.relPath },
        { key: 'type', stringValue: meta?.type ?? inferTypeFromPath(item.relPath) },
        { key: 'title', stringValue: meta?.title ?? path.basename(item.relPath, '.md') },
      ];

      const fileBytes = fs.readFileSync(item.fullPath);
      const fileBlob = new Blob([fileBytes], { type: 'text/markdown' });

      let op = await withRetry(
        () =>
          ai.fileSearchStores.uploadToFileSearchStore({
            fileSearchStoreName: state.storeName,
            file: fileBlob,
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
      if (completed % 10 === 0 || completed === batch.length) {
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
