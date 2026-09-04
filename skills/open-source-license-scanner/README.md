# 🚀 Open Source License Scanner (MCP Server)

## 📖 Overview
This directory contains the **Open Source License Scanner** skill, an MCP server designed to Checks repos for GPL/Copyleft licenses and flags them.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd open-source-license-scanner
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "open-source-license-scanner": {
      "command": "/path/to/repo/skills/open-source-license-scanner/venv/bin/python",
      "args": ["/path/to/repo/skills/open-source-license-scanner/server.py"],
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
