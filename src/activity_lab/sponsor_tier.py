"""FUNDING.yml configuration generator."""
from __future__ import annotations
from typing import Dict, List, Any

def generate_funding_yml(config: Dict[str, Any]) -> str:
    """Format GitHub Sponsors funding file content."""
    lines = ["# GitHub Funding Configuration"]
    for platform, accounts in config.items():
        if isinstance(accounts, list):
            lines.append(f"{platform}: [{', '.join(accounts)}]")
        else:
            lines.append(f"{platform}: {accounts}")
    return "\n".join(lines)
