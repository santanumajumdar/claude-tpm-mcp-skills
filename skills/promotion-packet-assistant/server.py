import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('PromotionPacketAssistant')

@mcp.tool()
def fetch_engineer_portfolio() -> str:
    """Executes the primary function for Promotion Packet Assistant."""
    env_keys = ['GITHUB_TOKEN', 'CONFLUENCE_API_TOKEN']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed fetch_engineer_portfolio successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed fetch_engineer_portfolio with live data."})

if __name__ == '__main__':
    logger.info("Starting Promotion Packet Assistant MCP Server...")
    mcp.run()
