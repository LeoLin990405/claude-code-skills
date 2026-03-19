# Claude Code 详细文档

> 来源: https://code.claude.com/docs
> 整理日期: 2026-01-30

---

## 1. 概述 (Overview)

### 核心定位
Claude Code 是 Anthropic 的 agentic 编码工具，运行在终端中，帮助将想法快速转化为代码。

### 安装方式

**原生安装 (推荐)**
```bash
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
```

**其他方式**
- Homebrew: `brew install --cask claude-code`
- WinGet: `winget install Anthropic.ClaudeCode`

### 核心功能
| 功能 | 描述 |
|------|------|
| 从描述构建功能 | 用自然语言描述需求，Claude 规划、编写、验证代码 |
| 调试和修复问题 | 描述 bug 或粘贴错误信息，Claude 分析并修复 |
| 导航任何代码库 | 询问代码库问题，获得深思熟虑的答案 |
| 自动化繁琐任务 | 修复 lint 问题、解决合并冲突、编写发布说明 |

### 多平台支持
- **终端 (CLI)**: 核心体验，运行 `claude` 开始
- **Web 版**: claude.ai/code，无需本地设置
- **桌面应用**: 独立应用，支持 diff 审查和并行会话
- **VS Code**: 原生扩展，内联 diff 和 @-mentions
- **JetBrains IDEs**: 插件支持
- **GitHub Actions**: 自动化代码审查和 issue 分类
- **GitLab CI/CD**: 事件驱动的 MR 自动化
- **Slack**: 在 Slack 中 @Claude 路由编码任务
- **Chrome**: 连接浏览器进行实时调试

---

## 2. 常见工作流程 (Common Workflows)

### 理解新代码库
```
> give me an overview of this codebase
> explain the main architecture patterns used here
> what are the key data models?
> how is authentication handled?
```

### 查找相关代码
```
> find the files that handle user authentication
> how do these authentication files work together?
> trace the login process from front-end to database
```

### 高效修复 Bug
```
> I'm seeing an error when I run npm test
> suggest a few ways to fix the @ts-ignore in user.ts
> update user.ts to add the null check you suggested
```

### 重构代码
```
> find deprecated API usage in our codebase
> suggest how to refactor utils.js to use modern JavaScript features
> refactor utils.js to use ES2024 features while maintaining the same behavior
> run tests for the refactored code
```

### Plan Mode (计划模式)

**何时使用**
- 多步骤实现
- 代码探索
- 交互式开发

**使用方法**
- 会话中切换: `Shift+Tab`
- 启动时: `claude --permission-mode plan`
- 无头模式: `claude --permission-mode plan -p "分析认证系统"`

### 使用子代理 (Subagents)
```
> /agents                    # 查看可用子代理
> review my recent code changes for security issues
> use the code-reviewer subagent to check the auth module
```

### 处理测试
```
> find functions in NotificationsService.swift that are not covered by tests
> add tests for the notification service
> add test cases for edge conditions in the notification service
> run the new tests and fix any failures
```

### 创建 Pull Request
```
> /commit-push-pr           # 一键提交、推送、创建 PR
> summarize the changes I've made to the authentication module
> create a pr
```

### 使用图片
- 拖放图片到 Claude Code 窗口
- 复制图片后 `Ctrl+V` 粘贴
- 提供图片路径: "Analyze this image: /path/to/image.png"

### 引用文件和目录
```
> Explain the logic in @src/utils/auth.js    # 引用单个文件
> What's the structure of @src/components?    # 引用目录
> Show me the data from @github:repos/owner/repo/issues  # MCP 资源
```

### Extended Thinking (扩展思考)
- 默认启用，最多 31,999 tokens 用于推理
- 切换: `Option+T` (macOS) 或 `Alt+T` (Windows/Linux)
- 查看思考过程: `Ctrl+O` 切换详细模式

### 恢复会话
```bash
claude --continue    # 继续最近的对话
claude --resume      # 选择要恢复的会话
```

### Git Worktrees 并行会话
```bash
git worktree add ../project-feature-a -b feature-a
cd ../project-feature-a
claude
```

### Unix 风格使用
```bash
# 作为 linter
claude -p 'you are a linter. please look at the changes vs. main and report any issues'

# 管道数据
cat build-error.txt | claude -p 'concisely explain the root cause' > output.txt

# 输出格式
claude -p 'analyze this code' --output-format json
claude -p 'parse this log' --output-format stream-json
```

---

## 3. MCP (Model Context Protocol)

### 核心概念
MCP 是 AI 工具集成的开源标准，让 Claude Code 连接到外部工具和数据源。

### 可实现的功能
- 从 issue tracker 实现功能
- 分析监控数据
- 查询数据库
- 集成设计稿
- 自动化工作流

### 安装 MCP 服务器

**HTTP 服务器 (推荐)**
```bash
claude mcp add --transport http <name> <url>
claude mcp add --transport http notion https://mcp.notion.com/mcp
```

