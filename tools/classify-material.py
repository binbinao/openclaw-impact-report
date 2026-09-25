#!/usr/bin/env python3
"""Decide where newly added material belongs, from its content.

The site has no ingestion step: a file lands in the repo and a human decides
where it goes. This tool reads the material and proposes the path.

Order of operations — content first, path second:

    read file -> extract title + body
              -> score all 15 sections with IDF-weighted keyword patterns
              -> rank, report confidence
              -> derive reports/<date>-<slug>/ + an index.html card

Daily briefs (``*-brief-YYYY-MM-DD.html``, or a brief-looking title) are
detected first and routed to ``briefs/<YYYY-MM>/`` + ``#daily`` instead.

Accuracy (leave-one-out over this repo's 132 curated reports):

    top-1  75.0%
    top-3  93.9%

A single guess is therefore *not* reliable enough to apply silently. By default
the tool prints its ranked proposal and stops; ``--apply --yes`` places and
indexes it without asking.

Usage:
    python3 tools/classify-material.py NEW.html                  # propose
    python3 tools/classify-material.py --explain NEW.html        # + score table
    python3 tools/classify-material.py --apply --yes NEW.html    # place + index
    python3 tools/classify-material.py --eval                    # score accuracy
    python3 tools/classify-material.py --section truck FILE      # force section
    python3 tools/classify-material.py --slug my-slug FILE       # force slug
    python3 tools/classify-material.py --check FILE              # verify placement

Exit: 0 applied/clean, 1 proposal-only or drift found, 2 error.
"""

from __future__ import annotations

import argparse
import datetime as dt
import math
import re
import sys
from collections import Counter
from pathlib import Path

# --------------------------------------------------------------------------
# Section knowledge. Order = tie-break priority: specific verticals first,
# catch-alls last. Base weights: 3 decisive, 2 strong, 1 supporting. The final
# weight is derived from corpus IDF, so a pattern that fires in nearly every
# report (e.g. 经济, 接口, Agent) is automatically discounted.
# --------------------------------------------------------------------------

