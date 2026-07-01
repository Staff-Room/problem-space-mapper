---
name: prd-convergence
description: Convergent-thinking method that turns a mapped problem space into a Product Requirements Document with problem evidence, scope, requirements, acceptance criteria, and open questions. Use when the user wants a PRD, product spec, requirements draft, product promise, scope boundary, or bridge from problem discovery into buildable product work.
---

# PRD Convergence

## Overview

Use the PRD as the bridge between problem discovery and solution execution. Every requirement should trace back to problem evidence, a principle, or an accepted decision.

## Inputs

- Problem map or `problem-space-divergence` output.
- User, buyer, stakeholder, and current alternative notes.
- Principles, ADRs, constraints, stakeholder map, C4 view, or known non-goals.
- Evidence quality and open questions.

## Pipeline

1. Restate the product promise in one sentence.
2. Name users, buyers, stakeholders, and jobs.
3. Define scope boundaries: in, out, later.
4. Use the requirements matrix shape: outcome, opportunity, candidate solution, assumption, validation check.
5. Split functional and non-functional requirements.
6. Add acceptance criteria and success metrics.
7. Call out risks, assumptions, research gaps, and C4 view needs.
8. Emit a PRD draft with traceability.

## Output

```md
## PRD: [product or capability]

**Product promise:** [one sentence]
**Problem evidence:** [bullets with confidence]
**Users and jobs:** [who; job; pain]
**Stakeholder map:** [key positions and tensions]
**Scope:** [in / out / later]
**Requirements matrix:** [functional and non-functional requirements with source]
**Acceptance criteria:** [testable conditions]
**Metrics:** [success and guardrails]
**Risks and assumptions:** [explicit]
**Open questions:** [what must be learned next]
**Validation example:** [what catches an untraced or over-scoped PRD]
```

Read [method.md](references/method.md) when translating a large problem map into implementation-ready scope.
