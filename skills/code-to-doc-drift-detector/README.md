# 🚀 Code To Doc Drift Detector (MCP Server)

## 📖 Overview
This directory contains the **Code To Doc Drift Detector** skill, an MCP server designed to Compares READMEs against current code behavior and flags drift.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd code-to-doc-drift-detector
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "code-to-doc-drift-detector": {
      "command": "/path/to/repo/skills/code-to-doc-drift-detector/venv/bin/python",
      "args": ["/path/to/repo/skills/code-to-doc-drift-detector/server.py"],
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
