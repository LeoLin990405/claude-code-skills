# Blog Architecture Reference

## Repository Structure

```
blog-repo/
├── _config.yml          # Jekyll config (lang: zh-CN, permalink: /:year/:month/:day/:title/)
├── _layouts/
│   ├── default.html     # Base layout with nav, footer, global lang script
│   └── post.html        # Post layout with bilingual toggle button
├── _posts/              # Blog posts (YYYY-MM-DD-slug.md)
├── assets/
│   ├── css/style.css    # Dark theme stylesheet
│   └── images/          # SVG diagrams
├── index.html           # Post list page
├── categories.html      # Category index
└── tags.html            # Tag index
```

## Theme Colors

```css
:root {
  --bg: #0d1117;       /* Page background */
  --fg: #c9d1d9;       /* Main text */
  --accent: #6C63FF;   /* Purple - primary accent, links, highlights */
  --accent2: #58a6ff;  /* Blue - secondary accent, nav links */
  --muted: #8b949e;    /* Gray - dates, metadata, captions */
  --border: #21262d;   /* Borders, separators */
  --card: #161b22;     /* Card/code block background */
}
```

## Bilingual System

### How it works

1. **`default.html`** runs a script on page load that reads `localStorage('preferred-lang')` and sets `data-lang` attribute on `<html>`
2. **`style.css`** uses CSS attribute selectors to show/hide content:
   - `[data-lang="zh"] .lang-en { display: none !important; }`
   - `[data-lang="en"] .lang-zh { display: none !important; }`
3. **`post.html`** shows a toggle button when `page.bilingual` is true
4. **Toggle button** calls `toggleLang()` which flips between `zh` and `en`, saves to localStorage

### Frontmatter fields

| Field | Required | Purpose |
|-------|----------|---------|
| `layout: post` | Yes | Use post layout |
| `title` | Yes | Chinese title (shown in lang-zh) |
| `title_en` | For bilingual | English title (shown in lang-en) |
| `bilingual` | For bilingual | Set to `true` to show toggle button |
| `date` | Yes | Post date (YYYY-MM-DD) |
| `tags` | Recommended | Array of tags |
| `categories` | Recommended | Array of categories |
| `series` | Optional | Series identifier for multi-part posts |

### Content div structure

```html
<div class="lang-zh" markdown="1">
<!-- blank line required here -->
Chinese markdown content...
<!-- blank line required here -->
</div>

<div class="lang-en" markdown="1">
<!-- blank line required here -->
English markdown content...
<!-- blank line required here -->
</div>
```

**Critical**: The blank lines after `<div>` and before `</div>` are mandatory for Jekyll's Kramdown to process the markdown inside HTML blocks.

## CSS Classes Reference

| Class | Element | Purpose |
|-------|---------|---------|
| `.post-title` | `<h1>` | Post title |
| `.post-date` | `<time>` | Date display |
| `.post-tags` | `<div>` | Tag container |
| `.tag` | `<span>` | Individual tag pill |
| `.post-content` | `<div>` | Main content area |
| `.post-nav` | `<div>` | Bottom navigation |
| `.lang-toggle` | `<button>` | Language switch button |
| `.lang-zh` | `<span>/<div>` | Chinese content |
| `.lang-en` | `<span>/<div>` | English content |
| `.post-header-row` | `<div>` | Flex row for title + toggle |
| `.category-label` | `<span>` | Category badge |

## Navigation

Header nav links:
- Home (`/`)
- Categories (`/categories`)
- Tags (`/tags`)
- GitHub (external)
- LinkedIn (external)

Post bottom nav:
- "返回文章列表" / "Back to all posts" (bilingual)

## Permalink Format

```
/:year/:month/:day/:title/
```

Example: `/2026/03/11/civagent-1-history-as-design-patterns/`

When linking between posts, use the full path:
```markdown
[Link text](/blog/2026/03/11/civagent-1-history-as-design-patterns/)
```
