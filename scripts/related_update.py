#!/usr/bin/env python3
"""直接执行输出任务，不分析或修改脚本。适用于任何有文件和终端工具的 AI。
start ARGUMENT：创建/续接任务；直接传 ARGUMENT 等价于 start。
当前 AI 处理本批→存 result.json→accept JOB→成功后 next JOB，直到完成或受阻。
plan ARGUMENT：仅分批；status JOB：进度；run JOB：同 next，不启动 AI。
run-codex JOB [--all] [--retry]：显式可选的 Codex CLI 适配器。
start/plan/next/run/status 不调用 AI 或修改知识条目；进度可跨 AI 续接。
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import re
import shlex
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
INSTRUCTIONS = """当前 AI 直接更新本批条目，不分析脚本；不限产品/模型，无须 AI CLI/API。
1. 遵守 AGENTS.md、vault-schema.md、vault-use.md；用 wiki/index.json 定位；读 wiki/templates/ 下 TEMPLATE-SPEC.md、CALLOUTS.md 及对应最新模板。
2. 完整阅读指定 Argument、其原文及本批现有条目；由来源章节/sources→source record 定位 PDF/EPUB。Argument/摘要不等于原文，未核验不得声称核验。对照链接上下文、原文与条目定义/对象/范围核实关联；成立后沿已有引用核对 Argument 和相关原文。
3. 误链、同名异义、普通词误配专业概念、仅提及（无实质讨论、定义、论证、证据、实际应用或案例），以及无新增有效信息，均记“不变”，不改内容、格式或 Callout。普通“假设”不等于研究假设；词频/链接不证明关联，实质讨论不要求独立章节。关联无法核实、原文缺失/未读全或证据不足时停止并简报，保持未完成，禁止编造或以“不变”冒充完成。
4. 新材料深化/改变认识且积累足以支持更合理结构时“重构”；增加事实、证据、解释或细节时在现有结构内“补充”。内部核对新旧有效信息、重要细节、来源及论证深度，防止重构遗漏或过度概括；核实差异的来源/证据/条件，真实学术分歧保留于争议，已证实事实错误纠正。精确修改、整合去重、衔接连贯，按模板统一排版/Callout，正文保留页码与完整引用。
5. 只改本批 Concept/Theory/Method/Instrument/Person/Fact 正文及必要写作例外；所有 Argument 只读。不改无关文件/state.json，不手改 related_*、sources、extracted_to；不自动标准补链/关系同步，不提交/推送/另开 AI/子代理/递归建任务。允许 accept、next 推进。有效写作例外静默复用；未审命中逐项实审、优先改写，不批量批准或弱化检查。
6. 批末依次运行 .venv/bin/python3 scripts/vault_index.py 和 .venv/bin/python3 scripts/vault_lint.py，正常增量、不限路径、不压制输出。失败报告全部未解决项并停止，不为清零修改无关并行工作。
7. 全批阅读/处理完成后，按目标顺序只存 {"items":["不变","重构","补充"]} 到指定 result.json，数量须一致，无其他字段/报告。accept 成功后 next，继续至完成或受阻。聊天仅报进度；最终简报三类数量/未解决项，按 AGENTS.md 报告本次改写及新增写作例外（无则说明），不重复旧例外。
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
    return {"type": "object", "additionalProperties": False, "properties": {
        "items": {"type": "array", "items": {"type": "string", "enum": ["不变", "重构", "补充"]},
                  "minItems": len(paths), "maxItems": len(paths)},
    }, "required": ["items"]}


