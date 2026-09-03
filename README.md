<div align="center">
  <h1>🧠 Claude TPM MCP Skills</h1>
  <p><b>A flagship megarepo of Model Context Protocol (MCP) servers and AI Skills for Engineering Leaders.</b></p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
</div>

## 📌 Overview
This repository contains a growing collection of 10+ advanced Claude AI skills designed specifically for Staff/Principal Technical Program Managers. By implementing the [Model Context Protocol (MCP)](https://modelcontextprotocol.io), these servers allow Claude to securely interface with your internal enterprise tools (Jira, AWS, GitHub, Datadog) to autonomously execute complex TPM workflows.

## 🚀 The Goal: 100+ Skills
We are actively building this into the ultimate AI toolkit for TPMs, scaling towards 100+ specialized skills.

## 📂 Available Skills

| Skill | Description | Key Integrations |
|-------|-------------|------------------|
| [Cloud Cost Optimizer](./skills/cloud-cost-optimizer) | Terminates idle resources and drafts Jira tickets. | `AWS Cost Explorer` |
| [Auto Triage Agent](./skills/auto-triage-agent) | Deduplicates and routes bug reports via embeddings. | `Jira`, `OpenAI` |
| [Tech Debt Quantifier](./skills/tech-debt-quantifier) | Translates SonarQube debt into business hours. | `SonarQube`, `Git` |
| [Root Cause Analyzer](./skills/root-cause-analyzer) | Triangulates Sev-1 failures via logs and commits. | `Datadog`, `GitHub` |
| [Contract Monitor](./skills/cross-repo-contract-monitor) | Analyzes OpenAPI schemas to prevent breaking changes. | `Swagger/OpenAPI` |
| [Security Remediation Bot](./skills/security-remediation-bot) | Auto-generates PRs to patch high-severity CVEs. | `Snyk`, `Dependabot` |
| [PRD to System Design](./skills/prd-to-system-design) | Converts PRDs to Mermaid.js C4 architecture diagrams. | `Confluence` |
| [Release Notes Intelligence](./skills/release-notes-intelligence) | Drafts tailored technical & business release notes. | `GitHub` |
| [Velocity Burnout Predictor](./skills/velocity-burnout-predictor) | Analyzes Git/Jira latency to flag engineering burnout. | `GitHub`, `Jira` |
| [Resource Allocation Matrix](./skills/resource-allocation-matrix) | Optimizes scheduling across projects based on PTO. | `BambooHR`, `Jira` |

## ⚙️ Getting Started
Each skill is completely self-contained. Navigate to a specific skill's directory and follow its `README.md` for end-to-end setup instructions, including the specific `claude_desktop_config.json` configuration needed.

## 🤝 Contributing
Want to add a skill? See our [Contributing Guidelines](CONTRIBUTING.md).

## 📄 License
MIT License - Copyright (c) 2026 Santanu Majumdar.
