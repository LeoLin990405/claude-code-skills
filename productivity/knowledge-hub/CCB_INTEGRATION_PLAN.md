# CCB + NotebookLM 知识库集成计划

## 目标

将 NotebookLM 作为 CCB 多 AI 协作系统的共享知识库，实现：
1. 所有 Provider 可查询 NotebookLM 中的文档
2. 研究结果自动存储到 NotebookLM
3. 统一的知识检索接口

---

## 系统架构

```
┌──────────────────────────────────────────────────────────────┐
│                      CCB Gateway (8765)                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌───────┐ ┌────────┐ │
│   │  Kimi   │ │  Qwen   │ │ DeepSeek │ │ Codex │ │ Gemini │ │
│   └────┬────┘ └────┬────┘ └────┬─────┘ └───┬───┘ └───┬────┘ │
│        │           │           │           │         │       │
│        └───────────┴───────────┼───────────┴─────────┘       │
│                                │                             │
│                                ▼                             │
│                    ┌───────────────────┐                     │
│                    │  Knowledge Router │  ← 新增组件         │
│                    └─────────┬─────────┘                     │
│                              │                               │
└──────────────────────────────┼───────────────────────────────┘
                               │
                               ▼
                    ┌───────────────────┐
                    │    NotebookLM     │
                    │   (notebooklm    │
                    │      CLI)         │
                    └───────────────────┘
                               │
                               ▼
                    ┌───────────────────┐
                    │   本地索引数据库   │
                    │  (SQLite/JSON)    │
                    └───────────────────┘
```

---

## 核心组件

### 1. Knowledge Router (新增)

**位置**: `~/.local/share/codex-dual/lib/knowledge/`

**功能**:
- 接收知识查询请求
- 匹配最相关的 notebook
- 调用 notebooklm CLI 执行查询
- 返回结构化结果

### 2. 本地索引数据库

**位置**: `~/.local/share/codex-dual/data/knowledge_index.db`

**Schema**:
```sql
-- notebooks 表
CREATE TABLE notebooks (
    id TEXT PRIMARY KEY,           -- NotebookLM notebook ID
    title TEXT NOT NULL,
    description TEXT,
    topics TEXT,                   -- JSON array: ["历史", "罗马"]
    source_count INTEGER,
    created_at TIMESTAMP,
    last_queried TIMESTAMP,
    query_count INTEGER DEFAULT 0
);

-- sources 表
CREATE TABLE sources (
    id TEXT PRIMARY KEY,
    notebook_id TEXT,
    title TEXT,
    type TEXT,                     -- pdf, url, markdown
    page_count INTEGER,
    FOREIGN KEY (notebook_id) REFERENCES notebooks(id)
);

-- query_cache 表 (可选，缓存常用查询)
CREATE TABLE query_cache (
    query_hash TEXT PRIMARY KEY,
    notebook_id TEXT,
    question TEXT,
    answer TEXT,
    references TEXT,               -- JSON
    created_at TIMESTAMP,
    ttl INTEGER DEFAULT 86400      -- 缓存有效期（秒）
);
```

### 3. CCB CLI 扩展

**新增命令**:
```bash
# 查询知识库
ccb-cli knowledge "问题"
ccb-cli knowledge "问题" --notebook <id>
ccb-cli knowledge "问题" --topic "历史"

# 同步索引
ccb-cli knowledge sync

# 列出知识库
ccb-cli knowledge list
ccb-cli knowledge list --topic "历史"

# 添加到知识库（触发 NotebookLM 上传流程）
ccb-cli knowledge add <file>
```

---

## API 设计

### Gateway API 扩展

**端点**: `POST /knowledge/query`

**请求**:
```json
{
    "question": "罗马帝国为什么衰落？",
    "notebook_id": "abc123",        // 可选，指定 notebook
    "topic": "历史",                // 可选，按主题筛选
    "max_sources": 3,               // 返回最多引用数
    "use_cache": true               // 是否使用缓存
}
```

**响应**:
```json
{
    "answer": "罗马帝国衰落的原因包括...",
    "notebook": {
        "id": "abc123",
        "title": "罗马史研究"
    },
    "references": [
        {
            "source_id": "src1",
            "title": "罗马的命运",
            "cited_text": "..."
        }
    ],
    "cached": false,
    "query_time_ms": 2500
}
```

**端点**: `POST /knowledge/sync`

同步 NotebookLM notebooks 到本地索引。

**端点**: `GET /knowledge/notebooks`

列出所有已索引的 notebooks。

---

## 实现步骤

### Phase 1: 基础架构 (Day 1-2)

1. **创建数据库 schema**
   ```bash
   mkdir -p ~/.local/share/codex-dual/data
   sqlite3 ~/.local/share/codex-dual/data/knowledge_index.db < schema.sql
   ```

