#!/bin/bash
##################################
### SVN 批量提交脚本
### 用法: svn_commit.sh "提交说明" [PATH]
##################################

if [ $# -lt 1 ]; then
    echo "用法: svn_commit.sh \"提交说明\" [PATH]"
    exit 1
fi

MESSAGE="$1"
PATH_ARG="${2:-.}"

echo "========================================"
echo "SVN 提交准备"
echo "========================================"

# 检查是否是 SVN 工作副本
if ! svn info "${PATH_ARG}" > /dev/null 2>&1; then
    echo "错误: ${PATH_ARG} 不是 SVN 工作副本"
    exit 1
fi

# 显示当前状态
echo "[当前状态]"
svn status "${PATH_ARG}"

echo ""
echo "[待提交说明]"
echo "${MESSAGE}"

echo ""
read -p "确认提交? (y/n): " CONFIRM
if [ "${CONFIRM}" != "y" ]; then
    echo "已取消"
    exit 0
fi

# 执行提交
echo ""
echo "[执行提交]"
svn commit -m "${MESSAGE}" "${PATH_ARG}"

if [ $? -eq 0 ]; then
    echo ""
    echo "提交成功!"
    svn info "${PATH_ARG}" | grep "Revision"
else
    echo ""
    echo "提交失败!"
    exit 1
fi
