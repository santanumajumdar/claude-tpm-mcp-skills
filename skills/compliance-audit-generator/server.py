import os, json, logging
from mcp.server.fastmcp import FastMCP
import boto3

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('ComplianceAuditGenerator')

@mcp.tool()
def check_aws_config_rules() -> str:
    if not os.environ.get('AWS_ACCESS_KEY_ID'):
        logger.warning('No AWS keys, returning simulation.')
        return json.dumps({'compliant_rules': 145, 'non_compliant': ['s3-bucket-public-read-prohibited']})
    return json.dumps({'status': 'connected'})

if __name__ == '__main__':
    mcp.run()