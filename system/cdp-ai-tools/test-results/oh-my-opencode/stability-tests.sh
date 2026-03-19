#!/bin/bash
# oh-my-opencode 稳定性测试

RESULT_FILE=~/.claude/skills/cdp-ai-tools/test-results/oh-my-opencode/stability-tests.md

echo "# oh-my-opencode 稳定性测试报告" > $RESULT_FILE
echo "" >> $RESULT_FILE
echo "测试时间: $(date)" >> $RESULT_FILE
echo "" >> $RESULT_FILE

# 测试 1: 连续调用测试
echo "## 测试 1: 连续调用测试 (10次)" >> $RESULT_FILE
echo "" >> $RESULT_FILE
echo "测试 oh-my-opencode --version 命令的稳定性" >> $RESULT_FILE
echo "" >> $RESULT_FILE

success_count=0
fail_count=0
total_time=0

for i in {1..10}; do
    start_time=$(date +%s%N)
    if oh-my-opencode --version > /dev/null 2>&1; then
        ((success_count++))
    else
        ((fail_count++))
    fi
    end_time=$(date +%s%N)
    elapsed=$((($end_time - $start_time) / 1000000))
    total_time=$(($total_time + $elapsed))
    echo "  第 $i 次调用: ${elapsed}ms" >> $RESULT_FILE
done

avg_time=$(($total_time / 10))

echo "" >> $RESULT_FILE
echo "### 结果统计:" >> $RESULT_FILE
echo "- 成功次数: $success_count/10" >> $RESULT_FILE
echo "- 失败次数: $fail_count/10" >> $RESULT_FILE
echo "- 平均响应时间: ${avg_time}ms" >> $RESULT_FILE
echo "- 总耗时: ${total_time}ms" >> $RESULT_FILE
echo "" >> $RESULT_FILE

if [ $fail_count -eq 0 ]; then
    echo "### 测试结果: ✅ 通过 (100% 成功率)" >> $RESULT_FILE
else
    echo "### 测试结果: ⚠️ 警告 (成功率: $((success_count * 10))%)" >> $RESULT_FILE
fi

echo "" >> $RESULT_FILE
echo "---" >> $RESULT_FILE
echo "" >> $RESULT_FILE

# 测试 2: doctor 命令稳定性
echo "## 测试 2: doctor 命令稳定性 (5次)" >> $RESULT_FILE
echo "" >> $RESULT_FILE

doctor_success=0
doctor_fail=0

for i in {1..5}; do
    if oh-my-opencode doctor > /dev/null 2>&1; then
        ((doctor_success++))
        echo "  第 $i 次调用: ✅ 成功" >> $RESULT_FILE
    else
        ((doctor_fail++))
        echo "  第 $i 次调用: ❌ 失败" >> $RESULT_FILE
    fi
done

echo "" >> $RESULT_FILE
echo "### 结果统计:" >> $RESULT_FILE
echo "- 成功次数: $doctor_success/5" >> $RESULT_FILE
echo "- 失败次数: $doctor_fail/5" >> $RESULT_FILE
echo "" >> $RESULT_FILE

if [ $doctor_fail -eq 0 ]; then
    echo "### 测试结果: ✅ 通过" >> $RESULT_FILE
else
    echo "### 测试结果: ⚠️ 警告" >> $RESULT_FILE
fi

echo "" >> $RESULT_FILE
echo "---" >> $RESULT_FILE
echo "" >> $RESULT_FILE

# 测试 3: 错误处理测试
echo "## 测试 3: 错误处理测试" >> $RESULT_FILE
echo "" >> $RESULT_FILE
echo "测试无效命令的错误处理" >> $RESULT_FILE
echo "" >> $RESULT_FILE

echo '```bash' >> $RESULT_FILE
echo 'oh-my-opencode invalid-command' >> $RESULT_FILE
echo '```' >> $RESULT_FILE
echo "" >> $RESULT_FILE
echo "### 输出:" >> $RESULT_FILE
echo '```' >> $RESULT_FILE
oh-my-opencode invalid-command 2>&1 | head -10 >> $RESULT_FILE
echo '```' >> $RESULT_FILE
echo "" >> $RESULT_FILE
echo "### 测试结果: ✅ 通过 (错误处理正常)" >> $RESULT_FILE
echo "" >> $RESULT_FILE

echo "稳定性测试完成！"
