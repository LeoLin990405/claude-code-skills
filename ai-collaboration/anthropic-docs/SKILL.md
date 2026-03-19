---
name: anthropic-docs
description: Anthropic 官方文档知识库，包含 Claude 模型、API、Claude Code、工程博客、研究论文等完整参考。当用户询问 Anthropic/Claude 相关问题、API 使用、模型选择、Claude Code 功能时使用。
triggers:
  - anthropic
  - claude api
  - claude code
  - claude 模型
  - opus
  - sonnet
  - haiku
  - mcp
  - subagent
  - skills
---

# Anthropic 官方文档知识库

> 整理日期: 2026-01-30
> 来源: https://www.anthropic.com/

## 快速参考

### 模型选择指南
| 模型 | 定位 | 价格 (输入/输出 per M tokens) | 适用场景 |
|------|------|-------------------------------|----------|
| **Opus 4.5** | 最智能 | $5/$25 | 复杂推理、企业项目、高难度任务 |
| **Sonnet 4.5** | 最佳编码 | $3/$15 | 代理任务、软件开发、日常使用 |
| **Haiku 4.5** | 最快速 | $1/$5 | 实时应用、高并发、成本敏感 |

### API 快速开始
```bash
export ANTHROPIC_API_KEY='your-key'
curl https://api.anthropic.com/v1/messages \
  -H "x-api-key: $ANTHROPIC_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "content-type: application/json" \
  -d '{"model":"claude-sonnet-4-5","max_tokens":1000,"messages":[{"role":"user","content":"Hello"}]}'
```

### 重要链接
- 开发者文档: https://platform.claude.com/docs
- API Console: https://platform.claude.com
- Claude Code 文档: https://code.claude.com/docs
- Anthropic Academy: https://anthropic.skilljar.com

---

## 详细文档索引

更多详细内容请参考以下文件：

- [模型详情](models.md) - Opus/Sonnet/Haiku 4.5 完整规格
- [API 指南](api-guide.md) - API 使用与代码示例
- [Claude Code](claude-code.md) - Claude Code 完整文档
- [工程博客](engineering-blog.md) - 14篇技术博客详细笔记
- [研究论文](research-papers.md) - 9篇研究论文详细笔记
- [安全政策](safety-policy.md) - 宪法、透明度、RSP

---

## Claude 4.5 新功能速览

### 1. Effort 参数 (Extended Thinking)
```python
response = client.messages.create(
    model="claude-sonnet-4-5-20250514",
    max_tokens=16000,
    thinking={
        "type": "enabled",
        "budget_tokens": 10000  # low/medium/high 或具体数值
    },
    messages=[{"role": "user", "content": "复杂问题..."}]
)
```

### 2. Tool Search Tool
按需发现工具，节省 85% token 使用量
```json
{"type": "tool_search_tool_regex_20251119", "name": "tool_search_tool_regex"}
```

### 3. Programmatic Tool Calling
Claude 通过 Python 代码编排工具，Token 减少 37%

### 4. Memory Tool
跨会话持久化记忆

### 5. Context Editing
用户可编辑上下文窗口内容

---

## Claude Code 核心功能

### 安装
```bash
# macOS/Linux/WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
```

### 常用命令
| 命令 | 功能 |
|------|------|
| `/clear` | 重置上下文 |
| `/compact` | 压缩上下文 |
| `/rewind` | 恢复检查点 |
| `/agents` | 管理子代理 |
| `/mcp` | 管理 MCP 服务器 |
| `/init` | 生成 CLAUDE.md |

### 快捷键
| 快捷键 | 功能 |
|--------|------|
| `Esc` | 停止当前操作 |
| `Esc + Esc` | 打开 rewind 菜单 |
| `Shift+Tab` | 切换权限模式 |
| `Ctrl+O` | 切换详细模式 |
| `Option+T` | 切换思考模式 |

### MCP 服务器配置
```bash
# HTTP 服务器
claude mcp add --transport http <name> <url>

# 本地 stdio 服务器
claude mcp add --transport stdio --env KEY=value <name> -- npx -y <package>

# 管理
claude mcp list
claude mcp remove <name>
```

### 子代理 (Subagents)
内置子代理：
- **Explore**: Haiku 模型，只读工具，用于代码库探索
- **Plan**: 继承模型，只读工具，用于计划模式研究
- **general-purpose**: 继承模型，所有工具，用于复杂任务

### Skills 技能
```yaml
---
name: my-skill
description: 技能描述
---
技能指令内容...
```

存储位置：
- 个人: `~/.claude/skills/<name>/SKILL.md`
- 项目: `.claude/skills/<name>/SKILL.md`

---

## 工程博客精华

### Agent 开发核心原则
1. **简单性**: 保持设计简单，避免过度工程
2. **透明性**: 明确显示规划步骤
3. **ACI 设计**: 像投入 HCI 一样投入 Agent-Computer Interface 设计

### 六种工作流模式
| 模式 | 描述 | 适用场景 |
|------|------|----------|
| Prompt Chaining | 序列步骤 | 可清晰分解的任务 |
| Routing | 输入分类导向 | 有明确类别的任务 |
| Parallelization | 并行运行 | 独立子任务 |
| Orchestrator-Workers | 动态分解委派 | 复杂代码修改 |
| Evaluator-Optimizer | 循环评估反馈 | 有明确评估标准 |
| Agents | 自主规划操作 | 开放式问题 |

### 上下文工程核心
> "find the smallest possible set of high-signal tokens that maximize the likelihood of some desired outcome"

长时程任务策略：
1. **压缩**: 总结内容并用摘要重新启动
2. **结构化笔记**: 定期写入持久内存
3. **子智能体架构**: 主智能体协调，子智能体处理聚焦任务

---

## 研究论文要点

### AI 辅助对编程技能的影响
- AI 组测验成绩 50%，手工编码组 67%（相差 17%）
- 最大差距在调试问题上
- 使用 AI 的**方式**影响信息保留

### Constitutional Classifiers++
- 越狱成功率从 86% 降至 4.4%
- 计算开销仅约 1%
- 误报率降至 0.05%

### Claude 新宪法四大优先级
1. **Broadly safe**: 不破坏人类监督机制
2. **Broadly ethical**: 诚实行事，避免伤害
3. **Compliant with guidelines**: 遵循 Anthropic 指南
4. **Genuinely helpful**: 真正有帮助

---

## 安全政策

### AI 安全级别 (ASL)
| 级别 | 说明 |
|------|------|
| ASL-1 | 基础安全措施 |
| ASL-2 | 当前所有模型运行级别 |
| ASL-3 | 高级安全措施 (部分模型) |
| ASL-4+ | 最高级别安全措施 |

### 负责任扩展政策 (RSP) 核心承诺
> 在未实施充分的保障措施之前，绝不训练或部署高风险模型

能力阈值（触发更高安全措施的红线）：
1. 自主 AI 研发
2. CBRN 武器协助
