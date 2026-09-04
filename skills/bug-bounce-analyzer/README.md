# 🚀 Bug Bounce Analyzer (MCP Server)

## 📖 Overview
This directory contains the **Bug Bounce Analyzer** skill, an MCP server designed to Identify tickets that are frequently reopened to find testing gaps.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd bug-bounce-analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "bug-bounce-analyzer": {
      "command": "/path/to/repo/skills/bug-bounce-analyzer/venv/bin/python",
      "args": ["/path/to/repo/skills/bug-bounce-analyzer/server.py"],
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
