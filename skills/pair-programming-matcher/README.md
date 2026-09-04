# 🚀 Pair Programming Matcher (MCP Server)

## 📖 Overview
This directory contains the **Pair Programming Matcher** skill, an MCP server designed to Suggest optimal pair programming pairs based on skill gaps.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd pair-programming-matcher
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "pair-programming-matcher": {
      "command": "/path/to/repo/skills/pair-programming-matcher/venv/bin/python",
      "args": ["/path/to/repo/skills/pair-programming-matcher/server.py"],
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
