# 🚀 Velocity Burnout Predictor (MCP Server)

## 📖 Overview
This directory contains the **Velocity Burnout Predictor** skill, implemented as a standard Model Context Protocol (MCP) server. When attached to Claude Desktop or Cursor, it grants the AI the ability to securely connect to your enterprise tools and autonomously execute the specialized TPM workflows defined in `prompt.md`.

---

## 🛠️ Prerequisites
Before running this skill, ensure you have the following installed:
- Python 3.10 or higher
- [Claude Desktop App](https://claude.ai/download) (or Cursor IDE)
- `uv` or `pip` for Python package management

### Required Environment Variables
To securely connect to your infrastructure, this server requires the following API keys:
- `GITHUB_TOKEN`\n- `JIRA_API_TOKEN`

---

## ⚙️ Installation & Setup

### 1. Local Setup
Navigate to this skill's directory and install the required dependencies:
```bash
cd velocity-burnout-predictor
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
    "velocity-burnout-predictor": {
      "command": "/path/to/repo/skills/velocity-burnout-predictor/venv/bin/python",
      "args": [
        "/path/to/repo/skills/velocity-burnout-predictor/server.py"
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
> "Claude, analyze sprint velocity and flag any engineers at risk of burnout based on weekend commit data."

Claude will now autonomously reason through the steps, execute the MCP tools, and present the final output!
