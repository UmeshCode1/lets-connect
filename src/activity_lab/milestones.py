"""GitHub Achievement milestone definitions, tier thresholds, and progress tracking."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, List, Optional


class Tier(str, Enum):
    NONE = "None"
    DEFAULT = "Default"
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"


@dataclass(frozen=True)
class BadgeDefinition:
    """Definition of an official GitHub Achievement badge."""
    slug: str
    display_name: str
    is_active: bool
    is_tiered: bool
    requires_public_repo: bool
    requires_peer: bool
    description: str
    thresholds: dict[Tier, int]

    def evaluate_tier(self, count: int) -> tuple[Tier, Optional[Tier], int]:
        """Determine current tier, next tier, and remaining count needed."""
        if not self.is_active or count <= 0:
            next_t = Tier.DEFAULT if Tier.DEFAULT in self.thresholds else None
            req = self.thresholds.get(next_t, 0) if next_t else 0
            return Tier.NONE, next_t, req

        current_tier = Tier.NONE
        next_tier: Optional[Tier] = None
        remaining_needed = 0

        # Ordered tier progression
        ordered_tiers = [Tier.DEFAULT, Tier.BRONZE, Tier.SILVER, Tier.GOLD]

        for idx, tier in enumerate(ordered_tiers):
            if tier not in self.thresholds:
                continue
            threshold = self.thresholds[tier]
            if count >= threshold:
                current_tier = tier
            else:
                next_tier = tier
                remaining_needed = threshold - count
                break

        return current_tier, next_tier, remaining_needed


# Official Achievement specifications verified against current GitHub documentation:
ACHIEVEMENT_REGISTRY: dict[str, BadgeDefinition] = {
    "pull-shark": BadgeDefinition(
        slug="pull-shark",
        display_name="Pull Shark",
        is_active=True,
        is_tiered=True,
        requires_public_repo=True,
        requires_peer=False,
        description="Merged your own pull requests into public repositories.",
        thresholds={
            Tier.DEFAULT: 2,
            Tier.BRONZE: 16,
            Tier.SILVER: 128,
            Tier.GOLD: 1024,
        },
    ),
    "pair-extraordinaire": BadgeDefinition(
        slug="pair-extraordinaire",
        display_name="Pair Extraordinaire",
        is_active=True,
        is_tiered=True,
        requires_public_repo=True,
        requires_peer=True,
        description="Co-authored a commit in a pull request that was merged.",
        thresholds={
            Tier.DEFAULT: 1,
            Tier.BRONZE: 10,
            Tier.SILVER: 24,
            Tier.GOLD: 48,
        },
    ),
    "starstruck": BadgeDefinition(
        slug="starstruck",
        display_name="Starstruck",
        is_active=True,
        is_tiered=True,
        requires_public_repo=True,
        requires_peer=True,
        description="Created a single public repository that reached a milestone number of stars.",
        thresholds={
            Tier.DEFAULT: 16,
            Tier.BRONZE: 128,
            Tier.SILVER: 512,
            Tier.GOLD: 4096,
        },
    ),
    "galaxy-brain": BadgeDefinition(
        slug="galaxy-brain",
        display_name="Galaxy Brain",
        is_active=True,
        is_tiered=True,
        requires_public_repo=True,
        requires_peer=True,
        description="Had your answer marked as the accepted answer in GitHub Discussions (non-self).",
        thresholds={
            Tier.DEFAULT: 2,
            Tier.BRONZE: 8,
            Tier.SILVER: 16,
            Tier.GOLD: 32,
        },
    ),
    "quickdraw": BadgeDefinition(
        slug="quickdraw",
        display_name="Quickdraw",
        is_active=True,
        is_tiered=False,
        requires_public_repo=True,
        requires_peer=False,
        description="Closed an issue or pull request within 5 minutes of opening it.",
        thresholds={
            Tier.DEFAULT: 1,
        },
    ),
    "yolo": BadgeDefinition(
        slug="yolo",
        display_name="YOLO",
        is_active=True,
        is_tiered=False,
        requires_public_repo=True,
        requires_peer=False,
        description="Merged a pull request without code reviews into an unprotected branch.",
        thresholds={
            Tier.DEFAULT: 1,
        },
    ),
    "public-sponsor": BadgeDefinition(
        slug="public-sponsor",
        display_name="Public Sponsor",
        is_active=True,
        is_tiered=False,
        requires_public_repo=False,
        requires_peer=True,
        description="Publicly sponsored open source work through GitHub Sponsors.",
        thresholds={
            Tier.DEFAULT: 1,
        },
    ),
    "heart-on-your-sleeve": BadgeDefinition(
        slug="heart-on-your-sleeve",
        display_name="Heart On Your Sleeve",
        is_active=False,
        is_tiered=False,
        requires_public_repo=True,
        requires_peer=False,
        description="RETIRED/UNRELEASED: Reacted with a heart emoji during experimental GitHub trial.",
        thresholds={},
    ),
    "open-sourcerer": BadgeDefinition(
        slug="open-sourcerer",
        display_name="Open Sourcerer",
        is_active=False,
        is_tiered=False,
        requires_public_repo=True,
        requires_peer=True,
        description="RETIRED/UNRELEASED: Merged PRs across multiple open source repositories during experimental trial.",
        thresholds={},
    ),
}


@dataclass
class MilestoneProgress:
    """Calculated progress snapshot for an achievement."""
    badge: BadgeDefinition
    current_count: int
    current_tier: Tier
    next_tier: Optional[Tier]
    remaining_for_next: int


def calculate_progress(slug: str, count: int) -> Optional[MilestoneProgress]:
    """Calculate progress toward a specific achievement given a count."""
    badge = ACHIEVEMENT_REGISTRY.get(slug)
    if not badge:
        return None
    cur, nxt, rem = badge.evaluate_tier(count)
    return MilestoneProgress(
        badge=badge,
        current_count=count,
        current_tier=cur,
        next_tier=nxt,
        remaining_for_next=rem,
    )
