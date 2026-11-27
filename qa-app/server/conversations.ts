import { Firestore } from '@google-cloud/firestore';

export interface StoredConversationSummary {
  id: string;
  title: string;
  createdAt: string;
  updatedAt: string;
  messageCount: number;
  approxBytes?: number;
}

export interface StoredConversation extends StoredConversationSummary {
  messages: unknown[];
}

export interface StorageUsageStats {
  count: number;
  maxCount: number;
  totalBytes: number;
  maxBytes: number;
}

const COLLECTION = process.env.FIRESTORE_COLLECTION || 'qa_conversations';
export const MAX_STORED_CONVERSATIONS = Number(process.env.FIRESTORE_MAX_CONVERSATIONS || 500);
// Hard ceiling at 900 MiB (~88% of Firestore's 1 GiB Always Free tier), leaving ~124 MiB for index overhead.
export const MAX_TOTAL_STORAGE_BYTES = Number(
  process.env.FIRESTORE_MAX_BYTES || 900 * 1024 * 1024,
);
// Keep individual Firestore documents well under Firestore's 1 MiB document limit.
const MAX_SINGLE_DOC_BYTES = 700 * 1024;

let firestoreClient: Firestore | null = null;
let firestoreDisabledReason: string | null = null;

function isCloudRunEnv(): boolean {
  return Boolean(
    process.env.K_SERVICE ||
      process.env.GOOGLE_CLOUD_PROJECT ||
      process.env.GOOGLE_APPLICATION_CREDENTIALS,
  );
}

function getFirestore(): Firestore | null {
  if (process.env.DISABLE_FIRESTORE === '1') {
    firestoreDisabledReason = 'disabled by env';
    return null;
  }
  if (!isCloudRunEnv()) {
    firestoreDisabledReason = 'local environment without GCP credentials';
    return null;
  }
  if (!firestoreClient) {
    firestoreClient = new Firestore({
      preferRest: true,
      ignoreUndefinedProperties: true,
      ...(process.env.FIRESTORE_DATABASE_ID
        ? { databaseId: process.env.FIRESTORE_DATABASE_ID }
        : {}),
    });
  }
  return firestoreClient;
}

function withTimeout<T>(promise: Promise<T>, ms: number): Promise<T> {
  return Promise.race([
    promise,
    new Promise<T>((_, reject) => setTimeout(() => reject(new Error('Firestore timeout')), ms)),
  ]);
}

function sanitizeId(rawId: string): string {
  const cleaned = rawId.replace(/[^a-zA-Z0-9_-]/g, '').slice(0, 80);
  if (!cleaned) {
    throw new Error('Invalid conversation ID');
  }
  return cleaned;
}

/**
 * Strip bulky redundant fields (such as full alias arrays and long chunk snippets)
 * before writing to Firestore so documents stay compact and well below 1 MiB.
 */
