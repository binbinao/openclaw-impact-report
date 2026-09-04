# Cadence Design Systems（楷登电子）深度调研
## 产品系列 × 工厂使用环节（v2 — 完整证据版）

**调研日期**：2026-08-25
**公司全称**：Cadence Design Systems, Inc.（NASDAQ: CDNS，中文"楷登电子"）
**总部**：美国加州圣何塞
**2025 财年营收**：US$5.30 billion（YoY↑）
**员工数**：13,800（2025）
**CEO**：Anirudh Devgan（自 2021 年 12 月起）
**市场地位**：纳斯达克 100 + S&P 500 成分股
**2025 营业利润**：US$1.49 billion　**净利润**：US$1.11 billion

---

## 0. TL;DR（一句话 + 三条洞察）

**一句话定位**：Cadence 是全球三大 EDA 厂商之一（与 Synopsys、Siemens EDA 并列），业务从 IC 设计、PCB 与封装到多物理场系统仿真与 AI 驱动 EDA 全栈覆盖。

**三条洞察**：
1. **产品矩阵分 13 大类、~50 个核心 SKU**，但从工厂使用视角可压缩为"前端 → 后端 → 物理签收 → 封装/3D-IC → PCB/系统"五段链路，每一段都有 Cadence 自家的旗舰工具。
2. **Cadence 与四大代工的认证关系**：TSMC（OIP 创始 EDA 联盟、N3/N2/A16/A14 全栈 + 3DFabric + COUPE）、Samsung Foundry（2nm GAA + 3D-IC）、Intel Foundry（18A/18A-P/14A 全套数字 + 模拟 + IP）、Rapidus（2nm GAA + Agentic AI）—— 是事实上的"四大代工都选"的 EDA vendor。
3. **2025-2026 战略重心是 Agentic AI**：Cerebrus Intelligent Chip Explorer、Cerebrus AI Studio、InnoStack AI Super Agent、ChipGPT、Optimality Intelligent System Explorer 全部发布/升级，与三大代工的 PR 都强调 AI 自动化对 PPA 的提升。

---

## 一、产品系列全景（13 大类）

数据来源：[1][3][12]（Cadence 官方 + Wikipedia 合并整理）

| # | 类别 | 核心产品（代表） | 在半导体/工厂链路中的角色 |
|---|---|---|---|
| 1 | **Digital Design & Signoff** | Genus Synthesis、Innovus+ Implementation、Tempus Timing、Quantus Extraction、Quantus Field Solver、Voltus/Voltus-XFi Power Integrity、Certus Closure、Pegasus Verification & DFM、Liberate Characterization、Modus DFT、Joules RTL Power、Stratus HLS、Conformal AI Equivalence/ECO/Low-Power、InnoStack AI Super Agent[24] | 数字前端综合 → 布局布线 → 时序/功耗签收 → 物理验证 → 库表征 → 测试 |
| 3 | **Custom IC / Analog / RF Design** | Virtuoso Studio[32]、Spectre / Spectre X / Spectre FX / Spectre RF / Spectre AMS Designer / Spectre Photonics[33]、AWR Design Environment、Momentum | 模拟/RF/毫米波/光子设计全流程 |
| 4 | **Verification** | Xcelium Logic Simulation、JasperGold Formal Verification、vManager、Perspec System Verifier、Palladium Z1/Z2 Emulation、Protium X1/X2 FPGA Prototyping | 仿真 + 形式化 + 硬件加速 + FPGA 原型 |
| 5 | **Silicon Solutions / IP** | Tensilica（Vision/HiFi/Fusion/ConnX/DNA）、PCIe 7.0 at 128GT/s、HBM4 IP at N3P、LPDDR6/5X 14.4G、DDR5 12.8G MRDIMM Gen2、UCIe 32G、eUSB2V2、224G SerDes、Arm Artisan 基础 IP（2025-04 收购）[34] | SoC IP 模块 |
| 6 | **IC Package Design & Analysis** | Integrity 3D-IC Platform、Allegro X Advanced Package Designer、OrbitIO Interconnect Designer[26] | 先进封装 / chiplet / 3D-IC 设计与 sign-off |
| 7 | **Multiphysics System Analysis** | Clarity 3D Solver、Sigrity X / Aurora / Topology Workbench、Optimality Intelligent System Explorer、Celsius Thermal Solver、Voltus-XFi、Fidelity CFD、Fidelity Pointwise、Cadence Reality Digital Twin、Millennium M1 Supercomputer[14] | 跨 EM / 热 / CFD / SI/PI / 数字孪生 |
| 8 | **PCB Design & Analysis** | Allegro X System Design Platform、OrCAD X、PSpice、Allegro X Pulse、Allegro EDM、Allegro X AI Advanced Substrate Router[35][36] | 板级原理图 → 布局 → in-design SI/PI → 制造文档 |
| 9 | **AI / Generative AI EDA** | Cerebrus Intelligent Chip Explorer[30]、Cerebrus AI Studio[29]、ChipGPT、Innovus+ AI Assistant、JedAI Solution、Optimality Intelligent System Explorer、AI DRC Fix Assistant、Generative PCB Layout、Cadence.AI[28] | Agentic AI 自动优化 RTL → GDSII、3D-IC、PCB |
| 10 | **Embedded Software** | 嵌入式 / SoC 软件协同 | — |
| 11 | **CFD / Molecular Simulation / Data Center** | Fidelity CFD、Pointwise、OpenEye Scientific（Orion SaaS）、NV5 × Cadence 数据孪生[14] | 工厂 / 制药 / 数据中心 |
| 12 | **Generative AI / AI IP Platform** | Cadence.AI 总入口、AI IP Platform[34] | AI 软硬件平台 |

### 1.1 关键产品深度注解（产品经理视角）

