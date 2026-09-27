import unittest
from datetime import datetime, timedelta
from activity_lab.pr_metrics import compute_cycle_hours

class TestPRMetrics(unittest.TestCase):
    def test_cycle_hours(self):
        t0 = datetime(2026, 9, 28, 10, 0)
        t1 = t0 + timedelta(hours=3, minutes=30)
        hours = compute_cycle_hours(t0, t1)
        self.assertEqual(hours, 3.5)

if __name__ == "__main__":
    unittest.main()
