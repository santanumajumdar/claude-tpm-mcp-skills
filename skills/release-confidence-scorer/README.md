# 🚀 Release Confidence Scorer (MCP Server)

## 📖 Overview
This directory contains the **Release Confidence Scorer** skill, an MCP server designed to Score a release candidate based on test passes and open P0s.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`\n- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd release-confidence-scorer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "release-confidence-scorer": {
      "command": "/path/to/repo/skills/release-confidence-scorer/venv/bin/python",
      "args": ["/path/to/repo/skills/release-confidence-scorer/server.py"],
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
