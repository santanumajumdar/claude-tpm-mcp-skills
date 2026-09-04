# 🚀 S3 Bucket Exposure Alerter (MCP Server)

## 📖 Overview
This directory contains the **S3 Bucket Exposure Alerter** skill, an MCP server designed to Instantly escalates newly created public S3 buckets.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `AWS_ACCESS_KEY_ID`\n- `SLACK_BOT_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd s3-bucket-exposure-alerter
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "s3-bucket-exposure-alerter": {
      "command": "/path/to/repo/skills/s3-bucket-exposure-alerter/venv/bin/python",
      "args": ["/path/to/repo/skills/s3-bucket-exposure-alerter/server.py"],
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
