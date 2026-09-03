# 🚀 Auto Triage Agent (MCP Server)

## 📖 Overview
This directory contains the **Auto Triage Agent** skill, implemented as a standard Model Context Protocol (MCP) server. When attached to Claude Desktop or Cursor, it grants the AI the ability to securely connect to your enterprise tools and autonomously execute the specialized TPM workflows defined in `prompt.md`.

---

## 🛠️ Prerequisites
Before running this skill, ensure you have the following installed:
- Python 3.10 or higher
- [Claude Desktop App](https://claude.ai/download) (or Cursor IDE)
- `uv` or `pip` for Python package management

### Required Environment Variables
To securely connect to your infrastructure, this server requires the following API keys:
- `JIRA_API_TOKEN`\n- `JIRA_BASE_URL`\n- `OPENAI_API_KEY (for embeddings)`

---

## ⚙️ Installation & Setup

### 1. Local Setup
Navigate to this skill's directory and install the required dependencies:
```bash
cd auto-triage-agent
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install mcp fastmcp
```

### 2. Connect to Claude Desktop
To make this skill available to Claude, you need to add it to your Claude Desktop configuration. 

Open your Claude Desktop config file:
- **Mac**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add the following configuration (replace `/path/to/repo` with your actual absolute path):

```json
{
  "mcpServers": {
    "auto-triage-agent": {
      "command": "/path/to/repo/skills/auto-triage-agent/venv/bin/python",
      "args": [
        "/path/to/repo/skills/auto-triage-agent/server.py"
      ],
      "env": {
        // Add your API keys here
      }
    }
  }
}
```

### 3. Restart Claude
Fully quit and restart the Claude Desktop application. You should now see a 🔌 plug icon indicating that the MCP server tools are successfully connected.

---

## 🎮 How to Use This Skill

1. **Apply the Persona**: Open the `prompt.md` file in this directory and copy its entire contents.
2. **Start a Conversation**: Paste the copied text into a new Claude chat to lock the AI into the specific TPM persona and workflow.
3. **Trigger the Workflow**: Give Claude a natural language command to execute the task. 

**Example Command:**
> "Claude, check the last 10 incoming bug reports and triage them."

Claude will now autonomously reason through the steps, execute the MCP tools, and present the final output!
