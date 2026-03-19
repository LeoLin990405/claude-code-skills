# CCB-Discussion - 多 AI 协作讨论

## 概述

让多个 AI Provider 参与任务讨论，从不同角度分析问题，Claude 汇总形成完整计划。

## 架构

```
用户提出问题/任务
    ↓
Claude (协调者)
    ↓
并行发送讨论请求 → Gateway API
    ↓
┌────┬────┬────┬────┬────┬────┬────┐
Kimi Qwen DeepS Codex Gemi iFlow OpCd
└────┴────┴────┴────┴────┴────┴────┘
    ↓
Claude 汇总（共识 + 分歧 + 决策）
    ↓
形成执行计划并分配角色
```

## 讨论模式

| 模式 | 参与 AI | 时间 | 适用场景 |
|------|---------|------|----------|
| **快速** | Kimi, Qwen, DeepSeek | 15-30s | 日常决策 |
| **完整** | 全部 7 个 | 60-120s | 重要决策 |
| **代码** | Codex, DeepSeek, Qwen | 30-60s | 代码设计 |
| **前端** | Gemini, Kimi, Qwen | 30-60s | 前端方案 |
| **架构** | Codex, DeepSeek, Gemini | 60-90s | 架构设计 |

## 使用方法

### 基本用法

```bash
# 快速讨论（3 个快速 AI）
讨论主题: "如何优化数据库查询性能"

# 完整讨论（7 个 AI）
讨论主题: "设计分布式任务调度系统"

# 专项讨论
代码讨论: "审查这段并发代码的设计"
```

## AI 能力矩阵

| AI | 中文 | 代码 | 推理 | 速度 | 最佳任务 |
|----|:----:|:----:|:----:|:----:|----------|
| **Kimi** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 🚀 | 文档、中文、快速问答 |
| **Qwen** | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 🚀 | 代码生成、数学 |
| **DeepSeek** | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⚡ | 算法、推理、证明 |
| **Codex** | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 🐢 | 架构设计、代码审查 |
| **Gemini** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | 🐢 | 前端、多模态 |
| **iFlow** | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⚡ | 工作流自动化 |
| **OpenCode** | ⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⚡ | 通用编程 |

## 实现示例

### 示例 1: 快速讨论（3 AI）

```bash
#!/bin/bash
# quick_discussion.sh

TOPIC="如何优化数据库查询性能"
PROVIDERS=("kimi" "qwen" "deepseek")

PROMPT="【任务讨论】
任务: $TOPIC

请分析这个任务，提出你的实现方案：
1. 整体策略
2. 关键技术（及理由）
3. 实现步骤
4. 潜在风险

请简洁回答，重点突出你的独特见解。"

echo "🚀 发起快速讨论: $TOPIC"

# 并行提交
declare -A REQUEST_IDS

for provider in "${PROVIDERS[@]}"; do
    ID=$(ccb-submit $provider "$PROMPT")
    REQUEST_IDS[$provider]=$ID
    echo "✓ $provider: $ID"
done

# 等待
echo "⏳ 等待 30 秒..."
sleep 30

# 收集回复
declare -A RESPONSES

for provider in "${PROVIDERS[@]}"; do
    id=${REQUEST_IDS[$provider]}
    response=$(ccb-query get $id 2>/dev/null || echo "超时")
    RESPONSES[$provider]=$response
done

# 生成讨论报告
cat > discussion_report.md <<EOF
# 多 AI 讨论报告

**主题**: $TOPIC
**参与**: Kimi, Qwen, DeepSeek
**时间**: $(date)

---

## 🚀 Kimi 的观点

${RESPONSES[kimi]}

---

## 🚀 Qwen 的观点

${RESPONSES[qwen]}

---

## ⚡ DeepSeek 的观点

${RESPONSES[deepseek]}

---

## Claude 汇总

[Claude 在这里提取共识和分歧，并给出决策]

EOF

echo "✅ 讨论报告: discussion_report.md"
```

### 示例 2: 完整讨论（7 AI）

