---
name: sql2sh
version: 2.0.0
description: |
  SQL 代码转 Doris ETL Shell 脚本的智能转换工具。用于：
  (1) 将 SQL 文件或 Markdown 中的 SQL 代码块转换为可执行的 shell 脚本
  (2) 智能识别日期粒度（日/周/月）并参数化 dt 分区字段
  (3) 自动添加 DELETE 语句实现幂等性
  (4) 智能分组 DDL/DML 语句
  (5) 生成带执行日志和耗时统计的标准化脚本
  触发条件：当用户提到"SQL转脚本"、"生成ETL脚本"、"构建sh脚本"、"把SQL写成脚本"等相关操作时使用。
changelog: CHANGELOG.md
---

# SQL to Shell Script Converter

## 快速开始

### 方式一：使用 Python 脚本（推荐）

```bash
# 基本用法
python3 scripts/sql2sh.py input.sql output.sh "脚本描述"

# 从 Markdown 转换
python3 scripts/sql2sh.py input.md output.sh "台球周报-营收分析"
```

### 方式二：手动转换流程

1. 读取 SQL 源文件
2. 提取所有 SQL 代码块
3. 识别目标表名和日期粒度
4. 按模板生成脚本

## 转换规则

### 日期参数化

| 粒度 | 变量名 | 默认值 | 识别关键词 |
|------|--------|--------|-----------|
| 周 | `WEEK_START` | `$(date -d "last monday" +%Y-%m-%d)` | week, weekly |
| 日 | `YYYY_MM_DD` | `$(date +%Y-%m-%d)` | daily, day |
| 月 | `MONTH_START` | `$(date +%Y-%m-01)` | month, monthly |

### SQL 块分组

1. **环境准备**: `SET`, `DELETE FROM`, `DROP TABLE IF EXISTS tmp_*`
2. **建表**: `CREATE TABLE`
3. **核心处理**: `INSERT INTO`, `SELECT`
4. **清理**: `DROP TABLE IF EXISTS tmp_*`

### 输出格式

```bash
#!/bin/bash
##################################
### 脚本名：<table_name>.sh
### 作用：<description>
##################################
source /opt/common.sh

if [ $# -lt 1 ]; then
    WEEK_START=$(date -d "last monday" +%Y-%m-%d)
else
    WEEK_START=$1
fi
echo "WEEK_START: ${WEEK_START}"

sql1="<SQL语句>"
echo "执行SQL1: 描述"; start_time=$(date +%s); ExecuteDoris "${sql1}"; echo "耗时 $(($(date +%s) - start_time)) 秒"

echo "######## <table_name> 完成 ########"
```

## 资源文件

| 文件 | 用途 |
|------|------|
| `scripts/sql2sh.py` | 核心转换脚本 |
| `references/template.md` | 模板规范文档 |
| `assets/script_template.sh` | 标准脚本模板 |

## 最佳实践

- 每个 SQL 块添加执行日志和耗时统计
- 临时表使用 `tmp_` 前缀，脚本末尾清理
- 大查询分批执行避免内存溢出
- 使用 `COALESCE` 处理 NULL 值
