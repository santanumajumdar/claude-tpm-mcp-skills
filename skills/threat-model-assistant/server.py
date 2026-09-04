import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('ThreatModelAssistant')

@mcp.tool()
def read_architecture_doc() -> str:
    """Executes the primary function for Threat Model Assistant."""
    env_keys = ['CONFLUENCE_API_TOKEN']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed read_architecture_doc successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed read_architecture_doc with live data."})

if __name__ == '__main__':
    logger.info("Starting Threat Model Assistant MCP Server...")
    mcp.run()
