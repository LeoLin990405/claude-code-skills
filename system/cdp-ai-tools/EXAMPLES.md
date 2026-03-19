# CDP AI Tools - 使用示例

## 场景 1：快速问答

### 使用豆包

```bash
$ ai-chat doubao "什么是递归？"
✓ 已连接到豆包: doubao://doubao-chat/chat/...
✓ 消息已发送
⏳ 等待响应...
💡 消息已成功发送到豆包，请在应用中查看响应
```

### 使用阶跃AI

```bash
$ ai-chat stepfun "什么是递归？"
✓ 已连接到阶跃AI: http://127.0.0.1:63008/chats/...
✓ 消息已发送
⏳ 等待响应...
💡 消息已成功发送到阶跃AI，请在应用中查看响应
```

## 场景 2：连续对话

```bash
# 第一个问题
$ ai-chat doubao "什么是递归？"
✓ 消息已发送

# 第二个问题（在同一个对话中）
$ ai-chat doubao "能举个例子吗？"
✓ 消息已发送

# 第三个问题（继续同一个对话）
$ ai-chat doubao "递归的时间复杂度如何计算？"
✓ 消息已发送
```

## 场景 3：清理对话

```bash
# 清理对话后发送新问题
$ ai-chat doubao --clear "这是一个新话题"
✓ 消息已发送
✓ 对话已清理
```

## 场景 4：自定义超时

```bash
# 对于复杂问题，增加超时时间
$ ai-chat doubao --timeout 120 "请详细分析这段代码的性能问题..."
✓ 消息已发送
⏳ 等待响应...（最多等待120秒）
```

## 场景 5：在 Claude Code 中使用

### 示例 1：单次问答

**用户输入：**
```
用豆包帮我解释一下什么是递归
```

**Claude Code 执行：**
```bash
ai-chat doubao "请解释什么是递归"
```

### 示例 2：连续对话

**用户输入：**
```
用豆包帮我学习递归，我想深入了解
```

**Claude Code 执行：**
```bash
# 第一个问题
ai-chat doubao "请详细解释什么是递归"

# 等待用户查看响应后，继续
ai-chat doubao "能举一个实际的代码例子吗？"

# 继续深入
ai-chat doubao "递归的优缺点是什么？"
```

### 示例 3：切换 AI

**用户输入：**
```
用阶跃AI再问一遍同样的问题
```

**Claude Code 执行：**
```bash
ai-chat stepfun --clear "请详细解释什么是递归"
```

### 示例 4：对比不同 AI 的回答

**用户输入：**
```
分别用豆包和阶跃AI回答这个问题，看看有什么不同
```

**Claude Code 执行：**
```bash
# 使用豆包
ai-chat doubao --clear "请解释什么是机器学习"

# 使用阶跃AI
ai-chat stepfun --clear "请解释什么是机器学习"
```

## 场景 6：与其他工具结合

### 与 CCB 集成

```bash
# 使用 Kimi
ccb-cli kimi "请解释什么是递归"

# 使用豆包
ai-chat doubao "请解释什么是递归"

# 使用 Gemini
ccb-cli gemini "请解释什么是递归"
```

### 批量处理

```bash
# 创建一个脚本
cat > ask_multiple.sh << 'EOF'
#!/bin/bash
questions=(
    "什么是递归？"
    "什么是动态规划？"
    "什么是贪心算法？"
)

for q in "${questions[@]}"; do
    echo "问题: $q"
    ai-chat doubao --clear "$q"
    sleep 5
done
EOF

chmod +x ask_multiple.sh
./ask_multiple.sh
```

## 场景 7：调试和故障排除

### 检查连接

```bash
# 检查豆包
curl http://localhost:9225/json | python3 -m json.tool

# 检查阶跃AI
curl http://localhost:9224/json | python3 -m json.tool
```

### 查看详细日志

```bash
# 使用 Python 直接运行，查看详细输出
cd ~/.claude/skills/cdp-ai-tools
python3 ai-chat doubao "测试消息"
```

## 场景 8：自动化工作流

### 代码审查助手

```bash
#!/bin/bash
# code_review.sh

# 读取代码文件
code=$(cat my_code.py)

# 使用豆包审查
ai-chat doubao --clear "请审查这段代码：\n$code"

# 等待响应
sleep 10

# 使用阶跃AI再审查一次
ai-chat stepfun --clear "请审查这段代码：\n$code"
```

### 学习助手

```bash
#!/bin/bash
# learning_assistant.sh

topic="$1"

# 第一步：基础概念
ai-chat doubao --clear "请解释 $topic 的基础概念"
sleep 5

# 第二步：深入理解
ai-chat doubao "请深入解释 $topic 的原理"
sleep 5

# 第三步：实践应用
ai-chat doubao "请给出 $topic 的实际应用例子"
sleep 5

# 第四步：常见问题
ai-chat doubao "关于 $topic，有哪些常见的误区和注意事项？"
```

使用：
```bash
./learning_assistant.sh "递归"
```

## 场景 9：多语言支持

```bash
# 中文
ai-chat doubao "什么是递归？"

# 英文
ai-chat doubao "What is recursion?"

# 混合
ai-chat doubao "请用中文解释 recursion"
```

## 场景 10：错误处理

### 连接失败

```bash
$ ai-chat doubao "测试"
✗ 连接失败: Connection refused

# 解决方法：启动豆包
/Applications/Doubao.app/Contents/MacOS/Doubao --remote-debugging-port=9225 &
```

### 超时

```bash
$ ai-chat doubao --timeout 10 "复杂问题"
✓ 消息已发送
⏳ 等待响应...
消息已发送到豆包，请在应用中查看响应。

# 解决方法：增加超时时间
ai-chat doubao --timeout 120 "复杂问题"
```

## 最佳实践

### 1. 连续对话时保持上下文

```bash
# ✅ 好的做法
ai-chat doubao "什么是递归？"
ai-chat doubao "能举个例子吗？"  # 基于上一个回答
ai-chat doubao "这个例子的时间复杂度是多少？"  # 继续深入
```

### 2. 独立问题使用 --clear

```bash
# ✅ 好的做法
ai-chat doubao --clear "今天天气怎么样？"
ai-chat doubao --clear "帮我写一个排序算法"  # 完全不相关的问题
```

### 3. 合理设置超时

```bash
# ✅ 好的做法
ai-chat doubao --timeout 30 "简单问题"  # 短超时
ai-chat doubao --timeout 120 "复杂分析任务"  # 长超时
```

### 4. 在应用中查看完整响应

虽然工具会尝试提取响应，但建议在 AI 应用界面中查看完整的、格式化的响应。

## 总结

CDP AI Tools 提供了一个统一、简单的接口来与本地 AI 应用交互，支持：

- ✅ 多个 AI 应用（豆包、阶跃AI）
- ✅ 连续对话
- ✅ 灵活配置
- ✅ Claude Code 集成
- ✅ 自动化工作流

开始使用：
```bash
ai-chat doubao "你好"
ai-chat stepfun "你好"
```
