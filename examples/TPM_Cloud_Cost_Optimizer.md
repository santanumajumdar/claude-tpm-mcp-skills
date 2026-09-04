# Example: TPM Cloud Cost Optimizer

**Scenario:** A Principal TPM needs to analyze a massive AWS Cost Explorer CSV export to find savings.

### ❌ Before (Normal Claude)
*Prompt:* "Analyze this AWS billing CSV and tell me how to save money."
*Response:* "Based on the CSV, you are spending a lot on EC2 and RDS. You should consider buying Reserved Instances, deleting unused EBS volumes, and rightsizing your instances to save money."
*(Result: Vague, generic advice. Not actionable for an engineering team.)*

### ✅ After (Using `cloud-cost-optimizer.md` Skill)
*Prompt:* [TPM uploads the skill persona, then attaches the CSV]
*Response:*
**1. Executive Summary (BLUF)**
- Immediate savings of $14,200/mo identified via zombie RDS instances and unattached EBS volumes.
- Long-term scaling bottleneck detected in us-east-1 NAT Gateway usage.

**2. Deep Dive Analysis**
- **EC2:** 45% of `m5.4xlarge` instances in `us-west-2` are peaking at 12% CPU. 
- **EBS:** 142 orphaned volumes total 50TB of wasted gp3 storage.

**3. Action Plan**
- **Immediate (By Friday):** 
  - Execute AWS CLI: `aws ec2 delete-volume --volume-id vol-0abcd1234` (See full script attached).
  - Owner: DevOps On-call.
- **Short-term (Next Sprint):** Migrate the 45 `m5.4xlarge` instances to `m6g.2xlarge` (Graviton2) for a 20% price-performance gain.

**4. Risks & Mitigations**
- *Risk:* Deleting orphaned EBS volumes might cause data loss if snapshots aren't taken.
- *Mitigation:* The provided bash script automatically takes a lifecycle snapshot before executing the delete command.

**5. Next Steps**
Would you like me to generate the exact Jira Epics for the DevOps team to execute this plan?
