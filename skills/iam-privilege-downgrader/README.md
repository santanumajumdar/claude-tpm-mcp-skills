# 🚀 Iam Privilege Downgrader (MCP Server)

## 📖 Overview
This directory contains the **Iam Privilege Downgrader** skill, an MCP server designed to Analyzes IAM roles and suggests downgrades based on last 90 days usage.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `AWS_ACCESS_KEY_ID`

---

## ⚙️ Installation & Setup

```bash
cd iam-privilege-downgrader
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "iam-privilege-downgrader": {
      "command": "/path/to/repo/skills/iam-privilege-downgrader/venv/bin/python",
      "args": ["/path/to/repo/skills/iam-privilege-downgrader/server.py"],
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
