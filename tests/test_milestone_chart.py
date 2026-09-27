import unittest
from activity_lab.milestone_chart import generate_milestone_mermaid

class TestMilestoneChart(unittest.TestCase):
    def test_mermaid_generation(self):
        chart = generate_milestone_mermaid({"Default": 2, "Bronze": 16})
        self.assertIn("graph LR", chart)
        self.assertIn("Default --> Bronze", chart)

if __name__ == "__main__":
    unittest.main()