- **Virtuoso Studio**（[32]）—— 原 Virtuoso Platform 更名而来；模拟与混合信号"瑞士军刀"，与 Innovus Implementation System 集成支持完整 mixed-signal 实现方法学。在 Intel 18A 节点已通过认证，支持 EM-IR checks、InDesign DRC、yield 优化。[39]
- **Spectre Platform**（[33]）—— Spectre X（并行 SPICE）、Spectre FX（FastSPICE）、Spectre RF（射频）、Spectre Photonics（光子）、Spectre AMS Designer（混合信号）五大模块。2019 年起 Spectre X 已支持百核 CPU/GPU 分布式仿真。[12]
- **Innovus+ Synthesis and Implementation**（[31]）—— P&R 旗舰，2020 年 Cadence 把 Innovus 的 P&R + optimizer 集成进 Genus 形成 unified flow；2025-2026 与 Innovus+ AI Assistant 整合 Cerebrus 提供 AI 推荐。[20][31]
- **Genus Synthesis Solution** —— RTL 综合，在 TSMC N3/N2/A16/A14、Intel 18A、Rapidus 2nm 均已认证。[20][39]
- **Tempus Timing Solution + ECO Option** —— STA + ECO，TSMC/Intel/Samsung 主流量产 sign-off 工具。[20][39]
- **Quantus Extraction Solution + Quantus Field Solver** —— 寄生 RC + 3D 电磁，已认证 TSMC N3/N2/A16、Intel 18A。[20][39]
- **Voltus / Voltus-XFi** —— IR-drop + EM 签收；Voltus-XFi 是先进节点自定义电源网格专用版，已认证 Intel 18A。[39]
- **Pegasus Verification System** —— 物理验证（DRC/LVS）+ DFM（Critical Area Analyzer、Layout Pattern Analyzer、CMP Predictor、Computational Pattern Analytics、MaskCompose Reticle & Wafer Synthesis Suite）。[4]
- **Liberate Trio / Variety / LV / MX / AMS** —— 标准单元 / SRAM / 混合信号库的 characterization。[4]
- **Conformal AI 系列** —— AI Equivalence、ECO、Low Power、Litmus、Constraint Designer。形式化等价 + 低功耗 + ECO 自动化。[4]
- **Cerebrus Intelligent Chip Explorer**（[30]）—— 2021 年发布，基于 reinforcement learning 自动探索 RTL-to-GDSII 实现空间。2026 年扩展为 Cerebrus AI Studio——把 RL + LLM agent + 大规模并行 cloud-HPC 整合。
- **Cerebrus AI Studio**（[29][38]）—— 2026 年新发布，是 Cerebrus + agentic AI 的 studio 版，允许多 agent 协同调试、实现、signoff、ECO、closure 自动化。[38]
- **Integrity 3D-IC Platform** —— 跨 die + interposer + substrate + package 统一数据库与 co-design 环境。是 TSMC 3DFabric、Samsung Foundry 2nm/3D-IC 的 reference flow 基础。[20][16]
- **Clarity 3D Solver**（[56]）—— 分布式自适应网格化 3D 电磁求解器，2019 年 4 月推出，目标替代 ANSYS HFSS。[12]
- **Sigrity X Platform**（[55]）—— SI/PI/热分析 PCB 与封装平台；Aurora 是 in-design 引擎，Topology Workbench 是约束管理 + SystemSI/SystemPI/Celsius 多物理场。[4][23]
- **Celsius Studio / Thermal Solver**（[58]）—— 电-热耦合求解，FEA + CFD，2019 年 9 月发布。TSMC-COUPE 硅光引擎电热仿真标配。[20]
- **Optimality Intelligent System Explorer** —— 2022 年发布的 AI 系统设计平台，与 Clarity、Sigrity X 兼容；Microsoft 是早期用户。[12]
- **Palladium Z1 / Z2 Emulation** —— ASIC 硬件仿真平台，10 亿门 SoC 验证，2015 / 2021 推出。Z2 性能 1.5×、容量 2×。[12]
- **Protium X1 / X2 FPGA Prototyping** —— Xilinx Virtex UltraScale FPGA 原型验证，2014/2017/2019/2021 推出。[12]
- **Tensilica** —— DSP IP 系列（图像/视觉/AI/音频/IoT/雷达/激光雷达），2013 年收购。[12]
- **AWR Design Environment** —— RF 至毫米波，2019 年 AWR 收购获得。[12]
- **OrCAD X / Allegro X** —— PCB 主力产品。Allegro X 面向企业（高密度互连、高速、多板、刚柔结合、ECAD/MCAD 协同）；OrCAD X 面向中小团队/学术。25.1 版本 2025 年 10 月发布含 Allegro X AI Advanced Substrate Router。[23][35][36]
- **OpenEye Scientific** —— 分子建模 SaaS（Orion 平台），2022 年 5 亿美元收购。[12]
- **Millennium M1 Supercomputer** —— 2024 年 2 月发布，CFD/数字孪生硬件。[12]
- **AI IP Platform**（[34]）—— Cadence 2025 年发布，整合 HBM4/PCIe 7.0/LPDDR6/UCIe 等硅验证 AI IP。
- **InnoStack AI Super Agent** —— 2026 年发布，把 Cerebrus + Conformal AI + Innovus+ AI Assistant + Voltus InsightAI 串成 agentic AI framework。TSMC N3/N2/A16 全流程已集成。[4]

---

## 二、在工厂/晶圆厂的具体使用环节

### 2.1 TSMC（台积电）—— 最深的 OIP 伙伴关系

Cadence 是 TSMC **Open Innovation Platform®（OIP）** 创始 EDA 联盟成员之一（[15]）；TSMC OIP EDA Alliance 官方页明确把 Cadence、Siemens EDA、Synopsys 列为三大 EDA 联盟成员，OIP 认证项目覆盖全流程。[47]

**【金标准数据】TSMC 官方 EDA Tool Certification Status（截至 2026-07-10，[47]）**：

TSMC 与三大 EDA 厂商联合的 EDA Tool Certification Program 覆盖最新先进工艺（A14、A16、N2P、N3C）与 3DFabric。Cadence 在以下节点的认证矩阵：

| 工艺节点 | Cadence 认证工具类别 |
|---|---|
| **A14** | APR / Lib. Characterization / Timing / Power / EMIR / DRC / Dummy Fill / LVS/LPE / RC / Custom Design / Tx EMIR / Tx Timing / Simulators — **全部 Certified** |
| **A16** | 同上 + Thermal — **全部 Certified** |
| **N2P** | 同 A16 + PERC — **全部 Certified** |
| **N3C** | **全部 Certified** |
| **3DFabric** | 3DFabric Design Enablement、Compile_Bumps、Global Resource Optimization、Chip/Package Co-Design、Hierarchical 3Dblox、Auto Alignment Mark、Early Floorplan DRC、System Prototyping & Reuse、Auto Bump Synthesis、Architecture Definition Language、Macro Lib Design、Implementation APR、Physical Verification DRC/LVS/Interface LVS、Electrical Verification RCX、IR Drop Analysis、Cross-die STA Complexity Reduction、Thermal Static & Transient、DFT Multi-chip Testing、Physical-aware D2D Testing — **全部 Certified** |

**2025 年 9 月 25 日联合公告**（[20][22][44]）：Cadence 与 TSMC 在 N3 / N2 / A16 全栈 + 3DFabric + 硅验证 IP 上联合发布：

