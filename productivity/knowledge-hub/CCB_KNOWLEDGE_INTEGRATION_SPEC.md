# CCB Knowledge Hub 集成完整规格书

> **目标读者**: 负责 CCB 代码库的 AI Agent
> **生成日期**: 2026-02-09
> **版本**: 1.0

---

## 1. 项目概述

### 1.1 目标

将 NotebookLM（Google 云端文档库，含 254+ notebooks）集成为 CCB 多 AI 协作系统的**共享知识库**，使所有 Provider（Kimi, Qwen, DeepSeek, Codex, Gemini 等）都能查询知识库中的文档资料。

### 1.2 当前状态

**已有基础实现**，但存在关键问题需要修复和增强：

| 组件 | 状态 | 位置 |
|------|------|------|
| Knowledge Router | ✅ 已有骨架 | `lib/knowledge/router.py` |
| Index Manager | ✅ 已有骨架 | `lib/knowledge/index_manager.py` |
| NotebookLM Client | ⚠️ 需要重写 | `lib/knowledge/notebooklm_client.py` |
| Obsidian Search | ✅ 基本可用 | `lib/knowledge/obsidian_search.py` |
| Gateway API | ✅ 已有端点 | `lib/gateway/knowledge_api.py` |
| CLI 工具 | ✅ 基本可用 | `bin/ccb-knowledge` |
| 数据库 Schema | ✅ 已有 | `lib/knowledge/schema.sql` |
| Cache | ✅ 已有 | `lib/knowledge/cache.py` |

---

## 2. 系统架构

```
┌──────────────────────────────────────────────────────────────────┐
│                      CCB Gateway (localhost:8765)                  │
├──────────────────────────────────────────────────────────────────┤
│                                                                    │
│   ┌─────────┐ ┌─────────┐ ┌──────────┐ ┌───────┐ ┌────────┐     │
│   │  Kimi   │ │  Qwen   │ │ DeepSeek │ │ Codex │ │ Gemini │     │
│   └────┬────┘ └────┬────┘ └────┬─────┘ └───┬───┘ └───┬────┘     │
│        │           │           │           │         │            │
│        └───────────┴───────────┼───────────┴─────────┘            │
│                                │                                   │
│                   ┌────────────▼────────────┐                     │
│                   │   Knowledge API Router   │ ← FastAPI 端点      │
│                   │   /knowledge/*           │                     │
│                   └────────────┬────────────┘                     │
│                                │                                   │
│                   ┌────────────▼────────────┐                     │
│                   │   KnowledgeRouter       │ ← 智能路由           │
│                   │   (router.py)           │                     │
│                   └──┬──────────────────┬───┘                     │
│                      │                  │                          │
│              ┌───────▼──────┐  ┌───────▼──────┐                  │
│              │ NotebookLM   │  │  Obsidian    │                  │
│              │  Client      │  │  Search      │                  │
│              └───────┬──────┘  └───────┬──────┘                  │
│                      │                  │                          │
└──────────────────────┼──────────────────┼──────────────────────────┘
                       │                  │
              ┌────────▼────────┐  ┌─────▼──────────────────┐
              │  notebooklm CLI │  │ ~/Desktop/新笔记        │
              │  (v0.3.2)       │  │ (Obsidian Vault)       │
              │  /Users/leo/    │  └────────────────────────┘
              │  .local/bin/    │
              │  notebooklm     │
              └────────┬────────┘
                       │
              ┌────────▼────────┐
              │  Google         │
              │  NotebookLM    │
              │  (254+ books)  │
              └────────────────┘
                       │
              ┌────────▼────────┐
              │  SQLite 索引    │
              │  knowledge_     │
              │  index.db       │
              └────────────────┘
```

---

## 3. 关键修复：NotebookLM Client 重写

### 3.1 问题

当前 `notebooklm_client.py` 使用错误的 CLI 接口。需要完全重写以匹配实际安装的 `notebooklm` CLI v0.3.2。

### 3.2 实际 CLI 位置和能力

```
二进制位置: /Users/leo/.local/bin/notebooklm
版本: 0.3.2 (notebooklm-py)
Python 包: notebooklm-py (pip install notebooklm-py)
```

### 3.3 CLI 完整命令参考

