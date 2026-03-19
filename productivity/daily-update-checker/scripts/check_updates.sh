#!/bin/bash

# Daily Update Checker Script
# 检查本地 CLI 工具更新

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 报告文件
REPORT_DIR="$HOME/.claude/skills/daily-update-checker/reports"
REPORT_FILE="$REPORT_DIR/update_report_$(date +%Y%m%d_%H%M%S).md"

# 创建报告目录
mkdir -p "$REPORT_DIR"

# 初始化报告
cat > "$REPORT_FILE" << EOF
# CLI 工具更新报告

**检查时间:** $(date '+%Y-%m-%d %H:%M:%S')  
**系统:** macOS $(sw_vers -productVersion 2>/dev/null || echo "Unknown")

---

EOF

echo -e "${BLUE}🔍 开始检查本地 CLI 工具更新...${NC}"
echo ""

# ============================================
# 检查 Homebrew 更新
# ============================================
check_homebrew() {
    echo -e "${BLUE}📦 检查 Homebrew 更新...${NC}"
    
    if ! command -v brew &> /dev/null; then
        echo -e "${YELLOW}⚠️  Homebrew 未安装${NC}"
        return
    fi
    
    # 更新 Homebrew 数据库
    brew update > /dev/null 2>&1
    
    # 获取可更新的包
    outdated=$(brew outdated --json 2>/dev/null || echo "[]")
    
    # 检查 AI Agent CLI 工具
    ai_tools=("claude" "claude-code" "codex" "gemini-cli")
    
    echo "## Homebrew 包更新" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    local has_updates=false
    
    for tool in "${ai_tools[@]}"; do
        if brew list "$tool" &> /dev/null; then
            current_version=$(brew list --versions "$tool" 2>/dev/null | awk '{print $2}')
            
            # 检查是否有更新
            if echo "$outdated" | grep -q "\"$tool\""; then
                latest_version=$(brew info "$tool" --json 2>/dev/null | grep -o '"versions":{[^}]*}' | grep -o '"stable":"[^"]*"' | cut -d'"' -f4)
                echo -e "${YELLOW}⬆️  $tool: $current_version → $latest_version${NC}"
                echo "- **$tool**: $current_version → $latest_version ⚠️" >> "$REPORT_FILE"
                has_updates=true
            else
                echo -e "${GREEN}✅ $tool: $current_version (最新)${NC}"
                echo "- **$tool**: $current_version ✅" >> "$REPORT_FILE"
            fi
        fi
    done
    
    if [ "$has_updates" = false ]; then
        echo "所有 Homebrew 包都是最新版本。" >> "$REPORT_FILE"
    else
        echo "" >> "$REPORT_FILE"
        echo "**更新命令:**" >> "$REPORT_FILE"
        echo "\`\`\`bash" >> "$REPORT_FILE"
        echo "brew upgrade claude claude-code codex gemini-cli" >> "$REPORT_FILE"
        echo "\`\`\`" >> "$REPORT_FILE"
    fi
    
    echo "" >> "$REPORT_FILE"
    echo "---" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
}

# ============================================
# 检查 npm 全局包更新
# ============================================
check_npm() {
    echo -e "${BLUE}📦 检查 npm 全局包更新...${NC}"
    
    if ! command -v npm &> /dev/null; then
        echo -e "${YELLOW}⚠️  npm 未安装${NC}"
        return
    fi
    
    echo "## npm 全局包更新" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    # 获取过时的包
    outdated=$(npm outdated -g --json 2>/dev/null || echo "{}")
    
    if [ "$outdated" = "{}" ] || [ -z "$outdated" ]; then
        echo -e "${GREEN}✅ 所有 npm 全局包都是最新版本${NC}"
        echo "所有 npm 全局包都是最新版本。" >> "$REPORT_FILE"
    else
        echo "$outdated" | grep -v "^{}$" | while read -r line; do
            if [ -n "$line" ]; then
                echo -e "${YELLOW}⬆️  发现可更新的包${NC}"
            fi
        done
        echo "发现可更新的 npm 包，请运行 \`npm outdated -g\` 查看详情。" >> "$REPORT_FILE"
    fi
    
    echo "" >> "$REPORT_FILE"
    echo "---" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
}

