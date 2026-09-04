# 美国汽车智能驾驶市场深度调研（2024–2026）

**报告周期**：2024-Q1 – 2026-Q2（重点 2025-Q4 – 2026-Q2）
**数据截止**：2026-08-13
**地理边界**：美国市场为主，必要对照中国市场

---

## 一句话结论（TL;DR）

美国 2024–2026 的智能驾驶市场呈现"L2 高度渗透、L3 名存实亡、L4 Robotaxi 一超多强"的断层格局：Waymo 以 500,000 单/周（3,067 辆车队、10 城市、220M 全自动英里）坐稳头部；Tesla 6/22/2025 启动奥斯汀 Robotaxi，但全奥斯汀仅部署 ~20 辆且 17 起 NHTSA 事故；Cruise 经 2024-Q4 GM 撤资、2025-02 不重启、2026-05 才在休斯顿重启监督测试；Mercedes 主动暂停 Drive Pilot L3；芯片端 Mobileye 2025 累计 230M 装车 + Q1 2026 营收 $558M（+27% YoY），NVIDIA Drive Orin/Thor 占高端 AI 计算 25-35% 份额；NHTSA 在 2026-03-18 将 Tesla FSD 320 万辆调查升至"工程分析"（EA26002），距离强制召回仅一步之遥。[7][33][48][70][17]

---

## 1. 美国市场分层：L2 / L2+ / L3 / L4 的真实落地差异

美国市场的"智驾"是个被滥用的词——SAE J3016 划分下的 L2、L2+、L3、L4 在监管责任、定价、运营模式上完全是不同的生意，但产业传播上常被一锅炖。下表是 2026-Q2 当前最权威的分层现实：

```
                  美国市场智驾分层（金字塔 2026-Q2 实际落地版）
                  ============================================
                       L4 Robotaxi  ←  真正无人，单车可独立计费
                     ─┬────────────┬─
                  L3  │            │  SAE 标准"条件性自动驾驶"
                高速  │            │  仅 Mercedes Drive Pilot 1 处
                拥堵  │            │  在加州/内华达保留，2026 暂停新车型
              ─┬──────┴────────────┴──────┬─
            L2+ │                          │  高速 NOA / 城市 NOA
          高速  │                          │  BlueCruise 97% 美高速覆盖
          NOA   │                          │  Super Cruise 75 万英里
               ─┤                          │  FSD Supervised 320 万辆
            L2  │                          │  Toyota Safety Sense / Honda
          ACC + │                          │  Sensing / Hyundai HDA 等
          LKA   │                          │  100% 渗透新车
```

**关键差异**：

| 维度 | L2 (基础) | L2+ (NOA) | L3 (有条件) | L4 (Robotaxi) |
|---|---|---|---|---|
| **2026 代表玩家** | Toyota Safety Sense 3.0 标配 [12] | Ford BlueCruise、GM Super Cruise、Tesla FSD (Supervised) | Mercedes Drive Pilot (S/EQS，2026 暂停新车型) [37] | Waymo、Zoox、Tesla Robotaxi、Cruise (重测) |
| **单车定价/年费** | 0（新车标配） | BlueCruise $495-$995/年 [35]；Super Cruise 3 年免费 [49]；FSD $8,000 一次性或 $99/月 | Drive Pilot $5,000-$10,000 一次性（奔驰 S/EQS 仅高速拥堵 <40mph） [37] | 会员价 $0.30-$0.70/英里（Waymo 早期数据） [3] |
| **运营责任** | 驾驶员全责 | 驾驶员须监控 | 系统在 ODD 内负责 | 系统全责（需 SAEL4 认证） |
| **市场规模** | 100% 新车 | 数百万存量 | < 5,000 辆 | Waymo 3,067 辆全国 [7] |
| **关键监管** | FMVSS 豁免 | FMVSS 豁免 | 各州 L3 立法 | NHTSA SGO 2021-01 + 州/地方法规 |
| **2026-Q2 真实状态** | 完全渗透 | 数百万用户，跑通商业模式 | **名存实亡**——Mercedes 主动退守 | Waymo 一超，Tesla/Cruise 极小规模 |

注：SAE J3016 定义 L0-L5 共 6 级，但产业实践中 L3 几乎无人生产，L2+ 是 2024-2026 的最大增量市场。

---

## 2. Tesla FSD 进展与 Robotaxi 真实数据

### 2.1 软件版本时间线

- **FSD v13（Supervised）**：2024-Q4 发布；硬件 HW4 上 5 倍参数、5 倍算力 [42]
- **FSD v14 (v14.3.5 / v14.3.6)**：2025-07 至 2025-08 推送，HW3 / HW4 双平台；含"端到端高速"功能 [42]
- **FSD v15（计划中）**：Musk 在 Q1 2026 财报电话会明确，"驾驶模型"将从 ~10 亿参数扩到 ~100 亿参数，定位为 v13 以来"最大架构改写"，目标窗口为 **2026 年末 - 2027 年初**[7]；Musk 同时承认"知道有重大架构改进要上时，部署大规模无人监督 FSD 不合理"——这与 Robotaxi 大规模扩张直接挂钩。

### 2.2 Robotaxi 启动与扩区

