import unittest
from activity_lab.semantic_release import determine_bump

class TestSemanticRelease(unittest.TestCase):
    def test_bumps(self):
        self.assertEqual(determine_bump(["feat", "fix"]), "minor")
        self.assertEqual(determine_bump(["fix", "chore"]), "patch")
        self.assertEqual(determine_bump(["feat!", "fix"]), "major")

if __name__ == "__main__":
    unittest.main()
