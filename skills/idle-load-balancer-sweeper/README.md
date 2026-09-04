# 🚀 Idle Load Balancer Sweeper (MCP Server)

## 📖 Overview
This directory contains the **Idle Load Balancer Sweeper** skill, an MCP server designed to Finds and removes unused ALBs/ELBs.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `AWS_ACCESS_KEY_ID`

---

## ⚙️ Installation & Setup

```bash
cd idle-load-balancer-sweeper
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "idle-load-balancer-sweeper": {
      "command": "/path/to/repo/skills/idle-load-balancer-sweeper/venv/bin/python",
      "args": ["/path/to/repo/skills/idle-load-balancer-sweeper/server.py"],
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
