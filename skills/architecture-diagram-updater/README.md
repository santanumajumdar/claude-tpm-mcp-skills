# 🚀 Architecture Diagram Updater (MCP Server)

## 📖 Overview
This directory contains the **Architecture Diagram Updater** skill, an MCP server designed to Regenerates Mermaid diagrams when specific repo folders change.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd architecture-diagram-updater
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "architecture-diagram-updater": {
      "command": "/path/to/repo/skills/architecture-diagram-updater/venv/bin/python",
      "args": ["/path/to/repo/skills/architecture-diagram-updater/server.py"],
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
