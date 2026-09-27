"""Repository view and clone traffic statistics aggregator."""
from __future__ import annotations
from typing import List, Dict

def aggregate_traffic(daily_stats: List[Dict[str, int]]) -> Dict[str, int]:
    """Sum total views and unique visitors across days."""
    total_views = sum(d.get("count", 0) for d in daily_stats)
    total_uniques = sum(d.get("uniques", 0) for d in daily_stats)
    return {"total_views": total_views, "total_uniques": total_uniques}
