---
name: cdp-ai-tools
description: 通过 CDP 与本地 AI 应用交互（豆包、阶跃AI、Ollama），支持完整操作：对话管理、文件上传、设置修改等
triggers:
  - cdp
  - 豆包
  - doubao
  - 阶跃
  - stepfun
  - ollama
  - 本地ai
  - local ai
---

# CDP AI Tools - 本地 AI 应用交互工具

通过 Chrome DevTools Protocol (CDP) 与本地运行的 AI 应用进行交互，支持豆包（Doubao）、阶跃AI（StepFun）和 Ollama。

## 功能特性

- ✅ 统一接口：一个命令支持多个 AI 应用
- ✅ 连续对话：默认保留对话历史，支持多轮问答
- ✅ 对话管理：列出、切换、删除、重命名对话
- ✅ 快捷操作：点击快捷按钮（编程、数据分析等）
- ✅ 设置管理：打开和修改应用设置
- ✅ Ollama 支持：完整的 HTTP API 集成
- ✅ 自动发送：使用 Enter 键自动发送消息
- ✅ 灵活配置：支持超时设置、对话清理等选项
- ✅ CCB 集成：可与其他 AI 工具协同工作

## 支持的 AI 应用

| AI 应用 | 标识符 | 接口类型 | 端口/URL |
|---------|--------|---------|----------|
| 豆包 | `doubao` | CDP | 9225 |
| 阶跃AI | `stepfun` | CDP | 9224 |
| Ollama | `ollama` | HTTP API | 11434 |

## 使用方法

### 基本消息发送

```bash
# 使用豆包
ai-chat doubao "你好，请解释什么是递归"

# 使用阶跃AI
ai-chat stepfun "你好，请解释什么是递归"

# 使用 Ollama
ai-chat ollama --model qwen2.5:7b "你好"
```

### 对话管理（Doubao & StepFun）

```bash
# 列出所有对话
ai-chat doubao --list-conversations

# 切换到指定对话（按索引）
ai-chat doubao --switch 0

# 删除指定对话
ai-chat doubao --delete 1

# 重命名对话
ai-chat doubao --rename 0 "新对话名称"
```

### 快捷操作（Doubao & StepFun）

```bash
# 点击快捷操作按钮
ai-chat doubao --quick-action "编程"
ai-chat doubao --quick-action "数据分析"
ai-chat doubao --quick-action "帮我写作"
```

### 设置管理（Doubao & StepFun）

```bash
# 打开设置面板
ai-chat doubao --settings
ai-chat stepfun --settings
```

### Ollama 特有功能

```bash
# 列出所有模型
ai-chat ollama --list-models

# 显示模型详情
ai-chat ollama --show-model qwen2.5:7b

# 拉取新模型
ai-chat ollama --pull llama2

# 生成响应（非对话模式）
ai-chat ollama --generate qwen2.5:7b "解释递归"

# 流式输出
ai-chat ollama --stream "你好"
```

### 连续对话（默认）

```bash
# 第一个问题
ai-chat doubao "什么是递归？"

# 第二个问题（在同一个对话中）
ai-chat doubao "能举个例子吗？"

# 第三个问题（继续同一个对话）
ai-chat doubao "递归的时间复杂度如何计算？"
```

### 清理对话（开启新话题）

```bash
# 清理对话后发送新问题
ai-chat doubao --clear "这是一个新话题"
ai-chat stepfun --clear "这是一个新话题"
```

### 高级选项

```bash
# 自定义超时时间（秒）
ai-chat doubao --timeout 120 "复杂的问题"

# 指定 Ollama 服务器地址
ai-chat ollama --base-url http://192.168.1.100:11434 "你好"

# 查看帮助
ai-chat --help
```

## 在 Claude Code 中使用

### 触发方式

当用户提到以下关键词时，Claude Code 应该使用此 skill：

- "使用豆包"、"问豆包"、"让豆包"
- "使用阶跃"、"问阶跃"、"让阶跃"
- "使用 Ollama"、"问 Ollama"
- "本地AI"、"CDP"
- "连续对话"、"多轮对话"
- "对话管理"、"切换对话"

### 使用示例

**示例 1：单次问答**

```
用户: "用豆包帮我解释一下什么是递归"

Claude 应该执行:
ai-chat doubao "请解释什么是递归"
```

**示例 2：连续对话**

```
用户: "用豆包问一下什么是递归，然后再问能不能举个例子"

Claude 应该执行:
ai-chat doubao "什么是递归？"
# 等待响应后
ai-chat doubao "能举个例子吗？"
```

**示例 3：对话管理**

```
用户: "列出豆包的所有对话"

Claude 应该执行:
ai-chat doubao --list-conversations
```

