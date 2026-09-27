import unittest
from activity_lab.badges import generate_svg_badge

class TestBadges(unittest.TestCase):
    def test_badge_generation(self):
        svg = generate_svg_badge("activity", "active", "#4c1")
        self.assertIn("<svg", svg)
        self.assertIn("activity", svg)
        self.assertIn("active", svg)
        self.assertIn("#4c1", svg)

if __name__ == "__main__":
    unittest.main()
