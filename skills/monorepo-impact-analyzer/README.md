# 🚀 Monorepo Impact Analyzer (MCP Server)

## 📖 Overview
This directory contains the **Monorepo Impact Analyzer** skill, an MCP server designed to Determines which microservices actually need to be rebuilt based on a monorepo PR.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd monorepo-impact-analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "monorepo-impact-analyzer": {
      "command": "/path/to/repo/skills/monorepo-impact-analyzer/venv/bin/python",
      "args": ["/path/to/repo/skills/monorepo-impact-analyzer/server.py"],
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