```bash
#!/bin/bash
# full_discussion.sh

TOPIC="设计分布式任务调度系统"
ALL_PROVIDERS=("kimi" "qwen" "deepseek" "iflow" "opencode" "codex" "gemini")

PROMPT="【架构讨论】
任务: $TOPIC

作为专家，请从你的专长角度分析：
1. 整体架构设计
2. 关键技术选型（及理由）
3. 实现步骤（按优先级）
4. 潜在风险和应对

请提供简洁但深入的分析。"

echo "📋 发起完整讨论: $TOPIC"

# 分组提交（快速先发，慢速后发）
FAST=("kimi" "qwen" "deepseek" "iflow" "opencode")
SLOW=("codex" "gemini")

declare -A REQUEST_IDS
declare -A START_TIMES

# 提交快速 AI
for provider in "${FAST[@]}"; do
    start=$(date +%s)
    ID=$(ccb-submit $provider "$PROMPT")
    REQUEST_IDS[$provider]=$ID
    START_TIMES[$provider]=$start
    echo "✓ $provider: $ID (${start}s)"
done

# 提交慢速 AI（稍微延迟）
sleep 5
for provider in "${SLOW[@]}"; do
    start=$(date +%s)
    ID=$(ccb-submit $provider "$PROMPT")
    REQUEST_IDS[$provider]=$ID
    START_TIMES[$provider]=$start
    echo "✓ $provider: $ID (${start}s)"
done

# 等待所有完成
echo "⏳ 等待所有 AI 回复（最多 90 秒）..."
sleep 90

# 收集回复
declare -A RESPONSES
declare -A RESPONSE_TIMES

for provider in "${ALL_PROVIDERS[@]}"; do
    id=${REQUEST_IDS[$provider]}
    start=${START_TIMES[$provider]}

    if response=$(ccb-query get $id 2>/dev/null); then
        end=$(date +%s)
        duration=$((end - start))
        RESPONSES[$provider]=$response
        RESPONSE_TIMES[$provider]=$duration
        echo "✅ $provider: ${duration}s"
    else
        echo "⏱️  $provider: 超时"
        RESPONSES[$provider]="[超时未响应]"
        RESPONSE_TIMES[$provider]="-"
    fi
done

# 生成完整报告
cat > full_discussion_report.md <<EOF
# 完整多 AI 讨论报告

**主题**: $TOPIC
**参与**: 7 个 AI Provider
**时间**: $(date)

---

## 参与统计

| AI | 响应时间 | 状态 | 速度等级 |
|----|---------:|:----:|:--------:|
EOF

for provider in "${ALL_PROVIDERS[@]}"; do
    time=${RESPONSE_TIMES[$provider]}
    if [ "$time" = "-" ]; then
        status="⏱️  超时"
        grade="-"
    else
        status="✅ 成功"
        if [ $time -lt 20 ]; then
            grade="🚀 Fast"
        elif [ $time -lt 60 ]; then
            grade="⚡ Medium"
        else
            grade="🐢 Slow"
        fi
    fi
    echo "| $provider | $time | $status | $grade |" >> full_discussion_report.md
done

cat >> full_discussion_report.md <<EOF

---

## 各 AI 观点

EOF

for provider in "${ALL_PROVIDERS[@]}"; do
    response=${RESPONSES[$provider]}
    time=${RESPONSE_TIMES[$provider]}

    # 图标
    if [[ "$provider" =~ ^(kimi|qwen)$ ]]; then
        icon="🚀"
    elif [[ "$provider" =~ ^(deepseek|iflow|opencode)$ ]]; then
        icon="⚡"
    else
        icon="🐢"
    fi

    cat >> full_discussion_report.md <<SUB
### $icon $provider (${time}s)

$response

---

SUB
done

cat >> full_discussion_report.md <<EOF

## Claude 综合汇总

### ✅ 共识点
[Claude 提取所有 AI 都同意的观点]

1. [共识 1]
2. [共识 2]
3. [...]

### ⚠️ 分歧点
[标记不同 AI 之间的分歧]

| 议题 | 观点 A | 观点 B | Claude 决策 | 理由 |
|------|--------|--------|------------|------|
| [议题] | [AI1: 观点] | [AI2: 观点] | [决策] | [理由] |

### 💡 独特贡献
[每个 AI 的独特见解]

- **Kimi**: [独特贡献]
- **Qwen**: [独特贡献]
- **DeepSeek**: [独特贡献]
- **Codex**: [独特贡献]
- **Gemini**: [独特贡献]
- **iFlow**: [独特贡献]
- **OpenCode**: [独特贡献]

---

## 📋 执行计划

### 任务分配

| 步骤 | 任务 | 负责 AI | 模型 | 原因 |
|------|------|---------|------|------|
| 1 | [任务 1] | [AI] | [模型] | [选择理由] |
| 2 | [任务 2] | [AI] | [模型] | [选择理由] |
| ... | ... | ... | ... | ... |

### 预期产出
- [ ] 产出 1
- [ ] 产出 2
- [ ] 产出 3

### 时间估算
[估算各阶段时间]

---

**生成时间**: $(date)
**报告位置**: $(pwd)/full_discussion_report.md
EOF

echo "✅ 完整讨论报告: full_discussion_report.md"
cat full_discussion_report.md
```

### 示例 3: 专项讨论（代码审查）

