# 🚀 Threat Model Assistant (MCP Server)

## 📖 Overview
This directory contains the **Threat Model Assistant** skill, an MCP server designed to Generate STRIDE threat models from architecture docs.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `CONFLUENCE_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd threat-model-assistant
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "threat-model-assistant": {
      "command": "/path/to/repo/skills/threat-model-assistant/venv/bin/python",
      "args": ["/path/to/repo/skills/threat-model-assistant/server.py"],
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
