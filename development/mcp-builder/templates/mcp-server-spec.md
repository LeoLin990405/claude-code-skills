# MCP Server Specification

> Fill in each section to define your MCP server. Remove sections that do not apply.

## Overview

| Field | Value |
|-------|-------|
| **Server Name** | `my-mcp-server` |
| **Description** | _What this server does in one sentence_ |
| **Language** | Python (FastMCP) / TypeScript (MCP SDK) |
| **Transport** | stdio / SSE / Streamable HTTP |
| **Auth** | None / API Key / OAuth 2.0 |

## Tools

Define each tool the server exposes.

### Tool: `tool_name`

| Field | Value |
|-------|-------|
| **Description** | _What this tool does_ |
| **Parameters** | See below |
| **Returns** | _Return type and structure_ |
| **Side Effects** | _None / Creates resource / Sends email / etc._ |
| **Error Cases** | _What can go wrong_ |

**Parameters:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `param1` | `string` | Yes | _Description_ |
| `param2` | `number` | No | _Description (default: 10)_ |

### Tool: `another_tool`

_Copy the block above for each additional tool._

## Resources

Define static or dynamic resources the server exposes.

### Resource: `resource://path/{id}`

| Field | Value |
|-------|-------|
| **URI Template** | `resource://server/items/{id}` |
| **Description** | _What this resource provides_ |
| **MIME Type** | `application/json` / `text/plain` |
| **Dynamic** | Yes / No |

## Prompts

Define reusable prompt templates the server exposes.

### Prompt: `prompt_name`

| Field | Value |
|-------|-------|
| **Description** | _What this prompt helps with_ |
| **Arguments** | See below |

**Arguments:**

| Name | Type | Required | Description |
|------|------|----------|-------------|
| `arg1` | `string` | Yes | _Description_ |

**Template:**

```
Given {arg1}, analyze the following...
```

## Authentication

| Field | Value |
|-------|-------|
| **Method** | None / API Key / OAuth 2.0 |
| **Key Location** | Environment variable: `MY_API_KEY` |
| **Scopes** | _OAuth scopes if applicable_ |
| **Rate Limits** | _Requests per minute / per day_ |

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| `fastmcp` | `>=2.0` | MCP server framework |
| `httpx` | `>=0.27` | HTTP client |

## Configuration

| Environment Variable | Required | Description |
|---------------------|----------|-------------|
| `MY_API_KEY` | Yes | API key for external service |
| `LOG_LEVEL` | No | Logging level (default: `INFO`) |

## Deployment

| Field | Value |
|-------|-------|
| **Install** | `pip install my-mcp-server` / `npm install my-mcp-server` |
| **Run** | `python -m my_server` / `npx my-mcp-server` |
| **Claude Config** | See below |

**claude_desktop_config.json / mcp-config.json:**

```json
{
  "mcpServers": {
    "my-mcp-server": {
      "command": "python",
      "args": ["-m", "my_server"],
      "env": {
        "MY_API_KEY": "..."
      }
    }
  }
}
```

## Testing Checklist

- [ ] Each tool returns expected output for valid input
- [ ] Each tool returns meaningful error for invalid input
- [ ] Resources resolve correctly with valid URIs
- [ ] Resources return 404 for invalid URIs
- [ ] Auth rejects unauthorized requests
- [ ] Server starts and responds to `initialize` handshake
- [ ] Server handles concurrent requests without state corruption
- [ ] Timeout and rate limit behavior verified
