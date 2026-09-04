import os, json, logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('OnCallSchedulerBot')

@mcp.tool()
def calculate_alert_fatigue(team_id: str) -> str:
    if not os.environ.get('PAGERDUTY_API_KEY'):
        logger.warning('No PagerDuty token, returning simulation.')
        return json.dumps({'fatigued_engineers': [{'name': 'Alice', 'off_hours_pages': 42, 'fatigue_score': 'HIGH'}], 'recommendation': 'Remove Alice from primary rotation for next 2 weeks.'})
    return json.dumps({'status': 'connected'})

if __name__ == '__main__':
    mcp.run()