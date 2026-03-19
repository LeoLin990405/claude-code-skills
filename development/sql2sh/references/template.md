# SQL 转脚本模板规范

## 脚本结构

```
#!/bin/bash
##################################
### 脚本名：<table_name>.sh
### 作用：<description>
##################################
source /opt/common.sh

# 日期参数处理
if [ $# -lt 1 ]; then
    <DATE_VAR>=<default_expr>
else
    <DATE_VAR>=$1
fi

# SQL 执行块 (可多个)
sql1="<SQL语句>"
ExecuteDoris "${sql1}"

echo "######## <table_name> 完成 ########"
```

## 日期变量规范

| 粒度 | 变量名 | 默认值 | 触发关键词 |
|------|--------|--------|-----------|
| 周 | `WEEK_START` | `$(date -d "last monday" +%Y-%m-%d)` | week, weekly, weekday |
| 日 | `YYYY_MM_DD` | `$(date +%Y-%m-%d)` | daily, day |
| 月 | `MONTH_START` | `$(date +%Y-%m-01)` | month, monthly |

## SQL 块分组原则

1. **环境准备块**: SET 语句、DELETE 清理、DROP 临时表
2. **DDL 块**: CREATE TABLE (临时表)
3. **核心处理块**: INSERT INTO, SELECT
4. **清理块**: DROP 临时表

## 转义规则

Shell 变量中的 SQL 需要转义：
- `\` → `\\`
- `"` → `\"`
- 保留 `${VAR}` 变量引用

## 最佳实践

1. 每个 SQL 块添加执行日志和耗时统计
2. 临时表使用 `tmp_` 前缀
3. 脚本末尾清理所有临时表
4. 使用 `COALESCE` 处理 NULL 值
5. 大查询分批执行避免内存溢出
