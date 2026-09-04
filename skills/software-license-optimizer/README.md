# 🚀 Software License Optimizer (MCP Server)

## 📖 Overview
This directory contains the **Software License Optimizer** skill, an MCP server designed to Find unused SaaS licenses to cut costs.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `OKTA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd software-license-optimizer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "software-license-optimizer": {
      "command": "/path/to/repo/skills/software-license-optimizer/venv/bin/python",
      "args": ["/path/to/repo/skills/software-license-optimizer/server.py"],
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
