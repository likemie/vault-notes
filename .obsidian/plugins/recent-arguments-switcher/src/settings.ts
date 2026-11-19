import type { Checkpoint } from "./recent-store";

export const ARGUMENT_ROOT = "wiki/arguments/";
export const BATCH_MS = 200;

export interface Position { x: number; y: number }
export interface PanelState { collapsed: boolean; position: Position | null }
export interface SaveState { panel: PanelState; checkpoint: Checkpoint | null }

export function readSaved(value: Partial<SaveState> | null): SaveState {
  const panel = value?.panel;
  const position = panel?.position;
  const old = value?.checkpoint;
  const checkpoint = old && Number.isFinite(old.at) && typeof old.day === "string" && Array.isArray(old.recent)
    ? {
        at: old.at, day: old.day,
        dayPaths: Array.isArray(old.dayPaths)
          ? old.dayPaths.filter(path => typeof path === "string").slice(0, 512) : null,
        recent: old.recent.filter(row => row && typeof row.path === "string" &&
          Number.isFinite(row.firstSeen) && typeof row.unread === "boolean").slice(0, 100),
      }
    : null;
  return {
    panel: {
      collapsed: typeof panel?.collapsed === "boolean" ? panel.collapsed : false,
      position: position && Number.isFinite(position.x) && Number.isFinite(position.y) ? position : null,
    },
    checkpoint,
  };
}