```bash
# === 认证 ===
notebooklm login                    # Google OAuth 登录
notebooklm auth check               # 检查认证状态
notebooklm auth check --test        # 完整认证验证（含网络测试）
notebooklm status                   # 显示当前上下文

# === Notebook 管理 ===
notebooklm list                     # 列出所有 notebooks（人类可读）
notebooklm list --json              # 列出所有 notebooks（JSON）
notebooklm create "标题"             # 创建新 notebook
notebooklm create "标题" --json      # 创建并返回 JSON（含 id）
notebooklm use <notebook_id>        # 设置当前上下文
notebooklm delete <notebook_id>     # 删除 notebook
notebooklm rename <id> "新标题"      # 重命名

# === Source 管理 ===
notebooklm source add <file_or_url>           # 添加来源
notebooklm source add <file_or_url> --json    # 添加并返回 JSON（含 source_id）
notebooklm source list                         # 列出当前 notebook 的来源
notebooklm source list --json                  # JSON 格式列出
notebooklm source wait <source_id>             # 等待来源处理完成
notebooklm source fulltext <source_id>         # 获取来源全文
notebooklm source fulltext <source_id> --json  # JSON 格式全文
notebooklm source guide <source_id>            # 获取来源导读

# === 聊天/查询 ===
notebooklm ask "问题"                          # 提问（使用当前 notebook）
notebooklm ask "问题" --json                   # 提问并返回 JSON（含引用）
notebooklm ask "问题" --new                    # 新对话
notebooklm ask "问题" -s <src_id1> -s <src_id2>  # 指定来源提问
notebooklm ask "问题" --notebook <notebook_id>    # 指定 notebook 提问

# === 研究 ===
notebooklm source add-research "关键词"                    # 快速网络研究
notebooklm source add-research "关键词" --mode deep        # 深度研究
notebooklm source add-research "关键词" --mode deep --no-wait  # 异步深度研究
notebooklm research status                                  # 检查研究状态
notebooklm research wait --import-all                       # 等待并导入所有研究结果

# === 生成内容 ===
notebooklm generate audio "说明"       # 生成播客
notebooklm generate video "说明"       # 生成视频
notebooklm generate report             # 生成报告
notebooklm generate quiz               # 生成测验
notebooklm generate mind-map           # 生成思维导图（同步，即时）
notebooklm generate data-table "说明"  # 生成数据表
notebooklm generate flashcards         # 生成闪卡
notebooklm generate slide-deck         # 生成幻灯片
notebooklm generate infographic        # 生成信息图

# === 下载 ===
notebooklm download audio ./output.mp3
notebooklm download video ./output.mp4
notebooklm download report ./report.md
notebooklm download mind-map ./map.json
notebooklm download quiz ./quiz.json
notebooklm download flashcards ./cards.json

# === 语言 ===
notebooklm language list              # 列出支持的语言
notebooklm language get               # 获取当前语言
notebooklm language set zh_Hans       # 设置为简体中文
```

### 3.4 CLI JSON 输出格式

**`notebooklm list --json`**:
```json
{
  "notebooks": [
    {
      "id": "abc123de-f456-7890-abcd-ef1234567890",
      "title": "《罗马帝国衰亡史》",
      "created_at": "2025-12-01T10:30:00Z"
    }
  ]
}
```

**`notebooklm source list --json`**:
```json
{
  "sources": [
    {
      "id": "src-abc123...",
      "title": "Chapter 1-5",
      "status": "ready"
    }
  ]
}
```

**`notebooklm ask "问题" --json`**:
```json
{
  "answer": "根据文档，罗马帝国衰落的原因包括...",
  "conversation_id": "conv-xxx",
  "turn_number": 1,
  "is_follow_up": false,
  "references": [
    {
      "source_id": "src-abc123...",
      "citation_number": 1,
      "cited_text": "相关引用文本..."
    }
  ]
}
```

### 3.5 并行安全

当多个 Agent 同时使用时，**不能用 `notebooklm use`**，必须用 `--notebook <id>` 或 `-n <id>` 标志：

```bash
# ❌ 错误（多 Agent 会互相覆盖上下文）
notebooklm use abc123
notebooklm ask "问题"

# ✅ 正确（并行安全）
notebooklm ask "问题" --notebook abc123
```

---

## 4. 现有代码分析与修复清单

### 4.1 文件目录

