---
name: ccb-unified
description: 统一 CCB + Subagent 集成平台 v1.0。通过 Gateway API 调度 9 个 AI Provider，结合 Claude Code Subagent 系统，实现分布式 AI 协作。支持异步调用、并行执行、智能路由、记忆系统。包含 9 个子 skills：async, parallel, research, workflow, memory, benchmark, discussion, stem, macro。整合了原有的 ccb, ask, all-plan, stem-modeling, macro-research-ccb skills。
triggers:
  - ccb unified
  - ccb subagent
  - distributed ai
  - 分布式协作
  - 多ai协作
  - 集成ccb
---

# CCB Unified - 统一 CCB + Subagent 集成平台 v1.0

## 架构概览

```
┌─────────────────────────────────────────────────────────────────────┐
│                     CCB Unified Platform                            │
│                                                                     │
│  ┌───────────────────────────────────────────────────────────────┐  │
│  │              Claude Code (Orchestrator)                        │  │
│  │              • 任务规划                                         │  │
│  │              • Subagent 调度                                    │  │
│  │              • 结果整合                                         │  │
│  └───────────────────────┬───────────────────────────────────────┘  │
│                          │                                          │
│       ┌──────────────────┼──────────────────┐                       │
│       │                  │                  │                       │
│       ▼                  ▼                  ▼                       │
│  ┌─────────┐      ┌─────────┐      ┌─────────┐                     │
│  │ Explore │      │  Plan   │      │  Bash   │                     │
│  │Subagent │      │Subagent │      │Subagent │                     │
│  └────┬────┘      └────┬────┘      └────┬────┘                     │
│       │                │                │                           │
│       │      ┌─────────▼─────────┐      │                           │
│       │      │  Gateway API       │      │                           │
│       │      │ localhost:8765     │      │                           │
│       └──────►                    ◄──────┘                           │
│              └─────────┬─────────┘                                  │
│                        │                                            │
│    ┌────┬────┬────┬───┼───┬────┬────┬────┬────┐                    │
│    ▼    ▼    ▼    ▼   ▼   ▼    ▼    ▼    ▼    ▼                    │
│  Kimi Qwen DeepS Cdex Gemi iFlo OpCd Clau Droid                    │
│   🚀   🚀   ⚡   🐢   🐢   ⚡   ⚡   ⚡    ⚡                          │
└─────────────────────────────────────────────────────────────────────┘
```

**核心能力：**
- **异步非阻塞** - 通过 Gateway API 实现
- **Subagent 并行** - Claude Code 的 Task tool
- **智能路由** - 根据任务类型选择最佳 Provider
- **记忆系统** - 双系统记忆 + 启发式检索
- **模块化** - 6 个子 skills 处理不同场景

---

## 子 Skills 架构

```
ccb-unified/
├── SKILL.md (本文件 - 主入口)
├── subskills/
│   ├── async.md           # 异步调用管理
│   ├── parallel.md        # 并行多 AI 协作
│   ├── research.md        # 深度研究（Subagent + CCB）
│   ├── workflow.md        # 工作流自动化
│   ├── memory.md          # 记忆系统操作
│   ├── benchmark.md       # 性能基准测试
│   ├── discussion.md      # 多 AI 协作讨论（整合 all-plan）
│   ├── stem.md            # STEM 学术建模（整合 stem-modeling）
│   └── macro.md           # 宏观研究（整合 macro-research-ccb）
└── examples/
    ├── async_example.sh
    ├── parallel_example.sh
    ├── research_example.sh
    ├── discussion_example.sh
    ├── stem_example.sh
    └── macro_example.sh
```

---

## 使用场景决策树

```
用户请求
    │
    ├─ 需要深度探索代码库？
    │  └─> 使用 /ccb-research（Explore Subagent + CCB）
    │
    ├─ 需要多个 AI 同时工作？
    │  └─> 使用 /ccb-parallel（异步并行）
    │
    ├─ 需要长时间任务不阻塞？
    │  └─> 使用 /ccb-async（异步提交）
    │
    ├─ 需要实现自动化流程？
    │  └─> 使用 /ccb-workflow（Bash Subagent + CCB）
    │
    ├─ 需要搜索历史记忆？
    │  └─> 使用 /ccb-memory（记忆检索）
    │
    └─ 需要对比 Provider 性能？
       └─> 使用 /ccb-benchmark（性能测试）
```

