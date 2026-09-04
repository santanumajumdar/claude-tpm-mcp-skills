# 🤖 Skill Discovery MCP Server (Agent-First Catalog)

This is a meta-MCP server built using the **AAS Core methodology**. 

Instead of humans manually browsing the `/claude-native-skills/` directory, you can attach this MCP server to Claude. **Claude will then be able to autonomously search the catalog of 400+ skills**, dynamically loading new capabilities, personas, and workflows into its own context as needed.

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "skill-discovery": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/TO/skills/skill-discovery-server/server.py"]
    }
  }
}
```