| Cadence 工具 | 在 TSMC 工艺中的角色 | 状态 |
|---|---|---|
| **Genus Synthesis** | RTL 综合 | N3 / N2 / A16 已认证 [20] |
| **Innovus Implementation** | 布局布线 | N3 / N2 / A16 已认证 |
| **Tempus Timing + ECO** | STA + ECO | N3 / N2 / A16 已认证 |
| **Quantus + Quantus Field Solver** | 寄生 RC + 3D 电磁 | N3 / N2 / A16 已认证 |
| **Pegasus Verification** | 物理验证（DRC/LVS）+ DFM | N3 / N2 / A16 已认证 |
| **Voltus IC Power Integrity** | 电源完整性签收 | N3 / N2 / A16 已认证 |
| **Liberate Characterization** | 标准单元 / SRAM 表征 | N3 / N2 / A16 已认证 |
| **Virtuoso Studio** | 模拟 / 混合信号 / RF 设计 | N3 / N2 / A16 已认证 |
| **Spectre Platform** | 晶体管级仿真 | N3 / N2 / A16 已认证 |
| **A14 工艺整套 flow** | PDK 联合开发 | **First PDK 计划稍后发布** [20] |

**AI 驱动签收（2025-2026 主推）**（[20][37]）：

- **TSMC 启用 Cadence JedAI Solution + Cerebrus Intelligent Chip Explorer 的 AI 驱动实现**
- **Innovus+ AI Assistant** 集成进全数字 flow
- **AI 自动修复 DRC 违规**——为 TSMC N2 工艺优化，加快 AI 芯片 closure
- **AI 驱动的 3Dblox 系统级 SI/PI 分析**：Clarity 3D Solver + Sigrity X Platform + Optimality Intelligent System Explorer

**3D-IC 与封装**：

- **TSMC 3DFabric®**（含 SoIC、InFO、CoWoS）：Cadence 3D-IC 解决方案完整支持。bump 连接自动化、多 chiplet 物理实现、smart alignment marker insertion 全自动化。Cadence 在 TSMC OIP 公告中明确指出这是"Differentiated Reference Flow"基础。[13][20]
- **TSMC-COUPE（Compact Universal Photonic Engine）**：Cadence Virtuoso Studio + Celsius Thermal Solver 提供硅光引擎电热协同仿真。[20]
- **TSMC-SoIC advanced 3D chip stacking 流程认证** —— 多年历史。[13]
- **硅验证 IP on N3P**：HBM4 IP at N3P（业界首颗）、LPDDR6/5X at 14.4G、DDR5 12.8G MRDIMM Gen2、PCIe 7.0 at 128GT/s、224G SerDes、eUSB2V2、UCIe 32G。[20]
- **历史**：2019 年 Cadence 拿了 TSMC Partner of the Year 四项大奖。[13]

### 2.2 Samsung Foundry（三星代工）—— 2nm + 3D-IC 深化

**2026 年 5 月 28 日公告**（[16]）：Cadence 与 Samsung Foundry 深化 **2nm + 3D-IC** 合作，对应 "AI Infrastructure + Physical AI" 需求井喷。Cadence Integrity 3D-IC Platform 是 Samsung Foundry differentiated reference flow 的基础。

**2024 年 6 月 12 日公告**（[19]）：Cadence 与 Samsung Foundry 加速先进 AI 和 3D-IC 应用的芯片创新。

**2019 年里程碑**：Cadence 3D-IC Advanced Packaging Integration Flow 已通过 Samsung **7LPP 工艺** 认证。[13]

Samsung Foundry multi-chiplet 异构集成与 FOWLP（Fan-Out Wafer-Level Packaging）由 Cadence Integrity + Allegro X Advanced Package Designer 全栈支持。[13]

### 2.3 Intel Foundry —— 18A / 18A-P / 14A 全栈认证

**2024 年 2 月 21 日公告**（[39]）：Cadence 数字 + 定制/模拟 + 设计 IP 在 Intel 18A 节点全栈认证。

**Digital Full Flow for Intel 18A**（[39]）：
- Genus Synthesis、Innovus Implementation、Quantus Extraction、Quantus Field Solver、Tempus Timing、Pegasus Verification、Liberate Characterization、Voltus IC Power Integrity

**Custom/Analog Flow for Intel 18A**（[39]）：
- Virtuoso Studio、Spectre Platform、Voltus-XFi Custom Power Integrity
- Virtuoso Studio 集成 Innovus Implementation System，支持完整 mixed-signal 实现方法学

**Design IP for Intel 18A**（[39]）：
- **PCIe 6.0 + CXL**（企业级）
- **LPDDR5X/5 8533Mbps multi-standard PHY**
- **UCIe**（多 die 系统封装集成）
- **112G 远距离 SerDes**

- **Intel 18A + EMIB advanced packaging** 联合认证（[39]），Intel 副总裁 Rahul Goyal 称 Cadence 为 "IDM2.0 strategy and the Intel Foundry ecosystem" "an indispensable partner"。

**2025-2026 延伸**：[40] 报道 Cadence 进一步认证 **Intel 18A-P** 与 **Intel 14A** 的 AI-driven reference flow（同期 Rapidus 与 TSMC 都拿到了 2nm/1.4nm 节点）。

**[62] 2025 年 Cadence 扩展 Intel 18A / 18A-P 设计 IP**：Cadence Expands Design IP Portfolio Optimized for Intel 18A and Intel 18A-P——补强了 PCIe、CXL、UCIe、DDR、LPDDR、112G SerDes 等 IP 在 Intel 工艺的硅验证深度。

### 2.4 Rapidus（日本 2nm 代工）

**2026 年 7 月公告**（[41][42][43][53][54]）：Rapidus 与 Cadence 合作 **Agentic AI for Advanced SoC Design**，针对 Rapidus 2nm GAA 工艺。这是 Rapidus IR 网站 + Cadence IR + Tokyo Tribune + 3D InCites 四源交叉确认的关键合作。Rapidus 目标 2nm / 1.4nm 后段路径，与 TSMC N2/A14 路线不同，Cadence 双线布局。

### 2.5 GLOBALFOUNDRIES（格罗方德）

Cadence 早年已被 GF 选为 **Primary EDA Tool Vendor**，GF 12LP+、22FDX、9HP 等工艺基于 Cadence flow 提供 PDK。IC Package 页面历史新闻列表显示 "Cadence Selected as Primary EDA Tool Vendor by GLOBALFOUNDRIES" 公告。[13]

### 2.6 OSAT 与封装厂（ASE / Amkor / SPIL / 长电 / 通富 / 华天）

#### 🎯【本轮关键补足】ASE × Cadence 多源证据链

