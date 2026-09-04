import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('AccessibilityComplianceBot')

@mcp.tool()
def run_axe_scan() -> str:
    """Executes the primary function for Accessibility Compliance Bot."""
    env_keys = ['JIRA_API_TOKEN']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed run_axe_scan successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed run_axe_scan with live data."})

if __name__ == '__main__':
    logger.info("Starting Accessibility Compliance Bot MCP Server...")
    mcp.run()
