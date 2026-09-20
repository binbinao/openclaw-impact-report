# Hugging Face 与 ModelScope 平台每日模型追踪报告（2026年3月24日）

## 1. 报告摘要

本报告追踪了 **Hugging Face** 和 **ModelScope** 两大主流AI模型平台在2026年3月24日的最新动态。Hugging Face 平台目前托管超过 **200万个公开模型**，用户数达 **1300万**[2][4]；ModelScope 持续深耕中文开源生态，Qwen3.5 系列正式发布并支持12GB显存LoRA微调[11]。

**主要发现**：
- **中国模型全球崛起**：中国厂商开发的模型占全球总下载量的 **41%**，首次超越美国[2][21]
- **调用量霸榜**：MiniMax M2.5 连续5周蝉联全球调用量冠军，周调用量达 **1.75万亿Token**[13][34]
- **智能体经济爆发**：OpenClaw 框架获 **25万GitHub星标**，引发大厂"养虾"热潮[15]
- **小模型成本革命**：GPT-5.4 nano 定价仅 **$0.20/百万Token**，行业进入"分钱计费"时代[26]

---

## 2. 🔥 热门趋势模型高亮

以下模型在近期呈现显著增长（增长超50%或累计增长超100次），按热度等级标注：

|热度|模型名称|开发者|增长亮点|
|:---:|:---|:---|:---|
|🔥🔥🔥|**MiniMax M2.5**|MiniMax|连续5周全球调用量第一，周调用量**1.75万亿Token**[13][34]|
|🔥🔥🔥|**Qwen3.5系列**|阿里巴巴|累计下载超**10亿次**，中国模型占全球下载**41%**[2][21]|
|🔥🔥🔥|**OpenClaw**|开源社区|GitHub星标突破**25万**，智能体框架新王者[15]|
|🔥🔥|**小米MiMo-V2-Pro**|小米|**1万亿参数**，全球第8、国内第2[29][31]|
|🔥🔥|**GLM-5-Turbo**|智谱AI|OpenClaw场景优化，Agent调用精准度**国产第1**[21][22]|
|🔥🔥|**Step 3.5 Flash**|阶跃星辰|全球调用量第2，Agent专用基座[13]|
|🔥|**Kimi K2.5**|月之暗面|被Cursor Composer 2采用，训练效率提升**1.25倍**[35][36]|
|🔥|**Mistral-Small-4-119B**|Mistral AI|Trending榜持续霸榜，**256k上下文**[1][5]|

---

## 3. Hugging Face 平台最新模型

