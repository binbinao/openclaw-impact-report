# Repository Guidelines

## Project Overview

`openclaw-impact-report` is a **content-only static site**: Chinese-language deep-research reports (深度调研报告) and daily self-evolution briefs (自进化简报), published via GitHub Pages at <https://binbinao.github.io/openclaw-impact-report/>.

There is **no application code, no build step, no package manager, no tests, and no CI**. Every artifact is hand-authored HTML (plus an optional Markdown source). The only tracked non-content files are `.gitignore`, `README.md`, one vestigial Python script, and one orphaned JSON config.

Practical consequence: an "implementation" here means editing HTML literals and committing. Nothing regenerates, minifies, or validates anything, so drift is normal and expected — your job when touching `index.html` is to not add more.

## Architecture & Data Flow

Three-layer, flat, zero-tooling. GitHub Pages serves the repo root verbatim (`main` branch, no `gh-pages`, no `/docs`, no `.nojekyll`, no `.github/workflows`).

```
index.html                      # hand-curated site index — the ONLY navigation surface
  ├─ <section id="auto">        # 15 sections; category = physical placement
  │    └─ <div class="report">  # one card per report/brief
  ├─ reports/<YYYY-MM-DD>-<slug>/<file>.html   # 131 leaf dirs, self-contained
  └─ briefs/<YYYY-MM>/evolution-brief-<YYYY-MM-DD>.html   # 102 files, monthly archive
```

Data flow: **author writes HTML → edits `index.html` card → `git push main` → Pages rebuilds.** No templating, no partials, no shared stylesheet. Each HTML file carries its own inline `<style>`; duplication across 261 files is the accepted design.

Deployment coupling: a report is not "published" until it has a card in `index.html`. Commit `9dfc490` is the canonical shape — report dir + `index.html` in one commit:

```
index.html
reports/2026-09-24-hf-cross-vendor-models/cross_vendor_hf_models.xlsx
reports/2026-09-24-hf-cross-vendor-models/hf-cross-vendor-models-2026-09-24.html
reports/2026-09-24-hf-cross-vendor-models/hf-cross-vendor-models-2026-09-24.md
```

## Key Directories

| Path | Purpose |
|---|---|
| `index.html` | Whole site index. 1322 lines, one inline `<style>` (**tag colors at 44–59**), **zero `<script>`**, 15 `<section>`, 138 `.report` cards, 275 hrefs (132 report links, 126 brief links, 2 external). |
| `reports/` | 134 dated leaf dirs `2026-03-11` → `2026-09-24`. Each self-contains its HTML, optional `.md`, optional asset subdir. |
| `reports/<slug>/images/` \| `imgs/` \| `diagrams/` | Asset dirs — 5 / 3 / 3 dirs respectively. Naming is **not** standardized; pick the one matching the report you are editing. |
| `briefs/<YYYY-MM>/` | Monthly brief archive, **all briefs live here**: `2026-05` (4), `2026-06` (30), `2026-07` (30, missing 07-20), `2026-08` (31), `2026-09` (25 evolution + 6 `hn-brief`). Total 126. |
| repo root | **Only 4 files**: `index.html`, `README.md`, `AGENTS.md`, `.gitignore`. Nothing else belongs here — briefs go to `briefs/<YYYY-MM>/`, reports to `reports/<date>-<slug>/`. |

All tracked files, by extension (370 total): `html` 261, `md` 39, `png` 47, `mmd` 18, `py` 1, `json` 1, `xlsx` 1, `svg` 1, `.gitignore` 1.

`reports/` holds 134 directories — 132 with an `index.html` card, plus 2 holding only a `.md` (no HTML, deliberately unindexed: `2026-03-24-hf-modelscope-tracking`, `2026-09-20-ai-platform-weekly`).

## Development Commands

**There are none.** No build, lint, test, format, or serve command exists or is required. `.gitignore` (`.DS_Store`, `._*`, `.idea/`, `.vscode/`, `*.swp`) is the entire config surface.

