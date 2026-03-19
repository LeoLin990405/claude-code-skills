#!/bin/bash
# 测试所有功能

echo "=== CDP AI Tools 功能测试 ==="
echo

echo "1. 测试 ai-chat 帮助信息"
ai-chat --help
echo

echo "2. 测试豆包对话管理"
echo "   - 列出对话"
ai-chat doubao --list-conversations
echo

echo "3. 测试阶跃AI对话管理"
echo "   - 列出对话"
ai-chat stepfun --list-conversations
echo

echo "4. 测试 Ollama 模型列表"
ai-chat ollama --list-models
echo

echo "5. 测试独立控制器"
echo "   - doubao_full_controller.py"
python3 doubao_full_controller.py --list-conversations
echo

echo "   - stepfun_full_controller.py"
python3 stepfun_full_controller.py --list-conversations
echo

echo "   - ollama_controller.py"
python3 ollama_controller.py --list-models
echo

echo "=== 所有测试完成 ==="
