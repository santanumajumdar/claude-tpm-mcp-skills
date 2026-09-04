# 🚀 Churn Correlation Analyzer (MCP Server)

## 📖 Overview
This directory contains the **Churn Correlation Analyzer** skill, an MCP server designed to Correlates specific bugs with user churn events.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`\n- `ZENDESK_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd churn-correlation-analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "churn-correlation-analyzer": {
      "command": "/path/to/repo/skills/churn-correlation-analyzer/venv/bin/python",
      "args": ["/path/to/repo/skills/churn-correlation-analyzer/server.py"],
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
