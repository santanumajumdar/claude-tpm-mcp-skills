# 🚀 Glossary Term Enforcer (MCP Server)

## 📖 Overview
This directory contains the **Glossary Term Enforcer** skill, an MCP server designed to Checks PRDs for inconsistent terminology.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `CONFLUENCE_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd glossary-term-enforcer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "glossary-term-enforcer": {
      "command": "/path/to/repo/skills/glossary-term-enforcer/venv/bin/python",
      "args": ["/path/to/repo/skills/glossary-term-enforcer/server.py"],
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
