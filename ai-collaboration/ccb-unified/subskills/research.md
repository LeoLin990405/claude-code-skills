# CCB-Research - 深度研究（Subagent + CCB）

## 概述

结合 Claude Code 的 Explore Subagent 和 CCB 的多 AI 能力，进行深度代码库研究和专业分析。

## 架构

```
用户研究请求
    ↓
Claude (主编排)
    ↓
启动 Explore Subagent → 探索代码库
    ↓
获取探索结果
    ↓
并行提交给多个 CCB Providers ← Gateway API
    ↓
收集所有 AI 的分析
    ↓
Claude 整合生成报告
```

## 研究类型

| 类型 | 说明 | Subagent | CCB Providers |
|------|------|----------|---------------|
| `architecture` | 架构分析 | Explore | Kimi, Qwen, Gemini |
| `security` | 安全审查 | Explore | Codex, DeepSeek, Kimi |
| `performance` | 性能优化 | Explore | Qwen, Codex, DeepSeek |
| `refactor` | 重构建议 | Explore | Codex, Gemini, Kimi |
| `dependency` | 依赖分析 | Explore | Qwen, Kimi |
| `custom` | 自定义研究 | 用户指定 | 用户指定 |

## 使用方法

### 架构分析

```bash
# 研究项目架构
研究目标: 分析 CCB 项目的整体架构

步骤:
1. 启动 Explore Subagent
2. 探索关键模块和文件
3. 提交给 Kimi (中文总结), Qwen (数据结构), Gemini (架构建议)
4. 生成综合报告
```

### 安全审查

```bash
# 安全漏洞扫描
研究目标: 识别潜在的安全问题

步骤:
1. Explore Subagent 查找敏感代码模式
2. 提交给 Codex (代码审查), DeepSeek (逻辑分析), Kimi (总结)
3. 生成安全报告
```

### 性能优化

```bash
# 性能瓶颈分析
研究目标: 识别性能瓶颈并提出优化建议

步骤:
1. Explore Subagent 查找热点代码
2. 提交给 Qwen (算法分析), Codex (优化建议), DeepSeek (推理)
3. 生成性能报告
```

## 实现示例

### 示例 1: 完整架构研究

```python
# Step 1: 启动 Explore Subagent
Task(
    subagent_type="Explore",
    prompt="""
    探索 ~/.local/share/codex-dual 项目:
    1. 识别主要模块和目录结构
    2. 查找关键入口文件
    3. 分析模块之间的依赖关系
    4. 识别设计模式
    """,
    description="探索 CCB 架构",
    model="sonnet"  # 使用快速模型
)

# Step 2: 获取探索结果
# exploration_result = [Subagent 返回的内容]

# Step 3: 并行提交给 CCB
```

```bash
# 继续 (Bash)
EXPLORATION_FILE="exploration_result.md"

# 并行提交给 3 个 AI 分析
ID1=$(ccb-submit kimi "中文总结以下项目架构: $(cat $EXPLORATION_FILE)")
ID2=$(ccb-submit qwen "分析以下数据结构和算法: $(cat $EXPLORATION_FILE)")
ID3=$(ccb-submit gemini 3p "建议架构优化方案: $(cat $EXPLORATION_FILE)")

echo "✓ 已提交给 3 个 AI 分析"
echo "Kimi: $ID1"
echo "Qwen: $ID2"
echo "Gemini: $ID3"

# Step 4: 等待完成
sleep 45

# Step 5: 收集结果
KIMI_RESULT=$(ccb-query get $ID1)
QWEN_RESULT=$(ccb-query get $ID2)
GEMINI_RESULT=$(ccb-query get $ID3)

# Step 6: 生成报告
cat <<EOF > architecture_analysis_$(date +%Y%m%d).md
# CCB 项目架构分析报告

**生成时间**: $(date)
**研究方法**: Explore Subagent + Multi-AI Analysis

---

## 1. 代码库探索 (Explore Subagent)

$(cat $EXPLORATION_FILE)

---

## 2. 中文架构总结 (Kimi)

$KIMI_RESULT

---

## 3. 数据结构分析 (Qwen)

$QWEN_RESULT

---

## 4. 架构优化建议 (Gemini)

$GEMINI_RESULT

---

## 5. 综合结论 (Claude)

[Claude 综合以上三个 AI 的分析，给出最终结论]

EOF

echo "✅ 报告已生成: architecture_analysis_$(date +%Y%m%d).md"
```

### 示例 2: 安全审查流程

```python
# Step 1: Explore Subagent 查找安全敏感代码
Task(
    subagent_type="Explore",
    prompt="""
    安全审查 ~/.local/share/codex-dual:
    1. 查找所有处理用户输入的代码
    2. 识别 SQL 查询（SQL 注入风险）
    3. 查找文件操作（路径遍历风险）
    4. 识别认证和授权逻辑
    5. 查找加密和密钥管理
    """,
    description="安全扫描",
    model="sonnet"
)
```