- **2025-06-22**：Tesla 在奥斯汀启动无人监督 Robotaxi 服务（最初邀请制），每单固定 $4.20，前排配 Tesla 员工监督 [8][9][10]
- **2026-Q2 全奥斯汀覆盖**：2026-06-03 扩至整个奥斯汀都市圈（含机场），约 245 平方英里 [7]，车型仍为 Model Y（非 Cybercab）
- **2026-04 跨城市扩张**：进入达拉斯、休斯顿，"Texas 成为全美第一个具多城市无监督 Robotaxi 部署的州" [7]
- **2026-06-22 一周年**：奥斯汀业务满 1 年，但实际运营规模与 Musk 早期"千辆级"承诺差距巨大 [7]

### 2.3 真实车队规模（被低估的核心数据）

Tesla 在 2025-06 启动后车队增长曲线平缓甚至下行，与 Waymo 形成指数级对比：

| 指标 | Tesla Robotaxi (2026-Q2) | Waymo (2025-12 报备，2026 持续) |
|---|---|---|
| **德州全州授权车辆** | **42 辆**（May 2026 州数据库） [7] | **577 辆** [7] |
| **奥斯汀活跃无监督车辆** | **~20 辆**（Robotaxi Tracker，2026-06），从 4 月 ~25 辆峰值回落 [7] | Waymo 在奥斯汀通过 Uber App 提供服务 |
| **每周付费单量** | 未披露，"low thousands" 估算 [7] | **500,000+ 单/周**（Waymo 2025-12 报备 250k paid trips weekly，2026-Q2 已翻倍） [7][47] |
| **NHTSA 备案事故** | 17 起（2025-07 至 2026-04），其中 2 起轻伤、1 起需住院 [7] | 464+ 起（2025 累计上报） [57]，但 17 起 在 NHTSA 关闭调查中无系统性违规 [53] |
| **车队平台** | Model Y（同家用车型） | Geely-极氪 / Jaguar I-PACE / Hyundai IONIQ 5（专用平台） [5] |

### 2.4 关键技术疑点（Reuters 2026-05-28 调查）

Reuters 基于 9 位前 Tesla 数据标注员、1 位前自动驾驶工程师、11 位交通安全研究员的访谈，发现 [7][11]：

- 奥斯汀启动前，Tesla 员工从晚 6 点至凌晨测试 Robotaxi 原型车；数据标注员花数百小时标注沿线路缘与路面标记
- Tesla 将 FSD airbag-deployment 撞车数据与"全国撞车平均（含未弹出气囊）"对比，安全优势被夸大约 **3 倍**；11 位交通安全研究员中 10 位称该统计"具误导性"
- 9 位前标注员中 7 位表示"不会信任 FSD 载他们自己"

**结论**：Tesla 的"无地图路线泛化"主张与 Reuters 调查的"路线专属准备"现实存在结构性张力；这构成了 v15 rewrite 前的最大叙事风险。

---

## 3. Waymo 真实运营数据（Alphabet 子公司）

### 3.1 车队与运营规模

- **车队规模（2025-12 上报）**：**3,067 辆** robotaxi 在全美运行第五代 Driver [7]
- **周单量**：从 2024-Q1 ~25,000 单/周 → 2025-Q4 ~250,000 单/周 [7] → 2026-Q2 **>500,000 单/周**（Tech Times 报道 Waymo 上报 NHTSA 数据） [7][46]
- **年度累计（2025 全年）**：超过 **15M 付费行程**；累计 **20M+** 终生付费行程 [46]
- **全自动英里累计**：截至 2026-03 末**220M 全自动英里**（折合"超过 250 个人类寿命的驾驶时间"） [1][2]

### 3.2 覆盖城市（2026-Q2，10 城+）

| 城市 | 启动年份 | 2026 状态 | 来源 |
|---|---|---|---|
| Phoenix（凤凰城） | 2020 (Rider Only) | 公开运营，机场待开通 | [1] |
| San Francisco（旧金山） | 2022-06 / 2024-06 公开 | Bay Area 服务区已统一 | [1][2] |
| Los Angeles（洛杉矶） | 2024 | 公开运营 | [1] |
| Austin（奥斯汀） | 2025-03 | Tesla Robotaxi 主要竞争城市 | [7] |
| Atlanta（亚特兰大） | 2025-06 | 5.4M 自治英里，机场服务 | [1] |
| Miami / Miami Beach | 2026 | Waymo + Uber 双 App | [3] |
| Nashville（纳什维尔） | 2026-04 / 2026-06-25 全开放 [4] | 累计数万人体验 | [4] |
| Dallas（达拉斯） | 2026-08-04 全开放（从 2025-12 起先内部开放） | 累计近 150,000 riders | [3] |
| Denver（丹佛） | 2026-Q3 起公开 | 内测开放 | [5] |
| Las Vegas（拉斯维加斯） | 2026-Q3 起公开 | 内测开放 | [5] |
| San Diego（圣地亚哥） | 2026-Q3 起公开 | 内测开放 | [5] |
| Tampa（坦帕） | 2026-Q3 起公开 | 内测开放 | [5] |
| **Portland（波特兰）** | 2026-04-28 宣布 [6] | 2026 年内启动 | [6] |

### 3.3 安全数据（截至 2026-03 末）

Waymo 自家最新分析 [1][2]：

