# CCB-Memory - 记忆系统操作

## 概述

管理 CCB 的双系统记忆架构，进行启发式检索和记忆整合。

## 双系统架构

```
┌─────────────────────────────────────────────┐
│         System 1 (快速记忆)                   │
│  • 即时归档会话                               │
│  • /clear 或 /compact 触发                    │
│  • 存储: session_archives 表                 │
└──────────────────┬──────────────────────────┘
                   │
                   ▼
          启发式检索 (Heuristic Retrieval)
          final_score = α×R + β×I + γ×T
                   │
                   ▼
┌──────────────────┴──────────────────────────┐
│         System 2 (深度记忆)                   │
│  • 夜间自动整合                               │
│  • 合并相似记忆                               │
│  • LLM 生成摘要                              │
│  • 存储: consolidated_memories 表            │
└─────────────────────────────────────────────┘
```

## 核心命令

### System 1 操作

```bash
# 保存当前会话
ccb-mem save [--importance 0.0-1.0]

# 列出最近归档
ccb-mem list [--limit 10]

# FTS5 全文搜索
ccb-mem search "关键词"

# 启发式检索（三维评分）
ccb-mem search-scored "查询" [--limit 5]

# 设置重要性
ccb-mem importance <memory_id> 0.8

# 应用时间衰减
ccb-mem decay --all

# 标记遗忘
ccb-mem forget <memory_id>

# 统计
ccb-mem stats
ccb-mem stats-v2  # 包含启发式指标
```

### System 2 操作

```bash
# 夜间完整流程
ccb-consolidate nightly

# 单独操作
ccb-consolidate decay      # 时间衰减
ccb-consolidate merge      # 合并相似记忆
ccb-consolidate abstract   # LLM 生成摘要
ccb-consolidate forget     # 清理过期记忆
ccb-consolidate stats      # 统计信息
```

## 启发式检索原理

### 三维评分公式

```
final_score = α × Relevance + β × Importance + γ × Recency

默认权重:
α = 0.4 (Relevance)
β = 0.3 (Importance)
γ = 0.3 (Recency)
```

### 维度详解

| 维度 | 来源 | 计算方法 | 取值范围 |
|------|------|----------|----------|
| **Relevance** | FTS5 BM25 | 关键词匹配质量 | 0.0 - 1.0 |
| **Importance** | 用户/LLM | 手动标记或自动评估 | 0.0 - 1.0 |
| **Recency** | 艾宾浩斯曲线 | exp(-λ × hours_since_access) | 0.0 - 1.0 |

### 时间衰减曲线

```
Recency = exp(-λ × hours_since_access)

λ = 0.1 (默认衰减率)

示例:
- 刚访问 (0小时): 1.0
- 1天前 (24小时): 0.09
- 3天前 (72小时): 0.001
- 1周前: ~0.0
```

## 使用场景

### 场景 1: 搜索历史对话

```bash
# 基础关键词搜索
ccb-mem search "React Hooks"

# 启发式搜索（推荐）
ccb-mem search-scored "React Hooks" --limit 5
```

返回结果包含：
- 记忆 ID
- 相关度评分
- 创建时间
- 最后访问时间
- 重要性评分
- 内容摘要

### 场景 2: 标记重要对话

```bash
# 保存当前会话并标记为高重要性
ccb-mem save --importance 0.9

# 或事后标记
MEMORY_ID="mem_abc123"
ccb-mem importance $MEMORY_ID 0.9
```

重要性评分指导：
- **0.9-1.0**: 关键决策、重要发现
- **0.7-0.8**: 有价值的讨论、解决方案
- **0.5-0.6**: 一般对话、参考信息
- **0.0-0.4**: 低价值内容

### 场景 3: 注入历史上下文

```bash
# 注入指定日期的记忆
ccb-mem inject 2026-02-05

# 注入最近 3 天的记忆
ccb-mem inject --days 3

# 注入特定主题的记忆
ccb-mem inject --query "CCB Gateway 架构"
```

### 场景 4: 夜间记忆整合

```bash
# 完整夜间流程（推荐在 cron 中运行）
ccb-consolidate nightly

# 等效于:
ccb-consolidate decay      # 1. 应用时间衰减
ccb-consolidate merge      # 2. 合并相似记忆 (>90%)
ccb-consolidate abstract   # 3. LLM 生成摘要
ccb-consolidate forget     # 4. 遗忘低价值记忆
```

## 配置文件

**`~/.ccb/heuristic_config.json`：**

```json
{
  "retrieval": {
    "relevance_weight": 0.4,
    "importance_weight": 0.3,
    "recency_weight": 0.3,
    "decay_rate": 0.1,
    "candidate_pool_size": 50,
    "final_limit": 5
  },
  "system2": {
    "merge_similarity_threshold": 0.9,
    "abstract_group_min_size": 5,
    "forget_score_threshold": 0.01,
    "forget_age_days": 90
  },
  "llm": {
    "provider": "ollama",
    "model": "qwen2.5:7b",
    "embedding_model": "nomic-embed-text"
  }
}
```