```bash
# Step 2: 提交给安全专家 AI
SECURITY_FINDINGS="security_findings.md"

ID1=$(ccb-submit codex o3 -a reviewer "代码安全审查: $(cat $SECURITY_FINDINGS)")
ID2=$(ccb-submit deepseek reasoner "逻辑漏洞分析: $(cat $SECURITY_FINDINGS)")
ID3=$(ccb-submit kimi "总结安全风险并给出优先级: $(cat $SECURITY_FINDINGS)")

# Step 3: 收集并生成安全报告
# [同上]
```

### 示例 3: 性能优化研究

```python
# Step 1: Explore Subagent 查找性能热点
Task(
    subagent_type="Explore",
    prompt="""
    性能分析 ~/.local/share/codex-dual:
    1. 查找循环嵌套深的代码
    2. 识别数据库查询（N+1 问题）
    3. 查找大文件读写操作
    4. 识别缓存使用
    5. 查找并发和异步代码
    """,
    description="性能扫描",
    model="haiku"  # 快速模型足够
)
```

```bash
# Step 2: 提交给性能专家 AI
PERF_ANALYSIS="performance_analysis.md"

ID1=$(ccb-submit qwen "算法复杂度分析: $(cat $PERF_ANALYSIS)")
ID2=$(ccb-submit codex o4-mini "代码优化建议: $(cat $PERF_ANALYSIS)")
ID3=$(ccb-submit deepseek "深度推理性能瓶颈: $(cat $PERF_ANALYSIS)")

# Step 3: 生成性能报告
# [同上]
```

## Subagent 配置

### Explore Subagent 参数

```python
Task(
    subagent_type="Explore",
    prompt="研究任务描述",
    description="简短描述 (3-5 词)",
    model="sonnet",  # sonnet | haiku | opus
    # thoroughness 参数 (在 prompt 中指定)
    # "quick" | "medium" | "very thorough"
)
```

### Thoroughness 级别

| 级别 | 适用场景 | 搜索深度 |
|------|---------|----------|
| `quick` | 快速探索、已知目标 | 基础搜索 |
| `medium` | 一般研究、中等复杂度 | 中等深度 |
| `very thorough` | 深度研究、复杂项目 | 全面搜索 |

## 研究报告模板

```markdown
# [研究类型] 分析报告

**项目**: [项目名称]
**研究目标**: [目标描述]
**生成时间**: [时间戳]
**研究方法**: Explore Subagent + Multi-AI Analysis

---

## 执行摘要

[3-5 句话总结关键发现]

---

## 1. 代码库探索 (Explore Subagent)

### 探索范围
- 文件数: [数量]
- 目录数: [数量]
- 关键模块: [列表]

### 关键发现
1. [发现 1]
2. [发现 2]
3. [...]

### 探索详情
[Subagent 的完整输出]

---

## 2. [AI 1 名称] 的分析

### 分析角度
[AI 的专长和分析角度]

### 关键观点
1. [观点 1]
2. [观点 2]

### 详细分析
[AI 的完整回答]

---

## 3. [AI 2 名称] 的分析

[同上]

---

## 4. [AI 3 名称] 的分析

[同上]

---

## 5. 综合结论 (Claude)

### 共识点
[所有 AI 都同意的观点]

### 分歧点
[AI 之间有分歧的地方]

### 推荐行动
1. [优先级高]
2. [优先级中]
3. [优先级低]

---

**附录**
- 探索原始数据: `exploration_raw.json`
- AI 响应原始数据: `ai_responses/`
```

## 最佳实践

1. **明确研究目标** - 在 Subagent prompt 中清晰描述
2. **选择合适的 thoroughness** - 避免过度探索
3. **选择专长匹配的 AI** - 安全找 Codex，中文找 Kimi
4. **并行提交** - 充分利用异步能力
5. **保存中间结果** - 便于追溯和复现
6. **结构化报告** - 使用统一的模板

## 性能考虑

### 时间估算

| 阶段 | 时间 | 备注 |
|------|------|------|
| Explore Subagent | 30-120s | 取决于项目大小和 thoroughness |
| CCB 并行分析 | 30-60s | 取决于 Provider 速度 |
| 报告生成 | 10-30s | Claude 整合 |
| **总计** | **70-210s** | **约 1-3.5 分钟** |

### 成本估算

```bash
# 估算单次研究成本
# Explore Subagent: ~5k tokens
# CCB 3 个 AI: ~15k tokens total
# 报告生成: ~2k tokens
# 总计: ~22k tokens ≈ $0.05 USD
```

## 故障排查

### Subagent 超时

```python
# 降低 thoroughness
Task(
    subagent_type="Explore",
    prompt="研究任务 (thoroughness: quick)",  # 降低级别
    description="快速探索",
    model="haiku"  # 使用更快的模型
)
```

### CCB Provider 失败

```bash
# 使用备选 Provider
if ! ccb-query get $ID1; then
    echo "Kimi 失败，使用 Qwen 作为备选"
    ID1_BACKUP=$(ccb-submit qwen "$(cat task1.txt)")
fi
```

---

*CCB-Research v1.0*
*Part of CCB Unified Platform*
