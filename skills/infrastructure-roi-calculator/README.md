# 🚀 Infrastructure Roi Calculator (MCP Server)

## 📖 Overview
This directory contains the **Infrastructure Roi Calculator** skill, an MCP server designed to Calculate the ROI of migrating services or refactoring architecture.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `AWS_ACCESS_KEY_ID`

---

## ⚙️ Installation & Setup

```bash
cd infrastructure-roi-calculator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "infrastructure-roi-calculator": {
      "command": "/path/to/repo/skills/infrastructure-roi-calculator/venv/bin/python",
      "args": ["/path/to/repo/skills/infrastructure-roi-calculator/server.py"],
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
