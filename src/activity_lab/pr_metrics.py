"""Pull request cycle and review time evaluation."""
from __future__ import annotations
from datetime import datetime
from typing import Optional

def compute_cycle_hours(created_at: datetime, merged_at: Optional[datetime]) -> Optional[float]:
    """Calculate total hours from pull request creation to merge."""
    if not merged_at:
        return None
    delta = merged_at - created_at
    return round(delta.total_seconds() / 3600.0, 2)
