# 🚀 Nps Feedback Categorizer (MCP Server)

## 📖 Overview
This directory contains the **Nps Feedback Categorizer** skill, an MCP server designed to Uses NLP to categorize Net Promoter Score text feedback.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `OPENAI_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd nps-feedback-categorizer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "nps-feedback-categorizer": {
      "command": "/path/to/repo/skills/nps-feedback-categorizer/venv/bin/python",
      "args": ["/path/to/repo/skills/nps-feedback-categorizer/server.py"],
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
