import os
import glob
import py_compile
import re

def check_python(dir_path):
    broken = []
    py_files = glob.glob(os.path.join(dir_path, "**", "*.py"), recursive=True)
    for pf in py_files:
        try:
            py_compile.compile(pf, doraise=True)
        except Exception as e:
            broken.append(f"Syntax error in {pf}")
    return len(py_files), broken

def check_markdown(dir_path):
    broken = []
    md_files = glob.glob(os.path.join(dir_path, "**", "*.md"), recursive=True)
    for md in md_files:
        with open(md, "r", encoding="utf-8") as f:
            content = f.read()
            # Basic check: look for unclosed markdown links [text](url without closing paren
            # This is a very rough heuristic
            if re.search(r'\[[^\]]+\]\([^\)]+$', content):
                broken.append(f"Malformed link in {md}")
    return len(md_files), broken

print("--- AUDITING TIER 1 (Native Skills) ---")
md_count, md_broken = check_markdown("claude-native-skills")
print(f"Checked {md_count} markdown skills. Broken: {len(md_broken)}")
for b in md_broken: print(b)

print("\n--- AUDITING TIER 2 (MCP Servers) ---")
py2_count, py2_broken = check_python("skills")
print(f"Checked {py2_count} python files. Broken: {len(py2_broken)}")
for b in py2_broken: print(b)

print("\n--- AUDITING TIER 3 (Harnesses) ---")
py3_count, py3_broken = check_python("claude-code-terminal-harnesses")
print(f"Checked {py3_count} python files. Broken: {len(py3_broken)}")
for b in py3_broken: print(b)

print("\n--- AUDITING TIER 5 (Swarms) ---")
py5_count, py5_broken = check_python("swarms")
print(f"Checked {py5_count} python files. Broken: {len(py5_broken)}")
for b in py5_broken: print(b)
