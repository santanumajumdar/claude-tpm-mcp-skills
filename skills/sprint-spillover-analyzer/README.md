# Sprint Spillover Analyzer

This MCP server analyzes Jira tickets (or generic ticket JSON) to identify items that have rolled over multiple sprints, categorizing the root causes for spillover to help teams improve their velocity predictability.

## Features
- **Spillover Detection:** Identifies tickets active across multiple sprint boundaries.
- **Root Cause Categorization:** Attempts to tag issues (e.g., Blocked, Scope Creep, Environment).
- **Executive Summary:** Generates a brief report for the Sprint Retrospective.
