# 🚀 Feature Request Clusterer (MCP Server)

## 📖 Overview
This directory contains the **Feature Request Clusterer** skill, an MCP server designed to Groups similar Zendesk/Intercom tickets into a single feature request.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `ZENDESK_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd feature-request-clusterer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "feature-request-clusterer": {
      "command": "/path/to/repo/skills/feature-request-clusterer/venv/bin/python",
      "args": ["/path/to/repo/skills/feature-request-clusterer/server.py"],
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