| 指标 | Waymo vs 人类驾驶员 | 折减事故数 |
|---|---|---|
| 严重伤亡或更糟碰撞 | **-94%** | 累计少 47 起 |
| 气囊弹出碰撞 | **-82%** | 累计少 305 起 |
| 任何伤害碰撞 | **-82%** | 累计少 707 起 |
| 行人受伤碰撞 | **-93%** | 累计少 76 起 |
| 骑自行车人受伤碰撞 | **-84%** | 累计少 48 起 |
| 摩托车手受伤碰撞 | **-84%** | 累计少 32 起 |

**当前运行速率**：每周 4M+ 英里 [1]——按 Waymo 估算，每 8 天少 1 起严重伤亡，每周少 6 起气囊碰撞、13 起任何伤害。

### 3.4 定价与监管关键事件

- **NHTSA 调查（2024-05 启动，2025-07-29 结案）**：调查 14 个月，审查 22 起涉及 440 辆 Waymo 车的事件，其中 17 起为碰撞；**结论：未发现系统性安全违规** [53]
- **NHTSA 调查二（2025-10 启动）**：聚焦 Waymo 在停靠校车附近"违反保护行人交通规则"；**2025-12 触发软件召回** [59]
- **首起致死事件**：2025 年内 Waymo Robotaxi 发生首起致死碰撞（详见后文）
- **纽约测试许可**：2026-03-31 到期，**Waymo 测试车在 NYC 不允许继续测试** [7 引用图说]
- **第六代 Waymo Driver**：搭载 **Hyundai IONIQ 5** 平台，2026-Q3 起在多个新城市内测 [5]

---

## 4. Cruise（GM 旗下）：从 2024 危机到 2026 重组

### 4.1 时间线（关键节点）

| 日期 | 事件 | 来源 |
|---|---|---|
| 2023-10-02 | 旧金山行人拖拽事故：Cruise 车辆将已被撞行人拖行约 20 英尺（7mph），行人重伤 | [12] |
| 2023-10-24 | 加州 DMV 吊销 Cruise 运营许可（指控隐瞒视频片段） | [12] |
| 2023-11 | CEO Kyle Vogt 辞职；公司裁员 ~25% | [12] |
| 2023-12 | NHTSA 启动正式调查；全美所有运营暂停 | [12][16] |
| 2024-01 | SEC 与 DOJ 启动调查 | [12] |
| 2024-04 | 凤凰城恢复人工数据采集（人类驾驶员手动） | [12] |
| 2024-05 | 凤凰城开始有监督自动驾驶测试 | [12] |
| 2024-06-11 | GM 宣布向 Cruise 再注资 **$850M** [15] | [15] |
| 2024-12-10 | **GM 宣布退出 Robotaxi 业务，停止为 Cruise 独立融资** [14] | [14] |
| 2025-02-06 | **Cruise 正式确认不会重启 Robotaxi 服务** [13] | [13] |
| 2025-02 | GM 再裁员 ~50%（约 1,000 人），CEO Marc Whitten（任期仅数月）离任 | [12] |
| 2026-04 | **凤凰城重启监督测试** [16] | [16] |
| 2026-05-31 | **休斯顿重启监督测试**：10 辆改装 Chevrolet Bolts 开始街道制图 [16] | [16] |
| 2026-05 | Houston 议会 6-5 投票通过 Cruise 测试许可（限 10am-4pm 晴好天气） | [16] |
| 2026-08（计划） | 凤凰城 + 休斯顿试点扩至 20 辆，休斯顿目标 9 月起载客 | [16] |

### 4.2 财务亏损与人员代价

- **2025 现金燃烧**：约 **$2.7B** [16]
- **GM 自 2016 累计投入 Cruise**：$10B+ [16]
- **裁员总数**：2023-12 ~24% + 2025-02 ~50%（剩余 1,000 人）[12]

### 4.3 NHTSA 调查当前状态

- **2023-12 启动的调查仍开放**——NHTSA 要求 Cruise 证明车辆能在低光照条件下检测并避开行人（即旧金山事故失败模式），Cruise 需每月向 NHTSA 提交报告 [16]

---

## 5. Aurora、Zoox 与第二梯队 Robotaxi

### 5.1 Aurora Innovation（AUR）：卡车先行 + 出租车双线

- **2025-05-01**：Aurora 在德州正式启动**商业 Class 8 无人卡车**运营，Dallas–Houston 双向定期 [24]
- **2025-08-07**：发布第二代 driverless trucks [27]
- **2025-10-28**：扩展至 Fort Worth – El Paso 第二条无人卡车路线 [25]
- **2026-Q1**：规划 Sun Belt 进一步扩张 [26]
- **2025 实际营收**：**$3M**（vs 2024 基本为 0）[26]
- **出租车业务**：Aurora Driver 同时供应乘用车 OEM，但未启动乘用车 Robotaxi 商业运营 [27]

### 5.2 Zoox（Amazon）：从原型到 8/10/2026 收费

