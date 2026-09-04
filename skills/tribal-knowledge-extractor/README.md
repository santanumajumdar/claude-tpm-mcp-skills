# 🚀 Tribal Knowledge Extractor (MCP Server)

## 📖 Overview
This directory contains the **Tribal Knowledge Extractor** skill, an MCP server designed to Analyzes Slack threads to generate Q&A pairs for the internal wiki.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `SLACK_BOT_TOKEN`\n- `CONFLUENCE_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd tribal-knowledge-extractor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "tribal-knowledge-extractor": {
      "command": "/path/to/repo/skills/tribal-knowledge-extractor/venv/bin/python",
      "args": ["/path/to/repo/skills/tribal-knowledge-extractor/server.py"],
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
