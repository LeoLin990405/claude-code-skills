---
name: obsidian-cli
description: Interact with Obsidian vaults via the CLI (v1.12.6+). Search, read, create, manage files, tags, properties, tasks, plugins, and more. Use when the user wants to query or manipulate their Obsidian vault programmatically. Requires Obsidian app running with CLI enabled.
triggers:
  - obsidian cli
  - obsidian search
  - obsidian tags
  - obsidian properties
  - vault search
  - vault stats
  - backlinks
  - orphan notes
---

# Obsidian CLI Skill

Comprehensive reference for Obsidian's built-in CLI (80+ commands). Enables programmatic vault management, search, tag/property operations, link graph queries, and more.

## Prerequisites

- **Obsidian app must be running**: the CLI connects to the main process over IPC
- **CLI enabled**: `"cli": true` in `~/Library/Application Support/obsidian/obsidian.json`
- **Catalyst license** required
- **Always prefix commands with `timeout 5`** to avoid hanging:
  ```bash
  timeout 5 obsidian <command>
  ```
- **If you see "Unable to connect to main process"**:
  ```bash
  killall Obsidian && sleep 2 && open -a Obsidian && sleep 5
  ```

## Usage Pattern

```bash
timeout 5 obsidian <command> [params] [flags]
timeout 5 obsidian vault=<name> <command>
```

| Syntax | Description | Example |
|--------|-------------|---------|
| `key=value` | Parameter | `query="search term"` |
| `key="val spaces"` | Quoted parameter | `file="My Note"` |
| `flagname` | Boolean flag | `total`, `verbose`, `counts` |
| `file=<name>` | Target file (wikilink-style) | `file="Daily Note"` |
| `path=<exact>` | Target file (exact path) | `path="folder/note.md"` |
| `--copy` | Copy output to clipboard | `search query="x" --copy` |
| `\n` / `\t` | Newline / tab in content | `content="line1\nline2"` |

### Output Formats

| Context | Formats |
|---------|---------|
| Most list commands | `format=json\|tsv\|csv` |
| Search | `format=text\|json` |
| Outline | `format=tree\|md\|json` |
| Properties | `format=yaml\|json\|tsv` |
| Base query | `format=json\|csv\|tsv\|md\|paths` |

## Command Reference

### General

```bash
timeout 5 obsidian version
timeout 5 obsidian help
timeout 5 obsidian help search
timeout 5 obsidian reload
timeout 5 obsidian restart
```

### Files And Folders

| Command | Key Params | Description |
|---------|-----------|-------------|
| `file` | file/path | Show file info |
| `files` | folder, ext, `total` | List vault files |
| `folder` | path, info | Show folder info |
| `folders` | folder, `total` | List vault folders |
| `open` | file/path, `newtab` | Open a file in Obsidian GUI |
| `create` | name/path, content, template, `overwrite`, `open` | Create or overwrite file |
| `read` | file/path | Read file contents |
| `append` | file/path, content, `inline` | Append to file |
| `prepend` | file/path, content, `inline` | Prepend after frontmatter |
| `move` | file/path, to | Move or rename file |
| `rename` | file/path, name | Rename file and preserve ext |
| `delete` | file/path, `permanent` | Delete file |

```bash
timeout 5 obsidian files total
timeout 5 obsidian files folder="Udacity" ext=md
timeout 5 obsidian read file="My Note"
timeout 5 obsidian create name="New Note" content="# Title\n\nContent"
timeout 5 obsidian append file="Daily" content="\n- New item" inline
timeout 5 obsidian move file="Old Name" to="new-folder"
timeout 5 obsidian open file="My Note" newtab
```

### Daily Notes

```bash
timeout 5 obsidian daily
timeout 5 obsidian daily:path
timeout 5 obsidian daily:read
timeout 5 obsidian daily:append content="- Task done"
timeout 5 obsidian daily:prepend content="## Morning"
```

### Search

```bash
timeout 5 obsidian search query="keyword"
timeout 5 obsidian search query="keyword" path="folder"
timeout 5 obsidian search query="keyword" limit=5 total
timeout 5 obsidian search query="keyword" case
timeout 5 obsidian search:context query="keyword"
timeout 5 obsidian search:open query="keyword"
```

### Tags

```bash
timeout 5 obsidian tags total
timeout 5 obsidian tags total counts
timeout 5 obsidian tags file="My Note"
timeout 5 obsidian tag name="project" total
timeout 5 obsidian tag name="resume" verbose
```

### Tasks

```bash
timeout 5 obsidian tasks total
timeout 5 obsidian tasks todo
timeout 5 obsidian tasks done
timeout 5 obsidian tasks file="Project"
timeout 5 obsidian task file="Note" line=5 toggle
timeout 5 obsidian task file="Note" line=5 done
```

### Properties

```bash
timeout 5 obsidian properties total counts
timeout 5 obsidian properties file="My Note"
timeout 5 obsidian property:read name="status" file="Note"
timeout 5 obsidian property:set name="status" value="complete" file="Note"
timeout 5 obsidian property:set name="tags" value="tag1,tag2" type=list file="Note"
timeout 5 obsidian property:remove name="draft" file="Note"
timeout 5 obsidian aliases total
```

### Links