To preview locally, any static server works — but note that **root-relative references are relative paths**, so serve from the repo root:

```bash
python3 -m http.server 8000    # then open http://localhost:8000/
```

The only meaningful QA is link/count integrity. Link checking **must** use `python3`, not shell `[ -e ]` — non-ASCII paths (`2026-05-11-智驾百草枯_...`) produce false positives under a non-UTF-8 shell locale:

```bash
# index.html invariants — expect all clean
python3 - <<'PY'
import re, pathlib
root = pathlib.Path(".")
idx = (root/"index.html").read_text(encoding="utf-8")

bad = [h for h in re.findall(r'href="([^"]+)"', idx)
       if not h.startswith(("http", "#")) and not (root/h.split("#")[0]).exists()]
print("broken local links:", len(bad), bad)

nav  = re.findall(r'<a href="#([a-z]+)">', idx)
secs = re.findall(r'<section id="([a-z]+)">', idx)
print("nav == sections:", nav == secs, "| sections:", len(secs))

for p in re.split(r'<section id="', idx)[1:]:
    sid  = p.split('"')[0]
    body = p.split('</section>')[0]
    n = body.count('class="report"')
    d = re.search(r'<span class="count">(.*?)<', body).group(1)
    ds = re.findall(r'<span class="date">(\d\d-\d\d)</span>', body)
    ok = (d.startswith(f"{n} ") if sid != "daily" else d.startswith("6 "))
    print(f"{sid:11} badge={d:14} cards={n:>3} {'OK' if ok else 'DRIFT'}"
          f"  desc-order={ds == sorted(ds, reverse=True)}")

fams = set(re.findall(r'<span class="tag ([a-z]+)"', idx))
css  = set(re.findall(r'\.tag\.([a-z]+)', idx))
print("tag families missing CSS:", sorted(fams - css))

dirs   = {p.name for p in (root/"reports").iterdir() if p.is_dir() and list(p.glob("*.html"))}
linked = {h.split('/')[1] for h in re.findall(r'href="(reports/[^"]+)"', idx)}
print(f"report coverage: {len(linked)}/{len(dirs)}  unlinked: {sorted(dirs - linked)}")

bfs = {str(p.relative_to(root)) for p in root.glob("briefs/*/*.html")}
bl  = set(re.findall(r'href="(briefs/[^"]+)"', idx))
print(f"brief coverage: {len(bl)}/{len(bfs)}  unlinked: {sorted(bfs - bl)}")

loose = sorted(p.name for p in root.iterdir() if p.is_file())
print("repo root files (expect exactly 4):", loose)
PY
```

Expect: `0` broken, `True`, all `OK`/`desc-order=True`, empty missing-CSS, `132/132`, `126/126`, and 4 root files. The `.md`-only dirs are excluded from coverage on purpose (see *Adding a `.md`-only entry*).

Rendered check (catches unstyled pills and overflow that regex cannot):

```bash
python3 -m http.server 8000 &        # serve from repo ROOT, then open localhost:8000
```

## Code Conventions & Common Patterns

### index.html card markup (copy verbatim; do not invent structure)

Category membership is encoded **only by physical placement inside a `<section id="...">`**. The `.tag.*` pill classes are cosmetic color labels, not the sectioning mechanism — `section id="auto"` legitimately contains `<span class="tag econ">`.

```html
<!-- ====== 汽车 & 智驾 ====== -->
<section id="auto">
  <h2 class="cat-title">🚗 汽车 &amp; 智驾 <span class="count">21 篇</span></h2>
  <div class="report-list">
    <div class="report">
      <span class="icon">🇺🇸</span>
      <div class="info">
        <a href="reports/2026-08-13-us-adas-deployment-2026/us-adas-deployment-2026.html">美国汽车智驾深度调研（2024–2026）</a>
        <div class="desc"><span class="tag auto">智驾</span>Waymo 一超、Tesla 试探、Cruise 重启 · 中国出海美国现状 · 64 来源</div>
      </div>
      <span class="date">08-13</span>
    </div>
```

