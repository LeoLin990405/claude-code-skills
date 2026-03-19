---
name: knowledge-hub
description: 统一知识库编排层 - 协调 NotebookLM (云端 254+ notebooks) + Obsidian (本地笔记) + pdf-to-notebook (全自动PDF pipeline) + Gateway API (ccb-knowledge)
triggers:
  - 研究
  - 查资料
  - 上传PDF
  - 上传书籍
  - 知识库
  - knowledge
  - ccb-knowledge
dependencies:
  - notebooklm
---

# Knowledge Hub - 统一知识库编排层

> **定位**: 高层编排技能，协调多个知识源。NotebookLM 底层 API 细节见 `notebooklm` skill。

## 架构

```
┌─────────────────────────────────────────────────────────────┐
│                  Knowledge Hub (编排层)                       │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  用户请求 → 路由决策 → 执行 → 返回结果                        │
│                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ NotebookLM   │  │  Obsidian    │  │ PDF Pipeline │      │
│  │ (云端 254+)  │  │ (本地笔记)   │  │ (全自动)     │      │
│  │              │  │              │  │              │      │
│  │ → notebooklm │  │ → MCP 工具   │  │ → pdf-to-    │      │
│  │   skill 底层 │  │ → ccb-knowledge│ │   notebook   │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                             │
├─────────────────────────────────────────────────────────────┤
│  Gateway API: http://localhost:8765/knowledge/*              │
│  CLI 工具:    ccb-knowledge | pdf-to-notebook               │
└─────────────────────────────────────────────────────────────┘
```

## 组件清单

| 组件 | 用途 | 接口 | 详细文档 |
|------|------|------|----------|
| **NotebookLM** | 云端文档库、AI 问答、生成播客/视频 | `notebooklm` CLI | **→ 见 `notebooklm` skill** |
| **Obsidian** | 本地 Markdown 笔记读写 | MCP server | vault: `~/Desktop/新笔记` |
| **pdf-to-notebook** | 全自动 PDF→NotebookLM pipeline | CLI | `pdf-to-notebook <pdf> "标题"` |
| **PyMuPDF** | PDF 分析/分割/文本提取 | Python | `pip install pymupdf` |
| **magic-pdf** | 扫描件 PDF→Markdown (OCR) | CLI | `magic-pdf pdf-command --pdf ...` |
| **Gateway API** | HTTP 统一接口 | REST | `http://localhost:8765/knowledge/*` |
| **ccb-knowledge** | CLI 统一入口 | 命令行 | `ccb-knowledge <subcommand>` |

---

## 路由决策 (核心逻辑)

**当用户提出知识类请求时，按以下规则选择路径：**

```
用户请求
  │
  ├── 包含 "播客/podcast/audio/video/quiz" ?
  │   └── YES → 直接用 notebooklm skill (生成类任务)
  │
  ├── 涉及 PDF 上传/书籍 ?
  │   └── YES → pdf-to-notebook (全自动 pipeline)
  │
  ├── "保存到笔记" / "写笔记" ?
  │   └── YES → Obsidian MCP
  │
  ├── 需要查询已有知识 ?
  │   ├── Gateway 运行中 → ccb-knowledge query "问题"
  │   │   (自动路由 NotebookLM/Obsidian，带缓存)
  │   └── Gateway 未运行 → notebooklm ask "问题"
  │
  └── "帮我研究 XXX" ?
      └── notebooklm create + source add-research
```

---

## Gateway API 接口

### ccb-knowledge CLI

```bash
# 查询 (自动路由到最匹配的 notebook/Obsidian)
ccb-knowledge query "什么是闭包?"
ccb-knowledge query "React hooks" -s notebooklm     # 指定来源
ccb-knowledge query "Vim 配置" -n <notebook_id>     # 指定 notebook
ccb-knowledge query "问题" --no-cache               # 绕过缓存

# 索引管理
ccb-knowledge sync           # 同步 NotebookLM notebooks 到本地索引
ccb-knowledge list           # 列出已索引的 notebooks
ccb-knowledge list --topic python  # 按主题过滤
ccb-knowledge search "React" # 搜索 notebooks
ccb-knowledge stats          # 统计信息

# Notebook 管理
ccb-knowledge create "标题"                    # 创建新 notebook
ccb-knowledge add <notebook_id> <file_or_url>  # 添加来源
ccb-knowledge auth                             # 检查认证状态
```

### HTTP 端点

| 方法 | 端点 | 用途 |
|------|------|------|
| POST | `/knowledge/query` | 查询知识（自动路由） |
| POST | `/knowledge/sync` | 同步 notebooks 到索引 |
| GET | `/knowledge/stats` | 统计信息 |
| GET | `/knowledge/notebooks` | 列出已索引 notebooks |
| GET | `/knowledge/search?q=` | 搜索 notebooks |
| POST | `/knowledge/create` | 创建 notebook |
| POST | `/knowledge/add-source` | 添加来源 |
| GET | `/knowledge/auth` | 检查认证状态 |

### 查询自动路由逻辑