- **2025**：在 Las Vegas Strip 启动免费公众乘坐 [48]
- **2026-04**：宣布扩至 San Francisco、Miami、Austin、Florida [48]
- **截至 2026-05**：累计 ~2M 全自动英里、**350,000+ 乘客**（免费） [48]
- **2026-08-05**：宣布**首条付费 Robotaxi 服务**——Las Vegas Strip，8/10 启动 [43][44][45]
- **NHTSA 商业豁免**：Zoox 是首个拿到无方向盘、无踏板目的建造 robotaxi NHTSA 商业豁免的公司 [45]
- **车队规模**：未公开具体数字，2026 年公开目标扩至数十至数百

### 5.3 中国公司在美 Robotaxi：基本缺席

见第 11 节详细分析。

---

## 6. 传统车企的 L2/L3 路径

### 6.1 Ford BlueCruise

- **2025 状态**：蓝区已覆盖美国 **97% 受控进出高速** [35]
- **2025 软件版本 IPMA-24.204.10.9**（秋季）+ **2026 IPMA-25.22.7.3.10B**（夏季）[35]
- **车辆覆盖**：Mustang Mach-E、F-150 Lightning、Explorer（ST-Line/ST/Platinum from 2025 MY）、Lincoln 车型 [35]
- **订阅价**：~$495-$995/年（数据基于 Ford 官网，未给出 2026 统一价目）
- **2026 趋势**：Ford 在 2025 文章中称"hands-free usage skyrockets" [36]

### 6.2 GM Super Cruise

- **2024-2025 网络扩展**：GM 将可用蓝区从 ~400,000 英里**扩至 750,000 英里**——成为北美最大 hands-free 高速公路网 [49][52]
- **2026 MY 升级**：与 Google Maps 整合、拖挂模式等 [51]
- **2026 累计 hands-free 英里**：**超过 10 亿英里** [50 引用 cartipsdaily 2026 数据]
- **覆盖车辆**：2024-2025 15% GM 车型含 Super Cruise [50]；CT4/CT5、Escalade、Silverado EV、Sierra EV 等

### 6.3 Mercedes Drive Pilot L3：主动暂停

- **2023-01-26**：内华达州首个认证 SAE L3 [32]
- **2026-03-24**：加州认证获批 [33][34]
- **2026 中期现状（Unanswered 2026-02-13）**：**Mercedes 已暂停在新车型部署 Drive Pilot**，包括 2026 S-Class 改款改为 **Level 2++ MB.Drive Assist Pro** [37]
- **理由**：成本 vs 需求、传感器成本、当前 ODD（< 40mph 拥堵）"提供收益有限" [37]
- **未来路线**：Mercedes 转向更高速度 L3 + 完整 L4，公共道路 L4 Robotaxi 原型已在 Abu Dhabi 测试，与 NVIDIA 合作核心计算 [37][40]

### 6.4 其他传统车企

- **Toyota Safety Sense**（TSS 3.0/4.0）：标配 L2 全速 ACC + LKA；不进入 L2+/L3 商业化 [12]
- **Stellantis / Stellantis Cloud-Enhanced ADAS**：Mobileye 在 Q2 2026 报新增高产量 Cloud-Enhanced ADAS design win [33]
- **Volvo EX90**：搭载 NVIDIA DRIVE AGX Orin，规划迁至 Thor [38]

---

## 7. 芯片与供应链：Mobileye / NVIDIA / Qualcomm 三足鼎立

### 7.1 Mobileye（MBLY，市值约 $130 亿）

- **2025 全年营收**：$1,894M；净亏 $392M [70]
- **2026-Q1 营收**：**$558M**，同比 **+27%** [70]
- **2026-Q2 营收**：**$508M**（与 2025-Q2 持平；按 GAAP 运营亏损 $30M、调整后运营利润 $46M/+46% YoY） [33]
- **2026 财年指引**：上调至 **$1,970M – $2,020M**，同比 +4% – 7% [33]
- **EyeQ 累计装车（2025 年末）**：超过 **230,000,000 辆** [70]
- **Q2 2026 EyeQ 出货量**：**9.3M**（[34] 引用 24/7 Wall St 数据）
- **EyeQ6 Lite 已上线，设定至 2027 年成为销量最大的汽车级视觉 SoC** [67]
- **Mobileye Chauffeur**：Polestar 4 + ECARX 集成，2026 起装车 [28][29][30]

### 7.2 NVIDIA DRIVE

- **Drive Orin**（254 TOPS）：**当前主流 L2/L3 中央计算平台**，设计赢包括 Mercedes、Volvo、Lucid、中国 OEM 多家 [38][41]
- **Drive Thor**（2,000 TOPS）：2025-2026 生产，首批客户 Mercedes CLA（MB.DRIVE ASSIST PRO 量产 2026-Q1） [40][41]
- **NVIDIA 全球域控制器市占率（H1 2025）**：约 **25-35%**（LinkedIn 行业分析） [63]
- **DriveOS**：安全认证操作系统 [38]

### 7.3 Qualcomm Snapdragon Ride

- **SA8775P**：与 Orin / EyeQ6 并列的 L2+ 主控平台 [63]
- **设计赢**：在 Toyota 等日系厂商占比相对较高；2025-2026 公开设计赢数据零散，但据 LinkedIn 估算占域控制器 ~10-15% 区间 [63]

### 7.4 芯片对比表

