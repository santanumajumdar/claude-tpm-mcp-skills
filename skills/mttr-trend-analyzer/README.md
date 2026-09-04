# 🚀 Mttr Trend Analyzer (MCP Server)

## 📖 Overview
This directory contains the **Mttr Trend Analyzer** skill, an MCP server designed to Tracks Mean Time To Recovery across different services.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `PAGERDUTY_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd mttr-trend-analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "mttr-trend-analyzer": {
      "command": "/path/to/repo/skills/mttr-trend-analyzer/venv/bin/python",
      "args": ["/path/to/repo/skills/mttr-trend-analyzer/server.py"],
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