```
~/.local/share/codex-dual/
├── bin/
│   └── ccb-knowledge              # CLI 工具（Python，通过 HTTP 调 Gateway）
├── lib/
│   ├── knowledge/
│   │   ├── __init__.py            # 导出 KnowledgeRouter, NotebookLMClient 等
│   │   ├── router.py              # 主路由（307行），query/sync/stats
│   │   ├── index_manager.py       # SQLite 索引管理（upsert/search/cache）
│   │   ├── notebooklm_client.py   # ⚠️ 需要重写（当前用 npm 的错误命令）
│   │   ├── obsidian_search.py     # 本地 Obsidian 搜索
│   │   ├── cache.py               # 查询缓存封装
│   │   └── schema.sql             # 数据库 schema
│   └── gateway/
│       ├── gateway_api.py         # 主 API（自动加载 knowledge_api）
│       └── knowledge_api.py       # Knowledge API 端点（4个端点）
├── config/
│   └── gateway.yaml               # Gateway 主配置
└── data/
    └── knowledge_index.db         # SQLite 索引数据库
```

### 4.2 具体修复任务

#### 任务 1: 重写 `notebooklm_client.py`（🔴 关键）

**问题**: 当前代码调用不存在的命令（如 `npm install -g notebooklm`），完全不工作。

**新实现要求**:

```python
"""NotebookLM CLI 封装 - 基于 notebooklm-py v0.3.2"""
import json
import subprocess
from typing import Any, Dict, List, Optional

NOTEBOOKLM_BIN = "/Users/leo/.local/bin/notebooklm"

class NotebookLMClient:
    def __init__(self, timeout: int = 60):
        self.timeout = timeout
        self.bin = NOTEBOOKLM_BIN

    def _run(self, args: List[str], timeout: Optional[int] = None) -> str:
        """执行 notebooklm CLI 命令并返回 stdout"""
        cmd = [self.bin] + args
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=timeout or self.timeout,
        )
        if result.returncode != 0:
            raise RuntimeError(f"notebooklm error: {result.stderr.strip()}")
        return result.stdout.strip()

    def _run_json(self, args: List[str], timeout: Optional[int] = None) -> Any:
        """执行命令并解析 JSON 输出"""
        output = self._run(args + ["--json"], timeout=timeout)
        return json.loads(output)

    def check_auth(self) -> bool:
        """检查认证状态"""
        try:
            result = self._run_json(["auth", "check"])
            checks = result.get("checks", {})
            return all(checks.values())
        except Exception:
            return False

    def list_notebooks(self) -> List[Dict[str, Any]]:
        """列出所有 notebooks"""
        result = self._run_json(["list"])
        return result.get("notebooks", [])

    def query(self, notebook_id: str, question: str) -> Dict[str, Any]:
        """查询特定 notebook（并行安全，使用 --notebook 参数）"""
        result = self._run_json(
            ["ask", question, "--notebook", notebook_id],
            timeout=120,
        )
        return {
            "answer": result.get("answer"),
            "references": result.get("references", []),
            "conversation_id": result.get("conversation_id"),
        }

    def search_notebooks(self, query: str) -> List[Dict[str, Any]]:
        """搜索最相关的 notebook（通过标题/描述匹配）"""
        notebooks = self.list_notebooks()
        query_lower = query.lower()
        scored = []
        for nb in notebooks:
            title = (nb.get("title") or "").lower()
            score = 0
            for word in query_lower.split():
                if word in title:
                    score += 1
            if score > 0:
                scored.append((score, nb))
        scored.sort(key=lambda x: x[0], reverse=True)
        return [nb for _, nb in scored[:10]]

    def get_sources(self, notebook_id: str) -> List[Dict[str, Any]]:
        """获取 notebook 的所有来源"""
        # 需要先 use，再 list（或未来 CLI 支持 --notebook）
        self._run(["use", notebook_id])
        result = self._run_json(["source", "list"])
        return result.get("sources", [])

    def add_source(self, notebook_id: str, file_or_url: str) -> Dict[str, Any]:
        """添加来源到 notebook"""
        self._run(["use", notebook_id])
        result = self._run_json(["source", "add", file_or_url])
        return result

    def create_notebook(self, title: str) -> Dict[str, Any]:
        """创建新 notebook"""
        result = self._run_json(["create", title])
        return result  # {"id": "...", "title": "..."}

    def get_summary(self, notebook_id: str) -> str:
        """获取 notebook 摘要"""
        self._run(["use", notebook_id])
        return self._run(["summary"])
```

