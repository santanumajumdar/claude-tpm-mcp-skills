# 🐘 PostgreSQL Secure Client (MCP)

This MCP server provides a strictly read-only (`SELECT`) database client, allowing Claude to query live production metrics without risking your schema.

## 🚀 Installation

1. Navigate to this directory and install dependencies:
```bash
cd skills/postgres-database-server
pip install -r requirements.txt
```

2. Add to your `claude_desktop_config.json`. You must provide a valid `DATABASE_URL` environment variable:
```json
{
  "mcpServers": {
    "postgres-client": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/TO/skills/postgres-database-server/server.py"],
      "env": {
        "DATABASE_URL": "postgresql://user:password@localhost:5432/mydb"
      }
    }
  }
}
```

3. Restart Claude Desktop. Claude can now execute `query_database`!
