# CCB Unified - 统一 CCB + Subagent 集成平台

**版本**: v1.0
**更新时间**: 2026-02-06

## 简介

CCB Unified 是一个统一的 CCB + Subagent 集成平台，通过 Gateway API 调度 9 个 AI Provider，结合 Claude Code 的 Subagent 系统，实现分布式 AI 协作。

## 架构

```
Claude (编排)
     ↓
 Subagents (Explore/Bash/Plan)
     ↓
Gateway API (localhost:8765)
     ↓
9 AI Providers (Kimi/Qwen/DeepSeek/Codex/Gemini/...)
```

## 核心能力

- ✅ **异步非阻塞** - 通过 Gateway API 实现
- ✅ **Subagent 并行** - Claude Code 的 Task tool
- ✅ **智能路由** - 根据任务类型自动选择 Provider
- ✅ **记忆系统** - 双系统记忆 + 启发式检索
- ✅ **模块化** - 6 个子 skills 处理不同场景

## 子 Skills

| Skill | 文件 | 用途 | 整合来源 |
|-------|------|------|----------|
| **async** | `subskills/async.md` | 异步调用管理 | 新增 |
| **parallel** | `subskills/parallel.md` | 并行多 AI 协作 | 新增 |
| **research** | `subskills/research.md` | 深度研究（Subagent + CCB） | 新增 |
| **workflow** | `subskills/workflow.md` | 工作流自动化 | 新增 |
| **memory** | `subskills/memory.md` | 记忆系统操作 | 新增 |
| **benchmark** | `subskills/benchmark.md` | 性能基准测试 | 新增 |
| **discussion** | `subskills/discussion.md` | 多 AI 协作讨论 | `all-plan` |
| **stem** | `subskills/stem.md` | STEM 学术建模（8 模型） | `stem-modeling` |
| **macro** | `subskills/macro.md` | 宏观研究（8 AI 串行） | `macro-research-ccb` |

## 快速开始

### 前提条件

1. **Gateway 运行中**:
   ```bash
   cd ~/.local/share/codex-dual
   python3 -m lib.gateway.gateway_server --port 8765
   ```

2. **检查状态**:
   ```bash
   curl http://localhost:8765/health
   ```

### 基本使用

```bash
# 调用统一 skill
/ccb-unified "创建一个 React 计数器组件"

# Claude 会自动:
# 1. 分析任务类型（前端）
# 2. 选择最佳 Provider（gemini 3f）
# 3. 异步提交
# 4. 返回结果
```

### 使用子 skills

```bash
# 异步提交
ccb-submit kimi "详细分析这个架构"

# 并行多 AI
ccb-cli kimi,qwen,deepseek "如何优化性能？"

# 深度研究（Explore + CCB）
# [通过 Claude 请求触发]

# 工作流自动化
bash ~/.claude/skills/ccb-unified/examples/workflow_example.sh

# 记忆检索
ccb-mem search-scored "React Hooks"

# 性能测试
bash ~/.claude/skills/ccb-unified/examples/benchmark_example.sh
```

## 配置文件

**位置**: `config.json`

主要配置项：
- Gateway URL 和超时
- Provider 分组
- Subagent 设置
- 各子 skill 的默认参数
- 智能路由规则

## 文件结构

```
ccb-unified/
├── SKILL.md              # 主 skill（本文件的详细版）
├── README.md             # 本文件
├── config.json           # 配置文件
├── subskills/            # 子 skills
│   ├── async.md
│   ├── parallel.md
│   ├── research.md
│   ├── workflow.md
│   ├── memory.md
│   └── benchmark.md
└── examples/             # 示例脚本
    ├── async_example.sh
    ├── parallel_example.sh
    ├── research_example.sh
    ├── workflow_example.sh
    └── benchmark_example.sh
```

## 使用场景决策

| 场景 | 推荐子 skill | 说明 |
|------|-------------|------|
| 长时间任务 | async | 避免阻塞 |
| 多 AI 对比 | parallel | 获得多角度答案 |
| 代码库研究 | research | Explore + 多 AI 分析 |
| 自动化流程 | workflow | Bash + AI 决策 |
| 搜索历史 | memory | 启发式检索 |
| 性能对比 | benchmark | Provider 基准测试 |
| 多 AI 讨论 | discussion | 架构设计、技术选型 |
| STEM 研究 | stem | 学术论文、数学推导 |
| 宏观研究 | macro | A 股市场分析 |

## 智能路由

当用户没有指定 Provider 时，自动选择最佳 Provider：

- **前端** → gemini 3f
- **算法** → codex o3
- **中文** → kimi
- **代码** → qwen
- **快速问答** → kimi

## 整合的原有 Skills

**ccb-unified** 完整整合了以下 CCB 相关 skills：

| 原 Skill | 整合方式 | 新位置 | 增强点 |
|---------|---------|-------|--------|
| `ccb` | 作为基础 | 核心架构 | + Subagent + 异步优先 |
| `ask` | 简化版 | async/parallel | + 智能路由 + 并行 |
| `all-plan` | 完整整合 | discussion | + Gateway API + 监控 |
| `stem-modeling` | 完整整合 | stem | + ccb-submit + Subagent |
| `macro-research-ccb` | 完整整合 | macro | + 监控 + 追踪表 |

**向后兼容**：原有 skills 的用户可以直接使用 ccb-unified，功能完全兼容并增强。

## 最佳实践

1. **保持 Gateway 运行** - 确保 http://localhost:8765 可访问
2. **异步优先** - 除非是简单快速任务
3. **选择合适的子 skill** - 根据任务类型
4. **利用 Subagent** - 复杂任务交给 Subagent
5. **并行处理** - 多个独立任务同时提交
6. **记忆管理** - 定期运行 consolidate
7. **监控性能** - 定期查看 Web UI 和成本

## 故障排查

### Gateway 未运行

```bash
✖ Gateway 未运行

启动命令:
  cd ~/.local/share/codex-dual && python3 -m lib.gateway.gateway_server --port 8765
```

### Provider 超时

```bash
# 切换到更快的 Provider
ccb-cli kimi "问题"  # 替代慢的 Codex/Gemini
```

### Subagent 失败

```bash
# 检查 Subagent 任务状态
/tasks list
```

## 更新日志

### v1.0 (2026-02-06)
- ✅ 统一 CCB + Subagent 架构
- ✅ **9 个子 skills** 模块化设计（async, parallel, research, workflow, memory, benchmark, discussion, stem, macro）
- ✅ **完整整合** 5 个原有 CCB skills（ccb, ask, all-plan, stem-modeling, macro-research-ccb）
- ✅ 智能路由和自动选择
- ✅ 完整的错误处理和降级策略
- ✅ 统一配置文件
- ✅ Web UI 和监控支持

## 相关文档

- **主 Skill**: `SKILL.md` - 完整说明
- **Gateway API**: `~/.local/share/codex-dual/docs/GATEWAY_API.md`
- **记忆系统**: `~/.local/share/codex-dual/docs/MEMORY_V2.md`
- **Subagent**: Claude Code 官方文档

## License

MIT

---

*CCB Unified v1.0 - Distributed AI Collaboration Platform*
