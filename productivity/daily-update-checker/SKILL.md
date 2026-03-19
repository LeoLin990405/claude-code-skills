---
name: daily-update-checker
description: 每天自动检查本地安装的 AI Agent CLI 工具和其他开发工具的更新。支持检查 Homebrew、npm、pip 等包管理器中的工具更新，并生成更新报告。使用场景：(1) 用户想要检查所有 CLI 工具的更新状态，(2) 需要生成可读的更新报告，(3) 设置定时检查任务。
---

# Daily Update Checker

每天自动检查本地安装的 AI Agent CLI 工具和其他开发工具的更新。

## 功能

- 检查 Homebrew 安装的 CLI 工具更新
- 检查 npm 全局安装的包更新
- 检查 pip 安装的包更新
- 生成结构化的更新报告
- 支持定时任务设置

## 支持的 CLI 工具

### AI Agent CLI
- claude (Claude Code)
- codex (OpenAI Codex)
- gemini (Google Gemini)
- kimi (Moonshot Kimi)
- qwen (Alibaba Qwen)
- deepseek (DeepSeek)
- opencode (OpenCode)
- iflow (iFlow)

### 开发工具
- brew (Homebrew)
- npm
- pip
- docker
- git
- python
- node

## 使用方法

### 手动检查更新

```bash
# 检查所有工具更新
ccb-cli claude "检查本地 CLI 工具更新"

# 或运行检查脚本
bash ~/.claude/skills/daily-update-checker/scripts/check_updates.sh
```

### 设置定时任务（macOS）

```bash
# 创建定时任务，每天上午9点检查
bash ~/.claude/skills/daily-update-checker/scripts/setup_cron.sh
```

## 更新报告格式

报告包含以下信息：
- 检查时间
- 每个 CLI 工具的当前版本
- 可用更新版本
- 更新建议
- 更新命令

## 脚本说明

### check_updates.sh
主检查脚本，执行所有更新检查并生成报告。

### setup_cron.sh
设置定时任务的脚本，将检查任务添加到 crontab。

## 示例

**检查所有更新：**
```
用户：检查我本地的 CLI 工具有没有更新
Claude：我来帮你检查所有已安装的 CLI 工具更新...
[运行检查脚本]
[生成报告]
```

**设置每日检查：**
```
用户：帮我设置每天自动检查更新
Claude：我来帮你设置定时任务...
[运行 setup_cron.sh]
[确认设置成功]
```