SECTIONS: list[tuple[str, str, list[tuple[str, int]]]] = [
    ("healthcare", "🏥 医疗信息化", [
        (r"HIS|EMR|EHR|PACS|RIS|LIS|医疗信息化|电子病历|医院信息", 3),
        (r"临床|诊疗|医疗", 2),
    ]),
    ("embodied", "🦾 具身智能 & 机器人", [
        (r"具身智能|人形机器人|灵巧手|世界模型|物理 ?AI|VLA|模仿学习", 3),
        (r"机器人|机械臂|sim2real|仿真到现实|中试基地|遥操作", 2),
        (r"抓取|locomotion|四足|双足", 2),
    ]),
    ("truck", "🚛 商用货车", [
        (r"商用货车|重卡|卡车|牵引车|货车座舱|卡车司机", 3),
        (r"座舱.*(司机|驾驶员)|车队运营|干线物流", 2),
    ]),
    ("auto", "🚗 汽车 & 智驾", [
        (r"智驾|智能驾驶|自动驾驶|ADAS|端到端|激光雷达|LIDAR|Robotaxi|NOA|域控", 3),
        (r"车企|主机厂|乘用车|新能源汽车|车规|Momenta|禾赛|地平线|小鹏|蔚来|理想|比亚迪|特斯拉|Tesla|Waymo", 2),
        (r"汽车|车辆|整车|汽配|Tier ?1|车圈", 2),
        (r"线控|底盘|电驱", 1),
    ]),
    ("chip", "🔬 芯片 & 算力", [
        (r"芯片|半导体|晶圆|制程|光刻|EDA|GPU|NPU|TPU|PPU|HBM|先进封装|Chiplet", 3),
        (r"英伟达|NVIDIA|AMD|Intel|台积电|中芯|平头哥|寒武纪|海光|昇腾|GTC|CUDA|训练集群", 2),
        (r"处理器|数据中心|液冷|NVLink|互联带宽", 2),
    ]),
    ("agent", "🧠 Agent & 工具链", [
        (r"Agent|智能体|OpenClaw|Hermes|MCP|工具调用|多智能体|multi-?agent|OMP", 3),
        (r"技能生态|skill|提示词工程|工作流自动化|编排|LangChain|AutoGPT|RAG|向量库|插件生态", 2),
        (r"copilot|代码生成|IDE", 1),
    ]),
    ("ai", "🤖 AI 大模型 & 产业", [
        (r"大模型|LLM|多模态|开源模型|模型.*(发布|横评|对比)|微调|fine-?tune|蒸馏|对齐|GPT|Claude|Gemini|Qwen|DeepSeek|Llama", 3),
        (r"人工智能|生成式|AIGC|预训练|token", 2),
        (r"算法|数据集|榜单|benchmark|评测", 2),
        (r"云厂商|云服务|算力平台|API ?定价|模型服务", 1),
    ]),
    ("policy", "🏛 政策 & 地缘", [
        (r"政策|规划|十五五|监管|合规|出口管制|制裁|禁令|地缘|国家安全|立法|白皮书|部委|国务院|发改委", 3),
        (r"央企|国企改革|战略规划|政府|两会|中美|关税|贸易战", 2),
        (r"认知战|信息战|舆论战", 2),
    ]),
    ("society", "🎓 教育 & 社会", [
        (r"教育|学校|课程|教学|学习法|考试|青少年|人才培养|招聘|就业", 3),
        (r"社会|公众|普通人|民生|人口|城市化|消费习惯", 2),
    ]),
    ("econ", "📈 宏观经济 & 数据", [
        (r"GDP|宏观经济|通胀|通缩|货币|利率|汇率|财政|股市|债市|衰退", 3),
        (r"资本流向|融资|投资回报|人均|收入|就业率|产业结构|进出口|区域经济|城市发展", 2),
        (r"经济|增长|数据.*(分析|洞察)|统计|可视化", 1),
    ]),
    ("chain", "🏭 供应链&产业", [
        (r"供应链|产能|制造|工厂|代工|供应商|尽职调查|产业链|上游|下游|库存|物流|采购", 3),
        (r"产业格局|生态位|国产替代|良率|产线|园区|基地|低空经济", 2),
        (r"通信硬件|消费电子", 2),
    ]),
    ("people", "👤 人物档案", [
        (r"专访|访谈录|人物|履历|传记|创始人|CEO|CTO|首席科学家", 3),
        (r"黄仁勋|杨植麟|Karpathy|李飞飞|张燕生|吴泰霖|李一帆|孙恺|向少卿", 3),
        (r"万字|团队背景|创业故事|个人经历", 2),
    ]),
    ("think", "💡 思考 & 人文", [
        (r"方法论|复盘|认知偏差|博弈论|领导力", 3),
        (r"哲学|民俗|节气|历史|传统|人文|心理|自我管理", 3),
        (r"管理|决策|启示|反思|洞见", 2),
        (r"文化", 1),
    ]),
    ("tech", "⚙️ 技术 & 基础架构", [
        (r"CAE|MBSE|PLM|数字线程|数字孪生|有限元|CFD|CAD", 3),
        (r"分布式|微服务|数据库|性能优化|可观测|运维|容器|Kubernetes|网络协议", 3),
        (r"系统工程|工程实践|最佳实践|技术选型|开源项目", 2),
        (r"架构|基础设施|调优|部署", 1),
    ]),
]

SECTION_IDS = [s[0] for s in SECTIONS]
HEADINGS = {s[0]: s[1] for s in SECTIONS}
# Short pill text per section, mirroring the existing index conventions
# (智驾, 宏观, 芯片 ...). Never derive this from the heading with a split().
TAG_LABELS = {
    "auto": "汽车", "truck": "商用车", "embodied": "具身", "chip": "芯片",
    "ai": "大模型", "agent": "Agent", "people": "人物", "chain": "供应链",
    "tech": "技术", "econ": "宏观", "policy": "政策", "society": "社会",
    "think": "思考", "healthcare": "医疗",
}
BRIEF_RE = re.compile(r"^(evolution|hn)-brief-(\d{4})-(\d{2})-(\d{2})\.html$")
DATE_RE = re.compile(r"(\d{4})-(\d{2})-(\d{2})")
ASCII_TOKEN_RE = re.compile(r"[A-Za-z][A-Za-z0-9+#-]{1,}")
GENERIC_STEMS = {"report", "index", "untitled", "temp", "tmp", "new", "final",
                 "output", "incoming", "draft", "material", "file", "doc",
                 "download", "untitled-1", "test"}
STOPWORDS = {"the", "and", "for", "with", "from", "into", "report", "deep", "dive",
             "analysis", "research", "in", "of", "on", "to", "a", "an", "vs", "by"}

