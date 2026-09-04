<div align="center">
  <h1>🧠 Big Tech AI Skills Megarepo (Claude, Cursor, Windsurf & MCP)</h1>
  <p><b>The ultimate library of 400+ AI Skills for TPMs, PMs, SDMs, and SDEs in Big Tech.</b></p>
  
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](http://makeapullrequest.com)
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
| [Open Source License Scanner](./skills/open-source-license-scanner) | Checks repos for GPL/Copyleft licenses and flags them. | `GitHub` |
| [Export Control Auditor](./skills/export-control-auditor) | Checks if code involves encryption algorithms requiring export control classification. | `GitHub` |
| [Accessibility Compliance Bot](./skills/accessibility-compliance-bot) | Connects to Lighthouse/axe to generate WCAG compliance tickets. | `Jira` |
| [Data Retention Enforcer](./skills/data-retention-enforcer) | Identifies databases lacking automated deletion scripts for GDPR. | `AWS_ACCESS_ID` |
| [Vendor Security Questionnaire Bot](./skills/vendor-security-questionnaire-bot) | Auto-drafts answers to vendor security questionnaires based on past responses. | `OPENAI_API` |
| [Multi Cloud Cost Comparator](./skills/multi-cloud-cost-comparator) | Compares AWS vs GCP pricing for current workloads. | `AWS_ACCESS_ID` |
| [Spot Instance Advisor](./skills/spot-instance-advisor) | Identifies workloads that can be safely moved to AWS Spot instances. | `AWS_ACCESS_ID` |
| [S3 Bucket Exposure Alerter](./skills/s3-bucket-exposure-alerter) | Instantly escalates newly created public S3 buckets. | `AWS_ACCESS_ID`, `SLACK_BOT` |
| [Idle Load Balancer Sweeper](./skills/idle-load-balancer-sweeper) | Finds and removes unused ALBs/ELBs. | `AWS_ACCESS_ID` |
| [Kubernetes Resource Rightsizer](./skills/kubernetes-resource-rightsizer) | Analyzes pod CPU/Mem usage to recommend lower limits. | `DATADOG_API` |
| [Flaky Test Quarantiner](./skills/flaky-test-quarantiner) | Identifies flaky tests and automatically skips them in CI while creating a Jira ticket. | `GitHub`, `Jira` |
| [Docker Image Bloat Analyzer](./skills/docker-image-bloat-analyzer) | Analyzes Dockerfiles to suggest base image optimizations. | `GitHub` |
| [Deployment Frequency Tracker](./skills/deployment-frequency-tracker) | Tracks deployments per day per developer. | `GitHub` |
| [Ci Pipeline Cost Estimator](./skills/ci-pipeline-cost-estimator) | Calculates the exact AWS/GCP cost of running a CI pipeline per PR. | `GitHub` |
| [Monorepo Impact Analyzer](./skills/monorepo-impact-analyzer) | Determines which microservices actually need to be rebuilt based on a monorepo PR. | `GitHub` |
| [Mttr Trend Analyzer](./skills/mttr-trend-analyzer) | Tracks Mean Time To Recovery across different services. | `PAGERDUTY_API` |
| [Runbook Staleness Detector](./skills/runbook-staleness-detector) | Flags runbooks in Confluence that haven't been updated in 6 months. | `CONFLUENCE` |
| [On Call Compensation Calculator](./skills/on-call-compensation-calculator) | Calculates payout for engineers based on off-hours pages. | `PAGERDUTY_API` |
| [Zombie Service Detector](./skills/zombie-service-detector) | Finds microservices with 0 traffic in the last 30 days. | `DATADOG_API` |
| [Canary Deployment Evaluator](./skills/canary-deployment-evaluator) | Automatically analyzes canary metrics and recommends rollback or full rollout. | `DATADOG_API` |
| [Story Point Calibration Bot](./skills/story-point-calibration-bot) | Identifies teams whose 5-point stories take wildly different times. | `Jira` |
| [Epic Dependency Grapher](./skills/epic-dependency-grapher) | Visualizes blocking dependencies across epics in a Mermaid diagram. | `Jira` |
| [Backlog Staleness Purger](./skills/backlog-staleness-purger) | Auto-closes Jira tickets older than 1 year with no updates. | `Jira` |
| [Capacity Vs Allocation Tracker](./skills/capacity-vs-allocation-tracker) | Compares planned sprint capacity vs actual hours logged. | `Jira` |
| [Sprint Goal Generator](./skills/sprint-goal-generator) | Uses AI to synthesize a 1-sentence sprint goal from the sprint backlog. | `Jira`, `OPENAI_API` |
| [Developer Happiness Surveyor](./skills/developer-happiness-surveyor) | Sends micro-surveys in Slack and aggregates sentiment. | `SLACK_BOT` |
| [Promotion Packet Assistant](./skills/promotion-packet-assistant) | Gathers an engineer's PRs, design docs, and incident resolutions for promo review. | `GitHub`, `CONFLUENCE` |
| [Interview Load Balancer](./skills/interview-load-balancer) | Ensures no engineer does more than 3 interviews per week. | `GREENHOUSE_API` |
| [Pto Bottleneck Predictor](./skills/pto-bottleneck-predictor) | Flags if a critical system's only experts are taking PTO at the same time. | `BAMBOOHR_API` |
| [Kudos Aggregator](./skills/kudos-aggregator) | Collects 'thank yous' across Slack channels into a weekly digest. | `SLACK_BOT` |
| [Feature Request Clusterer](./skills/feature-request-clusterer) | Groups similar Zendesk/Intercom tickets into a single feature request. | `ZENDESK` |
| [A B Test Significance Calculator](./skills/a-b-test-significance-calculator) | Connects to analytics to declare if an A/B test has reached statistical significance. | `MIXPANEL_SECRET` |
| [Competitor Feature Tracker](./skills/competitor-feature-tracker) | Scrapes competitor release notes and alerts PMs/TPMs. | `OPENAI_API` |
| [Churn Correlation Analyzer](./skills/churn-correlation-analyzer) | Correlates specific bugs with user churn events. | `Jira`, `ZENDESK` |
| [Nps Feedback Categorizer](./skills/nps-feedback-categorizer) | Uses NLP to categorize Net Promoter Score text feedback. | `OPENAI_API` |
| [Secrets In Code Remediator](./skills/secrets-in-code-remediator) | Finds leaked secrets, revokes them via API, and creates PRs to remove them. | `GitHub` |
| [Iam Privilege Downgrader](./skills/iam-privilege-downgrader) | Analyzes IAM roles and suggests downgrades based on last 90 days usage. | `AWS_ACCESS_ID` |
| [Dependency Confusion Preventer](./skills/dependency-confusion-preventer) | Checks package.json for internal package names vulnerable to public registry squatting. | `GitHub` |
| [Api Rate Limit Auditor](./skills/api-rate-limit-auditor) | Ensures all public APIs have appropriate rate limiting configured. | `AWS_ACCESS_ID` |
| [Ssrf Vulnerability Scanner](./skills/ssrf-vulnerability-scanner) | Scans code for URL parsing patterns susceptible to SSRF. | `GitHub` |
| [Code To Doc Drift Detector](./skills/code-to-doc-drift-detector) | Compares READMEs against current code behavior and flags drift. | `GitHub` |
| [Tribal Knowledge Extractor](./skills/tribal-knowledge-extractor) | Analyzes Slack threads to generate Q&A pairs for the internal wiki. | `SLACK_BOT`, `CONFLUENCE` |
| [Onboarding Buddy Matcher](./skills/onboarding-buddy-matcher) | Matches new hires with veterans based on shared interests or timezones. | `BAMBOOHR_API` |
| [Architecture Diagram Updater](./skills/architecture-diagram-updater) | Regenerates Mermaid diagrams when specific repo folders change. | `GitHub` |
| [Glossary Term Enforcer](./skills/glossary-term-enforcer) | Checks PRDs for inconsistent terminology. | `CONFLUENCE` |
| [Database Migration Reviewer](./skills/database-migration-reviewer) | Reviews SQL migrations for table locks or destructive operations. | `GitHub` |
| [Third Party Api Downtime Tracker](./skills/third-party-api-downtime-tracker) | Correlates internal errors with external API status pages (e.g. Stripe, Twilio). | `DATADOG_API` |
| [Pr Size Enforcer](./skills/pr-size-enforcer) | Warns developers in Slack if a PR exceeds 500 lines of code. | `GitHub`, `SLACK_BOT` |
| [Error Message Polisher](./skills/error-message-polisher) | Scans codebase for unhelpful error messages and suggests improvements. | `GitHub` |
| [Tpm Portfolio Summarizer](./skills/tpm-portfolio-summarizer) | Rolls up status across all 100 skills into a master executive dashboard. | `Jira`, `GitHub` |
| [Bug Bounce Analyzer](./skills/bug-bounce-analyzer) | Identify tickets that are frequently reopened to find testing gaps. | `Jira` |
| [Qa Test Gap Analyzer](./skills/qa-test-gap-analyzer) | Correlate PR code changes against E2E test coverage to find gaps. | `GitHub` |
| [Sprint Spillover Forecaster](./skills/sprint-spillover-forecaster) | Predict which tickets will spill over based on historical patterns. | `Jira` |
| [Release Confidence Scorer](./skills/release-confidence-scorer) | Score a release candidate based on test passes and open P0s. | `GitHub`, `Jira` |
| [Feature Adoption Tracker](./skills/feature-adoption-tracker) | Track post-launch feature usage in Mixpanel. | `MIXPANEL_SECRET` |
| [Contractor Billing Auditor](./skills/contractor-billing-auditor) | Cross-check Jira work logs with vendor invoices. | `Jira` |
| [Capex Opex Classifier](./skills/capex-opex-classifier) | Tag engineering tasks for accounting capitalization (CapEx vs OpEx). | `Jira` |
| [Infrastructure Roi Calculator](./skills/infrastructure-roi-calculator) | Calculate the ROI of migrating services or refactoring architecture. | `AWS_ACCESS_ID` |
| [Software License Optimizer](./skills/software-license-optimizer) | Find unused SaaS licenses to cut costs. | `OKTA` |
| [Team Topology Mapper](./skills/team-topology-mapper) | Analyze interactions to suggest Conway's Law optimizations. | `SLACK_BOT` |
| [Dependency Blocker Escalator](./skills/dependency-blocker-escalator) | Escalate aging cross-squad blockers automatically. | `Jira`, `SLACK_BOT` |
| [Prd Completeness Scorer](./skills/prd-completeness-scorer) | Score PRDs for missing edge cases and Non-Functional Requirements. | `CONFLUENCE` |
| [Engineering Kpi Dashboarder](./skills/engineering-kpi-dashboarder) | Aggregate DORA metrics (Deployment Frequency, Lead Time, MTTR). | `GitHub`, `DATADOG_API` |
| [Go To Market Sync](./skills/go-to-market-sync) | Generate technical briefs for Sales/Support teams. | `GitHub`, `CONFLUENCE` |
| [Stakeholder Update Generator](./skills/stakeholder-update-generator) | Draft status updates tailored to specific C-suite personas. | `Jira` |
| [Deprecated Api Tracker](./skills/deprecated-api-tracker) | Find usages of sunset APIs and create migration tickets. | `GitHub`, `Jira` |
| [Threat Model Assistant](./skills/threat-model-assistant) | Generate STRIDE threat models from architecture docs. | `CONFLUENCE` |
| [Compliance Drift Detector](./skills/compliance-drift-detector) | Check infrastructure against baseline SOC2 configs. | `AWS_ACCESS_ID` |
| [Data Privacy Auditor](./skills/data-privacy-auditor) | Scan PRs for new PII fields and flag for legal review. | `GitHub` |
| [Architecture Decision Record Generator](./skills/architecture-decision-record-generator) | Extract ADRs from technical design discussions. | `SLACK_BOT` |
| [Incident Timeline Extractor](./skills/incident-timeline-extractor) | Build precise incident timelines from Slack and PagerDuty. | `SLACK_BOT`, `PAGERDUTY_API` |
| [Postmortem Action Tracker](./skills/postmortem-action-tracker) | Ensure postmortem action items are prioritized in upcoming sprints. | `Jira`, `CONFLUENCE` |
| [Toil Quantifier](./skills/toil-quantifier) | Measure engineering time spent on manual ops/support tasks. | `Jira` |
| [Capacity Limit Forecaster](./skills/capacity-limit-forecaster) | Predict when database or storage limits will be hit. | `DATADOG_API` |
| [Alert Threshold Optimizer](./skills/alert-threshold-optimizer) | Suggest adjustments to noisy Datadog alerts. | `DATADOG_API` |
| [Standup Blocker Summarizer](./skills/standup-blocker-summarizer) | Extract blockers from daily async standups in Slack. | `SLACK_BOT` |
| [Meeting Cost Calculator](./skills/meeting-cost-calculator) | Calculate the dollar cost of engineering meetings to discourage over-inviting. | `GOOGLE_CALENDAR_API` |
| [Context Switch Monitor](./skills/context-switch-monitor) | Alert if engineers are assigned to too many distinct epics concurrently. | `Jira` |
| [Onboarding Checklist Generator](./skills/onboarding-checklist-generator) | Customize engineering onboarding plans based on team and role. | `CONFLUENCE` |
| [Pair Programming Matcher](./skills/pair-programming-matcher) | Suggest optimal pair programming pairs based on skill gaps. | `GitHub` |

## ⚙️ Getting Started
Each skill is completely self-contained. Navigate to a specific skill's directory and follow its `README.md` for end-to-end setup instructions, including the specific `claude_desktop_config.json` configuration needed.

## 🤝 Contributing
Want to add a skill? See our [Contributing Guidelines](CONTRIBUTING.md).

## 📄 License
MIT License - Copyright (c) 2026 Santanu Majumdar.
