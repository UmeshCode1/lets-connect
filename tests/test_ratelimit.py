import unittest
from activity_lab.ratelimit import is_rate_limited, calculate_backoff

class TestRateLimit(unittest.TestCase):
    def test_rate_limit(self):
        self.assertTrue(is_rate_limited(5))
        self.assertFalse(is_rate_limited(50))
        self.assertEqual(calculate_backoff(100.0, 80.0), 20)

if __name__ == "__main__":
    unittest.main()
