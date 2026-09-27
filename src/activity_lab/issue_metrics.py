"""Issue lifecycle and time-to-close metrics."""
from __future__ import annotations
from datetime import datetime
from typing import List, Dict

def average_resolution_days(issues: List[Dict[str, datetime]]) -> float:
    """Compute average days taken to close issues."""
    closed = [i for i in issues if i.get("closed_at") and i.get("created_at")]
    if not closed:
        return 0.0
    total_days = sum((i["closed_at"] - i["created_at"]).total_seconds() / 86400.0 for i in closed)
    return round(total_days / len(closed), 1)
