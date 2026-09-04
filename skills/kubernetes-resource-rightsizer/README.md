# 🚀 Kubernetes Resource Rightsizer (MCP Server)

## 📖 Overview
This directory contains the **Kubernetes Resource Rightsizer** skill, an MCP server designed to Analyzes pod CPU/Mem usage to recommend lower limits.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `DATADOG_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd kubernetes-resource-rightsizer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "kubernetes-resource-rightsizer": {
      "command": "/path/to/repo/skills/kubernetes-resource-rightsizer/venv/bin/python",
      "args": ["/path/to/repo/skills/kubernetes-resource-rightsizer/server.py"],
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
