# Anthropic 安全政策

> 由 Gemini 整理

## 1. Claude 宪法 (Claude Constitution)
**来源:** https://www.anthropic.com/constitution

### 核心内容要点
- **定义**: Claude 的"宪法"是其价值观和行为准则的集合，是训练过程的核心
- **目标**: 确保 Claude 在任何情况下都表现出安全、有益的行为
- **核心理念**: 强调培养"判断力"而非死板遵守规则

### 核心价值观优先级 (冲突时按此顺序)
1. **广泛安全 (Broadly safe)**: 不破坏人类监督
2. **广泛道德 (Broadly ethical)**: 诚实，不造成伤害
3. **遵守指南 (Compliant with Anthropic's guidelines)**: 符合具体操作规范
4. **真正有益 (Genuinely helpful)**: 积极帮助用户和社会

### 指令处理层级
```
Anthropic (最高权威)
    ↓
Operators (API 开发者)
    ↓
Users (终端用户)
```

### 关键概念
| 术语 | 说明 |
|------|------|
| Claude 的宪法 | 塑造 AI 行为的根本法则 |
| 判断力与价值观 | 宪法旨在培养的高级认知能力 |
| 负责人层级 | 处理多方指令时的优先级逻辑 |
| 操作者 vs 用户 | API 开发者与终端用户的区分 |
| 可纠正性 | AI 接受纠正并能停止行动的关键安全特性 |
| 评估意识 | 模型识别自己正处于测试环境中的能力 |

---

## 2. 透明度政策 (Transparency)
**来源:** https://www.anthropic.com/transparency

### 核心内容要点
- **透明度中心**: 集中展示 Anthropic 负责任 AI 开发的流程、计划和实践
- **模型报告**: 详细披露 Claude 各版本的性能、安全评估结果和部署保障措施
- **内容涵盖**: 架构、训练数据、硬件、能力基准及局限性

### 安全评估重点
- CBRN (生化核放) 风险评估
- 自主研发能力评估
- 网络安全风险评估
- 多语言无害性测试

### 关键概念
| 术语 | 说明 |
|------|------|
| 模型系统卡片 | 模型的"说明书"，包含性能、局限和安全信息 |
| 负责任扩展政策 (RSP) | 评估和管理灾难性风险的核心框架 |
| AI 安全级别标准 (ASL) | 随模型能力提升而升级的安全防护分级体系 |
| CBRN 评估 | 针对化学、生物、放射性、核威胁的专项测试 |
| 提示注入 | 一种常见的攻击手段，需在开发中重点防御 |
| RLHF/RLAIF | 利用人类或 AI 反馈来微调模型行为的关键技术 |

---

## 3. 负责任扩展政策 (RSP)
**来源:** https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy

### 核心承诺
> 在未实施充分的保障措施之前，绝不训练或部署高风险模型

### 核心原则
- **比例保护原则**: 保障措施的强度必须与模型的潜在风险成正比

### 能力阈值 (触发更高安全措施���红线)
1. **自主 AI 研发**: 模型能独立进行复杂的 AI 研究
2. **CBRN 武器**: 模型能协助制造或使用大规模杀伤性武器

### AI 安全级别 (ASL)
| 级别 | 说明 |
|------|------|
| ASL-1 | 基础安全措施 |
| ASL-2 | 当前所有模型运行级别 |
| ASL-3 | 高级安全措施 (部分模型) |
| ASL-4+ | 最高级别安全措施 |

### 关键概念
| 术语 | 说明 |
|------|------|
| 负责任扩展政策 (RSP) | 管理前沿 AI 风险的最高纲领 |
| 能力阈值 | 触发安全升级的红线 |
| 比例保护 | 风险与防御相匹配的原则 |
| 红队测试 | 模拟攻击以发现漏洞 |
| 负责任扩展官 | 监督政策执行的专门职位 |

---

## 安全相关链接

| 资源 | 链接 |
|------|------|
| Claude 宪法 | https://www.anthropic.com/constitution |
| 透明度中心 | https://www.anthropic.com/transparency |
| 安全与合规 | https://trust.anthropic.com |
| RSP 政策 | https://www.anthropic.com/news/announcing-our-updated-responsible-scaling-policy |
