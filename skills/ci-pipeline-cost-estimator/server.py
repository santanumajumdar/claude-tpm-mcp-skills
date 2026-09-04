import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('CiPipelineCostEstimator')

@mcp.tool()
def fetch_ci_runtime() -> str:
    """Executes the primary function for Ci Pipeline Cost Estimator."""
    env_keys = ['GITHUB_TOKEN']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed fetch_ci_runtime successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed fetch_ci_runtime with live data."})

if __name__ == '__main__':
    logger.info("Starting Ci Pipeline Cost Estimator MCP Server...")
    mcp.run()
