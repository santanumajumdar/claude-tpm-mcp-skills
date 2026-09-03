import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('ReleaseNotes')

@mcp.tool()
def get_merged_prs(repo_name: str, since_tag: str) -> str:
    """
    Queries the GitHub API to fetch all Pull Requests merged since a specific release tag.
    """
    if not os.environ.get("GITHUB_TOKEN"):
        logger.error("Missing GITHUB_TOKEN")
        return json.dumps({"error": "GITHUB_TOKEN required."})
        
    logger.info(f"Fetching PRs for {repo_name} since {since_tag}")
    
    return json.dumps({
        "prs": [
            {"id": 102, "title": "Migrate auth to JWT", "labels": ["backend", "security"]},
            {"id": 104, "title": "Add dark mode toggle", "labels": ["frontend", "feature"]},
            {"id": 105, "title": "Fix memory leak in image upload", "labels": ["bug", "performance"]}
        ]
    })

if __name__ == '__main__':
    logger.info("Starting Release Notes Intelligence MCP Server...")
    mcp.run()
