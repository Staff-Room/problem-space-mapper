# Validation Ladder

Every step in Mr. Problem needs a small validation surface. The goal is not test theater. The goal is to catch drift when the workflow gets larger.

## Ladder

| Step | Artifact | Validation Example Should Catch |
| --- | --- | --- |
| Intake | Problem intake | The agent jumps to a solution before naming user, pain, evidence, and current alternative. |
| Divergence | Problem map | The agent collapses onto the salient axis instead of the load-bearing axis. |
| Stakeholder mapping | Stakeholder map | The agent erases disagreement or fails to name missing voices. |
| Requirements shaping | Requirements matrix | The agent invents requirements that do not trace to evidence, opportunity, assumption, ADR, or principle. |
| Principle convergence | Principle set | The agent emits broad slogans instead of testable constraints. |
| ADR convergence | ADR | The agent records the decision but loses the reason and rejected alternatives. |
| C4 view | Architecture view | The agent draws the wrong level of detail for the decision being explained. |
| PRD convergence | PRD | The agent writes feature scope without acceptance criteria or evidence confidence. |
| Handoff | Session handoff | The next agent cannot tell what is known, unknown, decided, or still human judgment. |

## Validation Example Shape

Each validation example should include:

- **Prompt:** the user request that should trigger the skill.
- **Fixture:** minimal source material.
- **Expected properties:** things the output must include.
- **Anti-properties:** plausible bad behavior the output must avoid.
- **Regression value:** why this example exists.

Use `templates/validation-example.md` for new examples.
