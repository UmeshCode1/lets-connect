"""Unit tests for contributor statistics calculation."""

import unittest
from activity_lab.parser import parse_commit_message
from activity_lab.stats import calculate_stats


class TestStats(unittest.TestCase):
    def test_empty_commits(self):
        stats = calculate_stats([])
        self.assertEqual(stats.total_commits, 0)
        self.assertEqual(stats.commits_with_co_authors, 0)
        self.assertEqual(stats.co_authored_percentage, 0.0)
        self.assertEqual(len(stats.contributors), 0)

    def test_stats_with_commits_and_co_authors(self):
        c1 = parse_commit_message("feat: initial commit", author_name="Umesh", author_email="umesh@example.com")
        c2 = parse_commit_message(
            "feat: add feature A\n\nCo-authored-by: Sarah Code <sarah@example.com>",
            author_name="Umesh",
            author_email="umesh@example.com",
        )
        c3 = parse_commit_message("docs: update readme", author_name="Sarah", author_email="sarah@example.com")

        stats = calculate_stats([c1, c2, c3])
        self.assertEqual(stats.total_commits, 3)
        self.assertEqual(stats.commits_with_co_authors, 1)
        self.assertAlmostEqual(stats.co_authored_percentage, 33.333333, places=2)

        # Umesh: 2 primary commits
        umesh_summary = stats.contributors["umesh@example.com"]
        self.assertEqual(umesh_summary.primary_commits, 2)
        self.assertEqual(umesh_summary.co_authored_commits, 0)

        # Sarah: 1 primary commit, 1 co-authored
        sarah_summary = stats.contributors["sarah@example.com"]
        self.assertEqual(sarah_summary.primary_commits, 1)
        self.assertEqual(sarah_summary.co_authored_commits, 1)
        self.assertEqual(sarah_summary.total_contributions, 2)


if __name__ == "__main__":
    unittest.main()
