# 🚀 Error Message Polisher (MCP Server)

## 📖 Overview
This directory contains the **Error Message Polisher** skill, an MCP server designed to Scans codebase for unhelpful error messages and suggests improvements.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd error-message-polisher
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "error-message-polisher": {
      "command": "/path/to/repo/skills/error-message-polisher/venv/bin/python",
      "args": ["/path/to/repo/skills/error-message-polisher/server.py"],
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
