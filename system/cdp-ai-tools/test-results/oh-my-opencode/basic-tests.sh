#!/bin/bash
# oh-my-opencode 基本功能测试

RESULT_FILE=~/.claude/skills/cdp-ai-tools/test-results/oh-my-opencode/basic-tests.md

echo "# oh-my-opencode 基本功能测试报告" > $RESULT_FILE
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
    
    eval "$cmd" 2>&1 | head -30 >> $RESULT_FILE
    local exit_code=$?
    
    echo '```' >> $RESULT_FILE
    echo "" >> $RESULT_FILE
    
    if [ $exit_code -eq 0 ]; then
        echo "### 测试结果: ✅ 通过 (退出码: $exit_code)" >> $RESULT_FILE
    else
        echo "### 测试结果: ⚠️ 警告 (退出码: $exit_code)" >> $RESULT_FILE
    fi
    
    echo "" >> $RESULT_FILE
    echo "---" >> $RESULT_FILE
    echo "" >> $RESULT_FILE
}

echo "开始测试 oh-my-opencode 基本功能..."

# 测试版本信息
test_command "测试 1: 版本信息" "oh-my-opencode --version"

# 测试帮助信息
test_command "测试 2: 帮助信息" "oh-my-opencode --help"

# 测试 doctor 命令
test_command "测试 3: 健康检查 (doctor)" "oh-my-opencode doctor"

# 测试 get-local-version
test_command "测试 4: 获取本地版本" "oh-my-opencode get-local-version"

# 测试 MCP 命令
test_command "测试 5: MCP 服务器管理" "oh-my-opencode mcp --help"

echo "基本功能测试完成！结果保存在: $RESULT_FILE"
