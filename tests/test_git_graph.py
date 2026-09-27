import unittest
from activity_lab.git_graph import format_ascii_graph

class TestGitGraph(unittest.TestCase):
    def test_format_graph(self):
        res = format_ascii_graph(["commit A", "commit B"])
        self.assertIn("* commit A", res)
        self.assertIn("* commit B", res)

if __name__ == "__main__":
    unittest.main()
