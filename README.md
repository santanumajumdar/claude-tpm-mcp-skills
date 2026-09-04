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
| [Compliance Audit Generator](./skills/compliance-audit-generator) | Scans AWS Config to auto-generate SOC2/GDPR audits. | `AWS Config`, `GitHub` |
| [OKR Alignment Checker](./skills/okr-alignment-checker) | Maps Jira epics to quarterly Google Sheet OKRs. | `Jira`, `Google Sheets` |
| [Vendor Contract Analyzer](./skills/vendor-contract-analyzer) | Extracts SLA penalties and renewal dates from PDFs. | `OpenAI`, `PyPDF2` |
| [Chaos Engineering Planner](./skills/chaos-engineering-planner) | Analyzes Sev-1s to propose Gremlin chaos experiments. | `Datadog`, `Gremlin` |
| [On Call Scheduler Bot](./skills/on-call-scheduler-bot) | Adjusts PagerDuty rotations based on alert fatigue. | `PagerDuty` |
| [Epic Breakdown Assistant](./skills/epic-breakdown-assistant) | Converts high-level Epics into granular Jira stories. | `Jira` |
| [SLO Violation Detector](./skills/slo-violation-detector) | Monitors Datadog error budgets for feature freezes. | `Datadog` |
| [Sprint Retro Summarizer](./skills/sprint-retro-summarizer) | Aggregates Slack retro feedback into action items. | `Slack` |
| [Feature Flag Manager](./skills/feature-flag-manager) | Identifies stale LaunchDarkly flags for code cleanup. | `LaunchDarkly`, `Jira` |
| [CI/CD Bottleneck Finder](./skills/ci-cd-bottleneck-finder) | Analyzes GitHub Actions runtimes to find slow tests. | `GitHub Actions` |
| [Bug Bounce Analyzer](./skills/bug-bounce-analyzer) | Identify tickets that are frequently reopened to find testing gaps. | `Jira` |\n| [Qa Test Gap Analyzer](./skills/qa-test-gap-analyzer) | Correlate PR code changes against E2E test coverage to find gaps. | `GitHub` |\n| [Sprint Spillover Forecaster](./skills/sprint-spillover-forecaster) | Predict which tickets will spill over based on historical patterns. | `Jira` |\n| [Release Confidence Scorer](./skills/release-confidence-scorer) | Score a release candidate based on test passes and open P0s. | `GitHub`, `Jira` |\n| [Feature Adoption Tracker](./skills/feature-adoption-tracker) | Track post-launch feature usage in Mixpanel. | `MIXPANEL_SECRET` |\n| [Contractor Billing Auditor](./skills/contractor-billing-auditor) | Cross-check Jira work logs with vendor invoices. | `Jira` |\n| [Capex Opex Classifier](./skills/capex-opex-classifier) | Tag engineering tasks for accounting capitalization (CapEx vs OpEx). | `Jira` |\n| [Infrastructure Roi Calculator](./skills/infrastructure-roi-calculator) | Calculate the ROI of migrating services or refactoring architecture. | `AWS_ACCESS_ID` |\n| [Software License Optimizer](./skills/software-license-optimizer) | Find unused SaaS licenses to cut costs. | `OKTA` |\n| [Team Topology Mapper](./skills/team-topology-mapper) | Analyze interactions to suggest Conway's Law optimizations. | `SLACK_BOT` |\n| [Dependency Blocker Escalator](./skills/dependency-blocker-escalator) | Escalate aging cross-squad blockers automatically. | `Jira`, `SLACK_BOT` |\n| [Prd Completeness Scorer](./skills/prd-completeness-scorer) | Score PRDs for missing edge cases and Non-Functional Requirements. | `CONFLUENCE` |\n| [Engineering Kpi Dashboarder](./skills/engineering-kpi-dashboarder) | Aggregate DORA metrics (Deployment Frequency, Lead Time, MTTR). | `GitHub`, `DATADOG_API` |\n| [Go To Market Sync](./skills/go-to-market-sync) | Generate technical briefs for Sales/Support teams. | `GitHub`, `CONFLUENCE` |\n| [Stakeholder Update Generator](./skills/stakeholder-update-generator) | Draft status updates tailored to specific C-suite personas. | `Jira` |\n| [Deprecated Api Tracker](./skills/deprecated-api-tracker) | Find usages of sunset APIs and create migration tickets. | `GitHub`, `Jira` |\n| [Threat Model Assistant](./skills/threat-model-assistant) | Generate STRIDE threat models from architecture docs. | `CONFLUENCE` |\n| [Compliance Drift Detector](./skills/compliance-drift-detector) | Check infrastructure against baseline SOC2 configs. | `AWS_ACCESS_ID` |\n| [Data Privacy Auditor](./skills/data-privacy-auditor) | Scan PRs for new PII fields and flag for legal review. | `GitHub` |\n| [Architecture Decision Record Generator](./skills/architecture-decision-record-generator) | Extract ADRs from technical design discussions. | `SLACK_BOT` |\n| [Incident Timeline Extractor](./skills/incident-timeline-extractor) | Build precise incident timelines from Slack and PagerDuty. | `SLACK_BOT`, `PAGERDUTY_API` |\n| [Postmortem Action Tracker](./skills/postmortem-action-tracker) | Ensure postmortem action items are prioritized in upcoming sprints. | `Jira`, `CONFLUENCE` |\n| [Toil Quantifier](./skills/toil-quantifier) | Measure engineering time spent on manual ops/support tasks. | `Jira` |\n| [Capacity Limit Forecaster](./skills/capacity-limit-forecaster) | Predict when database or storage limits will be hit. | `DATADOG_API` |\n| [Alert Threshold Optimizer](./skills/alert-threshold-optimizer) | Suggest adjustments to noisy Datadog alerts. | `DATADOG_API` |\n| [Standup Blocker Summarizer](./skills/standup-blocker-summarizer) | Extract blockers from daily async standups in Slack. | `SLACK_BOT` |\n| [Meeting Cost Calculator](./skills/meeting-cost-calculator) | Calculate the dollar cost of engineering meetings to discourage over-inviting. | `GOOGLE_CALENDAR_API` |\n| [Context Switch Monitor](./skills/context-switch-monitor) | Alert if engineers are assigned to too many distinct epics concurrently. | `Jira` |\n| [Onboarding Checklist Generator](./skills/onboarding-checklist-generator) | Customize engineering onboarding plans based on team and role. | `CONFLUENCE` |\n| [Pair Programming Matcher](./skills/pair-programming-matcher) | Suggest optimal pair programming pairs based on skill gaps. | `GitHub` |\n
## ⚙️ Getting Started
Each skill is completely self-contained. Navigate to a specific skill's directory and follow its `README.md` for end-to-end setup instructions, including the specific `claude_desktop_config.json` configuration needed.

## 🤝 Contributing
Want to add a skill? See our [Contributing Guidelines](CONTRIBUTING.md).

## 📄 License
MIT License - Copyright (c) 2026 Santanu Majumdar.