```bash
#!/bin/bash
# code_discussion.sh

CODE="$1"
TOPIC="审查以下代码的设计和实现"
CODE_EXPERTS=("codex" "deepseek" "qwen")

PROMPT="【代码审查讨论】

请审查以下代码：

\`\`\`python
$CODE
\`\`\`

从你的专业角度分析：
1. 代码质量（可读性、风格）
2. 算法效率（时间/空间复杂度）
3. 潜在问题（bug、安全、边界）
4. 改进建议（具体代码）

请给出专业深入的分析。"

echo "🔍 代码审查讨论"

# 并行提交
declare -A REQUEST_IDS

for provider in "${CODE_EXPERTS[@]}"; do
    if [ "$provider" = "codex" ]; then
        model="o3"
        agent="-a reviewer"
    elif [ "$provider" = "deepseek" ]; then
        model="reasoner"
        agent=""
    else
        model=""
        agent=""
    fi

    ID=$(ccb-submit $provider $model $agent "$PROMPT")
    REQUEST_IDS[$provider]=$ID
    echo "✓ $provider: $ID"
done

# 等待
sleep 45

# 收集
declare -A RESPONSES

for provider in "${CODE_EXPERTS[@]}"; do
    id=${REQUEST_IDS[$provider]}
    response=$(ccb-query get $id)
    RESPONSES[$provider]=$response
done

# 生成审查报告
cat > code_review_discussion.md <<EOF
# 多 AI 代码审查报告

**审查时间**: $(date)
**参与**: Codex (o3), DeepSeek (reasoner), Qwen

---

## 被审查代码

\`\`\`python
$CODE
\`\`\`

---

## 🐢 Codex (o3) 的审查

${RESPONSES[codex]}

---

## ⚡ DeepSeek (reasoner) 的审查

${RESPONSES[deepseek]}

---

## 🚀 Qwen 的审查

${RESPONSES[qwen]}

---

## Claude 综合结论

### 🔴 严重问题（必须修复）
[高优先级问题]

### 🟡 改进建议（建议修复）
[中优先级问题]

### 🟢 良好实践（保持）
[值得保留的设计]

### ✨ 最佳改进方案
[综合所有 AI 的建议，给出最优代码]

\`\`\`python
# 改进后的代码
[改进版本]
\`\`\`

EOF

echo "✅ 审查报告: code_review_discussion.md"
```

## 讨论提示模板

### 架构设计讨论

```
【架构讨论】
任务: {任务描述}

请从你的专长角度分析：
1. 整体架构设计（组件、层次、交互）
2. 关键技术选型（及选择理由）
3. 实现步骤（按优先级排序）
4. 潜在风险和应对策略

请提供简洁但深入的专业分析。
```

### 技术选型讨论

```
【技术选型】
背景: {项目背景}
需求: {核心需求}

请对比分析以下方案：
- 方案 A: {方案 A}
- 方案 B: {方案 B}
- 方案 C: {方案 C}

从以下维度评估：
1. 技术成熟度
2. 学习曲线
3. 性能表现
4. 生态系统
5. 长期维护

给出你的推荐及理由。
```

### 代码审查讨论

```
【代码审查】
请审查以下代码：

```[语言]
{代码}
```

从专业角度分析：
1. 代码质量（可读性、风格、注释）
2. 算法效率（时间/空间复杂度）
3. 潜在问题（bug、安全漏洞、边界条件）
4. 改进建议（请给出具体代码）

请深入分析。
```

### 问题诊断讨论

```
【问题诊断】
现象: {问题现象}
环境: {环境信息}
日志: {相关日志}

请分析：
1. 可能的根本原因（按可能性排序）
2. 诊断步骤（如何验证）
3. 解决方案（临时 + 长期）
4. 预防措施

请给出系统性的诊断分析。
```

## 报告格式模板

```markdown
# {主题} - 多 AI 讨论报告

**主题**: {讨论主题}
**参与**: {AI 列表}
**模式**: {快速/完整/专项}
**时间**: {时间戳}

---

## 📊 参与统计

| AI | 响应时间 | 状态 | 观点长度 |
|----|---------:|:----:|:--------:|
| ... | ...s | ✅ | ...字 |

---

## 💬 各 AI 观点

### [图标] {AI 名称} ({响应时间}s)

{AI 的完整回答}

---

## 🎯 Claude 综合汇总

### ✅ 共识点
1. {共识 1}
2. {共识 2}

### ⚠️ 分歧点
| 议题 | 观点 | 决策 |
|------|------|------|
| ... | ... | ... |

### 💡 独特贡献
- **{AI}**: {独特见解}

### 📋 执行建议
{综合建议}

---

**生成时间**: {时间戳}
```

## 最佳实践

1. **选择合适模式** - 日常用快速，重要用完整
2. **明确讨论主题** - 清晰的问题描述
3. **给足等待时间** - 快速 30s，完整 90s
4. **提取关键信息** - Claude 汇总共识和分歧
5. **记录独特见解** - 每个 AI 的独特贡献
6. **形成行动计划** - 讨论后的具体行动
7. **保存讨论记录** - 便于后续参考

## 适用场景

| 场景 | 推荐模式 | 说明 |
|------|----------|------|
| 架构设计 | 完整 | 需要多角度分析 |
| 技术选型 | 完整 | 对比不同观点 |
| 代码审查 | 专项（代码） | 聚焦代码质量 |
| 快速决策 | 快速 | 时间有限 |
| 方案对比 | 完整 | 需要全面评估 |
| 问题诊断 | 快速/完整 | 视复杂度 |

## 性能考虑

| 模式 | AI 数量 | 预计时间 | 成本 |
|------|---------|----------|------|
| 快速 | 3 | 30s | 低 |
| 完整 | 7 | 90s | 中 |
| 专项 | 3-5 | 45-60s | 低-中 |

---

*CCB-Discussion v1.0*
*Part of CCB Unified Platform*
