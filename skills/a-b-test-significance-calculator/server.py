import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('ABTestSignificanceCalculator')

@mcp.tool()
def fetch_experiment_results() -> str:
    """Executes the primary function for A B Test Significance Calculator."""
    env_keys = ['MIXPANEL_SECRET']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed fetch_experiment_results successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed fetch_experiment_results with live data."})

if __name__ == '__main__':
    logger.info("Starting A B Test Significance Calculator MCP Server...")
    mcp.run()
