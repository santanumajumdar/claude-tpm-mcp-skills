# 🚀 Epic Dependency Grapher (MCP Server)

## 📖 Overview
This directory contains the **Epic Dependency Grapher** skill, an MCP server designed to Visualizes blocking dependencies across epics in a Mermaid diagram.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd epic-dependency-grapher
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "epic-dependency-grapher": {
      "command": "/path/to/repo/skills/epic-dependency-grapher/venv/bin/python",
      "args": ["/path/to/repo/skills/epic-dependency-grapher/server.py"],
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
