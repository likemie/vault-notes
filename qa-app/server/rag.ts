import fs from 'node:fs';
import path from 'node:path';
import { GoogleGenAI, Type, type Content, type FunctionDeclaration } from '@google/genai';
import {
  buildQuartzUrl,
  searchWikiIndex,
  type SearchMatch,
  type WikiEntry,
} from './wikiIndex.js';

export interface ChatHistoryTurn {
  role: 'user' | 'model';
  text: string;
}

export interface CitationItem {
  title: string;
  uri?: string;
  textSnippet?: string;
  entryPath?: string;
  entryType?: string;
  quartzUrl?: string;
}

export interface IndexMatchDTO {
  title: string;
  type: string;
  path: string;
  aliases: string[];
  score: number;
  quartzUrl?: string;
}

export interface ChatResponsePayload {
  answer: string;
  mode: 'file-search' | 'local-preview' | 'index-only';
  model: string;
  usedIndexQueries: Array<{ query: string; type?: string; hitCount: number }>;
  indexMatches: IndexMatchDTO[];
  citations: CitationItem[];
}

export interface RagConfig {
  apiKey: string;
  fileSearchStoreName?: string;
  defaultModel: string;
  quartzBaseUrl?: string;
  vaultWikiDir?: string;
}

const LOOKUP_TOOL: FunctionDeclaration = {
  name: 'lookup_wiki_index',
  description:
    'Search the academic knowledge base index (wiki/index.json) by Chinese/English concept name, theory, scholar name, method, instrument, fact, or alias to find canonical entry titles and file paths.',
  parameters: {
    type: Type.OBJECT,
    properties: {
      query: {
        type: Type.STRING,
        description:
          'Search term in Chinese or English (e.g., "再情境化", "Recontextualization", "John Hattie", "RCT").',
      },
      type: {
        type: Type.STRING,
        description: 'Optional entry category filter.',
        enum: ['concept', 'theory', 'argument', 'fact', 'method', 'instrument', 'person'],
      },
      limit: {
        type: Type.INTEGER,
        description: 'Maximum matches to return (1-20, default 10).',
      },
    },
    required: ['query'],
  },
};

