# 🚀 Contractor Billing Auditor (MCP Server)

## 📖 Overview
This directory contains the **Contractor Billing Auditor** skill, an MCP server designed to Cross-check Jira work logs with vendor invoices.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd contractor-billing-auditor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "contractor-billing-auditor": {
      "command": "/path/to/repo/skills/contractor-billing-auditor/venv/bin/python",
      "args": ["/path/to/repo/skills/contractor-billing-auditor/server.py"],
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
