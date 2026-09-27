import unittest
from activity_lab.codeowners import resolve_owner

class TestCodeowners(unittest.TestCase):
    def test_matching(self):
        rules = [("*", "@global-team"), ("*.py", "@python-lead")]
        self.assertEqual(resolve_owner("main.py", rules), "@python-lead")
        self.assertEqual(resolve_owner("README.md", rules), "@global-team")

if __name__ == "__main__":
    unittest.main()
