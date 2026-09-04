# 🚀 Standup Blocker Summarizer (MCP Server)

## 📖 Overview
This directory contains the **Standup Blocker Summarizer** skill, an MCP server designed to Extract blockers from daily async standups in Slack.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `SLACK_BOT_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd standup-blocker-summarizer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "standup-blocker-summarizer": {
      "command": "/path/to/repo/skills/standup-blocker-summarizer/venv/bin/python",
      "args": ["/path/to/repo/skills/standup-blocker-summarizer/server.py"],
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
