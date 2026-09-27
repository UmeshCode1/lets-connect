"""GitHub CODEOWNERS rule pattern evaluator."""
from __future__ import annotations
import fnmatch
from typing import List, Tuple

def resolve_owner(file_path: str, rules: List[Tuple[str, str]]) -> str:
    """Find matching owner based on top-to-bottom CODEOWNERS rules."""
    matched = "unassigned"
    for pattern, owner in rules:
        if fnmatch.fnmatch(file_path, pattern):
            matched = owner
    return matched