DIM, BOLD, RED, GREEN, YELLOW, CYAN, RESET = (
    "\x1b[2m", "\x1b[1m", "\x1b[31m", "\x1b[32m", "\x1b[33m", "\x1b[36m", "\x1b[0m"
)


# --------------------------------------------------------------------------
# Text extraction
# --------------------------------------------------------------------------

def strip_tags(html: str) -> str:
    html = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html)).strip()


def extract_text(path: Path) -> tuple[str, str]:
    """Return (title, body_text) for HTML or Markdown."""
    raw = path.read_text(encoding="utf-8", errors="replace")
    if path.suffix.lower() in (".html", ".htm"):
        title = ""
        for pat in (r"<title[^>]*>(.*?)</title>", r"<h1[^>]*>(.*?)</h1>"):
            m = re.search(pat, raw, re.S | re.I)
            if m:
                title = strip_tags(m.group(1))
                break
        return title, strip_tags(raw)
    title = ""
    for line in raw.splitlines():
        if line.strip().startswith("# "):
            title = line.strip()[2:].strip()
            break
    body = re.sub(r"[`*_>#\[\]()!]", " ", raw)
    return title, re.sub(r"\s+", " ", body).strip()


# --------------------------------------------------------------------------
# Corpus: the already-curated reports ARE the training data for IDF
# --------------------------------------------------------------------------

def indexed_sections(root: Path) -> dict[str, str]:
    """{report-dir: section-id} from index.html card placement."""
    html = (root / "index.html").read_text(encoding="utf-8")
    out: dict[str, str] = {}
    for chunk in re.split(r'<section id="', html)[1:]:
        sid = chunk.split('"', 1)[0]
        if sid == "daily":
            continue
        for href in re.findall(r'href="(reports/[^"]+)"', chunk.split("</section>", 1)[0]):
            out.setdefault(href.split("/")[1], sid)
    return out


def pattern_idf(root: Path) -> dict[str, float]:
    """IDF per pattern, measured over the curated corpus.

    Rare patterns (灵巧手, 认知战, 商用货车) stay decisive; patterns that fire in
    most reports (经济, 接口, Agent) are discounted automatically.
    """
    mapping = indexed_sections(root)
    texts: list[str] = []
    for dirname in mapping:
        files = sorted((root / "reports" / dirname).glob("*.html"))
        if not files:
            continue
        title, body = extract_text(files[0])
        texts.append(f"{title} {body[:20000]}".lower())
    n = max(len(texts), 1)
    idf: dict[str, float] = {}
    for _sid, _head, patterns in SECTIONS:
        for pat, base in patterns:
            rx = re.compile(pat, re.I)
            df = sum(1 for t in texts if rx.search(t))
            idf[pat] = base * (math.log((n + 1) / (df + 1)) + 0.5)
    return idf


# --------------------------------------------------------------------------
# Classification
# --------------------------------------------------------------------------

def score_sections(title: str, body: str, idf: dict[str, float]
                   ) -> list[tuple[str, float, list[str]]]:
    body_l, title_l = body.lower()[:120000], title.lower()
    out = []
    for sid, _head, patterns in SECTIONS:
        total = 0.0
        hits: list[str] = []
        for pat, base in patterns:
            w = idf.get(pat, float(base))
            rx = re.compile(pat, re.I)
            nb, nt = len(rx.findall(body_l)), len(rx.findall(title_l))
            if nb or nt:
                total += w * nb + 2 * w * nt          # title evidence counts double
                hits.append(f"{pat[:30]}x{nb}" + (f"+title x{nt}" if nt else ""))
        if total:
            out.append((sid, total, hits))
    return sorted(out, key=lambda r: -r[1])


def rank_sections(title: str, body: str, idf: dict[str, float]
                  ) -> list[tuple[str, float, list[str]]]:
    """Ranked sections with normalised confidence as the third element."""
    ranked = score_sections(title, body, idf)
    if not ranked:
        return [(sid, 0.0, []) for sid, _h, _p in SECTIONS]
    total = sum(v for _s, v, _h in ranked)
    return [(s, v / total, h) for s, v, h in ranked]


def detect_brief(name: str, title: str) -> str | None:
    if BRIEF_RE.match(name):
        return "hn" if name.startswith("hn-brief-") else "evolution"
    if re.search(r"自进化简报|evolution.?brief", title, re.I):
        return "evolution"
    if re.search(r"Hacker News|HN ?日报", title, re.I):
        return "hn"
    return None


# --------------------------------------------------------------------------
# Path derivation
# --------------------------------------------------------------------------

