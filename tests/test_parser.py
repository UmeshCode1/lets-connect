"""Unit tests for the git message and trailer parser."""

import unittest
from activity_lab.parser import parse_commit_message, CoAuthor


class TestParser(unittest.TestCase):
    def test_simple_commit_message(self):
        msg = "feat: add user authentication\n\nImplement OAuth2 and session handlers."
        meta = parse_commit_message(msg, sha="abc1234", author_name="Umesh", author_email="umesh@example.com")
        self.assertEqual(meta.subject, "feat: add user authentication")
        self.assertIn("Implement OAuth2", meta.body)
        self.assertFalse(meta.has_co_authors)
        self.assertEqual(len(meta.trailers), 0)

    def test_single_co_author(self):
        msg = (
            "fix: correct edge case in stats calculation\n\n"
            "This fixes off-by-one errors.\n\n"
            "Co-authored-by: Alex River <alex.river@example.com>"
        )
        meta = parse_commit_message(msg)
        self.assertTrue(meta.has_co_authors)
        self.assertEqual(len(meta.co_authors), 1)
        self.assertEqual(meta.co_authors[0].name, "Alex River")
        self.assertEqual(meta.co_authors[0].email, "alex.river@example.com")
        self.assertEqual(
            meta.co_authors[0].format_trailer(),
            "Co-authored-by: Alex River <alex.river@example.com>",
        )

    def test_multiple_co_authors_and_custom_trailers(self):
        msg = (
            "refactor: modularize parser\n\n"
            "Break down monolithic classes.\n\n"
            "Signed-off-by: Umesh Patel <umesh.code1@gmail.com>\n"
            "Co-authored-by: Alice Developer <alice@example.com>\n"
            "Co-authored-by: Bob Reviewer <bob@example.com>\n"
            "Fixes: #42"
        )
        meta = parse_commit_message(msg)
        self.assertEqual(len(meta.co_authors), 2)
        self.assertEqual(meta.co_authors[0].name, "Alice Developer")
        self.assertEqual(meta.co_authors[1].name, "Bob Reviewer")
        self.assertIn("Signed-off-by", meta.trailers)
        self.assertIn("Fixes", meta.trailers)
        self.assertEqual(meta.trailers["Fixes"], ["#42"])

    def test_empty_message(self):
        meta = parse_commit_message("")
        self.assertEqual(meta.subject, "")
        self.assertEqual(meta.body, "")
        self.assertFalse(meta.has_co_authors)

    def test_crlf_line_endings(self):
        """Regression test: Windows CRLF line endings must not break trailer detection."""
        msg = "fix: resolve auth edge case\r\n\r\nHandle OAuth token refresh on expiry.\r\n\r\nCo-authored-by: Sam Windows <sam@example.com>"
        meta = parse_commit_message(msg)
        self.assertEqual(meta.subject, "fix: resolve auth edge case")
        self.assertTrue(meta.has_co_authors)
        self.assertEqual(meta.co_authors[0].name, "Sam Windows")
        self.assertEqual(meta.co_authors[0].email, "sam@example.com")


if __name__ == "__main__":
    unittest.main()
