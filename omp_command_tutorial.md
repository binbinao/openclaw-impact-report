# OMP 命令小白实战手册

> 目标：看完这一篇,你应该知道 **敲哪个命令 → 看到什么效果 → 适合什么场景**。
> 文档基于 `omp v18.0.7`(本地 `~/.bun/bin/omp`)。

## 🧭 三秒钟选命令

| 我想做的事 | 用这个命令 |
| --- | --- |
| 打开 AI 终端,边聊边改代码 | `omp` |
| 一次问完就退出,把答案喂给脚本 | `omp -p "问题"` |
| 接上次没问完的会话 | `omp -c` |
| 换模型 / 换思考深度 | `Ctrl+P` 或 `--model` |
| 列出全部可用模型 | `omp models` |
| 改默认配置(审批、模型角色、思考) | `omp config set ...` |
| 装插件 / 扩展 | `omp plugin install ...` |
| 把会话导出成 HTML 给同事看 | `omp --export <id>` |

下面把每一类都展开讲。

---

## 0️⃣ 安装篇：macOS / Linux 安装 + IDE 搭配

> 前置要求：Bun 安装方式需要 **bun ≥ 1.3.14**；官方支持 macOS / Linux / Windows。

### 方式一：Bun 全局安装（官方推荐 ⭐）

**效果**：以 npm 包形式装进 bun 全局目录（`~/.bun/bin/omp`），升级、卸载都是一条命令。
**适合**：绝大多数人，尤其想持续跟进新版本的。

```sh
# 1. 先装 bun（macOS / Linux，已装可跳过）
curl -fsSL https://bun.sh/install | bash

# 2. 重开终端（或 source ~/.zshrc）后安装 omp
bun install -g @oh-my-pi/pi-coding-agent

# 3. 验证
omp --version        # 输出 omp/18.x.x 即成功
```

之后升级只需 `bun update -g @oh-my-pi/pi-coding-agent`。

### 方式二：一键脚本（macOS / Linux）

**效果**：下载预编译二进制到本地，**不依赖 bun**。
**适合**：不想装额外运行时、只想快速试用的。

```sh
curl -fsSL https://omp.sh/install | sh
```

⚠️ Alpine（musl）用户注意：先补动态库依赖 `apk add libstdc++ libgcc`，再跑安装脚本。

### 方式三：Homebrew（macOS / Linux）

**效果**：走 brew 第三方 tap，跟随 `brew upgrade` 统一管理。
**适合**：所有软件都用 brew 管的人。

```sh
brew install can1357/tap/omp
```

### 其他方式速览

| 方式 | 命令 | 适合谁 |
| --- | --- | --- |
| Nix | `nix profile install github:can1357/oh-my-pi` | NixOS / 声明式配置党 |
| mise | `mise use -g github:can1357/oh-my-pi` | 需要在多版本间固定/切换 |
| Windows | `irm https://omp.sh/install.ps1 \| iex` | PowerShell 用户 |

### 装完后的两步收尾

```sh
# 1. shell 补全（zsh 为例；bash/fish 用 omp completions bash / fish）
echo 'eval "$(omp completions zsh)"' >> ~/.zshrc

# 2. 首次配置向导：选 provider、登录、装可选依赖
omp setup
```

补全脚本由 omp 基于实时命令元数据自动生成，**永远不会和实际 CLI 脱节**。

### 搭配哪个 IDE？

| 你的主力编辑器 | 推荐打法 | 集成深度 |
| --- | --- | --- |
| **Zed** | Zed 内通过 ACP 协议驱动 `omp acp` | ★★★ 官方原生集成 |
| **VS Code / Cursor** | 内置终端跑 `omp --cwd <项目目录>` | ★★ 终端 TUI（无官方插件） |
| **JetBrains 系** | 内置终端跑 `omp` | ★★ 同上 |
| **纯终端流** | zellij / tmux 分屏 + `omp` | ★★ TUI 本体 |

**Zed 是唯一有官方 IDE 集成的**：通过 ACP（Agent Client Protocol）协议，Zed 里跑的就是终端里那个同一个 agent——直接读你正在看的 buffer、文件写入走编辑器的保存路径、破坏性操作在编辑器里弹一次权限确认。官方原话："No bridge, no plugin, no second brain to keep in sync"（无桥接、无插件、无需同步的第二大脑）。

VS Code / Cursor / JetBrains 目前**没有官方插件**。不过 omp 本身是 TUI 优先设计，在任何编辑器的内置终端里都能完整工作——编辑器负责"看"，omp 负责"改"。

