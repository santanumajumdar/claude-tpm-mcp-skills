import os, json, logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('SprintRetroSummarizer')

@mcp.tool()
def extract_themes(channel_id: str) -> str:
    return json.dumps({'went_well': ['CI/CD pipeline speed improved', 'Good cross-team communication'], 'needs_improvement': ['Staging environment was down for 2 days', 'Requirements for Epic X were vague'], 'action_items': ['DevOps to investigate staging stability (Owner: DevOps Lead)']})

if __name__ == '__main__':
    mcp.run()