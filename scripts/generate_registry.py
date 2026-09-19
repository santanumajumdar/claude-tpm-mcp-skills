import os
import json
import glob
import re

def get_skill_metadata(skill_path):
    readme_path = os.path.join(skill_path, "README.md")
    
    metadata = {
        "name": os.path.basename(skill_path),
        "description": "",
    }
    
    if os.path.exists(readme_path):
        with open(readme_path, "r", encoding="utf-8") as f:
            content = f.read()
            # Extract first paragraph as description
            match = re.search(r'#.*?\n\n(.*?)(?=\n\n|\Z)', content, re.DOTALL)
            if match:
                metadata["description"] = match.group(1).strip()
    
    return metadata

def main():
    skills_dir = "skills"
    if not os.path.exists(skills_dir):
        print(f"Directory {skills_dir} not found.")
        return

    skills = []
    # Iterate through immediate subdirectories of the skills folder
    for item in os.listdir(skills_dir):
        item_path = os.path.join(skills_dir, item)
        if os.path.isdir(item_path):
            skills.append(get_skill_metadata(item_path))
    
    # Sort alphabetically
    skills.sort(key=lambda x: x["name"])
    
    registry = {
        "total_skills": len(skills),
        "skills": skills
    }
    
    out_path = "skills_registry.json"
    import shutil
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
    shutil.copy(out_path, "docs/skills_registry.json")
    return
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(registry, f, indent=2)
    
    print(f"Generated registry with {len(skills)} skills at {out_path}")

if __name__ == "__main__":
    main()
