# 🚀 Database Migration Reviewer (MCP Server)

## 📖 Overview
This directory contains the **Database Migration Reviewer** skill, an MCP server designed to Reviews SQL migrations for table locks or destructive operations.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd database-migration-reviewer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "database-migration-reviewer": {
      "command": "/path/to/repo/skills/database-migration-reviewer/venv/bin/python",
      "args": ["/path/to/repo/skills/database-migration-reviewer/server.py"],
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
