# 🚀 Go To Market Sync (MCP Server)

## 📖 Overview
This directory contains the **Go To Market Sync** skill, an MCP server designed to Generate technical briefs for Sales/Support teams.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`\n- `CONFLUENCE_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd go-to-market-sync
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "go-to-market-sync": {
      "command": "/path/to/repo/skills/go-to-market-sync/venv/bin/python",
      "args": ["/path/to/repo/skills/go-to-market-sync/server.py"],
      "env": {
        // API Keys
      }
    }
  }
}
```

## 🎮 How to Use
1. Copy the contents of `prompt.md`.
2. Paste into Claude.
3. Command Claude to execute the workflow.
