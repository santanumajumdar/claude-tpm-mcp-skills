# 🚀 Data Privacy Auditor (MCP Server)

## 📖 Overview
This directory contains the **Data Privacy Auditor** skill, an MCP server designed to Scan PRs for new PII fields and flag for legal review.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd data-privacy-auditor
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "data-privacy-auditor": {
      "command": "/path/to/repo/skills/data-privacy-auditor/venv/bin/python",
      "args": ["/path/to/repo/skills/data-privacy-auditor/server.py"],
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
