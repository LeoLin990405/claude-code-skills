<div align="center">

[![English](https://img.shields.io/badge/Language-English-555555?style=for-the-badge)](README.md) &nbsp; [![中文](https://img.shields.io/badge/语言-中文-2ea44f?style=for-the-badge)](README.zh-CN.md)

# 🧩 Claude Code Skills

**为 [Claude Code](https://docs.anthropic.com/en/docs/claude-code) 精选的 65+ 技能合集**

[![Skills](https://img.shields.io/badge/skills-65%2B-blue?style=for-the-badge)](.)
[![Categories](https://img.shields.io/badge/categories-9-green?style=for-the-badge)](.)
[![Submodules](https://img.shields.io/badge/submodules-9-orange?style=for-the-badge)](.)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

*生产力 · 开发 · 文档 · 研究 · AI · 产品 · 安全 · 设计 · 系统*

</div>

---

## 架构

```
~/.claude/skills/              <-- install.sh 软链到这里
    obsidian-cli/    -> repo/productivity/obsidian-cli   (内置)
    pdf/             -> repo/documents/pdf               (内置)
    ...

claude-code-skills/            <-- 本仓库
├── productivity/        9 个规范可装单元    Obsidian、GWS、NotebookLM
├── development/        12 个规范可装单元    D3.js、R、MCP、前端
├── documents/           7 个规范可装单元    PDF、DOCX、PPTX、XLSX、MinerU
├── research/            5 个规范可装单元    140+ 科学、STEM、笔记、宏观
├── ai-collaboration/    5 个规范可装单元    多 AI 网关、Agent 团队
├── product-management/ 17 个规范可装单元    Lenny's Podcast 产品框架
├── security/            0 个直装单元        仅外部嵌套包
├── design/              7 个规范可装单元    Canvas、主题、GIF
├── system/              5 个规范可装单元    代理、CDP、SVN、通讯、OSS
├── install.sh                      软链安装器
├── CONTRIBUTING.md                 贡献指南
└── LICENSE                         MIT
```

---

## 🚀 快速开始

### 安装全部技能

```bash
git clone --recurse-submodules https://github.com/LeoLin990405/claude-code-skills.git
cd claude-code-skills && ./install.sh
```

### 只装某一类

```bash
./install.sh productivity    # 只装生产力类
```

### 只装规范表面(canonical)

```bash
./install.sh --canonical-only
```

保留各类 toolkit 路由器 + 规范技能,跳过旧兼容 wrapper(如 `all-plan`、provider 专属 CCB shim、`pm-*` 别名)。

| 档位 | 命令 | 含 | 跳过 |
|---|---|---|---|
| 默认 | `./install.sh` | 类路由器 + 规范技能 + 旧兼容 wrapper | 无 |
| 仅规范 | `./install.sh --canonical-only` | 类路由器 + 规范技能 | 旧 CCB shim、`all-plan`、`pm-*` |

打包策略见 [GOVERNANCE.md](GOVERNANCE.md)。

### 装单个技能

```bash
git clone --recurse-submodules https://github.com/LeoLin990405/claude-code-skills.git
ln -s "$PWD/claude-code-skills/productivity/obsidian-cli" ~/.claude/skills/obsidian-cli
```

---

## 📦 分类

下列数量对应 `./install.sh --canonical-only --list`:含类 toolkit 路由器,不含旧兼容 wrapper,外部嵌套包不展平进默认安装表面。

| | 类别 | 规范可装单元 | 亮点 |
|---|---------|--------|-----------|
| 🗂️ | 生产力 Productivity | 9 | Obsidian CLI、NotebookLM、Google Workspace |
| 💻 | 开发 Development | 12 | D3.js、R 分析、MCP、前端 |
| 📄 | 文档 Documents | 7 | PDF、DOCX、PPTX、XLSX、MinerU |
| 🔬 | 研究 Research | 5 | 140+ 科学技能、STEM 建模、研究流程 |
| 🤖 | AI 协作 | 5 | 多 AI 网关、Agent 团队 |
| 📊 | 产品管理 | 17 | Lenny's Podcast —— 86 个可执行 PM 技能 |
| 🔒 | 安全 Security | 0 直装 / 2 外部包 | Trail of Bits(50+)、ffuf |
| 🎨 | 设计 Design | 7 | Canvas 艺术、主题、GIF |
| ⚙️ | 系统 System | 5 | 代理、CDP、SVN、内部通讯 |

各类根目录还暴露从旧 `claude-skills` 伞仓迁来的 toolkit 路由器 `SKILL.md`(ai-collaboration→协调、productivity→知识、development→开发、documents→文档、design→设计、product-management→PM)。旧兼容 wrapper 仍留仓内供旧装法;要最小规范安装表面用 `./install.sh --canonical-only`。

> 完整的每类技能清单(逐个技能 + 描述 + 类型)见 [English README](README.md#-categories)。

---

## 🔗 子模块

9 个上游仓作为 submodule 链接。部分暴露根级 skill 可被 `install.sh` 直接软链,其余是嵌套上游包、保留在树内但不展平进默认安装表面。

```bash
git submodule update --remote --merge                                   # 更新全部子模块
git clone --recurse-submodules https://github.com/LeoLin990405/claude-code-skills.git
```

完整子模块表(仓库 / 类别 / 安装表面)见 [English README](README.md#-submodules)。

---

## 🤝 贡献

见 [CONTRIBUTING.md](CONTRIBUTING.md):如何加技能、报 bug、提 PR。

## 📄 许可

原创技能以 [MIT](LICENSE) 发布。子模块技能保留其上游原始许可。