#### 任务 2: 更新 `router.py` 中的 NotebookLM 查询逻辑

**当前问题**: `_query_notebooklm()` 方法需要匹配新的 Client 接口。

**关键修改点**:

1. `_find_best_notebook()` - 应该用 `search_notebooks()` 做关键词匹配
2. `_query_notebooklm()` - 调用 `client.query(notebook_id, question)` 并正确解析引用
3. `sync_notebooklm()` - 调用 `client.list_notebooks()` 并写入索引

**查询路由逻辑**:
```
1. 如果指定 notebook_id → 直接查询该 notebook
2. 如果未指定 → 搜索索引数据库找最匹配的 notebook
3. 如果索引为空 → 调用 client.list_notebooks() 在线搜索
4. 如果找不到任何匹配 → 返回 error
```

#### 任务 3: 增强 `index_manager.py`

**需要增加**:
1. `upsert_notebook()` 应存储更丰富的元数据
2. 增加全文搜索能力（SQLite FTS5 或 LIKE 模糊匹配）
3. 增加 `find_best_notebook(question)` 方法 - 根据问题关键词匹配 notebooks

#### 任务 4: 更新 Obsidian 路径

**当前配置**: `~/Documents/Obsidian/Main`（不存在）
**实际路径**: `/Users/leo/Desktop/新笔记`

需要在 `router.py` 和配置中修正默认路径。

#### 任务 5: 增强 `ccb-knowledge` CLI

需要增加的命令:

```bash
# 现有命令（保留）
ccb-knowledge query "问题"                    # 查询知识库
ccb-knowledge sync                            # 同步索引
ccb-knowledge stats                           # 统计信息
ccb-knowledge list                            # 列出 notebooks

# 新增命令
ccb-knowledge add <file_or_url>               # 添加来源到 notebook
ccb-knowledge add <file_or_url> --notebook ID # 指定 notebook
ccb-knowledge create "标题"                    # 创建 notebook
ccb-knowledge search "关键词"                  # 搜索 notebooks
ccb-knowledge ask "问题" --notebook ID         # 直接指定 notebook 查询
```

#### 任务 6: 增加 Gateway API 端点

在 `knowledge_api.py` 中增加:

```
POST /knowledge/add        - 添加来源（file/url）
POST /knowledge/create     - 创建 notebook
GET  /knowledge/search     - 搜索 notebooks
POST /knowledge/ask        - 直接查询指定 notebook
GET  /knowledge/auth       - 检查 NotebookLM 认证状态
```

---

## 5. 数据库 Schema（已有，无需修改）

```sql
-- notebooks 表 (NotebookLM notebooks)
CREATE TABLE IF NOT EXISTS notebooks (
    id TEXT PRIMARY KEY,           -- NotebookLM notebook UUID
    title TEXT NOT NULL,
    description TEXT,
    topics TEXT,                   -- JSON array: ["历史", "罗马"]
    source_count INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_queried TIMESTAMP,
    query_count INTEGER DEFAULT 0
);

-- sources 表 (notebook 内的文档来源)
CREATE TABLE IF NOT EXISTS sources (
    id TEXT PRIMARY KEY,
    notebook_id TEXT,
    title TEXT,
    type TEXT,                     -- pdf, url, markdown
    page_count INTEGER,
    FOREIGN KEY (notebook_id) REFERENCES notebooks(id)
);

-- obsidian_notes 表 (本地 Obsidian 笔记索引)
CREATE TABLE IF NOT EXISTS obsidian_notes (
    path TEXT PRIMARY KEY,
    title TEXT,
    tags TEXT,                     -- JSON array
    links TEXT,                    -- JSON array
    word_count INTEGER,
    modified_at TIMESTAMP,
    indexed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- query_cache 表
CREATE TABLE IF NOT EXISTS query_cache (
    query_hash TEXT PRIMARY KEY,
    source TEXT,                   -- "notebooklm" | "obsidian"
    question TEXT,
    answer TEXT,
    references_json TEXT,          -- JSON
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    ttl INTEGER DEFAULT 86400     -- 24 小时
);

-- 索引
CREATE INDEX IF NOT EXISTS idx_notebooks_topics ON notebooks(topics);
CREATE INDEX IF NOT EXISTS idx_obsidian_tags ON obsidian_notes(tags);
CREATE INDEX IF NOT EXISTS idx_cache_created ON query_cache(created_at);
```

