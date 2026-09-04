# 🚀 Zombie Service Detector (MCP Server)

## 📖 Overview
This directory contains the **Zombie Service Detector** skill, an MCP server designed to Finds microservices with 0 traffic in the last 30 days.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `DATADOG_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd zombie-service-detector
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "zombie-service-detector": {
      "command": "/path/to/repo/skills/zombie-service-detector/venv/bin/python",
      "args": ["/path/to/repo/skills/zombie-service-detector/server.py"],
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
