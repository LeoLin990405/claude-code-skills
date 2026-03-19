---
name: blog-writer
description: End-to-end Jekyll blog post creation with bilingual Chinese/English support, SVG diagrams, and agent team parallelization. Use when (1) writing new blog posts, (2) translating existing posts to bilingual format, (3) adding SVG illustrations to posts, (4) batch-processing multiple posts with agent teams, (5) publishing to GitHub Pages. Triggers on "write a blog post", "new blog", "add illustrations", "translate posts to bilingual", "publish to blog".
---

# Blog Writer Skill

Create, translate, and illustrate Jekyll blog posts for a dark-themed GitHub Pages blog with bilingual Chinese/English toggle support.

## Quick Reference

| Task | Command |
|------|---------|
| New post | Follow [New Post Workflow](#new-post-workflow) |
| Bilingual conversion | Follow [Bilingual Conversion](#bilingual-conversion) |
| Add diagrams | Follow [SVG Diagram Creation](#svg-diagram-creation) |
| Batch translate | Follow [Agent Team Patterns](#agent-team-patterns) |
| Publish | `cd <repo> && git add . && git commit && git push origin main` |

## Blog Architecture

See [references/architecture.md](references/architecture.md) for repo structure, theme colors, layout details.

## New Post Workflow

### 1. Create file

```
_posts/YYYY-MM-DD-slug-title.md
```

### 2. Frontmatter template

```yaml
---
layout: post
title: "中文标题"
title_en: "English Title"
date: YYYY-MM-DD
tags: [Tag1, Tag2]
categories: [essay, reading]  # or [engineering, learning]
bilingual: true
series: optional-series-name  # for multi-part series
---
```

### 3. Bilingual content structure

```markdown
<div class="lang-zh" markdown="1">

Chinese content here with full markdown support.

</div>

<div class="lang-en" markdown="1">

English content here with full markdown support.

</div>
```

**Critical rules:**
- Blank line AFTER opening `<div>` tag and BEFORE closing `</div>` tag (required for Jekyll markdown processing)
- Both divs must have parallel structure — same headings, same sections
- Series navigation links appear in BOTH divs (translated link text, identical URLs)
- References section appears in BOTH divs
- Tables, code blocks, blockquotes must be complete within each div

### 4. Series navigation pattern

```markdown
<!-- In lang-zh -->
**系列导航**：[一：标题](./) · [二：标题](url) · ...

<!-- In lang-en -->
**Series Navigation**: [I: Title](./) · [II: Title](url) · ...
```

### 5. Writing quality guidelines

- **Academic tone**: cite sources with `<sup>[N]</sup>`, include references section
- **Opening quote**: blockquote format, attributed with author
- **Structure**: clear numbered sections with `##` and `###`
- **Cross-references**: link between related posts using relative URLs
- **Code blocks**: preserve in both language divs unchanged
- **Tables**: fully translate headers and content in English div

## Bilingual Conversion

Convert an existing Chinese-only post to bilingual format:

### Step 1: Update frontmatter
Add `bilingual: true` and `title_en: "..."`. Keep all existing fields.

### Step 2: Wrap existing content
Wrap ALL existing Chinese content in `<div class="lang-zh" markdown="1">...</div>`.

### Step 3: Translate
Create `<div class="lang-en" markdown="1">...</div>` with full English translation.

### Translation rules:
- Academic, precise English register
- Chinese book titles: provide both original and translation — `《中国历代政治得失》(*China's Political Gains and Losses Through the Ages*)`
- Chinese names: romanized with characters on first use — `Qian Mu (钱穆)`
- Institution names: English + Chinese in parentheses — `Secretariat (中书省)`
- Quotes: translate with attribution noting original language
- References: Chinese refs get `[English translation]` added; English refs stay as-is
- ASCII diagrams: translate Chinese labels to English
- Keep all superscript ref numbers, links, formatting identical

## SVG Diagram Creation

### Theme colors (MUST use)

```
--bg:      #0d1117  (dark background)
--fg:      #c9d1d9  (foreground text)
--accent:  #6C63FF  (purple, primary accent)
--accent2: #58a6ff  (blue, secondary accent)
--muted:   #8b949e  (gray, labels)
--card:    #161b22  (dark card bg)
--border:  #21262d  (border lines)
--green:   #3fb950  (success/positive)
--orange:  #d29922  (warning/attention)
--red:     #f85149  (error/reject)
```

### SVG template

See [assets/svg-template.svg](assets/svg-template.svg) for base template.

### SVG requirements
- Width: 720px with `viewBox` for responsiveness
- Font: `sans-serif` (system fonts)
- Background: `#0d1117` or transparent
- No external dependencies (no Google Fonts, no CDN)
- English labels (works for both language versions)
- Clean, minimal, professional academic style

### Common diagram types

| Type | Use for | Key elements |
|------|---------|-------------|
| Flow diagram | Processes, pipelines | Boxes → arrows → boxes, feedback loops |
| Hierarchy | Org charts, module trees | Top-down boxes, varying line weights |
| Comparison | Before/after, mapping | Two columns with connecting arrows |
| Triangle/Tradeoff | Impossible triangles | Vertices + example positions inside |
| Timeline | Evolution, iterations | Horizontal nodes with annotations |
| Grid overview | Taxonomy, categories | NxM cells with icons/mini-diagrams |
| Hub-spoke | Theory bridges | Central hub with radiating connections |

### Insertion pattern

```markdown
![Alt text]({{ '/assets/images/filename.svg' | relative_url }})
```

Insert in BOTH `lang-zh` and `lang-en` divs at matching positions.

## Agent Team Patterns

### Parallel translation (N posts)

Launch N agents simultaneously, one per post:

```
Agent per post:
  - Read the post
  - Wrap Chinese in lang-zh div
  - Translate to English in lang-en div
  - Update frontmatter
  - Write the file
```

All agents run with `run_in_background: true` and `mode: bypassPermissions`.

### Parallel illustration (N posts)

Launch N agents simultaneously, one per post:

```
Agent per post:
  - Read the post
  - Identify 1-3 key diagrams needed
  - Create SVG files in assets/images/
  - Insert image references in both lang divs
  - Write all files
```

### Batch workflow (full pipeline)

For a new series of N posts:

```
Phase 1: Write all N posts in Chinese (N parallel agents)
Phase 2: Translate all to bilingual (N parallel agents)
Phase 3: Add diagrams to all (N parallel agents)
Phase 4: Single commit + push
```

### Agent prompt template

Each agent needs:
- File path
- Theme colors
- Bilingual structure rules
- Specific task (translate / illustrate / write)
- `mode: bypassPermissions` for file writes

## Homepage Auto-Update

The homepage (`index.html`) is **data-driven** — it automatically reflects new posts:

- **Series posts**: Any post with `series: civagent` (or other series name) appears in the series grid
- **Standalone essays**: Posts without a `series` field appear in the standalone section
- **All posts**: Every post appears in the chronological list

### When adding a new series

1. Add `series: series-name` to each post's frontmatter
2. Add a new series section to `index.html` following the CivAgent pattern:

```liquid
{% raw %}{% assign new_series = site.posts | where: "series", "new-series-name" | sort: "date" %}
{% if new_series.size > 0 %}
<section class="series-section">
  <h2 class="section-title">
    <span class="lang-zh">系列名称</span>
    <span class="lang-en">Series Name</span>
  </h2>
  ...
</section>
{% endif %}{% endraw %}
```

### Discipline tags

The homepage has color-coded discipline tags. To add new disciplines, add to `.discipline-tags` in `index.html` and define a color in `style.css`:

```css
.disc-tag[data-disc="newfield"] { border-color: #color; color: #color; }
```

Current disciplines: History (orange), Economics (green), Political Science (blue), Computer Science (purple), Organization Theory (lilac), Cognitive Psychology (red).

## Publishing Checklist

1. Verify all files exist: `ls _posts/YYYY-MM-DD-*.md`
2. Verify images: `ls assets/images/*.svg`
3. Check no broken image refs: `grep -r 'assets/images' _posts/ | grep -v '.svg'`
4. Verify series frontmatter: posts in a series must have `series: name`
5. Stage, commit, push: `git add _posts/ assets/images/ && git commit && git push origin main`
6. Verify deployment: check GitHub Pages build status
