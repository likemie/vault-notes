export interface SearchState {
  centerY: number | null;
  width: number;
  height: number;
  hidden: boolean;
  exactAliases: boolean;
}

export function clamp(value: number, min: number, max: number): number {
  return Math.min(Math.max(value, min), Math.max(min, max));
}

export function readSettings(saved: Partial<SearchState> | null): SearchState {
  function dimension(value: unknown, fallback: number, min: number, max: number): number {
    return typeof value === "number" && Number.isFinite(value) ? clamp(value, min, max) : fallback;
  }
  return {
    centerY: typeof saved?.centerY === "number" && Number.isFinite(saved.centerY) ? saved.centerY : null,
    width: dimension(saved?.width, 320, 240, 600),
    height: dimension(saved?.height, 330, 156, 720),
    hidden: saved?.hidden === true,
    exactAliases: saved?.exactAliases === true,
  };
}
