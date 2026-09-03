import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('ContractMonitor')

@mcp.tool()
def compare_openapi_specs(base_spec_url: str, pr_spec_url: str) -> str:
    """
    Downloads two OpenAPI schemas and performs a structural diff to find breaking changes.
    """
    logger.info(f"Comparing base spec ({base_spec_url}) against PR spec ({pr_spec_url})")
    
    # Simulated contract diff algorithm
    breaking_changes_detected = True
    
    if breaking_changes_detected:
        return json.dumps({
            "status": "FAILED",
            "breaking_changes": [
                {
                    "endpoint": "/api/v1/users/{id}",
                    "method": "GET",
                    "issue": "Required response field 'user_uuid' was removed."
                }
            ],
            "downstream_impact": ["Orders-API", "Billing-Service"]
        })
        
    return json.dumps({"status": "PASSED", "message": "No breaking changes detected."})

if __name__ == '__main__':
    logger.info("Starting Cross-Repo Contract Monitor MCP Server...")
    mcp.run()
