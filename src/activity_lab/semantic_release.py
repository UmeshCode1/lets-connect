"""Semantic version calculation based on commit types."""
from __future__ import annotations
from typing import List

def determine_bump(commit_types: List[str]) -> str:
    """Return major, minor, or patch bump based on commit prefixes."""
    types = [t.lower() for t in commit_types]
    if "breaking" in types or any("!" in t for t in types):
        return "major"
    if "feat" in types:
        return "minor"
    return "patch"
