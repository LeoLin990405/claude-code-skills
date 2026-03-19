# CCB-Parallel - 并行多 AI 协作

## 概述

同时向多个 AI Provider 提问，获得多角度答案并生成对比报告。

## 触发条件

- 需要多个 AI 的不同观点
- 需要快速获得多种方案
- 对比不同 AI 的能力
- 决策需要多方共识

## 预定义 Provider 组

| 组名 | Provider | 用途 |
|------|----------|------|
| `@fast` | Kimi, Qwen | 快速响应 |
| `@coding` | Qwen, DeepSeek, Codex, Kimi, Gemini | 代码相关 |
| `@chinese` | Kimi, Qwen, DeepSeek | 中文任务 |
| `@reasoning` | Codex o3, DeepSeek reasoner, Kimi thinking | 深度推理 |
| `@all` | 全部 9 个 | 全面分析 |

## 使用方法

### 基本用法

```bash
# 使用默认组 (@fast)
ccb-cli kimi,qwen,deepseek "如何优化 React 性能？"

# 或使用并行脚本
bash ~/.claude/skills/ccb-unified/examples/parallel_example.sh \
  "如何优化 React 性能？" \
  "kimi,qwen,deepseek"
```

### 使用预定义组

```bash
# 快速组
parallel_query() {
    local question=$1
    local providers=$2

    # 并行提交
    IFS=',' read -ra PROVIDERS <<< "$providers"
    declare -A REQUEST_IDS

    for provider in "${PROVIDERS[@]}"; do
        id=$(ccb-submit $provider "$question")
        REQUEST_IDS[$provider]=$id
        echo "✓ $provider: $id"
    done

    # 等待完成
    sleep 30

    # 收集结果
    for provider in "${PROVIDERS[@]}"; do
        id=${REQUEST_IDS[$provider]}
        result=$(ccb-query get $id)
        echo "## $provider 的回答" >> report.md
        echo "$result" >> report.md
        echo "" >> report.md
    done
}

# 使用
parallel_query "问题" "kimi,qwen,deepseek"
```

## 对比报告格式

生成的报告包含：

```markdown
# AI 对比报告

**问题**: [原始问题]
**提交时间**: [时间戳]
**参与 AI**: [Provider 列表]

---

## Kimi 的回答

[Kimi 的完整回答]

**评价**:
- 响应时间: 12s
- 字数: 850
- 关键点: [提取的关键点]

---

## Qwen 的回答

[Qwen 的完整回答]

**评价**:
- 响应时间: 8s
- 字数: 920
- 关键点: [提取的关键点]

---

## DeepSeek 的回答

[DeepSeek 的完整回答]

**评价**:
- 响应时间: 25s
- 字数: 1200
- 关键点: [提取的关键点]

---

## 综合分析

### 共识点
1. [所有 AI 都同意的观点]
2. [...]

### 分歧点
1. [AI 之间有分歧的地方]
2. [...]

### 推荐方案
[基于所有 AI 的意见，综合得出的推荐]

---

**生成时间**: [时间戳]
**报告位置**: `./ai_comparison_[timestamp].md`
```

## 使用示例

### 示例 1: 技术方案对比

```bash
# 问题：选择前端框架
QUESTION="React vs Vue vs Svelte，我应该选择哪个？考虑：学习曲线、生态系统、性能"

# 向 5 个 AI 提问
ccb-submit kimi "$QUESTION"      # → id1
ccb-submit qwen "$QUESTION"      # → id2
ccb-submit gemini 3f "$QUESTION" # → id3
ccb-submit codex o4-mini "$QUESTION" # → id4
ccb-submit deepseek chat "$QUESTION" # → id5

# 等待 30 秒
sleep 30

# 收集并对比
# [生成对比报告]
```

### 示例 2: 代码审查多视角

```bash
CODE=$(cat suspicious_function.py)

# 提交给 3 个审查者
ccb-submit codex o3 -a reviewer "审查安全性: $CODE"
ccb-submit deepseek reasoner "审查逻辑漏洞: $CODE"
ccb-submit kimi -a sisyphus "审查性能问题: $CODE"

# 等待并整合
# [生成综合审查报告]
```

### 示例 3: 多语言翻译对比

```bash
TEXT="The quick brown fox jumps over the lazy dog"

# 3 个 AI 翻译成中文
ccb-submit kimi "翻译成中文: $TEXT"
ccb-submit qwen "翻译成中文: $TEXT"
ccb-submit deepseek "翻译成中文: $TEXT"

# 对比翻译质量
# [生成翻译对比]
```

## 高级功能

### 1. 加权投票

```bash
# 根据 AI 的专长给予不同权重
vote_result() {
    local question=$1

    # Codex (代码) - 权重 0.4
    # Kimi (中文) - 权重 0.3
    # Qwen (综合) - 权重 0.3

    # [实现加权投票逻辑]
}
```

### 2. 相似度分析

```bash
# 分析回答的相似度
similarity_analysis() {
    local answers=("$@")

    # 使用 difflib 或 FTS5 计算相似度
    # 识别共识和分歧
}
```

### 3. 实时对比

```bash
# 实时显示各 AI 的回答进度
real_time_comparison() {
    # 使用 ccb-tail 流式输出
    ccb-tail -f $request_id1 &
    ccb-tail -f $request_id2 &
    ccb-tail -f $request_id3 &
    wait
}
```

## 性能考虑

### 并发限制

- 默认最多同时 5 个并发请求
- 可在配置文件调整

```json
{
  "parallel": {
    "max_concurrent": 5,
    "wait_time": 30
  }
}
```

### 成本控制

```bash
# 计算并行查询的总成本
calculate_cost() {
    curl http://localhost:8765/api/costs/by-provider | jq '
        .providers[] |
        select(.name == "kimi" or .name == "qwen" or .name == "deepseek") |
        .total_cost_usd
    ' | awk '{sum+=$1} END {print sum}'
}
```

## 故障排查

### 部分 Provider 超时

```bash
# 策略：忽略超时的 Provider，继续处理成功的
for id in $ID1 $ID2 $ID3; do
    result=$(ccb-query get $id 2>/dev/null)
    if [ $? -eq 0 ]; then
        echo "✅ 成功: $result"
    else
        echo "⏱️  超时或失败，跳过"
    fi
done
```

### 结果不一致

```bash
# 正常现象 - AI 的多样性
# 在报告中突出显示分歧点
# 让用户根据上下文判断
```

## 最佳实践

1. **选择合适的组** - 根据任务类型选择 Provider 组
2. **控制并发数** - 避免过多并发导致超时
3. **合理等待时间** - 快速 Provider 30s，慢速 60s
4. **突出共识和分歧** - 报告中清晰标注
5. **保存历史对比** - 便于追溯和分析

## 与 ccb-discussion 的区别

| 特性 | ccb-parallel | ccb-discussion |
|------|-------------|----------------|
| **交互轮次** | 1 轮 | 3 轮（提案→互评→修订） |
| **适用场景** | 快速获得多方意见 | 深度讨论形成共识 |
| **执行时间** | 30-60s | 5-10 分钟 |
| **输出** | 并行回答对比 | 多轮讨论记录 |

---

*CCB-Parallel v1.0*
*Part of CCB Unified Platform*
