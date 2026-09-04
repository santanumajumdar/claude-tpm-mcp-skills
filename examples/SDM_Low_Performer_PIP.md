# Example: SDM Low Performer PIP Drafter

**Scenario:** An Engineering Manager needs to place an engineer on a Performance Improvement Plan (PIP).

### ❌ Before (Normal Claude)
*Prompt:* "Write a PIP for my engineer John who isn't committing enough code."
*Response:* "Dear John, you are being placed on a PIP because your code output is too low. You need to write more code over the next 30 days. Let's meet to discuss."
*(Result: A legally risky, demotivating, and entirely subjective document.)*

### ✅ After (Using `low-performer-pip-drafter.md` Skill)
*Prompt:* [SDM uploads the skill persona, then pastes John's last 3 sprint metrics and peer feedback]
*Response:*
**1. Executive Summary (BLUF)**
- John's PR merge velocity is 60% below the SDE II baseline.
- Peer feedback indicates challenges with breaking down large epics independently.
- This 30-day PIP focuses on architectural scoping and independent delivery.

**2. Deep Dive Analysis**
- **Quantitative Gap:** SDE II expectation is 4-6 merged PRs per sprint. John is averaging 1.5. 
- **Qualitative Gap:** PRs are often reverted due to missing test coverage, indicating a gap in TDD fundamentals.

**3. Action Plan (30 Days)**
- **Week 1-2:** John must independently scope the 'Notification Service' epic into 5 INVEST-compliant Jira tickets. 
- **Week 3-4:** Deliver 3 tickets with 100% unit test coverage. All PRs must pass CI/CD without manual QA kickbacks.
- **Support System:** Assigned Sarah (Staff Engineer) as a strictly technical mentor for 1-hour pairing sessions on Tuesdays.

**4. Risks & Mitigations**
- *Risk:* Ambiguous criteria leading to HR dispute.
- *Mitigation:* The goals listed above are binary and objectively measurable via GitHub metrics. 

**5. Next Steps**
Please review this draft. Would you like me to generate the HR-approved email template to schedule the delivery of this document?
