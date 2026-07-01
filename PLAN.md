# Plan — One Repo, Either Coding Agent

## Context

This repo currently ships as a **Codex** skill set: `problem-map` (the orchestrator,
formerly "Mr. Problem"), `problem-space-divergence`, and the `principle` / `adr` /
`prd` convergence skills, plus portable markdown templates. In parallel, a richer set
of problem-space skills exists only inside Claude Code / the Claude desktop app
(`problem-space-validator`, `problem-space-evolver`, `product-grill-me`,
`notion-ontology-graph`), wired to Notion + InfraNodus.

The goal is to **collapse both lineages into this one repo** so the same skills run
under **either coding agent (Codex or Claude Code)**, stay **storage-agnostic**
(markdown always; InfraNodus if connected; degrade gracefully), and gain the missing
**second diamond** — a solution-space search that decomposes a problem until each
sub-problem is reliably findable in existing work, then maps how it is already solved.

The intended outcome: point either agent at a fuzzy idea, run `problem-map`, and get a
decomposed problem map + an evidence-backed solution-space map + convergence artifacts,
with no dependency on any specific storage backend.

## Decisions

1. **Evolve this public repo in place.** No new/private repo. Adapters and storage stay
   generic enough to remain public and sanitized (no transcripts, customer data, or
   project-specific wiring).
2. **Single source of truth per skill = its `SKILL.md`.** Both Codex and Claude Code read
   `SKILL.md` + YAML frontmatter natively. Skill bodies are **runtime-neutral prose** and
   reference sibling skills **by name** ("invoke the `problem-space-divergence` skill"),
   never by runtime syntax (`$foo` vs `Skill(foo)`). No forked bodies, no drift.
3. **`problem-map` is an interactive main-loop *skill* (orchestrator) in both runtimes** —
   not a Claude subagent (a subagent runs isolated and can't run the one-question-at-a-time
   interview). Heavy parallel work (solution-space searches) is dispatched as **worker
   subagents** where the runtime supports fan-out (Claude Code Agent/Workflow) and runs
   **sequentially** where it does not (Codex).
4. **Markdown is the canonical single source of truth.** InfraNodus is an optional
   **write-through mirror/enrichment**, gated by a startup capability probe; on failure the
   system logs and continues markdown-only. The divergence/decomposition method is authored
   to work on **reasoning alone** — the graph only sharpens it. **Notion is excluded** from
   this repo (a private overlay skill can add it later behind the same probe pattern).
5. **The two diamonds form a loop, not a pipeline** (see below).

## Runtime-agnostic mechanism

- `SKILL.md` per skill = canonical. Codex already has `agents/openai.yaml` per skill.
- `install.sh` wires each runtime:
  - **Codex:** symlink `skills/*` into `${CODEX_HOME:-$HOME/.codex}/skills/`.
  - **Claude Code:** symlink the same dirs into `~/.claude/skills/`.
- `scripts/validate_skills.py` is extended to check that both manifests stay in sync
  (every skill has a `SKILL.md`, and Codex `agents/openai.yaml` where required).

## Storage-agnostic layer

- Every artifact (`problem-intake.md`, `problem-map.md`, sub-problem records,
  solution-space findings, `prd.md`, `adr.md`) is a markdown file. The system is complete
  and correct with markdown alone.
- A shared **InfraNodus capability probe** (attempt `list_graphs`) sets an availability
  flag. When present, mirror the problem/solution graph in for structural extras
  (betweenness → load-bearing-claim detection, content-gaps, topical clustering). When
  absent, log `InfraNodus not connected — markdown-only` and continue.

## Second diamond — solution-space mapping

New skill **`solution-space-mapping`**, invoked by `problem-map` after the problem is
decomposed. It reuses the evidence-search machinery from the Claude-side
`problem-space-validator` (evidence tiers, claim ledger, subagent contract), ported in and
sanitized.

- **The bridge criterion *is* the search.** A sub-problem is "decomposed enough" when it can
  be **reliably located and identified in peer-reviewed research**. Decomposition terminates
  by attempting the solution-space search:
  - **Found in the literature** → atomic enough; map how it is solved; stop.
  - **Not findable / only partial matches** → still too compound → **recurse: split again**
    and re-search.
  - **Unfindable after genuine decomposition** → flag as **novel residue** (the real
    invention surface).
- **Solution-space source classes** (one worker thread per source per sub-problem, returning
  provenanced, tiered findings):
  1. Peer-reviewed research *(primary benchmark)*
  2. GitHub / open-source repositories
  3. Hugging Face datasets & models
  4. Other public datasets
- **Output** per sub-problem: a solution-space record (what exists, maturity tier, gaps),
  feeding `principle-convergence` / `adr-convergence` / `prd-convergence`.

## Build sequence

1. **Adapter layer** — `install.sh` + Claude Code symlink wiring; extend
   `scripts/validate_skills.py` to a dual-manifest check. Unblocks running everything under
   Claude Code.
2. **Storage-agnostic probe** — a shared "InfraNodus probe + graceful fallback" snippet
   referenced by every skill that can use the graph.
3. **Port the validator engine** into the repo (sanitized) as the solution-space search core.
4. **Write `solution-space-mapping`** and wire `problem-map`'s routing so the front diamond's
   decomposition loop calls it as the termination test.
5. **Recursion/termination logic** in `problem-map` (the "findable in peer-review?" gate).

## Verification

- `python3 scripts/validate_skills.py` passes (both manifests in sync).
- `install.sh` symlinks resolve under both `~/.codex/skills` and `~/.claude/skills`.
- Dry run under **each** agent: `problem-map` on a generic idea produces a decomposed
  problem map, runs `solution-space-mapping` per sub-problem, and emits convergence
  artifacts — once **with** InfraNodus connected and once **without** (identical markdown
  outputs; graph extras present only in the connected run).
