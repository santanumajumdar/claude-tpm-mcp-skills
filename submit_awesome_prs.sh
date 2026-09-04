#!/bin/bash
echo "🚀 Automatically submitting PRs to Awesome Lists..."

# Submit to ComposioHQ
gh repo fork ComposioHQ/awesome-claude-skills --clone=true
cd awesome-claude-skills
echo "- [Santanu's Big Tech AI Megarepo](https://github.com/santanumajumdar/claude-tpm-mcp-skills) - 400+ FAANG-tier Claude AI skills, MCP servers, and Cross-Agent terminal harnesses." >> README.md
git add README.md
git commit -m "Add Santanu's Big Tech AI Megarepo"
git push origin main
gh pr create --title "Add Santanu's Big Tech AI Megarepo (500+ Assets)" --body "Adding a massive, highly structured repository of 400+ Native Skills and 100+ MCP servers for Engineering Leaders."
cd ..
rm -rf awesome-claude-skills

echo "✅ PR submitted to ComposioHQ!"
