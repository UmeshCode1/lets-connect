"""ASCII sparkline generator for numerical sequences."""
from __future__ import annotations
from typing import List

TICKS = [" ", "▂", "▃", "▄", "▅", "▆", "▇", "█"]

def render_sparkline(values: List[float]) -> str:
    """Convert sequence of numbers into Unicode sparkline graph."""
    if not values:
        return ""
    min_v, max_v = min(values), max(values)
    span = max_v - min_v
    if span == 0:
        return TICKS[3] * len(values)
    res = []
    for v in values:
        idx = int(((v - min_v) / span) * (len(TICKS) - 1))
        res.append(TICKS[idx])
    return "".join(res)
