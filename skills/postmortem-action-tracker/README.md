# 🚀 Postmortem Action Tracker (MCP Server)

## 📖 Overview
This directory contains the **Postmortem Action Tracker** skill, an MCP server designed to Ensure postmortem action items are prioritized in upcoming sprints.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`\n- `CONFLUENCE_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd postmortem-action-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "postmortem-action-tracker": {
      "command": "/path/to/repo/skills/postmortem-action-tracker/venv/bin/python",
      "args": ["/path/to/repo/skills/postmortem-action-tracker/server.py"],
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
