"""Community health score evaluation."""
from __future__ import annotations
from typing import Dict, List, Any

STANDARD_FILES = ["README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md"]

def calculate_health_score(existing_files: List[str]) -> Dict[str, Any]:
    """Calculate community health score out of 100 based on standard files."""
    found = [f for f in STANDARD_FILES if f in existing_files]
    score = int((len(found) / len(STANDARD_FILES)) * 100)
    return {
        "score": score,
        "found": found,
        "missing": [f for f in STANDARD_FILES if f not in existing_files],
    }
