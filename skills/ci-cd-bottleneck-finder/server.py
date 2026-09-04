import os, json, logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('CICDBottleneckFinder')

@mcp.tool()
def analyze_step_durations(repo_name: str) -> str:
    return json.dumps({'average_total_duration_mins': 45.2, 'bottlenecks': [{'step': 'Run E2E Tests', 'avg_duration_mins': 32.5, 'recommendation': 'Implement test sharding/parallelization.'}, {'step': 'Docker Build', 'avg_duration_mins': 8.0, 'recommendation': 'Fix Docker layer caching; cache is missing in 80% of runs.'}]})

if __name__ == '__main__':
    mcp.run()