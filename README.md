# Problem Space Mapper

An agentic workflow skill repository for guiding messy ideas through problem discovery, divergence, convergence, and durable product artifacts.

The core agent is **Problem Map**. It runs the front half of a double-diamond workflow, then routes the resulting problem map into focused convergence skills:

- `problem-map`: orchestrates the session and decides which skill runs next.
- `problem-space-divergence`: opens a tidy-looking problem into its real dimensions, then collapses false axes.
- `principle-convergence`: extracts grounded principles and a minimal guiding ideal.
- `adr-convergence`: turns settled design choices into Architecture Decision Records.
- `prd-convergence`: turns problem evidence into a scoped Product Requirements Document.

## Install

Copy or symlink the skills into a Codex skills directory:

```bash
cp -R skills/* "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Then start with:

```text
Use $problem-map to map this idea before we build it.
```

## Repository Layout

```text
skills/
  problem-map/
  problem-space-divergence/
  principle-convergence/
  adr-convergence/
  prd-convergence/
templates/
examples/
scripts/
```

## Public Source Hygiene

This repository contains the reusable workflow system only. Raw meeting transcripts, voice notes, customer identifiers, and project-specific artifacts should stay out of this public repo unless explicitly sanitized.

## Validate

```bash
python3 scripts/validate_skills.py
```
