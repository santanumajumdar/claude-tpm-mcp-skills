# 🚀 Kudos Aggregator (MCP Server)

## 📖 Overview
This directory contains the **Kudos Aggregator** skill, an MCP server designed to Collects 'thank yous' across Slack channels into a weekly digest.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `SLACK_BOT_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd kudos-aggregator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "kudos-aggregator": {
      "command": "/path/to/repo/skills/kudos-aggregator/venv/bin/python",
      "args": ["/path/to/repo/skills/kudos-aggregator/server.py"],
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
