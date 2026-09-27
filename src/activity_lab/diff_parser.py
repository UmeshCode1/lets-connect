"""Git diff insertion/deletion counter."""
from __future__ import annotations
from typing import Dict

def parse_diff_stats(diff_text: str) -> Dict[str, int]:
    """Calculate number of line additions and deletions from unified diff."""
    additions = 0
    deletions = 0
    for line in diff_text.splitlines():
        if line.startswith("+++") or line.startswith("---"):
            continue
        if line.startswith("+"):
            additions += 1
        elif line.startswith("-"):
            deletions += 1
    return {"additions": additions, "deletions": deletions}