# ============================================
# 检查其他 CLI 工具版本
# ============================================
check_other_clis() {
    echo -e "${BLUE}🔧 检查其他 CLI 工具...${NC}"
    
    echo "## 其他 CLI 工具版本" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    declare -A cli_tools
    cli_tools=(
        ["kimi"]="kimi --version"
        ["qwen"]="qwen --version 2>/dev/null || echo 'N/A'"
        ["deepseek"]="deepseek --version 2>/dev/null || echo 'N/A'"
        ["trae"]="trae --version 2>/dev/null || echo 'N/A'"
        ["opencode"]="opencode --version 2>/dev/null || echo 'N/A'"
        ["iflow"]="iflow --version 2>/dev/null || echo 'N/A'"
    )
    
    for tool in "${!cli_tools[@]}"; do
        if command -v "$tool" &> /dev/null; then
            version=$(eval "${cli_tools[$tool]}" 2>/dev/null | head -1 || echo "版本信息不可用")
            echo -e "${GREEN}✅ $tool: $version${NC}"
            echo "- **$tool**: $version" >> "$REPORT_FILE"
        else
            echo -e "${YELLOW}⚠️  $tool: 未安装${NC}"
        fi
    done
    
    echo "" >> "$REPORT_FILE"
    echo "---" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
}

# ============================================
# 检查系统工具更新
# ============================================
check_system_tools() {
    echo -e "${BLUE}🖥️  检查系统工具...${NC}"
    
    echo "## 系统工具版本" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    # 检查常用工具
    tools=("git" "python3" "node" "docker")
    
    for tool in "${tools[@]}"; do
        if command -v "$tool" &> /dev/null; then
            case "$tool" in
                git)
                    version=$(git --version | awk '{print $3}')
                    ;;
                python3)
                    version=$(python3 --version | awk '{print $2}')
                    ;;
                node)
                    version=$(node --version | sed 's/v//')
                    ;;
                docker)
                    version=$(docker --version | awk '{print $3}' | sed 's/,//')
                    ;;
            esac
            echo -e "${GREEN}✅ $tool: $version${NC}"
            echo "- **$tool**: $version" >> "$REPORT_FILE"
        else
            echo -e "${YELLOW}⚠️  $tool: 未安装${NC}"
        fi
    done
    
    echo "" >> "$REPORT_FILE"
    echo "---" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
}

# ============================================
# 生成更新建议
# ============================================
generate_recommendations() {
    echo -e "${BLUE}💡 生成更新建议...${NC}"
    
    echo "## 更新建议" >> "$REPORT_FILE"
    echo "" >> "$REPORT_FILE"
    
    cat >> "$REPORT_FILE" << EOF
### 快速更新命令

\`\`\`bash
# 更新所有 Homebrew 包
brew upgrade

# 更新所有 npm 全局包
npm update -g

# 清理 Homebrew 缓存
brew cleanup
\`\`\`

### 推荐的更新顺序

1. **Homebrew 包** - 通常包含重要的安全更新
2. **npm 全局包** - 开发工具更新
3. **系统工具** - 根据需要手动更新

### 注意事项

- 更新前建议备份重要配置
- 生产环境建议先测试再更新
- 某些更新可能需要重新启动终端或系统
EOF
    
    echo "" >> "$REPORT_FILE"
}

# ============================================
# 主函数
# ============================================
main() {
    echo -e "${GREEN}╔════════════════════════════════════════════════════════╗${NC}"
    echo -e "${GREEN}║         Daily Update Checker - CLI 工具更新检查        ║${NC}"
    echo -e "${GREEN}╚════════════════════════════════════════════════════════╝${NC}"
    echo ""
    
    check_homebrew
    echo ""
    
    check_npm
    echo ""
    
    check_other_clis
    echo ""
    
    check_system_tools
    echo ""
    
    generate_recommendations
    
    # 添加报告尾部
    cat >> "$REPORT_FILE" << EOF

---

*报告生成时间: $(date '+%Y-%m-%d %H:%M:%S')*  
*下次检查建议: $(date -v+1d '+%Y-%m-%d') 09:00*
EOF
    
    echo -e "${GREEN}✅ 检查完成！${NC}"
    echo -e "${BLUE}📄 报告已保存至: $REPORT_FILE${NC}"
    echo ""
    
    # 显示报告摘要
    echo -e "${GREEN}📋 报告摘要:${NC}"
    echo "----------------------------------------"
    grep -E "^(## |\*\*.*\*\*:|✅|⬆️|⚠️)" "$REPORT_FILE" 2>/dev/null | head -20 || cat "$REPORT_FILE" | head -30
}

# 运行主函数
main "$@"
