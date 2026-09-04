# 🚀 Engineering Kpi Dashboarder (MCP Server)

## 📖 Overview
This directory contains the **Engineering Kpi Dashboarder** skill, an MCP server designed to Aggregate DORA metrics (Deployment Frequency, Lead Time, MTTR).

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`\n- `DATADOG_API_KEY`

---

## ⚙️ Installation & Setup

```bash
cd engineering-kpi-dashboarder
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "engineering-kpi-dashboarder": {
      "command": "/path/to/repo/skills/engineering-kpi-dashboarder/venv/bin/python",
      "args": ["/path/to/repo/skills/engineering-kpi-dashboarder/server.py"],
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
