# 🚀 Team Topology Mapper (MCP Server)

## 📖 Overview
This directory contains the **Team Topology Mapper** skill, an MCP server designed to Analyze interactions to suggest Conway's Law optimizations.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `SLACK_BOT_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd team-topology-mapper
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "team-topology-mapper": {
      "command": "/path/to/repo/skills/team-topology-mapper/venv/bin/python",
      "args": ["/path/to/repo/skills/team-topology-mapper/server.py"],
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
