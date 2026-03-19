# CCB-STEM - STEM 学术建模（8 模型分布式协作）

## 概述

使用 CCB 的 8 模型分布式架构（Claude/Gemini/Codex/OpenCode/iFlow/Kimi/Qwen/DeepSeek）进行 STEM 学术研究笔记、数学推导、工程文档和科学论文的创建。

## 8 模型架构（The Eight Sages）

```
                    Claude (逻辑架构师 & 编排者)
                              │
              ┌───────────────┼───────────────┐
              │               │               │
              ▼               ▼               ▼
       ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌──────────┐
       │  Gemini  │    │   Qwen   │    │   Kimi   │    │ DeepSeek │
       │ (SOTA)   │    │  (Math)  │    │(Chinese) │    │(Reasoning)│
       └────┬─────┘    └────┬─────┘    └────┬─────┘    └────┬─────┘
            │               │               │               │
            └───────────────┼───────────────┴───────────────┘
                            │
              ┌─────────────┼─────────────┐
              │             │             │
              ▼             ▼             ▼
       ┌──────────┐  ┌──────────┐  ┌──────────┐
       │  Codex   │  │  iFlow   │  │ OpenCode │
       │  (Code)  │  │(Diagrams)│  │  (Audit) │
       └────┬─────┘  └────┬─────┘  └────┬─────┘
            │             │             │
            └─────────────┼─────────────┘
                          │
                          ▼
                       Claude
                 (最终整合)
```

## 8 模型分工

| AI | 模型 | 核心职责 | 独特能力 |
|----|------|----------|----------|
| 🟢 **Claude** | Opus 4.6 | 编排 & 逻辑架构 | 中央协调 |
| 🔵 **Gemini** | 3-Flash | SOTA 研究 | 实时网络搜索 |
| 🟣 **Codex** | GPT-5/o3 | 代码实现 | 最佳代码生成 |
| 🟠 **OpenCode** | DeepSeek-V3 | 中文学术写作 | 最佳中文 |
| 🔷 **iFlow** | Cursor/GLM | Mermaid 图表 | 最佳图表 |
| 🔴 **Kimi** | Kimi | 代码审计 | 全面审查 |
| 🟡 **Qwen** | Qwen2.5 | 数学推导 | 最佳数学 |
| ⚫ **DeepSeek** | DeepSeek-V3/R1 | 深度推理 | 最佳逻辑 |

## 执行模式

### 模式 1: 自动串行（推荐）

```
Gemini(SOTA) → Qwen(Math) → OpenCode(中文) → Codex(Code) →
iFlow(Diagram) → Kimi(Audit) → DeepSeek(Reasoning) → Claude(整合)
```

**时间**: 约 10-15 分钟
**质量**: 最高

### 模式 2: 交互式（逐步确认）

每个 AI 完成后展示结果，等待用户确认再继续。

**时间**: 约 15-20 分钟（含确认）
**质量**: 最高 + 可控

## 使用方法

### 基本用法

```
研究主题: "随机森林算法的数学原理与实现"

模式: auto-pilot

Claude 将自动：
1. 编排 8 个 AI 的任务
2. 串行执行（一个完成后启动下一个）
3. 整合所有输出
4. 生成完整的学术笔记
```

### 高级用法

```
研究主题: "量子纠缠的信息论解释"

模式: interactive

指定输出文件: /path/to/quantum_entanglement_notes.md

要求:
- 包含 Mermaid 图表
- 中文案例研究
- Python 代码实现
- LaTeX 数学推导
```

## 研究笔记结构

```markdown
# {研究主题}

**创建时间**: {时间}
**研究方法**: 8-AI 分布式协作
**文件版本**: v1.0

---

## 📋 执行摘要 (Claude)

[3-5 句话概括核心发现]

---

## 🔵 SOTA 文献综述 (Gemini)

### 最新论文 (2024-2026)
1. [论文标题](DOI) - {venue}, {year}
   - 核心贡献: ...

### 基准对比
| 方法 | 指标 1 | 指标 2 | 发表 |
|------|--------|--------|------|
| ... | ... | ... | ... |

---

## 🟡 数学推导 (Qwen)

### 核心定理

$$
\begin{aligned}
f(x) &= \int_0^x g(t) \, dt \\
     &= G(x) - G(0)
\end{aligned}
$$

**证明**:
[逐步推导]

### 复杂度分析
| 维度 | 复杂度 | 证明 |
|------|--------|------|
| 时间 | O(n log n) | [证明] |
| 空间 | O(n) | [证明] |

---

## 🟣 代码实现 (Codex)

### 算法实现

\`\`\`python
from typing import List, Optional
import numpy as np

def algorithm(data: np.ndarray,
              params: dict) -> np.ndarray:
    """
    算法实现。

    Args:
        data: 输入数据
        params: 参数字典

    Returns:
        处理后的结果
    """
    # 实现代码
    pass

# 使用示例
result = algorithm(data, params)
\`\`\`

### 可视化

\`\`\`python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(1, 2, figsize=(12, 5))
# 绘图代码
\`\`\`

---

## 🔷 流程图 (iFlow)

### 算法流程

\`\`\`mermaid
flowchart TD
    A["输入数据"] --> B["预处理"]
    B --> C["核心算法"]
    C --> D["后处理"]
    D --> E["输出结果"]
\`\`\`

### 系统架构

\`\`\`mermaid
classDiagram
    class Model {
        +fit(X, y)
        +predict(X)
    }
\`\`\`

---

## 🟠 案例研究 (OpenCode - 中文)

### 案例 1: {标题}

**研究背景**
[中文描述]

**数据与方法**
- 数据规模: {具体数字}
- 分析方法: {具体方法}

**关键发现**
1. [发现 1 + 数据支持]
2. [发现 2 + 数据支持]

**启示**
[实践意义]

---

## 🔴 代码审计 (Kimi)

### 技术审计报告

| 指标 | 实际 | 目标 | 状态 |
|------|------|------|------|
| 代码模块 | 5 | ≥5 | ✅ |
| 语法错误 | 0 | 0 | ✅ |
| 文档覆盖 | 100% | ≥90% | ✅ |

### 发现问题
[列出问题及修复建议]

---

## ⚫ 深度推理分析 (DeepSeek)

### 推理链

**前提**:
1. [前提 1]
2. [前提 2]

**推理步骤**:
1. 由前提 1 和前提 2，可得...
2. 进一步推导...
3. 因此...

**结论**:
[最终结论]

### 政策影响分析
[相关政策、监管、伦理考虑]

---

## 📚 参考文献

1. [作者]. ({年}). {标题}. *{期刊}*, {卷}({期}), {页码}. DOI: {doi}

---

## 📎 附录

### A. 完整推导
[详细数学推导]

### B. 代码仓库
[GitHub 链接]

---

**文档状态**: ✅ 完成
**最后更新**: {时间}
**贡献者**: 8-AI Collaborative Team
```

