# 🚀 Prd Completeness Scorer (MCP Server)

## 📖 Overview
This directory contains the **Prd Completeness Scorer** skill, an MCP server designed to Score PRDs for missing edge cases and Non-Functional Requirements.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `CONFLUENCE_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd prd-completeness-scorer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "prd-completeness-scorer": {
      "command": "/path/to/repo/skills/prd-completeness-scorer/venv/bin/python",
      "args": ["/path/to/repo/skills/prd-completeness-scorer/server.py"],
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
