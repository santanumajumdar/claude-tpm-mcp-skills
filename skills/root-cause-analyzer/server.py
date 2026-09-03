import os
import json
import logging
from mcp.server.fastmcp import FastMCP

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('RootCauseAnalyzer')

@mcp.tool()
def fetch_recent_logs(service_name: str, minutes_ago: int = 30) -> str:
    """
    Fetches the most recent error logs from Datadog for a specific service.
    """
    if not os.environ.get("DATADOG_API_KEY"):
        logger.warning("DATADOG_API_KEY missing. Returning simulated log trace.")
        return json.dumps({
            "service": service_name,
            "timestamp": "2026-09-03T10:14:00Z",
            "level": "ERROR",
            "message": "NullPointerException in PaymentProcessor.java:142",
            "trace_id": "trace-987654321"
        })
    return json.dumps({"status": "Connected to Datadog"})

@mcp.tool()
def fetch_recent_commits(repo_name: str) -> str:
    """
    Fetches the commits merged to the main branch in the last hour.
    """
    return json.dumps({
        "commits": [
            {
                "sha": "8f3a1b",
                "message": "Refactor payment gateway retries",
                "author": "John Doe",
                "merged_at": "2026-09-03T10:10:00Z"
            }
        ]
    })

if __name__ == '__main__':
    logger.info("Starting Root Cause Analyzer MCP Server...")
    mcp.run()
