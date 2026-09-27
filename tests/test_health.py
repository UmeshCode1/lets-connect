import unittest
from activity_lab.health import calculate_health_score

class TestHealth(unittest.TestCase):
    def test_full_health(self):
        files = ["README.md", "LICENSE", "CONTRIBUTING.md", "CODE_OF_CONDUCT.md"]
        res = calculate_health_score(files)
        self.assertEqual(res["score"], 100)
        self.assertEqual(len(res["missing"]), 0)

if __name__ == "__main__":
    unittest.main()
