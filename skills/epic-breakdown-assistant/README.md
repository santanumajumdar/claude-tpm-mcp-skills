# 🚀 Epic Breakdown Assistant (MCP Server)

## 📖 Overview
This directory contains the **Epic Breakdown Assistant** skill, implemented as a standard Model Context Protocol (MCP) server. When attached to Claude Desktop or Cursor, it grants the AI the ability to securely connect to your enterprise tools and autonomously execute the specialized TPM workflows defined in `prompt.md`.

---

## 🛠️ Prerequisites
Before running this skill, ensure you have the following installed:
- Python 3.10 or higher
- [Claude Desktop App](https://claude.ai/download) (or Cursor IDE)
- `uv` or `pip` for Python package management

### Required Environment Variables
To securely connect to your infrastructure, this server requires the following API keys:
- `JIRA_API_TOKEN`\n- `JIRA_BASE_URL`

---

## ⚙️ Installation & Setup

### 1. Local Setup
Navigate to this skill's directory and install the required dependencies:
```bash
cd epic-breakdown-assistant
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Connect to Claude Desktop
Open your Claude Desktop config file:
- **Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add the following configuration (replace `/path/to/repo` with your actual absolute path):

```json
{
  "mcpServers": {
    "epic-breakdown-assistant": {
      "command": "/path/to/repo/skills/epic-breakdown-assistant/venv/bin/python",
      "args": [
        "/path/to/repo/skills/epic-breakdown-assistant/server.py"
      ],
      "env": {
        // Add your API keys here
      }
    }
  }
}
```

### 3. Restart Claude
Fully quit and restart the Claude Desktop application.

---

## 🎮 How to Use This Skill

1. **Apply the Persona**: Open the `prompt.md` file in this directory and copy its entire contents.
2. **Start a Conversation**: Paste the copied text into a new Claude chat.
3. **Trigger the Workflow**: Give Claude a natural language command:
> "Claude, break down the 'OAuth2.0 Migration' Epic into granular user stories with acceptance criteria."
