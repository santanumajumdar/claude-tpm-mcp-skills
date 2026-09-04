# 🚀 Third Party Api Downtime Tracker (MCP Server)

## 📖 Overview
This directory contains the **Third Party Api Downtime Tracker** skill, an MCP server designed to Correlates internal errors with external API status pages (e.g. Stripe, Twilio).

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `DATADOG_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd third-party-api-downtime-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "third-party-api-downtime-tracker": {
      "command": "/path/to/repo/skills/third-party-api-downtime-tracker/venv/bin/python",
      "args": ["/path/to/repo/skills/third-party-api-downtime-tracker/server.py"],
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
