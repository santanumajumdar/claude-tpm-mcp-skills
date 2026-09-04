# 🚀 Toil Quantifier (MCP Server)

## 📖 Overview
This directory contains the **Toil Quantifier** skill, an MCP server designed to Measure engineering time spent on manual ops/support tasks.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd toil-quantifier
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "toil-quantifier": {
      "command": "/path/to/repo/skills/toil-quantifier/venv/bin/python",
      "args": ["/path/to/repo/skills/toil-quantifier/server.py"],
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
