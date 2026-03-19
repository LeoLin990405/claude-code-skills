# CDP AI Tools - 快速开始

## 安装完成 ✅

CDP AI Tools skill 已经安装并可以使用！

## 快速测试

```bash
# 测试豆包
ai-chat doubao "你好"

# 测试阶跃AI
ai-chat stepfun "你好"

# 查看帮助
ai-chat --help
```

## 基本用法

### 1. 单次问答

```bash
# 使用豆包
ai-chat doubao "什么是递归？"

# 使用阶跃AI
ai-chat stepfun "什么是递归？"
```

### 2. 连续对话（默认）

```bash
# 第一个问题
ai-chat doubao "什么是递归？"

# 第二个问题（在同一个对话中）
ai-chat doubao "能举个例子吗？"

# 第三个问题（继续同一个对话）
ai-chat doubao "递归的时间复杂度如何计算？"
```

### 3. 清理对话

```bash
# 清理对话后发送新问题
ai-chat doubao --clear "这是一个新话题"
```

## 在 Claude Code 中使用

当你在 Claude Code 中提到以下关键词时，Claude 会自动使用这个 skill：

- "使用豆包"、"问豆包"、"让豆包"
- "使用阶跃"、"问阶跃"、"让阶跃"
- "本地AI"、"CDP"

### 示例对话

```
你: "用豆包帮我解释一下什么是递归"

Claude 会执行:
ai-chat doubao "请解释什么是递归"
```

## 文件结构

```
~/.claude/skills/cdp-ai-tools/
├── SKILL.md              # Skill 文档
├── README.md             # 本文件
├── ai-chat               # 统一命令行工具
├── lib/
│   └── unified_cdp.py   # 统一 CDP 接口
└── config.json          # 配置文件
```

## 配置

配置文件位于：`~/.claude/skills/cdp-ai-tools/config.json`

```json
{
  "doubao": {
    "port": 9225,
    "app_path": "/Applications/Doubao.app",
    "page_pattern": "doubao://doubao-chat/chat",
    "input_selector": "textarea.semi-input-textarea",
    "app_name": "豆包"
  },
  "stepfun": {
    "port": 9224,
    "app_path": "/Applications/阶跃AI.app",
    "page_pattern": "http://127.0.0.1:63008/chats",
    "input_selector": "[contenteditable=\"true\"]",
    "app_name": "阶跃AI"
  }
}
```

## 故障排除

### 问题：连接失败

```bash
# 检查豆包是否运行
ps aux | grep Doubao

# 启动豆包
/Applications/Doubao.app/Contents/MacOS/Doubao --remote-debugging-port=9225 &

# 检查阶跃AI是否运行
ps aux | grep 阶跃AI

# 启动阶跃AI
open -a "阶跃AI"
```

### 问题：消息未发送

- 确保 AI 应用在前台
- 确保聊天页面已打开
- 尝试手动在应用中发送一条消息

## 更多信息

详细文档请查看：`~/.claude/skills/cdp-ai-tools/SKILL.md`
