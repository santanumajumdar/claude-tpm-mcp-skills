# 🚀 Stakeholder Update Generator (MCP Server)

## 📖 Overview
This directory contains the **Stakeholder Update Generator** skill, an MCP server designed to Draft status updates tailored to specific C-suite personas.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd stakeholder-update-generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "stakeholder-update-generator": {
      "command": "/path/to/repo/skills/stakeholder-update-generator/venv/bin/python",
      "args": ["/path/to/repo/skills/stakeholder-update-generator/server.py"],
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
