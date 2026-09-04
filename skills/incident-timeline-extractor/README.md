# 🚀 Incident Timeline Extractor (MCP Server)

## 📖 Overview
This directory contains the **Incident Timeline Extractor** skill, an MCP server designed to Build precise incident timelines from Slack and PagerDuty.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `SLACK_BOT_TOKEN`\n- `PAGERDUTY_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd incident-timeline-extractor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "incident-timeline-extractor": {
      "command": "/path/to/repo/skills/incident-timeline-extractor/venv/bin/python",
      "args": ["/path/to/repo/skills/incident-timeline-extractor/server.py"],
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
