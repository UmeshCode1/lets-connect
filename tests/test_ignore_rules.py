import unittest
from activity_lab.ignore_rules import should_ignore

class TestIgnoreRules(unittest.TestCase):
    def test_ignore(self):
        patterns = ["*.pyc", "__pycache__", "build/"]
        self.assertTrue(should_ignore("foo.pyc", patterns))
        self.assertFalse(should_ignore("foo.py", patterns))

if __name__ == "__main__":
    unittest.main()
