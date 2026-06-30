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
- Principles, ADRs, constraints, or known non-goals.
- Evidence quality and open questions.

## Pipeline

1. Restate the product promise in one sentence.
2. Name users, buyers, stakeholders, and jobs.
3. Define scope boundaries: in, out, later.
4. Convert problem evidence into requirements.
5. Add acceptance criteria and success metrics.
6. Call out risks, assumptions, and research gaps.
7. Emit a PRD draft with traceability.

## Output

```md
## PRD: [product or capability]

**Product promise:** [one sentence]
**Problem evidence:** [bullets with confidence]
**Users and jobs:** [who; job; pain]
**Scope:** [in / out / later]
**Requirements:** [R1... with source]
**Acceptance criteria:** [testable conditions]
**Metrics:** [success and guardrails]
**Risks and assumptions:** [explicit]
**Open questions:** [what must be learned next]
```

Read [method.md](references/method.md) when translating a large problem map into implementation-ready scope.