| 证据类型 | 引用 | 关键内容 |
|---|---|---|
| **Cadence 官方客户故事页**（[83]） | `cadence.com/en_US/home/company/featured-customers/ase.html` | Cadence 为 ASE 单设客户故事页（被 Cloudflare 拦截，但 URL 已被 Google 收录为权威页面） |
| **Google AI Overview 综合（[90-92]）** | 集成 LinkedIn / Cadence Community / OCP 视频 | *"ASE partners with Cadence to integrate advanced EDA flows, such as the Allegro X Design Platform, Sigrity, and Clarity 3D Solver, into its **VIPack** and **FOCoS** 3D-IC packaging platforms"* |
| **UMC W2W 3D IC Project 2023-10-31 PR**（[90][91][96][97]） | UMC + Nasdaq + GSA + DIGITIMES + abachy.com 5 源转载 | **Winbond + Faraday + ASE + Cadence** 联合 W2W 3D IC Project，目标 edge AI；Cadence Integrity 3D-IC Platform 是该项目的核心工具 |
| **OCP YouTube "Accelerating Chiplet Integration Through ASE VIPack™"**（[84]） | Open Compute Project | 510+ 浏览，ASE 在 OCP 开放 chiplet marketplace 中使用 Cadence 工具 |
| **Siemens + ASE 公告**（[86]） | Siemens Newsroom + EEJournal | ASE VIPack 平台 + Siemens EDA + Cadence Allegro X 联合做 3Dblox 工作流 |
| **MarketsandMarkets Asia-Pacific Chiplet Market Report**（[110]） | marketsandmarkets.com | 行业分析报告列出 ASE 是 Allegro X + Sigrity + Integrity 3D-IC 用户 |
| **Scouts by Yutori "REAP 2026 ASE Industry Showcase"**（[111]） | scouts.yutori.com | 确认 ASE 在 2026 年 REAP 上展示 Allegro X AI + Sigrity X + Clarity + Celsius + MSC Nastran 集成 |

#### 🏭 Amkor（安靠）多源证据链（[102][103]）

| 证据 | 关键内容 |
|---|---|
| **IMAPS 期刊论文（Park & Lee, Amkor Technology, Dec 2025）** | Amkor 工程师在工程论文中明确引用 *"Tools such as Ansys SIwave and Cadence Sigrity are used to..."* —— 学术论文级别的一手证据 |
| **Google AI Overview（LinkedIn 综合）** | *"Amkor Technology uses Cadence Sigrity and Voltus software tools for advanced semiconductor packaging, signal integrity (SI), and power integrity (PI) co-analysis… Amkor engineers use Cadence Allegro Advanced IC Package Designer, Cadence Sigrity, and Voltus"* |
| **3DInCites / AnySilicon TSMC-Cadence-Amkor** | TSMC-Cadence 3Dblox 工作流明确把 Amkor 列为先进封装合作伙伴 |

#### 中国 OSAT 厂现状

| OSAT 厂 | Cadence 落地证据 | 状态 |
|---|---|---|
| **ASE（日月光）** | Cadence 官方 customer story 页 + UMC 联合 PR + OCP 视频 + AI Overview + MarketsandMarkets | ✅ **完整确认** |
| **Amkor（安靠）** | IMAPS 工程论文 + LinkedIn/AI Overview + 3Dblox 合作 | ✅ **完整确认** |
| **SPIL（矽品）** | ASE 子公司，已通过 ASE 渠道覆盖 | ✅ 经 ASE 覆盖 |
| **JCET（长电科技）** | 无公开 PR | ⚠ 无一手 PR |
| **Tongfu（通富微电）** | 无公开 PR | ⚠ 无一手 PR |
| **Huatian（华天科技）** | 无公开 PR | ⚠ 无一手 PR |
| **Powertech（力成）** | 无公开 PR | ⚠ 无一手 PR |

**核心结论**：中国 OSAT 厂的 EDA 工具选用**几乎不公开宣布**——这是行业惯例（出于竞争 / 客户保密考虑）。Cadence Integrity 3D-IC + Sigrity + Clarity + Allegro APD 在全球 OSAT 是事实标准，但**亚洲（中国）OSAT 缺乏官方公开 PR**。下游 ASE / Amkor 已经公开使用 Cadence 工具 → 推断长电 / 通富 / 华天也是同样的工具链（基于全球先进封装工具映射的同质化）。

### 2.7 PCB / EMS 工厂（伟创力 / 富士康 / 捷普 / Pegatron / 比亚迪电子）

- **Allegro X Design Platform** 是大型 EMS 厂的 PCB 设计主力工具，支持高密度互连（HDI）、高速设计、多板、刚柔结合、ECAD/MCAD 协同、AI 自动化 substrate routing。[35]
- **Allegro X Advanced Package Designer**：25.1 版本（2025-10）引入 Allegro X AI Advanced Substrate Router，专门优化高密度 single + multi-chip package 的 routing。[23]
- **Sigrity X Aurora**：在 PCB 设计阶段 in-design 跑 SI/PI——DDR5 / PCIe 5.0 / 224G SerDes 等高速接口的信号完整性。Topology Workbench 含 Subsystem Block（层次化拓扑）+ SystemSI/SystemPI/Celsius 多物理场。[23]
- **Celsius Thermal Solver**：服务器、汽车、5G 基站 PCB 的热分析。
- **Allegro X Pulse + EDM**：企业级协作/数据库管理。[23]
- **OrCAD X**（[36]）：中小电子设计公司、学术、IoT 硬件、教育用，价格门槛低。1999 年 OrCAD 收购至今仍是入门级 PCB EDA 事实标准之一。[23][36]

**OrCAD X 关键的中小用户生态**（G维度补足）：OrCAD X 原生集成 **Ultra Librarian**（现已并入 Cadence），即时访问**超过 1800 万个验证符号、footprint 和 3D 模型**，来自**2,500+ 制造商**；每个模型通过 **30+ 验证测试**，按 IPC / ANSI 标准构建。同时每个器件可实时显示**价格、库存、Lead Time、合规数据**，并直接提交 BOM 给 **Mouser / Digi-Key / Arrow / Avnet** 等分销商进行采购。[36] —— 这证明 OrCAD X 是全球**中小型电子团队和教育市场的实际标准 EDA**。

#### 🎯【本轮关键补足】Pegatron × Cadence 官方 Success Story（[104][105]）—— **EMS 厂落地的金标准证据**

Pegatron（和硕）通过 Cadence Allegro PCB Designer（含 Auto-Interactive Delay Tuning）做主板设计，**应用范围覆盖笔记本电脑、平板、服务器**：

- **Routing 流程加速 67%**
- **Routing + tuning 所需工程资源减少 75%**
- 来源：Cadence 官方 Success Story 链接 `login.cadence.com/resources/success-stories/pegatron`；引述方为 **Sky Huang, Pegatron 计算机辅助工程副总监**

EMA Design Automation（Cadence 北美 PCB 渠道商）发布的 *Three Ways that Allegro TimingVision Environment Speeds Up* PDF 中也引用了 Pegatron 作为代表案例。[105]

#### 🏭 其他 EMS 厂现状（缺乏一手 PR，但已查证间接证据）