|模型名称|模型链接|模型归类|模型简介|应用场景|
|:---|:---|:---|:---|:---|
|**Mistral-Small-4-119B-2603**|[HuggingFace](https://huggingface.co/mistralai/Mistral-Small-4-119B-2603)|文本生成|119B MoE参数（激活6.5B），支持256k上下文，长文本推理能力比肩GPT-OSS 120B[1][5]|长文档分析、数学推理、代码生成|
|**BitNet b1.58**|[HuggingFace](https://huggingface.co/blog/qvac/fabric-llm-finetune-bitnet)|文本生成|1比特LLM架构，显存占用比Gemma-3-1B低77.8%[3]|边缘侧AI、端侧部署、资源受限场景|
|**Qwen3.5-4B**|[HuggingFace](https://huggingface.co/Qwen)|文本生成|9.3GB模型大小，支持12GB显存LoRA微调，中文评测超75分[11]|医疗AI助手、垂直领域微调|
|**NVIDIA Nemotron 3 Ultra**|[NVIDIA](https://developer.nvidia.com)|文本生成|Blackwell架构优化，高吞吐推理[22][23]|企业级推理、高并发服务|
|**NVIDIA Nemotron 3 Nano 4B**|[NVIDIA](https://developer.nvidia.com)|文本生成|混合Mamba-Transformer架构，专为边缘侧设计[23][28]|IoT设备、移动端部署|

---

## 4. ModelScope 平台最新模型

|模型名称|模型链接|模型归类|模型简介|应用场景|
|:---|:---|:---|:---|:---|
|**Qwen3.5-4B-Instruct**|[ModelScope](https://modelscope.cn/models/Qwen/Qwen3.5-4B-Instruct)|文本生成|原生中文优化，C-EVAL/CMMLU超75分，支持12GB显存LoRA微调[11][13]|医疗、法律、金融垂直领域|
|**Qwen3.5-72B**|[ModelScope](https://modelscope.cn/models/Qwen/Qwen3.5-72B)|文本生成|旗舰级多语言模型，代码与数学能力大幅提升[18]|企业级对话、复杂推理|
|**悟空企业AI平台**|[阿里云](https://wukong.aliyun.com)|智能体|电商智能体平台，深度集成钉钉生态[13]|电商运营、客服自动化|
|**Wan 2.0**|[ModelScope](https://modelscope.cn/models/Qwen/Wan2.0)|视频生成|通义视频生成模型更新版[18]|短视频创作、广告制作|

---

## 5. 全球厂商最新模型

### 5.1 国际厂商

|厂商|模型名称|模型归类|模型简介|应用场景|定价|
|:---|:---|:---|:---|:---|:---|
|OpenAI|**GPT-5.4 mini**|文本生成|速度提升2倍，子智能体架构[26][28]|通用对话、Agent协调|$0.75/百万Token|
|OpenAI|**GPT-5.4 nano**|文本生成|专为分类和数据提取设计[26]|数据标注、文本分类|$0.20/百万Token|
|Anthropic|**Claude Haiku 4.5**|文本生成|代码与Agent能力匹配前代Sonnet 4[13][28]|代码生成、智能体任务|$1/百万Token|
|Google|**Gemini 2.5 Flash-Lite**|文本生成|市场最廉价生产级模型[13][25]|大规模自动化、成本敏感场景|$0.10/百万Token|
|NVIDIA|**Nemotron 3系列**|文本生成|Ultra/Omni/Nano三版本，GTC 2026发布[22][23]|企业推理、多模态、边缘部署|企业定制|
|Mistral AI|**Mistral Forge**|平台服务|允许从零训练领域模型[22][24]|企业定制化训练|企业定制|

### 5.2 中国厂商

|厂商|模型名称|模型归类|模型简介|应用场景|行业地位|
|:---|:---|:---|:---|:---|:---|
|小米|**MiMo-V2-Pro**|文本生成|1万亿参数，100万上下文[29][31]|复杂推理、超长文档|全球第8、国内第2|
|智谱AI|**GLM-5-Turbo**|文本生成|针对OpenClaw智能体深度优化[21][22]|Agent场景、工具调用|Agent精准度国产第1|
|字节跳动|**豆包2.0**|多模态|逻辑推理提升37%，支持8K视频生成[23][28]|视频创作、多模态对话|国内MAU 2.26亿|
|MiniMax|**M2.5**|文本生成|连续5周全球调用量冠军[13][34]|智能体场景、高性价比|全球调用量第1|
|月之暗面|**Kimi K2.5**|文本生成|注意力残差技术，训练效率升1.25倍[35][36]|编程辅助、长文本|被Cursor采用|

---

## 6. 行业趋势分析

### 6.1 Agent化（智能体化）浪潮

2026年3月，开源智能体框架 **OpenClaw**（俗称"龙虾"）在GitHub获得25万星标，引发了行业的"养虾"热潮[15]。模型不再仅仅是对话框，而是具备工具调用、长链路执行能力的行动者。智谱GLM-5-Turbo和小米MiMo-V2-Pro均将Agent性能作为核心卖点[21][31]。百度推出DuClaw，阿里云推出JVS Claw，旨在通过一键部署能力抢夺AI时代的超级入口[13]。

### 6.2 小模型效率竞赛（分钱计费时代）

GPT-5.4 nano（$0.20/百万Token）、Gemini 2.5 Flash-Lite（$0.10/百万Token）等模型的发布，标志着行业进入了"分钱计费"的极低成本自动化时代[13][26]。BitNet b1.58的1比特架构在显存占用上比Gemma-3-1B低77.8%，极大推动了边缘侧AI的普及[3]。

### 6.3 多模态原生化

Kimi K2.5和豆包2.0均实现了视觉、语音、文本的原生融合，不再依赖外部插件[23][35]。字节跳动的豆包2.0支持8K视频生成，多模态能力成为旗舰模型的标配。

### 6.4 中国开源生态崛起

2026年春季报告显示，中国已在月度及总下载量上超越美国，中国厂商开发的模型占据了过去一年全球总下载量的**41%**[2][21]。独立开发者或非关联开发者的贡献占比升至39%，而传统大厂的开发份额降至37%[2]。

---

## 7. 模型调用量排行榜（2026年3月第3周）

根据OpenRouter及社区统计数据，全球模型调用量排名如下：

|排名|模型名称|开发者|周调用量|备注|
|:---:|:---|:---|:---|:---|
|🥇|**MiniMax M2.5**|MiniMax|1.75万亿Token|连续5周冠军[13][34]|
|🥈|**Step 3.5 Flash**|阶跃星辰|-|Agent专用基座[13]|
|🥉|**DeepSeek V3.2**|DeepSeek|1.04万亿Token|长上下文王者[13]|
|4|**Xiaomi MiMo-V2-Pro**|小米|-|测试期代号Hunter Alpha[29]|
|5|**GLM-5-Turbo**|智谱AI|-|Agent精准度第1[21]|

---

## 8. 参考文献

[1] Hugging Face, 2026-03-18. mistralai/Mistral-Small-4-119B-2603. https://huggingface.co/mistralai/Mistral-Small-4-119B-2603

[2] Hugging Face Blog, 2026-03-17. State of Open Source on Hugging Face: Spring 2026. https://huggingface.co/blog/huggingface/state-of-os-hf-spring-2026

[3] QVAC Fabric, 2026-03-17. LoRA Fine-Tuning BitNet b1.58 LLMs on Heterogeneous Hardware. https://huggingface.co/blog/qvac/fabric-llm-finetune-bitnet

[4] Kukarella News, 2026-03-17. Hugging Face's Open Source AI Ecosystem Explodes. https://kukarella.com/news/hugging-faces-open-source-ai-ecosystem-explodes-p1773784803

[5] Silicon Republic, 2026-03-18. Mistral AI makes enterprise push with two new launches. https://siliconrepublic.com/machines/mistral-ai-france-small-4-forge-enterprise

[11] GitCode CSDN, 2026-03-23. Qwen3.5微调实战教程（非常详细），医疗AI助手从入门到精通. https://gitcode.csdn.net/69c0ba2754b52172bc637528.html

[13] TechInformed, 2026-03-20. OpenAI joins Anthropic and Google in the race for cheaper AI work. https://techinformed.com/openai-joins-anthropic-and-google-in-the-race-for-cheaper-ai-work

[15] 21财经, 2026-03-18. 傅盛玩「小龙虾」成热点，普通人该如何接住AI红利？. https://21jingji.com/article/20260318/herald/4038ec4be6007a9a9e2d61b9a46406a6.html

[18] 知乎专栏, 2026-03-23. AI 早报2026-03-23. https://zhuanlan.zhihu.com/p/2019331243498550593

[21] 新浪财经, 2026-03-19. 中国大模型第一股，彻底爆了. https://finance.sina.com.cn/tech/roll/2026-03-19/doc-inhrnqzz8771991.shtml

[22] NVIDIA Investor, 2026-03-16. NVIDIA Launches Nemotron Coalition of Leading Global AI Labs. https://investor.nvidia.com/news/press-release-details/2026/NVIDIA-Launches-Nemotron-Coalition-of-Leading-Global-AI-Labs-to-Advance-Open-Frontier-Models/default.aspx

[23] 新浪财经, 2026-03-18. 字节跳动火山引擎重磅发布:豆包大模型2.0将于2026年情人节升级. https://cj.sina.cn/articles/view/7879848900/1d5acf3c401902s5nm

[24] Zapier, 2026-03-24. Meta AI vs. ChatGPT: Which is better? [2026]. https://zapier.com/blog/meta-ai-vs-chatgpt

[25] LLM Stats, 2026-03-20. Gemini 3 Pro vs Gemini 2.5 Flash-Lite Comparison. https://llm-stats.com/models/compare/gemini-3-pro-preview-vs-gemini-2.5-flash-lite

[26] 9to5Mac, 2026-03-17. OpenAI releases GPT-5.4 mini and nano. https://9to5mac.com/2026/03/17/openai-releases-gpt-5-4-mini-and-nano-its-most-capable-small-models-yet

[28] The Neuron, 2026-03-18. OpenAI GPT-5.4 Mini and Nano: Subagents Explained. https://theneurondaily.com/p/openai-gave-gpt-5-4-mini-its-own-interns

[29] 香港商報, 2026-03-19. 小米發布AI大模型MiMo. https://hkcd.com.hk/hkcdweb/content/2026/03/19/content_8745636.html

[31] 小米官网, 2026-03-18. Xiaomi MiMo-V2-Pro. https://mimo.xiaomi.com/mimo-v2-pro

[34] 驱动之家, 2026-03-23. 国产大模型MiniMax M2.5再霸榜！连续5周全球大模型调用量冠军. https://news.mydrivers.com/1/1110/1110841.htm

[35] 新浪财经, 2026-03-18. 月之暗面创始人杨植麟首度披露 Kimi K2.5 技术路线. https://finance.sina.com.cn/tech/digi/2026-03-18/doc-inhrknav7633960.shtml

[36] 财新网, 2026-03-22. 美国AI编程应用Cursor承认新模型系基于Kimi K2.5 训练. https://caixin.com/2026-03-22/102425978.html

---

*报告生成时间：2026年3月24日 10:36 CST*