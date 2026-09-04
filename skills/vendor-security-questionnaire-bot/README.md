# 🚀 Vendor Security Questionnaire Bot (MCP Server)

## 📖 Overview
This directory contains the **Vendor Security Questionnaire Bot** skill, an MCP server designed to Auto-drafts answers to vendor security questionnaires based on past responses.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `OPENAI_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd vendor-security-questionnaire-bot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "vendor-security-questionnaire-bot": {
      "command": "/path/to/repo/skills/vendor-security-questionnaire-bot/venv/bin/python",
      "args": ["/path/to/repo/skills/vendor-security-questionnaire-bot/server.py"],
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
