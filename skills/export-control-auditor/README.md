# 🚀 Export Control Auditor (MCP Server)

## 📖 Overview
This directory contains the **Export Control Auditor** skill, an MCP server designed to Checks if code involves encryption algorithms requiring export control classification.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd export-control-auditor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "export-control-auditor": {
      "command": "/path/to/repo/skills/export-control-auditor/venv/bin/python",
      "args": ["/path/to/repo/skills/export-control-auditor/server.py"],
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
