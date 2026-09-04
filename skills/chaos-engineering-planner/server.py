import os, json, logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('ChaosEngineeringPlanner')

@mcp.tool()
def propose_chaos_experiment(failure_domain: str) -> str:
    return json.dumps({'experiment_name': f'Blackhole {failure_domain} primary node', 'blast_radius': 'Staging environment only', 'expected_outcome': 'Secondary node should take over within 30 seconds.', 'gremlin_attack_type': 'packet_loss'})

if __name__ == '__main__':
    mcp.run()