"""Pull Request code review tracking and participation analytics module."""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List, Optional


@dataclass
class ReviewSummary:
    """Aggregated metrics for code review participation."""

    total_reviews: int = 0
    approved: int = 0
    changes_requested: int = 0
    commented: int = 0
    dismissed: int = 0
    reviews_by_user: Dict[str, Dict[str, int]] = field(default_factory=dict)

    @property
    def approval_rate(self) -> float:
        """Percentage of reviews that were approvals."""
        if self.total_reviews == 0:
            return 0.0
        return round((self.approved / self.total_reviews) * 100.0, 1)


def aggregate_reviews(
    reviews: List[Dict[str, Any]],
    target_user: Optional[str] = None,
) -> ReviewSummary:
    """Aggregate a list of GitHub pull request review payloads into ReviewSummary metrics.

    :param reviews: List of review dicts returned by the GitHub API.
    :param target_user: Optional username to filter reviews for a specific reviewer.
    :return: ReviewSummary containing totals, breakdown, and reviewer distribution.
    """
    summary = ReviewSummary()

    for rev in reviews:
        user_info = rev.get("user") or {}
        reviewer = user_info.get("login") or "unknown"

        if target_user and reviewer.lower() != target_user.lower():
            continue

        state = (rev.get("state") or "").upper()
        if not state:
            continue

        summary.total_reviews += 1

        if reviewer not in summary.reviews_by_user:
            summary.reviews_by_user[reviewer] = {
                "APPROVED": 0,
                "CHANGES_REQUESTED": 0,
                "COMMENTED": 0,
                "DISMISSED": 0,
            }

        if state == "APPROVED":
            summary.approved += 1
            summary.reviews_by_user[reviewer]["APPROVED"] += 1
        elif state == "CHANGES_REQUESTED":
            summary.changes_requested += 1
            summary.reviews_by_user[reviewer]["CHANGES_REQUESTED"] += 1
        elif state == "COMMENTED":
            summary.commented += 1
            summary.reviews_by_user[reviewer]["COMMENTED"] += 1
        elif state == "DISMISSED":
            summary.dismissed += 1
            summary.reviews_by_user[reviewer]["DISMISSED"] += 1

    return summary
