import unittest
from activity_lab.dashboard import render_dashboard

class TestDashboard(unittest.TestCase):
    def test_render(self):
        res = render_dashboard({"commits": 100, "prs": 48, "badges": 8, "gold_unlocked": 2})
        self.assertIn("Unified Analytics Dashboard", res)
        self.assertIn("Merged PRs:         48", res)

if __name__ == "__main__":
    unittest.main()
