# 🚀 Pto Bottleneck Predictor (MCP Server)

## 📖 Overview
This directory contains the **Pto Bottleneck Predictor** skill, an MCP server designed to Flags if a critical system's only experts are taking PTO at the same time.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `BAMBOOHR_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd pto-bottleneck-predictor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "pto-bottleneck-predictor": {
      "command": "/path/to/repo/skills/pto-bottleneck-predictor/venv/bin/python",
      "args": ["/path/to/repo/skills/pto-bottleneck-predictor/server.py"],
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
