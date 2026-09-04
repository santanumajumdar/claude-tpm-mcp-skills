<div align="center">
  <h1>🧠 Big Tech AI Skills Megarepo (Claude, Cursor, Windsurf & MCP)</h1>
  <p><b>The ultimate library of 400+ AI Skills for TPMs, PMs, SDMs, and SDEs in Big Tech.</b></p>
  
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
  <a href="http://makeapullrequest.com"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
</div>

## 📌 Overview
This repository provides highly advanced AI personas and skills tailored for Engineering Leaders. We offer two distinct tiers of usage depending on your technical comfort level.

### 🌟 Tier 1: Claude Native Skills (No-Code)
Located in the `/claude-native-skills/` directory. These are purely prompt-based skills. 
**How to use:** Simply download the `.md` file and upload it directly into your Claude Web UI / Enterprise using the **"Upload skill"** button.
- 📁 **`/tpms`**: 100 Skills for Technical Program Managers
- 📁 **`/pms`**: 100 Skills for Product Managers
- 📁 **`/sdms`**: 100 Skills for Software Development Managers
- 📁 **`/sdes`**: 100 Skills for Software Engineers
- 📁 **`/executives`**: 5 Highly Strategic Skills for C-Suite (CTO, CISO, VPE, CPO)


### 🔌 Tier 2: MCP Servers (Advanced / Local Execution)
Located in the `/skills/` directory. These are the 100 TPM skills implemented as **Model Context Protocol (MCP)** servers. 
**How to use:** These require local Python execution. They connect directly to your local APIs (Jira, GitHub, Datadog, AWS) so Claude can autonomously fetch data and execute workflows.


### ⚙️ Tier 3: Claude Code Terminal Harnesses (Advanced CLI)
Located in `/claude-code-terminal-harnesses`. These are multi-phase, stateful agent frameworks designed specifically for developers using Anthropic's **Claude Code**, **Cursor**, **Windsurf**, and **Aider**. 
- Features custom terminal **Slash Commands** (e.g., `/tdd`, `/triage`).
- Maintains **Persistent Project Memory** across terminal sessions.
- Includes a 1-click installer (`install_harnesses.sh`) to inject them into `~/.claude/skills`.


### 🤖 Tier 4: Agent-First Skill Discovery (MCP Meta-Server)
Inspired by AAS Core, located in `/skills/skill-discovery-server`. 
Instead of manually searching for skills, run this MCP server. Claude will gain a `search_catalog` tool, allowing it to **autonomously query the 400+ skill JSON bundle** and hot-load new capabilities into its own context dynamically based on the current codebase problem.

---

---

## 📂 Available MCP Servers (Tier 2)