Brief cards in `#daily` differ — month-grouped, comma/dot-separated date links instead of one link per card:

```html
<div class="report">
  <span class="icon">📁</span>
  <div class="info">
    <span style="color:var(--gray-500);font-size:13px;">09月简报（4篇）</span>
    <div class="desc">
      <a href="briefs/2026-09/evolution-brief-2026-09-04.html" style="font-size:12px;">09-04</a> · <a href="briefs/2026-09/evolution-brief-2026-09-03.html" style="font-size:12px;">09-03</a>
    </div>
  </div>
  <span class="date">09月</span>
</div>
```

### Adding a report (the full cutover)

1. Create `reports/<YYYY-MM-DD>-<slug>/<slug>.html` — standalone doc, inline `<style>`, `<html lang="zh-CN">`, `<meta charset="utf-8">`, `<!DOCTYPE html>`.
2. Copy an `.md` source into the same dir if one exists (only 34 of 131 dirs have one — it is **not** required).
3. Insert a `<div class="report">` card into the matching `<section>` in `index.html`, **at the date-ordered position** (descending), with `<span class="date">MM-DD</span>` and a `<span class="tag <section-id>">` pill.
4. Bump that section's `<span class="count">N 篇</span>` by one.
5. Commit report dir + `index.html` together.

Pick the section by dominant topic — see the table below; ambiguous cases historically mis-filed were 电力/小费 (→ `econ`), 云厂商涨价/大模型商业模式 (→ `ai`), GTC/英伟达 (→ `chip`), OpenClaw/Hermes/OMP/技能清单 (→ `agent`).

### Section IDs and order

15 sections, document order == nav order (verified 1:1):

| id | heading | cards |
|---|---|---|
| `auto` | 🚗 汽车 &amp; 智驾 | 19 |
| `truck` | 🚛 商用货车 | 5 |
| `embodied` | 🦾 具身智能 &amp; 机器人 | 11 |
| `chip` | 🔬 芯片 &amp; 算力 | 14 |
| `ai` | 🤖 AI 大模型 &amp; 产业 | 13 |
| `agent` | 🧠 Agent &amp; 工具链 | 23 |
| `people` | 👤 人物档案 | 9 |
| `chain` | 🏭 供应链&amp;产业 | 5 |
| `tech` | ⚙️ 技术 &amp; 基础架构 | 13 |
| `econ` | 📈 宏观经济 &amp; 数据 | 8 |
| `policy` | 🏛 政策 &amp; 地缘 | 4 |
| `society` | 🎓 教育 &amp; 社会 | 5 |
| `think` | 💡 思考 &amp; 人文 | 2 |
| `healthcare` | 🏥 医疗信息化 | 1 |
| `daily` | 📰 每日简报 | 6 组 / 126 链接 |

**Every badge equals its actual card count** — keep it that way when adding a card. Cards carry `<span class="date">MM-DD</span>`. Exception: `daily` groups many briefs per card, so its badge is `6 组 / 126 篇` (group count / total brief links) — update the second number whenever a brief is added.

The old `zhangyu-power-synapx-*` file that lived at the repo root is now `reports/2026-09-14-zhangyu-synapx/zhangyu-power-synapx-deep-dive-2026-09-14.html`.

**Cards are sorted date-descending within each section.** Use the full `YYYY-MM-DD` from the directory name as the sort key, then render the short window in `<span class="date">MM-DD</span>`.

**One section per report — no cross-listing.** A report belongs in exactly one section; pick the dominant topic.

### Tag families

Each card's `.tag.*` pill is recolored to its **section's** family, so pill color reinforces section membership (previously `auto` held `.tag econ` pills). 14 families are used; colors cycle the original 6 tokens:

```
auto/truck/society → --olive        chain/chip → --sky
econ/policy/think  → --rust         ai/embodied/healthcare → --purple
people/agent       → --clay
```

