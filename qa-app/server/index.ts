import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import dotenv from 'dotenv';
import express, { type NextFunction, type Request, type Response } from 'express';
import { answerWithKnowledgeBase } from './rag.js';
import {
  buildQuartzUrl,
  getIndexStats,
  loadWikiIndex,
  resolveIndexPath,
  searchWikiIndex,
} from './wikiIndex.js';

const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);
// Works both under tsx (server/index.ts) and compiled (dist/server/index.js)
const APP_DIR = path.basename(path.dirname(__dirname)) === 'dist'
  ? path.resolve(__dirname, '..', '..')
  : path.resolve(__dirname, '..');

dotenv.config({ path: path.join(APP_DIR, '.env') });

interface AppConfigFile {
  fileSearchStoreName?: string;
  quartzBaseUrl?: string;
  defaultModel?: string;
}

function loadAppConfig(appDir: string): AppConfigFile {
  const cfgPath = path.join(appDir, 'data', 'app-config.json');
  if (!fs.existsSync(cfgPath)) return {};
  try {
    return JSON.parse(fs.readFileSync(cfgPath, 'utf-8')) as AppConfigFile;
  } catch {
    return {};
  }
}

const appConfig = loadAppConfig(APP_DIR);

const PORT = Number(process.env.PORT || 3000);
const GEMINI_API_KEY = process.env.GEMINI_API_KEY || '';
const FILE_SEARCH_STORE_NAME =
  process.env.FILE_SEARCH_STORE_NAME || appConfig.fileSearchStoreName || '';
const DEFAULT_MODEL =
  process.env.GEMINI_MODEL || appConfig.defaultModel || 'gemini-3.8-flash';
const APP_ACCESS_PASSWORD = process.env.APP_ACCESS_PASSWORD || '';
const QUARTZ_BASE_URL =
  process.env.QUARTZ_BASE_URL || appConfig.quartzBaseUrl || '';

const VAULT_WIKI_DIR = path.resolve(APP_DIR, '..', 'wiki');
const INDEX_PATH = resolveIndexPath(APP_DIR);
const wikiEntries = loadWikiIndex(INDEX_PATH);
const typeCounts = getIndexStats(wikiEntries);

console.log(
  `[server] Loaded ${wikiEntries.length} wiki entries from ${INDEX_PATH}`,
);

const app = express();
app.use(express.json({ limit: '1mb' }));

function requirePassword(req: Request, res: Response, next: NextFunction) {
  if (!APP_ACCESS_PASSWORD) {
    next();
    return;
  }
  const provided =
    req.header('x-access-password') ||
    req.header('authorization')?.replace(/^Bearer\s+/i, '') ||
    '';
  if (provided !== APP_ACCESS_PASSWORD) {
    res.status(401).json({ error: '访问密码无效或缺失' });
    return;
  }
  next();
}

app.get('/api/health', (_req, res) => {
  res.json({
    ok: true,
    indexCount: wikiEntries.length,
    typeCounts,
    storeConfigured: Boolean(FILE_SEARCH_STORE_NAME),
    apiKeyConfigured: Boolean(GEMINI_API_KEY),
    authRequired: Boolean(APP_ACCESS_PASSWORD),
    quartzBaseUrl: QUARTZ_BASE_URL || null,
    defaultModel: DEFAULT_MODEL,
  });
});

app.post('/api/auth/verify', (req, res) => {
  if (!APP_ACCESS_PASSWORD) {
    res.json({ ok: true, authRequired: false });
    return;
  }
  const password = String(req.body?.password ?? '');
  if (password !== APP_ACCESS_PASSWORD) {
    res.status(401).json({ ok: false, error: '密码错误' });
    return;
  }
  res.json({ ok: true, authRequired: true });
});

app.get('/api/index/search', requirePassword, (req, res) => {
  const q = String(req.query.q ?? '');
  const type = typeof req.query.type === 'string' && req.query.type ? req.query.type : undefined;
  const limit = req.query.limit ? Number(req.query.limit) : 20;
  const results = searchWikiIndex(wikiEntries, { query: q, type, limit }).map((m) => ({
    ...m,
    quartzUrl: buildQuartzUrl(m.path, QUARTZ_BASE_URL),
  }));
  res.json({ total: results.length, results });
});

app.get('/api/entry', requirePassword, (req, res) => {
  const entryPath = String(req.query.path ?? '');
  const entry = wikiEntries.find((e) => e.path === entryPath);
  if (!entry) {
    res.status(404).json({ error: '条目不存在于 wiki/index.json 中' });
    return;
  }

  let content: string | null = null;
  if (fs.existsSync(VAULT_WIKI_DIR)) {
    const cleanRel = entry.path.replace(/^wiki\//, '');
    const resolved = path.resolve(VAULT_WIKI_DIR, cleanRel);
    if (resolved.startsWith(path.resolve(VAULT_WIKI_DIR) + path.sep) && fs.existsSync(resolved)) {
      content = fs.readFileSync(resolved, 'utf-8');
    }
  }

  res.json({
    ...entry,
    quartzUrl: buildQuartzUrl(entry.path, QUARTZ_BASE_URL),
    content,
  });
});

app.post('/api/chat', requirePassword, async (req, res) => {
  if (!GEMINI_API_KEY) {
    res.status(500).json({ error: '服务端未配置 GEMINI_API_KEY' });
    return;
  }

  const message = String(req.body?.message ?? '').trim();
  if (!message) {
    res.status(400).json({ error: '问题内容不能为空' });
    return;
  }

  const history = Array.isArray(req.body?.history) ? req.body.history : [];
  const typeFilter =
    typeof req.body?.typeFilter === 'string' && req.body.typeFilter
      ? req.body.typeFilter
      : undefined;
  const model =
    typeof req.body?.model === 'string' && req.body.model ? req.body.model : undefined;
  const outputMode =
    typeof req.body?.outputMode === 'string' && req.body.outputMode
      ? (req.body.outputMode as 'qa' | 'synthesis' | 'report' | 'ppt')
      : undefined;

  try {
    const result = await answerWithKnowledgeBase(
      {
        apiKey: GEMINI_API_KEY,
        fileSearchStoreName: FILE_SEARCH_STORE_NAME || undefined,
        defaultModel: DEFAULT_MODEL,
        quartzBaseUrl: QUARTZ_BASE_URL || undefined,
        vaultWikiDir: fs.existsSync(VAULT_WIKI_DIR) ? VAULT_WIKI_DIR : undefined,
      },
      wikiEntries,
      { message, history, typeFilter, model, outputMode },
    );
    res.json(result);
  } catch (err) {
    console.error('[api/chat] error:', err);
    const msg = err instanceof Error ? err.message : '生成回答时发生未知错误';
    res.status(500).json({ error: msg });
  }
});

async function startServer() {
  const CLIENT_DIST = path.join(APP_DIR, 'dist', 'client');
  if (process.env.NODE_ENV !== 'development' && fs.existsSync(CLIENT_DIST)) {
    app.use(express.static(CLIENT_DIST));
    app.get('*', (_req, res) => {
      res.sendFile(path.join(CLIENT_DIST, 'index.html'));
    });
  } else {
    const { createServer: createViteServer } = await import('vite');
    const vite = await createViteServer({
      root: APP_DIR,
      server: { middlewareMode: true },
      appType: 'spa',
    });
    app.use(vite.middlewares);
  }

  app.listen(PORT, '0.0.0.0', () => {
    console.log(`[server] Listening on http://0.0.0.0:${PORT}`);
  });
}

startServer();
