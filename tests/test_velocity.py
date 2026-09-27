"""Unit tests for stargazer velocity and milestone projections."""

from datetime import datetime, timedelta, timezone
import unittest

from activity_lab.milestones import Tier
from activity_lab.velocity import calculate_star_velocity


class TestVelocity(unittest.TestCase):
    """Test suite for calculate_star_velocity logic."""

    def test_zero_stargazers(self):
        now = datetime(2026, 9, 28, 12, 0, 0, tzinfo=timezone.utc)
        report = calculate_star_velocity([], now=now)
        self.assertEqual(report.total_stars, 0)
        self.assertEqual(report.daily_velocity_7d, 0.0)
        self.assertIsNone(report.current_tier)
        self.assertEqual(report.next_tier, Tier.DEFAULT)
        self.assertEqual(report.stars_needed_for_next_tier, 16)
        self.assertIsNone(report.projected_date_next_tier)

    def test_velocity_and_momentum_positive(self):
        now = datetime(2026, 9, 28, 12, 0, 0, tzinfo=timezone.utc)
        # 14 stars in the past 7 days (2 stars/day)
        # 7 stars in the previous 7 days (1 star/day)
        recent_timestamps = [now - timedelta(days=i) for i in range(1, 8)] * 2
        prev_timestamps = [now - timedelta(days=8 + i) for i in range(7)]
        all_timestamps = recent_timestamps + prev_timestamps

        report = calculate_star_velocity(all_timestamps, now=now)
        self.assertEqual(report.total_stars, 21)
        self.assertEqual(report.daily_velocity_7d, 2.0)
        self.assertEqual(report.weekly_momentum_pct, 100.0)
        self.assertEqual(report.current_tier, Tier.DEFAULT)  # Threshold 16 reached
        self.assertEqual(report.next_tier, Tier.BRONZE)     # Next is 128
        self.assertEqual(report.stars_needed_for_next_tier, 107)  # 128 - 21
        self.assertIsNotNone(report.projected_date_next_tier)
        self.assertGreater(report.projected_days_to_next_tier, 0)


if __name__ == "__main__":
    unittest.main()
