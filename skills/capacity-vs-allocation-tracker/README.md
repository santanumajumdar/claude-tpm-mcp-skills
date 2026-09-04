# 🚀 Capacity Vs Allocation Tracker (MCP Server)

## 📖 Overview
This directory contains the **Capacity Vs Allocation Tracker** skill, an MCP server designed to Compares planned sprint capacity vs actual hours logged.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd capacity-vs-allocation-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "capacity-vs-allocation-tracker": {
      "command": "/path/to/repo/skills/capacity-vs-allocation-tracker/venv/bin/python",
      "args": ["/path/to/repo/skills/capacity-vs-allocation-tracker/server.py"],
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
