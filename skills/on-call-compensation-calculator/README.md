# 🚀 On Call Compensation Calculator (MCP Server)

## 📖 Overview
This directory contains the **On Call Compensation Calculator** skill, an MCP server designed to Calculates payout for engineers based on off-hours pages.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `PAGERDUTY_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd on-call-compensation-calculator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "on-call-compensation-calculator": {
      "command": "/path/to/repo/skills/on-call-compensation-calculator/venv/bin/python",
      "args": ["/path/to/repo/skills/on-call-compensation-calculator/server.py"],
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
