#!/bin/bash
##################################
### SVN 快速状态检查脚本
### 用法: svn_status.sh [PATH]
##################################

PATH_ARG="${1:-.}"

echo "========================================"
echo "SVN 状态检查: ${PATH_ARG}"
echo "========================================"

# 检查是否是 SVN 工作副本
if ! svn info "${PATH_ARG}" > /dev/null 2>&1; then
    echo "错误: ${PATH_ARG} 不是 SVN 工作副本"
    exit 1
fi

echo ""
echo "[仓库信息]"
svn info "${PATH_ARG}" 2>/dev/null | grep -E "^(URL|Repository Root|Revision|Last Changed)"

echo ""
echo "[工作副本状态]"
STATUS=$(svn status "${PATH_ARG}" 2>/dev/null)
if [ -z "${STATUS}" ]; then
    echo "无修改"
else
    echo "${STATUS}"
    echo ""
    echo "[统计]"
    echo "修改: $(echo "${STATUS}" | grep -c "^M" || echo 0)"
    echo "新增: $(echo "${STATUS}" | grep -c "^A" || echo 0)"
    echo "删除: $(echo "${STATUS}" | grep -c "^D" || echo 0)"
    echo "冲突: $(echo "${STATUS}" | grep -c "^C" || echo 0)"
    echo "未跟踪: $(echo "${STATUS}" | grep -c "^?" || echo 0)"
fi

echo ""
echo "[最近提交]"
svn log -l 3 "${PATH_ARG}" 2>/dev/null | head -20
