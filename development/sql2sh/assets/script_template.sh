#!/bin/bash
##################################
### 脚本名：{{TABLE_NAME}}.sh
### 作用：{{DESCRIPTION}}
##################################
source /opt/common.sh

if [ $# -lt 1 ]; then
    {{DATE_VAR}}={{DATE_DEFAULT}}
else
    {{DATE_VAR}}=$1
fi
echo "{{DATE_VAR}}: ${{{DATE_VAR}}}"

sql1="
{{SQL_BLOCK_1}}
"
echo "执行SQL1: {{SQL_DESC_1}}"; start_time=$(date +%s); ExecuteDoris "${sql1}"; echo "耗时 $(($(date +%s) - start_time)) 秒"

echo "######## {{TABLE_NAME}} 完成 ########"
