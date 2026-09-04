# 🚀 Interview Load Balancer (MCP Server)

## 📖 Overview
This directory contains the **Interview Load Balancer** skill, an MCP server designed to Ensures no engineer does more than 3 interviews per week.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GREENHOUSE_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd interview-load-balancer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "interview-load-balancer": {
      "command": "/path/to/repo/skills/interview-load-balancer/venv/bin/python",
      "args": ["/path/to/repo/skills/interview-load-balancer/server.py"],
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
