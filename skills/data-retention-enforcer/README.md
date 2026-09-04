# 🚀 Data Retention Enforcer (MCP Server)

## 📖 Overview
This directory contains the **Data Retention Enforcer** skill, an MCP server designed to Identifies databases lacking automated deletion scripts for GDPR.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `AWS_ACCESS_KEY_ID`

---

## ⚙️ Installation & Setup

```bash
cd data-retention-enforcer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "data-retention-enforcer": {
      "command": "/path/to/repo/skills/data-retention-enforcer/venv/bin/python",
      "args": ["/path/to/repo/skills/data-retention-enforcer/server.py"],
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
