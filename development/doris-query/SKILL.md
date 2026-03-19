---
name: doris-query
description: Safe read-only query tool for Doris data warehouse (111.231.70.22:9030). Only SELECT/SHOW/DESCRIBE/EXPLAIN allowed. 60s timeout. No DDL/DML.
triggers:
  - doris
  - 查询数据库
  - 查数据
  - sql查询
  - 数仓查询
  - query database
---

# Doris Query Skill (Read-Only)

安全的 Doris 数仓只读查询工具。

## 连接信息

| 别名 | Host | Port | User | 快捷名 |
|------|------|------|------|--------|
| **db1** (默认) | 111.231.70.22 | 9030 | linzhongyue | `db1`, `111` |
| **db2** | 1.117.17.157 | 9030 | linzhongyue | `db2`, `117` |

## 安全规则（强制）

1. **只允许只读操作**：SELECT, SHOW, DESCRIBE, EXPLAIN
2. **禁止所有写操作**：INSERT, UPDATE, DELETE, REPLACE, MERGE, LOAD, IMPORT
3. **禁止所有 DDL**：CREATE, DROP, ALTER, TRUNCATE, RENAME
4. **禁止管理操作**：GRANT, REVOKE, SET (除 set session), KILL, ADMIN
5. **单次查询超时 60 秒**
6. **查询结果默认限制 100 行**，用户可指定但不超过 10000 行

## 使用方式

所有查询通过 `~/.claude/skills/doris-query/query.py` 执行：

```bash
# 查询 db1（默认）
python3 ~/.claude/skills/doris-query/query.py "SHOW DATABASES"

# 查询 db2
python3 ~/.claude/skills/doris-query/query.py -d db2 "SHOW DATABASES"
python3 ~/.claude/skills/doris-query/query.py -d 117 "SHOW TABLES FROM ads"

# 指定输出格式
python3 ~/.claude/skills/doris-query/query.py --format table "SHOW TABLES FROM ads"
python3 ~/.claude/skills/doris-query/query.py --format csv -d db2 "SELECT * FROM dim.some_table LIMIT 5"
python3 ~/.claude/skills/doris-query/query.py --format json "DESCRIBE dwd.some_table"
```

## 常用查询模板

```sql
-- 查看所有库
SHOW DATABASES

-- 查看某库所有表
SHOW TABLES FROM ads

-- 查看表结构
DESCRIBE ads.table_name

-- 查看建表语句
SHOW CREATE TABLE ads.table_name

-- 查询数据（必须带 LIMIT）
SELECT * FROM ads.table_name LIMIT 100

-- 查看表行数
SELECT COUNT(*) FROM ads.table_name
```

## 注意事项

- 大表查询务必带 LIMIT，避免超时
- 如果查询超过 60 秒会自动终止
- 结果超过 10000 行会被截断
- 密码存储在 query.py 中，不要外泄
