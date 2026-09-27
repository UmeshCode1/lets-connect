import unittest
from activity_lab.branch_naming import is_valid_branch_name

class TestBranchNaming(unittest.TestCase):
    def test_valid_names(self):
        self.assertTrue(is_valid_branch_name("feature/user-authentication"))
        self.assertTrue(is_valid_branch_name("bugfix/login-redirect-loop"))

    def test_invalid_names(self):
        self.assertFalse(is_valid_branch_name("my_branch"))
        self.assertFalse(is_valid_branch_name("Feature/WrongCase"))

if __name__ == "__main__":
    unittest.main()
