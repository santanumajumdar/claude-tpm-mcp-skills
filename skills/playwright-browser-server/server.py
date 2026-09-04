from mcp.server.fastmcp import FastMCP
from playwright.sync_api import sync_playwright
import base64

mcp = FastMCP("Playwright Browser Automation")

@mcp.tool()
def navigate_and_screenshot(url: str) -> str:
    """
    Navigates to a URL and returns a base64 encoded screenshot.
    Use this to visually verify UI bugs.
    """
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="networkidle")
            screenshot_bytes = page.screenshot()
            browser.close()
            
            # Return as base64 string
            b64 = base64.b64encode(screenshot_bytes).decode('utf-8')
            return f"data:image/png;base64,{b64}"
    except Exception as e:
        return f"Error capturing screenshot: {str(e)}"

@mcp.tool()
def extract_dom(url: str) -> str:
    """
    Extracts the raw HTML DOM of a webpage after executing JavaScript.
    """
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page()
            page.goto(url, wait_until="networkidle")
            html = page.content()
            browser.close()
            return html
    except Exception as e:
        return f"Error extracting DOM: {str(e)}"

if __name__ == "__main__":
    mcp.run()