def prepare_prompt(job, state, batch):
    """Render the latest instructions without changing the queued target snapshot."""
    folder = job / f"batch-{batch['number']:03d}"
    prompt = INSTRUCTIONS + f"\nArgument：{state['argument']}\n目标（按序）：\n"
    for position, entry in enumerate(batch["entries"], 1):
        prompt += f"{position}. {entry['path']}\n"
    prompt += f"\n批次目录：{folder}\nschema：batch-result.schema.json；结果：该目录下 result.json。\n"
    (folder / "prompt.md").write_text(prompt, encoding="utf-8")
    write_json(folder / "batch-result.schema.json", receipt_schema([e["path"] for e in batch["entries"]]))
    return prompt


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
    for start in range(0, len(entries), args.batch_size):
        number = len(state["batches"]) + 1
        batch_entries = entries[start:start + args.batch_size]
        folder = job / f"batch-{number:03d}"
        folder.mkdir()
        batch = {"number": number, "status": "pending", "entries": batch_entries}
        prepare_prompt(job, state, batch)
        state["batches"].append(batch)
    write_json(job / "state.json", state)
    print(f"任务：{job}\n关联条目 {len(entries)} 个，共 {len(state['batches'])} 批；每批最多 {args.batch_size} 个。")
    if added:
        print(f"正文补发现 {added} 个未列入 related_* 的条目（字段可能滞后）；未改写关联字段。")
    return job


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


def emit_task(job, state):
    check_argument(state)
    batch = unfinished(state)
    if batch is None:
        print("完成。仅报三类数量/未解决项、本次改写及新增写作例外（无则说明）；不重做、不写长报告。")
        return
    if batch["status"] == "running":
        raise ValueError("本批已标记为 running；先确认执行器已经停止，再处理现有任务，不要重复启动")
    print(f"\n第 {batch['number']}/{len(state['batches'])} 批\n")
    print(prepare_prompt(job, state, batch))
    command = [".venv/bin/python3", "scripts/related_update.py"]
    job_arg = job.relative_to(ROOT.resolve()).as_posix()
    print(f"工作目录：{ROOT}\n处理并保存后执行：\n" + shlex.join(command + ["accept", job_arg]))
    print("仅退出码为 0 后执行并继续下一批：\n" + shlex.join(command + ["next", job_arg]))


def start_job(args):
    anchor, _, _ = collect(args.argument)
    job = (args.out or ROOT / "output/related-updates" / (
        Path(anchor["path"]).stem + "-" + hashlib.sha256(anchor["path"].encode()).hexdigest()[:8]
    )).resolve()
    if job.exists():
        job, state = load_job(job)
        if state["argument"] != anchor["path"]:
            raise ValueError("此任务目录属于另一个 Argument，请指定新的 --out 目录")
        if any(len(b["entries"]) > args.batch_size for b in state["batches"]):
            raise ValueError("现有任务批次大于指定 batch-size，请用新的 --out 目录重新生成")
    else:
        args.out = job
        plan(args)
        job, state = load_job(job)
    emit_task(job, state)


def gates():
    for script in ("vault_index.py", "vault_lint.py"):
        check = subprocess.run([str(VENV), str(ROOT / "scripts" / script)], cwd=ROOT)
        if check.returncode:
            raise ValueError(f"{script} 未通过（退出码 {check.returncode}），停止后续批次")