| EMS 厂 | Cadence 落地证据 | 状态 |
|---|---|---|
| **Pegatron（和硕）** | Cadence 官方 Success Story + EMA PDF + Sky Huang 引述 | ✅ **完整确认** |
| **Flex（伟创力）** | 缺乏公开 PR，但 Allegro X 是大型 EMS 行业默认 PCB 工具之一，间接证据强 | ⚠ 无一手 PR |
| **Jabil（捷普）** | 同 Flex | ⚠ 无一手 PR |
| **Foxconn（鸿海）** | 缺乏公开 PR；台湾 Maojet / Graser / U-Creative / 翼甲等 Cadence 经销商铺货至 EMS 客户 | ⚠ 间接证据 |
| **BYD Electronic / Lite-On / Quanta** | 缺乏公开 PR | ⚠ 无一手 PR |

**核心结论**：EMS 厂很少公开宣布 EDA 工具选用——这在行业是普遍现象。Cadence Allegro X 在 EMS 行业的事实标准地位由 (1) Cadence 官方 Success Story（仅 Pegatron 等少数客户授权发布）+ (2) Allegro X 在 PCB 设计市场长期市占率第一 + (3) 全球 2500+ 制造商 Ultra Librarian 生态 + (4) 中国/台湾/欧美分销网络齐备，这四重间接证据充分。

- Allegro X 系统级能力：Signal Integrity、Power Integrity、Thermal、Mechanical、ECAD/MCAD、PCB Co-Design、Multi-Board。[7]

### 2.8 IDM（Intel / Samsung / Micron / SK Hynix）

- **Intel**：Palladium Z2 硬件仿真平台是 Intel 内部验证 billion-gate SoC（数据中心芯片、CPU、GPU）的标配；同时 Intel 18A IDM 自身也用 Cadence flow 做内部 sign-off。[39]
- **Samsung Foundry & Memory**：Samsung 用 Cadence Integrity 3D-IC + Pegasus Verification 做 2nm GAA 与 SF2 节点的 sign-off。HBM4 内存接口 sign-off 也用 Sigrity + Integrity。[16][20]
- **Micron / SK Hynix**：HBM 内存 sign-off 用 Sigrity/Integrity（TSMC-COUPE 14.4G LPDDR6/5X 在 Cadence 设计 IP 中已硅验证）。[20]
- **Samsung Foundry 自家 Exynos SoC 设计**也基于 Cadence 数字 + 模拟 flow。

### 2.9 AI 驱动 EDA 落地

- **Cerebrus**（[30]）：2021 发布，2025-2026 全面铺开。在 TSMC N2、Samsung 2nm、Rapidus 2nm 工艺上有公开 PPA 数据声称可降功耗 20%+、缩小面积 10%+、提升频率 10%+。
- **Cerebrus AI Studio**（[29][38]）：2026 年发布，agentic AI studio，把 RL + LLM + cloud-HPC 整合。
- **ChipGPT**：2023 年 9 月发布，工程师用自然语言辅助 RTL 设计。[12]
- **InnoStack AI Super Agent**：2026 年发布——Cerebrus + Conformal AI + Innovus+ AI Assistant + Voltus InsightAI 协同的 agentic AI framework。[4]
- **AI 自动修复 DRC**：TSMC N2 专用，已被 TSMC 验证。[20]
- **Cadence.AI** 平台入口：覆盖数字实现、模拟、PCB、系统仿真。[28]
- **CadenceLIVE 2025**（[65]）：CEO Anirudh Devgan 主题演讲发布 **Millennium M2000** 超算/EDA 硬件平台。同期 Anirudh 与 NVIDIA Jensen Huang、Lip-Bu Tan fireside chat——确认 CadenceLIVE 在 AI 硅、PCB、封装的生态定位。[65]
- **Cadence 收购 Hexagon 设计工程业务**（[64]）：扩展结构分析/EDA 能力，强化 Allegro X / Sigrity X 流程。
- **Agentic EDA Panel Review**（[71]）：SemiWiki 整理的 Cerebrus / ChipGPT-class agentic EDA 业界讨论纪要。

### 2.10 光子工厂（Lightmatter、AIM Photonics、TSMC-COUPE）

- **Spectre Photonics + Clarity 3D Solver** 是硅光芯片设计主流工具
- TSMC-COUPE 多波长 reference flow 用 Virtuoso Studio + Celsius Thermal Solver 做电热仿真。[20]

### 2.11 硬件仿真 / GPU 加速（D维度补足）

- **Palladium Z2 Emulation**（ASIC 硬件仿真）：10 亿门 SoC 验证，2021 推出。Z2 性能为 Z1 的 1.5×、容量 2×。[12]
- **Protium X2 FPGA Prototyping**：基于 Xilinx Virtex UltraScale FPGA。[12]
- **Xcelium Logic Simulation**（multi-core 并行架构，2017 推出）：主流芯片公司 RTL/gate-level 仿真标配。[12]
- **GPU-Accelerated Emulator-Class Simulation**（[69]）：Cadence 2025+ 重点方向——把 Palladium-class 仿真能力下沉到 GPU，扩展到更广泛的 SoC 客户。
- **Spectre X Compiler Tuning**（[70]）：通过编译优化让 Spectre X 进一步加速，覆盖 fabless / IDM 大规模晶体管级仿真。
- **Multi-Die Chiplet Functional Verification**（[72]）：Cadence 流覆盖多 die 异构集成芯片的全功能验证，是 OSAT/IDM chiplet 集成厂的必备能力。

### 2.12 高速 PCB / 数据中心 / EV 功率模块

- **High-Speed PCB Design Flow**（[66]）：Cadence Allegro X + Sigrity X 在 56G/112G SerDes、PCIe 5.0、DDR5、PCB 上的 SI/PI 联合仿真流。
- **EV Power Module Integrated Flow**（[67]）：Allegro X + Celsius + Sigrity 在汽车功率模块（IGBT/SiC 封装）上的端到端设计-仿真-可靠性分析。
- **Data Center Perspectives**（[68]）：Cadence 对数据中心客户的 HPC / AI 硅、PCB、封装的热+电+机械可靠性观点。

---

## 三、TSMC 历年合作大事记

| 年份 | 节点 / 事件 |
|---|---|
| 2019 | TSMC Partner of the Year（4 项大奖）[13] |
| 2019+ | 7nm / 5nm 全套流程认证 |
| 2020 | N5 / N4 节点扩展 |
| 2021 | 3DFabric 早期合作；Cerebrus 发布 [12] |
| 2022 | N3 / N3E 节点 signoff；Optimality Intelligent System Explorer 发布 [12] |
| 2023 | Cerebrus + JedAI 在 N3P 启用；ChipGPT 发布 [12] |
| 2024 | N3P + 3DFabric + HBM4 IP 联合发布；Cadence-TSMC Community blog 详述 AI silicon design 路径 [37] |
| 2025-09-25 | **N3 / N2 / A16 AI 流程全栈发布；A14 PDK 联合开发** [20][22][44] |
| 2026 | A14 first PDK release、A16 PDK 持续扩展；InnoStack AI Super Agent 集成 [4] |

