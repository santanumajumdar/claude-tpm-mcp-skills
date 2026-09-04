# 🚀 Accessibility Compliance Bot (MCP Server)

## 📖 Overview
This directory contains the **Accessibility Compliance Bot** skill, an MCP server designed to Connects to Lighthouse/axe to generate WCAG compliance tickets.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd accessibility-compliance-bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "accessibility-compliance-bot": {
      "command": "/path/to/repo/skills/accessibility-compliance-bot/venv/bin/python",
      "args": ["/path/to/repo/skills/accessibility-compliance-bot/server.py"],
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
