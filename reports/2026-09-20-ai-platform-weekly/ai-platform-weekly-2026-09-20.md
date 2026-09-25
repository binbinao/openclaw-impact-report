# AI 模型平台周报：Hugging Face 与 ModelScope 最新动态追踪

**报告日期**：2026年9月20日  
**数据周期**：2026年9月14日 - 9月20日（2026年第38周）  
**数据来源**：Hugging Face Trending Models / Daily Papers / Trending Spaces、ModelScope 热门模型榜单、OpenRouter 调用量统计、行业公开报道

---

## 1. 执行摘要

2026年9月第三周，全球AI领域正式进入"智能体（Agentic AI）"爆发期。本周最显著的结构性变化是开源模型在调用量上对闭源模型的全面反超——开源模型已占据全球总调用量的78.4% [10]。中国AI生态表现尤为强劲，周调用量达61.17万亿Token，连续20周领跑全球 [9]。Hugging Face平台经历了重大格局变动，Nvidia宣布以约130亿美元的价格对其进行收购，这一交易将深刻影响开源AI基础设施的未来走向 [6]。在模型发布方面，OpenAI GPT-6 Astra的余温尚在，国内阶跃星辰Step 5 Preview与智谱GLM-5.3-FlashX的密集发布标志着国产大模型在推理速度与逻辑深度上已跨入全球第一梯队。本周研究重心从单纯的参数规模竞赛转向"递归自我改进（RSI）"与"空间理解"能力，AI正在从被动的文本生成工具进化为具备自主规划与行动能力的数字员工 [4]。

---

## 2. 🔥 热门趋势模型高亮区

以下模型在本周出现了显著增长（较前一日增长超过50%或累计增长超过100次），按热度分级标注：

| 热度 | 模型名称 | 增长类型 | 增长数据 | 增长原因分析 |
|:---|:---|:---|:---|:---|
| 🔥🔥🔥 | **GLM-5.3-FlashX** | 企业接入量环比增长 | **+60%** | 推理速度提升至200 tokens/s，9月18日发布后企业端快速接入 [11] |
| 🔥🔥🔥 | **DeepSeek-V4.1-Flash** | 72小时调用量爆发 | **指数级增长** | 9月10日发布后，OpenRouter平台调用量72小时内冲入全球前六 [9] |
| 🔥🔥 | **小米 MiMo-V2.5** | 周调用量环比增长 | **+230%** | 重回全球调用量前五，端侧部署优势持续释放 [9] |
| 🔥🔥 | **Qwen3.8-27B-GSQ** | 周下载量 | **47.9万次** | 量化版本下载增速首次超过原版模型，本地部署需求旺盛 [2] |
| 🔥🔥 | **Ternary Bonsai 2 27B** | 新发布即上榜 | **9月20日上线** | 三元权重压缩技术将53.8GB压缩至5.93GB，性能保留98.2% [2] |
| 🔥 | **DeepSeek-V4.1-Flash FP8量化版** | 72小时社区衍生下载 | **2200+次** | 社区自发量化优化，降低部署门槛 [7] |
| 🔥 | **LimiX-2** | GitHub星标 | **4200+** | 结构化数据处理全球Elo排名第一 [4] |

---

## 3. Hugging Face 平台结构化表格

### 3.1 Trending Models Top 15

本周Hugging Face榜单由Qwen 3.8家族与高效边缘模型主导，量化版本（GGUF/GSQ）的下载增速首次超过原版模型，反映出开发者对本地化部署的强烈需求。

