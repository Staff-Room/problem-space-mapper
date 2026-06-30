#!/usr/bin/env python3
"""Validate basic skill repository structure."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9-]+$")


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing opening frontmatter delimiter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("missing closing frontmatter delimiter")
    data: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        key, sep, value = line.partition(":")
        if not sep:
            raise ValueError(f"invalid frontmatter line: {line}")
        data[key.strip()] = value.strip().strip('"')
    return data


def main() -> int:
    failures: list[str] = []
    if not SKILLS.is_dir():
        failures.append("skills/ directory is missing")
    for skill_dir in sorted(SKILLS.iterdir() if SKILLS.exists() else []):
        if not skill_dir.is_dir():
            continue
        skill_file = skill_dir / "SKILL.md"
        if not skill_file.exists():
            failures.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        try:
            frontmatter = parse_frontmatter(skill_file)
        except ValueError as error:
            failures.append(f"{skill_dir.name}: {error}")
            continue
        name = frontmatter.get("name", "")
        description = frontmatter.get("description", "")
        if name != skill_dir.name:
            failures.append(f"{skill_dir.name}: frontmatter name must match directory")
        if not NAME_RE.match(name):
            failures.append(f"{skill_dir.name}: invalid skill name")
        if not description or "TODO" in description:
            failures.append(f"{skill_dir.name}: description is missing or unfinished")
        if len(description) > 1024:
            failures.append(f"{skill_dir.name}: description exceeds 1024 characters")
        if not (skill_dir / "agents" / "openai.yaml").exists():
            failures.append(f"{skill_dir.name}: missing agents/openai.yaml")
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("OK: skill repository structure is valid")
    return 0


if __name__ == "__main__":
    sys.exit(main())
