"""Unit tests for the GitHub Action runner module."""

from __future__ import annotations

import unittest
from unittest.mock import patch, MagicMock

from activity_lab.action_runner import evaluate_action
from activity_lab.parser import CommitMetadata, CoAuthor


class TestActionRunner(unittest.TestCase):
    @patch("activity_lab.action_runner.read_git_history")
    def test_evaluate_action_success_path(self, mock_read):
        mock_read.return_value = [
            CommitMetadata(
                sha="abc1234567890",
                author_name="Alice Smith",
                author_email="alice@example.com",
                subject="feat: add telemetry logging",
                body="",
                co_authors=[CoAuthor(name="Bob Jones", email="bob@example.com")],
            ),
            CommitMetadata(
                sha="def1234567890",
                author_name="Alice Smith",
                author_email="alice@example.com",
                subject="fix: resolve memory leak",
                body="",
            ),
        ]

        exit_code, summary_md, outputs = evaluate_action(
            repo_path=".",
            limit=10,
            enforce_coauthors=True,
            enforce_conventional=True,
        )

        self.assertEqual(exit_code, 0)
        self.assertEqual(outputs["compliance-status"], "success")
        self.assertEqual(outputs["total-commits"], "2")
        self.assertEqual(outputs["co-authored-commits"], "1")
        self.assertIn("Contribution Analytics", summary_md)
        self.assertIn("Alice Smith", summary_md)

    @patch("activity_lab.action_runner.read_git_history")
    def test_evaluate_action_enforce_coauthors_failure(self, mock_read):
        mock_read.return_value = [
            CommitMetadata(
                sha="111222333444",
                author_name="Solo Dev",
                author_email="solo@example.com",
                subject="feat: solitary commit",
                body="",
            ),
        ]

        exit_code, summary_md, outputs = evaluate_action(
            repo_path=".",
            enforce_coauthors=True,
        )

        self.assertEqual(exit_code, 1)
        self.assertEqual(outputs["compliance-status"], "failure")
        self.assertIn("No valid Co-authored-by trailers found", summary_md)

    @patch("activity_lab.action_runner.read_git_history")
    def test_evaluate_action_enforce_conventional_failure(self, mock_read):
        mock_read.return_value = [
            CommitMetadata(
                sha="555666777888",
                author_name="Non Conforming",
                author_email="bad@example.com",
                subject="Updated some files without conventional format",
                body="",
            ),
        ]

        exit_code, summary_md, outputs = evaluate_action(
            repo_path=".",
            enforce_conventional=True,
        )

        self.assertEqual(exit_code, 1)
        self.assertEqual(outputs["compliance-status"], "failure")
        self.assertIn("Conventional Commit Linting", summary_md)


if __name__ == "__main__":
    unittest.main()
