# 🚀 Feature Adoption Tracker (MCP Server)

## 📖 Overview
This directory contains the **Feature Adoption Tracker** skill, an MCP server designed to Track post-launch feature usage in Mixpanel.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `MIXPANEL_SECRET`

---

## ⚙️ Installation & Setup

```bash
cd feature-adoption-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "feature-adoption-tracker": {
      "command": "/path/to/repo/skills/feature-adoption-tracker/venv/bin/python",
      "args": ["/path/to/repo/skills/feature-adoption-tracker/server.py"],
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
