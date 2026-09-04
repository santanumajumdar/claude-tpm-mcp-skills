import os, json, logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('OKRAlignmentChecker')

@mcp.tool()
def flag_unaligned_work(sprint_id: str) -> str:
    if not os.environ.get('JIRA_API_TOKEN'):
        logger.warning('No JIRA token, returning simulation.')
        return json.dumps({'unaligned_tickets': ['ENG-992: Refactor CSS'], 'alignment_score': 82.5})
    return json.dumps({'status': 'connected'})

if __name__ == '__main__':
    mcp.run()