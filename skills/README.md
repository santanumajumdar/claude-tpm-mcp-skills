# 🔌 Tier 2: Model Context Protocol (MCP) Servers

Welcome to the heart of Tier 2. This directory contains **100+ local FastMCP servers**.

While Tier 1 skills are pure text prompts, Tier 2 MCP servers actually **execute code locally**. They allow Claude to autonomously fetch data from your databases, trigger GitHub Actions, query Jira, and read AWS CloudWatch logs.

## 🚀 How to Use
1. Navigate into any specific server's folder (e.g., `/postgres-database-server`).
2. Read its internal `README.md` for specific `requirements.txt` dependencies.
3. Add the server to your `claude_desktop_config.json`.

*To enable Agent-First Discovery so Claude can search this folder itself, use the [skill-discovery-server](./skill-discovery-server).*