### 参数说明

| 参数 | 默认值 | 说明 |
|------|-------|------|
| `relevance_weight` | 0.4 | 相关性权重 |
| `importance_weight` | 0.3 | 重要性权重 |
| `recency_weight` | 0.3 | 时间权重 |
| `decay_rate` | 0.1 | 时间衰减率 λ |
| `candidate_pool_size` | 50 | 候选记忆池大小 |
| `final_limit` | 5 | 最终返回结果数 |
| `merge_similarity_threshold` | 0.9 | 合并相似度阈值 |
| `forget_score_threshold` | 0.01 | 遗忘分数阈值 |
| `forget_age_days` | 90 | 遗忘年龄阈值 |

## 数据库结构

```
~/.ccb/ccb_memory.db
├── session_archives         # System 1: 会话归档
│   ├── id (PRIMARY KEY)
│   ├── session_id
│   ├── timestamp
│   ├── content
│   └── metadata
│
├── consolidated_memories    # System 2: 整合记忆
│   ├── id (PRIMARY KEY)
│   ├── source_ids (JSON)
│   ├── abstract
│   ├── created_at
│   └── importance_score
│
├── memory_importance        # 启发式: 重要性评分
│   ├── memory_id (FK)
│   ├── importance_score
│   └── set_by (user|llm)
│
├── memory_access_log        # 启发式: 访问追踪
│   ├── memory_id (FK)
│   ├── accessed_at
│   └── access_type
│
└── consolidation_log        # System 2: 审计日志
    ├── id
    ├── operation_type
    ├── affected_count
    └── timestamp
```

## 使用示例

### 示例 1: 完整工作流

```bash
# 1. 工作中保存重要会话
ccb-mem save --importance 0.8

# 2. 稍后搜索相关内容
ccb-mem search-scored "API 设计模式" --limit 5

# 3. 查看统计
ccb-mem stats-v2

# 4. 夜间自动整合
ccb-consolidate nightly
```

### 示例 2: 与 CCB 查询结合

```bash
# 先检索相关记忆
CONTEXT=$(ccb-mem search-scored "React 性能优化" --limit 3)

# 将记忆作为上下文提供给 AI
ccb-cli kimi "基于以下历史讨论，给出新的优化建议: $CONTEXT"
```

### 示例 3: Cron 自动化

```bash
# 添加到 crontab
# 每天凌晨 2 点运行夜间整合
0 2 * * * /usr/local/bin/ccb-consolidate nightly >> ~/.ccb/consolidate.log 2>&1
```

### 示例 4: 权重调整实验

```bash
# 场景：更重视时间新鲜度
cat > ~/.ccb/heuristic_config.json <<EOF
{
  "retrieval": {
    "relevance_weight": 0.3,
    "importance_weight": 0.2,
    "recency_weight": 0.5
  }
}
EOF

# 测试效果
ccb-mem search-scored "测试查询"
```

## 性能优化

### FTS5 索引

```sql
-- ccb_memory.db 使用 FTS5 全文索引
CREATE VIRTUAL TABLE session_archives_fts USING fts5(
    content,
    tokenize='porter unicode61'
);
```

### 查询优化

```bash
# 使用 candidate_pool_size 控制中间结果
# 更大的池子 = 更准确，但更慢
# 更小的池子 = 更快，但可能遗漏

# 默认 50 已足够，大型数据库可增加到 100
```

## 故障排查

### 搜索结果为空

```bash
# 检查数据库
sqlite3 ~/.ccb/ccb_memory.db "SELECT COUNT(*) FROM session_archives;"

# 重建 FTS5 索引
ccb-mem rebuild-index
```

### 时间衰减过快

```bash
# 降低 decay_rate
# 从 0.1 降到 0.05
{
  "retrieval": {
    "decay_rate": 0.05
  }
}
```

### 记忆合并过于激进

```bash
# 提高相似度阈值
{
  "system2": {
    "merge_similarity_threshold": 0.95  # 从 0.9 提高到 0.95
  }
}
```

## 最佳实践

1. **主动标记重要对话** - 不要依赖自动评估
2. **定期运行 consolidate** - 保持记忆库健康
3. **使用启发式搜索** - 比纯关键词搜索更智能
4. **注入相关上下文** - 提升 AI 回答质量
5. **监控统计信息** - `ccb-mem stats-v2`
6. **调整权重** - 根据实际需求定制
7. **清理过期记忆** - 定期运行 `ccb-consolidate forget`

## 与其他 Skills 集成

### 与 ccb-research 集成

```bash
# 研究前注入相关记忆
ccb-mem inject --query "项目架构"

# 研究后保存发现
# [完成研究后]
ccb-mem save --importance 0.9
```

### 与 ccb-workflow 集成

```bash
# 工作流执行前检索最佳实践
BEST_PRACTICES=$(ccb-mem search-scored "代码审查最佳实践")

# 工作流执行后保存经验
# [完成审查后]
ccb-mem save --importance 0.7
```

---

*CCB-Memory v1.0*
*Part of CCB Unified Platform*
