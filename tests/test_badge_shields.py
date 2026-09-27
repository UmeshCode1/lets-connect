import unittest
from activity_lab.badge_shields import make_shield_badge

class TestBadgeShields(unittest.TestCase):
    def test_badge(self):
        badge = make_shield_badge("status", "passing", "brightgreen")
        self.assertIn("img.shields.io/badge/status-passing-brightgreen.svg", badge)

if __name__ == "__main__":
    unittest.main()
