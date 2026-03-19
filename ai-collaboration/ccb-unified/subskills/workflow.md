# CCB-Workflow - 工作流自动化

## 概述

使用 Bash Subagent + CCB 实现复杂的自动化工作流，结合 shell 命令和 AI 决策。

## 架构

```
用户触发工作流
    ↓
Claude (编排)
    ↓
启动 Bash Subagent → 执行 Shell 命令
    ↓
关键决策点 → 调用 CCB Provider (通过 Gateway API)
    ↓
继续 Shell 执行
    ↓
完成并生成报告
```

## 预定义工作流

| 工作流 | 说明 | Subagent | CCB |
|--------|------|----------|-----|
| `code-review` | 自动代码审查 | Bash | Codex, Kimi |
| `test-analyze` | 测试+失败分析 | Bash | DeepSeek, Kimi |
| `deploy-check` | 部署前检查 | Bash | Qwen, Codex |
| `doc-generate` | 文档生成 | Bash | Kimi, Gemini |
| `refactor-safe` | 安全重构 | Bash | Codex, Kimi |

## 使用方法

### 代码审查工作流

```bash
# 自动审查所有修改的文件
工作流: code-review

步骤:
1. Bash Subagent: git diff --name-only HEAD~1 '*.py'
2. 对每个文件:
   - ccb-submit codex o3 -a reviewer "审查: $file"
   - ccb-submit kimi "中文总结问题: $file"
3. 收集结果并生成报告
```

### 测试分析工作流

```bash
# 运行测试并分析失败原因
工作流: test-analyze

步骤:
1. Bash Subagent: pytest tests/ --tb=short
2. 如果有失败:
   - ccb-submit deepseek reasoner "分析失败原因: $traceback"
   - ccb-submit kimi "建议修复方案: $traceback"
3. 生成修复建议报告
```

## 实现示例

### 示例 1: 完整代码审查工作流

```python
# Step 1: 启动 Bash Subagent 收集文件
Task(
    subagent_type="Bash",
    prompt="""
    找出所有修改的 Python 文件:
    git diff --name-only HEAD~1 '*.py' > changed_files.txt
    cat changed_files.txt
    """,
    description="收集修改文件",
    timeout=30
)

# Step 2: 获取文件列表
# changed_files = [文件列表]
```

```bash
# Step 3: 对每个文件进行审查 (Bash继续执行)
while IFS= read -r file; do
    echo "审查文件: $file"

    # 读取文件内容
    CODE=$(cat "$file")

    # 提交给 Codex 审查
    ID1=$(ccb-submit codex o3 -a reviewer "代码审查: $file

$CODE")

    # 提交给 Kimi 中文总结
    ID2=$(ccb-submit kimi "用中文总结代码问题: $file

$CODE")

    # 记录 request IDs
    echo "$file,$ID1,$ID2" >> review_tracking.csv
done < changed_files.txt

# Step 4: 等待所有审查完成
echo "等待审查完成..."
sleep 60

# Step 5: 收集结果
cat > review_report.md <<EOF
# 代码审查报告

**审查时间**: $(date)
**修改文件数**: $(wc -l < changed_files.txt)

---

EOF

while IFS=',' read -r file id1 id2; do
    echo "## $file" >> review_report.md
    echo "" >> review_report.md

    echo "### Codex 审查" >> review_report.md
    ccb-query get $id1 >> review_report.md
    echo "" >> review_report.md

    echo "### Kimi 总结" >> review_report.md
    ccb-query get $id2 >> review_report.md
    echo "" >> review_report.md
    echo "---" >> review_report.md
    echo "" >> review_report.md
done < review_tracking.csv

echo "✅ 审查报告已生成: review_report.md"
```

### 示例 2: 测试+分析工作流