```
POST /knowledge/query {"question": "...", "source": "auto"}
  │
  ├── 1. 搜索本地 SQLite 索引 → 找最匹配 notebook
  │      (基于 title/description/topics 关键词匹配)
  │
  ├── 2. 检查缓存 → 命中则直接返回 (TTL: 24h)
  │
  ├── 3. 查询 NotebookLM (notebooklm ask --notebook <id>)
  │      或 Obsidian (本地文件搜索)
  │
  └── 4. 缓存结果 → 返回
```

---

## 工作流

### A: 快速问答

```bash
# 优先通过 Gateway (带缓存 + 自动路由)
ccb-knowledge query "什么是闭包?"

# 或直接 NotebookLM (无缓存)
notebooklm ask "什么是闭包?" --notebook <id>
```

### B: 网络研究

```bash
# 1. 创建 notebook
notebooklm create "XXX 研究"

# 2. 深度网络研究 (自动搜索 + 导入来源)
notebooklm source add-research "XXX" --mode deep --import-all

# 3. 提问
notebooklm ask "总结关键内容"

# 4. (可选) 保存到 Obsidian
# 使用 Obsidian MCP: create_note
```

> NotebookLM 研究的完整选项 (--mode fast/deep, --from web/drive, subagent 模式等) → 见 `notebooklm` skill

### C: PDF 书籍上传 (全自动)

**一条命令完成: 分析 → 分割 → 转换 → 上传**

```bash
# 基本用法 (全自动)
pdf-to-notebook /path/to/book.pdf "《书名》"

# 预览模式 (只分析，不执行)
pdf-to-notebook /path/to/book.pdf "《书名》" --dry-run

# 上传到已有 notebook
pdf-to-notebook /path/to/book.pdf "《书名》" --notebook-id <id>

# 指定每片最大页数
pdf-to-notebook /path/to/book.pdf "《书名》" --max-pages 400

# 强制使用 magic-pdf (支持扫描件 OCR)
pdf-to-notebook /path/to/book.pdf "《书名》" --method magic-pdf
```

**自动处理流程：**

```
pdf-to-notebook
  │
  ├── [1/5] 分析: PyMuPDF 读取页数、目录、文本检测
  ├── [2/5] 规划: 按章节边界计算分割方案 (每片 ≤500 页)
  ├── [3/5] 分割: PyMuPDF 自动分割 PDF (无需 iLovePDF)
  ├── [4/5] 转换: PyMuPDF 文本提取 / MinerU Cloud API OCR
  └── [5/5] 上传: notebooklm create + source add (自动)
```

**转换方法选择：**

| 方法 | 适用场景 | 速度 | 依赖 |
|------|---------|------|------|
| `pymupdf` (默认) | 文本型 PDF | 极快 (秒级) | PyMuPDF (本地) |
| `mineru` | 扫描件/图片 PDF (OCR) | 快 (5-30秒) | MinerU Cloud API |
| `auto` | 自动检测 PDF 类型 | 按需 | - |

**MinerU API 配置：**
- Token: `~/.config/mineru/token` 或 `MINERU_API_TOKEN` 环境变量
- API 限制: 单文件 ≤200MB, ≤600 页, 批量 ≤200 文件
- 管理页面: https://mineru.net/apiManage/token

### D: 保存到 Obsidian

```bash
# 通过 Obsidian MCP
search_notes "关键词"     # 搜索现有笔记
read_note "笔记路径"      # 读取笔记
create_note "路径" "内容"  # 创建新笔记
update_note "路径" "内容"  # 更新笔记
```

---

## 工作流模板汇总

| 触发词 | 工作流 | 工具链 |
|--------|--------|--------|
| "XXX 是什么" / 查资料 | A: 快速问答 | ccb-knowledge query 或 notebooklm ask |
| "帮我研究 XXX" | B: 网络研究 | notebooklm create → add-research → ask |
| "上传这本 PDF" | C: PDF 上传 | `pdf-to-notebook` (全自动) |
| "生成播客/视频/报告" | → notebooklm skill | notebooklm generate audio/video/report |
| "保存到笔记" | D: Obsidian | Obsidian MCP create_note |
| "知识库统计" | Gateway API | ccb-knowledge stats |
| "同步索引" | Gateway API | ccb-knowledge sync |

---

## 限制

| 限制 | 说明 |
|------|------|
| NotebookLM 单次上传 | ≤600 页 (`pdf-to-notebook` 自动分割) |
| NotebookLM 生成限流 | audio/video/quiz 可能被 Google 限流 |
| 扫描件 PDF | MinerU Cloud API 自动处理 (token: `~/.config/mineru/token`) |
| Gateway 缓存 | TTL 24h，用 `--no-cache` 绕过 |

> 生成类任务的限流处理、重试策略、exit codes → 见 `notebooklm` skill

---

## 更新索引

```bash
# 同步 NotebookLM notebooks 到本地 SQLite 索引
ccb-knowledge sync

# 更新 skill 本地缓存 (供 Claude 快速查找)
notebooklm list --json > ~/.claude/skills/notebooklm/notebooks-index.json
```
