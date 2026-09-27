import unittest
from activity_lab.pr_template_gen import generate_pr_template

class TestPRTemplateGen(unittest.TestCase):
    def test_template(self):
        tmpl = generate_pr_template(["Testing Checklist"])
        self.assertIn("## Description", tmpl)
        self.assertIn("## Testing Checklist", tmpl)

if __name__ == "__main__":
    unittest.main()