### 最优结论（怎么选）

1. **装法最优 = Bun 全局安装**：官方推荐方式，升级 `bun update -g` 一步到位
2. **IDE 最优 = Zed + ACP**：目前集成度最高的组合，agent 与编辑器共享同一份上下文
3. **没有 Zed 也别纠结**：VS Code / Cursor + 内置终端 `omp`，零配置即可开工
4. **服务器 / 远程开发**：ssh 上去用 zellij/tmux 挂着 `omp` 跑长任务，断线不丢会话

---

## 1️⃣ 启动类：怎么把 OMP 跑起来

### `omp`（默认 launch）
**效果**：进入一个全屏交互终端(TUI),你打字,AI 回话,中间会自动读文件、改代码、跑命令。
**适合**：所有"和 AI 一起写代码"的场景。

```sh
omp
```
进入后屏幕长这样：
- 顶部：会话标题 + 当前模型
- 中部：对话流（你的消息、AI 思考、AI 回复、工具调用结果）
- 底部：输入框（提示符>）

直接输入问题回车就开始;`/` 开头的会被识别为内置命令。

### `omp "问题"`（带初始提示）
**效果**：直接开始会话,并把第一个问题塞进去。
**适合**：你想跳过"先打招呼",直接进入正题。

```sh
omp "列出 pytorch/ 下所有 chapter_* 目录"
```

### `omp -p "问题"`（print 模式 / 无头）
**效果**：AI 答完 → 退出。**不进** TUI,纯命令行。
**适合**：脚本、CI、子代理调用。

```sh
omp -p "总结 README.md 的前 3 条要点"
```

常见搭配：

```sh
omp -p --mode json "列出所有 TODO" > todos.json   # 输出 JSON
omp -p --print-thoughts "解释这段代码"             # 把思考过程也打出来
omp -p --max-time 10m "分析整个目录"              # 超过 10 分钟就强退
```

### `omp -c` / `omp --continue`
**效果**：把**上一次**的会话原样恢复(包含之前的对话、模型、思考级别)。
**适合**：上次聊到一半被打断,接着聊。

```sh
omp -c "上次说到的那个 bug 修了吗?"
```

### `omp --resume` / `omp --resume <id>`
**效果**：打开一个会话选择器(列出最近 N 个会话),选一个接着聊。
**适合**：跨项目恢复、找上次聊的那个会话。

```sh
omp --resume            # 打开选择器
omp --resume 1f9d       # 按 ID 前缀直接打开
```

### `omp --fork <id>`
**效果**：从已有会话复制一份,**新 ID、新分支**,改动不影响原会话。
**适合**：想"如果当时走了另一条路会怎样"。

```sh
omp --fork 1f9d "换个方案,试试用 numpy 实现"
```

### `omp --export <id>`
**效果**：把某个会话转成独立 HTML 文件,**然后退出**(不进入 TUI)。
**适合**：把 AI 协作过程分享给没装 omp 的同事。

```sh
omp --export 1f9d
# 生成的 HTML 默认在 ~/.omp/agent/sessions/.../1f9d.html
```

### `omp --from-claude` / `omp --from-codex`
**效果**：把别的工具(Claude Code / Codex)的历史会话导入 omp。
**适合**：换工具时不丢上下文。

---

## 2️⃣ 模型类：换 AI 大脑

### `omp --model <id>`
**效果**：本次会话用指定模型(临时覆盖)。
**适合**：临时想试一下更强的模型 / 便宜模型。

```sh
omp --model claude-sonnet-4-5          # 模糊匹配
omp --model openai/gpt-5.2             # 精确 provider/model
omp --model @slow                      # 用配置里的 slow 角色
```

### `omp --smol` / `--slow` / `--plan`
**效果**：分别设置"快/便宜"、"慢/强"、"规划专用"三个角色的模型。
**适合**：和 `--thinking` 配合,搭出"规划用强模型,执行用便宜模型"的工作流。

```sh
omp --slow anthropic/claude-opus-4-5:high --thinking xhigh -p "重构这个模块"
```

### `omp models`
**效果**：列出**当前能用的所有模型**(按 provider 分组)。
**适合**：选模型前先看有哪些。

```sh
omp models                       # 人类可读
omp models --json                # 机器可读
omp models openai-codex          # 只看 openai-codex 提供方
omp models find claude           # 模糊搜索
omp models refresh               # 刷新可用模型缓存
```

