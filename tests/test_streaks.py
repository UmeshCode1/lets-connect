import unittest
from datetime import date
from activity_lab.streaks import calculate_streaks

class TestStreaks(unittest.TestCase):
    def test_streaks(self):
        days = [date(2026, 9, 25), date(2026, 9, 26), date(2026, 9, 27)]
        res = calculate_streaks(days)
        self.assertEqual(res["longest_streak"], 3)
        self.assertEqual(res["current_streak"], 3)

    def test_empty_streaks(self):
        res = calculate_streaks([])
        self.assertEqual(res["current_streak"], 0)

if __name__ == "__main__":
    unittest.main()
