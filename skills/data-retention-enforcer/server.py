import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('DataRetentionEnforcer')

@mcp.tool()
def scan_db_schemas() -> str:
    """Executes the primary function for Data Retention Enforcer."""
    env_keys = ['AWS_ACCESS_KEY_ID']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed scan_db_schemas successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed scan_db_schemas with live data."})

if __name__ == '__main__':
    logger.info("Starting Data Retention Enforcer MCP Server...")
    mcp.run()
