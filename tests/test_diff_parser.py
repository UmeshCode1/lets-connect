import unittest
from activity_lab.diff_parser import parse_diff_stats

class TestDiffParser(unittest.TestCase):
    def test_diff_stats(self):
        diff = "--- a.py\n+++ b.py\n+def foo():\n-def bar():\n+    pass"
        res = parse_diff_stats(diff)
        self.assertEqual(res["additions"], 2)
        self.assertEqual(res["deletions"], 1)

if __name__ == "__main__":
    unittest.main()
