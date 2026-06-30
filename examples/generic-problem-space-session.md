# Generic Problem-Space Session

This example is intentionally generic and safe for a public repository.

## Prompt

Use `$mr-problem` to map a tool that helps small teams keep decisions from getting lost after design meetings.

## Expected Flow

1. Mr. Problem asks what breaks today, who feels it, why now, and how teams solve it today.
2. Problem-space divergence separates "recording decisions" from "preserving why the decision was made."
3. ADR convergence turns settled architectural choices into records.
4. PRD convergence scopes the first product around decision capture, search, and handoff.

## Example Handoff

**Problem map:** Teams do not only lose decisions; they lose the reasoning that makes decisions reversible.

**Residue:** Human judgment remains responsible for deciding whether a later change supersedes, refines, or conflicts with an existing record.

**Next convergence:** `adr-convergence` for the decision-log format, then `prd-convergence` for product scope.
