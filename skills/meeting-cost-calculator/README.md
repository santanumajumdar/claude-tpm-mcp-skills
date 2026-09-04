# 🚀 Meeting Cost Calculator (MCP Server)

## 📖 Overview
This directory contains the **Meeting Cost Calculator** skill, an MCP server designed to Calculate the dollar cost of engineering meetings to discourage over-inviting.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GOOGLE_CALENDAR_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd meeting-cost-calculator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "meeting-cost-calculator": {
      "command": "/path/to/repo/skills/meeting-cost-calculator/venv/bin/python",
      "args": ["/path/to/repo/skills/meeting-cost-calculator/server.py"],
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
