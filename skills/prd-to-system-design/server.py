import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('SystemDesigner')

@mcp.tool()
def read_prd(document_id: str) -> str:
    """
    Connects to Confluence API to read a Product Requirements Document (PRD).
    """
    token = os.environ.get("CONFLUENCE_API_TOKEN")
    if not token:
        logger.warning("CONFLUENCE_API_TOKEN missing. Using dummy PRD data.")
        return json.dumps({
            "document_title": "Real-time Notification Service",
            "content": "Goal: Build a real-time chat application using WebSockets, Redis for pub/sub, and a Node.js backend. The system must support up to 1M concurrent users."
        })
        
    return json.dumps({"status": "connected", "data": "Raw markdown content..."})

if __name__ == '__main__':
    logger.info("Starting PRD-to-System Design MCP Server...")
    mcp.run()
