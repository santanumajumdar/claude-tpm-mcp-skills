# 🚀 Docker Image Bloat Analyzer (MCP Server)

## 📖 Overview
This directory contains the **Docker Image Bloat Analyzer** skill, an MCP server designed to Analyzes Dockerfiles to suggest base image optimizations.

---

## 🛠️ Prerequisites
- Python 3.10+
- [Claude Desktop App](https://claude.ai/download) or Cursor IDE

### Required Environment Variables
- `GITHUB_TOKEN`

---

## ⚙️ Installation & Setup

```bash
cd docker-image-bloat-analyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Claude Desktop Configuration
Add this to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "docker-image-bloat-analyzer": {
      "command": "/path/to/repo/skills/docker-image-bloat-analyzer/venv/bin/python",
      "args": ["/path/to/repo/skills/docker-image-bloat-analyzer/server.py"],
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
