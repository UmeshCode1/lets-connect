"""Unit tests for the export formatting module."""

import json
import unittest

from activity_lab.parser import parse_commit_message
from activity_lab.stats import calculate_stats
from activity_lab.export import export_stats


def _make_stats():
    commits = [
        parse_commit_message("feat: initial", author_name="Alice", author_email="alice@example.com"),
        parse_commit_message(
            "feat: collab\n\nCo-authored-by: Bob Dev <bob@example.com>",
            author_name="Alice", author_email="alice@example.com",
        ),
        parse_commit_message("fix: bug", author_name="Bob", author_email="bob@example.com"),
    ]
    return calculate_stats(commits)


class TestExport(unittest.TestCase):
    def test_json_export_structure(self):
        stats = _make_stats()
        result = export_stats(stats, fmt="json")
        data = json.loads(result)
        self.assertIn("summary", data)
        self.assertIn("contributors", data)
        self.assertEqual(data["summary"]["total_commits"], 3)
        self.assertEqual(data["summary"]["commits_with_co_authors"], 1)
        self.assertAlmostEqual(data["summary"]["co_authored_percentage"], 33.33, places=1)

    def test_csv_export_has_header(self):
        stats = _make_stats()
        result = export_stats(stats, fmt="csv")
        lines = result.strip().splitlines()
        self.assertGreater(len(lines), 1)
        self.assertIn("email", lines[0])
        self.assertIn("total_contributions", lines[0])

    def test_table_export_contains_names(self):
        stats = _make_stats()
        result = export_stats(stats, fmt="table")
        self.assertIn("Alice", result)
        self.assertIn("Bob", result)

    def test_empty_stats_csv(self):
        from activity_lab.stats import RepositoryStats
        empty = RepositoryStats(total_commits=0, commits_with_co_authors=0)
        result = export_stats(empty, fmt="csv")
        self.assertEqual(result, "")


if __name__ == "__main__":
    unittest.main()
