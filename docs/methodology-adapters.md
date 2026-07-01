# Methodology Adapters

Mr. Problem should absorb adjacent methods as artifact adapters, not as new centers of gravity.

## Adapter Map

| Method | Borrow | Artifact Home | Validation Question |
| --- | --- | --- | --- |
| Opportunity Solution Trees | Outcome -> opportunity -> solution -> assumption | `templates/requirements-matrix.md` | Does every requirement trace to an opportunity or assumption? |
| IBIS dialog mapping | Issue -> position -> argument -> stakeholder | `templates/stakeholder-map.md` | Does the map preserve disagreement instead of flattening it? |
| C4 model | Context, container, component, code views | `templates/c4-view.md` | Is the view at the right level for the decision or requirement? |
| SkillWiki | Provenance-aware skill evolution | `templates/provenance-ledger.md` | Can a future agent see where the artifact came from? |
| SWE-Skills-Bench | Task-level validation examples | `templates/validation-example.md` | Would this example catch a regression in the skill? |

## Requirements Matrix Adapter

Opportunity Solution Trees are most useful after the problem map is stable. Convert them into a requirements matrix:

- outcome becomes success metric,
- opportunity becomes user need or pain,
- solution becomes candidate requirement,
- assumption becomes validation check,
- opportunity type can split into functional or non-functional requirement.

Do not keep the tree as the final artifact unless the user explicitly needs a visual tree. The durable handoff is the matrix.

## Stakeholder Map Adapter

IBIS dialog mapping is most useful when the problem depends on contested stakeholder perspectives.

Translate:

- issue -> open question or decision pressure,
- position -> stakeholder stance,
- argument -> reason, evidence, risk, or objection,
- unresolved issue -> validation gap.

Do not force agreement. The stakeholder map is valuable because it preserves conflict.

## C4 Adapter

C4 belongs when a PRD or ADR needs architecture clarity.

Use:

- System Context for stakeholder and external-system boundaries.
- Container for major deployable/runtime units.
- Component for internal responsibilities that explain a decision.
- Code only when implementation structure is already in scope.

Do not draw all four levels by default. Pick the smallest useful view.

## Provenance Adapter

Borrow from SkillWiki by keeping provenance attached to artifacts:

- source input,
- transformation skill,
- evidence confidence,
- emitted artifact,
- known limitations,
- validation examples.

This makes skill outputs reusable without pretending they are source truth.
