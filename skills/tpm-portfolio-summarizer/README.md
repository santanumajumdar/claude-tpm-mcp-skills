# 🚀 Tpm Portfolio Summarizer (MCP Server)

## 📖 Overview
This directory contains the **Tpm Portfolio Summarizer** skill, an MCP server designed to Rolls up status across all 100 skills into a master executive dashboard.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`\n- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd tpm-portfolio-summarizer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "tpm-portfolio-summarizer": {
      "command": "/path/to/repo/skills/tpm-portfolio-summarizer/venv/bin/python",
      "args": ["/path/to/repo/skills/tpm-portfolio-summarizer/server.py"],
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
