---
name: adr-convergence
description: Convergent-thinking method that turns a meeting, transcript, design session, or working notes into Architecture Decision Records preserving the decision and the reasoning behind it. Use when the user wants to converge on ADRs, pull decisions from a conversation, record what was decided and why, or close a design session with durable architecture records.
---

# ADR Convergence

## Overview

Extract decisions from divergent material and preserve the expert's because. An ADR without context, rejected alternatives, and consequences is not finished.

## Pipeline

1. Extract candidate decisions: commitments made against alternatives.
2. Recover particulars: context, options, chosen option, and why.
3. Ground in prior art when useful. If research is unavailable, mark grounding as `NEEDS RESEARCH`.
4. State consequences, scope, and what reversal would give up.
5. Reconcile against existing ADRs if provided: NEW, REFINES, SUPERSEDES, or CONFLICTS.
6. Emit one ADR per independent reversal point.

## Output

```md
## Decisions from [session]

**ADR-[n] - [Title].**
- **Status:** [Proposed / Accepted]
- **Decision:** [one or two sentences]
- **Context & Options:** [problem, alternatives, rejected options, why]
- **Consequences:** [what becomes easy; what is foreclosed]
- **Reconciliation:** [NEW / REFINES / SUPERSEDES / CONFLICTS]

**Handoff:** [records ready for persistence; flags]
```

Read [method.md](references/method.md) when extracting from long transcripts or reconciling against an existing decision log.