def derive_date(path: Path, text: str) -> str:
    m = DATE_RE.search(path.name)
    if m:
        return m.group(0)
    cn = re.search(r"(\d{4})年(\d{1,2})月(\d{1,2})日", text[:4000])
    if cn:
        return f"{cn.group(1)}-{int(cn.group(2)):02d}-{int(cn.group(3)):02d}"
    m = DATE_RE.search(text[:4000])
    if m:
        return m.group(0)
    return dt.date.fromtimestamp(path.stat().st_mtime).isoformat()


def derive_slug(path: Path, title: str, date: str, section: str) -> tuple[str, bool]:
    """ASCII slug. Returns (slug, needs_human_slug)."""
    stem = path.stem
    if re.fullmatch(r"[a-z0-9][a-z0-9._-]*", stem) and stem.lower() not in GENERIC_STEMS:
        return re.sub(r"[^a-z0-9]+", "-", stem.lower()).strip("-"), False
    tokens = [t.lower() for t in ASCII_TOKEN_RE.findall(title)]
    tokens = [t for t in tokens if t not in STOPWORDS]
    if tokens:
        return "-".join(dict.fromkeys(tokens))[:60].strip("-"), False
    return f"{date}-{section}-report", True


def plan(path: Path, root: Path, idf: dict[str, float],
         section_override: str | None, slug_override: str | None) -> dict:
    title, body = extract_text(path)
    date = derive_date(path, f"{title} {body}")

    kind = detect_brief(path.name, title)
    if kind:
        return {"kind": "brief", "brief_kind": kind, "source": path, "date": date,
                "title": title, "section": None, "ranked": [], "needs_slug": False,
                "dest_dir": root / "briefs" / date[:7],
                "dest_name": (path.name if BRIEF_RE.match(path.name)
                              else f"{kind}-brief-{date}.html")}

    ranked = rank_sections(title, body, idf)
    sid = section_override or ranked[0][0]

    # Already filed under reports/<date>-<slug>/: keep the directory.
    try:
        rel = path.resolve().relative_to((root / "reports").resolve())
        if len(rel.parts) >= 2 and DATE_RE.match(rel.parts[0]):
            return {"kind": "report", "source": path, "date": rel.parts[0][:10],
                    "title": title, "section": sid, "ranked": ranked[:3],
                    "dest_dir": root / "reports" / rel.parts[0], "dest_name": path.name,
                    "needs_slug": False, "already_filed": True}
    except ValueError:
        pass

    slug, needs_slug = derive_slug(path, title, date, sid)
    if slug_override:
        slug, needs_slug = re.sub(r"[^a-z0-9]+", "-", slug_override.lower()).strip("-"), False
    return {"kind": "report", "source": path, "date": date, "title": title,
            "section": sid, "ranked": ranked[:3], "needs_slug": needs_slug,
            "dest_dir": root / "reports" / f"{date}-{slug}",
            "dest_name": f"{slug}{path.suffix.lower()}"}


def confidence(ranked: list[tuple[str, float, list[str]]]) -> tuple[float, float]:
    """(top share, relative margin over runner-up)."""
    if not ranked:
        return 0.0, 0.0
    top = ranked[0][1]
    second = ranked[1][1] if len(ranked) > 1 else 0.0
    return top, ((top - second) / top if top else 0.0)


# --------------------------------------------------------------------------
# index.html integration
# --------------------------------------------------------------------------

def repo_root(start: Path) -> Path:
    for d in [start.resolve(), *start.resolve().parents]:
        if (d / "index.html").is_file() and (d / "briefs").is_dir():
            return d
    raise SystemExit(f"{RED}error:{RESET} not inside the report repo")


