# CCB-Benchmark - 性能基准测试

## 概述

对比不同 AI Provider 的性能、质量、成本，生成基准测试报告。

## 测试维度

| 维度 | 指标 | 测试方法 |
|------|------|----------|
| **速度** | 响应时间 (秒) | 同一问题发送给所有 Provider |
| **质量** | 准确性、完整性 | 标准问题集评分 |
| **成本** | Token 费用 (USD) | 统计 API 调用费用 |
| **稳定性** | 成功率 (%) | 100 次请求的失败率 |
| **一致性** | 多次结果相似度 | 同一问题 5 次测试 |

## 使用方法

### 基本速度测试

```bash
# 测试所有 Provider 的响应速度
测试命令: 速度基准测试

执行:
1. 准备测试问题："解释递归算法"
2. 并行提交给所有 9 个 Provider
3. 记录每个的响应时间
4. 生成对比表格
```

### 代码质量测试

```bash
# 测试代码生成质量
测试任务: "实现快速排序算法（Python）"

评分标准:
- 正确性 (40%): 能否正确排序
- 效率 (30%): 时间/空间复杂度
- 代码质量 (20%): 可读性、注释
- 完整性 (10%): 测试用例、文档
```

### 成本分析

```bash
# 分析最近 7 天的 Provider 成本
curl http://localhost:8765/api/costs/by-provider

# 计算每个 Provider 的平均 token 费用
# 生成成本对比图表
```

## 实现示例

### 示例 1: 完整速度基准测试

```bash
#!/bin/bash
# speed_benchmark.sh

QUESTION="用3句话解释量子纠缠"
PROVIDERS=("kimi" "qwen" "deepseek" "iflow" "opencode" "claude" "codex" "gemini")

echo "🚀 开始速度基准测试..."
echo "问题: $QUESTION"
echo ""

# 创建结果文件
echo "Provider,StartTime,EndTime,Duration,Status" > benchmark_results.csv

# 并行提交所有 Provider
declare -A REQUEST_IDS
declare -A START_TIMES

for provider in "${PROVIDERS[@]}"; do
    START=$(date +%s)
    START_TIMES[$provider]=$START

    # 异步提交
    ID=$(ccb-submit $provider "$QUESTION" 2>/dev/null)
    REQUEST_IDS[$provider]=$ID

    echo "✓ $provider: $ID (started at $START)"
done

echo ""
echo "⏳ 等待所有响应..."
sleep 60

# 收集结果
echo ""
echo "📊 收集结果..."

for provider in "${PROVIDERS[@]}"; do
    id=${REQUEST_IDS[$provider]}
    start=${START_TIMES[$provider]}

    # 尝试获取结果
    if result=$(ccb-query get $id 2>/dev/null); then
        end=$(date +%s)
        duration=$((end - start))
        status="success"

        echo "✅ $provider: ${duration}s"
    else
        end=$(date +%s)
        duration=$((end - start))
        status="timeout/failed"

        echo "❌ $provider: timeout"
    fi

    # 记录到 CSV
    echo "$provider,$start,$end,$duration,$status" >> benchmark_results.csv
done

# 生成报告
cat > speed_benchmark_report.md <<EOF
# CCB Provider 速度基准测试

**测试时间**: $(date)
**测试问题**: $QUESTION

---

## 结果汇总

| Provider | 响应时间 | 状态 | 速度等级 |
|----------|----------|------|----------|
EOF

# 按速度排序并添加到报告
sort -t',' -k4 -n benchmark_results.csv | tail -n +2 | while IFS=',' read -r provider start end duration status; do
    if [ $duration -lt 15 ]; then
        grade="🚀 Fast"
    elif [ $duration -lt 60 ]; then
        grade="⚡ Medium"
    else
        grade="🐢 Slow"
    fi

    echo "| $provider | ${duration}s | $status | $grade |" >> speed_benchmark_report.md
done

cat >> speed_benchmark_report.md <<EOF

---

## 统计分析

- **最快**: $(sort -t',' -k4 -n benchmark_results.csv | head -2 | tail -1 | cut -d',' -f1)
- **最慢**: $(sort -t',' -k4 -rn benchmark_results.csv | head -1 | cut -d',' -f1)
- **平均**: $(awk -F',' 'NR>1 {sum+=$4; count++} END {printf "%.1f", sum/count}' benchmark_results.csv)s

---

**原始数据**: benchmark_results.csv
EOF

echo ""
echo "✅ 报告已生成: speed_benchmark_report.md"
cat speed_benchmark_report.md
```

