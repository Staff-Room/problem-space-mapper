---
name: mr-problem
description: Orchestrates an agentic double-diamond workflow from fuzzy idea to durable product artifacts. Use when the user wants to map a problem, explore an idea before building, create "Mr. Problem", run a problem-space mapper, move from discovery into PRD/ADR/principles, or decide which convergence skill should run after a divergent session.
---

# Mr. Problem

## Overview

Guide the user through problem discovery before solution design. Start with the real pain, open the problem space, collapse it into a minimal map, then route to the right convergence artifact.

## Workflow

1. **Intake.** Capture the seed idea, current solution bias, intended audience, known evidence, and publishing constraints.
2. **Discovery.** Ask only enough questions to answer: what is broken, who has it, why now, how is it solved today, and what would prove it matters.
3. **Divergence.** If the problem statement is still tidy, invoke `problem-space-divergence` or follow [workflow.md](references/workflow.md).
4. **Convergence.** Route by target:
   - Need ideals or design laws: `principle-convergence`.
   - Need durable architectural choices: `adr-convergence`.
   - Need product scope: `prd-convergence`.
5. **Handoff.** Emit the current map, unresolved questions, chosen next skill, and the artifact ready for persistence.

## Rules

- Do not jump to product features until the problem map names the user, pain, current workaround, evidence, and cost of inaction.
- Do not publish raw transcripts, private customer details, or sensitive project names unless the user explicitly asks and the target is private.
- Treat unknowns as first-class output. Never invent evidence, citations, decisions, or user commitments.
- Keep the PRD as the bridge artifact between the problem diamond and the solution diamond.

## Output

```md
## Mr. Problem Session: [name]

**Problem map:** [one paragraph]
**User and pain:** [who has it; what breaks]
**Why now:** [trigger, timing, or constraint]
**Current alternatives:** [how it is solved today]
**Evidence:** [known proof; unknowns called out]
**Next convergence:** [principle-convergence / adr-convergence / prd-convergence]
**Handoff:** [artifact or prompt for the next skill]
```

Read [workflow.md](references/workflow.md) when the session needs the full double-diamond routing logic.
