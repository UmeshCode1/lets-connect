"""Test statement coverage percentage calculator."""
from __future__ import annotations

def calculate_coverage(total_statements: int, executed_statements: int) -> float:
    """Compute line coverage percentage rounded to 1 decimal place."""
    if total_statements <= 0:
        return 0.0
    return round((executed_statements / total_statements) * 100.0, 1)