Add a new section → add its `.tag.<id>` rule in the `<style>` block (lines 44–59) or the pill renders unstyled.

### Adding a brief

Daily briefs are **not** standalone cards — they are listed as date links inside the `#daily` month groups.

1. Write `briefs/<YYYY-MM>/evolution-brief-<YYYY-MM-DD>.html` (or `hn-brief-<YYYY-MM-DD>.html` for the HN digest). **Never** write briefs to the repo root; that was the historical mistake and 22 files were relocated.
2. Add a dated `<a>` into the matching month's group card `<div class="desc">`, keeping the ` · ` separator and **descending** date order.
3. Bump the group label `NN月简报（N篇）` and the `daily` badge total (`6 组 / N 篇`).
4. New month → add a whole new group card above the previous month's.

Briefs are relocation-safe: they carry no cross-directory asset references, and the only brief-to-brief links (`evolution-brief-2026-09-20` → `-09-19`, `-09-23` → `-09-22`) are same-directory, so moving a whole month together preserves them.

### Adding a `.md`-only entry

A directory with only a `.md` and no HTML gets **no index card** — linking a raw `.md` makes the browser download it rather than render it. See `2026-03-24-hf-modelscope-tracking` and `2026-09-20-ai-platform-weekly`; keep them filed and unindexed until they have an HTML.


### Report HTML conventions (three competing, pick per-era)

There is **no single canonical inner filename** across the 135 report HTML files:

| Inner filename | Count | Era |
|---|---|---|
| `<slug>.html` (e.g. `momenta-tech-stack-deep-dive.html`) | 87 | dominant; use this for new reports |
| `report.html` | 29 | 2026-03 → 2026-06 |
| `index.html` | 16 | 2026-03 → 2026-05 |
| `wechat-*.html` | 3 | one-off WeChat conversions |

Use `<slug>.html`. Back-links are inconsistent and **commonly broken**. Of 135 report files, 23 carry a site back-link, in 4 forms:

| Form | Count | Works? |
|---|---|---|
| `../../index.html` | 15 | yes |
| `https://binbinao.github.io/openclaw-impact-report/` | 4 | yes |
| `../index.html` | 3 | **no** — resolves to `reports/index.html`, which does not exist |
| `index.html` | 1 | **no** — resolves within the report's own dir |

Use `../../index.html`. The index is reachable via the browser back button regardless, so 112 of 135 files ship with no back-link at all.

### Styling

Two design eras coexist; match the era of the file you are editing rather than importing a third system.

- **`index.html`** — light theme, CSS custom properties at `:root` (`--bg:#F8F7F4`, `--card:#FFFFFF`, `--clay:#D97757`, `--olive:#788C5D`, `--rust:#B04A3F`, `--sky:#5B8BA0`, `--purple:#8B6B9E`), `system-ui` stack, one `@media (max-width:600px)` block.
- **2026-09 reports & briefs** — dark GitHub-like theme: `--bg:#0d1117`, `--card/--bg2:#161b22`, `--line/--border:#30363d`, `--tx/--txt:#e6edf3`, `--tx2/--dim:#8b949e`, `--accent:#58a6ff`.
- **Older reports** — standalone light or ad-hoc palettes.

Conventions: `system-ui, -apple-system, "PingFang SC", "Microsoft YaHei", sans-serif` for prose; `ui-monospace, SFMono-Regular, Menlo, Consolas, monospace` for numbers. Escape `&` as `&amp;` in headings (e.g. `AI &amp; 科技`). Emoji icons are used as visual markers — keep the pattern.

### Diagram workflow

