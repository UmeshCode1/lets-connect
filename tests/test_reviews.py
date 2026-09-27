"""Unit tests for Pull Request code review participation tracking."""

import unittest

from activity_lab.reviews import aggregate_reviews


class TestReviews(unittest.TestCase):
    """Test suite for aggregate_reviews logic."""

    def test_empty_reviews(self):
        summary = aggregate_reviews([])
        self.assertEqual(summary.total_reviews, 0)
        self.assertEqual(summary.approved, 0)
        self.assertEqual(summary.approval_rate, 0.0)
        self.assertEqual(len(summary.reviews_by_user), 0)

    def test_aggregation_and_breakdown(self):
        sample_reviews = [
            {"user": {"login": "alice"}, "state": "APPROVED"},
            {"user": {"login": "alice"}, "state": "COMMENTED"},
            {"user": {"login": "bob"}, "state": "CHANGES_REQUESTED"},
            {"user": {"login": "charlie"}, "state": "APPROVED"},
            {"user": {"login": "charlie"}, "state": "DISMISSED"},
        ]

        summary = aggregate_reviews(sample_reviews)
        self.assertEqual(summary.total_reviews, 5)
        self.assertEqual(summary.approved, 2)
        self.assertEqual(summary.changes_requested, 1)
        self.assertEqual(summary.commented, 1)
        self.assertEqual(summary.dismissed, 1)
        self.assertEqual(summary.approval_rate, 40.0)

        self.assertEqual(summary.reviews_by_user["alice"]["APPROVED"], 1)
        self.assertEqual(summary.reviews_by_user["alice"]["COMMENTED"], 1)
        self.assertEqual(summary.reviews_by_user["bob"]["CHANGES_REQUESTED"], 1)

    def test_filter_by_target_user(self):
        sample_reviews = [
            {"user": {"login": "alice"}, "state": "APPROVED"},
            {"user": {"login": "bob"}, "state": "APPROVED"},
            {"user": {"login": "alice"}, "state": "COMMENTED"},
        ]

        summary = aggregate_reviews(sample_reviews, target_user="alice")
        self.assertEqual(summary.total_reviews, 2)
        self.assertEqual(summary.approved, 1)
        self.assertEqual(summary.commented, 1)
        self.assertNotIn("bob", summary.reviews_by_user)
        self.assertIn("alice", summary.reviews_by_user)


if __name__ == "__main__":
    unittest.main()