---

## 主入口：ccb-unified

### 快速开始

```bash
# 检查环境
/ccb-unified check

# 智能路由（自动选择最佳 Provider）
/ccb-unified "创建一个 React 计数器组件"

# 指定 Provider
/ccb-unified kimi "解释递归"

# 带 Agent 角色
/ccb-unified codex o3 -a reviewer "审查代码"
```

### 工作流程

```
1. 用户输入任务
2. Claude 分析任务类型
3. 决定是否需要 Subagent
4. 选择合适的子 skill
5. 执行并返回结果
```

---

---

## 子 Skills 详解

### 基础调用类 (3个)

#### Skill 1: ccb-async (异步调用管理)

**文件**: `subskills/async.md`

### 用途
处理需要长时间运行的任务，避免阻塞主会话。

### 触发条件
- 任务预计耗时 > 30 秒
- 需要同时提交多个独立任务
- 用户明确要求异步执行

### 使用方法

```bash
# 异步提交
/ccb-async submit kimi "详细分析这个架构设计"
# → 返回 request_id

# 批量提交
/ccb-async batch "问题1" "问题2" "问题3"

# 查询状态
/ccb-async status <request_id>

# 获取结果
/ccb-async get <request_id>

# 列出所有待处理
/ccb-async pending
```

### 实现原理

```bash
# 通过 Gateway API 异步提交
curl -X POST http://localhost:8765/api/v1/submit \
  -H "Content-Type: application/json" \
  -d '{
    "provider": "kimi",
    "message": "任务内容",
    "agent_role": "sisyphus"
  }'
```

---

#### Skill 2: ccb-parallel (并行多 AI 协作)

**文件**: `subskills/parallel.md`

### 用途
同时向多个 AI Provider 提问，获得多角度答案。

### 触发条件
- 需要多个 AI 的不同观点
- 需要快速获得多种方案
- 对比不同 AI 的能力

### 使用方法

```bash
# 并行提问（默认 3 个快速 Provider）
/ccb-parallel "如何优化 React 性能？"

# 指定 Provider 组
/ccb-parallel -g @fast "快速问题"        # Kimi, Qwen
/ccb-parallel -g @coding "代码问题"      # Qwen, DeepSeek, Codex
/ccb-parallel -g @chinese "中文问题"     # Kimi, Qwen, DeepSeek

# 自定义 Provider
/ccb-parallel -p "kimi,qwen,gemini" "前端设计问题"

# 生成对比报告
/ccb-parallel --report "分布式系统设计"
```

### 实现原理

```bash
# 1. 并行提交到 Gateway
ID1=$(ccb-submit kimi "$QUESTION")
ID2=$(ccb-submit qwen "$QUESTION")
ID3=$(ccb-submit deepseek "$QUESTION")

# 2. 等待所有完成（30秒）
sleep 30

# 3. 收集结果
R1=$(ccb-query get $ID1)
R2=$(ccb-query get $ID2)
R3=$(ccb-query get $ID3)

# 4. 生成对比报告
cat <<EOF > comparison_report.md
# AI 对比报告
## Kimi: $R1
## Qwen: $R2
## DeepSeek: $R3
EOF
```

---

### 高级功能类 (3个)

#### Skill 3: ccb-research (深度研究)

**文件**: `subskills/research.md`

### 用途
结合 Explore Subagent 和 CCB，进行深度代码库研究和多 AI 分析。

### 触发条件
- 需要探索大型代码库
- 需要多轮 AI 交互
- 需要专业分析（架构、安全、性能）

### 使用方法

```bash
# 代码库架构分析
/ccb-research architecture "分析这个项目的架构"

# 安全审查
/ccb-research security "找出所有潜在安全问题"

# 性能优化建议
/ccb-research performance "识别性能瓶颈"

# 自定义研究
/ccb-research custom \
  --explore "找出所有 API 端点" \
  --analyze-with "kimi,codex" \
  --output "api_analysis.md"
```

