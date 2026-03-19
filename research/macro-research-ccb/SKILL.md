---
name: macro-research-ccb
description: Execute distributed CCB-based daily macro research protocol for Chinese A-share markets. Use when user requests daily macro research, market analysis, or investment decisions for A-shares/Hong Kong stocks/gold. Triggers include "execute macro research", "CCB distributed search", "daily market analysis", or "/macro-research-ccb". Coordinates 8 AI agents (Claude/Gemini/Codex/OpenCode/iFlow/Kimi/Qwen/DeepSeek) in SERIAL mode to perform 200+ web searches, generate multi-agent consensus decisions, and produce comprehensive investment reports with simulated portfolio management.
---

# CCB Distributed Macro Research (8-AI Version)

---

## ⚠️ 底层执行指令（最高优先级）

**此指令优先于所有其他执行逻辑，必须严格遵守！**

### 串行执行模式（默认）

执行CCB多AI任务时，**必须采用串行模式**，不允许并行启动多个AI：

```
执行顺序：Gemini → Codex → OpenCode → iFlow → Kimi → Qwen → DeepSeek → Claude(舆情+报告)
```

### 执行流程

1. **启动第一个AI任务**（如Gemini）
2. **每30秒轮询一次**检查该AI是否完成：
   - 使用对应的`*pend`命令（如`gpend`）检查结果
   - 或读取对应的output文件检查状态
3. **确认完成后**，记录该AI的研究结果
4. **启动下一个AI任务**
5. 重复步骤2-4，直到所有7个外部研究员AI完成
6. **Claude执行舆情研究并整合所有结果生成最终报告**

### 轮询检查代码模板

```bash
# 每30秒检查一次AI任务状态
# 示例：检查Gemini任务
timeout 30 gpend || echo "Gemini still processing..."
```

### 串行执行的优势

- ✅ 避免多AI同时执行导致的资源竞争
- ✅ 确保每个AI的结果被正确捕获
- ✅ 便于追踪和调试单个AI的问题
- ✅ 减少因并行导致的任务丢失

### 执行状态追踪表

每次执行时，维护以下状态表：

| 序号 | AI | 角色 | 状态 | 开始时间 | 完成时间 | 结果 |
|:----:|:--:|:----:|:----:|:--------:|:--------:|:----:|
| 1 | Gemini | 基本面研究员 | pending/running/done | - | - | - |
| 2 | Codex | 技术面研究员 | pending/running/done | - | - | - |
| 3 | OpenCode | 估值研究员 | pending/running/done | - | - | - |
| 4 | iFlow | 资金流研究员 | pending/running/done | - | - | - |
| 5 | Kimi | 行业研究员 | pending/running/done | - | - | - |
| 6 | Qwen | 国际宏观研究员 | pending/running/done | - | - | - |
| 7 | DeepSeek | 政策研究员 | pending/running/done | - | - | - |
| 8 | Claude | 舆情研究员+报告整合 | pending/running/done | - | - | - |

---

Execute comprehensive daily macro research using CCB (Claude Code Bridge) distributed multi-agent architecture. **8 AI agents** work in **serial mode** to analyze Chinese A-share markets from multiple perspectives. All agents perform web searches for real-time data.

## AI Agent Roles (8 Agents)

### 研究员团队（8个，负责数据收集与分析）

| Agent | Role | Search Focus | Searches |
|:-----:|:-----|:-------------|:--------:|
| 🟢 **Gemini** | 基本面研究员 | 宏观经济、央行政策、财政政策 | 25次 |
| 🟣 **Codex** | 技术面研究员 | K线形态、技术指标、量价分析 | 25次 |
| 🟠 **OpenCode** | 估值研究员 | PE/PB估值、风险溢价、国际对比 | 25次 |
| 🔴 **iFlow** | 资金流研究员 | 主力资金、融资融券、ETF流向 | 25次 |
| 🟡 **Kimi** | 行业研究员 | 行业轮动、板块热点、产业链分析 | 25次 |
| 🟤 **Qwen** | 国际宏观研究员 | 美股、港股、汇率、大宗商品 | 25次 |
| 🔷 **DeepSeek** | 政策研究员 | 监管政策、政策预期差、政策解读 | 25次 |
| 🔵 **Claude** | 舆情研究员 + 报告整合 | 北向资金、社交媒体、新闻情绪 + 最终报告 | 25次 |

**总计：200次联网搜索（8个研究员 × 25次）**

### 未来扩展（待Grok接入后）

| Agent | Role | 职责 |
|:-----:|:-----|:-----|
| ⚫ **Grok** | 报告写手 + 可视化专家 | 整合8个研究员观点，撰写最终报告，生成数据可视化图表 |

---

## 📊 报告结构（重要！）

### 报告必须以"投资决策摘要"开头

报告的**第一部分**必须是精炼的投资决策摘要，类似研报摘要，包含：

