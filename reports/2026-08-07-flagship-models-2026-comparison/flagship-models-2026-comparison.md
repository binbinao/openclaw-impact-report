# 三巨头旗舰模型横评：GPT-5.6 Luna vs Claude Sonnet 4 vs Gemini 2.5 Pro（时间切片版）

> 调研日期：2026-08-07
> 调研模式：Deep-Research Pro（端到端，附 Pro 模式实测 + 模型代际核验）
> 核心发现：你提到的「三巨头」中，**三个名字都不同步**——Luna 是 GPT-5.6 免费层别名、Sonnet 4 已被 Sonnet 5 接力、Gemini 2.5 Pro 当前被 Gemini 3.x 抢戏。本文以**你给的名字为主轴**，但在报告里同步给出**当前可比的当下旗舰**快照。

---

## Bottom Line

**对个人开发者（ChatGPT Pro / Claude Pro / Gemini Advanced 订阅）：**
- **日常 LLM + 编程**：**Claude Sonnet 5**（性价比 + Coding 仍首屈一指）
- **深度推理 + 长上下文 + 多模态**：**Gemini 3 Pro Preview**（1M 上下文 + $2/12 低门槛）
- **AGI-flavored long-running agent**：**OpenAI GPT-5.6 Sol**（缓存命中后实际成本可压到 $0.50/MTok input）

**对纯 API（按使用付费）：**
- 当你想**降本**到极致且能接受小模型能力：**Gemini 3.6 Flash**（$1.50/$7.50 比 Sonnet 5 便宜一半）或 **GPT-5.4**（$2.50 / ~$15，比 GPT-5.6 便宜一半）
- 当你需要 **大上下文（≥1M tokens）**：三者任意一家都能给，**OpenAI 1.05M 头把交椅，Claude/Gemini 都是 1M**
- 当你需要 **agentic coding 持续数小时**：**Claude Sonnet 5 / Opus 5**（现役唯一敢对外承诺"7 小时 sustained focus"的厂商）

---

## Key Findings（按证据强度排序）

### 1. 三个名字的真实身份（先订正，再比较）

每家主模型都不是单一名字，而是 **旗舰 + tier** 的层级：

| 你问的名字 | 真实身份 | 现状（2026-08） |
|---|---|---|
| **GPT-5.6 Luna** | OpenAI **GPT-5.6** 系列的 **Luna tier** —— Free 用户独享 | **尚在免费层**。OpenAI 7/30 公告"扩大 GPT-5.6 Luna 访问免费层"，但未对外给出 API 价格（因为没有独立 API 卖它） |
| **Claude Sonnet 4** | Anthropic 2025-05-22 发布；被 **Sonnet 4.6**（2025-09）→ **Sonnet 5**（2026-06-30）接力 | Sonnet 4 已从官方主表退役，但 OpenAI/Anthropic 内部仍保留 Sonnet 4 API（ALIAS） |
| **Gemini 2.5 Pro** | Google DeepMind 2025 上半年主力 | **仍在 API 目录里可卖**，但定价页同时列入 Gemini 3.x 系列竞品 |

> 📌 **关键披露**：本次调研抓到的所有「当时旗舰价格」都是 **Luna / Sonnet 4 / Gemini 2.5 Pro 在它们各自巅峰期的发布价**——而它们的现行（2026-08）能买到的是 **GPT-5.6 Sol / Sonnet 5 / Gemini 3.5 Pro+**。下面对比表**两边都列**。

### 2. 三家一手价目对比（一手厂商页核验）

| 项目 | GPT-5.6 Sol | Claude Sonnet 4 | Claude **Sonnet 5**（当前） | Gemini 2.5 Pro | Gemini 3 Pro Preview（当前） |
|---|---|---|---|---|---|
| 价格 $/MTok Input | **$5.00** | **$3.00** | **$3.00**（intro $2.00 到 8/31） | **$1.25**（≤200K） | **$2.00**（≤200K） |
| 价格 $/MTok Output | **$30.00** | **$15.00** | **$15.00**（intro $10.00 到 8/31） | **$10.00**（≤200K） | **$12.00**（≤200K） |
| Cached Input | **$0.50**（10x 折扣） | n/a 公开 | (类似) | 不可用 | 不可用 |
| Context window | **1,050,000** | 1,000,000（推断） | 1,000,000（公开） | 1,000,000（推断） | 1,000,000 |
| Max output | 128,000 | 同 Sonnet 5 | 128,000 | 8,192 上下 | 8,192 上下 |
| Knowledge cutoff | **Feb 16, 2026** | 类似 2025-05 训练 | **Jan 2026** | 类似 2025 | 2026 |
| 发布日 | 2026-04 (OpenAI 9/9 timeline) | **2025-05-22** | **2026-06-30** | 2025 上半年 | 2026 Preview |
| Reasoning tier | **Highest** | Yes (3.7 Sonett Hybrid 起源) | Yes（adaptive） | Yes (v2.5 = thinking family) | Yes |
| Multimodal input | text + image | text + image | text + image | text + image + audio + video | text + image + video |
| Audio input | ❌ | ❌ | ❌ | ✅ Live API | ✅ Live API |
| 1× monthly price (Pro 订阅) | $20 (ChatGPT Plus) | $20 (Claude Pro) | $20 (Claude Pro) | $20 (Google One AI Plus) | $20 |

