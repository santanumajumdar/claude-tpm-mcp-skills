# 🚀 Spot Instance Advisor (MCP Server)

## 📖 Overview
This directory contains the **Spot Instance Advisor** skill, an MCP server designed to Identifies workloads that can be safely moved to AWS Spot instances.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `AWS_ACCESS_KEY_ID`

---

## ⚙️ Installation & Setup

```bash
cd spot-instance-advisor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "spot-instance-advisor": {
      "command": "/path/to/repo/skills/spot-instance-advisor/venv/bin/python",
      "args": ["/path/to/repo/skills/spot-instance-advisor/server.py"],
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
