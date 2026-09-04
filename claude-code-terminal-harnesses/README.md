# ⚙️ Tier 3: Claude Code Terminal Harnesses (Advanced)

Welcome to the most advanced tier of this repository, architected by **Santanu Majumdar**. 
Unlike the single-shot prompts in Tier 1, these are **Multi-Phase Terminal Harnesses** explicitly designed for developers using the official Anthropic `claude` CLI tool (Claude Code).

These harnesses turn Claude Code from a reactive chat window into a highly opinionated, stateful software engineering partner.

### 🌟 Advanced Features Built-In:
1. **Interactive Slash Commands (`/`)**: Type commands like `/brainstorm`, `/write-tests`, or `/triage` directly into the terminal to force Claude into specific execution loops.
2. **Persistent Project Memory**: These harnesses are instructed to read and write to local `memory.md` files in your workspace, meaning Claude will *never* forget your project's context across sessions.
3. **Strict Execution Frameworks (e.g., TDD)**: The `Santanu-TDD-Super-Sprint` harness literally refuses to write implementation code until it has written and run failing unit tests via terminal execution.

---

### 🚀 1-Click Installation (For Claude Code Users)
To inject these harnesses directly into your Claude CLI so they auto-load every time you open your terminal:

```bash
cd claude-code-terminal-harnesses
./install_to_claude_cli.sh
```

### 🧠 The Harnesses
- `Santanu-TDD-Super-Sprint.md`: Enforces strict Test-Driven Development loops.
- `Santanu-Sev1-Incident-Commander.md`: Manages high-stress outages with triage and blast-radius tracking.
- `Santanu-Skill-Creator-Engine.md`: A meta-skill that interviews you to generate more terminal harnesses.
