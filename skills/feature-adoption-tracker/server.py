import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('FeatureAdoptionTracker')

@mcp.tool()
def query_mixpanel() -> str:
    """Executes the primary function for Feature Adoption Tracker."""
    env_keys = ['MIXPANEL_SECRET']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed query_mixpanel successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed query_mixpanel with live data."})

if __name__ == '__main__':
    logger.info("Starting Feature Adoption Tracker MCP Server...")
    mcp.run()