### TUI 内的快捷键
| 键 | 效果 |
| --- | --- |
| `Ctrl+P` | 循环到下一个模型 |
| `Shift+Ctrl+P` | 循环到上一个 |
| `Alt+P` | 临时选个模型,只这次有效 |
| `Alt+M` | 打开模型选择器,改默认 |
| `Alt+A` | 打开 Agent Hub(管理 subagent) |

---

## 3️⃣ 思考类：让 AI 多想 / 少想

### `omp --thinking <level>`
**效果**：控制 AI 每步思考的深入程度。
**适合**：复杂任务开高,简单任务开低省 token。

可选值:`off / minimal / low / medium / high / xhigh / max / auto`

```sh
omp --thinking high -p "解释这段代码"
omp --thinking max  -p "给一个金融系统的安全方案"
```

### `Ctrl+T`
**效果**：在 TUI 内切换"显示/隐藏思考块"。
**适合**：想看 AI 怎么想的 → 显示;嫌屏幕乱 → 隐藏。

### `Shift+Tab`
**效果**：循环切换思考级别。

### `omp --hide-thinking`
**效果**：本次启动默认不显示思考块。
**适合**：录屏 / 分享时屏幕干净点。

### magic keyword：`ultrathink`
**效果**：在 prompt 里直接写这个词,触发"本轮最深度思考"。
**适合**：偶尔一道难题,不想改全局配置。

```text
ultrathink 帮我设计一个能扛住双十一的订单系统
```

---

## 4️⃣ 工具类：让 AI 能不能动你的电脑

### `omp --tools a,b,c`
**效果**：本次会话**只允许**用列表里的工具。
**适合**：不放心?先限制 AI 只能读不能改。

```sh
omp --tools read,grep,glob "先分析,别改文件"
omp --tools "" --no-tools -p "纯聊天,什么都别调"   # 完全禁用工具
```

### `omp --approval-mode yolo`
**效果**：AI 做的所有操作自动放行,**不再询问**。
**适合**：跑批 / CI / 自动化任务,无人值守。

```sh
omp --yolo -p "把这个目录里所有 .py 文件加 type hint"
```

### `omp --approval-mode always-ask`
**效果**：每个工具调用都问一遍。
**适合**：第一次跑 AI 操作、不熟悉的环境。

### 默认模式 `write`
**效果**：读类操作默认放行,写类(bash、edit、write)每次问。
**适合**：日常使用,够安全也不烦。

### 配置化审批（`omp config`）
**效果**：写进配置,持久生效,所有会话默认遵守。

```sh
# 让 git 命令默认放行,但 rm -rf 永远拒绝
omp config set tools.approval '{"bash":"prompt"}'
omp config set bash.patterns '[
  {"match":"git *","approval":"allow"},
  {"match":"rm -rf *","approval":"deny"},
  {"match":"*","approval":"allow"}
]'
```

---

## 5️⃣ 内置斜杠命令（TUI 内输入 `/` 自动补全）

输入 `/` 会弹出菜单,以下是**最常用的 20 条**：

### 会话管理
| 命令 | 你看到的效果 |
| --- | --- |
| `/help` | 列出当前可用命令 + 工具清单 |
| `/init` | 扫当前目录,生成项目上下文(AGENTS.md 等) |
| `/new` | 开一个全新会话(丢掉当前) |
| `/clear` | 清空当前会话的实时对话流,历史保留 |
| `/resume` | 打开会话选择器,选旧的 |
| `/fork` | 从当前位置派生一个新分支会话 |
| `/tree` | 可视化当前会话的分支树 |
| `/status` | 显示当前 provider / 模型 / token 用量 / 工具 |

### 模型与模式
| 命令 | 效果 |
| --- | --- |
| `/model` | 切换模型 |
| `/plan` | 切换 plan 模式(只读、不动代码) |
| `/compact` | 手动触发上下文压缩,腾出空间 |
| `/agents` | 打开 Agent Hub,管理 subagents |
| `/skill:<name>` | 加载指定 skill |

### 输出 / 协作
| 命令 | 效果 |
| --- | --- |
| `/copy` | 复制最后一条 AI 回复 |
| `/share` | 生成加密分享链接(同 `omp share`) |
| `/join` | 加入协作会话 |
| `/usage` | 显示各 provider 账户的用量限额 |
| `/update` | 检查 / 安装 omp 自身更新 |
| `/settings` | 打开设置面板(交互式,带搜索) |
| `/hotkeys` | 列出当前所有键绑定 |

