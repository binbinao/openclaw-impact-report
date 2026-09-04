# OpenClaw 影响力报告

自进化简报与深度调研报告的静态站点。根目录 `index.html` 为索引页，按板块（汽车&智驾、宏观经济、AI&科技、人物档案、技术&基础架构、供应链&产业、商用货车、管理&思考、文化民俗、医疗信息化、每日简报）分类展示。

## 目录结构

```
index.html                     # 站点索引（所有链接均指向下方三层结构）
reports/<YYYY-MM-DD>-<slug>/   # 深度调研报告（每篇 .md 与 .html 成对存放）
briefs/<YYYY-MM>/              # 每日简报（按月归档）
```

## 命名约定

- 报告：`reports/<YYYY-MM-DD>-<slug>/`，目录内为对应的 `.md` 与 `.html`。
- 简报：`briefs/<YYYY-MM>/evolution-brief-<YYYY-MM-DD>.html`。

## 部署

GitHub Pages: <https://binbinao.github.io/openclaw-impact-report/>