## 使用 CCB + Subagent

### 方法 1: 直接 CCB 调用（串行）

```bash
# 串行执行 8 个 AI
# Step 1: Gemini SOTA
ID1=$(ccb-submit gemini 3f "SOTA research: {topic}")
sleep 30
SOTA=$(ccb-query get $ID1)

# Step 2: Qwen 数学
ID2=$(ccb-submit qwen "数学推导: {topic}, 基于: $SOTA")
sleep 30
MATH=$(ccb-query get $ID2)

# Step 3-8: 继续其他 AI...

# 最终整合
```

### 方法 2: 结合 Explore Subagent

```python
# Step 1: Explore Subagent 搜集文献
Task(
    subagent_type="Explore",
    prompt="搜集关于 {topic} 的学术论文和代码实现",
    description="文献综述",
    model="sonnet"
)

# Step 2: 获取文献后，启动 8-AI 协作
# 使用 Bash 或直接 ccb 命令
```

## 质量检查清单

### 内容要求
- [ ] 10+ LaTeX 公式 (Qwen)
- [ ] 5+ 代码示例 (Codex)
- [ ] 3+ Mermaid 图表 (iFlow)
- [ ] 3+ 中文案例 (OpenCode)
- [ ] 5+ SOTA 引用 (Gemini)
- [ ] 语法验证通过 (Kimi)
- [ ] 深度推理分析 (DeepSeek)

### 格式要求
- [ ] Mermaid 使用 `A["text"]` 格式
- [ ] LaTeX 在独立 `$$` 块
- [ ] 表格对齐正确
- [ ] 代码块有语言标签

## 命令参考

```bash
# 旧的 CLI 命令（stem-modeling skill）
gask <<'EOF'
[Gemini SOTA task]
EOF

qask <<'EOF'
[Qwen Math task]
EOF

# 新的统一方式（ccb-unified）
ccb-submit gemini 3f "[SOTA task]"
ccb-submit qwen "[Math task]"
ccb-submit opencode "[Chinese task]"
ccb-submit codex o3 "[Code task]"
ccb-submit iflow "[Diagram task]"
ccb-submit kimi "[Audit task]"
ccb-submit deepseek reasoner "[Reasoning task]"
```

## 时间估算

| 阶段 | AI | 时间 |
|------|----|----|
| SOTA 研究 | Gemini | 60-90s |
| 数学推导 | Qwen | 60-90s |
| 中文案例 | OpenCode | 60-90s |
| 代码实现 | Codex | 90-120s |
| 图表生成 | iFlow | 60-90s |
| 代码审计 | Kimi | 60-90s |
| 深度推理 | DeepSeek | 90-120s |
| 整合报告 | Claude | 60s |
| **总计** | **8 AI** | **10-15 分钟** |

## 最佳实践

1. **明确研究主题** - 清晰的问题定义
2. **串行执行** - 确保每个 AI 完成后再启动下一个
3. **保存中间结果** - 便于追溯和复现
4. **检查语法** - Kimi 审计非常重要
5. **整合报告** - Claude 最终整合所有内容
6. **版本控制** - 保存到 Git 仓库

## 适用场景

| 场景 | 说明 |
|------|------|
| STEM 研究笔记 | 数学、物理、工程 |
| 算法推导 | 理论 + 实现 |
| 工程文档 | 技术规范 |
| 科学论文草稿 | 学术写作 |
| 教学材料 | 讲义、实验 |

## 与 stem-modeling skill 的关系

**ccb-stem** 是对原 `stem-modeling` skill 的现代化改造：

| 特性 | stem-modeling | ccb-stem |
|------|---------------|----------|
| AI 数量 | 8 | 8（相同） |
| 调用方式 | 旧 CLI 命令（gask, qask等） | ccb-submit（统一） |
| 执行模式 | 串行 | 串行/并行可选 |
| Subagent | 不支持 | 支持 Explore |
| 异步 | 有限支持 | 完全异步 |
| 监控 | 无 | Gateway 监控 |

---

*CCB-STEM v1.0*
*Part of CCB Unified Platform*
*Based on STEM_SOP V7.0*