### 工作流程

```
1. 启动 Explore Subagent（快速探索代码库）
   ↓
2. Subagent 收集关键文件和模式
   ↓
3. 将发现提交给 CCB Providers（并行分析）
   ↓
4. Kimi: 中文总结
   Qwen: 数据结构分析
   Codex: 代码审查
   Gemini: 架构建议
   ↓
5. Claude 整合所有结果
   ↓
6. 生成综合报告
```

### 实现（使用 Task tool + Gateway API）

```python
# Step 1: 启动 Explore Subagent
Task(
    subagent_type="Explore",
    prompt="探索项目结构，识别关键 API 端点文件",
    description="探索代码库"
)

# Step 2: 获取 Subagent 结果后，并行提交给 CCB
exploration_result = [subagent 返回的内容]

# Step 3: 并行提交给多个 AI 分析
ccb-submit kimi "总结这些 API: $exploration_result"
ccb-submit qwen "分析数据结构: $exploration_result"
ccb-submit codex o3 "审查代码质量: $exploration_result"
ccb-submit gemini 3p "建议架构优化: $exploration_result"

# Step 4: 收集结果并整合
# ...
```

---

#### Skill 4: ccb-workflow (工作流自动化)

**文件**: `subskills/workflow.md`

### 用途
使用 Bash Subagent + CCB 实现复杂的自动化工作流。

### 触发条件
- 需要执行多步骤操作
- 需要 shell 命令 + AI 决策结合
- 需要自动化处理流程

### 使用方法

```bash
# 自动代码审查流程
/ccb-workflow code-review \
  --files "src/**/*.py" \
  --reviewers "codex,kimi" \
  --output "review_report.md"

# 自动化测试 + 分析
/ccb-workflow test-analyze \
  --run-tests "pytest tests/" \
  --analyze-failures "deepseek" \
  --suggest-fixes "kimi"

# 自定义工作流
/ccb-workflow custom \
  --steps "step1.sh,step2.sh" \
  --ai-checkpoints "kimi,qwen"
```

### 示例：自动代码审查工作流

```bash
#!/bin/bash
# Bash Subagent 执行

# Step 1: 收集待审查文件
FILES=$(find src -name "*.py" -newer .last_review)

# Step 2: 提交给 Codex 审查
for file in $FILES; do
    CODE=$(cat "$file")
    ccb-submit codex o3 -a reviewer "审查: $file\n\n$CODE"
done

# Step 3: 等待所有审查完成
sleep 60

# Step 4: 收集审查结果
# ...

# Step 5: 用 Kimi 生成中文总结
ccb-submit kimi "总结审查结果并给出优先级建议"
```

---

#### Skill 5: ccb-memory (记忆系统)

**文件**: `subskills/memory.md`

### 用途
管理 CCB 的双系统记忆，进行启发式检索。

### 使用方法

```bash
# 启发式搜索（三维评分）
/ccb-memory search "如何实现认证"

# 保存重要对话
/ccb-memory save --importance 0.9

# 夜间合并
/ccb-memory consolidate

# 记忆统计
/ccb-memory stats

# 注入历史上下文
/ccb-memory inject 2026-02-05
```

### 启发式检索原理

```
final_score = α × Relevance + β × Importance + γ × Recency

Relevance  - FTS5 BM25 关键词匹配
Importance - 用户标记的重要性 (0.0-1.0)
Recency    - 基于艾宾浩斯曲线的时间衰减

默认权重：α=0.4, β=0.3, γ=0.3
```

---

### 专业领域类 (3个)

#### Skill 6: ccb-benchmark (性能基准测试)

**文件**: `subskills/benchmark.md`

### 用途
对比不同 Provider 的性能、质量、成本。

### 使用方法

```bash
# 响应速度测试
/ccb-benchmark speed "简单问题"

# 代码质量对比
/ccb-benchmark code "实现快速排序"

# 推理能力对比
/ccb-benchmark reasoning "证明哥德巴赫猜想"

# 成本分析
/ccb-benchmark cost --days 7

# 生成对比报告
/ccb-benchmark report --all
```

