# Daily Update Checker - 使用示例

## 示例 1: 手动检查更新

**用户:** 帮我检查本地 CLI 工具的更新

**Claude:**
```
我来帮你检查所有已安装的 CLI 工具更新...

运行检查脚本...
```

Claude 会执行 `check_updates.sh` 脚本并生成报告。

---

## 示例 2: 设置每日自动检查

**用户:** 帮我设置每天自动检查 CLI 更新

**Claude:**
```
我来帮你设置定时任务...

1. 运行 setup_cron.sh
2. 选择检查时间（默认早上 9:00）
3. 确认设置
4. 可选择立即运行一次
```

---

## 示例 3: 查看更新报告

**用户:** 查看最近的更新报告

**Claude:**
```
我来查看最近的更新报告...

[显示报告文件列表]
[显示最新报告内容]
```

---

## 示例 4: 手动运行检查

直接在终端运行：

```bash
# 运行检查
bash ~/.claude/skills/daily-update-checker/scripts/check_updates.sh

# 查看报告
ls -la ~/.claude/skills/daily-update-checker/reports/

# 查看日志
tail -f ~/.claude/skills/daily-update-checker/update.log
```

---

## 支持的 CLI 工具

### AI Agent CLI
- claude (Claude Code)
- codex (OpenAI Codex)
- gemini (Google Gemini)
- kimi (Moonshot Kimi)
- qwen (Alibaba Qwen)
- deepseek (DeepSeek)

### 开发工具
- Homebrew 包
- npm 全局包
- git, python3, node, docker

---

## 报告位置

- **报告文件**: `~/.claude/skills/daily-update-checker/reports/`
- **日志文件**: `~/.claude/skills/daily-update-checker/update.log`
- **脚本位置**: `~/.claude/skills/daily-update-checker/scripts/`
