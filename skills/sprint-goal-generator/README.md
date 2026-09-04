# 🚀 Sprint Goal Generator (MCP Server)

## 📖 Overview
This directory contains the **Sprint Goal Generator** skill, an MCP server designed to Uses AI to synthesize a 1-sentence sprint goal from the sprint backlog.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `JIRA_API_TOKEN`\n- `OPENAI_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd sprint-goal-generator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "sprint-goal-generator": {
      "command": "/path/to/repo/skills/sprint-goal-generator/venv/bin/python",
      "args": ["/path/to/repo/skills/sprint-goal-generator/server.py"],
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