### 测试维度

| 维度 | 指标 | 测试方法 |
|------|------|----------|
| **速度** | 响应时间 | 同一问题发送给所有 Provider |
| **质量** | 准确性、完整性 | 标准问题集评分 |
| **成本** | Token 费用 | 统计 API 费用 |
| **稳定性** | 失败率 | 100 次请求成功率 |

---

#### Skill 7: ccb-discussion (多 AI 协作讨论)

**文件**: `subskills/discussion.md`

### 用途
让多个 AI Provider 参与任务讨论，从不同角度分析问题，Claude 汇总形成完整计划。**整合了原 `all-plan` skill**。

### 触发条件
- 需要多 AI 的不同观点
- 架构设计、技术选型决策
- 代码审查、方案对比
- 复杂问题的多角度分析

### 讨论模式

| 模式 | 参与 AI | 时间 | 适用场景 |
|------|---------|------|----------|
| **快速** | 3个快速AI | 15-30s | 日常决策 |
| **完整** | 7个AI | 60-120s | 重要决策 |
| **专项** | 3-5个专家AI | 30-60s | 特定领域 |

### 使用示例

```bash
# 快速讨论
讨论主题: "如何优化数据库查询性能"
模式: 快速（Kimi, Qwen, DeepSeek）

# 完整讨论
讨论主题: "设计分布式任务调度系统"
模式: 完整（7个AI参与）

# 代码专项讨论
代码讨论: "审查并发代码设计"
参与: Codex, DeepSeek, Qwen
```

### 工作流程

```
1. Claude 并行发送讨论请求 → Gateway API
2. 各 AI 独立分析并回复
3. Claude 汇总（提取共识 + 标记分歧）
4. 形成执行计划并分配角色
```

**原 `all-plan` skill 用户**：直接使用此 skill，功能完全兼容并增强。

---

#### Skill 8: ccb-stem (STEM 学术建模)

**文件**: `subskills/stem.md`

### 用途
使用 8 模型分布式架构进行 STEM 学术研究、数学推导、工程文档创建。**整合了原 `stem-modeling` skill**。

### 8 模型分工

| AI | 角色 | 核心职责 |
|----|------|----------|
| 🟢 Claude | 编排 & 逻辑 | 中央协调 |
| 🔵 Gemini | SOTA 研究 | 实时搜索 |
| 🟣 Codex | 代码实现 | 最佳代码 |
| 🟠 OpenCode | 中文写作 | 案例研究 |
| 🔷 iFlow | Mermaid 图表 | 流程图 |
| 🔴 Kimi | 代码审计 | 全面审查 |
| 🟡 Qwen | 数学推导 | LaTeX 公式 |
| ⚫ DeepSeek | 深度推理 | 逻辑分析 |

### 执行模式

```
串行执行: Gemini → Qwen → OpenCode → Codex → iFlow → Kimi → DeepSeek → Claude

时间: 约 10-15 分钟
质量: 最高
```

### 使用示例

```
研究主题: "随机森林算法的数学原理与实现"
模式: auto-pilot

输出:
- SOTA 文献综述（Gemini）
- 数学推导（Qwen）
- 代码实现（Codex）
- 流程图（iFlow）
- 中文案例（OpenCode）
- 代码审计（Kimi）
- 深度推理（DeepSeek）
- 最终整合（Claude）
```

**原 `stem-modeling` skill 用户**：直接使用此 skill，调用方式从旧 CLI（gask, qask）升级为统一的 `ccb-submit`。

---

#### Skill 9: ccb-macro (宏观研究)

**文件**: `subskills/macro.md`

### 用途
8 AI 串行协作进行中国 A 股市场日常宏观研究，管理 1000万模拟投资组合。**整合了原 `macro-research-ccb` skill**。

### 8 AI 研究团队

