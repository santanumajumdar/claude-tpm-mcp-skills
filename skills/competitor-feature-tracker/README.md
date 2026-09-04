# 🚀 Competitor Feature Tracker (MCP Server)

## 📖 Overview
This directory contains the **Competitor Feature Tracker** skill, an MCP server designed to Scrapes competitor release notes and alerts PMs/TPMs.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `OPENAI_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd competitor-feature-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "competitor-feature-tracker": {
      "command": "/path/to/repo/skills/competitor-feature-tracker/venv/bin/python",
      "args": ["/path/to/repo/skills/competitor-feature-tracker/server.py"],
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
