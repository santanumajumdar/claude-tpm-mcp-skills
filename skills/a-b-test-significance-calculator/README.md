# 🚀 A B Test Significance Calculator (MCP Server)

## 📖 Overview
This directory contains the **A B Test Significance Calculator** skill, an MCP server designed to Connects to analytics to declare if an A/B test has reached statistical significance.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `MIXPANEL_SECRET`

---

## ⚙️ Installation & Setup

```bash
cd a-b-test-significance-calculator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "a-b-test-significance-calculator": {
      "command": "/path/to/repo/skills/a-b-test-significance-calculator/venv/bin/python",
      "args": ["/path/to/repo/skills/a-b-test-significance-calculator/server.py"],
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
