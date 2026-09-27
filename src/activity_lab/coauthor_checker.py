"""Co-authored-by git trailer syntax validator."""
from __future__ import annotations
import re

COAUTHOR_PATTERN = re.compile(r"^Co-authored-by:\s+([^<]+)\s+<([^>]+)>$", re.IGNORECASE)

def validate_coauthor_string(trailer_line: str) -> bool:
    """Check if line adheres to strict RFC git trailer co-authorship syntax."""
    return bool(COAUTHOR_PATTERN.match(trailer_line.strip()))
