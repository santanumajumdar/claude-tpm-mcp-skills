# 🚀 Sprint Spillover Forecaster (MCP Server)

## 📖 Overview
This directory contains the **Sprint Spillover Forecaster** skill, an MCP server designed to Predict which tickets will spill over based on historical patterns.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd sprint-spillover-forecaster
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "sprint-spillover-forecaster": {
      "command": "/path/to/repo/skills/sprint-spillover-forecaster/venv/bin/python",
      "args": ["/path/to/repo/skills/sprint-spillover-forecaster/server.py"],
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