**示例 4：使用 Ollama**

```
用户: "用 Ollama 的 qwen2.5 模型解释递归"

Claude 应该执行:
ai-chat ollama --model qwen2.5:7b "请解释什么是递归"
```

## 技术架构

### 文件结构

```
~/.claude/skills/cdp-ai-tools/
├── SKILL.md                      # 本文档
├── lib/
│   └── unified_cdp.py            # 统一 CDP 基类
├── doubao_full_controller.py     # 豆包完整控制器
├── stepfun_full_controller.py    # 阶跃AI完整控制器
├── ollama_controller.py          # Ollama HTTP API 控制器
├── button_controller.py          # 按钮操作控制器
└── explore_buttons.py            # 按钮探索工具

~/.local/bin/
└── ai-chat                       # 统一命令行工具
```

### 控制器功能对比

| 功能 | Doubao | StepFun | Ollama |
|------|--------|---------|--------|
| 基本消息发送 | ✅ | ✅ | ✅ |
| 连续对话 | ✅ | ✅ | ✅ |
| 列出对话 | ✅ | ✅ | ❌ |
| 切换对话 | ✅ | ✅ | ❌ |
| 删除对话 | ✅ | ✅ | ❌ |
| 重命名对话 | ✅ | ✅ | ❌ |
| 快捷操作 | ✅ | ✅ | ❌ |
| 设置管理 | ✅ | ✅ | ❌ |
| 模型管理 | ❌ | ❌ | ✅ |
| 流式输出 | ❌ | ❌ | ✅ |

## 开发指南

### 添加新的 AI 应用

1. 创建新的控制器文件（如 `newai_controller.py`）
2. 继承 `UnifiedCDP` 类（CDP 应用）或创建独立类（HTTP API 应用）
3. 实现必要的方法
4. 在 `ai-chat` 中添加新的选项
5. 更新 SKILL.md 文档

### 扩展现有功能

1. 在对应的控制器文件中添加新方法
2. 在 `ai-chat` 中添加命令行参数
3. 测试新功能
4. 更新文档

## 故障排除

### 连接失败

```bash
# 检查应用是否运行
ps aux | grep -i doubao
ps aux | grep -i stepfun

# 检查调试端口是否开启
lsof -i :9225  # 豆包
lsof -i :9224  # 阶跃AI
lsof -i :11434 # Ollama
```

### Ollama 连接失败

```bash
# 检查 Ollama 服务是否运行
curl http://localhost:11434/api/tags

# 启动 Ollama 服务
ollama serve
```

### 对话管理功能不工作

对话管理功能依赖于页面元素选择器，如果 AI 应用更新了界面，可能需要更新选择器。

## 更新日志

### v2.0.0 (2026-02-26)

- ✨ 添加完整的对话管理功能（列出、切换、删除、重命名）
- ✨ 添加快捷操作按钮支持
- ✨ 添加设置管理功能
- ✨ 添加 Ollama 完整支持
- ✨ 统一所有功能到 ai-chat 命令
- 📝 更新文档，添加完整的使用指南

### v1.0.0 (2026-02-25)

- 🎉 初始版本
- ✅ 支持豆包和阶跃AI基本消息发送
- ✅ 支持连续对话
- ✅ 统一 CDP 接口

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！

## OpenCode 集成

### OpenCode 可以调用 CDP AI Tools

OpenCode 可以通过 `ccb-cli` 调用 `ai-chat` 命令，实现与本地 AI 应用的交互。

#### 基本用法

```bash
# 让 OpenCode 使用豆包
ccb-cli opencode "请使用 ai-chat doubao 问：什么是递归？"

# 让 OpenCode 使用 Ollama
ccb-cli opencode "请执行命令: ai-chat ollama --list-models"

# 让 OpenCode 管理对话
ccb-cli opencode "请使用 ai-chat doubao --list-conversations"
```

#### 快捷脚本

使用 `opencode-ai` 快捷脚本：

```bash
# 直接使用
opencode-ai doubao "你好"
opencode-ai ollama "解释递归"
opencode-ai stepfun "什么是装饰器"
```

#### 多 AI 协作

```bash
ccb-cli opencode "请执行以下任务：
1. 用 ai-chat doubao 问：Python 的装饰器是什么？
2. 用 ai-chat stepfun 问：能举个例子吗？
3. 用 ai-chat ollama 问：应用场景有哪些？
4. 整合三个回答给我总结"
```

#### 技术原理

```
用户 → ccb-cli → OpenCode → ai-chat → 本地 AI 应用
                     ↓
                 执行命令
                     ↓
                 返回结果
```

详细文档: `cat ~/.claude/skills/cdp-ai-tools/OPENCODE_INTEGRATION.md`
