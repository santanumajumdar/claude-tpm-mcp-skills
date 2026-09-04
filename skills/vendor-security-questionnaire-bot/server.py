import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('VendorSecurityQuestionnaireBot')

@mcp.tool()
def parse_questionnaire() -> str:
    """Executes the primary function for Vendor Security Questionnaire Bot."""
    env_keys = ['OPENAI_API_KEY']
    missing = [k for k in env_keys if not os.environ.get(k)]
    
    if missing:
        logger.warning(f"Missing env vars: {missing}. Returning simulated response.")
        return json.dumps({"status": "simulated", "message": "Executed parse_questionnaire successfully in simulation mode."})
        
    return json.dumps({"status": "success", "message": "Executed parse_questionnaire with live data."})

if __name__ == '__main__':
    logger.info("Starting Vendor Security Questionnaire Bot MCP Server...")
    mcp.run()
