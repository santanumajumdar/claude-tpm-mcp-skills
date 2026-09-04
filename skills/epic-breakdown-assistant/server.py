import os, json, logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('EpicBreakdownAssistant')

@mcp.tool()
def generate_user_stories(epic_summary: str) -> str:
    return json.dumps({'epic': epic_summary, 'stories': [{'title': 'Implement OAuth callback endpoint', 'points': 5, 'ac': 'Endpoint accepts auth code and exchanges for token.'}, {'title': 'Update DB schema for refresh tokens', 'points': 3, 'ac': 'Schema updated and migration script provided.'}]})

if __name__ == '__main__':
    mcp.run()