Mermaid is **authored as `.mmd` and pre-rendered to `.png` offline**, then both are committed. **No file renders Mermaid in the browser** — zero reports link a Mermaid runtime. 18 `.mmd` files ship alongside 47 `.png`; 3 `.md` sources also carry ```` ```mermaid ```` fences. Reference the PNG from HTML:

```html
<img src="images/evolution-mindmap.png" alt="...">
<div class="diagram-caption">图 1 · 架构演进</div>
```

`reports/2026-03-30-google-ai-adoption-framework/diagrams/puppeteer.json` (`{"args":["--no-sandbox","--disable-setuid-sandbox"]}`) is the orphaned launch config from that pipeline; no runner exists in-repo. `reports/2026-03-26-yang-zhilin-ai-research-revolution/generate_images.py` is a one-off PIL script with hardcoded Linux font paths — do not treat either as build infrastructure.

### External dependencies

Only **two** report files reference an external CDN, each a one-off:

- `reports/2026-07-18-waic-2026-guancha-news-2026-07-18/…html` — `echarts@5.5.0`, 5 canvas charts.
- `reports/2026-08-25-cadence-design-systems-deep-dive/…html` — Google Fonts (DM Sans / Instrument Serif).

Briefs are otherwise 100% self-contained (CSS-only charts, zero `<script>`, zero `<img>`, zero `<link>`), except for a Google Fonts `@import` (Inter + JetBrains Mono) in 23 briefs dated 2026-06-15..2026-07-07. Prefer self-contained.

### Markdown sources

`.md` files are authoring sources, not rendered by the site — HTML is the published artifact and there is no md→html pipeline. Conventions: single `# ` H1 first line, no YAML front matter (only 1 exception: `reports/2026-03-26-openclaw-guide/index.md`). `.md` and `.html` are maintained separately; the HTML is **not** generated from the MD.

### Brief content structure

`evolution-brief-*.html` is a recurring report with a stable-but-evolving section order. Modern (P111+, 2026-09) headings:

```
🎯 本期核心发现 / 本期四大发现
📊 能力状态            (感知层 self_scan.py)
⚠️ 弱点与日志诊断       (诊断层 weakness_scan.py)
🩺 健康度评分
🔬 知识摄取 / 外部知识摄取  (学习层 knowledge_ingest.py)
📈 趋势对比与预测验证
🧬 进化建议（按投入产出比排序）
🔮 下期预测
📋 数据校正记录（对往期的修订）   ← optional
🛠 技术备注                      ← optional
```

The brief references the agent-side scripts `self_scan.py` / `weakness_scan.py` / `knowledge_ingest.py` by name — those live outside this repo. `hn-brief-*.html` is a separate template (Hacker News digest: 今日概况 / 必读 Top 5 / AI 相关动态 / 编程 & 开源 / 安全 & 政策 / 榜单尾部 / 今日最热讨论) with HTML-entity emoji headings (`&#128202;`) rather than literal emoji.

Titles carry an episode number: `Hermes 自进化简报 · 第 119 期 · 2026-09-24`. The counter is monotonic across the whole archive; read the newest brief for the current value before writing the next.

### Known drift — do not "fix" opportunistically

Leave these alone unless asked; they are pre-existing and orthogonal to any normal change:

- 4 report HTML files are intentionally not index-linked: `2026-03-22-lsdyna-starccm-hardware/hardware_analysis_v2.html`, `2026-03-29-us-ai-strategy/wechat-{simple,converted,full}.html`.
- 5 files omit `<html lang>`; `reports/2026-03-29-us-ai-strategy/wechat-converted.html` is an HTML fragment with no doctype/head (a WeChat paste artifact).
- 2 directories hold a `.md` with no HTML and no index card (deliberate — see *Adding a `.md`-only entry*).
- **The one remaining non-ASCII path:** `reports/2026-05-11-智驾百草枯_深度调研报告_20260511/智驾百草枯_深度调研报告_20260511.html` (kept as-is because renaming breaks its published URL). This is exactly why link checks must be `python3` — a shell `[ -e ]` loop fails on this path under a non-UTF-8 locale. `git ls-files` also hides it unless you pass `-c core.quotePath=false`. New paths must be ASCII.

**Resolved — do not re-introduce:**