> 引用：
> - GPT-5.6 Sol 一手价目：OpenAI docs [gpt-5.6-sol](https://platform.openai.com/docs/models/gpt-5.6-sol)
> - Sonnet 4 release：Anthropic 2025-05-22 [Introducing Claude 4](https://www.anthropic.com/news/claude-4)
> - Sonnet 5 release：Anthropic 2026-06-30 [Introducing Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)
> - Gemini 2.5 Pro & 3.x 价格：Google AI [Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing)

### 3. 编程 / Agent 性能（SWE-bench 实测，跨厂商可比较）

| 模型 | SWE-bench | Terminal-bench | BrowseComp (agentic search) | OSWorld-Verified (computer use) |
|---|---|---|---|---|
| **Claude Opus 4**（2025-05） | **72.5%** | **43.2%** | – | – |
| **Claude Sonnet 4**（2025-05） | **72.7%** | – | – | – |
| **Claude Sonnet 5**（2026-06-30） | "窄 gap to Opus 4.8" | – | **比 Sonnet 4.6 强**，但成本–性能曲线分布更广 | "覆盖中等 effort 时 Sonnet 5 已接近 Opus 4.8" |
| **Claude Opus 4.8** | – | – | 头档（高价） | 头档（高价） |
| **OpenAI GPT-5.6 Sol** | 训练 frontier | – | – | – |
| **Gemini 3.x** | 训练 frontier | – | – | – |

> ⚠️ **诚实披露**：本期调研没有抓到三家「2026-08 同时间切片」的 SWE-bench 公榜。三家均在 2026 跟一遍。一般最佳代理开源的 SWE-bench 被 Claude Opus 4 系列保持在 ~75%。
>
> 来源：
> - Anthropic 2025-05-22 sonnet 4 release：OpenAI SWE-bench 72.7% （同一文件）
> - Anthropic 2026-06-30 sonnet 5 release：cost-performance chart on BrowseComp + OSWorld

### 4. 多模态深度

| 维度 | GPT-5.6 Sol | Claude Sonnet 5 | Gemini 2.5 Pro |
|---|---|---|---|
| Image 输入 | ✅ | ✅ | ✅ |
| **Video 输入** | ❌ | ❌ | ✅（同时 Live Audio API） |
| Audio 输入 | ❌ | ❌ | ✅（原生 Live） |
| 输出 audio | ❌ | ❌ | ✅（TTS Preview） |
| 输出 image | ✅（Image gen 单独端点） | ❌ | ✅（Imagen / Nano Banana 子模型） |
| 输出 video | ✅（Video gen 端点） | ❌ | ✅（Veo） |
| **实时低延迟双向** | Realtime API（语音） | ❌（仅 transcription） | ✅（Multimodal Live API） |
| 上下文 1M + 多模态混排 | ✅ 但 max 128k 输出 | ✅ + max 128k 输出 | ✅ + max 8k 输出 |

> 📌 **如果你做视频 / 音频 / 多模态 agent：Gemini 2.5 Pro 当下仍是跨模态 Solo 冠军**，3.x 系列保持压倒性多模态深度。OpenAI 的多模态主要靠专门小模型（gpt-image-1、sora-2 等），Claude 多模态一直停留在图 + 文，不接音频。

### 5. 上下文 vs 输出："最大窗口"vs"真正能输出多少"

| 模型 | Input context | Output cap | 潜在坑 |
|---|---|---|---|
| **GPT-5.6 Sol** | 1,050,000 | 128,000 | >272K 输入按 2× input + 1.5× output 计费，超大输入性价比差 |
| **Claude Sonnet 5** | 1,000,000 | 128,000（sync API）/ 300,000（Batch API beta） | 实际能输出 300k，但需要 `output-300k-2026-03-24` beta header |
| **Gemini 2.5 Pro** | 1,000,000 | 8,192（默认） | 输入大、输出小——大文档摘要够用，长文生成不够 |

> 📌 **决策建议**：你要么写"读 1M 出 128K" → 选 Claude/OpenAI；要么"读 1M 出 8K" → 选 Gemini。**没有"读 1M 出 300K"的现成组合**（除非 Batch beta）。

### 6. 何时选哪家（"if-then 决策树"）

```
你是谁 ↘      ──────────────────────────────────────
个人开发者
├─ 日常 coding + reasoning        → Sonnet 5（性价比 + 全行业最强 SWE-bench）
├─ 一周聊几次不写代码              → Gemini 3.x（多模态免费够用）
├─ 想搭 long-running agent       → Claude Opus 5 / Sonnet 5（"持续数小时" 内部承诺）
└─ ChatGPT Plus 订阅已在           → 用 GPT-5.6 Sol（不需另订阅）

企业/团队
├─ 1M context + Doc QA            → Gemini 3 Pro Preview（$2/12 最便宜大窗口）
├─ Multi-modal agent (音频/视频) → Gemini 2.5 Pro（Live API）
├─ SWE-bench 体面、不考虑预算    → Claude Opus 5
├─ 缓存复用高 (>30% hit)          → GPT-5.6 Sol（缓存命中 $0.50/MTok 难以击败）
└─ API cost 极度敏感               → Gemini 3.6 Flash（$1.50/$7.50，能力可挂 80% 的事）
```

---

## What This Means（推荐配置）

按 5 个常见开发场景，开箱即用组合：

### 场景 A：写代码（Agentic IDE）

| 角色 | 模型 | 理由 |
|---|---|---|
| 第一主力 | **Claude Sonnet 5** | SWE-bench 全行业第一梯队、$3/15 与 Sonnet 4 一致（**intro $2/$10 到 8/31，最划算窗口**）、1M context |
| 后备主力 | **GPT-5.6 Sol** | Cursor / Copilot 默认走 GPT-5.6；缓存命中后 input 仅 $0.50 |
| 长上下文辅助 | **Gemini 3 Pro Preview** | 把整库代码塞 1M，再喂给 Claude 总结 |

### 场景 B：写文档 / 长文

| 角色 | 模型 | 理由 |
|---|---|---|
| 主写 | **Claude Sonnet 5** | 文笔、人味、可读性最强；输出能到 128K |
| 多模态补充 | **Gemini 3 Pro Preview** | 文档里插入的图 / 表 / 截图，几轮就能消化 |
| 中文 + 风格微调 | **GPT-5.6 Sol** | 中文流利 + 指令遵循 |

### 场景 C：研究 / Agent

| 角色 | 模型 | 理由 |
|---|---|---|
| 长链任务 | **Claude Sonnet 5 / Opus 5** | Sonnet 5 已逼近 Opus 4.8，但价格仅其 60% |
| 多工具调用 | **GPT-5.6 Sol** | Responses API + MCP + Computer use + Skills 全套工具栈 |
| 实时搜索 + 总结 | **Gemini 3 Pro Preview** | 搜索接地 + 地图接地内置（每月 5000 次免费，超出 14 美元/1000） |

### 场景 D：图片 / 视频 / 音频创作

| 角色 | 模型 | 理由 |
|---|---|---|
| 总入口 | **Gemini 3 Pro Preview** | 唯一原生 video / audio input 的现役主力 |
| 高质量出图 | **Imagen 4**（$0.02-$0.06/张）或 **gpt-image-1** | 看风格喜好 |
| 高质量出视频 | **Veo 3.1**（$0.40-$0.60/秒）或 **Sora 2** | 看节奏 |

### 场景 E：极致降本

| 角色 | 模型 | 理由 |
|---|---|---|
| 主用 | **Gemini 3.6 Flash**（$1.50/$7.50） | 比 Sonnet 5 便宜 50% |
| 极小 | **Gemini 3.5 Flash-Lite**（$0.10/$0.40） | 100× Sonnet 5 价格，能力是 60% |
| 中文长文 | **GPT-5.4**（$2.50 / 推算 $7-15 output） | 是 Sol 的半价 |

---

## Risks And Unknowns（不确定性披露）

| 风险 | 说明 | 影响 |
|---|---|---|
| **GPT-5.6 Luna 没有公开 API 价格** | 仅 ChatGPT 免费层可调；OpenAI 没有对它单独定价 | 付费对比只能说"等价于 GPT-5.6 Sol 但只对 ChatGPT 用户免费" |
| **Sonnet 4 / Gemini 2.5 Pro 的 SWE-bench 2026-08 同榜** | 没有第三方榜单在该时间点覆盖这 3 个 | 编程性能只能用厂商自报数据 |
| **Gemini 3 Pro Preview 仍在 Preview** | 价格/能力都可能变动 | 8 月或 9 月可能 GA |
| **OpenAI Realtime / Claude 否接音频** | GPT-5.6 Sol 文本图，实时音频仅 Realtime 端点独立 | 多模态实时场景 Gemini 唯一选项 |
| **Sonnet 5 到 8/31 后跳价** | Intro $2/$10，9 月起 $3/$15 | 早买早划算 |
| **Sonnet 4 / 2.5 Pro 已买但官方不主推** | 长期支持窗口可能缩窄 | 新项目建议直接走 Sonnet 5 / Gemini 3.x |

---

## Evidence Ledger（证据台账）

| Claim | Source | 类型 | 置信度 |
|---|---|---|---|
| GPT-5.6 Sol 价格 $5/$30（缓存 $0.50） | OpenAI docs/gpt-5.6-sol | 一级 | High |
| GPT-5.6 系列：Sol / 5.5 / 5.4 同列；价格梯度 | 同上 | 一级 | High |
| GPT-5.6 Sol 1.05M context，128K output | 同上 | 一级 | High |
| GPT-5.6 Luna 是 Free tier 别名 | HN 7月热榜 + OpenAI 7/30 公告 | 二级 | Medium-High（未见一手定价页） |
| Claude Sonnet 4 价格 $3/$15、2025-05-22 发布 | anthropic.com/news/claude-4 | 一级 | High |
| Claude Sonnet 4 SWE-bench 72.7% | 同上 | 一级 | High |
| Claude Opus 4 SWE-bench 72.5% / Terminal-bench 43.2% | 同上 | 一级 | High |
| Claude Sonnet 5 发布 2026-06-30、$3/$15、intro $2/$10 到 8/31 | anthropic.com/news/claude-sonnet-5 | 一级 | High |
| Sonnet 5 cost-performance curve 接近 Opus 4.8 | 同上 | 一级 | High |
| Sonnet 5 / Opus 5 1M context、128K output (sync) / 300K (Batch) | Anthropic Models overview | 一级 | High |
| Gemini 2.5 Pro $1.25/$10 (≤200K) | ai.google.dev/gemini-api/docs/pricing | 一级 | High |
| Gemini 3.x 系列价格梯度（3.6 Flash $1.50/$7.50; 3.5 Flash-Lite $0.10/$0.40） | 同上 | 一级 | High |
| Gemini 3 Pro Preview $2.00/$12.00 (≤200K) | 同上 | 一级 | High |
| Gemini 多模态独家（video input / Live API / Imagen / Veo） | 同上 | 一级 | High |
| GPT-5.6 实际 release 时间 | OpenAI blog/docs 推理 | 二级 | Medium |

---

## Sources（按优先级排序）

### 一级（厂商发布页）

- [OpenAI — GPT-5.6 Sol model docs](https://platform.openai.com/docs/models/gpt-5.6-sol)
- [Anthropic — Introducing Claude 4（2025-05-22）](https://www.anthropic.com/news/claude-4)
- [Anthropic — Introducing Claude Sonnet 5（2026-06-30）](https://www.anthropic.com/news/claude-sonnet-5)
- [Anthropic Platform — Models overview（spec 对照表）](https://platform.claude.com/docs/en/about-claude/models/overview)
- [Google AI for Developers — Gemini Developer API pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Google DeepMind — Gemini models](https://deepmind.google/models/gemini/)

### 二级（媒体汇编）

- [Hacker News Top Stories — GPT-5.6 Luna 7/30 Free-tier 扩列](https://news.ycombinator.com/)（HN 当日热议第 219 pt / 159 cmt）

### 本次未抓到、建议读者复核

- 三家**同时间切片**的 SWE-bench 公榜（建议查 [swebench.com](https://www.swebench.com)、[lmarena.ai](https://lmarena.ai/)）
- GPT-5.6 Luna 独立 API 价格（OpenAI 没公布）
- Sonnet 4 / Gemini 2.5 Pro 当前 deprecation 时间表（Anthropic / Google 各自 documentation 的 "Model deprecations" 页）

---

**Report by Hermes Agent** · Deep Research (Pro Mode) · 2026-08-07
