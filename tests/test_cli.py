"""Unit tests for the CLI handlers."""

import io
import unittest
from unittest.mock import patch
from activity_lab.cli import main


class TestCLI(unittest.TestCase):
    @patch("sys.stdout", new_callable=io.StringIO)
    def test_cli_milestones(self, mock_stdout):
        exit_code = main(["milestones"])
        self.assertEqual(exit_code, 0)
        output = mock_stdout.getvalue()
        self.assertIn("Pull Shark", output)
        self.assertIn("Pair Extraordinaire", output)
        self.assertIn("Galaxy Brain", output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_cli_format_coauthor(self, mock_stdout):
        exit_code = main(["format-coauthor", "--name", "Ada Lovelace", "--email", "ada@example.com"])
        self.assertEqual(exit_code, 0)
        output = mock_stdout.getvalue()
        self.assertIn("Co-authored-by: Ada Lovelace <ada@example.com>", output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_cli_run_action(self, mock_stdout):
        exit_code = main(["run-action", "--repo", ".", "--limit", "5"])
        self.assertEqual(exit_code, 0)
        output = mock_stdout.getvalue()
        self.assertIn("Contribution Analytics", output)

    @patch("sys.stdout", new_callable=io.StringIO)
    def test_cli_ai_review(self, mock_stdout):
        exit_code = main(["ai-review", "--title", "feat: implement test feature"])
        self.assertEqual(exit_code, 0)
        output = mock_stdout.getvalue()
        self.assertIn("AI PR Review", output)


if __name__ == "__main__":
    unittest.main()

