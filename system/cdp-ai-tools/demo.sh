#!/bin/bash
# CDP AI Tools 功能演示

echo "╔════════════════════════════════════════════════════════════╗"
echo "║         CDP AI Tools - 完整功能演示                        ║"
echo "╚════════════════════════════════════════════════════════════╝"
echo

echo "📋 支持的 AI 应用:"
echo "  • 豆包 (Doubao) - CDP 端口 9225"
echo "  • 阶跃AI (StepFun) - CDP 端口 9224"
echo "  • Ollama - HTTP API 端口 11434"
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "1️⃣  基本消息发送"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo
echo "命令: ai-chat doubao \"你好\""
echo "命令: ai-chat stepfun \"你好\""
echo "命令: ai-chat ollama \"你好\""
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "2️⃣  对话管理（Doubao & StepFun）"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo
echo "📝 列出所有对话:"
ai-chat doubao --list-conversations
echo
echo "命令示例:"
echo "  • ai-chat doubao --switch 0          # 切换到第一个对话"
echo "  • ai-chat doubao --delete 1          # 删除第二个对话"
echo "  • ai-chat doubao --rename 0 \"新名称\" # 重命名对话"
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "3️⃣  快捷操作（Doubao & StepFun）"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo
echo "命令示例:"
echo "  • ai-chat doubao --quick-action \"编程\"     # 点击编程按钮"
echo "  • ai-chat doubao --quick-action \"数据分析\" # 点击数据分析按钮"
echo "  • ai-chat doubao --settings                # 打开设置"
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "4️⃣  Ollama 特有功能"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo
echo "🤖 可用模型:"
ai-chat ollama --list-models | jq -r '.models[] | "  • \(.name) (\(.details.parameter_size))"'
echo
echo "命令示例:"
echo "  • ai-chat ollama --pull llama2                    # 拉取新模型"
echo "  • ai-chat ollama --generate qwen2.5:7b \"问题\"    # 生成响应"
echo "  • ai-chat ollama --stream \"问题\"                 # 流式输出"
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "5️⃣  连续对话示例"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo
echo "# 第一个问题"
echo "ai-chat doubao \"什么是递归？\""
echo
echo "# 第二个问题（在同一对话中）"
echo "ai-chat doubao \"能举个例子吗？\""
echo
echo "# 第三个问题（继续同一对话）"
echo "ai-chat doubao \"递归的时间复杂度如何计算？\""
echo

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "✅ 演示完成！"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo
echo "📚 查看完整文档: cat SKILL.md"
echo "🧪 运行测试: ./test_all.sh"
echo "❓ 获取帮助: ai-chat --help"
echo
