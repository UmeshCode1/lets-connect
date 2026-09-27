"""Simple .gitignore pattern matching module."""
from __future__ import annotations
import fnmatch
from typing import List

def should_ignore(file_path: str, ignore_patterns: List[str]) -> bool:
    """Return True if path matches any gitignore glob pattern."""
    for pat in ignore_patterns:
        pat = pat.strip()
        if not pat or pat.startswith("#"):
            continue
        if fnmatch.fnmatch(file_path, pat) or fnmatch.fnmatch(file_path.split("/")[-1], pat):
            return True
    return False
