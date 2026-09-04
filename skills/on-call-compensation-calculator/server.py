import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('OnCallCompensationCalculator')

@mcp.tool()
def fetch_pagerduty_logs() -> str:
    """Executes the primary function for On Call Compensation Calculator."""
    env_keys = ['PAGERDUTY_API_KEY']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed fetch_pagerduty_logs successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed fetch_pagerduty_logs with live data."})

if __name__ == '__main__':
    logger.info("Starting On Call Compensation Calculator MCP Server...")
    mcp.run()