```markdown
## 📊 投资决策摘要

### 🎯 核心要点（3-5条）
1. [最重要的市场信号]
2. [关键政策/数据变化]
3. [资金流向核心结论]
4. [技术面关键信号]
5. [估值核心判断]

### ⚡ 预期差（市场可能忽视的信息）
- [预期差1：xxx]
- [预期差2：xxx]

### 🟢 买入机会
- **板块**：[推荐板块及理由]
- **个股方向**：[推荐方向，不具体荐股]
- **时机**：[建议买入时机]

### 🔴 卖出/减仓关注
- **风险板块**：[需要警惕的板块]
- **止盈信号**：[何时考虑止盈]
- **止损触发**：[风险警示]

### 📈 今日操作建议
| 操作 | 方向 | 仓位变化 | 理由 |
|------|------|----------|------|
| [买入/卖出/持有] | [标的方向] | [+X%/-X%] | [简要理由] |
```

---

## 💰 模拟投资组合管理

### 投资经理身份设定

你是一位管理**1000万人民币**的投资经理，需要：
1. 每日根据研究结果调整组合
2. 详细说明每次调仓的理由
3. 追踪组合表现并复盘

### 投资纪律（强制规则）

| 规则 | 限制 | 说明 |
|------|------|------|
| **投资范围** | A股、港股、黄金 | 仅限这三类资产 |
| **单一持仓** | 2%-10% | 单个标的占比 |
| **单一行业** | ≤30% | 行业集中度上限 |
| **现金仓位** | 0%-50% | 根据市场情绪决定 |
| **止损线** | -8% | 单一持仓触发止损 |
| **止盈线** | +25%部分/+50%全部 | 分批止盈 |

### 组合输出格式

```markdown
## 💰 模拟投资组合（1000万人民币）

### 当前持仓
| 资产 | 类型 | 仓位 | 金额(万) | 成本 | 现价 | 盈亏 |
|------|------|------|----------|------|------|------|
| 沪深300ETF | A股 | 20% | 200 | 4.10 | 4.15 | +1.2% |
| 黄金ETF | 黄金 | 10% | 100 | 5.00 | 5.10 | +2.0% |
| ... | ... | ... | ... | ... | ... | ... |
| 现金 | 现金 | 15% | 150 | - | - | - |

### 今日调仓
| 操作 | 标的 | 变化 | 理由 |
|------|------|------|------|
| 加仓 | 半导体ETF | +5% | 政策利好+资金流入 |
| 减仓 | 消费ETF | -3% | 估值偏高+资金流出 |

### 调仓理由详解
[详细说明为什么做出这些调整，引用7个AI的研究结论]

### 组合表现追踪
| 日期 | 组合净值 | 日收益 | 累计收益 | 沪深300 | 超额收益 |
|------|----------|--------|----------|---------|----------|
| T-1 | 1.023 | +0.5% | +2.3% | +1.8% | +0.5% |
| T | 1.028 | +0.5% | +2.8% | +2.0% | +0.8% |
```

---

## Quick Start

**⚠️ IMPORTANT: 串行执行模式 - 一次只执行一个AI**

### 单阶段执行（推荐）
```
Today is [DATE], execute CCB distributed research in SERIAL mode
```

Claude will:
- Check all 8 AI connections
- Execute AI tasks **one by one** (not parallel)
- Poll every 30 seconds for completion
- Wait for each AI to finish before starting next
- Execute own sentiment research
- **Generate final report**

### 执行顺序（8个AI）
```
1. Gemini (基本面) → 等待完成 →
2. Codex (技术面) → 等待完成 →
3. OpenCode (估值) → 等待完成 →
4. iFlow (资金流) → 等待完成 →
5. Kimi (行业) → 等待完成 →
6. Qwen (国际宏观) → 等待完成 →
7. DeepSeek (政策) → 等待完成 →
8. Claude (舆情+报告整合) → 生成最终报告
```

---

## Workflow

### 串行执行流程（Serial Execution）

**Step 1: Check CCB Environment**
```bash
bash scripts/check_ccb_status.sh
```

**Step 2: 串行执行7个外部研究员AI任务（一次一个）**

⚠️ **必须按顺序执行，每个AI完成后才能启动下一个！**

**2.1 Gemini (基本面研究):**
```bash
# 启动任务
gask <<'EOF'
[Load: assets/task_templates/gemini_fundamental.txt]
EOF

# 每30秒轮询检查，直到完成
gpend
```
✅ 确认Gemini完成后，继续下一个

**2.2 Codex (技术面研究):**
```bash
cask <<'EOF'
[Load: assets/task_templates/codex_technical.txt]
EOF

cpend
```
✅ 确认Codex完成后，继续下一个

**2.3 OpenCode (估值研究):**
```bash
oask <<'EOF'
[Load: assets/task_templates/opencode_valuation.txt]
EOF

opend
```
✅ 确认OpenCode完成后，继续下一个

