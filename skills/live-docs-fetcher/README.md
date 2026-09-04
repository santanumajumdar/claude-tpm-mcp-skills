# 📚 Live Documentation Fetcher (MCP)

This MCP server actively prevents Claude from hallucinating APIs by scraping the live, official documentation for any framework (Next.js 15, React 19, Stripe).

## 🚀 Installation

1. Navigate to this directory and install dependencies:
```bash
cd skills/live-docs-fetcher
pip install -r requirements.txt
```

2. Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "live-docs": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/TO/skills/live-docs-fetcher/server.py"]
    }
  }
}
```

3. Restart Claude Desktop. Claude now has the `fetch_documentation` tool!