**SSE 服务器 (已弃用)**
```bash
claude mcp add --transport sse <name> <url>
```

**本地 stdio 服务器**
```bash
claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable \
  -- npx -y airtable-mcp-server
```

### 管理服务器
```bash
claude mcp list              # 列出所有服务器
claude mcp get github        # 获取特定服务器详情
claude mcp remove github     # 移除服务器
/mcp                         # 在 Claude Code 中检查状态
```

### 作用域 (Scope)
| 作用域 | 存储位置 | 适用范围 |
|--------|----------|----------|
| local (默认) | ~/.claude.json | 当前项目，仅自己可见 |
| project | .mcp.json | 团队共享，提交到版本控制 |
| user | ~/.claude.json | 所有项目，仅自己可见 |

### 实际示例

**Sentry 错误监控**
```bash
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
> /mcp  # 认证
> "What are the most common errors in the last 24 hours?"
```

**GitHub 代码审查**
```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/
> "Review PR #456 and suggest improvements"
```

**PostgreSQL 数据库**
```bash
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub \
  --dsn "postgresql://readonly:pass@prod.db.com:5432/analytics"
> "What's our total revenue this month?"
```

### MCP Tool Search
当 MCP 工具定义超过上下文窗口 10% 时自动启用，按需动态加载工具。

```bash
ENABLE_TOOL_SEARCH=auto:5 claude  # 自定义 5% 阈值
ENABLE_TOOL_SEARCH=false claude   # 禁用
```

---

## 4. 子代理 (Subagents)

### 核心概念
子代理是专门处理特定任务的 AI 助手，在独立上下文窗口中运行，有自定义系统提示、特定工具访问和独立权限。

### 内置子代理

| 子代理 | 模型 | 工具 | 用途 |
|--------|------|------|------|
| Explore | Haiku | 只读工具 | 文件发现、代码搜索、代码库探索 |
| Plan | 继承 | 只读工具 | 计划模式下的代码库研究 |
| general-purpose | 继承 | 所有工具 | 复杂研究、多步骤操作、代码修改 |

### 创建自定义子代理

**使用 /agents 命令**
```
/agents → Create new agent → User-level → Generate with Claude
```

**手动创建文件**
```markdown
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep
model: sonnet
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```

### 存储位置
| 位置 | 作用域 | 优先级 |
|------|--------|--------|
| --agents CLI 标志 | 当前会话 | 1 (最高) |
| .claude/agents/ | 当前项目 | 2 |
| ~/.claude/agents/ | 所有项目 | 3 |
| Plugin agents/ | 插件启用处 | 4 (最低) |

### 配置字段
| 字段 | 必需 | 描述 |
|------|------|------|
| name | 是 | 唯一标识符 |
| description | 是 | Claude 何时委托给此子代理 |
| tools | 否 | 可用工具，省略则继承所有 |
| disallowedTools | 否 | 禁止的工具 |
| model | 否 | sonnet, opus, haiku, inherit |
| permissionMode | 否 | default, acceptEdits, dontAsk, bypassPermissions, plan |
| skills | 否 | 启动时加载的技能 |
| hooks | 否 | 生命周期钩子 |

### 前台/后台运行
- **前台**: 阻塞主对话直到完成
- **后台**: 并发运行，可继续工作
- `Ctrl+B`: 将运行中的任务转到后台

---

## 5. Skills (技能)

### 核心概念
Skills 扩展 Claude 的能力，创建 `SKILL.md` 文件，Claude 在相关时自动使用，或用 `/skill-name` 直接调用。

### 创建技能

**目录结构**
```
my-skill/
├── SKILL.md           # 主指令 (必需)
├── template.md        # 模板
├── examples/
│   └── sample.md      # 示例输出
└── scripts/
    └── validate.sh    # 脚本
```

**SKILL.md 示例**
```yaml
---
name: explain-code
description: Explains code with visual diagrams and analogies
---

When explaining code, always include:
1. **Start with an analogy**: Compare the code to something from everyday life
2. **Draw a diagram**: Use ASCII art to show the flow
3. **Walk through the code**: Explain step-by-step
4. **Highlight a gotcha**: Common mistake or misconception
```

### 存储位置
| 位置 | 路径 | 适用范围 |
|------|------|----------|
| Enterprise | 托管设置 | 组织所有用户 |
| Personal | ~/.claude/skills/<name>/SKILL.md | 所有项目 |
| Project | .claude/skills/<name>/SKILL.md | 仅当前项目 |
| Plugin | <plugin>/skills/<name>/SKILL.md | 插件启用处 |

### Frontmatter 字段
| 字段 | 描述 |
|------|------|
| name | 显示名称，成为 /slash-command |
| description | 用途描述，Claude 用于决定何时使用 |
| argument-hint | 自动完成时显示的参数提示 |
| disable-model-invocation | true 时仅用户可调用 |
| user-invocable | false 时从 / 菜单隐藏 |
| allowed-tools | 技能激活时可用的工具 |
| model | 使用的模型 |
| context | 设为 fork 在子代理中运行 |
| agent | context: fork 时使用的子代理类型 |
| hooks | 技能生命周期钩子 |

