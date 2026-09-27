"""Contribution streak calculation engine."""
from datetime import date, timedelta
from typing import List, Dict

def calculate_streaks(dates: List[date]) -> Dict[str, int]:
    """Calculate current and longest contribution day streaks."""
    if not dates:
        return {"current_streak": 0, "longest_streak": 0}

    unique_days = sorted(set(dates))
    longest = 1
    current = 1

    for i in range(1, len(unique_days)):
        if unique_days[i] == unique_days[i - 1] + timedelta(days=1):
            current += 1
            if current > longest:
                longest = current
        else:
            current = 1

    return {"current_streak": current, "longest_streak": longest}
