import unittest
from activity_lab.stargazer_chart import render_sparkline

class TestStargazerChart(unittest.TestCase):
    def test_sparkline(self):
        line = render_sparkline([1, 5, 2, 8, 10])
        self.assertEqual(len(line), 5)

if __name__ == "__main__":
    unittest.main()
