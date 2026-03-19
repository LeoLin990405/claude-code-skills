<div align="center">

# 🧩 Claude Code Skills

**A curated collection of 60+ skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code)**

[![Skills](https://img.shields.io/badge/skills-60%2B-blue?style=for-the-badge)](.)
[![Categories](https://img.shields.io/badge/categories-9-green?style=for-the-badge)](.)
[![Submodules](https://img.shields.io/badge/submodules-12-orange?style=for-the-badge)](.)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

*Productivity · Development · Documents · Research · AI · PM · Security · Design · System*

</div>

---

## Architecture

```
~/.claude/skills/              <-- symlinked by install.sh
    obsidian-cli/    -> repo/productivity/obsidian-cli   (submodule)
    pdf/             -> repo/documents/pdf               (bundled)
    ...

claude-code-skills/            <-- this repository
├── productivity/        8 skills   Obsidian, GWS, NotebookLM
├── development/        13 skills   Playwright, D3.js, iOS, R, MCP
├── documents/           6 skills   PDF, DOCX, PPTX, XLSX, MinerU
├── research/            6 skills   140+ scientific, ARIS, STEM
├── ai-collaboration/    5 skills   Multi-AI Gateway, Agent Teams
├── product-management/ 16 skills   Lenny's Podcast PM framework
├── security/            2 skills   Trail of Bits (50+), ffuf
├── design/              7 skills   Canvas, themes, GIF, assets
├── system/              5 skills   Proxy, CDP, SVN, comms, OSS
├── install.sh                      Symlink installer
├── CONTRIBUTING.md                 Contribution guide
└── LICENSE                         MIT
```

---

## 🚀 Quick Start

### Install All Skills

```bash
git clone --recurse-submodules https://github.com/LeoLin990405/claude-code-skills.git
cd claude-code-skills && ./install.sh
```

### Install One Category

```bash
./install.sh productivity    # Only productivity skills
```

### Install a Single Skill

```bash
cd ~/.claude/skills
git clone https://github.com/LeoLin990405/obsidian-cli-skill.git obsidian-cli
```

---

## 📦 Categories

| | Category | Skills | Highlights |
|---|---------|--------|-----------|
| 🗂️ | [Productivity](#%EF%B8%8F-productivity) | 8 | Obsidian CLI, NotebookLM, Google Workspace |
| 💻 | [Development](#-development) | 13 | Playwright, D3.js, iOS Simulator, R Analytics |
| 📄 | [Documents](#-documents) | 6 | PDF, DOCX, PPTX, XLSX, MinerU |
| 🔬 | [Research](#-research) | 6 | 140+ Scientific Skills, ARIS, STEM Modeling |
| 🤖 | [AI Collaboration](#-ai-collaboration) | 5 | Multi-AI Gateway, Agent Teams, Superpowers |
| 📊 | [Product Management](#-product-management) | 16 | Lenny's Podcast -- 86 actionable PM skills |
| 🔒 | [Security](#-security) | 2 | Trail of Bits (50+ skills), ffuf |
| 🎨 | [Design](#-design) | 7 | Canvas Art, Themes, GIF Creation |
| ⚙️ | [System](#%EF%B8%8F-system) | 5 | Proxy, CDP, SVN, Internal Comms |

---

### 🗂️ Productivity

| Skill | Description | Type |
|-------|-------------|------|
| **[obsidian-cli](productivity/obsidian-cli)** | Obsidian vault CLI -- 80+ commands for search, tags, properties, links | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/LeoLin990405/obsidian-cli-skill) |
| **[obsidian-markdown](productivity/obsidian-markdown)** | Obsidian Flavored Markdown -- wikilinks, callouts, embeds | `bundled` |
| **[obsidian-bases](productivity/obsidian-bases)** | Obsidian Bases -- database views, filters, formulas | `bundled` |
| **[json-canvas](productivity/json-canvas)** | JSON Canvas files -- nodes, edges, mind maps | `bundled` |
| **[gws-workspace](productivity/gws-workspace)** | Google Workspace CLI -- Drive, Gmail, Sheets, Calendar | `bundled` |
| **[knowledge-hub](productivity/knowledge-hub)** | NotebookLM + Obsidian + PDF pipeline orchestration | `bundled` |
| **[notebooklm](productivity/notebooklm)** | NotebookLM API -- notebooks, sources, podcasts | `bundled` |
| **[daily-update-checker](productivity/daily-update-checker)** | Auto-check CLI tool updates (Homebrew, npm, pip) | `bundled` |

### 💻 Development

| Skill | Description | Type |
|-------|-------------|------|
| **[playwright-skill](development/playwright-skill)** | Browser automation and testing with Playwright | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/lackeyjb/playwright-skill) |
| **[claude-d3js-skill](development/claude-d3js-skill)** | D3.js interactive data visualizations | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/chrisvoncsefalvay/claude-d3js-skill) |
| **[ios-simulator-skill](development/ios-simulator-skill)** | iOS app testing and automation | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/conorluddy/ios-simulator-skill) |
| **[github-repo-design](development/github-repo-design)** | GitHub repo design and README best practices | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/LeoLin990405/github-repo-design-skill) |
| **[r-analytics](development/r-analytics)** | R language data analysis and visualization | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/LeoLin990405/r-analytics-skill) |
| **[frontend-design](development/frontend-design)** | Production-grade frontend with high design quality | `bundled` |
| **[webapp-testing](development/webapp-testing)** | Web app testing with Playwright | `bundled` |
| **[web-artifacts-builder](development/web-artifacts-builder)** | React + Tailwind + shadcn/ui artifacts | `bundled` |
| **[mcp-builder](development/mcp-builder)** | Build MCP servers for LLM tool integration | `bundled` |
| **[skill-creator](development/skill-creator)** | Guide for creating new Claude Code skills | `bundled` |
| **[algorithmic-art](development/algorithmic-art)** | Algorithmic art generation | `bundled` |
| **[doris-query](development/doris-query)** | Doris data warehouse read-only queries | `bundled` |
| **[sql2sh](development/sql2sh)** | SQL to Doris ETL shell scripts | `bundled` |

### 📄 Documents

| Skill | Description | Type |
|-------|-------------|------|
| **[pdf](documents/pdf)** | PDF manipulation -- extract, create, merge, forms | `bundled` |
| **[docx](documents/docx)** | Word documents -- tracked changes, comments | `bundled` |
| **[pptx](documents/pptx)** | PowerPoint presentations | `bundled` |
| **[xlsx](documents/xlsx)** | Excel spreadsheets -- formulas, charts | `bundled` |
| **[doc-coauthoring](documents/doc-coauthoring)** | Structured document co-authoring workflow | `bundled` |
| **[mineru](documents/mineru)** | PDF/DOC/PPT to Markdown via MinerU API | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/LeoLin990405/mineru-skill) |

### 🔬 Research

| Skill | Description | Type |
|-------|-------------|------|
| **[claude-scientific-skills](research/claude-scientific-skills)** | 140+ scientific skills for data, bio, chem, physics | `bundled` |
| **[aris](research/aris)** | Auto Research In Sleep -- overnight research agent | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/LeoLin990405/Auto-claude-code-research-in-sleep) |
| **[stem-modeling](research/stem-modeling)** | STEM academic modeling with multi-AI collaboration | `bundled` |
| **[history-note-processor](research/history-note-processor)** | Historical reading notes (4-step methodology) | `bundled` |
| **[blog-writer](research/blog-writer)** | Jekyll blog posts -- bilingual, SVG diagrams | `bundled` |
| **[macro-research-ccb](research/macro-research-ccb)** | Distributed macro research for A-shares | `bundled` |

### 🤖 AI Collaboration

| Skill | Description | Type |
|-------|-------------|------|
| **[ccb-unified](ai-collaboration/ccb-unified)** | 9-provider AI orchestration via Gateway API | `bundled` |
| **[agent-teams](ai-collaboration/agent-teams)** | Multi-session Claude Code team orchestration | `bundled` |
| **[superpowers](ai-collaboration/superpowers)** | Skill discovery and usage framework | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/obra/superpowers) |
| **[anthropic-docs](ai-collaboration/anthropic-docs)** | Anthropic official docs knowledge base | `bundled` |
| **[find-skills](ai-collaboration/find-skills)** | Discover and install agent skills | `bundled` |

### 📊 Product Management

All skills derived from [Lenny's Podcast](https://www.lennysnewsletter.com/) -- 86 actionable PM skills:

| Skill | Focus Area |
|-------|-----------|
| **[lenny-skills](product-management/lenny-skills)** | 86 actionable PM skills (master index) |
| **[lenny-strategy](product-management/lenny-strategy)** | Vision, roadmap, OKRs, PRDs |
| **[lenny-growth](product-management/lenny-growth)** | PMF, growth loops, pricing, retention |
| **[lenny-hiring](product-management/lenny-hiring)** | Job descriptions, interviews, onboarding |
| **[lenny-execution](product-management/lenny-execution)** | Shipping, timelines, cross-functional |
| **[lenny-marketing](product-management/lenny-marketing)** | Positioning, storytelling, launch |
| **[lenny-sales](product-management/lenny-sales)** | Founder sales, enterprise, BD |
| **[lenny-design](product-management/lenny-design)** | Design systems, reviews, engineering |
| **[lenny-technology](product-management/lenny-technology)** | AI strategy, LLMs, tech debt |
| **[lenny-communication](product-management/lenny-communication)** | Presentations, writing, alignment |
| **[lenny-decision](product-management/lenny-decision)** | Decision processes, trade-offs |
| **[lenny-research](product-management/lenny-research)** | User interviews, surveys, usability |
| **[lenny-advanced](product-management/lenny-advanced)** | Product taste, systems thinking |
| **[lenny-career](product-management/lenny-career)** | Ideation, productivity, imposter syndrome |
| **[lenny-startup](product-management/lenny-startup)** | Fundraising, pivoting, team rituals |
| **[lenny-playbooks](product-management/lenny-playbooks)** | Curated skill combos by role |

### 🔒 Security

| Skill | Description | Type |
|-------|-------------|------|
| **[trailofbits-security](security/trailofbits-security)** | 50+ security auditing, fuzzing, and analysis skills | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/trailofbits/skills) |
| **[ffuf_claude_skill](security/ffuf_claude_skill)** | ffuf web fuzzing for penetration testing | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/jthack/ffuf_claude_skill) |

### 🎨 Design

| Skill | Description | Type |
|-------|-------------|------|
| **[canvas-design](design/canvas-design)** | Visual art in PNG/PDF | `bundled` |
| **[brand-guidelines](design/brand-guidelines)** | Anthropic brand colors and typography | `bundled` |
| **[theme-factory](design/theme-factory)** | 10 pre-set themes for any artifact | `bundled` |
| **[cli-demo-gif](design/cli-demo-gif)** | CLI demo GIFs via vhs | `bundled` |
| **[slack-gif-creator](design/slack-gif-creator)** | Animated GIFs optimized for Slack | `bundled` |
| **[asciinema-recorder](design/asciinema-recorder)** | Terminal session recording | `bundled` |
| **[web-asset-generator](design/web-asset-generator)** | Favicons, app icons, OG images | [![Submodule](https://img.shields.io/badge/↗-submodule-blue)](https://github.com/alonw0/web-asset-generator) |

### ⚙️ System

| Skill | Description | Type |
|-------|-------------|------|
| **[proxy-manager](system/proxy-manager)** | Proxifier + Clash Verge + Charles management | `bundled` |
| **[cdp-ai-tools](system/cdp-ai-tools)** | CDP interaction with local AI apps | `bundled` |
| **[internal-comms](system/internal-comms)** | Internal communications templates | `bundled` |
| **[svn](system/svn)** | SVN version control operations | `bundled` |
| **[oss-contribution](system/oss-contribution)** | Open source contribution etiquette | `bundled` |

---

## 🔗 Submodules

12 skills are linked from their upstream repositories:

| Skill | Repository | Category |
|-------|-----------|----------|
| obsidian-cli | [LeoLin990405/obsidian-cli-skill](https://github.com/LeoLin990405/obsidian-cli-skill) | Productivity |
| claude-d3js-skill | [chrisvoncsefalvay/claude-d3js-skill](https://github.com/chrisvoncsefalvay/claude-d3js-skill) | Development |
| playwright-skill | [lackeyjb/playwright-skill](https://github.com/lackeyjb/playwright-skill) | Development |
| ios-simulator-skill | [conorluddy/ios-simulator-skill](https://github.com/conorluddy/ios-simulator-skill) | Development |
| github-repo-design | [LeoLin990405/github-repo-design-skill](https://github.com/LeoLin990405/github-repo-design-skill) | Development |
| r-analytics | [LeoLin990405/r-analytics-skill](https://github.com/LeoLin990405/r-analytics-skill) | Development |
| mineru | [LeoLin990405/mineru-skill](https://github.com/LeoLin990405/mineru-skill) | Documents |
| aris | [LeoLin990405/Auto-claude-code-research-in-sleep](https://github.com/LeoLin990405/Auto-claude-code-research-in-sleep) | Research |
| superpowers | [obra/superpowers](https://github.com/obra/superpowers) | AI Collaboration |
| trailofbits-security | [trailofbits/skills](https://github.com/trailofbits/skills) | Security |
| ffuf_claude_skill | [jthack/ffuf_claude_skill](https://github.com/jthack/ffuf_claude_skill) | Security |
| web-asset-generator | [alonw0/web-asset-generator](https://github.com/alonw0/web-asset-generator) | Design |

```bash
# Update all submodules
git submodule update --remote --merge

# Clone with submodules
git clone --recurse-submodules https://github.com/LeoLin990405/claude-code-skills.git
```

---

## 🤝 Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for details on adding skills, reporting bugs, and submitting PRs.

## 📄 License

Original skills are released under the [MIT License](LICENSE). Submodule skills retain their original upstream licenses.
