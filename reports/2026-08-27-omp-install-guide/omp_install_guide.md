# OMP 安装指南：macOS / Linux 安装与 IDE 搭配

> 本文是 **OMP（oh-my-pi coding agent）** 的独立安装指南，覆盖 macOS / Linux 全部安装方式、装完收尾步骤，以及 IDE 搭配建议。命令用法请见姊妹篇《[OMP 命令小白实战手册](../2026-08-27-omp-cli-tutorial/omp-cli-tutorial.html)》。
>
> 前置要求：Bun 安装方式需要 **bun ≥ 1.3.14**；官方支持 macOS / Linux / Windows。

## 📦 三种主流安装方式

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

## 🔧 装完后的两步收尾

```sh
# 1. shell 补全（zsh 为例；bash/fish 用 omp completions bash / fish）
echo 'eval "$(omp completions zsh)"' >> ~/.zshrc

# 2. 首次配置向导：选 provider、登录、装可选依赖
omp setup
```

补全脚本由 omp 基于实时命令元数据自动生成，**永远不会和实际 CLI 脱节**。

## 💻 搭配哪个 IDE？

| 你的主力编辑器 | 推荐打法 | 集成深度 |
| --- | --- | --- |
| **Zed** | Zed 内通过 ACP 协议驱动 `omp acp` | ★★★ 官方原生集成 |
| **VS Code / Cursor** | 内置终端跑 `omp --cwd <项目目录>` | ★★ 终端 TUI（无官方插件） |
| **JetBrains 系** | 内置终端跑 `omp` | ★★ 同上 |
| **纯终端流** | zellij / tmux 分屏 + `omp` | ★★ TUI 本体 |

**Zed 是唯一有官方 IDE 集成的**：通过 ACP（Agent Client Protocol）协议，Zed 里跑的就是终端里那个同一个 agent——直接读你正在看的 buffer、文件写入走编辑器的保存路径、破坏性操作在编辑器里弹一次权限确认。官方原话："No bridge, no plugin, no second brain to keep in sync"（无桥接、无插件、无需同步的第二大脑）。

VS Code / Cursor / JetBrains 目前**没有官方插件**。不过 omp 本身是 TUI 优先设计，在任何编辑器的内置终端里都能完整工作——编辑器负责"看"，omp 负责"改"。

## 🏆 最优结论（怎么选）

1. **装法最优 = Bun 全局安装**：官方推荐方式，升级 `bun update -g` 一步到位
2. **IDE 最优 = Zed + ACP**：目前集成度最高的组合，agent 与编辑器共享同一份上下文
3. **没有 Zed 也别纠结**：VS Code / Cursor + 内置终端 `omp`，零配置即可开工
4. **服务器 / 远程开发**：ssh 上去用 zellij/tmux 挂着 `omp` 跑长任务，断线不丢会话
