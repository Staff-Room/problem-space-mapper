# Problem Map Workflow

## Purpose

Problem Map is an orchestrator, not a writer. It keeps an agent from mistaking the first plausible solution for the real problem.

## Double Diamond

### Diamond 1: Problem

1. **Open.** Gather who, pain, context, stakes, current workaround, constraints, evidence, and non-obvious alternatives.
2. **Map.** Use `problem-space-divergence` to find dimensions, collapse false axes, and name irreducible residue.
3. **Stabilize.** Emit a problem map with uncertainty visible.

### Diamond 2: Solution

Do not enter the solution diamond until the problem map is stable enough to explain what a solution must preserve.

Route convergence by artifact:

- `principle-convergence`: when the session surfaced reusable laws, ideals, or design principles.
- `adr-convergence`: when the session settled architecture, process, data, or product decisions against alternatives.
- `prd-convergence`: when the next step is product scope, requirements, acceptance criteria, or delivery planning.

## Discovery Prompts

Use these sparingly. Ask the smallest useful set.

- What is broken in the world?
- Who has this problem, and who pays for it?
- What are they doing today instead?
- Why is now the moment this hurts?
- What would make this problem expensive, urgent, or embarrassing?
- What would count as proof that the problem is real?
- What solution are we already biased toward?
- What must remain human judgment?

## Handoff Contract

Every handoff should include:

- problem statement
- audience and stakeholder map
- current alternatives
- evidence and missing evidence
- collapsed dimensions
- irreducible residue
- decisions already made
- recommended next skill
