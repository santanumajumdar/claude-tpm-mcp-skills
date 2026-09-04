# 🚀 Canary Deployment Evaluator (MCP Server)

## 📖 Overview
This directory contains the **Canary Deployment Evaluator** skill, an MCP server designed to Automatically analyzes canary metrics and recommends rollback or full rollout.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `DATADOG_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd canary-deployment-evaluator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "canary-deployment-evaluator": {
      "command": "/path/to/repo/skills/canary-deployment-evaluator/venv/bin/python",
      "args": ["/path/to/repo/skills/canary-deployment-evaluator/server.py"],
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
