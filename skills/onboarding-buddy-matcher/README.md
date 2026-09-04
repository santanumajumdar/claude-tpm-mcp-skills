# 🚀 Onboarding Buddy Matcher (MCP Server)

## 📖 Overview
This directory contains the **Onboarding Buddy Matcher** skill, an MCP server designed to Matches new hires with veterans based on shared interests or timezones.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `BAMBOOHR_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd onboarding-buddy-matcher
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "onboarding-buddy-matcher": {
      "command": "/path/to/repo/skills/onboarding-buddy-matcher/venv/bin/python",
      "args": ["/path/to/repo/skills/onboarding-buddy-matcher/server.py"],
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
