import unittest
from activity_lab.commit_linter import validate_commit_message

class TestCommitLinter(unittest.TestCase):
    def test_valid_commits(self):
        self.assertTrue(validate_commit_message("feat: implement oauth login"))
        self.assertTrue(validate_commit_message("fix(api): handle null payload"))
        self.assertTrue(validate_commit_message("refactor!: redesign database schema"))

    def test_invalid_commits(self):
        self.assertFalse(validate_commit_message("updated files"))
        self.assertFalse(validate_commit_message("Fixed bug"))

if __name__ == "__main__":
    unittest.main()
