import unittest
from activity_lab.markdown_report import generate_markdown_report

class TestMarkdownReport(unittest.TestCase):
    def test_report_generation(self):
        data = {"repo": "UmeshCode1/lets-connect", "commits": 50, "prs": 15, "contributors": 2}
        rep = generate_markdown_report(data)
        self.assertIn("# Repository Activity Report", rep)
        self.assertIn("Total Commits", rep)
        self.assertIn("50", rep)

if __name__ == "__main__":
    unittest.main()
