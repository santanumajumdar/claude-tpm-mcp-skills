from mcp.server.fastmcp import FastMCP
import json
import os
from pathlib import Path

# Initialize FastMCP server
mcp = FastMCP("Skill Discovery Server")

# Locate the skills bundle
REPO_ROOT = Path(__file__).parent.parent.parent
BUNDLE_PATH = REPO_ROOT / "claude-native-skills" / "skills_bundle.json"

@mcp.tool()
def search_catalog(query: str, role_filter: str = None) -> str:
    """
    Searches the massive catalog of 400+ Claude skills and returns the best matches.
    Use this to dynamically load new skills and capabilities into your own context.
    
    Args:
        query: The problem you are trying to solve (e.g., 'system design', 'reduce aws cost', 'pip').
        role_filter: Optional. Filter by role ('tpms', 'pms', 'sdms', 'sdes', 'executives').
    """
    if not BUNDLE_PATH.exists():
        return "Error: skills_bundle.json not found. Ensure you are running this in the correct directory."
        
    try:
        with open(BUNDLE_PATH, 'r', encoding='utf-8') as f:
            skills = json.load(f)
    except Exception as e:
        return f"Error reading catalog: {str(e)}"
        
    results = []
    query_terms = query.lower().split()
    
    for skill in skills:
        if role_filter and skill.get("role_category") != role_filter:
            continue
            
        skill_id = skill.get("skill_id", "").lower()
        content = skill.get("prompt_content", "").lower()
        
        # Simple scoring based on term frequency
        score = sum(1 for term in query_terms if term in skill_id or term in content)
        
        if score > 0:
            results.append((score, skill))
            
    if not results:
        return f"No skills found matching '{query}'."
        
    # Sort by score descending and take top 3
    results.sort(key=lambda x: x[0], reverse=True)
    top_skills = results[:3]
    
    output = f"🔍 Found {len(results)} skills matching your query. Here are the top {len(top_skills)}:\n\n"
    
    for score, skill in top_skills:
        output += f"### Skill ID: {skill['skill_id']} (Category: {skill['role_category']})\n"
        output += "--- CONTENT START ---\n"
        output += skill['prompt_content'] + "\n"
        output += "--- CONTENT END ---\n\n"
        
    return output

if __name__ == "__main__":
    mcp.run()
