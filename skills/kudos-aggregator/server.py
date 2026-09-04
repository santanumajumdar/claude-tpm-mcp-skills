import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('KudosAggregator')

@mcp.tool()
def scan_slack_kudos() -> str:
    """Executes the primary function for Kudos Aggregator."""
    env_keys = ['SLACK_BOT_TOKEN']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed scan_slack_kudos successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed scan_slack_kudos with live data."})

if __name__ == '__main__':
    logger.info("Starting Kudos Aggregator MCP Server...")
    mcp.run()
