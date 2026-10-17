#!/usr/bin/env python3
"""Build batches of related-entry review prompts; optionally run Codex serially.

plan ARGUMENT [--batch-size 3] [--out DIR] creates a new, resumable job.
next JOB prints the first unfinished batch prompt; status JOB shows progress.
accept JOB validates result.json from a manually executed batch and runs gates.
run JOB [--all] [--retry] calls codex exec, then independently runs vault gates.
No AI calls or wiki edits occur during plan/next/status.
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import re
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
VENV = ROOT / ".venv/bin/python3"
if __name__ == "__main__" and VENV.exists() and Path(sys.prefix).resolve() != ROOT / ".venv":
    import os
    os.execv(str(VENV), [str(VENV), *sys.argv])

import yaml

FIELDS = tuple(f"related_{kind}" for kind in (
    "concepts", "theories", "methods", "instruments", "persons", "facts"
))
TARGET_TYPES = {"concept", "theory", "method", "instrument", "person", "fact"}
LINK = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
INSTRUCTIONS = """你正在维护一个教育研究学术知识库。本任务是更新关联条目正文，不是手动刷新 related_* 字段。
仅更新 Concept、Theory、Method、Instrument、Person、Fact。排除 related_arguments 及正文中的所有 Argument 目标；Argument 只作为阅读、引用和证据追溯材料，不修改其正文。

先读取 AGENTS.md、vault-schema.md、vault-use.md；用 wiki/index.json 定位条目。读取 wiki/templates/TEMPLATE-SPEC.md、wiki/templates/CALLOUTS.md 和每个目标类型的最新模板。

完整阅读指定 Argument 和它对应的原文（通过 Argument 的来源章节、sources 和 source record 定位 PDF / EPUB，不把 Argument 当原文）。完整阅读本批每个现有知识条目；沿其引用回查已有 Argument 和支持相关主张的原文上下文。只读到提炼或摘要时不得声称核验了原文。原文缺失、无法完整阅读或关键证据不足，必须标记 blocked 并具体说明，不用常识补齐。

对于本批的每个目标，执行以下要求：

请完整阅读原文及现有知识库条目，判断当前积累的信息是否足以支持结构性重构，还是仅需补充完善。若新材料能够深化或改变现有认识，且已有信息足以形成更合理的论述结构，则进行整体重构；若主要增加事实、证据、解释或细节，则在现有结构下补充。
重构必须充分整合新旧内容，保留已有的有效信息、重要细节和论证深度，避免因结构调整造成信息损失或过度概括。对新旧材料中的差异与矛盾，确有学术分歧的，保留不同观点并纳入“争议”部分；已经证实的事实性错误则直接纠正。
无论重构还是补充，都应检查新旧内容的衔接，消除重复论述。按照wiki/templates里对应的模板统一排版及 Callout 格式，确保条目的信息完整性、逻辑连贯性和学术准确性。

具体执行边界：

