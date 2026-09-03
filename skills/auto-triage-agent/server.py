import os
import json
import logging
from typing import List, Dict
from mcp.server.fastmcp import FastMCP

# Mocking sentence-transformers for fast startup in template
try:
    from sentence_transformers import SentenceTransformer
    MODEL_AVAILABLE = True
except ImportError:
    MODEL_AVAILABLE = False

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

mcp = FastMCP('AutoTriageAgent')

@mcp.tool()
def find_similar_tickets(bug_description: str) -> str:
    """
    Embeds the incoming bug report and queries the Jira vector store to find duplicates.
    """
    if not os.environ.get("JIRA_API_TOKEN"):
        return json.dumps({"error": "JIRA_API_TOKEN not configured."})

    logger.info(f"Processing bug description: {bug_description[:50]}...")
    
    # Simulate Vector DB lookup
    similarity_score = 0.92
    
    if similarity_score > 0.90:
        return json.dumps({
            "duplicate_found": True,
            "similar_ticket_id": "ENG-1042",
            "similarity_score": similarity_score,
            "ticket_status": "IN PROGRESS"
        })
    
    return json.dumps({"duplicate_found": False})

if __name__ == '__main__':
    logger.info("Starting Auto Triage Agent MCP Server...")
    mcp.run()
