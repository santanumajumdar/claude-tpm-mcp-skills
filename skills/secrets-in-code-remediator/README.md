# 🚀 Secrets In Code Remediator (MCP Server)

## 📖 Overview
This directory contains the **Secrets In Code Remediator** skill, an MCP server designed to Finds leaked secrets, revokes them via API, and creates PRs to remove them.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd secrets-in-code-remediator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "secrets-in-code-remediator": {
      "command": "/path/to/repo/skills/secrets-in-code-remediator/venv/bin/python",
      "args": ["/path/to/repo/skills/secrets-in-code-remediator/server.py"],
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
