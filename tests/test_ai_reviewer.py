"""Unit tests for the AI PR Reviewer module."""

from __future__ import annotations

import unittest
from unittest.mock import patch, MagicMock

from activity_lab.ai_reviewer import (
    ReviewResult,
    generate_heuristic_review,
    review_pull_request,
    call_anthropic_api,
)


class TestAiReviewer(unittest.TestCase):
    def test_heuristic_review_conventional_title(self):
        result = generate_heuristic_review(
            title="feat(ui): add dashboard layout",
            body="Implements dashboard layout.\n\nCo-authored-by: Alice <alice@example.com>",
            diff="+ def render():\n+     pass\n- def old_render():\n-     pass",
            commit_messages=["feat(ui): initial layout", "feat(ui): add widgets"],

        )
        self.assertTrue(result.is_conventional)
        self.assertEqual(result.risk_level, "LOW")
        self.assertEqual(result.source, "heuristic")
        self.assertIn("Alice <alice@example.com>", result.suggested_coauthors)
        self.assertTrue(len(result.highlights) > 0)

    def test_heuristic_review_high_risk_detection(self):
        result = generate_heuristic_review(
            title="fix: delete credentials token and drop table users",
            body="Security fix",
            diff="DROP TABLE users;",
        )
        self.assertEqual(result.risk_level, "HIGH")

    def test_review_markdown_formatting(self):
        result = ReviewResult(
            title="docs: update architecture diagram",
            is_conventional=True,
            summary="All diagrams updated.",
            highlights=["Added sequence diagram"],
            suggested_coauthors=["Bob <bob@example.com>"],
            risk_level="LOW",
            source="heuristic",
        )
        md = result.to_markdown()
        self.assertIn("### 🤖 GitHub Activity Lab - AI PR Review", md)
        self.assertIn("✅ `docs: update architecture diagram`", md)
        self.assertIn("🟢 Low Risk", md)
        self.assertIn("Bob <bob@example.com>", md)

    @patch("activity_lab.ai_reviewer.call_anthropic_api")
    def test_review_pull_request_with_api_mock(self, mock_api):
        mock_api.return_value = '```json\n{"summary": "API Review Succeeded", "highlights": ["Test highlight"], "suggested_coauthors": [], "risk_level": "LOW"}\n```'
        result = review_pull_request(
            title="feat: add something",
            api_key="sk-ant-test-key",
            model="claude-3-7-sonnet-20250219",
        )
        self.assertEqual(result.summary, "API Review Succeeded")
        self.assertIn("claude-api", result.source)
        self.assertEqual(result.risk_level, "LOW")

    def test_review_fallback_when_no_api_key(self):
        result = review_pull_request(
            title="fix(ci): fix workflow permissions",
            body="Clean update",
        )
        self.assertEqual(result.source, "heuristic")
        self.assertTrue(result.is_conventional)


if __name__ == "__main__":
    unittest.main()
