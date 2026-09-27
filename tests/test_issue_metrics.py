import unittest
from datetime import datetime, timedelta
from activity_lab.issue_metrics import average_resolution_days

class TestIssueMetrics(unittest.TestCase):
    def test_avg_days(self):
        t0 = datetime(2026, 9, 20)
        issues = [{"created_at": t0, "closed_at": t0 + timedelta(days=4)}]
        self.assertEqual(average_resolution_days(issues), 4.0)

if __name__ == "__main__":
    unittest.main()
