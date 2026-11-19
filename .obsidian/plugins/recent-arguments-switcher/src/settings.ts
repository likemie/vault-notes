import type { Checkpoint } from "./recent-store";

export const ARGUMENT_ROOT = "wiki/arguments/";
export const BATCH_MS = 200;

export interface PanelState { dock: "right"; collapsed: boolean; centerY: number | null }
export interface SaveState { panel: PanelState; checkpoint: Checkpoint | null }

export function readSaved(value: Partial<SaveState> | null): SaveState {
  const panel = value?.panel;
  const docked = panel?.dock === "right";
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
      dock: "right",
      collapsed: docked && typeof panel.collapsed === "boolean" ? panel.collapsed : true,
      centerY: docked && typeof panel.centerY === "number" && Number.isFinite(panel.centerY) ? panel.centerY : null,
    },
    checkpoint,
  };
}
