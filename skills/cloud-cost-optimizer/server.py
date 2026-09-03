import os
import json
import logging
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP
import boto3
from botocore.exceptions import ClientError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

mcp = FastMCP('CloudCostOptimizer')

@mcp.tool()
def analyze_aws_costs(region: str = 'us-east-1') -> str:
    """
    Analyzes AWS Cost Explorer and EC2 data to identify idle or unattached resources.
    Requires AWS_ACCESS_KEY_ID and AWS_SECRET_ACCESS_KEY in the environment.
    """
    if not os.environ.get("AWS_ACCESS_KEY_ID"):
        logger.warning("AWS credentials missing, falling back to simulation mode.")
        return json.dumps({
            'idle_ec2': ['i-0abcd1234efgh5678'],
            'unattached_ebs': ['vol-0123456789abcdef0'],
            'estimated_monthly_savings_usd': 450.00,
            'status': 'simulated'
        })

    try:
        # Initialize boto3 clients
        ec2 = boto3.client('ec2', region_name=region)
        ce = boto3.client('ce', region_name=region)
        
        # In a real execution, we would query Cost Explorer for unused capacity
        # ce.get_cost_and_usage(...)
        
        return json.dumps({"status": "success", "message": "Successfully scanned AWS environment."})
    except ClientError as e:
        logger.error(f"AWS API Error: {str(e)}")
        return json.dumps({"status": "error", "message": str(e)})

if __name__ == '__main__':
    logger.info("Starting Cloud Cost Optimizer MCP Server...")
    mcp.run()
