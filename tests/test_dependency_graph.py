import unittest
from activity_lab.dependency_graph import build_dependency_graph

class TestDependencyGraph(unittest.TestCase):
    def test_graph(self):
        raw = {"app": ["requests", "urllib3"]}
        g = build_dependency_graph(raw)
        self.assertIn("app", g)
        self.assertIn("requests", g)
        self.assertIn("urllib3", g)

if __name__ == "__main__":
    unittest.main()
