#!/bin/bash
# CDP AI Tools - 安装验证脚本

echo "╔══════════════════════════════════════════════════════════╗"
echo "║          CDP AI Tools - 安装验证                          ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""

# 检查 skill 目录
echo "1. 检查 skill 目录..."
if [ -d ~/.claude/skills/cdp-ai-tools ]; then
    echo "   ✅ Skill 目录存在"
else
    echo "   ✗ Skill 目录不存在"
    exit 1
fi

# 检查文件
echo ""
echo "2. 检查必要文件..."
files=(
    "SKILL.md"
    "README.md"
    "ai-chat"
    "lib/unified_cdp.py"
    "config.json"
)

for file in "${files[@]}"; do
    if [ -f ~/.claude/skills/cdp-ai-tools/$file ]; then
        echo "   ✅ $file"
    else
        echo "   ✗ $file 缺失"
    fi
done

# 检查命令
echo ""
echo "3. 检查命令..."
if command -v ai-chat &> /dev/null; then
    echo "   ✅ ai-chat 命令可用"
else
    echo "   ✗ ai-chat 命令不可用"
fi

# 检查 AI 应用
echo ""
echo "4. 检查 AI 应用..."

# 检查豆包
if ps aux | grep -i doubao | grep -v grep > /dev/null; then
    echo "   ✅ 豆包正在运行"
    if lsof -i :9225 | grep LISTEN > /dev/null 2>&1; then
        echo "      ✅ 端口 9225 已监听"
    else
        echo "      ⚠️  端口 9225 未监听"
    fi
else
    echo "   ⚠️  豆包未运行"
fi

# 检查阶跃AI
if ps aux | grep -i 阶跃AI | grep -v grep > /dev/null; then
    echo "   ✅ 阶跃AI正在运行"
    if lsof -i :9224 | grep LISTEN > /dev/null 2>&1; then
        echo "      ✅ 端口 9224 已监听"
    else
        echo "      ⚠️  端口 9224 未监听"
    fi
else
    echo "   ⚠️  阶跃AI未运行"
fi

# 测试命令
echo ""
echo "5. 测试命令..."
if ai-chat --help > /dev/null 2>&1; then
    echo "   ✅ ai-chat --help 正常"
else
    echo "   ✗ ai-chat --help 失败"
fi

echo ""
echo "╔══════════════════════════════════════════════════════════╗"
echo "║  验证完成                                                ║"
echo "╚══════════════════════════════════════════════════════════╝"
echo ""
echo "📝 使用方法："
echo "   ai-chat doubao \"你好\""
echo "   ai-chat stepfun \"你好\""
echo ""
echo "📚 详细文档："
echo "   ~/.claude/skills/cdp-ai-tools/SKILL.md"
echo "   ~/.claude/skills/cdp-ai-tools/README.md"
