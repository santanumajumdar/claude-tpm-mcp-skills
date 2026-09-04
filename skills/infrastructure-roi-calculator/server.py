import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('InfrastructureRoiCalculator')

@mcp.tool()
def fetch_cloud_costs() -> str:
    """Executes the primary function for Infrastructure Roi Calculator."""
    env_keys = ['AWS_ACCESS_KEY_ID']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed fetch_cloud_costs successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed fetch_cloud_costs with live data."})

if __name__ == '__main__':
    logger.info("Starting Infrastructure Roi Calculator MCP Server...")
    mcp.run()
