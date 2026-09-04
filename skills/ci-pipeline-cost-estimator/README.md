# 🚀 Ci Pipeline Cost Estimator (MCP Server)

## 📖 Overview
This directory contains the **Ci Pipeline Cost Estimator** skill, an MCP server designed to Calculates the exact AWS/GCP cost of running a CI pipeline per PR.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd ci-pipeline-cost-estimator
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "ci-pipeline-cost-estimator": {
      "command": "/path/to/repo/skills/ci-pipeline-cost-estimator/venv/bin/python",
      "args": ["/path/to/repo/skills/ci-pipeline-cost-estimator/server.py"],
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
