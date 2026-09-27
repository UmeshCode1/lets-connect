"""Contributor showcase generator."""
from __future__ import annotations
from typing import List, Dict

def make_contributors_table(contributors: List[Dict[str, str]]) -> str:
    """Generate Markdown grid of contributors."""
    headers = "| Contributor | Role | Profile |\n|---|---|---|"
    rows = []
    for c in contributors:
        name = c.get("name", "Unknown")
        role = c.get("role", "Contributor")
        url = c.get("url", "#")
        rows.append(f"| **{name}** | {role} | [{name}]({url}) |")
    return headers + "\n" + "\n".join(rows)
