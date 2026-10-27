#!/usr/bin/env python3
"""直接执行输出任务，不分析或修改脚本。适用于任何有文件和终端工具的 AI。
start ARGUMENT：创建/续接任务；直接传 ARGUMENT 等价于 start。
当前 AI 只处理本批→存 result.json→accept JOB（检查并登记完成）→停止，等用户再次指示才取下一批。
plan ARGUMENT：仅分批；status JOB：进度；run JOB：同 next，不启动 AI。
run-codex JOB [--retry]：显式可选的 Codex CLI 适配器，每次只执行一批。
start/plan/next/run/status 不调用 AI 或修改知识条目；进度可跨 AI 续接。
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import re
import shlex
import shutil
import subprocess
import sys
import unicodedata
from pathlib import Path

import vaultlib

ROOT = vaultlib.ROOT
VENV = ROOT / ".venv/bin/python3"
if __name__ == "__main__":
    vaultlib.ensure_venv()

import yaml

FIELDS = tuple(f"related_{kind}" for kind in (
    "concepts", "theories", "methods", "instruments", "persons", "facts"
))
TARGET_TYPES = {"concept", "theory", "method", "instrument", "person", "fact"}
LINK = re.compile(r"(?<!!)\[\[([^\]\n]+)\]\]")
INSTRUCTIONS = """本次只处理下列一批，完成后停止；未经用户再次指示，不获取或处理下一批。
遵守 AGENTS.md、vault-schema.md；用 wiki/index.json 定位。首先完整读取现有目标条目、下列必读规范及本批模板，判断模板符合性：结构、内容归位或 Callout 不符，必须列入“重构”，不以有无新增信息为前提。不能凭记忆或沿用旧格式；规范优先于模板，不建无证据的空章节，不复制模板说明。
完整阅读指定 Argument、经 source record 定位的原文，核对链接语境与概念含义，并回查已有引用。误链、同名异义、普通词误配专业概念、仅提及而无实质讨论/应用/证据，不据此补入内容；原条目符合模板时记“不变”，否则仍按模板重构。无法核验、原文未读全或证据不足则停止，不得以“不变”冒充完成。
重构标准：原条目不符合对应模板，必须整体“重构”；模板符合时，若新材料能够深化或改变现有认识，且已有信息足以形成更合理的论述结构，则进行整体“重构”；若主要增加事实、证据、解释或细节，则在现有结构下“补充”；无新增有效信息则“不变”。
重构必须充分整合新旧内容，保留已有的有效信息、重要细节和论证深度，避免因结构调整造成信息损失或过度概括。对新旧材料中的差异与矛盾，应先核实其来源、证据及适用条件。确有学术分歧的，保留不同观点并纳入“争议”部分；已经证实的事实性错误则直接纠正。
无论重构还是补充，都应检查新旧内容的衔接，消除重复论述，保留页码与引用；完成后逐节对照模板检查结构、内容归位及 Callout。
确认误链时运行 .venv/bin/python3 scripts/wiki_linker.py exclude <所在条目路径> --sentence '<完整可见句子>' --target '<目标路径>' --record-only 登记，普通补链时去除，保留本任务 Argument 快照；仅提及不记例外。只改本批非 Argument 条目正文及必要例外记录。
按目标顺序将等量状态写入指定 result.json 的 items 数组，每项只能为“不变／重构／补充”之一，不写其他字段。运行下方 accept，由其执行正常增量 vault_index→vault_lint 并登记本批完成，无须重复手动检查；随后停止，失败也停止。无需计划、进度或逐条报告，受阻说明原因。
"""


def stamp():
    return dt.datetime.now(dt.timezone.utc).isoformat()


def read_json(path):
    return vaultlib.load_json(path, required=True)


def write_json(path, value):
    vaultlib.dump_json(path, value, indent=2, atomic=True)


def fingerprint(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def key(value):
    return unicodedata.normalize("NFC", value).casefold()


def target(value):
    value = str(value).strip().removeprefix("[[").removesuffix("]]")
    return vaultlib.parse_wikilink(value)[0].removesuffix(".md").strip()


def read_note(path):
    text = path.read_text(encoding="utf-8")
    split = vaultlib.split_frontmatter(text)
    if not split.found:
        raise ValueError(f"缺少 frontmatter: {path}")
    return yaml.safe_load(split.raw) or {}, split.body


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


def entry_template(entry):
    meta, _ = read_note(ROOT / entry["path"])
    kind = meta.get("type")
    if kind != entry["type"] or kind not in TARGET_TYPES:
        raise ValueError(f"条目类型与任务不符，请重新生成任务: {entry['path']}")
    if kind == "fact":
        subtype = meta.get("subtype")
        if subtype not in {"policy", "event", "organization", "program"}:
            raise ValueError(f"Fact 缺少有效 subtype，无法选择模板: {entry['path']}")
        name = f"template-fact-{subtype}.md"
    elif kind == "person" and (meta.get("subtype") == "school" or "/persons/schools/" in entry["path"]):
        name = "template-school.md"
    else:
        name = f"template-{kind}.md"
    path = Path("wiki/templates") / name
    if not (ROOT / path).is_file():
        raise ValueError(f"缺少对应模板: {path}")
    return path.as_posix()


def grouped_batches(entries, batch_size):
    """Keep one type and one concrete template per batch, preserving entry order."""
    groups = {}
    for entry in entries:
        template = entry_template(entry)
        groups.setdefault((entry["type"], template), []).append(entry)
    for kind in ("concept", "theory", "method", "instrument", "person", "fact"):
        for (group_kind, template), members in groups.items():
            if group_kind == kind:
                for start in range(0, len(members), batch_size):
                    yield {"type": kind, "template": template, "entries": members[start:start + batch_size]}


def prepare_prompt(job, state, batch, *, managed=False):
    """Render the latest instructions without changing the queued target snapshot."""
    folder = job / f"batch-{batch['number']:03d}"
    instructions = INSTRUCTIONS
    if managed:
        instructions = instructions.replace(
            "运行下方 accept，由其执行正常增量 vault_index→vault_lint 并登记本批完成，无须重复手动检查；随后停止，失败也停止。",
            "保存结果后停止；外部执行器负责正常增量 vault_index→vault_lint 及登记本批完成，勿调用本脚本。",
        )
    entry_templates = [entry_template(entry) for entry in batch["entries"]]
    templates = list(dict.fromkeys(entry_templates))
    if batch.get("template") and (templates != [batch["template"]]
            or any(e["type"] != batch["type"] for e in batch["entries"])):
        raise ValueError("本批类型或模板已变化，请重新生成任务")
    prompt = instructions + f"\nArgument：{state['argument']}\n"
    if len(templates) == 1:
        prompt += f"本批类型：{batch['entries'][0]['type']}；统一模板：{templates[0]}\n"
    prompt += "目标（按序）：\n"
    for position, (entry, template) in enumerate(zip(batch["entries"], entry_templates), 1):
        # Old queues remain readable without reordering existing status records.
        suffix = f" → 模板 {templates.index(template) + 1}" if len(templates) > 1 else ""
        prompt += f"{position}. {entry['path']}{suffix}\n"
    prompt += "\n必读规范：wiki/templates/TEMPLATE-SPEC.md、wiki/templates/CALLOUTS.md\n"
    if len(templates) > 1:
        prompt += "\n".join(f"模板 {i}：{path}" for i, path in enumerate(templates, 1)) + "\n"
    prompt += f"\n结果：{folder / 'result.json'}\n"
    (folder / "prompt.md").write_text(prompt, encoding="utf-8")
    write_json(folder / "batch-result.schema.json", receipt_schema([e["path"] for e in batch["entries"]]))
    return prompt


def plan(args):
    anchor, entries, added = collect(args.argument)
    if not entries:
        raise ValueError("没有可处理的关联条目")
    batches = list(grouped_batches(entries, args.batch_size))
    job = (args.out or ROOT / "output/related-updates" / (
        Path(anchor["path"]).stem + "-" + dt.datetime.now().strftime("%Y%m%d-%H%M%S")
    )).resolve()
    if job == ROOT.resolve() or ROOT.resolve() not in job.parents:
        raise ValueError("任务目录必须位于当前 vault 内")
    job.mkdir(parents=True, exist_ok=False)
    state = {"version": 1, "root": str(ROOT), "created": stamp(),
             "argument": anchor["path"], "argument_hash": fingerprint(ROOT / anchor["path"]),
             "batches": []}
    for group in batches:
        number = len(state["batches"]) + 1
        folder = job / f"batch-{number:03d}"
        folder.mkdir()
        batch = {"number": number, "status": "pending", **group}
        prepare_prompt(job, state, batch)
        state["batches"].append(batch)
    write_json(job / "state.json", state)
    print(f"任务：{job}\n关联条目 {len(entries)} 个，按类型/模板分为 {len(state['batches'])} 批；每批最多 {args.batch_size} 个。")
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
        print("完成。")
        return
    if batch["status"] == "running":
        raise ValueError("本批已标记为 running；先确认执行器已经停止，再处理现有任务，不要重复启动")
    print(f"\n第 {batch['number']}/{len(state['batches'])} 批\n")
    print(prepare_prompt(job, state, batch))
    command = [".venv/bin/python3", "scripts/related_update.py"]
    job_arg = job.relative_to(ROOT.resolve()).as_posix()
    print(f"工作目录：{ROOT}\n保存结果后检查本批，然后停止：\n" + shlex.join(command + ["accept", job_arg]))


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
        print(f"第 {batch['number']} 批通过检查。本次停止，等待用户指示。")


def advance_job(args):
    """Compatibility entry point: accept only, never reveal the next batch."""
    accept_job(args)


def run_codex_job(args):
    """Optional CLI adapter; never used by the provider-neutral chat workflow."""
    with vault_lock():
        job, state = load_job(args.job)
        check_argument(state)
        executable = shutil.which("codex")
        if not executable:
            raise ValueError("未找到 codex CLI；仍可用 next 输出指令，在聊天中执行")
        if (batch := unfinished(state)) is not None:
            check_argument(state)
            if batch["status"] != "pending" and not args.retry:
                raise ValueError(f"第 {batch['number']} 批状态为 {batch['status']}；核对日志后用 --retry 继续")
            folder = job / f"batch-{batch['number']:03d}"
            prepare_prompt(job, state, batch, managed=True)
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
            print(f"第 {batch['number']} 批通过检查。本次停止，等待用户指示。", flush=True)
            return
        print("所有批次已通过检查。")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    for name, help_text in (("start", "当前聊天执行：生成或续接任务，直接输出本批完整指令"),
                            ("plan", "仅生成清单和分批指令，不调用 AI")):
        create = commands.add_parser(name, help=help_text)
        create.add_argument("argument", help="Argument 标题或完整路径")
        create.add_argument("--batch-size", type=int, default=5)
        create.add_argument("--out", type=Path)
    for command in ("next", "status", "run", "accept", "advance", "run-codex"):
        help_text = {"run": "通用 AI 会话执行：输出本批指令，不启动任何 AI CLI",
                     "advance": "兼容旧命令：只校验本批并停止，同 accept",
                     "run-codex": "可选适配器：明确使用 Codex CLI 执行一批后停止"}.get(command)
        sub = commands.add_parser(command, help=help_text)
        sub.add_argument("job", type=Path)
        if command in {"run", "run-codex"}:
            sub.add_argument("--retry", action="store_true", help=("重试首个未完成批次，保留旧结果" if command == "run-codex"
                             else "兼容参数；由当前 AI 复查首个未完成批次，不启动外部执行器"))
    argv = sys.argv[1:]
    if not argv:
        print('请直接执行任务，不必分析本脚本。当前聊天中的 AI 应根据用户指定的 Argument 运行：')
        print('适用于任何具备本地文件读写及终端能力的 AI；不依赖 Codex CLI 或模型 API。')
        print(shlex.join([str(VENV), str(Path(__file__).resolve()), "start", "Argument名称或完整路径"]))
        print('只处理输出的这一批→存 result.json→accept 检查→停止。等用户再次指示后才取下一批。')
        print('若上下文没有明确的 Argument，请只询问需要处理哪篇文献。使用 --help 查看其他命令。')
        return 0
    if argv[0] not in {"start", "plan", "next", "status", "run", "accept", "advance", "run-codex"} and not argv[0].startswith("-"):
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
        elif args.command == "advance":
            advance_job(args)
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