### 退出 / 暂停
| 命令 | 效果 |
| --- | --- |
| `/pause` | **只 TUI**:暂停所有代理,Esc 恢复 |
| `Ctrl+C` | 中断当前 AI 输出 |

---

## 6️⃣ `omp config`：改配置的万能入口

### 列出全部设置
```sh
omp config list                  # 按 tab 分组,带默认值和类型
omp config list --json           # 机器可读
```
**效果**：一张表,所有可调旋钮一目了然。

### 查看单个设置
```sh
omp config get defaultThinkingLevel
omp config get tools.approvalMode --json
```

### 修改单个设置
```sh
omp config set defaultThinkingLevel high
omp config set theme.dark titanium
omp config set compaction.enabled false
omp config set tools.approval '{"bash":"allow","read":"allow"}'   # 对象用 JSON
omp config set enabledModels '["claude-sonnet-4-5"]'              # 数组用 JSON
```
**效果**：立刻写入 `~/.omp/agent/config.yml`,下次启动生效。

### 重置
```sh
omp config reset steeringMode    # 写回 schema 默认值
```

### 找配置文件在哪
```sh
omp config path                  # 打印当前 agent 目录
```

### 配置文件位置（优先级从低到高）
```text
builtin defaults  <  ~/.omp/agent/config.yml  <  <cwd>/.omp/config.yml  <  --config <file>  <  CLI flag/env
```
简单说：**项目级配置会盖掉全局,CLI flag 会盖掉项目级**。

### 常用 YAML 片段
```yaml
# ~/.omp/agent/config.yml

modelRoles:                       # 角色 → 模型 映射
  default: anthropic/claude-sonnet-4-5
  smol: openai/gpt-4.1-mini
  slow: anthropic/claude-opus-4-5:high

defaultThinkingLevel: high        # off|minimal|low|medium|high|xhigh|max|auto

tools:
  approvalMode: write             # always-ask|write|yolo
  approval:
    bash: prompt
    read: allow

compaction:
  strategy: snapcompact
  thresholdPercent: 80

theme:
  dark: titanium
```

---

## 7️⃣ 常用子命令（不是 TUI 内的命令,是终端直接敲的）

| 命令 | 你输入后会发生什么 |
| --- | --- |
| `omp models` | 列出全部模型 |
| `omp config ...` | 配置管理 |
| `omp setup` | 首次配置向导 / 装可选依赖(如 `omp setup python` 装 Python 内核) |
| `omp agents unpack` | 把内置 subagents 导出到 `~/.omp/agent/agents/` |
| `omp agents unpack --project` | 导出到 `./.omp/agents/` |
| `omp plugin install <name>` | 从市场装插件 |
| `omp plugin list` | 列出已装插件 |
| `omp install <pkg>` | 安装 / 链接本地扩展包 |
| `omp usage` | 各 provider 账户的限额 / 余额 |
| `omp stats` | 用量统计 |
| `omp update` | 检查 / 安装 omp 自身更新 |
| `omp gc` | 跑存储垃圾回收 |
| `omp ps` | 列出 omp 管理的后台进程 |
| `omp share` | 加密分享当前会话 |
| `omp completions bash` | 打印 bash 补全脚本 |
| `omp token <provider>` | 取 provider 的 API key / OAuth token |
| `omp ssh` | 管理 SSH host 配置 |
| `omp read <path>` | CLI 测 read 工具(可读 URL、内部 URI) |
| `omp grep <pattern>` | CLI 测 grep 工具 |
| `omp search "<query>"` | CLI 测 web_search |
| `omp say "hello"` | 本地 TTS 播放 |
| `omp bench` | 给模型跑 TTFT / 吞吐基准 |
| `omp --version` | 看版本 |

---

## 8️⃣ 必背的 10 个键

TUI 里这些键会让你效率翻倍：

| 键 | 效果 |
| --- | --- |
| `Ctrl+P` | 下一个模型 |
| `Alt+P` | 临时选个模型 |
| `Alt+M` | 打开模型选择器 |
| `Alt+Shift+P` | 切换 plan 模式 |
| `Ctrl+T` | 显示/隐藏思考块 |
| `Shift+Tab` | 循环思考级别 |
| `Ctrl+O` | 展开/折叠工具输出 |
| `Ctrl+R` | 搜 prompt 历史 |
| `Ctrl+Q` 或 `Ctrl+Enter` | 排一条 follow-up 消息(等当前 AI 输出完才发) |
| `Ctrl+L` | 开/关 live 语音模式 |
| `Alt+A` | 打开 Agent Hub |

