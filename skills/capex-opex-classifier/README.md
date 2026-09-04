# 🚀 Capex Opex Classifier (MCP Server)

## 📖 Overview
This directory contains the **Capex Opex Classifier** skill, an MCP server designed to Tag engineering tasks for accounting capitalization (CapEx vs OpEx).

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd capex-opex-classifier
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "capex-opex-classifier": {
      "command": "/path/to/repo/skills/capex-opex-classifier/venv/bin/python",
      "args": ["/path/to/repo/skills/capex-opex-classifier/server.py"],
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
