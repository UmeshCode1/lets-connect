"""Commit punchcard activity matrix calculation."""
from typing import List, Dict
from datetime import datetime

def build_punchcard(timestamps: List[datetime]) -> Dict[int, Dict[int, int]]:
    """Build 7x24 commit frequency matrix (day_of_week x hour)."""
    matrix = {day: {hour: 0 for hour in range(24)} for day in range(7)}
    for dt in timestamps:
        matrix[dt.weekday()][dt.hour] += 1
    return matrix
