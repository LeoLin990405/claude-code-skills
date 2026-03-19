#!/bin/bash
# CCB Provider 完整测试脚本

RESULT_FILE=~/.claude/skills/cdp-ai-tools/test-results/ccb-providers.md

echo "# CCB Provider 完整测试报告" > $RESULT_FILE
echo "" >> $RESULT_FILE
echo "测试时间: $(date)" >> $RESULT_FILE
echo "" >> $RESULT_FILE

# 测试函数
test_provider() {
    local provider=$1
    local model=$2
    local prompt="1+1等于几？请简短回答"
    
    echo "## 测试 $provider" >> $RESULT_FILE
    echo "" >> $RESULT_FILE
    echo "### 基本调用测试" >> $RESULT_FILE
    echo '```' >> $RESULT_FILE
    
    if [ -n "$model" ]; then
        echo "命令: ccb-cli $provider $model \"$prompt\"" >> $RESULT_FILE
        timeout 30 ccb-cli $provider $model "$prompt" 2>&1 | head -10 >> $RESULT_FILE
    else
        echo "命令: ccb-cli $provider \"$prompt\"" >> $RESULT_FILE
        timeout 30 ccb-cli $provider "$prompt" 2>&1 | head -10 >> $RESULT_FILE
    fi
    
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

# 测试所有 Provider
echo "开始测试 CCB Provider..."

test_provider "kimi" ""
test_provider "qwen" ""
test_provider "iflow" ""
test_provider "opencode" "mm"
test_provider "codex" "o4-mini"
test_provider "gemini" "3f"
test_provider "qoder" ""

echo "测试完成！结果保存在: $RESULT_FILE"
