"""Changelog generator based on conventional commit prefixes."""
from __future__ import annotations
from typing import List, Dict

def build_changelog(commit_messages: List[str]) -> Dict[str, List[str]]:
    """Group commit subjects into Features, Fixes, and Maintenance."""
    sections = {"Features": [], "Bug Fixes": [], "Chores & Maintenance": []}
    for msg in commit_messages:
        first_line = msg.splitlines()[0].strip()
        if first_line.startswith("feat"):
            sections["Features"].append(first_line)
        elif first_line.startswith("fix"):
            sections["Bug Fixes"].append(first_line)
        else:
            sections["Chores & Maintenance"].append(first_line)
    return sections