function sanitizePathInsideWiki(vaultWikiDir: string, entryPath: string): string | null {
  const cleanRel = entryPath.replace(/^wiki\//, '');
  const resolved = path.resolve(vaultWikiDir, cleanRel);
  const base = path.resolve(vaultWikiDir);
  if (!resolved.startsWith(base + path.sep)) {
    return null;
  }
  return fs.existsSync(resolved) ? resolved : null;
}

function formatIndexContext(matches: SearchMatch[]): string {
  if (matches.length === 0) {
    return '（未在 wiki/index.json 中命中直接匹配的条目标题或别名。）';
  }
  return matches
    .map((m, i) => {
      const aliases = m.aliases.length > 0 ? ` | 别名: ${m.aliases.slice(0, 6).join(' / ')}` : '';
      return `${i + 1}. [${m.type}] ${m.title} (${m.path})${aliases}`;
    })
    .join('\n');
}

/**
 * Step 1: Let Gemini inspect wiki/index.json via function calling to resolve
 * Chinese/English terms, abbreviations, and aliases before full-text retrieval.
 */
async function resolveIndexEntries(
  ai: GoogleGenAI,
  model: string,
  entries: WikiEntry[],
  userMessage: string,
  typeFilter?: string,
): Promise<{
  matches: SearchMatch[];
  usedQueries: Array<{ query: string; type?: string; hitCount: number }>;
}> {
  const usedQueries: Array<{ query: string; type?: string; hitCount: number }> = [];
  const merged = new Map<string, SearchMatch>();

  const addMatches = (list: SearchMatch[]) => {
    for (const item of list) {
      const existing = merged.get(item.path);
      if (!existing || item.score > existing.score) {
        merged.set(item.path, item);
      }
    }
  };

  // Always run a fast deterministic lookup on the raw user message as baseline.
  const directHits = searchWikiIndex(entries, {
    query: userMessage,
    type: typeFilter,
    limit: 8,
  });
  addMatches(directHits);

  const plannerPrompt = [
    '你是教育研究学术知识库的检索规划助手。',
    '根据用户问题，调用 lookup_wiki_index 工具在 wiki/index.json 中查找最相关的规范条目（可分别用中文术语、英文术语、学者名或缩写多次检索）。',
    typeFilter ? `用户已限定条目类型为: ${typeFilter}。` : '如需区分概念、理论、论证、方法、工具、事实、人物，可传入 type。',
    '拿到满意的候选条目后，直接用一句话总结检索完成即可。',
  ].join('\n');

  const contents: Content[] = [{ role: 'user', parts: [{ text: userMessage }] }];

  try {
    for (let step = 0; step < 3; step++) {
      const resp = await ai.models.generateContent({
        model,
        contents,
        config: {
          systemInstruction: plannerPrompt,
          tools: [{ functionDeclarations: [LOOKUP_TOOL] }],
          temperature: 0,
        },
      });

      const calls = resp.functionCalls;
      if (!calls || calls.length === 0) {
        break;
      }

      const modelParts = resp.candidates?.[0]?.content?.parts;
      if (modelParts) {
        contents.push({ role: 'model', parts: modelParts });
      }

      const responseParts = [];
      for (const call of calls) {
        if (call.name !== 'lookup_wiki_index') continue;
        const args = (call.args ?? {}) as Record<string, unknown>;
        const q = String(args.query ?? '').trim();
        const t = typeof args.type === 'string' && args.type ? args.type : typeFilter;
        const lim = typeof args.limit === 'number' ? args.limit : 10;

        const hits = q ? searchWikiIndex(entries, { query: q, type: t, limit: lim }) : [];
        usedQueries.push({ query: q, type: t, hitCount: hits.length });
        addMatches(hits);

        responseParts.push({
          functionResponse: {
            name: 'lookup_wiki_index',
            response: {
              matches: hits.map((h) => ({
                title: h.title,
                type: h.type,
                path: h.path,
                aliases: h.aliases.slice(0, 6),
              })),
            },
          },
        });
      }

      if (responseParts.length === 0) break;
      contents.push({ role: 'user', parts: responseParts });
    }
  } catch (err) {
    // Index planner errors should not block retrieval; directHits remain available.
    console.warn('[rag] index planner fallback:', err instanceof Error ? err.message : err);
  }

  const sorted = Array.from(merged.values())
    .sort((a, b) => b.score - a.score)
    .slice(0, 15);

  return { matches: sorted, usedQueries };
}

function matchEntryByTitleOrPath(
  entries: WikiEntry[],
  rawTitle?: string,
): WikiEntry | undefined {
  if (!rawTitle) return undefined;
  const cleaned = rawTitle.replace(/\.md$/i, '').trim().toLowerCase();
  return entries.find(
    (e) =>
      e.path.toLowerCase() === rawTitle.toLowerCase() ||
      e.title.toLowerCase() === cleaned ||
      path.basename(e.path, '.md').toLowerCase() === cleaned,
  );
}

/**
 * Execute two-stage RAG:
 * 1) Resolve canonical wiki/index.json entries via function calling.
 * 2) Answer with Gemini File Search Store (or local wiki preview if store is unset locally).
 */
export async function answerWithKnowledgeBase(
  config: RagConfig,
  entries: WikiEntry[],
  params: {
    message: string;
    history?: ChatHistoryTurn[];
    typeFilter?: string;
    model?: string;
  },
): Promise<ChatResponsePayload> {
  const ai = new GoogleGenAI({ apiKey: config.apiKey });
  const activeModel = params.model || config.defaultModel;
  const plannerModel = 'gemini-3.8-flash';

  const { matches, usedQueries } = await resolveIndexEntries(
    ai,
    plannerModel,
    entries,
    params.message,
    params.typeFilter,
  );

  const indexMatchesDTO: IndexMatchDTO[] = matches.map((m) => ({
    title: m.title,
    type: m.type,
    path: m.path,
    aliases: m.aliases,
    score: m.score,
    quartzUrl: buildQuartzUrl(m.path, config.quartzBaseUrl),
  }));

  const historyContents: Content[] = (params.history ?? []).slice(-8).map((turn) => ({
    role: turn.role,
    parts: [{ text: turn.text }],
  }));

  const systemInstruction = [
    '你是“教育研究学术维基知识库”的在线问答助手。',
    '回答规则：',
    '1. 严格依据检索到的知识库条目与索引上下文作答，不编造未检索到的学者观点、实证数据或页码。',
    '2. 明确区分概念界定（concept）、理论框架（theory）、单篇文献论证（argument）、政策事实（fact）、研究方法（method）、测量工具（instrument）与人物（person）。',
    '3. 若材料存在局限、分歧或仅在局部文献中成立，须如实说明限定条件。',
    '4. 回答中直接引用具体条目名称（如 [[条目名]] 或条目路径），文末给出“参考条目”列表。',
    '5. 若知识库中没有足够依据回答某个子问题，请明确告知“当前知识库未见直接记录”，不要凭空补充。',
  ].join('\n');

  const promptWithIndex = [
    '### 来自 wiki/index.json 的候选条目索引',
    formatIndexContext(matches),
    '',
    '### 用户问题',
    params.message,
  ].join('\n');

  // Primary cloud mode: Gemini File Search Store
  if (config.fileSearchStoreName) {
    const fileSearchConfig: {
      fileSearchStoreNames: string[];
      metadataFilter?: string;
    } = {
      fileSearchStoreNames: [config.fileSearchStoreName],
    };
    if (params.typeFilter) {
      fileSearchConfig.metadataFilter = `type = "${params.typeFilter}"`;
    }

    const response = await ai.models.generateContent({
      model: activeModel,
      contents: [
        ...historyContents,
        { role: 'user', parts: [{ text: promptWithIndex }] },
      ],
      config: {
        systemInstruction,
        tools: [{ fileSearch: fileSearchConfig }],
        temperature: 0.2,
      },
    });

    const citations: CitationItem[] = [];
    const seen = new Set<string>();
    const groundingChunks =
      response.candidates?.[0]?.groundingMetadata?.groundingChunks ?? [];

    for (const chunk of groundingChunks) {
      const ctx = chunk.retrievedContext;
      if (!ctx) continue;
      const title = ctx.title || ctx.uri || '未知条目';
      const dedupeKey = `${title}::${ctx.uri ?? ''}`;
      if (seen.has(dedupeKey)) continue;
      seen.add(dedupeKey);

      const matchedEntry = matchEntryByTitleOrPath(entries, ctx.title);
      citations.push({
        title: matchedEntry?.title ?? title,
        uri: ctx.uri ?? undefined,
        textSnippet: ctx.text ? ctx.text.slice(0, 260) : undefined,
        entryPath: matchedEntry?.path,
        entryType: matchedEntry?.type,
        quartzUrl: matchedEntry
          ? buildQuartzUrl(matchedEntry.path, config.quartzBaseUrl)
          : undefined,
      });
    }

    return {
      answer: response.text ?? '未生成有效回答，请尝试换一种表述或放宽类型过滤。',
      mode: 'file-search',
      model: activeModel,
      usedIndexQueries: usedQueries,
      indexMatches: indexMatchesDTO,
      citations,
    };
  }

  // Local fallback mode: when FILE_SEARCH_STORE_NAME is not yet configured, read top matched local wiki/*.md files
  if (config.vaultWikiDir && fs.existsSync(config.vaultWikiDir) && matches.length > 0) {
    const localSnippets: string[] = [];
    const citations: CitationItem[] = [];

    for (const m of matches.slice(0, 6)) {
      const fullPath = sanitizePathInsideWiki(config.vaultWikiDir, m.path);
      if (!fullPath) continue;
      const content = fs.readFileSync(fullPath, 'utf-8').slice(0, 5000);
      localSnippets.push(`--- [${m.type}] ${m.title} (${m.path}) ---\n${content}`);
      citations.push({
        title: m.title,
        entryPath: m.path,
        entryType: m.type,
        quartzUrl: buildQuartzUrl(m.path, config.quartzBaseUrl),
      });
    }

    const localPrompt = [
      promptWithIndex,
      '',
      '### 本地预览模式读取到的候选条目正文（当前尚未配置 FILE_SEARCH_STORE_NAME，仅读取索引命中的前 6 篇）',
      localSnippets.join('\n\n'),
    ].join('\n');

    const response = await ai.models.generateContent({
      model: activeModel,
      contents: [...historyContents, { role: 'user', parts: [{ text: localPrompt }] }],
      config: {
        systemInstruction,
        temperature: 0.2,
      },
    });

    return {
      answer: response.text ?? '未生成有效回答。',
      mode: 'local-preview',
      model: activeModel,
      usedIndexQueries: usedQueries,
      indexMatches: indexMatchesDTO,
      citations,
    };
  }

  return {
    answer:
      '已完成 `wiki/index.json` 索引检索，但尚未配置 `FILE_SEARCH_STORE_NAME`，且当前运行环境未挂载本地 `wiki/` 目录。请先运行 `npm run sync` 建立 Gemini File Search Store 并填入 `.env` 中的 `FILE_SEARCH_STORE_NAME`。',
    mode: 'index-only',
    model: activeModel,
    usedIndexQueries: usedQueries,
    indexMatches: indexMatchesDTO,
    citations: [],
  };
}