想看完整列表 → `omp --help` 或 TUI 内 `/hotkeys`。

---

## 9️⃣ 5 个让生活变简单的 flag

只记这 5 个,90% 场景够用：

| Flag | 一句话作用 | 例子 |
| --- | --- | --- |
| `--model <id>` | 换模型 | `--model gpt-5.2` |
| `--thinking <lv>` | 控制思考深度 | `--thinking high` |
| `--yolo` | 全自动,啥也别问 | 跑批任务 |
| `-p` | 无头模式,答完退出 | `omp -p "..."` |
| `-c` / `--continue` | 接上次会话 | `omp -c` |

---

## 🔟 D2L 项目里的实际玩法

### A. 扫一遍项目,生成阅读路线
```sh
cd /Users/duobinji/Documents/GitHub/d2l
omp -p "扫描 pytorch/,列出所有 chapter_* 目录,按官方推荐顺序输出"
```
**你会看到**：一个排序好的目录列表 + 每个目录的一句话简介。

### B. 找一个 issue,让 AI 排查
```sh
# 先开个交互会话
omp
# 在 TUI 里输入：
> @pytorch/chapter_multilayer-perceptrons/mlp.ipynb 这个 notebook 第 3 个 cell 报错,
> 帮我看一下原因并修复
```
**你会看到**：AI 读文件 → 看代码 → 跑命令复现 → 给出修复。

### C. 批量翻译 docstring
```sh
omp --slow claude-opus-4-5:high --thinking high -p \
  "把 pytorch/chapter_preliminaries/ndarray.py 里所有英文 docstring 翻译成中文,代码和签名保持不变"
```
**你会看到**：diff 视图 + 修改后的文件(默认要你确认才落盘)。

### D. 并行给每章生成 README 摘要
```sh
omp -p "orchestrate:为 pytorch/ 下每个 chapter_* 目录并行生成 README 摘要,写入 _mydocs/summaries/<chapter>.md"
```
**你会看到**：多个 subagent 同时开干,各自认领不同章节,最后合并结果。

### E. 项目内单独开一份配置
在仓库根新建 `.omp/config.yml`：
```yaml
modelRoles:
  default: anthropic/claude-sonnet-4-5
  smol: openai/gpt-4.1-mini
tools:
  approval:
    bash: allow       # 这个项目里允许任意 bash
    notebook: prompt  # 改 notebook 前问一声
```
之后在该目录跑 `omp`,自动加载这份配置。

### F. 给同事发一份"我和 AI 协作的完整记录"
```sh
omp --resume             # 选要导出的会话
omp --export <id>        # 生成 HTML
open ~/.omp/agent/sessions/<encoded>/<id>.html
```

---

## ❓ 卡住了怎么办

| 现象 | 试试 |
| --- | --- |
| 命令不存在 / 行为不对 | `omp <command> --help` 或 `omp --help` |
| 想看某个设置当前值 | `omp config get <key>` |
| 改坏了想回到默认 | `omp config reset <key>` |
| AI 不听指挥 | `/clear` 或 `/new` 开新会话;或者 `/compact` 压缩上下文 |
| 上下文太满、AI 变笨 | `/compact`,或在配置里调 `compaction.thresholdPercent` |
| 看不到模型列表 | `omp models refresh`,检查 API key |
| 当前快捷键是啥 | TUI 内 `/hotkeys` |
| 装了插件没生效 | `/reload-plugins` |
| 想看底层文档 | 官方文档:`omp://cli-reference.md`、`omp://settings.md` 等 |

---

## 📚 想再深入看

| 想了解 | 看哪里 |
| --- | --- |
| 完整 CLI flag | `omp --help` / `omp://cli-reference.md` |
| 所有设置项 | `omp config list` / `omp://settings.md` |
| 模型与自定义 provider | `omp://models.md` |
| 斜杠命令怎么实现的 | `omp://slash-command-internals.md` |
| 会话怎么存的 | `omp://session.md` |
| 键盘绑定怎么改 | `omp://keybindings.md` |
| Magic keywords | `omp://magic-keywords.md` |
| 装扩展 / 插件 | `omp://extensions.md` / `omp://marketplace.md` |
| 环境变量全表 | `omp://environment-variables.md` |

> **一句话总结**：装它用 `bun install -g @oh-my-pi/pi-coding-agent`；日常就是 `omp` 进 TUI、用 `/` 命令、`Ctrl+P` 换模型、`Ctrl+T` 看思考;要自动化就 `omp -p`;要改全局行为就 `omp config`。