export function compactMessagesForStorage(messages: unknown[]): unknown[] {
  const compacted = messages.map((raw) => {
    if (!raw || typeof raw !== 'object') return raw;
    const msg = raw as Record<string, unknown>;
    const copy: Record<string, unknown> = {
      id: msg.id,
      role: msg.role,
      text: typeof msg.text === 'string' ? msg.text : String(msg.text ?? ''),
      ...(msg.mode ? { mode: msg.mode } : {}),
      ...(msg.model ? { model: msg.model } : {}),
      ...(msg.webSupplement ? { webSupplement: msg.webSupplement } : {}),
    };

    if (Array.isArray(msg.usedIndexQueries)) {
      copy.usedIndexQueries = msg.usedIndexQueries.slice(0, 8);
    }

    if (Array.isArray(msg.indexMatches)) {
      copy.indexMatches = msg.indexMatches.slice(0, 10).map((item) => {
        const m = (item ?? {}) as Record<string, unknown>;
        return {
          title: m.title,
          type: m.type,
          path: m.path,
          ...(m.quartzUrl ? { quartzUrl: m.quartzUrl } : {}),
        };
      });
    }

    if (Array.isArray(msg.citations)) {
      copy.citations = msg.citations.slice(0, 12).map((item) => {
        const c = (item ?? {}) as Record<string, unknown>;
        const snippet =
          typeof c.textSnippet === 'string' ? c.textSnippet.slice(0, 120) : undefined;
        return {
          title: c.title,
          ...(c.entryPath ? { entryPath: c.entryPath } : {}),
          ...(c.entryType ? { entryType: c.entryType } : {}),
          ...(c.quartzUrl ? { quartzUrl: c.quartzUrl } : {}),
          ...(snippet ? { textSnippet: snippet } : {}),
        };
      });
    }

    if (Array.isArray(msg.webSources)) {
      copy.webSources = msg.webSources.slice(0, 10);
    }

    if (Array.isArray(msg.webSearchQueries)) {
      copy.webSearchQueries = msg.webSearchQueries.slice(0, 6);
    }

    return copy;
  });

  // Safety trim if a single long conversation ever approaches Firestore's 1 MiB doc limit
  let serializedBytes = Buffer.byteLength(JSON.stringify(compacted), 'utf-8');
  while (serializedBytes > MAX_SINGLE_DOC_BYTES && compacted.length > 2) {
    compacted.shift();
    serializedBytes = Buffer.byteLength(JSON.stringify(compacted), 'utf-8');
  }
  return compacted;
}

/**
 * Determine which oldest conversation IDs to prune so total count and bytes stay
 * strictly below MAX_STORED_CONVERSATIONS and MAX_TOTAL_STORAGE_BYTES.
 */
export function selectIdsToPrune(
  docsNewestFirst: Array<{ id: string; approxBytes: number }>,
  maxCount = MAX_STORED_CONVERSATIONS,
  maxBytes = MAX_TOTAL_STORAGE_BYTES,
): string[] {
  const toDelete: string[] = [];
  let keptCount = 0;
  let keptBytes = 0;

  for (const doc of docsNewestFirst) {
    const size = Math.max(0, doc.approxBytes || 0);
    if (keptCount + 1 > maxCount || (keptCount > 0 && keptBytes + size > maxBytes)) {
      toDelete.push(doc.id);
    } else {
      keptCount++;
      keptBytes += size;
    }
  }
  return toDelete;
}

export async function listRemoteConversations(): Promise<{
  mode: 'firestore' | 'local';
  reason?: string;
  conversations: StoredConversationSummary[];
  usage?: StorageUsageStats;
}> {
  const db = getFirestore();
  if (!db) {
    return { mode: 'local', reason: firestoreDisabledReason ?? undefined, conversations: [] };
  }
  try {
    const snap = await withTimeout(
      db
        .collection(COLLECTION)
        .select('id', 'title', 'createdAt', 'updatedAt', 'messageCount', 'approxBytes')
        .orderBy('updatedAt', 'desc')
        .limit(MAX_STORED_CONVERSATIONS)
        .get(),
      5000,
    );
    let totalBytes = 0;
    const conversations: StoredConversationSummary[] = snap.docs.map((doc) => {
      const data = doc.data();
      const approxBytes = Number(data.approxBytes ?? 0);
      totalBytes += approxBytes;
      return {
        id: doc.id,
        title: String(data.title ?? '未命名对话'),
        createdAt: String(data.createdAt ?? ''),
        updatedAt: String(data.updatedAt ?? ''),
        messageCount: Number(data.messageCount ?? 0),
        approxBytes,
      };
    });
    return {
      mode: 'firestore',
      conversations,
      usage: {
        count: conversations.length,
        maxCount: MAX_STORED_CONVERSATIONS,
        totalBytes,
        maxBytes: MAX_TOTAL_STORAGE_BYTES,
      },
    };
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    console.warn('[firestore] list failed, falling back to local:', msg);
    return { mode: 'local', reason: msg, conversations: [] };
  }
}

