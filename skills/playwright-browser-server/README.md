# 🎭 Playwright Browser Automation (MCP)

This MCP server allows Claude to spin up headless Chromium browsers, navigate to URLs, extract DOM data, and take screenshots (`base64`) to visually debug UI issues.

## 🚀 Installation

1. Navigate to this directory and install dependencies:
```bash
cd skills/playwright-browser-server
pip install -r requirements.txt
playwright install chromium
```

2. Add to your `claude_desktop_config.json`:
```json
{
  "mcpServers": {
    "playwright-browser": {
      "command": "python3",
      "args": ["/ABSOLUTE/PATH/TO/skills/playwright-browser-server/server.py"]
    }
  }
}
```

3. Restart Claude Desktop. Claude now has the `navigate_and_screenshot` and `extract_dom` tools!
