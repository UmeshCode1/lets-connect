import unittest
from activity_lab.coauthor_checker import validate_coauthor_string

class TestCoauthorChecker(unittest.TestCase):
    def test_valid_syntax(self):
        line = "Co-authored-by: Daksh Sahni <daksh@example.com>"
        self.assertTrue(validate_coauthor_string(line))

    def test_invalid_syntax(self):
        self.assertFalse(validate_coauthor_string("Co-authored-by: Daksh Sahni"))
        self.assertFalse(validate_coauthor_string("Invalid trailer"))

if __name__ == "__main__":
    unittest.main()
