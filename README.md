# Claude Code Skills Collection

60+ skills for [Claude Code](https://docs.anthropic.com/en/docs/claude-code) organized by category. Includes both original skills and curated community skills (via git submodules).

## Quick Install

```bash
# Clone with all submodules
git clone --recurse-submodules https://github.com/LeoLin990405/claude-code-skills.git

# Install all skills (symlinks to ~/.claude/skills/)
cd claude-code-skills
./install.sh

# Or install a specific category
./install.sh productivity
```

## Categories

### 🗂️ Productivity (7 skills)
| Skill | Description | Source |
|-------|-------------|--------|
| [obsidian-cli](productivity/obsidian-cli) | Obsidian vault CLI (80+ commands) — search, tags, properties, links | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/LeoLin990405/obsidian-cli-skill) |
| [obsidian-markdown](productivity/obsidian-markdown) | Obsidian Flavored Markdown — wikilinks, callouts, embeds | direct |
| [obsidian-bases](productivity/obsidian-bases) | Obsidian Bases — database views, filters, formulas | direct |
| [json-canvas](productivity/json-canvas) | JSON Canvas files — nodes, edges, mind maps | direct |
| [gws-workspace](productivity/gws-workspace) | Google Workspace CLI — Drive, Gmail, Sheets, Calendar | direct |
| [knowledge-hub](productivity/knowledge-hub) | NotebookLM + Obsidian + PDF pipeline orchestration | direct |
| [daily-update-checker](productivity/daily-update-checker) | Auto-check CLI tool updates (Homebrew, npm, pip) | direct |
| [notebooklm](productivity/notebooklm) | NotebookLM API — notebooks, sources, podcasts | direct |

### 💻 Development (10 skills)
| Skill | Description | Source |
|-------|-------------|--------|
| [frontend-design](development/frontend-design) | Production-grade frontend with high design quality | direct |
| [claude-d3js-skill](development/claude-d3js-skill) | D3.js interactive data visualizations | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/chrisvoncsefalvay/claude-d3js-skill) |
| [playwright-skill](development/playwright-skill) | Browser automation with Playwright | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/lackeyjb/playwright-skill) |
| [ios-simulator-skill](development/ios-simulator-skill) | iOS app testing and automation | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/conorluddy/ios-simulator-skill) |
| [github-repo-design](development/github-repo-design) | GitHub repo design & README best practices | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/LeoLin990405/github-repo-design-skill) |
| [r-analytics](development/r-analytics) | R language data analysis and visualization | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/LeoLin990405/r-analytics-skill) |
| [webapp-testing](development/webapp-testing) | Web app testing with Playwright | direct |
| [web-artifacts-builder](development/web-artifacts-builder) | React + Tailwind + shadcn/ui artifacts | direct |
| [mcp-builder](development/mcp-builder) | Build MCP servers for LLM tool integration | direct |
| [skill-creator](development/skill-creator) | Guide for creating new Claude Code skills | direct |

### 📄 Documents (6 skills)
| Skill | Description | Source |
|-------|-------------|--------|
| [pdf](documents/pdf) | PDF manipulation — extract, create, merge, forms | direct |
| [docx](documents/docx) | Word documents — tracked changes, comments | direct |
| [pptx](documents/pptx) | PowerPoint presentations | direct |
| [xlsx](documents/xlsx) | Excel spreadsheets — formulas, charts | direct |
| [doc-coauthoring](documents/doc-coauthoring) | Structured doc co-authoring workflow | direct |
| [mineru](documents/mineru) | PDF/DOC/PPT → Markdown via MinerU API | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/LeoLin990405/mineru-skill) |

### 🔬 Research (6 skills)
| Skill | Description | Source |
|-------|-------------|--------|
| [claude-scientific-skills](research/claude-scientific-skills) | 140+ scientific skills for data/bio/chem/physics | direct |
| [aris](research/aris) | Auto Research In Sleep — overnight research agent | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/LeoLin990405/Auto-claude-code-research-in-sleep) |
| [stem-modeling](research/stem-modeling) | STEM academic modeling with multi-AI | direct |
| [history-note-processor](research/history-note-processor) | Historical reading notes (4-step methodology) | direct |
| [blog-writer](research/blog-writer) | Jekyll blog posts — bilingual, SVG diagrams | direct |
| [macro-research-ccb](research/macro-research-ccb) | Distributed macro research for A-shares | direct |

