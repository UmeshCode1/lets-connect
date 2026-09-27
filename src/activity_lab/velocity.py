"""Stargazer velocity, momentum, and Starstruck milestone projection module."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from typing import List, Optional

from activity_lab.milestones import ACHIEVEMENT_REGISTRY, Tier


@dataclass
class VelocityReport:
    """Analysis of repository stargazer acquisition rate and projected milestones."""

    total_stars: int
    daily_velocity_7d: float
    daily_velocity_30d: float
    weekly_momentum_pct: float
    current_tier: Optional[Tier]
    next_tier: Optional[Tier]
    stars_needed_for_next_tier: int
    projected_days_to_next_tier: Optional[int]
    projected_date_next_tier: Optional[str]


def calculate_star_velocity(
    timestamps: List[datetime],
    now: Optional[datetime] = None,
) -> VelocityReport:
    """Calculate star acquisition rate, momentum, and estimate time to next Starstruck tier.

    :param timestamps: List of datetime objects when each star was added.
    :param now: Current reference time (defaults to timezone.utc now).
    :return: VelocityReport with velocity, momentum, and projected milestone dates.
    """
    if now is None:
        now = datetime.now(timezone.utc)

    # Ensure all timestamps are timezone-aware (UTC)
    normalized = []
    for ts in timestamps:
        if ts.tzinfo is None:
            ts = ts.replace(tzinfo=timezone.utc)
        normalized.append(ts)
    normalized.sort()

    total_stars = len(normalized)

    # Rolling window counts
    t_7d = now - timedelta(days=7)
    t_14d = now - timedelta(days=14)
    t_30d = now - timedelta(days=30)

    stars_last_7d = sum(1 for t in normalized if t >= t_7d)
    stars_prev_7d = sum(1 for t in normalized if t_14d <= t < t_7d)
    stars_last_30d = sum(1 for t in normalized if t >= t_30d)

    daily_velocity_7d = round(stars_last_7d / 7.0, 2)
    daily_velocity_30d = round(stars_last_30d / 30.0, 2)

    # Weekly momentum: percentage change from previous 7 days to last 7 days
    if stars_prev_7d == 0:
        weekly_momentum_pct = 100.0 if stars_last_7d > 0 else 0.0
    else:
        weekly_momentum_pct = round(((stars_last_7d - stars_prev_7d) / stars_prev_7d) * 100.0, 1)

    # Starstruck milestone evaluation
    starstruck = ACHIEVEMENT_REGISTRY.get("starstruck")
    thresholds = starstruck.thresholds if starstruck else {}

    current_tier: Optional[Tier] = None
    next_tier: Optional[Tier] = None
    stars_needed = 0

    for tier, req in thresholds.items():
        if total_stars >= req:
            current_tier = tier
        else:
            next_tier = tier
            stars_needed = req - total_stars
            break

    # Time projection
    velocity_for_projection = daily_velocity_7d if daily_velocity_7d > 0 else daily_velocity_30d

    if next_tier is not None and velocity_for_projection > 0:
        days_needed = int(round(stars_needed / velocity_for_projection))
        proj_date = (now + timedelta(days=days_needed)).strftime("%Y-%m-%d")
    else:
        days_needed = None
        proj_date = None

    return VelocityReport(
        total_stars=total_stars,
        daily_velocity_7d=daily_velocity_7d,
        daily_velocity_30d=daily_velocity_30d,
        weekly_momentum_pct=weekly_momentum_pct,
        current_tier=current_tier,
        next_tier=next_tier,
        stars_needed_for_next_tier=stars_needed,
        projected_days_to_next_tier=days_needed,
        projected_date_next_tier=proj_date,
    )
