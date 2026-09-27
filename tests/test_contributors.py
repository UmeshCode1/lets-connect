import unittest
from activity_lab.contributors import make_contributors_table

class TestContributors(unittest.TestCase):
    def test_table_output(self):
        users = [{"name": "Umesh", "role": "Author", "url": "https://github.com/UmeshCode1"}]
        table = make_contributors_table(users)
        self.assertIn("| Contributor |", table)
        self.assertIn("**Umesh**", table)

if __name__ == "__main__":
    unittest.main()
