# 🚀 Pr Size Enforcer (MCP Server)

## 📖 Overview
This directory contains the **Pr Size Enforcer** skill, an MCP server designed to Warns developers in Slack if a PR exceeds 500 lines of code.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`\n- `SLACK_BOT_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd pr-size-enforcer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "pr-size-enforcer": {
      "command": "/path/to/repo/skills/pr-size-enforcer/venv/bin/python",
      "args": ["/path/to/repo/skills/pr-size-enforcer/server.py"],
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
