import os
import sys

def validate():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    native_dir = os.path.join(repo_root, "claude-native-skills")
    
    required_sections = [
        "## 🎭 1. Agent Persona",
        "## 🎯 2. Core Directives",
        "## 📥 3. Input Requirements",
        "## 📋 4. Algorithmic Execution Protocol",
        "## 🚫 5. Anti-Patterns & Constraints",
        "## 📊 6. Expected Output Structure"
    ]
    
    errors = 0
    for root, _, files in os.walk(native_dir):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    content = f.read()
                    
                for section in required_sections:
                    if section not in content:
                        print(f"❌ Error: {file} is missing required section: '{section}'")
                        errors += 1
                        
    if errors > 0:
        print(f"\nFailed with {errors} errors. Please use the standard Big Tech template.")
        sys.exit(1)
    else:
        print("✅ All skills passed validation!")
        sys.exit(0)

if __name__ == "__main__":
    validate()
