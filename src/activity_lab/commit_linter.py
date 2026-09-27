"""Conventional commit syntax validation."""
from __future__ import annotations
import re

CONVENTIONAL_PATTERN = re.compile(r"^(feat|fix|docs|style|refactor|perf|test|build|ci|chore|revert)(\([\w\-]+\))?!?:\s+.+$")

def validate_commit_message(msg: str) -> bool:
    """Validate subject line adheres to Conventional Commits 1.0.0."""
    first_line = msg.splitlines()[0].strip()
    return bool(CONVENTIONAL_PATTERN.match(first_line))
