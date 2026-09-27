"""Parser for .gitattributes directives."""
from __future__ import annotations
from typing import Dict, List

def parse_gitattributes(text: str) -> Dict[str, Dict[str, str]]:
    """Parse pattern and attribute pairs from .gitattributes text."""
    rules = {}
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        parts = line.split()
        if len(parts) >= 2:
            pattern = parts[0]
            attrs = {}
            for attr in parts[1:]:
                if "=" in attr:
                    k, v = attr.split("=", 1)
                    attrs[k] = v
                else:
                    attrs[attr] = "true"
            rules[pattern] = attrs
    return rules
