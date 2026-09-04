# 🚀 Architecture Decision Record Generator (MCP Server)

## 📖 Overview
This directory contains the **Architecture Decision Record Generator** skill, an MCP server designed to Extract ADRs from technical design discussions.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `SLACK_BOT_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd architecture-decision-record-generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "architecture-decision-record-generator": {
      "command": "/path/to/repo/skills/architecture-decision-record-generator/venv/bin/python",
      "args": ["/path/to/repo/skills/architecture-decision-record-generator/server.py"],
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
