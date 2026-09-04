from mcp.server.fastmcp import FastMCP
import requests
from bs4 import BeautifulSoup

mcp = FastMCP("Live Documentation Fetcher")

@mcp.tool()
def fetch_documentation(url: str) -> str:
    """
    Scrapes a documentation URL (e.g., React, Next.js, Stripe docs) to prevent hallucination.
    Extracts the main readable text, stripping away navbars and footers.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer"]):
            script.extract()
            
        text = soup.get_text(separator='\n')
        # Collapse whitespace
        lines = (line.strip() for line in text.splitlines())
        chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
        text = '\n'.join(chunk for chunk in chunks if chunk)
        
        return text[:20000] # Return max 20k chars to fit context window
    except Exception as e:
        return f"Error fetching documentation: {str(e)}"

if __name__ == "__main__":
    mcp.run()