- Section badges equal card counts; cards are date-descending; nav order matches document order; pill colors follow the section (first reorg).
- All briefs live under `briefs/<YYYY-MM>/` and **all 126 are index-linked** — repo root holds only 4 files (second reorg).
- The 4 broken report back-links are fixed (`../../index.html`).
- The 2 loose `reports/*.md` were filed into dated dirs; `reports/` root has no loose files.

### Not a duplicate — do not merge

Nearby-titled reports that look redundant but are separate authored works (measured text similarity 0.04–0.19, i.e. distinct):

- `2026-05-02-ai-education-blind-spots` vs `2026-05-02-ai-education-gaps` — same origin, different write-up.
- `2026-07-22-hermes-official-top20-2026-07-22` vs `2026-07-22-hermes-skills-top20-2026-07-22`.
- `2026-03-20-huang-jensen-gtc`, `2026-03-21-nvidia-gtc`, `2026-03-18-nvidia-gtc-2026` — three independent GTC reports.

## Important Files

| File | Role |
|---|---|
| `index.html` | Entry point and the only navigation. Editing it is the publish step. |
| `README.md` | Chinese overview of the 15 sections, naming rules, the add-a-report steps, and a one-liner link check. Silent on per-report assets and the Pages branch mechanism. |
| `.gitignore` | Only config file. |
| `reports/2026-09-24-hf-cross-vendor-models/hf-cross-vendor-models-2026-09-24.html` | Newest report; best current reference for dark-theme report styling. |
| `briefs/2026-09/evolution-brief-2026-09-24.html` | Newest brief (P119); best reference for the brief template. |
| `reports/2026-03-30-google-ai-adoption-framework/` | Only dir with both `imgs/` and `diagrams/`, plus the `.mmd`+PNG+puppeteer pipeline. |
| `reports/2026-03-26-yang-zhilin-ai-research-revolution/generate_images.py` | Only `.py` file; PIL image generation for that report's PNGs. |

## Runtime/Tooling Preferences

- **Runtime:** none. No Node, Bun, Python, or Ruby dependency is required to build, preview, or publish. `python3` is used only for ad-hoc verification scripts (stdlib only — no `pip` installs).
- **Package manager:** none. Do not introduce `package.json`, lockfiles, bundlers, or a framework — there is no tooling layer to justify them, and Pages serves raw files.
- **Git:** `main` is the only branch, direct-to-`main`, no PRs, no CI gates. Remote `git@github.com:binbinao/openclaw-impact-report.git`. 306 commits, 2026-03-11 → 2026-09-24.
- **Commit messages:** mixed style, no enforced convention. Observed prefixes: `Add` (52), `docs:` (27), `feat:` (17), `Fix` (11), `add:` (7), `Evolution Brief <date> (P<n>)`, plus some Chinese-subject commits. Match the surrounding history; a suitable form is `add: <报告标题>` or `feat: 新增<主题>报告`.
- **Encoding:** everything is UTF-8. Exactly one non-ASCII path survives (see *Known drift*); new paths must be ASCII. Never rely on shell globs for path checks — use `python3`.

## Testing & QA

No test framework, no suite, no coverage expectation. Verification is manual and structural:

1. **Open the artifact in a browser.** This is the primary check — visual correctness at 960px (index) / 1280px (report) and under `@media (max-width:600px)`.
2. **Link integrity** via the `python3` snippet in Development Commands. Expect `broken index links: 0`. Broken *back-links* inside `reports/<slug>/*.html` already exist (`../index.html` should be `../../index.html`) — the Back button works, so this is cosmetic.
3. **Count badges** via the second snippet. `auto`/`econ` are known-drifting; your own edit must not add new drift.
4. **HTML sanity** when authoring a new file: `<!DOCTYPE html>`, `<html lang="zh-CN">`, `<meta charset="utf-8">`, `<meta name="viewport">`, single inline `<style>`, no `<script>` unless justified. `grep -c '<script' <file>` should be `0` for briefs.
5. **Asset references** resolve relative to the HTML file — verify each `<img src>` path exists in the same dir or its asset subdir.
