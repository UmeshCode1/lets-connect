import unittest
from activity_lab.summary import format_kpi_card

class TestSummary(unittest.TestCase):
    def test_kpi_card(self):
        card = format_kpi_card("Commits", 120, "Last 30 days")
        self.assertIn("Commits", card)
        self.assertIn("120", card)

if __name__ == "__main__":
    unittest.main()