| 厂商 | 旗舰 SoC | 算力 (TOPS) | 美国 L2/L3 主力客户 | 2025-2026 关键动作 |
|---|---|---|---|---|
| **Mobileye** | EyeQ6 High / EyeQ Ultra | EyeQ6 ~5x EyeQ5；Ultra Ultra ~172 | Polestar (Chauffeur) + VW/Stellantis | Q1 2026 营收 +27% YoY；累计装车 230M [70] |
| **NVIDIA** | Drive Orin / Thor | Orin 254；Thor 2,000 | Mercedes (MB.DRIVE ASSIST PRO) + Volvo + Lucid | Thor 量产 2026-Q1，首发 CLA [40] |
| **Qualcomm** | SA8775P / SA8797P | SA8775P ~30-50 | Toyota/Lexus、部分中国 | Ride Pilot SDK 扩 [63] |
| **Tesla 自研** | HW4 / AI4 | 144 (HW4) | 仅 Tesla 自用 | 自研路线，**不外销** [64] |

---

## 8. 监管与法规

### 8.1 SAE J3016 与 NHTSA

- **SAE J3016（2021-04 最新修订）**：0-5 级自动驾驶定义；产业事实标准，但**法律上仅是参考**
- **NHTSA SGO 2021-01**：要求 L3+ 运营方上报碰撞数据；2024-08 进一步要求上报所有 SAE L2 ADAS 撞车数据
- **FMVSS（联邦机动车辆安全标准）豁免**：每个无方向盘/踏板的 L4 Robotaxi 都需要 NHTSA 单独豁免；目前获豁免的仅 **Nuro（低速 2018/2020）、Zoox（2026）**等极少数 [45]

### 8.2 州/地方层面

| 州 | L3 立法 | L4 法规 | 2026 关键 |
|---|---|---|---|
| **California** | Mercedes Drive Pilot L3 2026-03-24 获批 [33] | DMV Autonomous Vehicle Tester (Drivered) / Driverless Permit | Zoox SF 免费乘坐、Waymo 全开放 |
| **Nevada** | Mercedes Drive Pilot L3 2023-01 首个 [32] | DMV AV 牌照 | Waymo Las Vegas 试点 |
| **Arizona** | 无 L3 特定立法 | 较宽松，无里程限制 | Waymo Phoenix 全开放、Zoox 计划 |
| **Texas** | 无 L3 立法 | **SB 2807（2025-06 通过）**要求商业 AV 运营方向 TxDMV 备案并自证 SAE L4 [60][61][62] | Tesla / Waymo / Aurora / Zoox 全在德州运营；2026-05-28 SB 2807 生效 |
| **New York** | L3 立法待定 | DMV AV 测试许可（需市议会批） | Waymo 测试许可 2026-03-31 到期未续 [7 引用图说] |

### 8.3 德州 SB 2807 关键内容

- 89R Texas Legislature 于 **2025-06** 通过 [62]
- **生效日**：**2026-05-28** [62]
- 要求：在德州"州内公路"商业运营 AV 的运营商，须向 TxDMV 申请授权 + 自证 SAE L4 能力 + 标识车辆 + 上报事故 + 配合执法 [60][61]
- **2026-05-28 报备数据**：Tesla 42 辆、Waymo 577 辆、Avride 317 辆、Zoox 35 辆 [7]

---

## 9. 事故与安全数据：NHTSA 调查记录

### 9.1 Tesla

| 调查编号 | 启动 | 当前状态 | 关键事实 | 来源 |
|---|---|---|---|---|
| **EA22002** | 2022 | 部分结束，仍持续 | Autopilot 撞应急车辆 | [17] |
| **PE24031** | 2024-10 | 升级至 EA26002 | 低能见度条件 FSD 撞车 | [17][18] |
| **PE25012** | 2025-10-07 | 初步评估进行中 | FSD 违反交通安全法规 | [19] |
| **EA26002** | 2026-03-18 | **"工程分析"**（强制召回前一步） | 涵盖 **3.2M** Tesla 车辆（Model S/X/3/Y + Cybertruck），9 起撞车含 1 致死 | [17][18][20][22] |
| **旧金山 Robotaxi 事故 17 起** | 2025-07 至 2026-04 | 已上报 | 2 起轻伤、1 起需住院 | [7] |

**EA26002 关键事实**：Tesla FSD "未能检测并在低能见度条件（眩光、空气浮质）下警告驾驶员"；"摄像头性能下降前未提供警报，直到撞车前瞬间"；"碰撞发生前 30 秒内 FSD 处于使用状态"系列事件中 1 起致死 [17][18]。

### 9.2 Waymo

| 调查编号 | 启动 | 当前状态 | 关键事实 | 来源 |
|---|---|---|---|---|
| **PE24016** | 2024-05 | **2025-07-29 已结案** | 22 起涉及 440 辆车事件，**未发现系统性违规** | [53] |
| **校车周边违规调查** | 2025-10 | 2025-12 软件召回 | Waymo 在停靠校车附近违规保护行人的规则 | [59] |
| **2025 全年累计上报** | — | — | 464+ 起 [57] | [57] |
| **首起致死事件** | 2025 年内 | 详情未完整披露 | — | [57] |

### 9.3 Cruise

| 调查 | 状态 |
|---|---|
| NHTSA 2023-12 启动调查 | **截至 2026-05 仍开放** [16] |
| 旧金山 DMV 2023-10-24 吊销许可 | 未恢复 [12] |

---