| AI | 角色 | 研究领域 | 搜索 |
|----|------|----------|:----:|
| Gemini | 基本面研究员 | 宏观经济、央行 | 25次 |
| Codex | 技术面研究员 | K线、指标 | 25次 |
| OpenCode | 估值研究员 | PE/PB估值 | 25次 |
| iFlow | 资金流研究员 | 主力资金 | 25次 |
| Kimi | 行业研究员 | 板块轮动 | 25次 |
| Qwen | 国际宏观研究员 | 美股、汇率 | 25次 |
| DeepSeek | 政策研究员 | 监管政策 | 25次 |
| Claude | 舆情+报告 | 北向资金 | 25次 |

**总计**: 200 次联网搜索

### 串行执行（强制）

```
Gemini → Codex → OpenCode → iFlow → Kimi → Qwen → DeepSeek → Claude

每个完成后才启动下一个
每 30 秒轮询检查状态
总时间: 约 12 分钟
```

### 报告结构

```markdown
1. 📊 投资决策摘要（最前面！）
   - 核心要点、预期差、买入机会、卖出关注
2. 💰 模拟投资组合（1000万）
   - 持仓、调仓、表现追踪
3. 🤖 多 Agent 共识
   - 8研究员观点、3投资经理、风控官
4. 📈 市场回顾
5. 🏭 行业深度
6. 🌍 国际宏观
7. ⏱️ 执行摘要（3分钟速读）
```

### 使用示例

```
今天是 2026-02-07，执行 CCB 分布式研究（串行模式）
初始资金：1000万人民币

自动执行：
1. 串行启动 8 个研究员
2. 每个完成后保存中间结果
3. Claude 整合生成完整报告
4. 给出投资建议和组合调整
```

**原 `macro-research-ccb` skill 用户**：直接使用此 skill，调用方式升级为 `ccb-submit`，增强了监控和追踪。

---

## 统一配置文件

**`~/.claude/skills/ccb-unified/config.json`：**

```json
{
  "gateway": {
    "url": "http://localhost:8765",
    "timeout": 300
  },
  "providers": {
    "fast": ["kimi", "qwen"],
    "medium": ["deepseek", "iflow", "opencode"],
    "slow": ["codex", "gemini"],
    "coding": ["qwen", "deepseek", "codex", "kimi", "gemini"],
    "chinese": ["kimi", "qwen", "deepseek"]
  },
  "subagents": {
    "explore": {
      "timeout": 120,
      "thoroughness": "medium"
    },
    "bash": {
      "timeout": 60
    },
    "plan": {
      "timeout": 90
    }
  },
  "async": {
    "default_wait": 30,
    "poll_interval": 5,
    "max_retries": 3
  },
  "parallel": {
    "default_group": "@fast",
    "max_concurrent": 5,
    "wait_time": 30
  },
  "research": {
    "default_analyzers": ["kimi", "qwen", "codex"],
    "exploration_depth": "medium",
    "report_format": "markdown"
  }
}
```

---

## 智能路由规则

当用户没有指定 Provider 时，根据任务类型自动选择：

```python
def auto_select_provider(task: str) -> str:
    """智能选择 Provider"""

    # 前端任务
    if any(kw in task for kw in ["React", "Vue", "CSS", "前端", "UI"]):
        return "gemini 3f"

    # 算法推理
    if any(kw in task for kw in ["算法", "证明", "数学", "推理"]):
        return "codex o3"

    # 代码审查
    if any(kw in task for kw in ["审查", "review", "安全"]):
        return "codex o3"

    # 中文任务
    if any(kw in task for kw in ["翻译", "中文", "总结"]):
        return "kimi"

    # 代码生成
    if any(kw in task for kw in ["实现", "代码", "Python", "编写"]):
        return "qwen"

    # 默认：快速响应
    return "kimi"
```

---

## 使用示例

### 示例 1: 深度代码库研究

```bash
# 用户请求："分析这个项目的架构并给出优化建议"

# Claude 决策：使用 ccb-research
/ccb-research architecture "分析项目架构"

# 内部流程：
# 1. 启动 Explore Subagent → 探索代码库
# 2. 并行提交给 4 个 AI:
#    - Kimi: 中文总结
#    - Qwen: 数据结构分析
#    - Codex: 代码质量审查
#    - Gemini: 架构优化建议
# 3. Claude 整合结果生成报告
```

### 示例 2: 并行多 AI 对比

