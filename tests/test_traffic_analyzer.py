import unittest
from activity_lab.traffic_analyzer import aggregate_traffic

class TestTrafficAnalyzer(unittest.TestCase):
    def test_traffic(self):
        stats = [{"count": 100, "uniques": 20}, {"count": 150, "uniques": 35}]
        res = aggregate_traffic(stats)
        self.assertEqual(res["total_views"], 250)
        self.assertEqual(res["total_uniques"], 55)

if __name__ == "__main__":
    unittest.main()
