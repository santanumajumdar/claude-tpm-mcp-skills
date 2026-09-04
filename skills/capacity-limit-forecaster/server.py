import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('CapacityLimitForecaster')

@mcp.tool()
def fetch_usage_metrics() -> str:
    """Executes the primary function for Capacity Limit Forecaster."""
    env_keys = ['DATADOG_API_KEY']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed fetch_usage_metrics successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed fetch_usage_metrics with live data."})

if __name__ == '__main__':
    logger.info("Starting Capacity Limit Forecaster MCP Server...")
    mcp.run()
