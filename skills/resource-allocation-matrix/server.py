import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('ResourceAllocator')

@mcp.tool()
def get_roster() -> str:
    """
    Connects to BambooHR or internal HR tools to fetch engineer skills and PTO schedules.
    """
    return json.dumps({
        "engineers": [
            {"name": "Alice", "skills": ["Backend", "Python", "AWS"], "pto_upcoming": True},
            {"name": "Bob", "skills": ["Frontend", "React"], "pto_upcoming": False},
            {"name": "Charlie", "skills": ["DevOps", "Kubernetes"], "pto_upcoming": False}
        ]
    })

@mcp.tool()
def get_projects() -> str:
    """
    Fetches high-level epics and their required skill profiles from Jira.
    """
    return json.dumps({
        "projects": [
            {"name": "Project X", "priority": "High", "needs": ["Backend", "DevOps"]},
            {"name": "Project Y", "priority": "Low", "needs": ["Frontend"]}
        ]
    })

if __name__ == '__main__':
    logger.info("Starting Resource Allocation Matrix MCP Server...")
    mcp.run()
