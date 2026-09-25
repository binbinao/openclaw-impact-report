# OpenClaw 影响力报告

自进化简报与深度调研报告的静态站点。根目录 `index.html` 为索引页，按 15 个板块分类展示。

## 目录结构

```
index.html                              # 站点索引（所有链接均指向下方三层结构）
AGENTS.md                               # 仓库约定（分类规则、命名、校验脚本）
tools/classify-material.py              # 按内容判断新材料该放哪个路径
tools/sync-daily.py                     # 归档散落简报 + 重建 #daily + 修正徽标
tools/test_tools.py                     # 回归测试
tools/hooks/pre-commit                  # 拦截新增的根目录文件
reports/<YYYY-MM-DD>-<slug>/            # 深度调研报告（HTML 必需，.md 可选）
briefs/<YYYY-MM>/                       # 每日简报（按月归档）
```

仓库根目录只保留 `index.html` / `README.md` / `AGENTS.md` / `.gitignore` 与 `tools/`，其余内容一律归入 `reports/` 或 `briefs/`。

## 板块（15）

`index.html` 内的分区顺序与导航一致，每区 `count` 徽标等于该区实际卡片数：

| 板块 | id | 篇数 |
|---|---|---|
| 🚗 汽车 & 智驾 | `auto` | 19 |
| 🚛 商用货车 | `truck` | 5 |
| 🦾 具身智能 & 机器人 | `embodied` | 11 |
| 🔬 芯片 & 算力 | `chip` | 14 |
| 🤖 AI 大模型 & 产业 | `ai` | 13 |
| 🧠 Agent & 工具链 | `agent` | 23 |
| 👤 人物档案 | `people` | 9 |
| 🏭 供应链&产业 | `chain` | 5 |
| ⚙️ 技术 & 基础架构 | `tech` | 13 |
| 📈 宏观经济 & 数据 | `econ` | 8 |
| 🏛 政策 & 地缘 | `policy` | 4 |
| 🎓 教育 & 社会 | `society` | 5 |
| 💡 思考 & 人文 | `think` | 2 |
| 🏥 医疗信息化 | `healthcare` | 1 |
| 📰 每日简报 | `daily` | 6 组 / 126 篇 |

## 命名约定

- **报告**：`reports/<YYYY-MM-DD>-<slug>/`，目录内主文件为 `<slug>.html`（历史目录中存在 `report.html`、`index.html` 两种旧写法）。
- **简报**：`briefs/<YYYY-MM>/evolution-brief-<YYYY-MM-DD>.html`；Hacker News 日报为 `briefs/<YYYY-MM>/hn-brief-<YYYY-MM-DD>.html`。全部按月归档，不放根目录。
- **路径**：一律 ASCII，不使用中文文件名。
- **图片/图表**：目录内 `images/`、`imgs/` 或 `diagrams/`；Mermaid 以 `.mmd` 编写并预渲染为 `.png` 一同提交（不在浏览器端渲染）。

## 新增一篇报告

1. 建目录 `reports/<YYYY-MM-DD>-<slug>/`，放入 `<slug>.html`（内联 `<style>`，无外链依赖）。
2. 在 `index.html` 对应板块**按日期倒序**插入卡片，日期写 `MM-DD`，标签类名用该板块 id。
3. 该板块 `count` 徽标数字 +1。
4. 提交报告目录与 `index.html`。

## 新增材料：先判内容，再定路径

新材料入库时**先读内容判断归属，再决定放哪**：

```bash
python3 tools/classify-material.py NEW.html              # 只出建议（不动文件）
python3 tools/classify-material.py --explain NEW.html    # 附完整打分表
python3 tools/classify-material.py --apply --yes NEW.html # 落盘并写入索引
python3 tools/classify-material.py --section truck NEW.html  # 手动覆盖分区
python3 tools/classify-material.py --eval               # 查看分类准确率
```

它按顺序做三件事：

1. **判定是否每日简报**（文件名或标题含「自进化简报 / Hacker News」）→ 进 `briefs/<YYYY-MM>/` 与 `#daily`；
2. 否则用 **IDF 加权关键词**对 15 个板块打分排序，关键词权重由本仓库 132 篇已归档报告自动推得，因此「经济」「接口」「Agent」这类高频词会自动降权，「灵巧手」「认知战」「商用货车」这类稀有词保持决定性；
3. 得到日期 + slug，落到 `reports/<YYYY-MM-DD>-<slug>/`，并插入 `index.html` 对应板块的日期倒序位置、递增徽标。

准确率（对仓库自身 132 篇已归档报告留一验证）：

| 指标 | 数值 |
|---|---|
| top-1 | **77.3%** |
| top-3 | **93.2%** |

因为单选约四次会错一次，**默认只给建议不落盘**。确认后加 `--section` 与 `--apply --yes`。输出会显示 top share 与领先幅度，便于判断是否在「猜」。

### 根目录保护

仓库根目录只允许 `index.html` / `README.md` / `AGENTS.md` / `.gitignore` / `tools/`。每个克隆启用一次钩子：

```bash
git config core.hooksPath tools/hooks
```

钩子只拦截**新增**的根目录文件，并直接打印正确的归档命令；`git commit --no-verify` 可跳过。

## 归档与校验

每日简报由外部流程生成，**它会把文件写到仓库根目录且不更新索引**。生成后执行：

```bash
python3 tools/sync-daily.py          # 归档散落简报 + 依据磁盘重建 #daily + 修正徽标
python3 tools/sync-daily.py --check  # 仅检查，退出码 1 表示不同步
```

脚本幂等，可在任意子目录运行。它会：

1. 把根目录散落的 `*-brief-<日期>.html` 移入 `briefs/<YYYY-MM>/`；
2. 依据磁盘上实际存在的简报**重建** `index.html` 的 `#daily` 区（月份分组、组标签、徽标一并校正）；
3. 修正与卡片数不符的板块徽标。

回归测试：

```bash
python3 tools/test_tools.py          # 21 项，离线
```

随后做链接校验：

```bash
python3 - <<'PY'
import re, pathlib
root = pathlib.Path(".")
idx = (root/"index.html").read_text(encoding="utf-8")
bad = [h for h in re.findall(r'href="([^"]+)"', idx)
       if not h.startswith(("http", "#")) and not (root/h.split("#")[0]).exists()]
print("broken links:", len(bad), bad)
PY
```

预期输出 `broken links: 0 []`。完整校验（徽标、排序、标签配色、覆盖率）见 `AGENTS.md`。
