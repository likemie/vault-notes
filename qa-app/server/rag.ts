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

export interface WebSourceItem {
  title: string;
  uri: string;
}

export interface ChatResponsePayload {
  answer: string;
  mode: 'file-search' | 'local-preview' | 'index-only';
  model: string;
  usedIndexQueries: Array<{ query: string; type?: string; hitCount: number }>;
  indexMatches: IndexMatchDTO[];
  citations: CitationItem[];
  webSupplement?: string;
  webSources?: WebSourceItem[];
  webSearchQueries?: string[];
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

export type OutputMode = 'qa' | 'synthesis' | 'report' | 'ppt';

const OUTPUT_MODE_INSTRUCTIONS: Record<OutputMode, string> = {
  qa: '输出模式：常规研究问答。先给出清楚的中心判断或问题结构，再围绕主张与根据展开，末尾列明参考条目与证据边界。',
  synthesis:
    '输出模式：学术综合／论文写作底稿（按 vault-use.md 最高证据标准）。围绕“核心判断与根据”组织，不逐篇罗列“研究 A 认为……研究 B 认为……”；每一部分先立可讨论判断，再给直接证据、机制解释、竞争性研究比较、方法/样本/测量条件差异与局限；使用规范 APA 后引。',
  report:
    '输出模式：主题／政策报告。围绕现实问题形成有证据支持的结构化判断（可视证据结构采用问题界定、现状与变化、关键发现、机制解释、分化与风险、综合判断等），用 Fact 与政策材料描述现状，用 Argument 评估研究支持强度，政策建议须区分“证据支持的判断”与“基于现有材料的推论”。',
  ppt:
    '输出模式：PPT 叙事结构与演讲底稿。按“提出问题 → 必要背景 → 矛盾或待解现象 → 核心证据 → 机制与差异 → 综合判断与含义”设计认知推进路线；每一部分给出表达判断的页面标题（不用“背景/理论/现状”等中性标签）与一句核心 message，并保留支撑证据与限定条件。',
};

const ACADEMIC_WRITING_STYLE_RULES = [
  '【学术段落论证与写作风格（强制执行）】',
  '1. 严禁过度分点与大纲体罗列：正文必须以连贯、完整的学术段落（continuous prose）展开论证，禁止把主体写成“1. 大标题”下面挂“• **小标题**：一两句话”的碎点清单，也禁止用项目符号替代句间逻辑衔接。只有在文末列“参考条目”或确需跨维度对比时使用 Markdown 表格，其余部分一律写完整段落。',
  '2. 坚持“主张 → 证据 → 推理 → 限定”的段落结构：每个自然段开头用一两句明确提出本段的核心判断（不使用“核心是：”“原因如下：”等空洞冒号前缀，也不以无回指对象的“值得注意的是”“由此可见”起段），随后展开支撑该判断的实证发现、机制链条、研究设计或政策事实，交代证据强度、反例与适用条件，并在句末用规范 APA 后引标明出处。',
  '3. 图表规范：严禁手绘 ASCII 字符画框图。若问题确实需要结构或机制图示，请使用标准 ```mermaid 代码块（仅限 flowchart TD / flowchart LR / sequenceDiagram），且节点标签中含有括号或冒号时务必用双引号包裹，例如 `A["标签（说明）"]`。',
  '4. 避免无信息量的否定转折（如“不是……而是……”“并非……而是……”），仅在文献中确实存在相互竞争的命题需要辨析时才使用。',
  '5. 严禁使用商业与互联网套话（如“抓手”“具体抓手”“赋能”“闭环”“跃迁”“赛道”“痛点”“底层逻辑”“顶层设计”“颗粒度”“全链路”等）以及 AI 模板句（如“这不仅是……更是……”“为我们提供了全新视角”“具有重要理论与现实意义”）。',
  '6. 避免无根据的评价词（“重要”“关键”“深刻”“卓越”“领先”）代替实质论证；不使用感叹号或反问句代替论证；同一概念保持译名稳定。',
].join('\n');

function buildVaultUseSystemInstruction(outputMode: OutputMode = 'qa'): string {
  return [
    '你是教育研究学术维基知识库的在线问答助手，必须严格遵循本库的《Vault Use》检索、综合、引用与写作规范：',
    '',
    '【一、知识对象分工与核验层级】',
    '1. 区分 7 类条目职能：Concept（概念界定与边界）、Theory（解释机制）、Argument（单篇文献论证、证据与局限）、Fact（政策/组织/事件情境）、Method（研究设计）、Instrument（测量工具）、Person（学者思想脉络）。',
    '2. wiki/index.json 的命中结果仅作为检索线索（L0），不得当作证据本身。非 Argument 条目中的概括不能直接越过 Argument 归于原作者。',
    '3. 本在线系统索引的是 wiki/ 提炼条目与 Argument，未直接读取原始 PDF/EPUB 全文（未达到 L3 Source verified）。因此严禁声称“已核对原文件/原文”，只可说明“依据知识库条目 / Argument 提炼”，并保留检索文本中明确记载的作者、年份与页码。',
    '4. 严禁编造未检索到的学者观点、实证数字、统计结果或页码；如某一重要维度在检索结果中缺失，须明确标注为“当前知识库未见直接记录 / 证据缺口”，不得用常识填补。',
    '',
    '【二、综合分析与材料关系判断】',
    '1. 先给出中心判断或清楚的议题结构；以“综合主张及其根据”为基本单位组织内容，不按检索到的文件名顺序逐篇流水账式罗列（不写“研究 A 认为……研究 B 认为……”）。',
    '2. 明确判断多条材料之间的关系类型：累积关系（独立证据支持相近判断）、机制关系（构成条件/过程/中介链条）、竞争关系（结论冲突，需比较对象、方法、测量与情境）、条件关系、历史演化关系或层级关系（个体/课堂/学校/国家/全球）。',
    '3. 不得把“多篇文献共同提及”自动写成“学术共识”或因果关系；对支持证据、反例、竞争性解释、研究局限与适用条件分别交代。',
    '',
    '【三、APA 引用与库内定位】',
    '1. 一般使用 APA 后引格式：先陈述主张与证据，再在句末或段末附 `(Author, Year)` 或 `(Author, Year, p. 12)`（仅使用检索文本中确切出现的作者—年份与页码，不私自汉化作者姓氏，不猜测卷期或 DOI）。仅在比较不同作者立场或追踪概念归属时使用叙述式引用。',
    '2. 引用 Concept、Theory、Fact、Method 等非 Argument 条目中的文献结论时，尽可能回溯其中提到的 Argument 与 APA 出处。',
    '3. 回答末尾单独列出“参考条目”，写明条目名称与库内路径（例如 `[[条目名]]` 与 `wiki/.../*.md`），方便用户回库核查。',
    '',
    ACADEMIC_WRITING_STYLE_RULES,
    '',
    `【五、当前回答模式】\n${OUTPUT_MODE_INSTRUCTIONS[outputMode]}`,
  ].join('\n');
}

async function runWebSupplement(
  ai: GoogleGenAI,
  model: string,
  userMessage: string,
  vaultAnswer: string,
): Promise<{
  webSupplement?: string;
  webSources: WebSourceItem[];
  webSearchQueries: string[];
}> {
  const prompt = [
    '用户开启了“允许外部联网补充”。下面先给出用户问题以及内部学术知识库（已检索）的回答摘要。',
    '请你使用 Google Search 检索外部公开信息，仅补充：',
    '1. 知识库尚未覆盖的缺口或最新政策/研究动态；',
    '2. 若有直接可核对的官方文件、时间节点或统计来源，请简要说明；',
    '3. 若知识库回答已充分或网上无可靠补充，请简短说明“无额外必要外部补充”。',
    '写作保持严谨质朴学术语态，禁用夸张评价词和套话。',
    '',
    `【用户问题】\n${userMessage}`,
    '',
    `【内部知识库已有回答摘要】\n${vaultAnswer.slice(0, 2200)}`,
  ].join('\n');

  try {
    const resp = await ai.models.generateContent({
      model,
      contents: prompt,
      config: {
        systemInstruction: [
          '你负责为教育研究学术知识库做外部公开信息补充。',
          '只补充内部知识库尚未覆盖的公开政策文件、最新统计或学术进展；若无可靠补充则简短说明即可。',
          ACADEMIC_WRITING_STYLE_RULES,
        ].join('\n'),
        tools: [{ googleSearch: {} }],
        temperature: 0.2,
      },
    });

    const gm = resp.candidates?.[0]?.groundingMetadata;
    const webSources: WebSourceItem[] = [];
    const seen = new Set<string>();
    for (const chunk of gm?.groundingChunks ?? []) {
      const w = chunk.web;
      if (!w?.uri) continue;
      if (seen.has(w.uri)) continue;
      seen.add(w.uri);
      webSources.push({
        title: w.title || w.uri,
        uri: w.uri,
      });
    }

    return {
      webSupplement: resp.text ?? undefined,
      webSources,
      webSearchQueries: gm?.webSearchQueries ?? [],
    };
  } catch (err) {
    console.warn('[rag] web supplement error:', err instanceof Error ? err.message : err);
    return {
      webSupplement: `外部联网检索调用失败：${err instanceof Error ? err.message : '未知错误'}`,
      webSources: [],
      webSearchQueries: [],
    };
  }
}

/**
 * Execute two-stage RAG (plus optional sequential Google Search web supplement):
 * 1) Resolve canonical wiki/index.json entries via function calling.
 * 2) Answer with Gemini File Search Store (or local wiki preview if store is unset locally).
 * 3) Optionally supplement external gaps via Google Search in a separate turn.
 */
export async function answerWithKnowledgeBase(
  config: RagConfig,
  entries: WikiEntry[],
  params: {
    message: string;
    history?: ChatHistoryTurn[];
    typeFilter?: string;
    model?: string;
    outputMode?: OutputMode;
    allowWebSearch?: boolean;
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

  const systemInstruction = buildVaultUseSystemInstruction(params.outputMode ?? 'qa');

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

    const vaultAnswer = response.text ?? '未生成有效回答，请尝试换一种表述或放宽类型过滤。';
    const webExtra = params.allowWebSearch
      ? await runWebSupplement(ai, activeModel, params.message, vaultAnswer)
      : undefined;

    return {
      answer: vaultAnswer,
      mode: 'file-search',
      model: activeModel,
      usedIndexQueries: usedQueries,
      indexMatches: indexMatchesDTO,
      citations,
      ...(webExtra ?? {}),
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

    const vaultAnswer = response.text ?? '未生成有效回答。';
    const webExtra = params.allowWebSearch
      ? await runWebSupplement(ai, activeModel, params.message, vaultAnswer)
      : undefined;

    return {
      answer: vaultAnswer,
      mode: 'local-preview',
      model: activeModel,
      usedIndexQueries: usedQueries,
      indexMatches: indexMatchesDTO,
      citations,
      ...(webExtra ?? {}),
    };
  }

  const fallbackAnswer =
    '已完成 `wiki/index.json` 索引检索，但尚未配置 `FILE_SEARCH_STORE_NAME`，且当前运行环境未挂载本地 `wiki/` 目录。请先运行 `npm run sync` 建立 Gemini File Search Store 并填入 `.env` 中的 `FILE_SEARCH_STORE_NAME`。';
  const webExtra = params.allowWebSearch
    ? await runWebSupplement(ai, activeModel, params.message, fallbackAnswer)
    : undefined;

  return {
    answer: fallbackAnswer,
    mode: 'index-only',
    model: activeModel,
    usedIndexQueries: usedQueries,
    indexMatches: indexMatchesDTO,
    citations: [],
    ...(webExtra ?? {}),
  };
}
