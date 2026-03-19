#!/bin/bash
# CDP AI Tools 完整测试脚本

RESULT_FILE=~/.claude/skills/cdp-ai-tools/test-results/cdp-tools.md

echo "# CDP AI Tools 完整测试报告" > $RESULT_FILE
echo "" >> $RESULT_FILE
echo "测试时间: $(date)" >> $RESULT_FILE
echo "" >> $RESULT_FILE

# 测试函数
test_command() {
    local name=$1
    local cmd=$2
    
    echo "## $name" >> $RESULT_FILE
    echo "" >> $RESULT_FILE
    echo '```bash' >> $RESULT_FILE
    echo "$cmd" >> $RESULT_FILE
    echo '```' >> $RESULT_FILE
    echo "" >> $RESULT_FILE
    echo "### 输出:" >> $RESULT_FILE
    echo '```' >> $RESULT_FILE
    
    timeout 10 eval "$cmd" 2>&1 | head -20 >> $RESULT_FILE
    local exit_code=$?
    
    echo '```' >> $RESULT_FILE
    echo "" >> $RESULT_FILE
    
    if [ $exit_code -eq 0 ]; then
        echo "### 测试结果: ✅ 通过" >> $RESULT_FILE
    else
        echo "### 测试结果: ❌ 失败 (退出码: $exit_code)" >> $RESULT_FILE
    fi
    
    echo "" >> $RESULT_FILE
    echo "---" >> $RESULT_FILE
    echo "" >> $RESULT_FILE
}

echo "开始测试 CDP AI Tools..."

# 测试 ai-chat 帮助
test_command "ai-chat 帮助信息" "ai-chat --help"

# 测试豆包
test_command "豆包 - 列出对话" "ai-chat doubao --list-conversations"

# 测试阶跃AI
test_command "阶跃AI - 列出对话" "ai-chat stepfun --list-conversations"

# 测试 Ollama
test_command "Ollama - 列出模型" "ai-chat ollama --list-models"

# 测试独立控制器
cd ~/.claude/skills/cdp-ai-tools
test_command "豆包控制器 - 列出对话" "python3 doubao_full_controller.py --list-conversations"
test_command "阶跃AI控制器 - 列出对话" "python3 stepfun_full_controller.py --list-conversations"
test_command "Ollama控制器 - 列出模型" "python3 ollama_controller.py --list-models"

echo "测试完成！结果保存在: $RESULT_FILE"
