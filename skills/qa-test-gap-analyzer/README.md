# 🚀 Qa Test Gap Analyzer (MCP Server)

## 📖 Overview
This directory contains the **Qa Test Gap Analyzer** skill, an MCP server designed to Correlate PR code changes against E2E test coverage to find gaps.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd qa-test-gap-analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "qa-test-gap-analyzer": {
      "command": "/path/to/repo/skills/qa-test-gap-analyzer/venv/bin/python",
      "args": ["/path/to/repo/skills/qa-test-gap-analyzer/server.py"],
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
