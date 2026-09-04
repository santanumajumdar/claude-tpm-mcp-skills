# 🚀 Backlog Staleness Purger (MCP Server)

## 📖 Overview
This directory contains the **Backlog Staleness Purger** skill, an MCP server designed to Auto-closes Jira tickets older than 1 year with no updates.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd backlog-staleness-purger
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "backlog-staleness-purger": {
      "command": "/path/to/repo/skills/backlog-staleness-purger/venv/bin/python",
      "args": ["/path/to/repo/skills/backlog-staleness-purger/server.py"],
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
