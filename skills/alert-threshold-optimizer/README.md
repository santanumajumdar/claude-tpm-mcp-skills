# 🚀 Alert Threshold Optimizer (MCP Server)

## 📖 Overview
This directory contains the **Alert Threshold Optimizer** skill, an MCP server designed to Suggest adjustments to noisy Datadog alerts.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `DATADOG_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd alert-threshold-optimizer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "alert-threshold-optimizer": {
      "command": "/path/to/repo/skills/alert-threshold-optimizer/venv/bin/python",
      "args": ["/path/to/repo/skills/alert-threshold-optimizer/server.py"],
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
