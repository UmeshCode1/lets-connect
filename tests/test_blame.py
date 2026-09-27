import unittest
from activity_lab.blame import calculate_ownership

class TestBlame(unittest.TestCase):
    def test_ownership(self):
        authors = ["alice", "alice", "bob", "alice"]
        res = calculate_ownership(authors)
        self.assertEqual(res["alice"], 75.0)
        self.assertEqual(res["bob"], 25.0)

if __name__ == "__main__":
    unittest.main()
