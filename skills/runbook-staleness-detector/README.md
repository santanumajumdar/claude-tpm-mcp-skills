# 🚀 Runbook Staleness Detector (MCP Server)

## 📖 Overview
This directory contains the **Runbook Staleness Detector** skill, an MCP server designed to Flags runbooks in Confluence that haven't been updated in 6 months.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `CONFLUENCE_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd runbook-staleness-detector
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "runbook-staleness-detector": {
      "command": "/path/to/repo/skills/runbook-staleness-detector/venv/bin/python",
      "args": ["/path/to/repo/skills/runbook-staleness-detector/server.py"],
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
