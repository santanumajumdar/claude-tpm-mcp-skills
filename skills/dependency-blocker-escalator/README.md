# 🚀 Dependency Blocker Escalator (MCP Server)

## 📖 Overview
This directory contains the **Dependency Blocker Escalator** skill, an MCP server designed to Escalate aging cross-squad blockers automatically.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`\n- `SLACK_BOT_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd dependency-blocker-escalator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "dependency-blocker-escalator": {
      "command": "/path/to/repo/skills/dependency-blocker-escalator/venv/bin/python",
      "args": ["/path/to/repo/skills/dependency-blocker-escalator/server.py"],
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
