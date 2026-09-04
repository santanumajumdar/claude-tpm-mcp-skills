# 🚀 Capacity Limit Forecaster (MCP Server)

## 📖 Overview
This directory contains the **Capacity Limit Forecaster** skill, an MCP server designed to Predict when database or storage limits will be hit.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `DATADOG_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd capacity-limit-forecaster
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "capacity-limit-forecaster": {
      "command": "/path/to/repo/skills/capacity-limit-forecaster/venv/bin/python",
      "args": ["/path/to/repo/skills/capacity-limit-forecaster/server.py"],
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