def insert_card(root: Path, pl: dict) -> bool:
    sid = pl["section"]
    html_path = root / "index.html"
    html = html_path.read_text(encoding="utf-8")
    m = re.search(r'(<section id="' + re.escape(sid) + r'">)(.*?)(</section>)', html, re.S)
    if not m:
        print(f"{RED}error:{RESET} section #{sid} not found", file=sys.stderr)
        return False
    inner = m.group(2)
    rel = (pl["dest_dir"].relative_to(root) / pl["dest_name"]).as_posix()
    tag = TAG_LABELS.get(sid, sid)
    card = (
        f'    <div class="report">\n'
        f'      <span class="icon">📄</span>\n'
        f'      <div class="info">\n'
        f'        <a href="{rel}">{pl["title"] or pl["dest_name"]}</a>\n'
        f'        <div class="desc"><span class="tag {sid}">{tag}</span>待补充摘要</div>\n'
        f'      </div>\n'
        f'      <span class="date">{pl["date"][5:]}</span>\n'
        f'    </div>'
    )
    mmdd = pl["date"][5:]
    pos, found = len(inner), False
    for c in re.finditer(r'    <div class="report">.*?\n    </div>', inner, re.S):
        d = re.search(r'<span class="date">(\d\d-\d\d)</span>', c.group(0))
        if d and d.group(1) < mmdd:
            pos, found = c.start(), True
            break
    if not found:
        pos = inner.rstrip().rfind("\n  </div>") + 1 if "  </div>" in inner else len(inner)
    inner = inner[:pos] + card + "\n" + inner[pos:]
    inner = re.sub(r'(<span class="count">)\d+( 篇)',
                   lambda mm: f"{mm.group(1)}{inner.count('class=\"report\"')}{mm.group(2)}",
                   inner, count=1)
    html_path.write_text(html[: m.start(2)] + inner + html[m.end(2):], encoding="utf-8")
    return True


def index_brief(root: Path) -> bool:
    """Briefs are indexed by sync-daily.py — single source of truth."""
    import subprocess
    r = subprocess.run([sys.executable, str(root / "tools" / "sync-daily.py")],
                       cwd=root, capture_output=True, text=True)
    sys.stdout.write(r.stdout)
    return r.returncode == 0


# --------------------------------------------------------------------------
# Reporting / evaluation
# --------------------------------------------------------------------------

def describe(pl: dict, root: Path, explain: bool) -> None:
    if pl.get("already_filed"):
        print(f"{CYAN}already filed{RESET} {pl['source'].relative_to(root)}")
        print(f"  section  {pl['section']}  {HEADINGS.get(pl['section'], '')}")
        return
    print(f"{BOLD}{pl['source'].name}{RESET}  {DIM}({pl['kind']}){RESET}")
    if pl["title"]:
        print(f"  title    {pl['title'][:88]}")
    if pl["kind"] == "brief":
        print(f"  routed   daily brief ({pl['brief_kind']}) -> briefs/<YYYY-MM>/ + #daily")
        print(f"  ->       {GREEN}{(pl['dest_dir'].relative_to(root) / pl['dest_name']).as_posix()}{RESET}")
        return

    top, margin = confidence(pl["ranked"])
    print(f"  section  {BOLD}{pl['section']}{RESET}  {HEADINGS.get(pl['section'], '')}"
          f"  {DIM}(top share {top:.0%}, margin {margin:.0%}){RESET}")
    if explain:
        for sid, share, hits in pl["ranked"]:
            print(f"    {DIM}{sid:11} {share:>6.1%}  {'; '.join(hits[:3])[:110]}{RESET}")
    if margin < 0.25 and not explain:
        print(f"    {YELLOW}runner-up:{RESET} "
              + ", ".join(f"{s} {v:.0%}" for s, v, _ in pl["ranked"][1:3])
              + f"  {DIM}(use --section to override){RESET}")
    dest = (pl["dest_dir"].relative_to(root) / pl["dest_name"]).as_posix()
    print(f"  date     {pl['date']}")
    print(f"  ->       {GREEN}{dest}{RESET}")
    if pl["needs_slug"]:
        print(f"  {YELLOW}note{RESET}     no ASCII signal in the title — placeholder slug; "
              f"pass --slug <name>")


