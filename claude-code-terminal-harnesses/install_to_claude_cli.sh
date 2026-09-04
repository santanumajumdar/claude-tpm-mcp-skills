#!/bin/bash
# 🚀 Santanu Majumdar - Claude Code Harness Installer

echo "======================================================"
echo "🧠 Installing Tier 3: Santanu Claude Code Harnesses..."
echo "======================================================"

CLAUDE_SKILLS_DIR="$HOME/.claude/skills"

# Create the skills directory if it doesn't exist
mkdir -p "$CLAUDE_SKILLS_DIR"

# Copy the harnesses
cp *.md "$CLAUDE_SKILLS_DIR/"

echo "✅ Success! The Santanu Terminal Harnesses have been injected into $CLAUDE_SKILLS_DIR"
echo "You can now use custom slash commands like /brainstorm, /triage, and /write-tests inside Claude Code!"