## 10. 中国出海玩家在美国的实际状态

### 10.1 总览

中国头部新能源车企在美国的真实定位（2026-Q2）：

| 公司 | 美国整车销售 | 美国智驾功能 | 备注 |
|---|---|---|---|
| **蔚来 NIO** | **0**（无进口，无本地组装） | 无 | 2022 宣布进美国，**未实现**；主要资源欧洲[66] |
| **小鹏 XPeng** | **0 整车** | **通过 G6/G9 出口至极少数量经销商**（2025 H1 进入英国、意大利、爱尔兰等欧洲 46 国） [56] | 美国市场未启动零售；通过 VW 合作输出智驾方案 |
| **理想 Li Auto** | **0**（2023 取消美国上市计划） | 无 | 中国市场专注；无美国渠道 [12] |
| **比亚迪 BYD** | **0 整车零售**（100% 关税） | 无 | 2025-07 暂停墨西哥工厂计划 [54][55]；2026-Q2 通过加拿大（6.1% 关税额度内）开 ~20 家经销 [61 引用 thedailyautomotive] |
| **中国 Robotaxi（萝卜快跑、文远知行等）** | 美国基本无运营 | 仅 Pony.ai、Aurora 背景投资 | 美国"中国造" Robotaxi 缺席 |

### 10.2 BYD 在美核心数据（2026-Q2）

- 美国对中国 EV 关税：**100%+** [55 引用 cartax]
- BYD 2023 宣布墨西哥 150K 产能工厂 → **2025-07 暂停**（贸易不确定性 + Trump 关税） [54]
- 2026-02 BYD 与 Geely 联合竞标日产-奔驰 230K 产能墨西哥工厂（仍在谈判）[57]
- 墨西哥 2025-09 起对中国 EV 关税升至 **50%** [55 引用 eletric-vehicles.com]
- BYD 加拿大："6.1% 关税额度新规" → 计划魁北克、BC 等开 ~20 家经销商，2026 年内开始零售 [61]

### 10.3 XPeng 的美国策略

- 2025-07 月报：XPeng 进入 46 国，新增英国/意大利/爱尔兰 [56]
- 2025 全年海外交付：**45,008 辆**（+96% YoY），2025 年末覆盖 **60 国** [58]
- 美国市场：未启动零售；与大众汽车合作输出 E/E 架构与智驾方案
- **XPeng G6 / G9 / Mona M03**：中国主销；2024 末曾在挪威、荷兰试点

### 10.4 中国对美智驾输出的间接路径

- **Mobileye Chauffeur + ECARX + Polestar 4**：中国 OEM 在欧洲采用 Mobileye Chauffeur + Polestar 平台，但实际数据闭环在美国/欧洲 [28][29][30]
- **小鹏 XNGP / 华为 ADS**：仅在中国数据闭环
- **Mobileye Q2 2026 报新增 Stellantis Cloud-Enhanced ADAS 设计赢**，包含 17 款 ICE/EV 车型，2026 起陆续推出 [65]——这条线通过 OEM 把中国可控的智驾方案间接带进美国市场

---

## 11. 关键风险与不确定性

### 11.1 监管

- **NHTSA EA26002 vs Tesla**：320 万辆调查距离"召回"仅一步。Musk 若 v15 未在 2026-Q4 推出，监管可能强制要求 FSD 在低能见度条件下失效或限制使用区域
- **德州 SB 2807**：2026-05-28 生效后，对未通过 SAE L4 自证的运营商可能吊销州内运营权
- **加州 DMV** 对 Zoox 商业豁免仍开放，但 Zoox 是首批受益者，后续厂商未必能获相同豁免

### 11.2 技术

- **Tesla FSD v15 推迟风险**：Musk 在 2026-Q1 已暗示推迟 6 个月——若 2026 末未发布，"奥斯汀 20 辆车"叙事会被持续放大
- **Tesla 摄像头-only 路线**：Reuters 调查指出其路线专属准备与 Musk 主张冲突 [11]
- **Waymo L4 成本下降速度**：当前单车成本 $50K-$100K 估算（业界口径），尚未实现与人类司机成本交叉

### 11.3 商业

- **Cruise 重启风险**：Phoenix 测试尚未载客；休斯顿 2026-09 计划载客能否兑现存疑
- **Zoox 收费后能否扩量**：免费 → 收费转换可能拉低 ride 数
- **Aurora 卡车商业化速度**：2025 全年仅 $3M 营收，距 IPO 时"百亿美元"叙事差距大

### 11.4 中国出海的不确定性

- **BYD 美国市场入场**：100%+ 关税 + Trump 政府对 USMCA 收紧，进入美国至少要 2-3 年
- **XPeng 美国**：暂无明确零售时间表
- **Mobileye / ECARX / Polestar 间接路径**：是"中国数据闭环进入美国"的最现实通道，但美国 OEM 更倾向直接控制平台

---

## Sources