### 示例 2: 代码质量基准测试

```bash
#!/bin/bash
# code_quality_benchmark.sh

TASK="实现 Python 快速排序算法，包含类型提示和文档字符串"
PROVIDERS=("qwen" "codex" "deepseek" "kimi")

echo "📝 代码质量基准测试..."

# 提交给所有 Provider
declare -A CODE_IDS

for provider in "${PROVIDERS[@]}"; do
    ID=$(ccb-submit $provider "$TASK")
    CODE_IDS[$provider]=$ID
    echo "✓ $provider: $ID"
done

sleep 60

# 收集代码
mkdir -p benchmark_code
for provider in "${PROVIDERS[@]}"; do
    id=${CODE_IDS[$provider]}
    code=$(ccb-query get $id)
    echo "$code" > "benchmark_code/${provider}_quicksort.py"
done

# 提交给 Codex 进行质量评分
EVALUATION=$(cat <<EOF
请评分以下 4 个 AI 生成的快速排序实现，满分 100 分：

$(for provider in "${PROVIDERS[@]}"; do
    echo "=== $provider ==="
    cat "benchmark_code/${provider}_quicksort.py"
    echo ""
done)

评分标准:
- 正确性 (40分): 算法是否正确
- 效率 (30分): 时间/空间复杂度
- 代码质量 (20分): 可读性、风格
- 完整性 (10分): 文档、类型提示

输出格式:
Provider | 正确性 | 效率 | 代码质量 | 完整性 | 总分
EOF
)

EVAL_ID=$(ccb-submit codex o3 -a reviewer "$EVALUATION")
sleep 45

SCORES=$(ccb-query get $EVAL_ID)

# 生成报告
cat > code_quality_benchmark.md <<EOF
# 代码质量基准测试

**测试任务**: $TASK
**测试时间**: $(date)

---

## 评分结果

$SCORES

---

## 生成的代码

$(for provider in "${PROVIDERS[@]}"; do
    echo "### $provider"
    echo '```python'
    cat "benchmark_code/${provider}_quicksort.py"
    echo '```'
    echo ""
done)

---

**原始代码**: benchmark_code/
EOF

echo "✅ 报告已生成: code_quality_benchmark.md"
```

### 示例 3: 成本分析

```bash
#!/bin/bash
# cost_analysis.sh

echo "💰 CCB 成本分析..."

