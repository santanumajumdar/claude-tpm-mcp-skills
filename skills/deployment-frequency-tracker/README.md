# 🚀 Deployment Frequency Tracker (MCP Server)

## 📖 Overview
This directory contains the **Deployment Frequency Tracker** skill, an MCP server designed to Tracks deployments per day per developer.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd deployment-frequency-tracker
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "deployment-frequency-tracker": {
      "command": "/path/to/repo/skills/deployment-frequency-tracker/venv/bin/python",
      "args": ["/path/to/repo/skills/deployment-frequency-tracker/server.py"],
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