### 🤖 AI Collaboration (4 skills)
| Skill | Description | Source |
|-------|-------------|--------|
| [ccb-unified](ai-collaboration/ccb-unified) | 9-provider AI orchestration via Gateway API | direct |
| [agent-teams](ai-collaboration/agent-teams) | Multi-session Claude Code team orchestration | direct |
| [superpowers](ai-collaboration/superpowers) | Skill discovery and usage framework | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/obra/superpowers) |
| [anthropic-docs](ai-collaboration/anthropic-docs) | Anthropic official docs knowledge base | direct |
| [find-skills](ai-collaboration/find-skills) | Discover and install agent skills | direct |

### 📊 Product Management (16 skills)
All [Lenny's Podcast](https://www.lennysnewsletter.com/) PM skills:

| Skill | Focus Area |
|-------|-----------|
| lenny-skills | 86 actionable PM skills (master index) |
| lenny-strategy | Vision, roadmap, OKRs, PRDs |
| lenny-growth | PMF, growth loops, pricing, retention |
| lenny-hiring | Job descriptions, interviews, onboarding |
| lenny-execution | Shipping, timelines, cross-functional |
| lenny-marketing | Positioning, storytelling, launch |
| lenny-sales | Founder sales, enterprise, BD |
| lenny-design | Design systems, reviews, engineering |
| lenny-technology | AI strategy, LLMs, tech debt |
| lenny-communication | Presentations, writing, alignment |
| lenny-decision | Decision processes, trade-offs |
| lenny-research | User interviews, surveys, usability |
| lenny-advanced | Product taste, systems thinking |
| lenny-career | Ideation, productivity, imposter syndrome |
| lenny-startup | Fundraising, pivoting, team rituals |
| lenny-playbooks | Curated skill combos by role |

### 🔒 Security (2 skills)
| Skill | Description | Source |
|-------|-------------|--------|
| [trailofbits-security](security/trailofbits-security) | 50+ security auditing, fuzzing, analysis skills | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/trailofbits/skills) |
| [ffuf_claude_skill](security/ffuf_claude_skill) | ffuf web fuzzing for penetration testing | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/jthack/ffuf_claude_skill) |

### 🎨 Design (6 skills)
| Skill | Description | Source |
|-------|-------------|--------|
| [canvas-design](design/canvas-design) | Visual art in PNG/PDF | direct |
| [brand-guidelines](design/brand-guidelines) | Anthropic brand colors & typography | direct |
| [theme-factory](design/theme-factory) | 10 pre-set themes for any artifact | direct |
| [cli-demo-gif](design/cli-demo-gif) | CLI demo GIFs via vhs | direct |
| [slack-gif-creator](design/slack-gif-creator) | Animated GIFs optimized for Slack | direct |
| [web-asset-generator](design/web-asset-generator) | Favicons, app icons, OG images | [![GitHub](https://img.shields.io/badge/-submodule-blue)](https://github.com/alonw0/web-asset-generator) |

### ⚙️ System (7 skills)
| Skill | Description | Source |
|-------|-------------|--------|
| [proxy-manager](system/proxy-manager) | Proxifier + Clash Verge + Charles management | direct |
| [cdp-ai-tools](system/cdp-ai-tools) | CDP interaction with local AI apps | direct |
| [internal-comms](system/internal-comms) | Internal communications templates | direct |
| [svn](system/svn) | SVN version control operations | direct |
| [oss-contribution](system/oss-contribution) | Open source contribution etiquette | direct |
| [asciinema-recorder](design/asciinema-recorder) | Terminal session recording | direct |
| [doris-query](development/doris-query) | Doris data warehouse read-only queries | direct |
| [sql2sh](development/sql2sh) | SQL to Doris ETL shell scripts | direct |

## Submodules

12 skills are linked as git submodules — they stay in sync with their upstream repos:

```bash
# Update all submodules to latest
git submodule update --remote --merge

# Update a specific submodule
cd productivity/obsidian-cli && git pull
```

## Creating New Skills

See [skill-creator](development/skill-creator) for a guide on creating new skills.

## License

Original skills: MIT. Submodule skills retain their original licenses.
