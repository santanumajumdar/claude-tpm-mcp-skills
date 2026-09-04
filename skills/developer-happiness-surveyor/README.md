# 🚀 Developer Happiness Surveyor (MCP Server)

## 📖 Overview
This directory contains the **Developer Happiness Surveyor** skill, an MCP server designed to Sends micro-surveys in Slack and aggregates sentiment.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `SLACK_BOT_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd developer-happiness-surveyor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "developer-happiness-surveyor": {
      "command": "/path/to/repo/skills/developer-happiness-surveyor/venv/bin/python",
      "args": ["/path/to/repo/skills/developer-happiness-surveyor/server.py"],
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
