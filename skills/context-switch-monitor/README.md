# 🚀 Context Switch Monitor (MCP Server)

## 📖 Overview
This directory contains the **Context Switch Monitor** skill, an MCP server designed to Alert if engineers are assigned to too many distinct epics concurrently.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd context-switch-monitor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "context-switch-monitor": {
      "command": "/path/to/repo/skills/context-switch-monitor/venv/bin/python",
      "args": ["/path/to/repo/skills/context-switch-monitor/server.py"],
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
