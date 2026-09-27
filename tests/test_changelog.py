import unittest
from activity_lab.changelog import build_changelog

class TestChangelog(unittest.TestCase):
    def test_grouping(self):
        msgs = ["feat: add api", "fix: resolve bug", "docs: update guide"]
        res = build_changelog(msgs)
        self.assertEqual(len(res["Features"]), 1)
        self.assertEqual(len(res["Bug Fixes"]), 1)
        self.assertEqual(len(res["Chores & Maintenance"]), 1)

if __name__ == "__main__":
    unittest.main()
