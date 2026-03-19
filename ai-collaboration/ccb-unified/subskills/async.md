# CCB-Async - 异步调用管理

## 概述

处理需要长时间运行的 AI 任务，通过 Gateway API 实现异步非阻塞调用。

## 触发条件

- 任务预计耗时 > 30 秒
- 需要同时提交多个独立任务
- 慢速 Provider (Codex, Gemini)
- 用户明确要求异步执行

## 命令

### 单个异步提交

```bash
ccb-submit <provider> [model] [options] "prompt"

# 示例
ccb-submit kimi "详细分析这个架构设计"
ccb-submit codex o3 -a reviewer "审查代码"
ccb-submit gemini 3p "前端设计方案"
```

### 批量异步提交

```bash
# 方法 1: 并行提交多个任务
ID1=$(ccb-submit kimi "问题1")
ID2=$(ccb-submit qwen "问题2")
ID3=$(ccb-submit deepseek "问题3")

# 方法 2: 使用循环
for question in "Q1" "Q2" "Q3"; do
    ccb-submit kimi "$question"
done
```

### 查询状态

```bash
# 查询单个请求状态
ccb-query status <request_id>

# 列出所有待处理请求
ccb-query pending

# 获取完成的结果
ccb-query get <request_id>
```

## 工作流程

```
1. 提交请求 → Gateway API
   ↓
2. Gateway 返回 request_id
   ↓
3. 继续其他工作（不阻塞）
   ↓
4. 定期查询状态
   ↓
5. 任务完成后获取结果
```

## 超时处理

ccb-cli 自动超时切换：

```bash
# ccb-cli 内部逻辑
ccb-cli kimi "复杂任务"
# 如果超时，自动切换到异步模式
# 返回 request_id 供后续查询
```

## 使用示例

### 示例 1: 异步代码审查

```bash
# 提交审查任务
REQUEST_ID=$(ccb-submit codex o3 -a reviewer "审查以下代码: ...")

echo "✓ 审查任务已提交: $REQUEST_ID"
echo "继续其他工作..."

# 30 秒后查询结果
sleep 30
RESULT=$(ccb-query get $REQUEST_ID)

if [ $? -eq 0 ]; then
    echo "✅ 审查完成"
    echo "$RESULT"
else
    echo "⏳ 仍在处理中，稍后查询"
fi
```

### 示例 2: 批量翻译

```bash
# 提交 10 个翻译任务
for i in {1..10}; do
    FILE="chapter_$i.txt"
    CONTENT=$(cat "$FILE")
    ID=$(ccb-submit kimi "翻译成英文: $CONTENT")
    echo "chapter_$i -> $ID"
done

# 等待所有完成
sleep 60

# 批量获取结果
for id in $(ccb-query pending | grep -o 'req_[a-z0-9]*'); do
    ccb-query get $id > "result_$id.txt"
done
```

### 示例 3: 异步 + Subagent

```bash
# 用 Explore Subagent 探索代码库（阻塞）
Task(
    subagent_type="Explore",
    prompt="找出所有 API 端点",
    description="探索 API"
)

# 获取探索结果后，异步分析
ENDPOINTS=$(cat exploration_result.txt)

# 并行提交给 3 个 AI 分析
ID1=$(ccb-submit kimi "总结: $ENDPOINTS")
ID2=$(ccb-submit qwen "数据分析: $ENDPOINTS")
ID3=$(ccb-submit codex o3 "安全审查: $ENDPOINTS")

# 等待所有完成
sleep 45

# 收集结果
R1=$(ccb-query get $ID1)
R2=$(ccb-query get $ID2)
R3=$(ccb-query get $ID3)

# 整合报告
cat <<EOF > api_analysis.md
# API 分析报告

## 总结 (Kimi)
$R1

## 数据分析 (Qwen)
$R2

## 安全审查 (Codex)
$R3
EOF
```

## 状态码

| 状态 | 描述 |
|------|------|
| `pending` | 已提交，等待处理 |
| `processing` | 正在处理 |
| `completed` | 已完成 |
| `failed` | 失败 |
| `timeout` | 超时 |

## 轮询策略

```bash
# 智能轮询
check_async_result() {
    local request_id=$1
    local max_attempts=12  # 最多等待 60 秒
    local attempt=0

    while [ $attempt -lt $max_attempts ]; do
        STATUS=$(ccb-query status $request_id | jq -r '.status')

        case $STATUS in
            completed)
                ccb-query get $request_id
                return 0
                ;;
            failed|timeout)
                echo "✖ 任务失败: $STATUS"
                return 1
                ;;
            *)
                echo "⏳ 等待中... ($attempt/$max_attempts)"
                sleep 5
                ((attempt++))
                ;;
        esac
    done

    echo "⏱️  超时，请稍后手动查询"
    return 2
}

# 使用
check_async_result $REQUEST_ID
```

## 最佳实践

1. **慢速 Provider 必须异步** - Codex, Gemini
2. **并行提交** - 多个独立任务一次性提交
3. **合理等待** - 快速 Provider 30s，慢速 60-90s
4. **错误处理** - 检查状态码，处理失败情况
5. **结果保存** - 重要结果保存到文件

## 性能对比

| 模式 | 响应时间 | 阻塞 | 并发 |
|------|----------|------|------|
| **同步** | 立即返回结果 | ✅ 阻塞 | ❌ 串行 |
| **异步** | 立即返回 ID | ❌ 不阻塞 | ✅ 并行 |

## 故障排查

### 请求一直 pending

```bash
# 检查 Gateway 状态
curl http://localhost:8765/health

# 检查 Provider 状态
curl http://localhost:8765/providers
```

### 无法获取结果

```bash
# 检查请求是否存在
ccb-query status <request_id>

# 查看 Gateway 日志
tail -f ~/.ccb/gateway.log
```

---

*CCB-Async v1.0*
*Part of CCB Unified Platform*
