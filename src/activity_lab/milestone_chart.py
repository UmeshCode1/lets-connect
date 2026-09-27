"""Mermaid chart generator for GitHub milestones."""
from __future__ import annotations
from typing import Dict

def generate_milestone_mermaid(tiers: Dict[str, int]) -> str:
    """Generate Mermaid graph for milestone progression."""
    lines = ["graph LR"]
    prev = None
    for name, req in tiers.items():
        node = f"{name}[{name}: {req}]"
        if prev:
            lines.append(f"  {prev} --> {node}")
        else:
            lines.append(f"  {node}")
        prev = name
    return "\n".join(lines)
