"""Unit tests for achievement milestone definitions and tier calculations."""

import unittest
from activity_lab.milestones import (
    ACHIEVEMENT_REGISTRY,
    Tier,
    calculate_progress,
)


class TestMilestones(unittest.TestCase):
    def test_registry_contains_expected_achievements(self):
        expected_keys = [
            "pull-shark",
            "pair-extraordinaire",
            "starstruck",
            "galaxy-brain",
            "quickdraw",
            "yolo",
            "public-sponsor",
            "heart-on-your-sleeve",
            "open-sourcerer",
        ]
        for key in expected_keys:
            self.assertIn(key, ACHIEVEMENT_REGISTRY)

    def test_pull_shark_tier_progression(self):
        badge = ACHIEVEMENT_REGISTRY["pull-shark"]

        # Below 2
        tier, next_tier, remaining = badge.evaluate_tier(1)
        self.assertEqual(tier, Tier.NONE)
        self.assertEqual(next_tier, Tier.DEFAULT)
        self.assertEqual(remaining, 1)

        # Reached default (2)
        tier, next_tier, remaining = badge.evaluate_tier(2)
        self.assertEqual(tier, Tier.DEFAULT)
        self.assertEqual(next_tier, Tier.BRONZE)
        self.assertEqual(remaining, 14)

        # Reached Bronze (16)
        tier, next_tier, remaining = badge.evaluate_tier(16)
        self.assertEqual(tier, Tier.BRONZE)
        self.assertEqual(next_tier, Tier.SILVER)
        self.assertEqual(remaining, 112)

        # Reached Gold (1024)
        tier, next_tier, remaining = badge.evaluate_tier(1024)
        self.assertEqual(tier, Tier.GOLD)
        self.assertIsNone(next_tier)
        self.assertEqual(remaining, 0)

    def test_pair_extraordinaire_tier_progression(self):
        badge = ACHIEVEMENT_REGISTRY["pair-extraordinaire"]

        # 1 merged PR
        tier, next_tier, remaining = badge.evaluate_tier(1)
        self.assertEqual(tier, Tier.DEFAULT)
        self.assertEqual(next_tier, Tier.BRONZE)
        self.assertEqual(remaining, 9)

        # 10 merged PRs
        tier, next_tier, remaining = badge.evaluate_tier(10)
        self.assertEqual(tier, Tier.BRONZE)
        self.assertEqual(next_tier, Tier.SILVER)
        self.assertEqual(remaining, 14)

    def test_inactive_achievements(self):
        badge = ACHIEVEMENT_REGISTRY["heart-on-your-sleeve"]
        self.assertFalse(badge.is_active)
        tier, next_tier, remaining = badge.evaluate_tier(100)
        self.assertEqual(tier, Tier.NONE)

    def test_calculate_progress_helper(self):
        progress = calculate_progress("pull-shark", 5)
        self.assertIsNotNone(progress)
        self.assertEqual(progress.current_tier, Tier.DEFAULT)
        self.assertEqual(progress.next_tier, Tier.BRONZE)
        self.assertEqual(progress.remaining_for_next, 11)


if __name__ == "__main__":
    unittest.main()