| Skill | Description | Key Integrations |
|-------|-------------|------------------|
| [Cloud Cost Optimizer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/cloud-cost-optimizer) | Terminates idle resources and drafts Jira tickets. | `AWS Cost Explorer` |
| [Auto Triage Agent](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/auto-triage-agent) | Deduplicates and routes bug reports via embeddings. | `Jira`, `OpenAI` |
| [Tech Debt Quantifier](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/tech-debt-quantifier) | Translates SonarQube debt into business hours. | `SonarQube`, `Git` |
| [Root Cause Analyzer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/root-cause-analyzer) | Triangulates Sev-1 failures via logs and commits. | `Datadog`, `GitHub` |
| [Contract Monitor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/cross-repo-contract-monitor) | Analyzes OpenAPI schemas to prevent breaking changes. | `Swagger/OpenAPI` |
| [Security Remediation Bot](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/security-remediation-bot) | Auto-generates PRs to patch high-severity CVEs. | `Snyk`, `Dependabot` |
| [PRD to System Design](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/prd-to-system-design) | Converts PRDs to Mermaid.js C4 architecture diagrams. | `Confluence` |
| [Release Notes Intelligence](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/release-notes-intelligence) | Drafts tailored technical & business release notes. | `GitHub` |
| [Velocity Burnout Predictor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/velocity-burnout-predictor) | Analyzes Git/Jira latency to flag engineering burnout. | `GitHub`, `Jira` |
| [Resource Allocation Matrix](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/resource-allocation-matrix) | Optimizes scheduling across projects based on PTO. | `BambooHR`, `Jira` |
| [Compliance Audit Generator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/compliance-audit-generator) | Scans AWS Config to auto-generate SOC2/GDPR audits. | `AWS Config`, `GitHub` |
| [OKR Alignment Checker](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/okr-alignment-checker) | Maps Jira epics to quarterly Google Sheet OKRs. | `Jira`, `Google Sheets` |
| [Vendor Contract Analyzer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/vendor-contract-analyzer) | Extracts SLA penalties and renewal dates from PDFs. | `OpenAI`, `PyPDF2` |
| [Chaos Engineering Planner](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/chaos-engineering-planner) | Analyzes Sev-1s to propose Gremlin chaos experiments. | `Datadog`, `Gremlin` |
| [On Call Scheduler Bot](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/on-call-scheduler-bot) | Adjusts PagerDuty rotations based on alert fatigue. | `PagerDuty` |
| [Epic Breakdown Assistant](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/epic-breakdown-assistant) | Converts high-level Epics into granular Jira stories. | `Jira` |
| [SLO Violation Detector](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/slo-violation-detector) | Monitors Datadog error budgets for feature freezes. | `Datadog` |
| [Sprint Retro Summarizer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/sprint-retro-summarizer) | Aggregates Slack retro feedback into action items. | `Slack` |
| [Feature Flag Manager](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/feature-flag-manager) | Identifies stale LaunchDarkly flags for code cleanup. | `LaunchDarkly`, `Jira` |
| [CI/CD Bottleneck Finder](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/ci-cd-bottleneck-finder) | Analyzes GitHub Actions runtimes to find slow tests. | `GitHub Actions` |
| [Open Source License Scanner](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/open-source-license-scanner) | Checks repos for GPL/Copyleft licenses and flags them. | `GitHub` |
| [Export Control Auditor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/export-control-auditor) | Checks if code involves encryption algorithms requiring export control classification. | `GitHub` |
| [Accessibility Compliance Bot](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/accessibility-compliance-bot) | Connects to Lighthouse/axe to generate WCAG compliance tickets. | `Jira` |
| [Data Retention Enforcer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/data-retention-enforcer) | Identifies databases lacking automated deletion scripts for GDPR. | `AWS_ACCESS_ID` |
| [Vendor Security Questionnaire Bot](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/vendor-security-questionnaire-bot) | Auto-drafts answers to vendor security questionnaires based on past responses. | `OPENAI_API` |
| [Multi Cloud Cost Comparator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/multi-cloud-cost-comparator) | Compares AWS vs GCP pricing for current workloads. | `AWS_ACCESS_ID` |
| [Spot Instance Advisor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/spot-instance-advisor) | Identifies workloads that can be safely moved to AWS Spot instances. | `AWS_ACCESS_ID` |
| [S3 Bucket Exposure Alerter](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/s3-bucket-exposure-alerter) | Instantly escalates newly created public S3 buckets. | `AWS_ACCESS_ID`, `SLACK_BOT` |
| [Idle Load Balancer Sweeper](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/idle-load-balancer-sweeper) | Finds and removes unused ALBs/ELBs. | `AWS_ACCESS_ID` |
| [Kubernetes Resource Rightsizer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/kubernetes-resource-rightsizer) | Analyzes pod CPU/Mem usage to recommend lower limits. | `DATADOG_API` |
| [Flaky Test Quarantiner](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/flaky-test-quarantiner) | Identifies flaky tests and automatically skips them in CI while creating a Jira ticket. | `GitHub`, `Jira` |
| [Docker Image Bloat Analyzer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/docker-image-bloat-analyzer) | Analyzes Dockerfiles to suggest base image optimizations. | `GitHub` |
| [Deployment Frequency Tracker](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/deployment-frequency-tracker) | Tracks deployments per day per developer. | `GitHub` |
| [Ci Pipeline Cost Estimator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/ci-pipeline-cost-estimator) | Calculates the exact AWS/GCP cost of running a CI pipeline per PR. | `GitHub` |
| [Monorepo Impact Analyzer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/monorepo-impact-analyzer) | Determines which microservices actually need to be rebuilt based on a monorepo PR. | `GitHub` |
| [Mttr Trend Analyzer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/mttr-trend-analyzer) | Tracks Mean Time To Recovery across different services. | `PAGERDUTY_API` |
| [Runbook Staleness Detector](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/runbook-staleness-detector) | Flags runbooks in Confluence that haven't been updated in 6 months. | `CONFLUENCE` |
| [On Call Compensation Calculator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/on-call-compensation-calculator) | Calculates payout for engineers based on off-hours pages. | `PAGERDUTY_API` |
| [Zombie Service Detector](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/zombie-service-detector) | Finds microservices with 0 traffic in the last 30 days. | `DATADOG_API` |
| [Canary Deployment Evaluator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/canary-deployment-evaluator) | Automatically analyzes canary metrics and recommends rollback or full rollout. | `DATADOG_API` |
| [Story Point Calibration Bot](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/story-point-calibration-bot) | Identifies teams whose 5-point stories take wildly different times. | `Jira` |
| [Epic Dependency Grapher](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/epic-dependency-grapher) | Visualizes blocking dependencies across epics in a Mermaid diagram. | `Jira` |
| [Backlog Staleness Purger](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/backlog-staleness-purger) | Auto-closes Jira tickets older than 1 year with no updates. | `Jira` |
| [Capacity Vs Allocation Tracker](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/capacity-vs-allocation-tracker) | Compares planned sprint capacity vs actual hours logged. | `Jira` |
| [Sprint Goal Generator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/sprint-goal-generator) | Uses AI to synthesize a 1-sentence sprint goal from the sprint backlog. | `Jira`, `OPENAI_API` |
| [Developer Happiness Surveyor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/developer-happiness-surveyor) | Sends micro-surveys in Slack and aggregates sentiment. | `SLACK_BOT` |
| [Promotion Packet Assistant](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/promotion-packet-assistant) | Gathers an engineer's PRs, design docs, and incident resolutions for promo review. | `GitHub`, `CONFLUENCE` |
| [Interview Load Balancer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/interview-load-balancer) | Ensures no engineer does more than 3 interviews per week. | `GREENHOUSE_API` |
| [Pto Bottleneck Predictor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/pto-bottleneck-predictor) | Flags if a critical system's only experts are taking PTO at the same time. | `BAMBOOHR_API` |
| [Kudos Aggregator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/kudos-aggregator) | Collects 'thank yous' across Slack channels into a weekly digest. | `SLACK_BOT` |
| [Feature Request Clusterer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/feature-request-clusterer) | Groups similar Zendesk/Intercom tickets into a single feature request. | `ZENDESK` |
| [A B Test Significance Calculator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/a-b-test-significance-calculator) | Connects to analytics to declare if an A/B test has reached statistical significance. | `MIXPANEL_SECRET` |
| [Competitor Feature Tracker](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/competitor-feature-tracker) | Scrapes competitor release notes and alerts PMs/TPMs. | `OPENAI_API` |
| [Churn Correlation Analyzer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/churn-correlation-analyzer) | Correlates specific bugs with user churn events. | `Jira`, `ZENDESK` |
| [Nps Feedback Categorizer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/nps-feedback-categorizer) | Uses NLP to categorize Net Promoter Score text feedback. | `OPENAI_API` |
| [Secrets In Code Remediator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/secrets-in-code-remediator) | Finds leaked secrets, revokes them via API, and creates PRs to remove them. | `GitHub` |
| [Iam Privilege Downgrader](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/iam-privilege-downgrader) | Analyzes IAM roles and suggests downgrades based on last 90 days usage. | `AWS_ACCESS_ID` |
| [Dependency Confusion Preventer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/dependency-confusion-preventer) | Checks package.json for internal package names vulnerable to public registry squatting. | `GitHub` |
| [Api Rate Limit Auditor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/api-rate-limit-auditor) | Ensures all public APIs have appropriate rate limiting configured. | `AWS_ACCESS_ID` |
| [Ssrf Vulnerability Scanner](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/ssrf-vulnerability-scanner) | Scans code for URL parsing patterns susceptible to SSRF. | `GitHub` |
| [Code To Doc Drift Detector](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/code-to-doc-drift-detector) | Compares READMEs against current code behavior and flags drift. | `GitHub` |
| [Tribal Knowledge Extractor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/tribal-knowledge-extractor) | Analyzes Slack threads to generate Q&A pairs for the internal wiki. | `SLACK_BOT`, `CONFLUENCE` |
| [Onboarding Buddy Matcher](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/onboarding-buddy-matcher) | Matches new hires with veterans based on shared interests or timezones. | `BAMBOOHR_API` |
| [Architecture Diagram Updater](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/architecture-diagram-updater) | Regenerates Mermaid diagrams when specific repo folders change. | `GitHub` |
| [Glossary Term Enforcer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/glossary-term-enforcer) | Checks PRDs for inconsistent terminology. | `CONFLUENCE` |
| [Database Migration Reviewer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/database-migration-reviewer) | Reviews SQL migrations for table locks or destructive operations. | `GitHub` |
| [Third Party Api Downtime Tracker](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/third-party-api-downtime-tracker) | Correlates internal errors with external API status pages (e.g. Stripe, Twilio). | `DATADOG_API` |
| [Pr Size Enforcer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/pr-size-enforcer) | Warns developers in Slack if a PR exceeds 500 lines of code. | `GitHub`, `SLACK_BOT` |
| [Error Message Polisher](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/error-message-polisher) | Scans codebase for unhelpful error messages and suggests improvements. | `GitHub` |
| [Tpm Portfolio Summarizer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/tpm-portfolio-summarizer) | Rolls up status across all 100 skills into a master executive dashboard. | `Jira`, `GitHub` |
| [Bug Bounce Analyzer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/bug-bounce-analyzer) | Identify tickets that are frequently reopened to find testing gaps. | `Jira` |
| [Qa Test Gap Analyzer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/qa-test-gap-analyzer) | Correlate PR code changes against E2E test coverage to find gaps. | `GitHub` |
| [Sprint Spillover Forecaster](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/sprint-spillover-forecaster) | Predict which tickets will spill over based on historical patterns. | `Jira` |
| [Release Confidence Scorer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/release-confidence-scorer) | Score a release candidate based on test passes and open P0s. | `GitHub`, `Jira` |
| [Feature Adoption Tracker](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/feature-adoption-tracker) | Track post-launch feature usage in Mixpanel. | `MIXPANEL_SECRET` |
| [Contractor Billing Auditor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/contractor-billing-auditor) | Cross-check Jira work logs with vendor invoices. | `Jira` |
| [Capex Opex Classifier](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/capex-opex-classifier) | Tag engineering tasks for accounting capitalization (CapEx vs OpEx). | `Jira` |
| [Infrastructure Roi Calculator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/infrastructure-roi-calculator) | Calculate the ROI of migrating services or refactoring architecture. | `AWS_ACCESS_ID` |
| [Software License Optimizer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/software-license-optimizer) | Find unused SaaS licenses to cut costs. | `OKTA` |
| [Team Topology Mapper](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/team-topology-mapper) | Analyze interactions to suggest Conway's Law optimizations. | `SLACK_BOT` |
| [Dependency Blocker Escalator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/dependency-blocker-escalator) | Escalate aging cross-squad blockers automatically. | `Jira`, `SLACK_BOT` |
| [Prd Completeness Scorer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/prd-completeness-scorer) | Score PRDs for missing edge cases and Non-Functional Requirements. | `CONFLUENCE` |
| [Engineering Kpi Dashboarder](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/engineering-kpi-dashboarder) | Aggregate DORA metrics (Deployment Frequency, Lead Time, MTTR). | `GitHub`, `DATADOG_API` |
| [Go To Market Sync](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/go-to-market-sync) | Generate technical briefs for Sales/Support teams. | `GitHub`, `CONFLUENCE` |
| [Stakeholder Update Generator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/stakeholder-update-generator) | Draft status updates tailored to specific C-suite personas. | `Jira` |
| [Deprecated Api Tracker](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/deprecated-api-tracker) | Find usages of sunset APIs and create migration tickets. | `GitHub`, `Jira` |
| [Threat Model Assistant](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/threat-model-assistant) | Generate STRIDE threat models from architecture docs. | `CONFLUENCE` |
| [Compliance Drift Detector](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/compliance-drift-detector) | Check infrastructure against baseline SOC2 configs. | `AWS_ACCESS_ID` |
| [Data Privacy Auditor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/data-privacy-auditor) | Scan PRs for new PII fields and flag for legal review. | `GitHub` |
| [Architecture Decision Record Generator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/architecture-decision-record-generator) | Extract ADRs from technical design discussions. | `SLACK_BOT` |
| [Incident Timeline Extractor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/incident-timeline-extractor) | Build precise incident timelines from Slack and PagerDuty. | `SLACK_BOT`, `PAGERDUTY_API` |
| [Postmortem Action Tracker](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/postmortem-action-tracker) | Ensure postmortem action items are prioritized in upcoming sprints. | `Jira`, `CONFLUENCE` |
| [Toil Quantifier](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/toil-quantifier) | Measure engineering time spent on manual ops/support tasks. | `Jira` |
| [Capacity Limit Forecaster](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/capacity-limit-forecaster) | Predict when database or storage limits will be hit. | `DATADOG_API` |
| [Alert Threshold Optimizer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/alert-threshold-optimizer) | Suggest adjustments to noisy Datadog alerts. | `DATADOG_API` |
| [Standup Blocker Summarizer](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/standup-blocker-summarizer) | Extract blockers from daily async standups in Slack. | `SLACK_BOT` |
| [Meeting Cost Calculator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/meeting-cost-calculator) | Calculate the dollar cost of engineering meetings to discourage over-inviting. | `GOOGLE_CALENDAR_API` |
| [Context Switch Monitor](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/context-switch-monitor) | Alert if engineers are assigned to too many distinct epics concurrently. | `Jira` |
| [Onboarding Checklist Generator](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/onboarding-checklist-generator) | Customize engineering onboarding plans based on team and role. | `CONFLUENCE` |
| [Pair Programming Matcher](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/skills/pair-programming-matcher) | Suggest optimal pair programming pairs based on skill gaps. | `GitHub` |

## ⚙️ Getting Started
Each skill is completely self-contained. Navigate to a specific skill's directory and follow its `README.md` for end-to-end setup instructions, including the specific `claude_desktop_config.json` configuration needed.

## 🤝 Contributing
Want to add a skill? See our [Contributing Guidelines](https://github.com/santanumajumdar/claude-tpm-mcp-skills/tree/main/CONTRIBUTING.md).

## 📄 License
MIT License - Copyright (c) 2026 Santanu Majumdar.