**数据库位置**: `~/.local/share/codex-dual/data/knowledge_index.db`

---

## 6. Gateway 集成细节

### 6.1 现有端点（`knowledge_api.py` 已实现）

```python
# 已在 gateway_api.py 中自动加载:
# from .knowledge_api import get_knowledge_api_router
# app.include_router(knowledge_router)  # 注册到 /knowledge/* 路径

POST /knowledge/query     # 查询知识库
POST /knowledge/sync      # 同步索引
GET  /knowledge/stats     # 统计信息
GET  /knowledge/notebooks # 列出 notebooks（支持 ?topic= 过滤）
```

### 6.2 请求/响应模型（已有）

```python
class QueryRequest(BaseModel):
    question: str
    source: str = "auto"           # "auto" | "notebooklm" | "obsidian"
    notebook_id: Optional[str] = None
    use_cache: bool = True

class QueryResponse(BaseModel):
    answer: Optional[str] = None
    source: str                    # 实际使用的来源
    references: List[Dict] = []    # 引用列表
    cached: bool = False
    confidence: float = 0.0
    error: Optional[str] = None
```

### 6.3 需要新增的端点

```python
# POST /knowledge/create
class CreateRequest(BaseModel):
    title: str

class CreateResponse(BaseModel):
    notebook_id: str
    title: str
    success: bool

# POST /knowledge/add-source
class AddSourceRequest(BaseModel):
    notebook_id: str
    file_or_url: str               # 文件路径或 URL

class AddSourceResponse(BaseModel):
    source_id: str
    title: str
    status: str                    # "processing" | "ready"
    success: bool

# GET /knowledge/auth
class AuthResponse(BaseModel):
    authenticated: bool
    email: Optional[str] = None

# GET /knowledge/search?q=关键词
# 返回匹配的 notebooks 列表
```

---

## 7. 配置系统

### 7.1 当前配置（在 `router.py` 中硬编码的默认值）

```yaml
knowledge:
  db_path: ~/.local/share/codex-dual/data/knowledge_index.db
  obsidian:
    vault_path: ~/Desktop/新笔记    # ⚠️ 需要从 ~/Documents/Obsidian/Main 修正为这个
    excluded_folders: [.obsidian, .trash, templates]
  notebooklm:
    bin_path: /Users/leo/.local/bin/notebooklm  # 新增：CLI 路径
    timeout: 60
    max_retries: 2
  cache:
    enabled: true
    ttl: 86400                     # 24 小时
    max_entries: 1000
  routing:
    default_source: auto
    local_first: true              # 先查 Obsidian，再查 NotebookLM
    confidence_threshold: 0.7
```

### 7.2 建议：将配置移到 `config/knowledge.yaml`

创建独立配置文件 `~/.local/share/codex-dual/config/knowledge.yaml`，让 `router.py` 加载它。

---

## 8. 使用场景

### 场景 1: Provider 自动查询知识库

```
用户 → "解释罗马帝国的经济危机"
     ↓
Claude 检测到"历史"类问题
     ↓
ccb-knowledge query "罗马帝国的经济危机"
     ↓
KnowledgeRouter.query()
  → 搜索索引 → 找到 "《罗马帝国衰亡史》" notebook
  → notebooklm ask "罗马帝国的经济危机" --notebook <id> --json
  → 解析答案 + 引用
     ↓
返回答案给用户（含文献引用）
```

### 场景 2: 同步 NotebookLM 索引

```bash
ccb-knowledge sync
     ↓
Gateway POST /knowledge/sync
     ↓
KnowledgeRouter.sync_notebooklm()
  → notebooklm list --json
  → 解析 254+ notebooks
  → 写入 SQLite notebooks 表
     ↓
返回: {"notebooks_synced": 254, "success": true}
```

### 场景 3: AI + 知识库协作

```bash
# 用户问 Kimi 一个问题
ccb-cli kimi "详细解释拜占庭的城墙防御体系"

# Kimi 回答后，自动用知识库补充引用
ccb-knowledge query "拜占庭城墙防御" --source notebooklm

# 合并两个结果呈现给用户
```

### 场景 4: 上传新资料到知识库

