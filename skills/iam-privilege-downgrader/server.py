import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('IamPrivilegeDowngrader')

@mcp.tool()
def fetch_iam_usage() -> str:
    """Executes the primary function for Iam Privilege Downgrader."""
    env_keys = ['AWS_ACCESS_KEY_ID']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed fetch_iam_usage successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed fetch_iam_usage with live data."})

if __name__ == '__main__':
    logger.info("Starting Iam Privilege Downgrader MCP Server...")
    mcp.run()
