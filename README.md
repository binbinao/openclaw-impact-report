# OpenClaw 影响力报告

自进化简报与深度调研报告的静态站点。根目录 `index.html` 为索引页，按 15 个板块分类展示。

## 目录结构

```
index.html                              # 站点索引（所有链接均指向下方三层结构）
AGENTS.md                               # 仓库约定（分类规则、命名、校验脚本）
reports/<YYYY-MM-DD>-<slug>/            # 深度调研报告（HTML 必需，.md 可选）
briefs/<YYYY-MM>/                       # 每日简报（按月归档）
```

仓库根目录只保留 `index.html` / `README.md` / `AGENTS.md` / `.gitignore`，其余内容一律归入 `reports/` 或 `briefs/`。

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
| 📰 每日简报 | `daily` | 6 组 / 125 篇 |

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

## 校验

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

## 部署

GitHub Pages 直接从 `main` 分支根目录发布，无构建步骤，无 CI：<https://binbinao.github.io/openclaw-impact-report/>

推送即生效。**改动文件路径会让已发布的外链失效**，重命名目录前需确认外部引用。
