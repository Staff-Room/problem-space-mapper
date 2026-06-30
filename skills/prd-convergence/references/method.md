# PRD Convergence Method

## Traceability

Every requirement must trace to one of:

- direct problem evidence
- a collapsed dimension
- an irreducible residue
- a principle
- an accepted ADR
- a user-stated constraint

If a requirement cannot trace to one of these, put it under "candidate feature" or remove it.

## Scope Boundary

Use three buckets:

- **In:** required to satisfy the product promise.
- **Out:** explicitly not part of this PRD.
- **Later:** valuable but not required for the first proof.

The "out" section is not optional. Scope boundaries are part of the product.

## Acceptance Criteria

Write acceptance criteria as observable checks. Avoid vague criteria like "easy to use" unless paired with a measurable proxy.

## Evidence Confidence

Mark each major assumption:

- **Observed:** directly seen in customer behavior, data, or artifacts.
- **Stated:** reported by a user or stakeholder.
- **Inferred:** reasoned from context but not yet validated.
- **Unknown:** needed but currently missing.
