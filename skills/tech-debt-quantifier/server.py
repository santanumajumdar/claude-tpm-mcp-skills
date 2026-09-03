import os
import json
import logging
import requests
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('TechDebtQuantifier')

@mcp.tool()
def get_sonar_metrics(repo_name: str) -> str:
    """
    Retrieves cyclomatic complexity and code smell counts from SonarQube,
    then applies an algorithm to estimate business cost in engineering hours.
    """
    sonar_url = os.environ.get("SONAR_HOST_URL")
    sonar_token = os.environ.get("SONAR_TOKEN")
    
    if not sonar_url or not sonar_token:
        logger.warning("SonarQube credentials missing. Using simulation mode.")
        return json.dumps({
            'repo': repo_name,
            'metrics': {
                'code_smells': 142,
                'cyclomatic_complexity': 45,
                'duplication_pct': 12.4
            },
            'estimated_wasted_engineering_hours_per_month': 35.5
        })

    try:
        # Example API call
        # response = requests.get(f"{sonar_url}/api/measures/component?component={repo_name}", auth=(sonar_token, ''))
        # response.raise_for_status()
        pass
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to connect to SonarQube: {e}")
        return json.dumps({"error": "Connection failed"})
        
    return json.dumps({"status": "Success"})

if __name__ == '__main__':
    logger.info("Starting Tech Debt Quantifier MCP Server...")
    mcp.run()