```python
# Step 1: 启动 Bash Subagent 运行测试
Task(
    subagent_type="Bash",
    prompt="""
    运行测试并捕获输出:
    pytest tests/ --tb=short 2>&1 | tee test_output.txt

    if [ ${PIPESTATUS[0]} -ne 0 ]; then
        echo "TESTS_FAILED" > test_status.txt
    else
        echo "TESTS_PASSED" > test_status.txt
    fi
    """,
    description="运行测试",
    timeout=120
)
```

```bash
# Step 2: 检查测试结果
STATUS=$(cat test_status.txt)

if [ "$STATUS" = "TESTS_FAILED" ]; then
    echo "❌ 测试失败，开始分析..."

    # 提取失败信息
    FAILURES=$(grep -A 20 "FAILED" test_output.txt)

    # 提交给 DeepSeek 深度分析
    ID1=$(ccb-submit deepseek reasoner "分析测试失败原因:

$FAILURES")

    # 提交给 Kimi 修复建议
    ID2=$(ccb-submit kimi "给出修复建议:

$FAILURES")

    # 等待分析完成
    sleep 45

    # 生成报告
    cat > test_failure_report.md <<EOF
# 测试失败分析报告

**时间**: $(date)
**失败测试数**: $(grep -c "FAILED" test_output.txt)

---

## 失败详情

\`\`\`
$FAILURES
\`\`\`

---

## DeepSeek 分析

$(ccb-query get $ID1)

---

## Kimi 修复建议

$(ccb-query get $ID2)

EOF

    echo "📝 失败报告: test_failure_report.md"
else
    echo "✅ 所有测试通过"
fi
```

### 示例 3: 部署前检查工作流

```bash
#!/bin/bash
# deploy_check_workflow.sh

echo "🔍 开始部署前检查..."

# 1. 检查 Git 状态
if ! git diff-index --quiet HEAD --; then
    echo "❌ 有未提交的更改"
    exit 1
fi

# 2. 运行测试
if ! pytest tests/; then
    echo "❌ 测试失败"
    exit 1
fi

# 3. 检查依赖
echo "检查依赖冲突..."
DEPS=$(pip check 2>&1)

if [ -n "$DEPS" ]; then
    # 有依赖问题，询问 AI
    ID=$(ccb-submit qwen "分析 Python 依赖冲突并给出解决方案:

$DEPS")

    sleep 15
    SOLUTION=$(ccb-query get $ID)

    echo "⚠️  依赖问题分析:"
    echo "$SOLUTION"
fi

# 4. 安全检查
echo "运行安全扫描..."
SECURITY=$(bandit -r src/ 2>&1)

if echo "$SECURITY" | grep -q "High"; then
    # 有高危问题
    ID=$(ccb-submit codex o3 -a reviewer "安全审查:

$SECURITY")

    sleep 30
    REVIEW=$(ccb-query get $ID)

    echo "🔒 安全审查结果:"
    echo "$REVIEW"

    read -p "是否继续部署？[y/N] " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "❌ 部署已取消"
        exit 1
    fi
fi

echo "✅ 所有检查通过，可以部署"
```

### 示例 4: 文档生成工作流

```python
# Step 1: Explore Subagent 探索代码
Task(
    subagent_type="Explore",
    prompt="探索项目结构，识别所有公共 API",
    description="探索 API",
    model="haiku"
)

# Step 2: 获取 API 列表
# api_list = [探索结果]
```

```bash
# Step 3: 为每个 API 生成文档
while IFS= read -r api; do
    # 提取函数签名和代码
    CODE=$(grep -A 20 "def $api" src/*.py)

    # 提交给 Kimi 生成中文文档
    ID=$(ccb-submit kimi "为以下函数生成详细的中文文档（包括参数、返回值、示例）:

$CODE")

    echo "$api,$ID" >> doc_tracking.csv
done < api_list.txt

# Step 4: 收集并汇总
sleep 30

cat > API_DOCS.md <<EOF
# API 文档

**生成时间**: $(date)

---

EOF

while IFS=',' read -r api id; do
    echo "## $api" >> API_DOCS.md
    ccb-query get $id >> API_DOCS.md
    echo "" >> API_DOCS.md
done < doc_tracking.csv

echo "✅ 文档已生成: API_DOCS.md"
```

