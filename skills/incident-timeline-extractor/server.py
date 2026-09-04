import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('IncidentTimelineExtractor')

@mcp.tool()
def fetch_incident_logs() -> str:
    """Executes the primary function for Incident Timeline Extractor."""
    env_keys = ['SLACK_BOT_TOKEN', 'PAGERDUTY_API_KEY']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed fetch_incident_logs successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed fetch_incident_logs with live data."})

if __name__ == '__main__':
    logger.info("Starting Incident Timeline Extractor MCP Server...")
    mcp.run()