def run_eval(root: Path) -> int:
    """Leave-one-out accuracy over this repo's curated reports.

    Honest evaluation: the classifier is scored on the very corpus it learned
    its IDF from, which is a mild optimistic bias, but it is the only labelled
    data available and it is the same corpus placement decisions are made in.
    """
    mapping = indexed_sections(root)
    items: list[tuple[str, str, str, str]] = []
    for dirname, actual in mapping.items():
        files = sorted((root / "reports" / dirname).glob("*.html"))
        if files:
            t, b = extract_text(files[0])
            items.append((dirname, actual, t, b))
    idf = pattern_idf(root)
    t1 = t3 = 0
    misses: list[tuple[str, str, str, float]] = []
    shares: list[float] = []
    for dirname, actual, title, body in items:
        ranked = rank_sections(title, body, idf)
        order = [s for s, _, _ in ranked]
        shares.append(ranked[0][1])
        if order[0] == actual:
            t1 += 1
        else:
            misses.append((dirname, actual, order[0], ranked[0][1]))
        if actual in order[:3]:
            t3 += 1
    n = max(len(items), 1)
    print(f"corpus: {len(items)} reports   patterns: {sum(len(p) for _, _, p in SECTIONS)}")
    print(f"top-1: {t1}/{n} = {t1/n:.1%}")
    print(f"top-3: {t3}/{n} = {t3/n:.1%}")
    clear = sum(1 for s in shares if s >= 0.5)
    print(f"top share >=0.5: {clear}/{n} ({clear/n:.0%})")
    print(f"\n{DIM}top-1 misses ({len(misses)}) — confirm these by hand:{RESET}")
    for d, a, p, s in misses[:20]:
        print(f"  {DIM}{d[:46]:48} {a:11}->{p:11} share={s:.2f}{RESET}")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="*", help="new material to route")
    ap.add_argument("--apply", action="store_true", help="move file(s) and update index.html")
    ap.add_argument("--yes", action="store_true",
                    help="with --apply, do not require confirmation (needed off a TTY)")
    ap.add_argument("--explain", action="store_true", help="print the full score table")
    ap.add_argument("--eval", action="store_true", help="report leave-one-out accuracy")
    ap.add_argument("--section", help=f"force a section id ({', '.join(SECTION_IDS)})")
    ap.add_argument("--slug", help="force the report slug")
    ap.add_argument("--check", action="store_true", help="verify placement of existing files")
    args = ap.parse_args()

    root = repo_root(Path.cwd())
    if args.section and args.section not in SECTION_IDS:
        print(f"{RED}error:{RESET} unknown section '{args.section}'\n"
              f"  valid: {', '.join(SECTION_IDS)}", file=sys.stderr)
        return 2
    if args.eval:
        return run_eval(root)
    if not args.paths:
        ap.error("no input files (or pass --eval)")

    idf = pattern_idf(root)
    plans = []
    for raw in args.paths:
        p = Path(raw)
        if not p.is_file():
            print(f"{RED}error:{RESET} not a file: {p}", file=sys.stderr)
            return 2
        plans.append(plan(p, root, idf, args.section, args.slug))

    if args.check:
        ok = True
        for pl in plans:
            want = pl["dest_dir"] / pl["dest_name"]
            if pl["source"].resolve() != want.resolve():
                ok = False
                print(f"{RED}misplaced{RESET} {pl['source']} -> expected {want.relative_to(root)}")
                if pl["kind"] == "report":
                    print(f"  {DIM}proposed section: {pl['section']}{RESET}")
        print(f"{GREEN}ok{RESET} placements valid" if ok else f"{RED}drift detected{RESET}")
        return 0 if ok else 1

    for pl in plans:
        describe(pl, root, args.explain)
        print()

    if not args.apply:
        low = [p for p in plans if p["kind"] == "report"
               and confidence(p["ranked"])[1] < 0.25]
        if low:
            print(f"{YELLOW}low confidence{RESET} on {len(low)} file(s) — confirm the section, "
                  f"then re-run with --section <id> --apply --yes")
        else:
            print(f"{DIM}proposal only — re-run with --apply --yes to place and index{RESET}")
        return 1

    if not args.yes and sys.stdin.isatty():
        reply = input(f"{BOLD}Apply {len(plans)} placement(s)? [y/N] {RESET}").strip().lower()
        if reply not in ("y", "yes"):
            print("aborted")
            return 1

    for pl in plans:
        if pl.get("already_filed"):
            print(f"{DIM}unchanged{RESET} {pl['source'].relative_to(root)}")
            continue
        dest_dir, dest_name = pl["dest_dir"], pl["dest_name"]
        if dest_dir.exists() and (dest_dir / dest_name).exists():
            print(f"{RED}error:{RESET} destination exists: "
                  f"{(dest_dir / dest_name).relative_to(root)}", file=sys.stderr)
            return 2
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / dest_name
        if pl["source"].resolve() != dest.resolve():
            pl["source"].rename(dest)
            print(f"{YELLOW}moved{RESET} {pl['source'].name} -> {dest.relative_to(root)}")
        if pl["kind"] == "brief":
            index_brief(root)
        elif dest.suffix.lower() in (".html", ".htm"):
            if insert_card(root, pl):
                print(f"{GREEN}indexed{RESET} section #{pl['section']}")
        else:
            print(f"{DIM}not indexed: {dest.suffix} does not render in a browser{RESET}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