## 工作流模板

### 通用模板结构

```bash
#!/bin/bash
# workflow_template.sh

set -e  # 出错立即退出

# 1. 前置检查
echo "检查环境..."
# [检查命令]

# 2. 主要任务
echo "执行主要任务..."
# [Bash 命令]

# 3. 决策点 - 调用 CCB
if [ 需要AI决策 ]; then
    ID=$(ccb-submit <provider> "任务描述")
    sleep 30
    RESULT=$(ccb-query get $ID)

    # 根据 AI 建议决定下一步
    if [[ "$RESULT" =~ "继续" ]]; then
        # 继续执行
    else
        # 中止或调整
    fi
fi

# 4. 后续任务
# [更多 Bash 命令]

# 5. 生成报告
echo "生成报告..."
cat > report.md <<EOF
# 工作流报告
...
EOF

echo "✅ 完成"
```

## 错误处理

### 超时重试

```bash
retry_with_timeout() {
    local max_attempts=3
    local timeout=30
    local attempt=1

    while [ $attempt -le $max_attempts ]; do
        echo "尝试 $attempt/$max_attempts..."

        if timeout $timeout "$@"; then
            return 0
        fi

        echo "⏱️  超时，重试..."
        ((attempt++))
        sleep 5
    done

    echo "❌ 所有尝试失败"
    return 1
}

# 使用
retry_with_timeout ccb-cli kimi "问题"
```

### AI 调用失败降级

```bash
call_ai_with_fallback() {
    local primary=$1
    local fallback=$2
    local question=$3

    ID=$(ccb-submit $primary "$question")
    sleep 30

    if ! RESULT=$(ccb-query get $ID 2>/dev/null); then
        echo "⚠️  $primary 失败，使用 $fallback"
        ID=$(ccb-submit $fallback "$question")
        sleep 30
        RESULT=$(ccb-query get $ID)
    fi

    echo "$RESULT"
}

# 使用
ANSWER=$(call_ai_with_fallback codex kimi "代码问题")
```

## 最佳实践

1. **明确工作流步骤** - 每个步骤有清晰的输入输出
2. **关键点调用 AI** - 不是每步都需要 AI，仅决策点
3. **异步提交** - 多个独立 AI 调用并行提交
4. **保存中间结果** - 便于调试和追溯
5. **错误处理** - 每个关键步骤都有错误处理
6. **生成报告** - 工作流结束后生成结构化报告
7. **幂等性** - 工作流可以重复执行

## 与 CI/CD 集成

### GitHub Actions

```yaml
name: AI-Powered Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2

      - name: Install CCB CLI
        run: |
          # 安装 ccb-cli

      - name: Run Review Workflow
        run: |
          bash ~/.claude/skills/ccb-unified/workflows/code_review.sh

      - name: Upload Report
        uses: actions/upload-artifact@v2
        with:
          name: review-report
          path: review_report.md
```

### Cron 定时任务

```bash
# crontab -e

# 每天凌晨 1 点运行依赖检查
0 1 * * * bash /path/to/dependency_check_workflow.sh >> /var/log/ccb-workflow.log 2>&1

# 每周一早上 9 点生成文档
0 9 * * 1 bash /path/to/doc_generate_workflow.sh
```

## 性能考虑

### 并行执行

```bash
# 串行（慢）
for file in *.py; do
    ccb-cli kimi "分析 $file"
done

# 并行（快）
for file in *.py; do
    ccb-submit kimi "分析 $file" &
done
wait

# 收集结果
```

### 批量处理

```bash
# 收集所有文件内容
FILES_CONTENT=$(cat file1.py file2.py file3.py)

# 一次性提交给 AI
ccb-submit codex o3 "批量审查以下文件: $FILES_CONTENT"
```

---

*CCB-Workflow v1.0*
*Part of CCB Unified Platform*