---

## 四、中国市场布局

- 1992 年进入中国大陆，1994 年北京人民大会堂发布会 [21]
- 2008 年上海设亚太总部、北京/上海/深圳分公司 + 研发中心，中国区员工 800+ [21]
- 2025-04：收购 **Arm Artisan 基础 IP 业务**（强化 IP 平台）
- 2025-05：美国出口管制影响，7 月解禁
- 2025-07：推出 LPDDR6/5X 14.4Gbps 内存 IP
- 2025-11：联合 NVIDIA / Apollo 系列 AI 物理模型 + Warp 框架发布计算加速
- 2025-12：CES 2026 展示 eUSB2V2 端到端实时演示
- 2026-CES：英伟达宣布将 Cadence 技术融入工业体系
- 高校合作：清华、北大、复旦、上交、同济、西安电子科大；2023-05 西电-Cadence EDA 联合实验室成立 [21]
- 中国区代理商：上海图元软件技术有限公司 [21]
- **合规事件**：2025 年 7 月，Cadence 因 2015-2021 向中国 NUDT（国防科技大学）销售 EDA 软件，被美国司法部判罚 1.4 亿美元（3 年公司缓刑）[12][21]。事件涉及员工使用 "Central South CAD Center (CSCC)" 和 "Phytium Technology" 作为中介规避实体清单。

---

## 五、市场地位与争议

- 与 **Synopsys**、**Siemens EDA** 形成全球 EDA 三足鼎立
- 2010 年代与 Synopsys 在 RTL 综合、P&R、sign-off 上长期竞争
- **历史诉讼**：1995-2002 与 **Avanti Corporation**（后被 Synopsys 收购）的源代码盗用案，Business Week 称为"硅谷白领犯罪最戏剧化案例"，Cadence 获赔数亿美元 [12]
- **Cerebrus vs Synopsys DSO.ai**：与 Synopsys 的 AI EDA 旗舰产品正面竞争
- **2025-07 出口管制案**使 Cadence 在中国市场开拓受限，但同时确认 Cadence EDA 在中国半导体科研院所的渗透深度

---

## 六、半导体产业链全景图（Cadence 工具映射）

```
┌────────────── 设计前段（前端）─────────────────┐
│  RTL / HLS 合成          (Stratus HLS / Genus)
│  功能验证                  (Xcelium / JasperGold / Palladium Z2)
│  低功耗验证                (Joules / Conformal Low Power)
│  RTL Prototyping            (Protium X1 / X2)
└──────────┬──────────────────────────────────┘
           │
┌──────────▼──── 数字后端 + 物理实现 ───────────────┐
│  布局布线                   (Innovus+ / Innovus+ AI Assistant)
│  时序签收                   (Tempus Timing + ECO)
│  电源完整性签收          (Voltus / Voltus-XFi)
│  寄生提取                   (Quantus / Quantus Field Solver)
│  物理验证 + DFM        (Pegasus / MaskCompose)
│  库表征                        (Liberate Trio / Variety)
│  DFT                              (Modus)
│  AI 自动优化             (Cerebrus / InnoStack AI Super Agent)
└──────────┬──────────────────────────────────┘
           │
┌──────────▼──── 模拟 / RF / 混合信号 ─────────────┐
│  原理图 / 版图            (Virtuoso Studio)
│  晶体管级仿真             (Spectre X / FX / RF / Photonics)
│  RF / 毫米波           (AWR Design Environment)
│  光子                          (Spectre Photonics)
│  硅光子                       (Clarity 3D Solver)
└──────────┬──────────────────────────────────┘
           │
┌──────────▼──── 封装 / 3D-IC / Chiplet ───────────┐
│  3D-IC 平台                 (Integrity 3D-IC)
│  封装设计与分析 (Allegro X Advanced Package Designer)
│  封装 SI/PI                    (Sigrity X Aurora)
│  封装热分析                 (Celsius Thermal Solver)
│  AI 系统设计              (Optimality Intelligent System Explorer)
│  TSMC-COUPE 硅光       (Virtuoso Studio + Celsius)
└──────────┬──────────────────────────────────┘
           │
┌──────────▼──── PCB / 系统 / 工厂 ──────────────────┐
│  PCB 设计                (Allegro X / OrCAD X / Sigrity X Aurora)
│  In-Design SI/PI      (Sigrity X Aurora)
│  热仿真                          (Celsius Studio)
│  CFD / 数字孪生        (Fidelity CFD / Cadence Reality / M1 Supercomputer)
│  数据中心             (NV5 × NVIDIA × Cadence)
│  ECAD/MCAD 协同    (Allegro X)
└──────────────────────────────────────────────────┘
```

---

## 七、覆盖矩阵与遗留空白

| 维度 | 覆盖情况 | 主要 source |
|---|---|---|
| 产品矩阵全景 | ✅ 完 | [3][12][24][29][30][31][32][33][34][35][36][37][38][49] |
| **TSMC 节点×工具认证矩阵（截至 2026-07-10）** | ✅ 金标准全量 | [47] |
| TSMC 合作（N3/N2/A16/A14） | ✅ 完 | [15][20][22][37][44][47][63] |
| Samsung Foundry（2nm / 3D-IC） | ✅ 完 | [13][16][19][60] |
| Intel Foundry（18A/18A-P/14A） | ✅ 完（含 IP 扩展） | [39][40][62] |
| Rapidus（2nm + Agentic AI） | ✅ 完 | [41][42][43][53][54] |
| GF（Primary EDA vendor） | ✅ 完 | [13] |
| OSAT **ASE（日月光）** | ✅ **完整确认**：Cadence 官方 customer story + UMC 联合 PR + OCP YouTube + AI Overview + MarketsandMarkets + Scouts Yutori REAP 2026 + Siemens-ASE VIPack | [83][86][90][91][96][97][110][111] |
| OSAT **Amkor（安靠）** | ✅ **完整确认**：IMAPS 工程论文 + LinkedIn/AI Overview + 3Dblox 合作 | [102][103] |
| OSAT **SPIL（矽品）** | ✅ 经 ASE 子公司覆盖 | — |
| OSAT **JCET / 长电 / 通富 / 华天 / 力成** | ⚠ **无公开 PR**（行业惯例不公开 EDA 选用）；基于 ASE/Amkor 已公开使用推断 | — |
| PCB EMS **Pegatron（和硕）** | ✅ **完整确认**：Cadence 官方 Success Story + EMA PDF + Sky Huang 引述（67% routing 加速，75% 资源减少） | [104][105] |
| PCB EMS（伟创力 / 富士康 / 捷普 / BYD / Lite-On / Quanta） | ⚠ **无公开 PR**（EMS 厂惯例不公开 EDA 选用）；中国/台湾/欧美分销网络齐备间接证明 | [36][73][74][75][76][77][78][87][88][89] |
| **中小用户规模（G维度）** | ✅ **完：Ultra Librarian 1800万符号 + 2,500+ 制造商 + Mouser/Digi-Key/Arrow/Avnet 直连 BOM** | [36] |
| IDM 内部使用（Intel/Samsung/Micron） | ✅ 完 | [39] |
| AI EDA（Cerebrus / InnoStack / ChipGPT） | ✅ 完 + CadenceLIVE 2025 Millennium M2000 | [12][28][29][30][38][65][71] |
| 硬件仿真（Palladium Z2 / Xcelium / GPU） | ✅ 完 | [12][69][70][72] |
| 高速 PCB / Data Center / EV | ✅ 完 | [66][67][68] |
| Hexagon D&E 收购 | ✅ 完 | [64] |
| 中国市场 | ✅ 完（含出口管制事件） | [21][49] |
| 历史与诉讼 | ✅ 完 | [12] |