[1] https://waymo.com/blog/shorts/safetydata-june26 — Waymo safety data 220M miles (June 2026)
[2] https://waymo.com/safety/impact — Waymo Safety Impact hub
[3] https://waymo.com/blog/shorts/dallas-open-to-all — Waymo Dallas open to all 2026-08-04
[4] https://waymo.com/blog/shorts/nashville-june2026 — Waymo Nashville opens 2026-06-25
[5] https://waymo.com/blog/shorts/ro-den-lv-sd-tmpa — Waymo 4 new cities 2026-07-08
[6] https://waymo.com/blog/shorts/waymo-in-portland — Waymo Portland announce 2026-04-28
[7] https://www.techtimes.com/articles/318160/20260610/tesla-robotaxi-trails-waymo-42-577-texasaustin-map-masks-20-car-fleet-until-fsd-v15-rewrite.htm — Tech Times: Tesla Trails Waymo 42-577 in TX (2026-06-10)
[8] https://techcrunch.com/2025/06/22/tesla-launches-robotaxi-rides-in-austin-with-big-promises-and-unanswered-questions — TechCrunch: Tesla Robotaxi Austin launch 2025-06-22
[9] https://fortune.com/2025/06/22/elon-musk-tesla-robotaxi-service-launch-austin-420-flat-fee — Fortune: Tesla Robotaxi $4.20 flat fee 2025-06-22
[10] https://www.cnbc.com/2025/06/20/tesla-robotaxi-launch-austin.html — CNBC: Tesla Robotaxi launch details 2025-06-20
[11] https://www.reuters.com/business/autos-transportation/tesla-fsd-safety-claims-misleading-2026-05-28 — Reuters: Tesla FSD safety inflated 2026-05-28
[12] https://www.birow.com/cruise-journey — Birow: Cruise Journey 2025-04
[13] https://www.fox7austin.com/news/no-more-cruise-robotaxis-general-motors-acquisition — Fox7: Cruise not relaunching 2025-02-06
[14] https://www.cnbc.com/2024/12/10/gm-halts-funding-of-robotaxi-development-by-cruise.html — CNBC: GM exits robotaxi 2024-12-10
[15] https://techcrunch.com/2024/06/11/gm-gives-cruise-850m-lifeline-as-it-relaunches-robotaxis-in-houston — TechCrunch: GM $850M lifeline Cruise 2024-06-11
[16] https://newsalot.net/2026/05/31/gms-cruise-resumes-robotaxi-testing-in-houston-after-18-month-pause — Newsalot: Cruise resumes Houston 2026-05-31
[17] https://www.cnbc.com/2026/03/19/tesla-nhtsa-full-self-driving-fsd-reduced-visibility.html — CNBC: Tesla NHTSA reduced visibility 2026-03-19
[18] https://electrek.co/2026/03/19/nhtsa-upgrades-tesla-fsd-visibility-investigation-3-2-million-vehicles — Electrek: NHTSA upgrades Tesla FSD 2026-03-19
[19] https://static.nhtsa.gov/odi/inv/2025/INOA-PE25012-19171.pdf — NHTSA PE25012 FSD investigation 2025-10-07
[20] https://static.nhtsa.gov/odi/inv/2026/INOA-EA26002-10023.pdf — NHTSA EA26002 Tesla FSD 2026-03-18
[22] https://motorillustrated.com/nhtsas-fsd-investigation-enters-recall-track-phase-covering-3-2-million-vehicles/178820 — MotorIllustrated: NHTSA FSD 3.2M recall-track 2026-03-20
[24] https://ir.aurora.tech/news-events/press-releases/detail/119/aurora-begins-commercial-driverless-trucking-in-texas-ushering-in-a-new-era-of-freight — Aurora IR: Commercial driverless trucking Texas 2025-05-01
[25] https://ir.aurora.tech/news-events/press-releases/detail/128/aurora-expands-driverless-trucking-service-from-fort-worth-to-el-paso — Aurora IR: Fort Worth to El Paso expansion 2025-10-28
[26] https://www.post-gazette.com/business/tech-news/2026/02/12/aurora-innovation-driverless-trucks-sun-belt/stories/202602120068 — Post-Gazette: Aurora $3M revenue 2025
[27] https://aurora.tech/newsroom/progress-in-2024-readying-for-commercial-launch — Aurora: Progress in 2024
[28] https://www.mobileye.com/news/polestar-selects-mobileye-to-bring-autonomous-technology-to-polestar-4 — Mobileye: Polestar 4 Chauffeur
[29] https://media.polestar.com/releases/538 — Polestar: Luminar LiDAR Mobileye Chauffeur
[30] https://www.mobileye.com/news/ecarx-announces-mobileye-collaboration-for-polestar-future-products — Mobileye: ECARX Polestar collaboration
[32] https://group.mercedes-benz.com/technology/autonomous-driving/driving/drive-pilot-nevada.html — Mercedes: Drive Pilot Nevada 2023-01-26
[33] https://ir.mobileye.com/news-releases/news-release-details/mobileye-releases-second-quarter-2026-results-updates-guidance — Mobileye IR: Q2 2026 $508M revenue, 9.3M EyeQ shipments
[34] https://www.fool.com/earnings/call-transcripts/2026/04/23/mobileye-mbly-q1-2026-earnings-transcript — Motley Fool: Mobileye Q1 2026 transcript
[35] https://www.ford.com/technology/bluecruise — Ford: BlueCruise hands-free 97% highways
[36] https://www.fromtheroad.ford.com/us/en/articles/2026/2025-bluecruise-trends-hands-free-usage-skyrockets — Ford: BlueCruise 2025 trends
[37] https://unanswered.io/guide/mercedes-level-3-autonomous-driving-usa-availability — Unanswered: Mercedes Drive Pilot USA Status Feb 2026
[38] https://www.nvidia.com/en-us/solutions/autonomous-vehicles — NVIDIA: Robotaxi AV solutions
[40] https://electrek.co/2026/01/05/nvidia-unveils-open-source-ai-for-autonomous-driving-ships-in-mercedes-benz-cla-in-q1-2026 — Electrek: NVIDIA open-source AI Mercedes CLA 2026-01-05
[41] https://datacentremagazine.com/globenewswire/3190664 — Data Centre Mag: Nvidia automotive computing market 2026
[42] https://www.basenor.com/pages/tesla-software-updates — Basenor: Tesla Software Updates 2026
[43] https://www.cnbc.com/2026/08/05/amazon-zoox-paid-robotaxi-rides-las-vegas.html — CNBC: Zoox paid rides Vegas 2026-08-05
[44] https://techcrunch.com/2026/08/05/zoox-to-start-charging-for-robotaxi-rides-in-las-vegas — TechCrunch: Zoox paid Vegas 2026-08-05
[45] https://www.latimes.com/business/story/2026-08-10/zoox-to-begin-paid-rides-following-regulatory-approval — LATimes: Zoox paid rides 2026-08-10
[46] https://waymo.com/blog/2025/12/2025-year-in-review — Waymo 2025 Year in Review (15M rides, 20M lifetime)
[47] https://www.thedriverlessdigest.com/p/waymos-2025-year-in-review-the-year — Driverless Digest: Waymo 2025 review
[48] https://evmagazine.com/articles/zoox-robotaxi-is-expanding-in-las-vegas-and-san-francisco — EV Magazine: Zoox 2M miles 350K riders
[49] https://investor.gm.com/news-releases/news-release-details/gm-expands-super-cruise-network-750000-hands-free-miles-largest — GM Investor: Super Cruise 750K miles
[50] https://gmauthority.com/blog/2024/10/15-percent-of-gm-vehicles-will-include-super-cruise-in-2025 — GM Authority: 15% GM vehicles Super Cruise 2025
[51] https://gmauthority.com/blog/2025/07/gm-super-cruise-gets-these-enhancements-for-2026-model-year-vehicles — GM Authority: Super Cruise 2026 MY
[52] https://www.gm-trucks.com/general-motors-expands-super-cruise-to-over-750000-miles-of-roads — GM-Trucks: Super Cruise 750K miles 160M safety
[53] https://www.huschblackwell.com/newsandinsights/nhtsa-closes-waymo-investigation-key-takeaways-for-the-av-industry — Husch Blackwell: NHTSA closes Waymo probe 2025-07-29
[54] https://www.electrive.com/2025/07/03/byd-halts-mexico-factory-plans-amid-trumps-trade-tensions — Electrive: BYD halts Mexico factory 2025-07-03
[55] https://www.cfr.org/articles/what-canadian-and-mexican-ev-imports-from-china-mean-for-the-united-states — CFR: Mexico Canada China EV imports
[56] https://ir.xiaopeng.com/news-releases/news-release-details/xpeng-announces-vehicle-delivery-results-july-2025 — XPeng IR: July 2025 delivery
[57] https://humanoidliability.com/resources/waymo-2025-incident-tracker — Waymo 2025 Incident Tracker
[58] https://www.prnewswire.com/news-releases/xpeng-announces-vehicle-delivery-results-for-december-and-full-year-2025-302651514.html — PR Newswire: XPeng FY2025 delivery 45K overseas
[59] https://bgr.com/2051218/waymo-recall-self-driving-cars-safety-concerns — BGR: Waymo school bus safety recall Dec 2025
[60] https://www.txdmv.gov/AVprogram — TxDMV: Automated Vehicles Regulatory Program SB2807
[61] https://capitol.texas.gov/tlodocs/89R/billtext/html/SB02807F.HTM — Texas Legislature: SB2807 enrolled
[62] https://dallasexpress.com/state/texas-self-driving-law-takes-effect-today-robotaxis-av-trucks-need-txdmv-permit — Dallas Express: Texas AV law effective 2026-05-28
[63] https://www.linkedin.com/pulse/adas-soc-wars-nvidia-drive-orin-vs-qualcomm-sa8775p-eyeq6-mudduluru-hos0c — LinkedIn: ADAS SoC Wars - NVIDIA Orin vs Qualcomm vs Mobileye
[64] https://www.eetimes.com/what-is-nvidia-doing-in-automotive — EE Times: NVIDIA automotive Thor
[65] https://iot-automotive.news/mobileye-reveals-new-wins-for-key-tech-platforms-with-large-global-automaker — IoT Automotive: Mobileye new design wins
[66] https://chip.computer/guides/autonomous-driving-chips-guide — Chip.computer: AD chips guide 2026
[67] https://www.mobileye.com/news/mobileye-eyeq6-lite-launches-to-speed-adas-upgrades-worldwide — Mobileye: EyeQ6 Lite launch 46M vehicles
[70] https://ir.mobileye.com/news-releases/news-release-details/mobileye-releases-first-quarter-2026-results-updates-full-year — Mobileye IR: Q1 2026 $558M revenue, 230M cumulative EyeQ
