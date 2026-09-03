# Contributing to Claude TPM MCP Skills

First off, thank you for considering contributing! The goal of this megarepo is to reach 100+ high-quality MCP skills for Engineering Leaders and TPMs.

## How to Add a New Skill

1. **Fork the Repository**: Create your own fork and branch off `main`.
2. **Create the Skill Directory**: Create a new folder under `/skills` (e.g., `/skills/my-new-skill`).
3. **Required Files**: Your new skill directory MUST contain:
   - `server.py`: The FastMCP server implementation.
   - `prompt.md`: The System Prompt constraints and execution instructions.
   - `README.md`: End-to-end setup instructions (use existing skills as a template).
   - `requirements.txt`: Specific Python dependencies for your skill.
4. **Submit a Pull Request**: Provide a clear description of the business value your skill provides.

## Code Style
- Use standard PEP 8 formatting.
- Ensure all MCP tools have comprehensive docstrings (Claude reads these!).
- Handle API rate limits and errors gracefully in `server.py`.
