"""Git blame line ownership distribution calculator."""
from __future__ import annotations
from typing import List, Dict

def calculate_ownership(blame_authors: List[str]) -> Dict[str, float]:
    """Calculate percentage ownership of file lines per author."""
    if not blame_authors:
        return {}
    total = len(blame_authors)
    counts = {}
    for a in blame_authors:
        counts[a] = counts.get(a, 0) + 1
    return {a: round((cnt / total) * 100.0, 1) for a, cnt in counts.items()}