```bash
timeout 5 obsidian backlinks file="My Note"
timeout 5 obsidian backlinks file="My Note" total
timeout 5 obsidian links file="My Note" total
timeout 5 obsidian unresolved total
timeout 5 obsidian unresolved counts verbose
timeout 5 obsidian orphans total
timeout 5 obsidian deadends total
```

### Outline

```bash
timeout 5 obsidian outline file="My Note"
timeout 5 obsidian outline file="My Note" format=md
timeout 5 obsidian outline file="My Note" format=json
timeout 5 obsidian outline file="My Note" total
```

### Bookmarks

```bash
timeout 5 obsidian bookmarks
timeout 5 obsidian bookmarks total verbose
timeout 5 obsidian bookmark file="My Note" title="Fav"
```

### Templates

```bash
timeout 5 obsidian templates total
timeout 5 obsidian template:read name="daily" resolve title="Test"
timeout 5 obsidian template:insert name="daily"
```

### Bases

```bash
timeout 5 obsidian bases
timeout 5 obsidian base:query file="projects" format=json
timeout 5 obsidian base:query file="tasks" format=csv
timeout 5 obsidian base:create file="projects" name="New Item" content="..."
```

### Plugins

```bash
timeout 5 obsidian plugins
timeout 5 obsidian plugins filter=community versions
timeout 5 obsidian plugins:enabled
timeout 5 obsidian plugin id="dataview"
timeout 5 obsidian plugin:enable id="dataview"
timeout 5 obsidian plugin:disable id="dataview"
timeout 5 obsidian plugin:install id="dataview" enable
timeout 5 obsidian plugin:uninstall id="dataview"
```

### Themes And Snippets

```bash
timeout 5 obsidian themes
timeout 5 obsidian theme
timeout 5 obsidian theme:set name="Minimal"
timeout 5 obsidian snippets
timeout 5 obsidian snippet:enable name="custom"
```

### Command Palette And Hotkeys

```bash
timeout 5 obsidian commands
timeout 5 obsidian command id="editor:toggle-bold"
timeout 5 obsidian hotkeys total
timeout 5 obsidian hotkey id="editor:toggle-bold"
```

### Vault And Workspace

```bash
timeout 5 obsidian vault
timeout 5 obsidian vaults verbose
timeout 5 obsidian workspace
timeout 5 obsidian workspaces
timeout 5 obsidian workspace:save name="coding"
timeout 5 obsidian workspace:load name="coding"
timeout 5 obsidian tabs
timeout 5 obsidian recents total
```

### Sync And History

```bash
timeout 5 obsidian sync:status
timeout 5 obsidian sync off
timeout 5 obsidian sync on
timeout 5 obsidian sync:history file="Note" total
timeout 5 obsidian history file="Note"
timeout 5 obsidian history:restore file="Note" version=3
timeout 5 obsidian diff file="Note" from=1 to=3
```

### Other

```bash
timeout 5 obsidian random
timeout 5 obsidian random:read
timeout 5 obsidian wordcount file="Note"
timeout 5 obsidian web url="https://example.com"
```

### Developer

```bash
timeout 5 obsidian devtools
timeout 5 obsidian dev:errors
timeout 5 obsidian dev:screenshot path="/tmp/shot.png"
timeout 5 obsidian eval code="app.vault.getFiles().length"
```

## Common Workflows

### Vault Health Check

```bash
timeout 5 obsidian vault
timeout 5 obsidian unresolved total
timeout 5 obsidian orphans total
timeout 5 obsidian deadends total
```

### Tag-Based Queries

```bash
timeout 5 obsidian tags total counts
timeout 5 obsidian tag name="resume" verbose
timeout 5 obsidian search query="#project"
```

### Property Bulk Operations

```bash
timeout 5 obsidian property:read name="status" file="Project"
timeout 5 obsidian property:set name="status" value="complete" file="Project"
timeout 5 obsidian property:set name="tags" value="done,archived" type=list file="Project"
```

### Daily Note Workflow

```bash
timeout 5 obsidian daily:append content="\n## $(date +%H:%M) Update\n- Task completed"
timeout 5 obsidian daily:read
```

## CLI Vs Direct File Access

| Operation | Best Tool | Reason |
|-----------|-----------|--------|
| Create or edit notes | Direct file write | Faster, no timeout risk |
| Batch file ops | Direct file system | More reliable for bulk |
| Search content | CLI `search` or grep | CLI uses Obsidian's index |
| Tag queries | CLI `tags` or `tag` | Only CLI has tag index |
| Property CRUD | CLI `property:*` | Atomic, no parse errors |
| Backlinks or orphans | CLI `backlinks` or `orphans` | Only CLI has link graph |
| Open in GUI | CLI `open` | Opens specific file |
| Plugin management | CLI `plugin:*` | Only way from terminal |

## Troubleshooting

| Issue | Fix |
|-------|-----|
| `Unable to connect to main process` | `killall Obsidian && sleep 2 && open -a Obsidian && sleep 5` |
| CLI hangs | Always use `timeout 5` prefix |
| Wrong vault | Use `vault=<name>` as first param |
| Command not found | Check `obsidian help` for latest commands |
| Empty output | Some commands return empty on success; check with `total` flag |