**2.4 iFlow (资金流研究):**
```bash
iask <<'EOF'
[Load: assets/task_templates/iflow_capital.txt]
EOF

ipend
```
✅ 确认iFlow完成后，继续下一个

**2.5 Kimi (行业研究):**
```bash
kask <<'EOF'
[Load: assets/task_templates/kimi_sector.txt]
EOF

kpend
```
✅ 确认Kimi完成后，继续下一个

**2.6 Qwen (国际宏观研究):**
```bash
qask <<'EOF'
[Load: assets/task_templates/qwen_global.txt]
EOF

qpend
```
✅ 确认Qwen完成后，继续下一个

**2.7 DeepSeek (政策研究):**
```bash
dskask <<'EOF'
[Load: assets/task_templates/deepseek_policy.txt]
EOF

# 等待DeepSeek完成（通过bash-notification）
```
✅ 确认DeepSeek完成后，继续Claude研究

**Step 3: Execute Own Research (Claude - 舆情研究)**

Claude executes 25 web searches covering:
- 北向资金流向 (10次)
- 社交媒体与新闻情绪 (10次)
- 市场情绪指标 (5次)

**Step 4: Claude生成最终报告**

整合所有8个研究员的结果，生成最终报告：
- 投资决策摘要
- 多Agent共识分析
- 投资经理辩论（激进/中性/保守）
- 风险管理委员会决议
- 模拟投资组合建议

1. **📊 投资决策摘要**（最重要！放在最前面）
   - 核心要点（3-5条）
   - 预期差
   - 买入机会
   - 卖出/减仓关注
   - 今日操作建议

2. **💰 模拟投资组合**
   - 当前持仓明细
   - 今日调仓及理由
   - 组合表现追踪

3. **🤖 多Agent共识决策**
   - 7研究员观点汇总
   - 3投资经理建议
   - 风控官审核

4. **📈 市场回顾**
   - A股、港股、美股
   - 大宗商品、汇率

5. **🏭 行业深度分析**
   - 热点板块
   - 产业链分析

6. **🌍 国际宏观环境**
   - 美联储政策
   - 地缘政治风险

7. **⏱️ 执行摘要**（3分钟速读版）

---

## Key Features

### 7-AI Serial Architecture

- **Reliability**: Each AI completes before next starts
- **Traceability**: Easy to identify which AI failed
- **Coverage**: 175+ web searches for comprehensive data
- **Independence**: Real AI disagreements, not simulated
- **Specialization**: Each AI focuses on domain expertise
- **Polling**: Check every 30 seconds for completion

### Multi-Agent Decision Framework

**Layer 1: 7 Researchers** (Independent opinions)
- 舆情研究员 (Claude) - 市场情绪
- 基本面研究员 (Gemini) - 宏观政策
- 技术面研究员 (Codex) - 技术指标
- 估值研究员 (OpenCode) - 估值水平
- 资金流研究员 (iFlow) - 资金动向
- 行业研究员 (Kimi) - 板块轮动
- 国际宏观研究员 (Qwen) - 外部环境

**Layer 2: 3 Portfolio Managers**
- 激进型PM (高风险容忍)
- 稳健型PM (平衡配置)
- 保守型PM (资本保全)

**Layer 3: Risk Officer**
- 风险矩阵分析
- VaR、夏普比率计算
- 批准/修改/否决决策

### Confidence Index Calculation

```
信心指数 = (研究员共识度 × 40% + 投资经理共识度 × 40% + 风控评级 × 20%) × 100

研究员共识度 = 一致观点数量 / 7
```

---

## Examples

**串行执行模式（推荐）:**
```
Today is 2026-01-27, execute CCB distributed research in SERIAL mode.
Initial capital: 10M RMB.
```

**带上下文的执行:**
```
Today is 2026-01-28, execute CCB distributed research in SERIAL mode.
Yesterday's portfolio: [paste holdings table]
Update portfolio and explain all adjustments with detailed reasoning.
```

**Weekend Review:**
```
This week is 2026-01-27 to 2026-01-31.
Summarize all adjustments, performance, correct/incorrect decisions.
Calculate weekly return vs benchmark.
Plan next week's strategy.
```

---

## Troubleshooting

**AI not responding:**
1. Test connection: `cping` / `gping` / `oping` / `iping` / `kping` / `qping`
2. If offline, Claude can substitute for that role
3. Report will note which AIs were real vs substituted

**Collect results:**
```bash
gpend  # Gemini
cpend  # Codex
opend  # OpenCode
ipend  # iFlow
kpend  # Kimi
qpend  # Qwen
```

---

## References

- **Search Protocol**: See `references/research_protocol.md` for 175-search allocation
- **Multi-Agent Framework**: See `references/multi_agent_framework.md` for decision architecture
- **Task Templates**: See `assets/task_templates/` for AI-specific prompts
