#!/usr/bin/env python3
"""Initialize a non-destructive project workspace for this skill."""

from __future__ import annotations

import argparse
from datetime import datetime, timezone
from pathlib import Path


FILES = {
    "project-state.md": """# Project state

- Topic: {topic}
- Time cutoff: {cutoff}
- State: stage_1_research
- Last update: {updated}
- Completed gates: none
- Current task: Establish the factual terrain
""",
    "research-dossier.md": "# Research dossier\n\n## Scope\n\n## Findings by mechanism\n\n## Conflicts and gaps\n",
    "source-ledger.md": "# Source ledger\n\n| Source | Type | Event date | Status | Supports | Cannot support | Follow-up |\n|---|---|---|---|---|---|---|\n",
    "chronology.md": "# Chronology\n\n| Date | Event | Status | Source | Significance |\n|---|---|---|---|---|\n",
    "actor-map.md": "# Actor map\n\n## States and agencies\n\n## Firms and finance\n\n## Workers, communities, and civil society\n\n## Relationships\n",
    "unresolved-questions.md": "# Unresolved questions\n\n## Factual gaps\n\n## Interpretive forks\n\n## Author decisions\n",
    "user-decisions.md": "# User decisions\n\n| Date | Stage | Decision or reservation | Consequence |\n|---|---|---|---|\n",
    "argument-map.md": "# Argument map\n\n## Competing explanations\n\n## Counterevidence\n\n## Proposed governing thesis\n",
    "style-profile.md": "# Project style profile\n\nUse the skill-level profile unless the user approves project-specific overrides.\n",
    "narrative-brief.md": "# Narrative brief\n\nNot started. Complete only in Stage 3.\n",
    "draft.md": "# Draft\n\nDrafting is locked until Stage 3 approval.\n",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("--topic", required=True)
    parser.add_argument("--cutoff", default="current")
    args = parser.parse_args()

    project_dir = args.project_dir.resolve()
    project_dir.mkdir(parents=True, exist_ok=True)
    if any(project_dir.iterdir()):
        raise SystemExit(f"Refusing to initialize non-empty directory: {project_dir}")

    values = {
        "topic": args.topic,
        "cutoff": args.cutoff,
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    for name, template in FILES.items():
        (project_dir / name).write_text(template.format(**values), encoding="utf-8")
    print(project_dir)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

