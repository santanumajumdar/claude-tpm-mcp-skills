# 🚀 Api Rate Limit Auditor (MCP Server)

## 📖 Overview
This directory contains the **Api Rate Limit Auditor** skill, an MCP server designed to Ensures all public APIs have appropriate rate limiting configured.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `AWS_ACCESS_KEY_ID`

---

## ⚙️ Installation & Setup

```bash
cd api-rate-limit-auditor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "api-rate-limit-auditor": {
      "command": "/path/to/repo/skills/api-rate-limit-auditor/venv/bin/python",
      "args": ["/path/to/repo/skills/api-rate-limit-auditor/server.py"],
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