- 本批逐项审读，不因存在 related 链接就强行增补；顺带提及且不足以支持更新的条目可以 unchanged，但必须说明判断依据。
- 重构前列出现有有效内容及其来源，完成后逐项核对保留情况；明确调整章节与整合的理由。按规范精确修改已有文件。
- 每项保留页码和完整的文献引用关系。分别报告 restructure、supplement、unchanged 或 blocked，并记录实际读取的来源、原文范围和具体理由。
- 仅修改本批列出的目标正文及必要的写作例外记录。不要改写指定 Argument、无关条目或本任务的 state.json；生成字段由规范脚本维护。不要提交、推送、启动其他 AI 会话、子代理或递归调用 related_update.py。
- 不手工维护 related_*、Argument sources、source record extracted_to，不自动运行标准补链/关系同步流程。
- 有效写作例外静默复用；未匹配的写作用词和否定转折须逐项实质审查，优先准确改写。禁止批量批准 ID 或弱化检查。
- 结束前依次运行 .venv/bin/python3 scripts/vault_index.py 和 .venv/bin/python3 scripts/vault_lint.py，使用正常增量范围，不限定路径、不压制输出。失败时报告全部未解决项，不声称完成，也不修改无关的并行工作来清零检查。
- 用 batch-result.schema.json 规定的 JSON 汇报本批所有目标，不能遗漏、重复或用总述代替逐项结论。source_verified=true 仅在本次确实完成以上原文阅读和核验时填写；sources_read 写实际文件/URL及页码或章节。rewrites 记录具体改写；new_exceptions 只列本次新增批准的 entry 与 ID，无新增则为空数组。
"""


def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path, value):
    temp = path.with_suffix(path.suffix + ".tmp")
    temp.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temp.replace(path)


def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def key(value):
    return unicodedata.normalize("NFC", value).casefold()


def target(value):
    value = str(value).strip().removeprefix("[[").removesuffix("]]")
    return value.replace("\\|", "|").split("|", 1)[0].split("#", 1)[0].removesuffix(".md").strip()


def read_note(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", text, re.S)
    if not match:
        raise ValueError(f"缺少 frontmatter: {path}")
    return yaml.safe_load(match[1]) or {}, text[match.end():]


class Lookup:
    def __init__(self):
        self.entries = read_json(ROOT / "wiki/index.json")
        self.paths = {}
        self.names = {}
        for entry in self.entries:
            self.paths[key(entry["path"].removesuffix(".md"))] = entry
            for name in {entry["title"], Path(entry["path"]).stem, *entry.get("aliases", [])}:
                candidates = self.names.setdefault(key(name), {})
                candidates[entry["path"]] = entry

    def resolve(self, value):
        name = target(value)
        path = Path(name)
        if path.is_absolute():
            name = path.resolve().relative_to(ROOT.resolve()).as_posix()
        exact = self.paths.get(key(name.removesuffix(".md")))
        if exact:
            return exact
        matches = list(self.names.get(key(name), {}).values())
        if len(matches) > 1:
            raise ValueError(f"条目不唯一，请使用完整路径: {value}")
        return matches[0] if matches else None


def body_links(body):
    # Fences and inline code are examples, not evidence of a relationship.
    lines = []
    fence = None
    for line in body.splitlines():
        marker = re.match(r"^\s*(?:>\s*)*(`{3,}|~{3,})", line)
        if marker:
            token = marker[1]
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            lines.append(line)
    clean = re.sub(r"(`+).*?\1", "", "\n".join(lines))
    clean = re.sub(r"<!--.*?-->|%%.*?%%", "", clean, flags=re.S)
    return [m[1] for m in LINK.finditer(clean)]


def collect(argument):
    lookup = Lookup()
    anchor = lookup.resolve(argument)
    if not anchor or anchor["type"] != "argument":
        raise ValueError("请指定索引中已有的 Argument 标题或完整路径")
    meta, body = read_note(ROOT / anchor["path"])
    entries = {}
    for field in FIELDS:
        values = meta.get(field, []) or []
        if not isinstance(values, list):
            raise ValueError(f"{field} 应为列表")
        for value in values:
            entry = lookup.resolve(value)
            if not entry:
                raise ValueError(f"{field} 无法解析: {value}；请先核对条目或刷新索引")
            if entry["type"] in TARGET_TYPES:
                entries.setdefault(entry["path"], {**entry, "discovered_by": []})["discovered_by"].append(field)
    added = 0
    for value in body_links(body):
        entry = lookup.resolve(value)
        if not entry or entry["type"] not in TARGET_TYPES:
            continue
        if entry["path"] not in entries:
            entries[entry["path"]] = {**entry, "discovered_by": []}
            added += 1
        if "body" not in entries[entry["path"]]["discovered_by"]:
            entries[entry["path"]]["discovered_by"].append("body")
    return anchor, list(entries.values()), added


def receipt_schema(paths):
    item = {"type": "object", "additionalProperties": False, "properties": {
        "path": {"type": "string", "enum": paths},
        "action": {"type": "string", "enum": ["restructure", "supplement", "unchanged", "blocked"]},
        "source_verified": {"type": "boolean"},
        "sources_read": {"type": "array", "items": {"type": "string"}},
        "reason": {"type": "string"},
        "rewrites": {"type": "string"},
    }}
    item["required"] = list(item["properties"])
    exception = {"type": "object", "additionalProperties": False,
                 "properties": {"entry": {"type": "string"}, "id": {"type": "string"}},
                 "required": ["entry", "id"]}
    return {"type": "object", "additionalProperties": False, "properties": {
        "items": {"type": "array", "items": item},
        "new_exceptions": {"type": "array", "items": exception},
        "unresolved": {"type": "array", "items": {"type": "string"}},
    }, "required": ["items", "new_exceptions", "unresolved"]}


def plan(args):
    anchor, entries, added = collect(args.argument)
    if not entries:
        raise ValueError("没有可处理的关联条目")
    job = (args.out or ROOT / "output/related-updates" / (
        Path(anchor["path"]).stem + "-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    )).resolve()
    if job == ROOT.resolve() or ROOT.resolve() not in job.parents:
        raise ValueError("任务目录必须位于当前 vault 内")
    job.mkdir(parents=True, exist_ok=False)
    state = {"version": 1, "root": str(ROOT), "created": stamp(),
             "argument": anchor["path"], "argument_hash": fingerprint(ROOT / anchor["path"]),
             "batches": []}
    instruction = INSTRUCTIONS
    for start in range(0, len(entries), args.batch_size):
        number = len(state["batches"]) + 1
        batch_entries = entries[start:start + args.batch_size]
        folder = job / f"batch-{number:03d}"
        folder.mkdir()
        prompt = instruction + f"\n\n指定 Argument：{anchor['path']}\n\n本批目标（逐项完成）：\n"
        for entry in batch_entries:
            prompt += f"- {entry['path']}（{entry['type']}；{entry['title']}）\n"
        prompt += f"\n本批结果 schema：{folder / 'batch-result.schema.json'}\n"
        prompt += f"手动在聊天中执行时，将符合 schema 的最终 JSON 保存到：{folder / 'result.json'}\n"
        (folder / "prompt.md").write_text(prompt, encoding="utf-8")
        write_json(folder / "batch-result.schema.json", receipt_schema([e["path"] for e in batch_entries]))
        state["batches"].append({"number": number, "status": "pending", "entries": batch_entries})
    write_json(job / "state.json", state)
    print(f"任务：{job}\n关联条目 {len(entries)} 个，共 {len(state['batches'])} 批；每批最多 {args.batch_size} 个。")
    if added:
        print(f"正文补发现 {added} 个未列入 related_* 的条目（字段可能滞后）；未改写关联字段。")


def load_job(job):
    job = job.resolve()
    state = read_json(job / "state.json")
    if state.get("version") != 1 or state.get("root") != str(ROOT):
        raise ValueError("任务版本或 vault 路径不匹配")
    if any(e.get("type") not in TARGET_TYPES for b in state["batches"] for e in b["entries"]):
        raise ValueError("此旧任务包含 Argument 或其他不支持的更新目标，请重新生成任务")
    return job, state


def unfinished(state):
    return next((b for b in state["batches"] if b["status"] != "done"), None)


@contextlib.contextmanager
def vault_lock():
    directory = ROOT / "output/related-updates"
    directory.mkdir(parents=True, exist_ok=True)
    with (directory / ".vault-run.lock").open("w") as lock:
        try:
            fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError("此 vault 已有一个关联更新执行器在运行")
        yield


def check_argument(state):
    if fingerprint(ROOT / state["argument"]) != state["argument_hash"]:
        raise ValueError("指定 Argument 已改变。请重新生成任务，避免沿用旧目标清单。")


def gates():
    for script in ("vault_index.py", "vault_lint.py"):
        check = subprocess.run([str(VENV), str(ROOT / "scripts" / script)], cwd=ROOT)
        if check.returncode:
            raise ValueError(f"{script} 未通过（退出码 {check.returncode}），停止后续批次")


def validate_receipt(result, batch):
    if set(result) != {"items", "new_exceptions", "unresolved"}:
        raise ValueError("结果必须包含 items、new_exceptions、unresolved")
    if not all(isinstance(result[k], list) for k in result):
        raise ValueError("结果的三个字段均应为列表")
    expected = [e["path"] for e in batch["entries"]]
    items = result.get("items", [])
    if sorted(i["path"] for i in items) != sorted(expected):
        raise ValueError("结果遗漏、重复或包含本批以外的目标")
    for item in items:
        if item["action"] not in {"restructure", "supplement", "unchanged"}:
            raise ValueError(f"条目受阻: {item['path']}: {item['reason']}")
        if (item["source_verified"] is not True or not item["sources_read"]
                or not isinstance(item["sources_read"], list)
                or not all(isinstance(s, str) and s.strip() for s in item["sources_read"])
                or not isinstance(item["reason"], str) or not item["reason"].strip()
                or not isinstance(item.get("rewrites"), str)):
            raise ValueError(f"原文核验记录不完整: {item['path']}")
    for exception in result["new_exceptions"]:
        if (set(exception) != {"entry", "id"} or not isinstance(exception["entry"], str)
                or not re.fullmatch(r"[0-9a-f]{16}", exception["id"])):
            raise ValueError("新批准写作例外的格式错误")
    if result.get("unresolved"):
        raise ValueError("存在未解决事项: " + "; ".join(result["unresolved"]))


def accept_job(args):
    with vault_lock():
        job, state = load_job(args.job)
        check_argument(state)
        batch = unfinished(state)
        if batch is None:
            print("所有批次已完成。")
            return
        receipt = job / f"batch-{batch['number']:03d}" / "result.json"
        validate_receipt(read_json(receipt), batch)
        gates()
        batch.update(status="done", finished=stamp())
        batch.pop("error", None)
        write_json(job / "state.json", state)
        print(f"第 {batch['number']} 批通过检查。")


def run_job(args):
    with vault_lock():
        job, state = load_job(args.job)
        check_argument(state)
        executable = shutil.which("codex")
        if not executable:
            raise ValueError("未找到 codex CLI；仍可用 next 输出指令，在聊天中执行")
        while (batch := unfinished(state)) is not None:
            check_argument(state)
            if batch["status"] != "pending" and not args.retry:
                raise ValueError(f"第 {batch['number']} 批状态为 {batch['status']}；核对日志后用 --retry 继续")
            folder = job / f"batch-{batch['number']:03d}"
            receipt = folder / "result.json"
            if receipt.exists():
                receipt.rename(folder / ("result-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S-%f") + ".json"))
            batch.update(status="running", started=stamp())
            write_json(job / "state.json", state)
            command = [executable, "exec", "--cd", str(ROOT), "--sandbox", "workspace-write",
                       "--output-schema", str(folder / "batch-result.schema.json"),
                       "--output-last-message", str(receipt), "-"]
            print(f"执行第 {batch['number']} 批，目标 {len(batch['entries'])} 个。", flush=True)
            try:
                with (folder / "execution.log").open("a", encoding="utf-8") as log:
                    process = subprocess.run(command, input=(folder / "prompt.md").read_text(encoding="utf-8"),
                                             text=True, cwd=ROOT, stdout=log, stderr=subprocess.STDOUT)
                if process.returncode:
                    raise ValueError(f"Codex 返回 {process.returncode}；见 {folder / 'execution.log'}")
                validate_receipt(read_json(receipt), batch)
                # Never accept the agent's success claim as a substitute for vault gates.
                gates()
                batch.update(status="done", finished=stamp())
                batch.pop("error", None)
            except (Exception, KeyboardInterrupt) as error:
                batch.update(status="blocked", error=str(error) or "执行被中断")
                write_json(job / "state.json", state)
                raise
            write_json(job / "state.json", state)
            print(f"第 {batch['number']} 批通过检查。", flush=True)
            if not args.all:
                return
        print("所有批次已通过检查。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    create = commands.add_parser("plan", help="生成清单和分批指令，不调用 AI")
    create.add_argument("argument", help="Argument 标题或完整路径")
    create.add_argument("--batch-size", type=int, default=3)
    create.add_argument("--out", type=Path)
    for command in ("next", "status", "run", "accept"):
        sub = commands.add_parser(command)
        sub.add_argument("job", type=Path)
        if command == "run":
            sub.add_argument("--all", action="store_true", help="串行执行全部剩余批次，遇错停止")
            sub.add_argument("--retry", action="store_true", help="重试首个未完成批次，保留旧结果")
    args = parser.parse_args()
    try:
        if args.command == "plan":
            if args.batch_size < 1:
                raise ValueError("batch-size 必须至少为 1")
            plan(args)
        elif args.command == "run":
            run_job(args)
        elif args.command == "accept":
            accept_job(args)
        else:
            job, state = load_job(args.job)
            if args.command == "status":
                for batch in state["batches"]:
                    print(f"{batch['number']:03d} {batch['status']}: " + ", ".join(e["title"] for e in batch["entries"]))
                    if batch.get("error"):
                        print("    " + batch["error"])
            elif (batch := unfinished(state)) is not None:
                print((job / f"batch-{batch['number']:03d}" / "prompt.md").read_text(encoding="utf-8"))
            else:
                print("所有批次已完成。")
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError) as error:
        print(f"错误：{error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("执行中断；已保存状态。", file=sys.stderr)
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
