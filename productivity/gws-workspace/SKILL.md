---
name: gws-workspace
description: Google Workspace CLI - manage Drive, Gmail, Sheets, Calendar, Docs, Slides, Tasks, and more via gws command
triggers:
  - google workspace
  - google drive
  - gmail
  - google sheets
  - google calendar
  - google docs
  - google slides
  - google tasks
  - google keep
  - gws
  - drive files
  - spreadsheet
  - send email
---

# Google Workspace CLI (gws)

Use the `gws` CLI tool to interact with Google Workspace services. The tool is installed at `/Users/leo/.npm-global/bin/gws` and authenticated with `zhongyuelin990405@gmail.com`.

## Command Pattern

```bash
gws <service> <resource> [sub-resource] <method> [flags]
```

## Available Services

| Service | Description |
|---------|-------------|
| `drive` | Files, folders, shared drives |
| `gmail` | Send, read, manage email |
| `sheets` | Read/write spreadsheets |
| `calendar` | Calendars and events |
| `docs` | Read/write Google Docs |
| `slides` | Read/write presentations |
| `tasks` | Task lists and tasks |
| `people` | Contacts and profiles |
| `chat` | Chat spaces and messages |
| `forms` | Google Forms |
| `keep` | Google Keep notes |
| `meet` | Google Meet conferences |

## Key Flags

| Flag | Description |
|------|-------------|
| `--params '<JSON>'` | URL/query parameters as JSON |
| `--json '<JSON>'` | Request body as JSON (POST/PATCH/PUT) |
| `--upload <PATH>` | File to upload (multipart) |
| `--output <PATH>` | Output file for binary responses |
| `--format <FMT>` | Output: json (default), table, yaml, csv |
| `--page-all` | Auto-paginate (NDJSON output) |
| `--page-limit <N>` | Max pages (default: 10) |

## Schema Discovery

Use `gws schema` to discover API methods and their parameters:

```bash
# List available methods for a service
gws schema drive.files.list
gws schema gmail.users.messages.send

# Show full schema with resolved references
gws schema sheets.spreadsheets.get --resolve-refs
```

## Common Examples

### Drive
```bash
# List files
gws drive files list --params '{"pageSize": 10}'

# Search files
gws drive files list --params '{"q": "name contains '\''report'\''", "pageSize": 5}'

# Get file metadata
gws drive files get --params '{"fileId": "FILE_ID"}'

# Download file
gws drive files get --params '{"fileId": "FILE_ID", "alt": "media"}' --output ./file.pdf

# Upload file
gws drive files create --json '{"name": "test.txt", "mimeType": "text/plain"}' --upload ./test.txt

# Delete file
gws drive files delete --params '{"fileId": "FILE_ID"}'
```

### Gmail
```bash
# List messages
gws gmail users messages list --params '{"userId": "me", "maxResults": 5}'

# Read a message
gws gmail users messages get --params '{"userId": "me", "id": "MSG_ID"}'

# Send email (base64url encoded)
gws gmail users messages send --params '{"userId": "me"}' --json '{"raw": "BASE64_ENCODED_EMAIL"}'

# List labels
gws gmail users labels list --params '{"userId": "me"}'
```

### Sheets
```bash
# Read spreadsheet
gws sheets spreadsheets get --params '{"spreadsheetId": "SHEET_ID"}'

# Read values
gws sheets spreadsheets values get --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A1:D10"}'

# Write values
gws sheets spreadsheets values update --params '{"spreadsheetId": "SHEET_ID", "range": "Sheet1!A1", "valueInputOption": "USER_ENTERED"}' --json '{"values": [["Hello", "World"]]}'
```

### Calendar
```bash
# List calendars
gws calendar calendarList list

# List events
gws calendar events list --params '{"calendarId": "primary", "maxResults": 10, "timeMin": "2026-03-01T00:00:00Z"}'

# Create event
gws calendar events insert --params '{"calendarId": "primary"}' --json '{"summary": "Meeting", "start": {"dateTime": "2026-03-10T10:00:00+08:00"}, "end": {"dateTime": "2026-03-10T11:00:00+08:00"}}'
```

### Tasks
```bash
# List task lists
gws tasks tasklists list

# List tasks
gws tasks tasks list --params '{"tasklist": "TASKLIST_ID"}'

# Create task
gws tasks tasks insert --params '{"tasklist": "TASKLIST_ID"}' --json '{"title": "New task"}'
```

### Docs
```bash
# Get document
gws docs documents get --params '{"documentId": "DOC_ID"}'
```

## Important Notes

- Gmail userId is always `"me"` for the authenticated user
- Path parameters go in `--params`, request body in `--json`
- Use `gws schema <service.resource.method>` when unsure about parameters
- Binary downloads require `--output` flag
- For email sending, the `raw` field must be base64url-encoded RFC 2822 message
