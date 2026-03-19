---
name: svn
description: |
  SVN (Subversion) 版本控制操作技能。用于执行 SVN 仓库的常见操作，包括：
  (1) 检出仓库 (checkout)
  (2) 更新代码 (update)
  (3) 提交更改 (commit)
  (4) 查看状态和日志 (status, log, info)
  (5) 分支和标签管理 (branch, tag)
  (6) 文件操作 (add, delete, revert, resolve)
  (7) 差异比较 (diff)
  触发条件：当用户提到 svn、subversion、版本控制、检出、提交代码、更新代码、查看日志等相关操作时使用。
triggers:
  - svn
  - subversion
  - 版本控制
  - 提交代码
  - 推送代码
  - svn提交
  - svn更新
---

# SVN 版本控制技能

## 权限规则 (重要!)

**只允许上传操作，禁止以下危险操作：**
- ❌ `svn delete` / `svn rm` - 禁止删除文件
- ❌ `svn revert` - 禁止撤销修改
- ❌ `svn merge` - 禁止合并操作
- ❌ `svn switch` - 禁止切换分支
- ❌ 任何带 `--force` 的命令

**允许的操作：**
- ✅ `svn checkout` - 检出仓库
- ✅ `svn update` - 更新代码
- ✅ `svn add` - 添加新文件
- ✅ `svn commit` - 提交更改
- ✅ `svn status` - 查看状态
- ✅ `svn info` - 查看信息
- ✅ `svn log` - 查看日志
- ✅ `svn diff` - 查看差异

## 已配置仓库

### data_group_sql_job (数据组SQL脚本)
| 配置项 | 值 |
|--------|-----|
| **仓库地址** | `https://svn.coding.net/serverless-100013832940/motern_brain/data_group_sql_job` |
| **账号** | `linzy@motern.com` |
| **密码** | `Wudaohai1940@` |
| **本地路径** | `/Users/leo/Projects/data_group_sql_job` |
| **备用路径** | `/Users/leo/Desktop/data_group_sql_job` (受 macOS 沙盒限制，需 Full Disk Access) |
| **说明** | 数据仓库 ETL 脚本 (ods/dwd/dws/dim/ads 各层) |

## 标准操作流程 (必须严格按顺序执行)

### 提交修改流程

```
Step 1: svn info   → 检查工作副本是否正常
Step 2: svn update → 同步远程最新代码（避免冲突）
Step 3: 读取最新文件内容（update 后可能有远程改动）
Step 4: 修改文件
Step 5: svn diff   → 确认改动内容正确
Step 6: svn commit → 提交（需用户确认后执行）
```

### 详细步骤

**Step 1: 检查工作副本**
```bash
svn info /Users/leo/Projects/data_group_sql_job
```
- 如果报 `not a working copy`，需要先 checkout
- 如果报 `Operation not permitted`，说明 macOS 权限问题，需切换到 Projects 目录

**Step 2: 同步最新代码**
```bash
svn update /Users/leo/Projects/data_group_sql_job --username linzy@motern.com --password 'Wudaohai1940@' --non-interactive
```
- 必须在修改前先 update，避免覆盖他人提交

**Step 3: 读取最新文件**
- update 后用 Read 工具读取要修改的文件
- 确认文件内容是最新版本再修改

**Step 4: 修改文件**
- 使用 Edit 工具精确修改

**Step 5: 确认差异**
```bash
svn diff /Users/leo/Projects/data_group_sql_job/<文件名>
```
- 展示给用户确认改动无误

**Step 6: 提交**
```bash
svn commit -m "提交说明" /Users/leo/Projects/data_group_sql_job/<文件名> --username linzy@motern.com --password 'Wudaohai1940@' --non-interactive
```

### 新增文件流程

```bash
# 1. update
svn update /Users/leo/Projects/data_group_sql_job --username linzy@motern.com --password 'Wudaohai1940@' --non-interactive

# 2. 创建文件（Write 工具）

# 3. 添加到版本控制
svn add /Users/leo/Projects/data_group_sql_job/<新文件名>

# 4. 检查状态
svn status /Users/leo/Projects/data_group_sql_job

# 5. 提交
svn commit -m "提交说明" /Users/leo/Projects/data_group_sql_job/<新文件名> --username linzy@motern.com --password 'Wudaohai1940@' --non-interactive
```

## 查询命令

```bash
# 查看仓库状态
svn status /Users/leo/Projects/data_group_sql_job

# 查看最近提交日志
svn log -l 10 /Users/leo/Projects/data_group_sql_job

# 查看某个文件的日志
svn log -l 5 /Users/leo/Projects/data_group_sql_job/<文件名>

# 搜索包含某个表名的文件
grep -rl "表名" /Users/leo/Projects/data_group_sql_job/
```

## 常见问题

### macOS 权限问题
Desktop 目录受 macOS 沙盒保护，Claude Code 可能无法访问。解决方案：
1. 系统设置 → Privacy & Security → Full Disk Access → 添加终端应用
2. 或将仓库复制到不受限目录：`cp -R ~/Desktop/data_group_sql_job ~/Projects/data_group_sql_job`

### 工作副本损坏
如果 `svn info` 报错 `not a working copy`，重新 checkout：
```bash
svn checkout https://svn.coding.net/serverless-100013832940/motern_brain/data_group_sql_job /Users/leo/Projects/data_group_sql_job --username linzy@motern.com --password 'Wudaohai1940@' --non-interactive
```