export async function getRemoteConversation(id: string): Promise<StoredConversation | null> {
  const db = getFirestore();
  if (!db) return null;
  const safeId = sanitizeId(id);
  const doc = await withTimeout(db.collection(COLLECTION).doc(safeId).get(), 5000);
  if (!doc.exists) return null;
  const data = doc.data()!;
  return {
    id: doc.id,
    title: String(data.title ?? '未命名对话'),
    createdAt: String(data.createdAt ?? ''),
    updatedAt: String(data.updatedAt ?? ''),
    messageCount: Number(data.messageCount ?? (Array.isArray(data.messages) ? data.messages.length : 0)),
    approxBytes: Number(data.approxBytes ?? 0),
    messages: Array.isArray(data.messages) ? data.messages : [],
  };
}

export async function saveRemoteConversation(conv: {
  id: string;
  title: string;
  createdAt?: string;
  updatedAt?: string;
  messages: unknown[];
}): Promise<{
  saved: boolean;
  mode: 'firestore' | 'local';
  reason?: string;
  prunedCount?: number;
  usage?: StorageUsageStats;
}> {
  const db = getFirestore();
  if (!db) {
    return { saved: false, mode: 'local', reason: firestoreDisabledReason ?? undefined };
  }
  const safeId = sanitizeId(conv.id);
  const now = new Date().toISOString();
  const compactedMessages = compactMessagesForStorage(
    Array.isArray(conv.messages) ? conv.messages : [],
  );

  const basePayload = {
    id: safeId,
    title: String(conv.title || '新研究对话').slice(0, 120),
    createdAt: conv.createdAt || now,
    updatedAt: conv.updatedAt || now,
    messageCount: compactedMessages.length,
    messages: compactedMessages,
  };
  const approxBytes = Buffer.byteLength(JSON.stringify(basePayload), 'utf-8');
  const payload = { ...basePayload, approxBytes };

  try {
    await withTimeout(db.collection(COLLECTION).doc(safeId).set(payload, { merge: true }), 5000);

    // Enforce count + total-bytes ceiling so storage never approaches 1 GiB
    const snap = await withTimeout(
      db
        .collection(COLLECTION)
        .select('updatedAt', 'approxBytes')
        .orderBy('updatedAt', 'desc')
        .get(),
      5000,
    );
    const ordered = snap.docs.map((d) => ({
      id: d.id,
      approxBytes: Number(d.data().approxBytes ?? 0),
    }));
    const pruneIds = selectIdsToPrune(ordered);
    for (const oldId of pruneIds) {
      await withTimeout(db.collection(COLLECTION).doc(oldId).delete(), 5000);
    }

    const totalBytes = ordered
      .filter((d) => !pruneIds.includes(d.id))
      .reduce((sum, d) => sum + d.approxBytes, 0);

    return {
      saved: true,
      mode: 'firestore',
      prunedCount: pruneIds.length,
      usage: {
        count: ordered.length - pruneIds.length,
        maxCount: MAX_STORED_CONVERSATIONS,
        totalBytes,
        maxBytes: MAX_TOTAL_STORAGE_BYTES,
      },
    };
  } catch (err) {
    const msg = err instanceof Error ? err.message : String(err);
    console.warn('[firestore] save failed, falling back to local:', msg);
    return { saved: false, mode: 'local', reason: msg };
  }
}

export async function deleteRemoteConversation(id: string): Promise<{ deleted: boolean }> {
  const db = getFirestore();
  if (!db) return { deleted: false };
  const safeId = sanitizeId(id);
  try {
    await withTimeout(db.collection(COLLECTION).doc(safeId).delete(), 5000);
    return { deleted: true };
  } catch (err) {
    console.warn('[firestore] delete failed:', err instanceof Error ? err.message : err);
    return { deleted: false };
  }
}