# 获取成本数据
SUMMARY=$(curl -s http://localhost:8765/api/costs/summary)
BY_PROVIDER=$(curl -s http://localhost:8765/api/costs/by-provider)

# 解析数据
TOTAL_COST=$(echo "$SUMMARY" | jq -r '.total_cost_usd')
TOTAL_REQUESTS=$(echo "$SUMMARY" | jq -r '.total_requests')
AVG_COST=$(echo "scale=6; $TOTAL_COST / $TOTAL_REQUESTS" | bc)

# 生成报告
cat > cost_analysis_report.md <<EOF
# CCB 成本分析报告

**生成时间**: $(date)
**统计周期**: 最近 30 天

---

## 总体统计

- **总成本**: \$${TOTAL_COST} USD
- **总请求数**: $TOTAL_REQUESTS
- **平均每请求**: \$${AVG_COST} USD

---

## 按 Provider 成本

| Provider | 请求数 | 总成本 | 平均成本 | 占比 |
|----------|--------|--------|----------|------|
EOF

echo "$BY_PROVIDER" | jq -r '.providers[] |
    "\(.name) | \(.total_requests) | $\(.total_cost_usd) | $\(.avg_cost_per_request) | \(.percentage)%"' \
    >> cost_analysis_report.md

cat >> cost_analysis_report.md <<EOF

---

## 成本优化建议

1. **使用快速 Provider** - Kimi, Qwen 成本更低
2. **缓存重复查询** - 启用 Gateway 缓存
3. **批量处理** - 减少请求次数
4. **选择合适模型** - 简单任务用小模型

---

**数据来源**: Gateway API (http://localhost:8765)
EOF

echo "✅ 报告已生成: cost_analysis_report.md"
cat cost_analysis_report.md
```

### 示例 4: 稳定性测试

```bash
#!/bin/bash
# stability_test.sh

PROVIDER="kimi"
ITERATIONS=100
QUESTION="1+1等于几？"

echo "🔄 稳定性测试: $PROVIDER (${ITERATIONS}次)"

SUCCESS=0
FAILED=0
TIMEOUT=0

for i in $(seq 1 $ITERATIONS); do
    echo -n "测试 $i/$ITERATIONS... "

    ID=$(ccb-submit $PROVIDER "$QUESTION" 2>/dev/null)

    if [ -z "$ID" ]; then
        echo "❌ 提交失败"
        ((FAILED++))
        continue
    fi

    sleep 5

    if result=$(ccb-query get $ID 2>/dev/null); then
        echo "✅"
        ((SUCCESS++))
    else
        echo "⏱️  超时"
        ((TIMEOUT++))
    fi
done

SUCCESS_RATE=$(echo "scale=2; $SUCCESS * 100 / $ITERATIONS" | bc)

# 生成报告
cat > stability_report_${PROVIDER}.md <<EOF
# ${PROVIDER} 稳定性测试报告

**测试时间**: $(date)
**测试次数**: $ITERATIONS
**测试问题**: $QUESTION

---

## 结果统计

- ✅ 成功: $SUCCESS (${SUCCESS_RATE}%)
- ❌ 失败: $FAILED
- ⏱️  超时: $TIMEOUT

---

## 稳定性评级

EOF

if (( $(echo "$SUCCESS_RATE >= 95" | bc -l) )); then
    echo "⭐⭐⭐⭐⭐ 优秀 (≥95%)" >> stability_report_${PROVIDER}.md
elif (( $(echo "$SUCCESS_RATE >= 90" | bc -l) )); then
    echo "⭐⭐⭐⭐ 良好 (≥90%)" >> stability_report_${PROVIDER}.md
elif (( $(echo "$SUCCESS_RATE >= 80" | bc -l) )); then
    echo "⭐⭐⭐ 一般 (≥80%)" >> stability_report_${PROVIDER}.md
else
    echo "⭐⭐ 较差 (<80%)" >> stability_report_${PROVIDER}.md
fi

echo ""
echo "✅ 报告已生成: stability_report_${PROVIDER}.md"
cat stability_report_${PROVIDER}.md
```

## 标准测试集

### 问题分类

| 类别 | 示例问题 | 评分标准 |
|------|----------|----------|
| **简单问答** | "Python 如何定义函数？" | 准确性、简洁性 |
| **代码生成** | "实现二分查找" | 正确性、效率、质量 |
| **推理** | "证明根号2是无理数" | 逻辑严谨性、完整性 |
| **中文理解** | "翻译并解释成语" | 准确性、文化理解 |
| **长文本** | "总结3000字文章" | 完整性、关键点提取 |

## 自动化测试

### Cron 定时基准测试

```bash
# crontab -e

# 每周一凌晨 3 点运行完整基准测试
0 3 * * 1 bash ~/.claude/skills/ccb-unified/benchmarks/full_benchmark.sh >> /var/log/ccb-benchmark.log 2>&1
```

### CI/CD 集成

```yaml
# .github/workflows/benchmark.yml
name: CCB Benchmark

on:
  schedule:
    - cron: '0 0 * * 1'  # 每周一

jobs:
  benchmark:
    runs-on: ubuntu-latest
    steps:
      - name: Run Benchmark
        run: bash benchmarks/full_benchmark.sh

      - name: Upload Report
        uses: actions/upload-artifact@v2
        with:
          name: benchmark-report
          path: benchmark_reports/
```

## 最佳实践

1. **定期测试** - 每周运行一次完整基准测试
2. **标准问题集** - 使用固定的测试问题
3. **多维度评估** - 不只看速度，还要看质量和成本
4. **保存历史数据** - 追踪性能趋势
5. **公平对比** - 相同的问题、相同的环境
6. **自动化** - 使用 cron 或 CI/CD 自动运行

## 报告格式

### 综合基准测试报告模板

```markdown
# CCB 综合基准测试报告

**测试日期**: [日期]
**测试版本**: [CCB 版本]

---

## 1. 速度测试

[速度对比表格]

## 2. 质量测试

[质量评分表格]

## 3. 成本分析

[成本对比表格]

## 4. 稳定性测试

[稳定性统计]

## 5. 综合排名

| 排名 | Provider | 综合得分 | 推荐场景 |
|------|----------|----------|----------|
| 1 | Kimi | 92 | 中文问答、快速响应 |
| 2 | Qwen | 90 | 代码生成、数学 |
| ... | ... | ... | ... |

---

## 6. 结论与建议

[分析和建议]
```

---

*CCB-Benchmark v1.0*
*Part of CCB Unified Platform*
