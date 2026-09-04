# 🚀 Deprecated Api Tracker (MCP Server)

## 📖 Overview
This directory contains the **Deprecated Api Tracker** skill, an MCP server designed to Find usages of sunset APIs and create migration tickets.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`\n- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd deprecated-api-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "deprecated-api-tracker": {
      "command": "/path/to/repo/skills/deprecated-api-tracker/venv/bin/python",
      "args": ["/path/to/repo/skills/deprecated-api-tracker/server.py"],
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
