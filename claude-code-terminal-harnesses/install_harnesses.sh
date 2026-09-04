#!/bin/bash
# 🚀 Santanu Majumdar - Cross-Agent Terminal Harness Installer
# Supports: Claude Code, Cursor, Windsurf, Aider

echo "======================================================"
echo "🧠 Installing Tier 3: Santanu Terminal Harnesses..."
echo "======================================================"

# 1. Claude Code
if [ -d "$HOME/.claude" ]; then
    mkdir -p "$HOME/.claude/skills"
    cp *.md "$HOME/.claude/skills/"
    echo "✅ Installed for Claude Code CLI (~/.claude/skills)"
fi

# 2. Cursor IDE
if [ -d "$HOME/.cursor" ]; then
    mkdir -p "$HOME/.cursor/rules"
    cp *.md "$HOME/.cursor/rules/"
    echo "✅ Installed for Cursor IDE (~/.cursor/rules)"
fi

# 3. Windsurf
if [ -d "$HOME/.windsurf" ]; then
    mkdir -p "$HOME/.windsurf/rules"
    cp *.md "$HOME/.windsurf/rules/"
    echo "✅ Installed for Windsurf IDE (~/.windsurf/rules)"
fi

echo "======================================================"
echo "🎉 Success! The harnesses are now globally available across your AI coding agents."