2. **实现索引同步**
   - 调用 `notebooklm list --json`
   - 解析并存入 SQLite
   - 定期自动同步 (每小时)

3. **创建 Knowledge Router 模块**
   ```python
   # ~/.local/share/codex-dual/lib/knowledge/router.py
   class KnowledgeRouter:
       def query(self, question: str, notebook_id: str = None) -> dict
       def find_relevant_notebook(self, question: str) -> str
       def sync_index(self) -> int
   ```

### Phase 2: Gateway 集成 (Day 3-4)

1. **添加 Gateway 端点**
   - `/knowledge/query`
   - `/knowledge/sync`
   - `/knowledge/notebooks`

2. **实现查询路由逻辑**
   - 如果指定 notebook_id → 直接查询
   - 如果指定 topic → 筛选相关 notebooks
   - 如果都没有 → 用关键词匹配最相关 notebook

3. **添加缓存层**
   - 相同问题 + 相同 notebook → 返回缓存
   - TTL 24 小时

### Phase 3: CLI 集成 (Day 5)

1. **扩展 ccb-cli**
   ```bash
   ccb-cli knowledge "问题"
   ccb-cli knowledge sync
   ccb-cli knowledge list
   ```

2. **添加 Agent 角色**
   ```bash
   ccb-cli kimi -a librarian "问题"  # 自动查询知识库
   ```

### Phase 4: 自动化工作流 (Day 6-7)

1. **研究结果自动存储**
   - CCB 研究任务完成后
   - 自动创建 NotebookLM notebook
   - 保存研究来源

2. **智能路由**
   - 检测问题类型
   - 自动决定是否查询知识库
   - 结合 AI 回答 + 知识库引用

---

## 文件结构

```
~/.local/share/codex-dual/
├── lib/
│   ├── knowledge/
│   │   ├── __init__.py
│   │   ├── router.py         # 知识路由器
│   │   ├── index.py          # 索引管理
│   │   ├── cache.py          # 查询缓存
│   │   └── notebooklm.py     # NotebookLM CLI 封装
│   └── gateway/
│       └── knowledge_api.py  # Gateway API 端点
├── data/
│   └── knowledge_index.db    # SQLite 索引
└── config/
    └── knowledge.yaml        # 配置文件
```

---

## 配置文件

**`~/.local/share/codex-dual/config/knowledge.yaml`**:
```yaml
knowledge:
  # 索引设置
  index:
    sync_interval: 3600        # 同步间隔（秒）
    db_path: ~/.local/share/codex-dual/data/knowledge_index.db

  # 缓存设置
  cache:
    enabled: true
    ttl: 86400                 # 24小时
    max_entries: 1000

  # 查询设置
  query:
    timeout: 30                # 秒
    max_retries: 2
    default_sources: 3

  # 自动存储
  auto_save:
    enabled: true
    min_sources: 3             # 研究结果至少3个来源才保存
```

---

## 使用示例

### 示例 1: 直接查询知识库

```bash
# 用户
ccb-cli knowledge "罗马帝国衰落的原因是什么？"

# 系统
1. 搜索索引 → 找到 "罗马史研究" notebook
2. 调用 notebooklm ask "罗马帝国衰落的原因是什么？"
3. 返回答案 + 引用
```

### 示例 2: AI + 知识库协作

```bash
# 用户
ccb-cli kimi "详细解释罗马帝国的经济危机"

# 系统
1. Kimi 生成初步回答
2. 自动查询知识库补充引用
3. 合并返回：AI 分析 + 文献支持
```

### 示例 3: 研究后自动保存

```bash
# 用户
ccb-cli gemini "研究拜占庭帝国的灭亡"

# 系统
1. Gemini 执行网络研究
2. 研究完成后自动创建 NotebookLM notebook
3. 保存所有来源
4. 更新本地索引
```

---

## 依赖

- `notebooklm` CLI (已安装)
- `sqlite3`
- Python 3.9+
- CCB Gateway (已有)

---

## 注意事项

1. **NotebookLM 限制**
   - 每日查询有限额
   - 添加缓存减少重复查询

2. **索引同步**
   - 首次同步可能较慢 (254 notebooks)
   - 增量同步只更新变化

3. **隐私**
   - 知识库内容不会发送给其他 AI
   - 只有 NotebookLM 处理实际文档

---

## 验收标准

- [ ] `ccb-cli knowledge "问题"` 可正常查询
- [ ] `ccb-cli knowledge sync` 可同步索引
- [ ] Gateway `/knowledge/query` API 可用
- [ ] 查询缓存生效
- [ ] 研究结果可自动保存到 NotebookLM