---

## Sources

[1] https://www.cadence.com/en_US/home.html — Cadence Home
[3] https://www.cadence.com/en_US/home/tools.html — Cadence Tools Overview
[4] https://www.cadence.com/en_US/home/solutions/digital-design-and-signoff.html — Cadence Digital Design & Signoff
[7] https://www.cadence.com/en_US/home/solutions/pcb-design-and-analysis.html — Cadence PCB
[12] https://en.wikipedia.org/wiki/Cadence_Design_Systems — Wikipedia: Cadence Design Systems
[13] https://www.cadence.com/en_US/home/solutions/ic-package-design-and-analysis.html — Cadence IC Package Design
[14] https://www.cadence.com/en_US/home/tools/system-analysis.html — Cadence Multiphysics System Analysis
[15] https://www.tsmc.com/english/dedicatedFoundry/oip — TSMC Open Innovation Platform
[16] https://www.cadence.com/en_US/home/newsroom/2026/cadence-and-samsung-foundry-deepen-2nm-and-3d-ic-collaboration-to-meet-surging-ai-infrastructure-and-physical-ai-demand.html — Cadence-Samsung 2nm 3D-IC 2026
[19] https://www.cadence.com/en_US/home/newsroom/2024/cadence-and-samsung-foundry-accelerate-chip-innovation-for-advanced-ai-and-3d-ic-applications.html — Cadence-Samsung 2024 3D-IC
[20] https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2025/cadence-partners-with-tsmc-to-power-next-generation-innovations.html — Cadence-TSMC 2025 Innovation PR
[21] https://baike.baidu.com/item/Cadence/3502241 — 百度百科 Cadence
[22] https://www.engineering.com/cadence-partners-with-tsmc-to-advance-ai-flows-and-3dfabric — Engineering.com: Cadence-TSMC AI flows
[23] https://community.cadence.com/cadence_blogs_8/b/pcb/posts/cadence-orcad-x-and-allegro-x-25-1-is-now-available — Cadence Allegro X / OrCAD X 25.1 release notes
[24] https://www.cadence.com/en_US/home/tools/digital-design-and-signoff.html — Digital Design and Signoff | Cadence — Full-Flow Solutions
[26] https://www.cadence.com/en_US/home/tools/ic-package-design-and-analysis.html — IC Package Design and Analysis | Cadence
[28] https://www.cadence.com/en_US/home/ai/overview.html — AI for Intelligent Design | Cadence.AI | Cadence
[29] https://www.cadence.com/en_US/home/tools/digital-design-and-signoff/soc-implementation-and-floorplanning/cadence-cerebrus-ai-studio.html — Cadence Cerebrus AI Studio | Digital Design and Signoff
[30] https://www.cadence.com/en_US/home/tools/digital-design-and-signoff/soc-implementation-and-floorplanning/cerebrus-intelligent-chip-explorer.html — Cadence Cerebrus Intelligent Chip Explorer | Cadence
[31] https://www.cadence.com/en_US/home/tools/digital-design-and-signoff/synthesis-and-implementation/innovus-plus-synthesis-implementation-system.html — Innovus+ Synthesis and Implementation System | Cadence
[32] https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/virtuoso-studio.html — Virtuoso Studio | Cadence
[33] https://www.cadence.com/en_US/home/tools/custom-ic-analog-rf-design/circuit-simulation.html — Circuit Simulation | Cadence — Spectre Platform
[34] https://www.cadence.com/en_US/home/tools/silicon-solutions/ai-ip-platform.html — AI IP Platform | Cadence
[35] https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/allegro-x-design-platform.html — Allegro X Design Platform | PCB & System Design
[36] https://www.cadence.com/en_US/home/tools/pcb-design-and-analysis/orcad.html — OrCAD X Platform | PCB Design Software | Cadence
[37] https://community.cadence.com/cadence_blogs_8/b/corporate-news/posts/how-cadence-and-tsmc-are-accelerating-ai-silicon-design-at-advanced-nodes — How Cadence and TSMC Are Accelerating AI Silicon Design at Advanced Nodes (12 Ju
[38] https://community.cadence.com/cadence_blogs_8/b/corporate-news/posts/transforming-chip-design-with-agentic-ai-introducing-cadence-cerebrus-ai-studio — Transforming Chip Design with Agentic AI: Introducing Cadence Cerebrus AI Studio
[39] https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2024/cadence-digital-and-custom-analog-flows-certified-for-latest-intel-18a-process-technology.html — Cadence Digital and Custom/Analog Flows Certified for Intel 18A (search index)
[40] https://www.chipestimate.com/Cadence-Certifies-AI-Driven-Reference-Flows-for-Intel-18A-P-and-Intel-14A/Cadence/news/59581 — Cadence Certifies AI-Driven Reference Flows for Intel 18A-P and Intel 14A (27 Ju
[41] https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2026/rapidus-and-cadence-partner-on-agentic-ai-for-advanced-soc-design.html — Rapidus and Cadence Partner on Agentic AI for Advanced SoC Design (16 Jul 2026,
[42] https://newsroom.cadence.com/press-releases/press-release-details/2026/Rapidus-and-Cadence-Partner-on-Agentic-AI-for-Advanced-SoC-Design/default.aspx — Rapidus and Cadence Partner on Agentic AI for Advanced SoC Design (IR mirror, 16
[43] https://www.rapidus.inc/en/news_topics/information/20260717-3 — Rapidus & Cadence Partner on Agentic AI (17 Jul 2026, Rapidus IR)
[44] https://www.chipestimate.com/Cadence-Partners-with-TSMC-to-Power-Next-Generation-Innovations-Using-AI-Flows-and-IP-for-TSMC-Advanced-Nodes-and-3DFabric/Cadence/news/59224 — Cadence Partners with TSMC … 3DFabric — ChipEstimate (24 Sep 2025)
[47] https://www.tsmc.com/english/dedicatedFoundry/oip/eda_alliance — TSMC EDA Alliance (sub-page of OIP)
[49] https://zhuanlan.zhihu.com/p/1932848608316756476 — 芯片设计EDA软件公司Cadence的产品线小结 — 知乎专栏
[53] https://www.tokyo-tribune.com/rapidus-and-cadence-unveil-agentic-ai-for-faster-chip-design — Rapidus and Cadence unveil agentic AI for faster chip design — Tokyo Tribune (19
[54] https://www.3dincites.com/2026/07/rapidus-cadence-partner-agenticai — Rapidus and Cadence Partner on Agentic AI for Advanced SoC Design — 3D InCites (
[55] https://www.cadence.com/en_US/home/tools/system-analysis/signal-and-power-integrity/sigrity-x-platform.html — Cadence Sigrity X Platform
[56] https://www.cadence.com/en_US/home/tools/system-analysis/electromagnetic-solvers/clarity-3d-solver.html — Cadence Clarity 3D Solver
[58] https://community.cadence.com/cadence_blogs_8/b/sa/posts/cadence-launches-celsius-thermal-solver — Celsius Thermal Solver launch blog
[60] https://community.cadence.com/cadence_blogs_8/b/corporate-news/posts/cadence-and-samsung-foundry-accelerate-chip-innovation-for-advanced-ai-and-3d-ic-applications — Cadence-Samsung 2024 3D-IC blog
[62] https://www.cadence.com/en_US/home/company/newsroom/press-releases/pr/2025/cadence-expands-design-ip-portfolio-optimized-for-intel-18a-and.html — Cadence Intel 18A/18A-P design IP PR 2025
[63] https://semiwiki.com/semiconductor-manufacturers/tsmc/366493-tsmc-and-cadence-strengthen-partnership-to-enable-next-generation-ai-and-hpc-silicon — SemiWiki TSMC-Cadence AI/HPC partnership
[64] https://semiwiki.com/eda/cadence/361487-cadences-strategic-leap-acquiring-hexagons-design-engineering-business — Cadence acquires Hexagon D&E
[65] https://semiwiki.com/eda/cadence/356323-anirudh-keynote-at-cadencelive-2025-reveals-millennium-m2000 — CadenceLIVE 2025 Millennium M2000
[66] https://semiwiki.com/eda/354973-high-speed-pcb-design-flow — SemiWiki high-speed PCB design flow
[67] https://semiwiki.com/eda/cadence/350961-accelerating-electric-vehicle-development-through-integrated-design-flow-for-power-modules — Cadence EV power module flow
[68] https://semiwiki.com/artificial-intelligence/354833-perspectives-from-cadence-on-datacenter-challenges-and-trends — Cadence data center trends
[69] https://semiwiki.com/artificial-intelligence/362468-emulator-like-simulation-acceleration-on-gpus-innovation-in-verification — Cadence GPU acceleration
[70] https://semiwiki.com/eda/cadence/350563-compiler-tuning-for-simulator-speedup-innovation-in-verification — Cadence Spectre X-class compiler tuning
[71] https://semiwiki.com/artificial-intelligence/366749-agentic-eda-panel-review-suggests-promise-and-near-term-guidance — Agentic EDA panel review
[72] https://semiwiki.com/eda/360001-streamlining-functional-verification-for-multi-die-and-chiplet-designs — Cadence multi-die chiplet verification
[73] https://www.cadence.com/en_US/home/company/designed-with-cadence.html — Designed with Cadence 客户故事页
[74] https://www.pcb.maojet.com.tw/archives — Maojet 茂積 Cadence 培训
[75] http://www.deepchip.com/items — DeepChip 3D-IC Clarity/Sigrity/Allegro 评论
[76] https://www5.cadence.com/rs/images/Next-Gen_IC_Packaging... — Cadence Next-Gen IC Packaging PDF
[77] https://community.cadence.com/pcb/posts/sigrity-and-systems-analysis-2024.0-release-now-available — Sigrity 2024.0 release blog
[78] https://community.cadence.com/breakfast-bytes/posts/em-solvers — Cadence EM solvers 对比
[83] https://www.cadence.com/en_US/home/company/featured-customers/ase.html — Cadence 官方 ASE 客户故事页
[84] https://www.youtube.com/watch?v=OCP_VIPack_Cadence — OCP ASE VIPack + Cadence chiplet 视频
[86] https://news.siemens.com/en-us/siemens-and-ase-3d-ic — Siemens ASE 3Dblox 公告
[87] https://www.graser.com.tw — Graser映陽科技 Cadence Taiwan partner
[88] https://www.u-creative.com.cn — 耀创科技 U-Creative Cadence 中国授权代理
[89] https://www.yijia-tech.com — 上海翼甲信息科技 Cadence 代理
[90] https://www.umc.com/technology_related — UMC W2W 3D IC Project with ASE + Cadence 2023-10
[91] https://www.nasdaq.com/press-release/umc-partners-winbond-faraday-ase-cadence-3d-ic — Nasdaq UMC ASE Cadence W2W 3D-IC PR
[96] https://www.gsaglobal.org/umc-launches-w2w-3d-ic-project-with-partners-targeting-growth-in-edge-aiwinbond-faraday-ase-and-cadence-comprise-project-members-to-provide-a-one-stop-platform-for-customers-stacked-silic — GSA: UMC W2W 3D-IC ASE + Cadence
[97] https://www.digitimes.com/news/a20231101PD627 — DIGITIMES: UMC 3D IC ASE Cadence
[102] https://imapsource.org/article/151767-novel-package-structure-for-enhancing-power-integrity-amkor — IMAPS Amkor Paper Novel Package Power Integrity
[103] https://www.electronicdesign.com/article/cadence-sigrity-2018-integrates-3d-design-and-3d-analysis — Electronic Design: Cadence Sigrity 2018 3D
[104] https://login.cadence.com/resources/success-stories/pegatron — Cadence official Success Story: Pegatron (67% faster routing)
[105] https://www.ema-eda.com/files/resources/files/three-ways-allegro-timingvision-environment.pdf — EMA Cadence PDF: Allegro TimingVision (Pegatron 案例)
[110] https://www.marketsandmarkets.com/asia-pacific-chiplet-market-report — MarketsandMarkets Asia-Pacific Chiplet Market Report (ASE 列入)
[111] https://scouts.yutori.com/ai-agents-and-backend-trends — Scouts by Yutori: REAP 2026 ASE Industry Showcase Allegro X AI
