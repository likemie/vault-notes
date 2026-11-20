export const LIMIT = 100;
const DAY = 86_400_000;
const DAY_SNAPSHOT_LIMIT = 512;
const PATH_ORDER = new Intl.Collator("zh-CN", { numeric: true });

export interface ArgumentNote {
  path: string;
  title: string;
  created: string | null;
}

interface HistoryEntry {
  path: string;
  firstSeen: number;
  unread: boolean;
}

export interface Checkpoint {
  at: number;
  day: string;
  dayPaths: string[] | null;
  recent: HistoryEntry[];
}

export interface RecentNote extends ArgumentNote, HistoryEntry {
  awaitingDate: boolean;
}

export function dayKey(value: number): string {
  const date = new Date(value);
  return [date.getFullYear(), String(date.getMonth() + 1).padStart(2, "0"),
    String(date.getDate()).padStart(2, "0")].join("-");
}

export function creationDay(value: unknown): string | null {
  if (value instanceof Date && Number.isFinite(value.getTime())) value = value.toISOString();
  if (typeof value !== "string") return null;
  // MyNotes records a calendar date. Keep that date even when the YAML loader emits a UTC Date.
  const match = /^(\d{4}-\d{2}-\d{2})(?:[T ]\d{2}:\d{2}.*)?$/.exec(value.trim());
  if (!match) return null;
  const day = match[1];
  const at = Date.parse(day + "T00:00:00Z");
  return Number.isFinite(at) && new Date(at).toISOString().slice(0, 10) === day ? day : null;
}

type NoteDate = { created: string | null; firstSeen?: number };

function noteDay(note: NoteDate): string | null {
  return note.created ?? (note.firstSeen ? dayKey(note.firstSeen) : null);
}

export function displayDate(note: NoteDate, now: number): string {
  const day = noteDay(note);
  if (!day) return "日期未知";
  const elapsed = Math.round((Date.parse(dayKey(now)) - Date.parse(day)) / DAY);
  const label = elapsed === 0 ? "今天" : elapsed === 1 ? "昨天" :
    elapsed > 1 && elapsed < 7 ? elapsed + " 天前" : day.slice(day.startsWith(dayKey(now).slice(0, 4)) ? 5 : 0);
  return note.created ? label : label + "发现";
}

export function dateDescription(note: NoteDate): string {
  if (note.created) return "创建日期 " + note.created;
  if (note.firstSeen) return "首次发现于 " + dayKey(note.firstSeen) + "，创建日期未知";
  return "创建日期未知";
}

export function compareCreationDays(a: string | null, b: string | null): number {
  if (a === b) return 0;
  return (a ?? "") > (b ?? "") ? -1 : 1;
}

export class RecentStore {
  private readonly notes = new Map<string, RecentNote>();
  private readonly removed = new Map<string, { note: RecentNote; at: number }>();
  private readonly pendingStartup = new Set<string>();
  private readonly previousDayPaths: Set<string> | null;

  constructor(private readonly previous: Checkpoint | null) {
    this.previousDayPaths = previous?.dayPaths ? new Set(previous.dayPaths) : null;
  }

  seed(notes: Iterable<{ note: ArgumentNote; hasMetadata: boolean }>, now: number): void {
    const persisted = new Map(this.previous?.recent.map(entry => [entry.path, entry]));
    for (const { note, hasMetadata } of notes) {
      const prior = persisted.get(note.path);
      const unread = prior?.unread ?? this.addedWhileAway(note, now);
      this.notes.set(note.path, { ...note, firstSeen: prior?.firstSeen ?? 0, unread, awaitingDate: false });
      if (!prior && !hasMetadata && this.previous) this.pendingStartup.add(note.path);
    }
  }

  upsert(note: ArgumentNote, at: number, hasMetadata: boolean): boolean {
    this.pruneRemoved(at);
    const restored = this.removed.get(note.path);
    this.removed.delete(note.path);
    const current = this.notes.get(note.path);
    const prior = current ?? restored?.note;
    const firstSeen = prior?.firstSeen ?? at;
    const awaitingDate = !note.created && (prior?.awaitingDate ?? true);
    let unread = prior?.unread ?? (!note.created || note.created === dayKey(at));
    if (hasMetadata && this.pendingStartup.delete(note.path)) unread = this.addedWhileAway(note, at);
    if (prior?.awaitingDate && note.created && note.created < dayKey(firstSeen)) unread = false;
    if (current && current.title === note.title && current.created === note.created &&
        current.unread === unread && current.awaitingDate === awaitingDate) return false;
    this.notes.set(note.path, { ...note, firstSeen, unread, awaitingDate });
    return true;
  }

  rename(oldPath: string, note: ArgumentNote, at: number, hasMetadata: boolean): boolean {
    this.pruneRemoved(at);
    const prior = this.notes.get(oldPath) ?? this.removed.get(oldPath)?.note;
    this.notes.delete(oldPath);
    this.removed.delete(oldPath);
    if (this.pendingStartup.delete(oldPath)) this.pendingStartup.add(note.path);
    if (prior) {
      this.notes.set(note.path, { ...prior, path: note.path });
      // A rename can precede the metadata cache for the new path.
      if (!hasMetadata) return true;
    }
    return this.upsert(note, at, hasMetadata) || oldPath !== note.path;
  }

  remove(path: string, at: number): boolean {
    this.pendingStartup.delete(path);
    const note = this.notes.get(path);
    if (!note) return false;
    this.pruneRemoved(at);
    this.removed.set(path, { note, at });
    this.notes.delete(path);
    return true;
  }

  removeFolder(path: string, at: number): boolean {
    let changed = false;
    for (const file of this.notes.keys()) {
      if (file.startsWith(path + "/")) changed = this.remove(file, at) || changed;
    }
    return changed;
  }

  read(path: string): boolean {
    const note = this.notes.get(path);
    if (!note) return false;
    this.pendingStartup.delete(path);
    if (!note.unread) return false;
    note.unread = false;
    return true;
  }

  snapshot(now: number) {
    const day = dayKey(now);
    const todayPaths: string[] = [];
    const sorted = Array.from(this.notes.values(), note => ({ note, day: noteDay(note) }));
    for (const { note } of sorted) {
      if (note.created === day) todayPaths.push(note.path);
    }
    sorted.sort((a, b) => {
      return compareCreationDays(a.day, b.day) || b.note.firstSeen - a.note.firstSeen ||
        PATH_ORDER.compare(a.note.path, b.note.path);
    });
    const rows = sorted.slice(0, LIMIT).map(({ note }) => note);
    const checkpoint: Checkpoint = {
      at: now, day, dayPaths: todayPaths.length <= DAY_SNAPSHOT_LIMIT ? todayPaths : null,
      recent: rows.map(({ path, firstSeen, unread }) => ({ path, firstSeen, unread })),
    };
    return {
      rows, unread: rows.filter(row => row.unread).length,
      today: todayPaths.length, checkpoint,
    };
  }

  private addedWhileAway(note: ArgumentNote, now: number): boolean {
    const previous = this.previous;
    if (!previous || !note.created || note.created > dayKey(now)) return false;
    return note.created > previous.day ||
      (note.created === previous.day && this.previousDayPaths !== null && !this.previousDayPaths.has(note.path));
  }

  private pruneRemoved(now: number): void {
    // Reuse the record if a sync client replaces a file with a short delete/create pair.
    for (const [path, entry] of this.removed) {
      if (now - entry.at <= 2000) break;
      this.removed.delete(path);
    }
  }
}