```bash
# 创建 notebook
ccb-knowledge create "《新书名》"

# 上传 MinerU 转换后的 Markdown
ccb-knowledge add ~/MinerU/part1/full.md --notebook <new_id>
ccb-knowledge add ~/MinerU/part2/full.md --notebook <new_id>

# 同步索引
ccb-knowledge sync
```

---

## 9. 实现步骤（按优先级排序）

### Phase 1: 修复核心（Day 1）

1. **重写 `notebooklm_client.py`**
   - 按照第 3.5 节的代码模板实现
   - 使用 `/Users/leo/.local/bin/notebooklm` CLI
   - 所有方法必须能正确调用和解析 JSON

2. **更新 `router.py` 的查询逻辑**
   - `_query_notebooklm()` 使用新的 Client 接口
   - 修正 Obsidian 默认路径为 `/Users/leo/Desktop/新笔记`

3. **测试基本查询流程**
   ```bash
   # 启动 Gateway
   cd ~/.local/share/codex-dual && python3 -m lib.gateway.gateway_server --port 8765

   # 测试同步
   ccb-knowledge sync

   # 测试查询
   ccb-knowledge query "什么是机器学习？"
   ```

### Phase 2: 增强功能（Day 2）

4. **增强 `index_manager.py`**
   - 添加 `find_best_notebook(question)` 智能匹配
   - 添加中文分词匹配（可用 jieba 或简单的字符匹配）

5. **增加 Gateway API 端点**
   - `POST /knowledge/create`
   - `POST /knowledge/add-source`
   - `GET /knowledge/auth`
   - `GET /knowledge/search?q=`

6. **更新 `ccb-knowledge` CLI**
   - 添加 `create`, `add`, `search`, `ask` 子命令

### Phase 3: 集成优化（Day 3）

7. **创建 `config/knowledge.yaml`** 配置文件
8. **添加首次同步逻辑** - Gateway 启动时自动同步
9. **添加定期同步** - 每小时自动同步一次
10. **测试完整工作流**

---

## 10. 环境信息

| 项目 | 值 |
|------|------|
| 操作系统 | macOS (Darwin 23.2.0) |
| Python | 3.x |
| CCB 根目录 | `~/.local/share/codex-dual/` |
| Gateway 端口 | 8765 |
| notebooklm CLI | `/Users/leo/.local/bin/notebooklm` (v0.3.2) |
| Obsidian Vault | `/Users/leo/Desktop/新笔记` |
| 数据库 | `~/.local/share/codex-dual/data/knowledge_index.db` |
| Gateway 数据库 | `~/.ccb_config/gateway.db` |
| Notebook 数量 | 254+ |
| Gateway 框架 | FastAPI |
| NotebookLM 每日限额 | 有限（需要缓存减少调用） |

---

## 11. 验收标准

- [ ] `notebooklm_client.py` 重写完成，能正确调用 `notebooklm` CLI
- [ ] `ccb-knowledge sync` 能同步所有 254+ notebooks 到索引
- [ ] `ccb-knowledge query "问题"` 能自动找到最相关 notebook 并返回答案
- [ ] `ccb-knowledge query "问题" --notebook-id <id>` 能查询指定 notebook
- [ ] 查询缓存生效（相同问题第二次查询从缓存返回）
- [ ] Obsidian 搜索使用正确的 vault 路径
- [ ] Gateway API 所有端点可用
- [ ] 新增的 `create`, `add-source`, `search`, `auth` 端点可用
- [ ] `ccb-knowledge` CLI 所有新增子命令可用
- [ ] 并行查询时不会出现上下文冲突（使用 `--notebook` 参数）

---

## 12. 注意事项

1. **NotebookLM 认证**: CLI 需要先 `notebooklm login`，Session 可能过期
2. **限额**: NotebookLM 有每日查询限制，必须实现缓存
3. **并行安全**: 永远使用 `--notebook <id>` 参数，不要用 `notebooklm use`
4. **超时**: NotebookLM 查询可能需要 10-60 秒，设置足够的 timeout
5. **索引同步**: 首次同步 254+ notebooks 可能较慢，增量同步只更新变化
6. **Obsidian MCP**: 已配置在 `~/.claude/settings.json` 中，通过 `npx mcp-obsidian` 访问
7. **不要修改 Gateway 核心**: 只修改 `lib/knowledge/` 目录和 `lib/gateway/knowledge_api.py`
