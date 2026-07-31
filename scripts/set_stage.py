#!/usr/bin/env python3
"""Move a project through valid workflow states without skipping gates."""

from __future__ import annotations

import argparse
import re
from datetime import datetime, timezone
from pathlib import Path


STATES = [
    "stage_1_research",
    "stage_1_discussion",
    "stage_2_interpretation",
    "stage_2_discussion",
    "stage_3_prewrite",
    "stage_3_drafting",
    "stage_3_revision",
    "complete",
]

TASKS = {
    "stage_1_research": "Establish the factual terrain",
    "stage_1_discussion": "Discuss Stage 1 findings and research gaps",
    "stage_2_interpretation": "Form and test competing interpretations",
    "stage_2_discussion": "Discuss the governing thesis and argumentative risks",
    "stage_3_prewrite": "Build and discuss the hidden narrative structure",
    "stage_3_drafting": "Draft the article",
    "stage_3_revision": "Audit and revise the article",
    "complete": "Project complete",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("project_dir", type=Path)
    parser.add_argument("new_state", choices=STATES)
    parser.add_argument("--rollback", action="store_true")
    parser.add_argument("--approval-note")
    args = parser.parse_args()

    state_file = args.project_dir.resolve() / "project-state.md"
    text = state_file.read_text(encoding="utf-8")
    match = re.search(r"^- State: (.+)$", text, flags=re.MULTILINE)
    if not match or match.group(1) not in STATES:
        raise SystemExit("Cannot determine a valid current state")

    current = match.group(1)
    old_index = STATES.index(current)
    new_index = STATES.index(args.new_state)
    if args.rollback:
        if new_index >= old_index:
            raise SystemExit("Rollback must target an earlier state")
    elif new_index != old_index + 1:
        raise SystemExit(f"Invalid transition: {current} -> {args.new_state}")

    gated = {
        ("stage_1_discussion", "stage_2_interpretation"),
        ("stage_2_discussion", "stage_3_prewrite"),
        ("stage_3_prewrite", "stage_3_drafting"),
    }
    if (current, args.new_state) in gated and not args.approval_note:
        raise SystemExit("This transition requires --approval-note with the user's explicit approval")

    updated = datetime.now(timezone.utc).isoformat(timespec="seconds")
    text = re.sub(r"^- State: .+$", f"- State: {args.new_state}", text, flags=re.MULTILINE)
    text = re.sub(r"^- Last update: .+$", f"- Last update: {updated}", text, flags=re.MULTILINE)
    text = re.sub(r"^- Current task: .+$", f"- Current task: {TASKS[args.new_state]}", text, flags=re.MULTILINE)
    if args.approval_note:
        gate = f"{current} -> {args.new_state}"
        completed = re.search(r"^- Completed gates: (.+)$", text, flags=re.MULTILINE)
        existing = completed.group(1) if completed else "none"
        new_completed = gate if existing == "none" else f"{existing}; {gate}"
        text = re.sub(r"^- Completed gates: .+$", f"- Completed gates: {new_completed}", text, flags=re.MULTILINE)
    state_file.write_text(text, encoding="utf-8")

    if args.approval_note:
        decisions = args.project_dir.resolve() / "user-decisions.md"
        with decisions.open("a", encoding="utf-8") as handle:
            handle.write(f"| {updated} | {current} | {args.approval_note} | Advance to {args.new_state} |\n")

    print(f"{current} -> {args.new_state}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
