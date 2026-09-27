"""Simple ASCII git branch graph visualization."""
from __future__ import annotations
from typing import List

def format_ascii_graph(commits: List[str]) -> str:
    """Format list of commits into standard ASCII tree lines."""
    lines = []
    for idx, c in enumerate(commits):
        connector = "* " if idx == 0 else "|\n* "
        lines.append(f"{connector}{c}")
    return "\n".join(lines)
