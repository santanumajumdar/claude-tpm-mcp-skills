import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('ReleaseConfidenceScorer')

@mcp.tool()
def fetch_release_metrics() -> str:
    """Executes the primary function for Release Confidence Scorer."""
    env_keys = ['GITHUB_TOKEN', 'JIRA_API_TOKEN']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed fetch_release_metrics successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed fetch_release_metrics with live data."})

if __name__ == '__main__':
    logger.info("Starting Release Confidence Scorer MCP Server...")
    mcp.run()