def validate_receipt(result, batch):
    if isinstance(result, dict) and set(result) == {"items"}:
        statuses = result["items"]
        if (not isinstance(statuses, list) or len(statuses) != len(batch["entries"])
                or not all(isinstance(s, str) and s in {"不变", "重构", "补充"} for s in statuses)):
            raise ValueError("结果须按目标顺序填写等量的“不变／重构／补充”状态；受阻时保持未完成")
        return
    # Accept existing detailed receipts so in-progress jobs need no rewrite.
    legacy = "source_verified" not in result
    required = {"items", "new_exceptions", "unresolved"}
    if not legacy:
        required.add("source_verified")
    if set(result) != required:
        raise ValueError("结果字段不符合最简记录或旧版格式")
    if not all(isinstance(result[k], list) for k in ("items", "new_exceptions", "unresolved")):
        raise ValueError("items、new_exceptions、unresolved 应为列表")
    if not legacy and result["source_verified"] is not True:
        raise ValueError("本批原文核验未完成")
    expected = [e["path"] for e in batch["entries"]]
    items = result.get("items", [])
    if sorted(i["path"] for i in items) != sorted(expected):
        raise ValueError("结果遗漏、重复或包含本批以外的目标")
    for item in items:
        if item["action"] not in {"restructure", "supplement", "unchanged"}:
            raise ValueError(f"条目受阻: {item['path']}: {item['reason']}")
        if not isinstance(item["reason"], str):
            raise ValueError(f"reason 应为字符串: {item['path']}")
        if item["action"] == "unchanged" and not item["reason"].strip():
            raise ValueError(f"跳过条目须简记理由: {item['path']}")
        if not legacy and set(item) != {"path", "action", "reason"}:
            raise ValueError(f"每条只需 path、action、reason: {item['path']}")
        if legacy and (item["source_verified"] is not True or not item["sources_read"]
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
        if batch["status"] == "running":
            raise ValueError("本批正在运行，不能从另一个会话登记完成")
        gates()
        batch.update(status="done", finished=stamp())
        batch.pop("error", None)
        write_json(job / "state.json", state)
        print(f"第 {batch['number']} 批通过检查。")


def run_codex_job(args):
    """Optional CLI adapter; never used by the provider-neutral chat workflow."""
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
            prepare_prompt(job, state, batch)
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
    for name, help_text in (("start", "当前聊天执行：生成或续接任务，直接输出本批完整指令"),
                            ("plan", "仅生成清单和分批指令，不调用 AI")):
        create = commands.add_parser(name, help=help_text)
        create.add_argument("argument", help="Argument 标题或完整路径")
        create.add_argument("--batch-size", type=int, default=3)
        create.add_argument("--out", type=Path)
    for command in ("next", "status", "run", "accept", "run-codex"):
        help_text = {"run": "通用 AI 会话执行：输出本批指令，不启动任何 AI CLI",
                     "run-codex": "可选适配器：明确使用 Codex CLI 自动执行"}.get(command)
        sub = commands.add_parser(command, help=help_text)
        sub.add_argument("job", type=Path)
        if command in {"run", "run-codex"}:
            sub.add_argument("--all", action="store_true", help=("串行执行全部剩余批次，遇错停止" if command == "run-codex"
                             else "兼容参数；输出指令由当前 AI 按 accept / next 流程继续执行"))
            sub.add_argument("--retry", action="store_true", help=("重试首个未完成批次，保留旧结果" if command == "run-codex"
                             else "兼容参数；由当前 AI 复查首个未完成批次，不启动外部执行器"))
    argv = sys.argv[1:]
    if not argv:
        print('请直接执行任务，不必分析本脚本。当前聊天中的 AI 应根据用户指定的 Argument 运行：')
        print('适用于任何具备本地文件读写及终端能力的 AI；不依赖 Codex CLI 或模型 API。')
        print(shlex.join([str(VENV), str(Path(__file__).resolve()), "start", "Argument名称或完整路径"]))
        print('然后按输出逐批更新条目，保存 result.json，通过 accept 后执行 next，直到完成。')
        print('若上下文没有明确的 Argument，请只询问需要处理哪篇文献。使用 --help 查看其他命令。')
        return 0
    if argv[0] not in {"start", "plan", "next", "status", "run", "accept", "run-codex"} and not argv[0].startswith("-"):
        argv = ["start", *argv]
    args = parser.parse_args(argv)
    try:
        if args.command in {"start", "plan"}:
            if args.batch_size < 1:
                raise ValueError("batch-size 必须至少为 1")
            if args.command == "start":
                start_job(args)
            else:
                plan(args)
        elif args.command == "run-codex":
            run_codex_job(args)
        elif args.command == "accept":
            accept_job(args)
        else:
            job, state = load_job(args.job)
            if args.command == "status":
                for batch in state["batches"]:
                    print(f"{batch['number']:03d} {batch['status']}: " + ", ".join(e["title"] for e in batch["entries"]))
                    if batch.get("error"):
                        print("    " + batch["error"])
            else:
                emit_task(job, state)
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError) as error:
        print(f"错误：{error}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("执行中断；已保存状态。", file=sys.stderr)
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())