### 字符串替换
| 变量 | 描述 |
|------|------|
| $ARGUMENTS | 调用时传递的所有参数 |
| $ARGUMENTS[N] | 按索引访问特定参数 |
| $N | $ARGUMENTS[N] 的简写 |
| ${CLAUDE_SESSION_ID} | 当前会话 ID |

### 动态上下文注入
```yaml
---
name: pr-summary
description: Summarize changes in a pull request
context: fork
agent: Explore
---

## Pull request context
- PR diff: !`gh pr diff`
- PR comments: !`gh pr view --comments`
- Changed files: !`gh pr diff --name-only`
```

---

## 6. 最佳实践 (Best Practices)

### 核心约束
> Claude 的上下文窗口填充快，性能随填充而下降。

### 最高杠杆建议
**给 Claude 验证自己工作的方式**：测试、截图、预期输出。

| 策略 | 之前 | 之后 |
|------|------|------|
| 提供验证标准 | "实现验证邮箱的函数" | "写 validateEmail 函数。测试用例: user@example.com 为 true, invalid 为 false。实现后运行测试" |
| 视觉验证 UI | "让仪表板更好看" | "[粘贴截图] 实现这个设计。截图结果并与原图比较。列出差异并修复" |
| 解决根本原因 | "构建失败了" | "构建失败，错误: [粘贴错误]。修复并验证构建成功。解决根本原因，不要抑制错误" |

### 推荐工作流
1. **探索**: Plan Mode 读取文件
2. **计划**: 创建详细实现计划
3. **实现**: Normal Mode 编码
4. **提交**: 创建 PR

### CLAUDE.md 最佳实践

**应包含**
- Claude 无法猜测的 Bash 命令
- 与默认不同的代码风格规则
- 测试指令和首选测试运行器
- 仓库礼仪 (分支命名、PR 约定)
- 项目特定的架构决策
- 开发环境怪癖 (必需的环境变量)
- 常见陷阱或非显而易见的行为

**不应包含**
- Claude 可以通过阅读代码弄清楚的内容
- Claude 已知的标准语言约定
- 详细的 API 文档 (改为链接)
- 经常变化的信息
- 长篇解释或教程
- 代码库的逐文件描述
- 不言自明的做法如"写干净的代码"

### 会话管理
- `/clear`: 在不相关任务之间重置上下文
- `/rewind` 或 `Esc + Esc`: 恢复检查点
- `/compact <instructions>`: 自定义压缩
- `--continue`: 恢复最近会话
- `--resume`: 选择要恢复的会话

### 使用子代理进行调查
```
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

### 常见失败模式

| 模式 | 问题 | 解决方案 |
|------|------|----------|
| 厨房水槽会话 | 一个任务开始，问不相关的问题，再回到第一个任务 | 不相关任务之间 `/clear` |
| 反复纠正 | Claude 做错，纠正，还是错，再纠正 | 两次失败后 `/clear` 并写更好的初始提示 |
| 过度指定的 CLAUDE.md | 太长，Claude 忽略一半 | 无情修剪，转换为钩子 |
| 信任后验证差距 | Claude 产生看起来正确但不处理边缘情况的实现 | 始终提供验证 |
| 无限探索 | 要求 Claude "调查"某事但不限定范围 | 缩小调查范围或使用子代理 |

### 扩展和自动化

**无头模式**
```bash
claude -p "Explain what this project does"
claude -p "List all API endpoints" --output-format json
claude -p "Analyze this log file" --output-format stream-json
```

**并行会话**
- Claude Desktop: 可视化管理多个本地会话
- Claude Code on the web: 在 Anthropic 安全云基础设施上运行

**跨文件扇出**
```bash
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

---

## 7. 快捷键参考

| 快捷键 | 功能 |
|--------|------|
| `Esc` | 停止 Claude 当前操作 |
| `Esc + Esc` | 打开 rewind 菜单 |
| `Shift+Tab` | 切换权限模式 |
| `Ctrl+G` | 在编辑器中打开计划 |
| `Ctrl+O` | 切换详细模式 |
| `Ctrl+B` | 将任务转到后台 |
| `Option+T` / `Alt+T` | 切换思考模式 |
| `Ctrl+V` | 粘贴图片 |

---

## 8. 常用命令

| 命令 | 功能 |
|------|------|
| `/help` | 获取帮助 |
| `/clear` | 重置上下文 |
| `/compact` | 压缩上下文 |
| `/rewind` | 恢复检查点 |
| `/resume` | 恢复会话 |
| `/rename` | 重命名会话 |
| `/agents` | 管理子代理 |
| `/mcp` | 管理 MCP 服务器 |
| `/permissions` | 配置权限 |
| `/sandbox` | 启用沙箱 |
| `/init` | 生成 CLAUDE.md |
| `/context` | 查看上下文使用 |
| `/commit-push-pr` | 一键提交推送创建 PR |

