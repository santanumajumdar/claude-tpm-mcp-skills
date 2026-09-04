# 🚀 Promotion Packet Assistant (MCP Server)

## 📖 Overview
This directory contains the **Promotion Packet Assistant** skill, an MCP server designed to Gathers an engineer's PRs, design docs, and incident resolutions for promo review.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`\n- `CONFLUENCE_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd promotion-packet-assistant
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "promotion-packet-assistant": {
      "command": "/path/to/repo/skills/promotion-packet-assistant/venv/bin/python",
      "args": ["/path/to/repo/skills/promotion-packet-assistant/server.py"],
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
