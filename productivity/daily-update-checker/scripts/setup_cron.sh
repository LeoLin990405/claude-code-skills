#!/bin/bash

# Setup Daily Update Checker Cron Job
# 设置每日自动检查更新的定时任务

set -e

# 颜色定义
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

SCRIPT_PATH="$HOME/.claude/skills/daily-update-checker/scripts/check_updates.sh"
LOG_PATH="$HOME/.claude/skills/daily-update-checker/update.log"

# 检查脚本是否存在
if [ ! -f "$SCRIPT_PATH" ]; then
    echo -e "${RED}❌ 错误: 检查脚本不存在: $SCRIPT_PATH${NC}"
    exit 1
fi

# 确保脚本可执行
chmod +x "$SCRIPT_PATH"

echo -e "${BLUE}🔧 设置每日更新检查定时任务...${NC}"
echo ""

# 检查是否已存在定时任务
existing_cron=$(crontab -l 2>/dev/null | grep -c "check_updates.sh" || echo "0")

if [ "$existing_cron" -gt 0 ]; then
    echo -e "${YELLOW}⚠️  已存在更新检查定时任务${NC}"
    echo ""
    echo "当前定时任务:"
    crontab -l | grep "check_updates.sh"
    echo ""
    read -p "是否重新设置? (y/n): " confirm
    if [ "$confirm" != "y" ]; then
        echo -e "${YELLOW}已取消${NC}"
        exit 0
    fi
    # 删除旧的定时任务
    crontab -l 2>/dev/null | grep -v "check_updates.sh" | crontab -
fi

# 选择检查时间
echo "请选择每日检查时间:"
echo "1) 早上 9:00 (推荐)"
echo "2) 中午 12:00"
echo "3) 下午 6:00"
echo "4) 晚上 10:00"
echo "5) 自定义"
echo ""
read -p "请选择 (1-5): " time_choice

case $time_choice in
    1)
        HOUR=9
        MINUTE=0
        ;;
    2)
        HOUR=12
        MINUTE=0
        ;;
    3)
        HOUR=18
        MINUTE=0
        ;;
    4)
        HOUR=22
        MINUTE=0
        ;;
    5)
        read -p "输入小时 (0-23): " HOUR
        read -p "输入分钟 (0-59): " MINUTE
        ;;
    *)
        echo -e "${YELLOW}无效选择，使用默认时间 9:00${NC}"
        HOUR=9
        MINUTE=0
        ;;
esac

# 验证时间
if ! [[ "$HOUR" =~ ^[0-9]+$ ]] || [ "$HOUR" -lt 0 ] || [ "$HOUR" -gt 23 ]; then
    echo -e "${RED}❌ 无效的小时，使用默认值 9${NC}"
    HOUR=9
fi

if ! [[ "$MINUTE" =~ ^[0-9]+$ ]] || [ "$MINUTE" -lt 0 ] || [ "$MINUTE" -gt 59 ]; then
    echo -e "${RED}❌ 无效的分钟，使用默认值 0${NC}"
    MINUTE=0
fi

# 创建日志目录
mkdir -p "$(dirname "$LOG_PATH")"

# 创建新的定时任务
cron_job="$MINUTE $HOUR * * * $SCRIPT_PATH >> $LOG_PATH 2>&1"

# 添加到 crontab
(crontab -l 2>/dev/null || echo "") | {
    cat
    echo "# Daily Update Checker - CLI工具更新检查"
    echo "$cron_job"
} | crontab -

echo ""
echo -e "${GREEN}✅ 定时任务设置成功！${NC}"
echo ""
echo "📅 检查时间: 每天 $(printf "%02d:%02d" $HOUR $MINUTE)"
echo "📝 日志文件: $LOG_PATH"
echo "🔍 检查脚本: $SCRIPT_PATH"
echo ""

# 显示当前所有定时任务
echo -e "${BLUE}📋 当前所有定时任务:${NC}"
echo "----------------------------------------"
crontab -l | grep -v "^#" | grep -v "^$" || echo "无其他定时任务"
echo "----------------------------------------"
echo ""

# 询问是否立即运行一次
read -p "是否立即运行一次检查? (y/n): " run_now
if [ "$run_now" = "y" ]; then
    echo ""
    echo -e "${BLUE}🚀 立即运行检查...${NC}"
    echo ""
    "$SCRIPT_PATH"
fi

echo ""
echo -e "${GREEN}🎉 设置完成！${NC}"
echo ""
echo "💡 提示:"
echo "   • 使用 'crontab -l' 查看所有定时任务"
echo "   • 使用 'crontab -e' 编辑定时任务"
echo "   • 使用 'tail -f $LOG_PATH' 查看更新日志"
echo "   • 报告文件保存在: $HOME/.claude/skills/daily-update-checker/reports/"