| 模型名称 | 模型链接 | 模型归类 | 模型简介 | 模型应用场景 |
|:---|:---|:---|:---|:---|
| google/timesfm-3.0-pytorch | [链接](https://huggingface.co/google/timesfm-3.0-pytorch) | 时间序列预测 | Google推出的时间序列基础模型，44.4万次下载，领域SOTA性能 | 金融预测、能源负荷预测、零售需求预测 |
| Qwen/Qwen3.8-27B | [链接](https://huggingface.co/Qwen/Qwen3.8-27B) | 多模态理解与生成 | 阿里通义千问最新旗舰，670万次下载，1.4万星标，支持图文多模态理解 | 智能客服、内容创作、代码生成、多模态问答 |
| ISTA-DASLab/Qwen3.8-27B-GSQ | [链接](https://huggingface.co/ISTA-DASLab/Qwen3.8-27B-GSQ) | 量化推理 | Qwen3.8-27B的GSQ量化版本，47.9万次下载，增长极快 | 本地部署、边缘计算、资源受限环境推理 |
| openbmb/MiniCPM5-2B | [链接](https://huggingface.co/openbmb/MiniCPM5-2B) | 边缘端生成 | 面壁智能2B参数轻量模型，33万次下载，高点赞比 | 手机端AI助手、嵌入式设备、离线翻译 |
| XHToken/Spark-X2.5-4B | [链接](https://huggingface.co/XHToken/Spark-X2.5-4B) | 轻量化智能体 | 4B参数轻量智能体模型，3万次下载，适配RTX PC | 桌面端AI助手、自动化办公、个人知识管理 |
| Edge0/Edge0-35B-A3B-preview | [链接](https://huggingface.co/Edge0/Edge0-35B-A3B-preview) | MoE文本生成 | 35B参数MoE架构预览版，下载量突破3.7万 | 文本生成、对话系统、内容摘要 |
| deepseek-ai/DeepSeek-V4.1-Flash | [链接](https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash) | 多模态/Agent | DeepSeek最新Flash版本，39.1万次下载，KV缓存减少75% | 智能体任务、图文理解、高效推理 |
| zai-org/GLM-5.3 | [链接](https://huggingface.co/zai-org/GLM-5.3) | 通用大模型 | 智谱AI 753B参数旗舰模型，88.8万次下载 | 通用对话、复杂推理、科学研究辅助 |
| m-a-p/YuE2-3B | [链接](https://huggingface.co/m-a-p/YuE2-3B) | 音频/音乐生成 | 3B参数音乐生成模型，1.1万次下载，音频榜第一 | 音乐创作、背景音乐生成、音频内容生产 |
| Lightricks/LTX-2.5 | [链接](https://huggingface.co/Lightricks/LTX-2.5) | 视频生成 | Lightricks开源视频生成标杆，160万次下载 | 短视频创作、广告制作、影视预演 |
| TokenRhythm/NeoHorse-1-4B | [链接](https://huggingface.co/TokenRhythm/NeoHorse-1-4B) | 小参数推理 | 4B参数推理模型，高增长率，适配移动端 | 移动端推理、实时对话、轻量级Agent |
| tencent/AuK | [链接](https://huggingface.co/tencent/AuK) | 语音编辑/生成 | 腾讯混元系列新基座，专注语音编辑与生成 | 语音合成、音频编辑、语音克隆 |
| MiniMaxAI/MiniMax-H3 | [链接](https://huggingface.co/MiniMaxAI/MiniMax-H3) | 全模态生成 | MiniMax全模态生成模型，支持2K视频+原生音频 | 视频生成、音频生成、多模态内容创作 |
| unsloth/Qwen3.8-27B-GGUF | [链接](https://huggingface.co/unsloth/Qwen3.8-27B-GGUF) | 本地部署优化 | Qwen3.8-27B的GGUF量化版本，开发者首选微调底座 | 本地推理、模型微调、私有化部署 |
| meta-llama/Llama-3.1-8B | [链接](https://huggingface.co/meta-llama/Llama-3.1-8B) | 指令遵循 | Meta经典8B模型，保持高热度长青 | 指令遵循任务、文本分类、基础NLP |

### 3.2 Daily Papers 热门论文

本周研究重心从单纯的参数规模转向"递归自我改进（RSI）"与"空间理解" [4]。

| 论文名称 | 论文链接 | 研究归类 | 论文简介 | 应用场景 |
|:---|:---|:---|:---|:---|
| Vidu S2 (清华大学) | [链接](https://huggingface.co/papers/week/2026-W38) | 空间视频生成 | 聚焦实时交互式、可编辑的空间视频生成，获得超过680个点赞 | 空间视频创作、交互式媒体、虚拟现实 |
| Atria Dawn (InternLM) | [链接](https://huggingface.co/papers/week/2026-W38) | 智能体超智能 | 提出"智能体超智能"概念，通过验证工具交互训练科学研究智能体 | 科学研究自动化、智能体训练、知识发现 |
| ScienceBuddy | [链接](https://huggingface.co/papers/week/2026-W38) | 递归自我改进 | 研究递归自我改进方法，将生物医学准确率从42.2%提升至73.3% | 生物医学研究、药物发现、精准医疗 |
| LimiX-2 (Stable AI) | [链接](https://huggingface.co/papers/week/2026-W38) | 结构化数据智能 | 针对结构化数据智能的上下文机制网络，GitHub星标突破4200 | 数据分析、表格理解、结构化信息提取 |

### 3.3 Trending Spaces 热门应用

| 应用名称 | 应用链接 | 应用归类 | 应用简介 | 应用场景 |
|:---|:---|:---|:---|:---|
| YuE2-3B Music Generator | [链接](https://huggingface.co/spaces) | 音乐生成 | 支持从歌词和风格提示词生成完整歌曲 | 音乐创作、歌曲demo制作、风格化音乐 |
| MiniCPM5-2B WebGPU Pi | [链接](https://huggingface.co/spaces) | 浏览器编码智能体 | 完全在浏览器中运行的编码智能体，利用WebGPU实现零服务器成本推理 | 浏览器端编程辅助、在线代码生成、轻量开发 |
| StepAudio 3 Music Studio | [链接](https://huggingface.co/spaces) | 音频协作工具 | 阶跃星辰出品的协作式音频混音与人声编排工具 | 音频后期制作、多人协作混音、人声处理 |

---

## 4. ModelScope 平台结构化表格

### 4.1 热门模型榜单 Top 10

| 模型名称 | 模型链接 | 模型归类 | 模型简介 | 模型应用场景 |
|:---|:---|:---|:---|:---|
| Xing4.0-29B-A4B (星辰) | [链接](https://aipintai.com/post/700) | 通用大模型 | 中电信发布，国内首个全栈国产化（昇腾+昇思）百亿模型 | 政务AI、企业服务、国产化替代 |
| ZDTaichu5.0-9B (紫东太初) | [链接](https://aipintai.com/post/700) | 空间理解 | 空间理解能力登顶，对标GPT-6 Astra | 空间推理、机器人导航、3D场景理解 |
| Atria-Dawn-Preview | [链接](https://aipintai.com/post/700) | 智能体模型 | 7440亿参数超大规模智能体模型 | 科学研究智能体、复杂任务规划、自主决策 |
| DeepSeek-V4.1-Flash | [链接](https://aipintai.com/post/700) | 多模态/Agent | 跨平台流量明星，图文理解效率极高 | 智能体任务、图文理解、高效推理 |
| LimiX-2 | [链接](https://aipintai.com/post/700) | 结构化数据处理 | 结构化数据处理全球Elo排名第一 | 表格分析、数据提取、结构化信息处理 |
| Ternary Bonsai 2 27B | [链接](https://aipintai.com/post/700) | 极致压缩模型 | 三元权重压缩技术，53.8GB压缩至5.93GB，性能保留98.2% | 消费级显卡部署、边缘推理、资源受限场景 |
| Meridian (Viggle AI) | [链接](https://aipintai.com/post/700) | 视频生成 | 几何引导视频生成模型 | 视频创作、动画制作、几何场景生成 |
| LingBot-VLA 2.0 | [链接](https://aipintai.com/post/700) | 具身智能 | 视觉-语言-动作一体化模型 | 机器人控制、具身智能、自动化操作 |
| Qwen3.8-27B-Instruct | [链接](https://aipintai.com/post/700) | 指令微调 | 社区微调热度最高的底座模型 | 指令遵循、对话系统、定制化微调 |
| StepAudio 3 | [链接](https://phemex.com/news/article/zhipu-launches-glm53flashx-model-with-200-tokenss-inference-speed-97092) | 语音交互 | 实时语音交互模型系列 | 语音助手、实时对话、语音合成 |

### 4.2 平台重要更新与活动

| 更新项目 | 更新类型 | 上线日期 | 内容简介 | 影响与意义 |
|:---|:---|:---|:---|:---|
| WorldSimReady-Home 数据集 | 数据集 | 9月18日 | 包含10万平方米高保真家居场景 | 助力具身智能Sim2Real迁移 [5] |
| 魔搭紫皮书 | 指南文档 | 9月17日 | 《开源模型社区实战指南》正式发布 | 系统化指导开发者应用开源AI [5] |
| 具身智能挑战赛 | 竞赛活动 | 本周启动 | 蚂蚁灵波联合魔搭发起，奖金池28万元 | 推动模型向机器人场景落地 [2] |

---

## 5. 本周重大发布汇总

| 发布日期 | 模型/产品 | 发布方 | 核心特性 | 关键指标 |
|:---|:---|:---|:---|:---|
| 9月20日 | Step 5 Preview | 阶跃星辰 | 600B参数MoE架构，API预览开启 | 推理得分比肩Kimi K3 [11] |
| 9月20日 | Ternary Bonsai 2 27B | 社区 | 三元权重压缩技术 | 53.8GB→5.93GB，性能保留98.2% [2] |
| 9月18日 | GLM-5.3-FlashX | 智谱AI | 推理速度200 tokens/s | 企业接入量环比+60% [11] |
| 9月15日 | Gemini 3.8 Live | Google | 近实时语音和视觉交互 | 音频基准得分97.7% [1] |
| 9月10日 | DeepSeek-V4.1-Flash | DeepSeek | KV缓存减少75% | 72小时冲入全球前六 [9] |
| 9月2日 | Muse Spark 1.3 | Meta | 闭源旗舰，默认路由模型 | 单价降至$0.10/1M tokens [8] |

---

## 6. 融资与行业动态

### 6.1 融资事件

| 公司 | 融资轮次 | 融资金额 | 估值 | 资金用途 |
|:---|:---|:---|:---|:---|
| Crusoe | F轮 | 3.9亿美元 | 30.9亿美元 | 建设"AI工厂" [6] |
| 智谱AI | 新一轮 | 约50亿美元 | 大幅攀升 | 投入"全自我训练"系统 [11] |
| Temporal Technologies | 战略融资 | 5.5亿美元 | 未披露 | 长程AI智能体运行平台 [6] |

### 6.2 重大行业事件

**Nvidia收购Hugging Face**：Nvidia宣布以约130亿美元的价格收购Hugging Face，这一交易将重塑开源AI基础设施格局。Hugging Face作为全球最大的开源模型托管平台，其归属变更将对模型分发、社区治理和开源生态产生深远影响 [6]。

**OpenAI GPT-6 Astra更新**：9月初发布后进入大规模企业应用阶段，本周重点更新了"Daybreak"网络安全防护版本，强化了模型在安全领域的应用能力 [1]。

**Meta Muse Spark 1.3**：本周确认为Meta AI的默认路由模型，单价降至$0.10/1M tokens，标志着闭源旗舰模型进入价格竞争阶段 [8]。

---

## 7. 全球调用量数据

本周全球AI总调用量达**127万亿Token**，创历史新高。中国厂商表现亮眼，具体数据如下：

| 排名 | 模型/厂商 | 周调用量 | 环比变化 | 备注 |
|:---|:---|:---|:---|:---|
| 1 | 中国模型合计 | 61.17万亿Token | 稳定增长 | 连续20周领跑全球 [9] |
| 2 | 腾讯混元Hy4 Preview | 16.8万亿Token | 稳定 | 全球单模型第二 [9] |
| 3 | 小米MiMo-V2.5 | 未披露 | **+230%** | 重回全球前五 [9] |
| - | 全球开源模型占比 | 78.4% | 持续上升 | 开源全面反超闭源 [10] |

---

## 8. 关键趋势分析

### 8.1 全栈国产化加速

以星辰Xing4.0为代表，中国AI产业实现了从算力（昇腾）、框架（昇思）到模型架构的完全自主可控，且性能达到国际领先水平。这一趋势标志着中国AI生态正在摆脱对国外技术栈的依赖，构建完整的自主创新体系 [2]。

### 8.2 从对话到行动：Agentic AI成为主旋律

本周发布的所有旗舰模型（GPT-6 Astra、Gemini 3.8 Live、Step 5 Preview）均强调"计算机使用"和"自主规划"能力。AI正在从聊天机器人进化为能够自主执行任务的数字员工，这一转变将深刻影响企业工作流程和生产力工具的设计 [8]。

### 8.3 小模型统治下载榜

尽管万亿参数模型频出，但83%的下载量仍集中在1B以下的轻量化模型。这一数据揭示了端侧部署的强劲需求——开发者更倾向于选择能够在本地设备上高效运行的小型模型，而非依赖云端推理的大型模型 [10]。

### 8.4 量化与压缩技术成为新战场

本周Qwen3.8-27B-GSQ量化版本下载增速首次超过原版模型，Ternary Bonsai 2以三元权重压缩技术实现89%的体积缩减。模型压缩与量化技术正在成为开源社区的新竞争焦点，直接影响模型的部署成本和可及性 [2]。

### 8.5 递归自我改进（RSI）研究升温

ScienceBuddy论文展示了递归自我改进方法将生物医学准确率从42.2%提升至73.3%的显著效果，Atria Dawn则提出了"智能体超智能"概念。这一研究方向预示着AI系统将具备自我优化能力，可能成为通向更高智能水平的关键路径 [4]。

---

## 参考文献

[1] [aireleasetracker.com - OpenAI & Google Model Releases September 2026](https://aireleasetracker.com/releases/september-2026)

[2] [aipintai.com - ModelScope 热门模型与 Xing4.0 发布动态 (2026-09-17)](https://aipintai.com/post/700)

[3] [huggingface.co - Trending Spaces and Models September 2026](https://huggingface.co/spaces)

[4] [huggingface.co - Daily Papers Highlights (Sept 14-20, 2026)](https://huggingface.co/papers/week/2026-W38)

[5] [cnblogs.com - 魔搭社区具身智能数据集与紫皮书上线 (2026-09-18)](https://cnblogs.com/know-data/p/19761045)

[6] [sacra.com - Nvidia Acquisition of Hugging Face and AI Funding Rounds](https://sacra.com/c/hugging-face)

[7] [vllm.ai - DeepSeek V4.1-Flash Community Adoption and Metrics](https://recipes.vllm.ai/deepseek-ai/DeepSeek-V4.1-Flash)

[8] [atlabyte.com - Meta Connect 2026 and Muse Model Strategy](https://atlabyte.com/en/news/meta-connect-2026-zuckerberg-to-unveil-camera-free-glasses-phoenix-headset-and-ai-agent-muse)

[9] [eastmoney.com - 全球 AI 大模型 Token 调用量周报 (2026-09-15)](https://finance.eastmoney.com/a/202609153874473329.html)

[10] [sina.cn - 中国模型下载量首超美国研究报告 (2026-09-16)](https://finance.sina.cn/stock/jdts/2026-09-16/detail-iniryvce3039106.d.html?node_id=76993)

[11] [phemex.com - 智谱 GLM-5.3-FlashX 与阶跃星辰 Step 5 发布动态](https://phemex.com/news/article/zhipu-launches-glm53flashx-model-with-200-tokenss-inference-speed-97092)