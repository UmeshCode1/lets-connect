"""Repository programming language detection and breakdown."""
from __future__ import annotations
from pathlib import Path
from typing import Dict, List

EXTENSIONS = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".html": "HTML",
    ".css": "CSS",
    ".md": "Markdown",
    ".json": "JSON",
    ".yml": "YAML",
    ".yaml": "YAML",
}

def analyze_languages(file_paths: List[str]) -> Dict[str, int]:
    """Tally file occurrences by programming language."""
    breakdown = {}
    for p in file_paths:
        ext = Path(p).suffix.lower()
        lang = EXTENSIONS.get(ext, "Other")
        breakdown[lang] = breakdown.get(lang, 0) + 1
    return breakdown
