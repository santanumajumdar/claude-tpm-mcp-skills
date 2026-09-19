import os
import json
import re

def get_tier1_skills():
    skills = []
    base_dir = "claude-native-skills"
    for root, _, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                name = file.replace(".md", "").replace("-", " ").title()
                # Try to extract description
                desc = f"A native Claude prompt skill located in {os.path.relpath(root, base_dir)}"
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read(500)
                    match = re.search(r'#.*?\n+(.*?)(?=\n|$)', content)
                    if match and match.group(1).strip():
                        desc = match.group(1).strip()
                skills.append({
                    "name": name,
                    "description": desc,
                    "tier": 1,
                    "type": "Markdown Prompt",
                    "path": os.path.join(root, file)
                })
    return skills

def get_tier2_skills():
    skills = []
    base_dir = "skills"
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path):
            readme_path = os.path.join(item_path, "README.md")
            desc = "An MCP server for technical project management."
            if os.path.exists(readme_path):
                with open(readme_path, "r", encoding="utf-8") as f:
                    content = f.read(1000)
                    match = re.search(r'#.*?\n\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
                    if match:
                        desc = match.group(1).strip().replace('\n', ' ')
            skills.append({
                "name": item.replace("-", " ").title(),
                "description": desc,
                "tier": 2,
                "type": "MCP / Python",
                "path": item_path
            })
    return skills

def get_tier3_skills():
    skills = []
    base_dir = "claude-code-terminal-harnesses"
    for item in os.listdir(base_dir):
        if item.endswith(".md") and item != "README.md":
            skills.append({
                "name": item.replace(".md", "").replace("-", " ").title(),
                "description": "An advanced Claude Code terminal harness.",
                "tier": 3,
                "type": "CLI Harness",
                "path": os.path.join(base_dir, item)
            })
    return skills

def get_tier4_skills():
    return [{
        "name": "Skill Discovery Server",
        "description": "An MCP Meta-Server that acts as a router to dynamically discover and load tools.",
        "tier": 4,
        "type": "MCP Meta-Server",
        "path": "skills/skill-discovery-server"
    }]

def get_tier5_skills():
    skills = []
    base_dir = "swarms"
    if os.path.exists(base_dir):
        for item in os.listdir(base_dir):
            item_path = os.path.join(base_dir, item)
            if os.path.isdir(item_path):
                skills.append({
                    "name": item.replace("-", " ").title(),
                    "description": "An autonomous multi-agent swarm.",
                    "tier": 5,
                    "type": "Multi-Agent Swarm",
                    "path": item_path
                })
    return skills

def main():
    all_skills = []
    all_skills.extend(get_tier1_skills())
    all_skills.extend(get_tier2_skills())
    all_skills.extend(get_tier3_skills())
    all_skills.extend(get_tier4_skills())
    all_skills.extend(get_tier5_skills())
    
    registry = {
        "total_skills": len(all_skills),
        "skills": all_skills
    }
    
    os.makedirs("docs", exist_ok=True)
    with open("docs/full_registry.json", "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
    print(f"Generated docs/full_registry.json with {len(all_skills)} skills")

if __name__ == "__main__":
    main()
