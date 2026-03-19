#!/usr/bin/env python3
"""
Doris Data Warehouse Read-Only Query Tool

Safety constraints:
  - Only SELECT / SHOW / DESCRIBE / EXPLAIN allowed
  - 60-second query timeout
  - No DDL / DML / admin operations
  - Result set capped at 10000 rows
"""

import argparse
import json
import re
import sys
import time

import pymysql

# ── Connection Config ────────────────────────────────────────────────
DB_CONNECTIONS = {
    "db1": {
        "alias": ["db1", "111", "111.231.70.22"],
        "host": "111.231.70.22",
        "port": 9030,
        "user": "linzhongyue",
        "password": "lin#$ZHONG90+.!Yue",
    },
    "db2": {
        "alias": ["db2", "117", "1.117.17.157"],
        "host": "1.117.17.157",
        "port": 9030,
        "user": "linzhongyue",
        "password": "LZY#20@25@!!08+26+lzy",
    },
}

DEFAULT_DB = "db1"

COMMON_CONFIG = {
    "connect_timeout": 10,
    "read_timeout": 60,
    "write_timeout": 10,
    "charset": "utf8mb4",
}


def resolve_connection(name: str) -> dict:
    """Resolve a connection name/alias to a config dict."""
    name = name.strip().lower()
    for key, cfg in DB_CONNECTIONS.items():
        if name == key or name in cfg["alias"]:
            return {
                "host": cfg["host"],
                "port": cfg["port"],
                "user": cfg["user"],
                "password": cfg["password"],
                **COMMON_CONFIG,
            }
    available = ", ".join(
        f'{k} ({c["host"]})' for k, c in DB_CONNECTIONS.items()
    )
    print(f"❌ Unknown connection: '{name}'. Available: {available}", file=sys.stderr)
    sys.exit(1)

MAX_ROWS = 10000
QUERY_TIMEOUT = 60  # seconds

# ── SQL Safety ───────────────────────────────────────────────────────
ALLOWED_PREFIXES = ("select", "show", "describe", "desc", "explain")

FORBIDDEN_KEYWORDS = [
    "insert", "update", "delete", "replace", "merge",
    "create", "drop", "alter", "truncate", "rename",
    "grant", "revoke", "kill",
    "load", "import", "export",
    "admin", "recover", "backup", "restore",
]


def validate_sql(sql: str) -> tuple[bool, str]:
    """Validate that the SQL is a safe read-only query."""
    cleaned = sql.strip().rstrip(";").strip()
    if not cleaned:
        return False, "Empty query"

    # Remove leading comments
    stripped = re.sub(r"^(/\*.*?\*/\s*|--[^\n]*\n\s*)*", "", cleaned, flags=re.DOTALL).strip()
    lower = stripped.lower()

    # Must start with allowed prefix
    if not any(lower.startswith(p) for p in ALLOWED_PREFIXES):
        return False, f"Only {', '.join(w.upper() for w in ALLOWED_PREFIXES)} queries are allowed"

    # Check for forbidden keywords (word boundary match)
    for kw in FORBIDDEN_KEYWORDS:
        if re.search(rf"\b{kw}\b", lower):
            return False, f"Forbidden keyword detected: {kw.upper()}"

    # Block multiple statements (semicolon in the middle)
    # Allow semicolons inside string literals by rough check
    without_strings = re.sub(r"'[^']*'", "", cleaned)
    without_strings = re.sub(r'"[^"]*"', "", without_strings)
    if ";" in without_strings.rstrip(";"):
        return False, "Multiple statements are not allowed"

    return True, "OK"


# ── Formatting ───────────────────────────────────────────────────────
def format_table(columns: list[str], rows: list[tuple]) -> str:
    """Format results as an aligned text table."""
    if not rows:
        return "(0 rows returned)"

    str_rows = [[str(v) if v is not None else "NULL" for v in row] for row in rows]
    widths = [max(len(c), max((len(r[i]) for r in str_rows), default=0)) for i, c in enumerate(columns)]

    header = " | ".join(c.ljust(w) for c, w in zip(columns, widths))
    sep = "-+-".join("-" * w for w in widths)
    body = "\n".join(" | ".join(v.ljust(w) for v, w in zip(r, widths)) for r in str_rows)

    return f"{header}\n{sep}\n{body}"


def format_csv(columns: list[str], rows: list[tuple]) -> str:
    """Format results as CSV."""
    def escape(v):
        s = str(v) if v is not None else ""
        if "," in s or '"' in s or "\n" in s:
            return '"' + s.replace('"', '""') + '"'
        return s

    lines = [",".join(columns)]
    for row in rows:
        lines.append(",".join(escape(v) for v in row))
    return "\n".join(lines)


def format_json(columns: list[str], rows: list[tuple]) -> str:
    """Format results as JSON array."""
    result = []
    for row in rows:
        result.append({col: (val if val is not None else None) for col, val in zip(columns, row)})
    return json.dumps(result, ensure_ascii=False, indent=2, default=str)


FORMATTERS = {
    "table": format_table,
    "csv": format_csv,
    "json": format_json,
}


# ── Main ─────────────────────────────────────────────────────────────
def run_query(sql: str, fmt: str = "table", db: str = DEFAULT_DB) -> None:
    # 1. Validate
    ok, msg = validate_sql(sql)
    if not ok:
        print(f"❌ BLOCKED: {msg}", file=sys.stderr)
        sys.exit(1)

    # 2. Connect & execute
    db_config = resolve_connection(db)
    conn = None
    try:
        conn = pymysql.connect(**db_config)
        print(f"[{db_config['host']}:{db_config['port']}]")
        cursor = conn.cursor()

        # Set session query timeout
        try:
            cursor.execute(f"SET query_timeout = {QUERY_TIMEOUT * 1000}")
        except Exception:
            pass  # Not all Doris versions support this

        start = time.time()
        cursor.execute(sql)
        elapsed = time.time() - start

        # 3. Fetch results
        if cursor.description:
            columns = [desc[0] for desc in cursor.description]
            rows = cursor.fetchmany(MAX_ROWS)
            total = len(rows)

            # Check if more rows exist
            extra = cursor.fetchone()
            truncated = extra is not None

            formatter = FORMATTERS.get(fmt, format_table)
            print(formatter(columns, rows))

            # Footer
            info = f"\n({total} row{'s' if total != 1 else ''}"
            if truncated:
                info += f", truncated at {MAX_ROWS}"
            info += f", {elapsed:.2f}s)"
            print(info)
        else:
            print(f"(Query executed, {elapsed:.2f}s)")

    except pymysql.err.OperationalError as e:
        code, msg = e.args if len(e.args) == 2 else (0, str(e))
        if "timeout" in str(msg).lower() or code == 1969:
            print(f"❌ TIMEOUT: Query exceeded {QUERY_TIMEOUT}s limit", file=sys.stderr)
        else:
            print(f"❌ ERROR: {msg}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ ERROR: {e}", file=sys.stderr)
        sys.exit(1)
    finally:
        if conn:
            conn.close()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Doris read-only query tool")
    parser.add_argument("sql", help="SQL query to execute")
    parser.add_argument("--db", "-d", default=DEFAULT_DB, help="Connection name: db1 (111.231.70.22) or db2 (1.117.17.157). Default: db1")
    parser.add_argument("--format", "-f", choices=["table", "csv", "json"], default="table", help="Output format (default: table)")
    args = parser.parse_args()

    run_query(args.sql, args.format, args.db)
