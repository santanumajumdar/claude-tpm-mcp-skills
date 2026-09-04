# 🚀 Onboarding Checklist Generator (MCP Server)

## 📖 Overview
This directory contains the **Onboarding Checklist Generator** skill, an MCP server designed to Customize engineering onboarding plans based on team and role.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `CONFLUENCE_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd onboarding-checklist-generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "onboarding-checklist-generator": {
      "command": "/path/to/repo/skills/onboarding-checklist-generator/venv/bin/python",
      "args": ["/path/to/repo/skills/onboarding-checklist-generator/server.py"],
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
