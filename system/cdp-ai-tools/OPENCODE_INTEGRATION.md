# OpenCode 集成指南

## 概述

OpenCode 可以通过 `ccb-cli` 调用 CDP AI Tools，实现与本地 AI 应用（豆包、阶跃AI、Ollama）的交互。

## 使用方式

### 方式 1: 让 OpenCode 直接调用 ai-chat

```bash
# 让 OpenCode 使用豆包
ccb-cli opencode "请使用 ai-chat doubao 命令问一下：什么是递归？"

# 让 OpenCode 使用 Ollama
ccb-cli opencode "请使用 ai-chat ollama --list-models 列出所有模型"

# 让 OpenCode 管理对话
ccb-cli opencode "请使用 ai-chat doubao --list-conversations 列出豆包的所有对话"
```

### 方式 2: 让 OpenCode 执行复杂的工作流

```bash
# 让 OpenCode 协调多个 AI
ccb-cli opencode "请执行以下任务：
1. 使用 ai-chat doubao 问：什么是递归？
2. 使用 ai-chat stepfun 问同样的问题
3. 使用 ai-chat ollama 问同样的问题
4. 比较三个 AI 的回答，总结差异"
```

### 方式 3: 在 Claude Code 中让 OpenCode 调用

```
用户: "让 OpenCode 用豆包帮我解释递归"

Claude 执行:
ccb-cli opencode "请使用 ai-chat doubao '请解释什么是递归'"
```

## 实际测试

让我测试一下 OpenCode 是否能成功调用：

```bash
# 测试 1: 列出 Ollama 模型
ccb-cli opencode "执行命令: ai-chat ollama --list-models"

# 测试 2: 列出豆包对话
ccb-cli opencode "执行命令: ai-chat doubao --list-conversations"

# 测试 3: 发送消息
ccb-cli opencode "使用 ai-chat doubao 发送消息：你好"
```

## 使用场景

### 场景 1: 多 AI 协作

```bash
ccb-cli opencode "请帮我做以下事情：
1. 用 ai-chat doubao 问：Python 的装饰器是什么？
2. 用 ai-chat stepfun 问：能举个装饰器的例子吗？
3. 用 ai-chat ollama 问：装饰器的应用场景有哪些？
4. 整合三个回答，给我一个完整的总结"
```

### 场景 2: 对话管理

```bash
ccb-cli opencode "请帮我管理豆包的对话：
1. 列出所有对话
2. 如果有超过 5 个对话，删除最旧的几个
3. 把第一个对话重命名为'重要对话'"
```

### 场景 3: 模型管理

```bash
ccb-cli opencode "请帮我管理 Ollama 模型：
1. 列出所有已安装的模型
2. 检查是否有 llama2 模型
3. 如果没有，帮我拉取 llama2 模型"
```

## 技术原理

```
用户 → Claude Code → ccb-cli → OpenCode → ai-chat → 本地 AI 应用
                                    ↓
                                执行 bash 命令
                                    ↓
                            调用 CDP/HTTP API
                                    ↓
                            返回结果给 OpenCode
                                    ↓
                            OpenCode 处理并返回
```

## 优势

1. **多 AI 协作**: OpenCode 可以协调多个本地 AI 应用
2. **智能调度**: OpenCode 可以根据任务选择合适的 AI
3. **自动化**: OpenCode 可以执行复杂的工作流
4. **统一接口**: 通过 ccb-cli 统一调用

## 注意事项

1. **确保 ai-chat 在 PATH 中**:
   ```bash
   which ai-chat  # 应该返回 /Users/leo/.local/bin/ai-chat
   ```

2. **确保本地 AI 应用正在运行**:
   - 豆包: 端口 9225
   - 阶跃AI: 端口 9224
   - Ollama: 端口 11434

3. **超时设置**: 对于复杂任务，可能需要增加超时时间:
   ```bash
   ccb-cli opencode -t 300 "长时间任务..."
   ```

## 示例脚本

创建一个快捷脚本 `opencode-ai`:

```bash
#!/bin/bash
# 让 OpenCode 调用本地 AI

AI_TYPE=$1
shift
MESSAGE="$@"

ccb-cli opencode "请使用 ai-chat $AI_TYPE 发送消息：$MESSAGE"
```

使用方式：
```bash
chmod +x opencode-ai
./opencode-ai doubao "你好"
./opencode-ai ollama "解释递归"
```

## 更新时间

2026-02-26
