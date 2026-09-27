"""GitHub API rate limit tracking and backoff logic."""
from __future__ import annotations
from typing import Dict

def is_rate_limited(remaining: int, threshold: int = 10) -> bool:
    """Return True if available rate limit falls below safety threshold."""
    return remaining < threshold

def calculate_backoff(reset_timestamp: float, now_timestamp: float) -> int:
    """Calculate sleep seconds required until rate limit resets."""
    return max(0, int(reset_timestamp - now_timestamp))