```bash
# 用户请求："如何优化 React 性能？我想听听多个 AI 的建议"

# Claude 决策：使用 ccb-parallel
/ccb-parallel -g @coding "如何优化 React 性能？"

# 内部流程：
# 1. 并行提交给 Qwen, DeepSeek, Codex
# 2. 等待 30 秒
# 3. 生成对比报告
```

### 示例 3: 自动化工作流

```bash
# 用户请求："自动审查所有新修改的 Python 文件"

# Claude 决策：使用 ccb-workflow
/ccb-workflow code-review \
  --files "git diff --name-only HEAD~1 '*.py'" \
  --reviewers "codex,kimi" \
  --output "review_$(date +%Y%m%d).md"

# 内部流程：
# 1. Bash Subagent 执行 git diff
# 2. 对每个文件提交 Codex 审查（异步）
# 3. Kimi 生成中文总结
# 4. 保存报告
```

---

## 错误处理

### Gateway 未运行

```bash
# 自动检测并提示
✖ Gateway 未运行

启动命令:
  cd ~/.local/share/codex-dual && python3 -m lib.gateway.gateway_server --port 8765
```

### Provider 超时

```bash
# 自动降级到更快的 Provider
⏱️  Codex 超时，自动切换到 DeepSeek
```

### Subagent 失败

```bash
# 回退到直接 Gateway 调用
⚠️  Explore Subagent 失败，使用直接搜索模式
```

---

## 性能优化

### 1. 异步优先

```bash
# ✅ 推荐：异步非阻塞
ccb-submit kimi "问题"

# ❌ 不推荐：同步阻塞（仅快速任务）
ccb-cli kimi "问题"
```

### 2. 批量并行

```bash
# ✅ 推荐：一次性提交多个
/ccb-parallel -p "kimi,qwen,deepseek" "问题"

# ❌ 不推荐：串行等待
ccb-cli kimi "问题"
ccb-cli qwen "问题"
ccb-cli deepseek "问题"
```

### 3. Subagent 缓存

```bash
# Explore Subagent 的结果可以复用
# 避免重复探索相同的代码库
```

---

## 监控和统计

### Web UI

访问 `http://localhost:8765/web` 查看：
- 实时请求监控
- Provider 状态
- 成本分析
- 记忆统计
- Subagent 任务列表

### CLI 统计

```bash
# Gateway 统计
curl http://localhost:8765/api/stats

# 成本分析
curl http://localhost:8765/api/costs/summary

# 记忆统计
ccb-mem stats-v2

# Subagent 任务
/tasks list
```

---

## 最佳实践

1. **保持 Gateway 运行** - 确保 http://localhost:8765 可访问
2. **异步优先** - 除非是简单快速任务，否则使用异步模式
3. **合理选择子 skill** - 根据任务类型选择最合适的子 skill
4. **利用 Subagent** - 复杂任务交给 Subagent 处理
5. **并行处理** - 多个独立任务同时提交
6. **记忆管理** - 定期运行 `ccb-mem consolidate`
7. **监控性能** - 定期查看 Web UI 和成本报告

---

## 版本历史

### v1.0 (2026-02-06)
- ✅ 统一 CCB + Subagent 架构
- ✅ 6 个子 skills 模块化设计
- ✅ 智能路由和自动选择
- ✅ 完整的错误处理和降级策略
- ✅ 统一配置文件
- ✅ Web UI 和监控

---

## 相关文档

- **Gateway API**: `~/.local/share/codex-dual/docs/GATEWAY_API.md`
- **记忆系统**: `~/.local/share/codex-dual/docs/MEMORY_V2.md`
- **Subagent 文档**: Claude Code 官方文档
- **原有 skills**:
  - `~/.claude/skills/ccb/SKILL.md` - 基础 CCB
  - `~/.claude/skills/ask/SKILL.md` - 简单调用
  - `~/.claude/skills/stem-modeling/SKILL.md` - STEM 研究
  - `~/.claude/skills/macro-research-ccb/SKILL.md` - 宏观研究

---

*CCB Unified Version: v1.0*
*Last Updated: 2026-02-06*
*Architecture: Gateway API + Subagent Integration*
