# 🚀 Flaky Test Quarantiner (MCP Server)

## 📖 Overview
This directory contains the **Flaky Test Quarantiner** skill, an MCP server designed to Identifies flaky tests and automatically skips them in CI while creating a Jira ticket.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`\n- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd flaky-test-quarantiner
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "flaky-test-quarantiner": {
      "command": "/path/to/repo/skills/flaky-test-quarantiner/venv/bin/python",
      "args": ["/path/to/repo/skills/flaky-test-quarantiner/server.py"],
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
