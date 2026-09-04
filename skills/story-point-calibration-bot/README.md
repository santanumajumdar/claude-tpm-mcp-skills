# 🚀 Story Point Calibration Bot (MCP Server)

## 📖 Overview
This directory contains the **Story Point Calibration Bot** skill, an MCP server designed to Identifies teams whose 5-point stories take wildly different times.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd story-point-calibration-bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "story-point-calibration-bot": {
      "command": "/path/to/repo/skills/story-point-calibration-bot/venv/bin/python",
      "args": ["/path/to/repo/skills/story-point-calibration-bot/server.py"],
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
