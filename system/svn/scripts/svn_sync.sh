#!/bin/bash
##################################
### SVN 同步脚本 (更新+提交)
### 用法: svn_sync.sh "提交说明" [PATH]
##################################

if [ $# -lt 1 ]; then
    echo "用法: svn_sync.sh \"提交说明\" [PATH]"
    exit 1
fi

MESSAGE="$1"
PATH_ARG="${2:-.}"

echo "========================================"
echo "SVN 同步: ${PATH_ARG}"
echo "========================================"

# 检查是否是 SVN 工作副本
if ! svn info "${PATH_ARG}" > /dev/null 2>&1; then
    echo "错误: ${PATH_ARG} 不是 SVN 工作副本"
    exit 1
fi

# Step 1: 更新
echo "[Step 1] 更新到最新版本..."
svn update "${PATH_ARG}"
if [ $? -ne 0 ]; then
    echo "更新失败，请检查冲突"
    exit 1
fi

# Step 2: 检查状态
echo ""
echo "[Step 2] 检查本地修改..."
STATUS=$(svn status "${PATH_ARG}")
if [ -z "${STATUS}" ]; then
    echo "无本地修改，无需提交"
    exit 0
fi
echo "${STATUS}"

# Step 3: 自动添加新文件
echo ""
echo "[Step 3] 添加新文件..."
svn status "${PATH_ARG}" | grep "^?" | awk '{print $2}' | while read f; do
    echo "添加: $f"
    svn add "$f"
done

# Step 4: 提交
echo ""
echo "[Step 4] 提交更改..."
echo "提交说明: ${MESSAGE}"
svn commit -m "${MESSAGE}" "${PATH_ARG}"

if [ $? -eq 0 ]; then
    echo ""
    echo "同步完成!"
    svn info "${PATH_ARG}" | grep "Revision"
else
    echo ""
    echo "提交失败!"
    exit 1
fi
