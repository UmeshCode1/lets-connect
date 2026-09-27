import unittest
from activity_lab.caching import CacheStore

class TestCaching(unittest.TestCase):
    def test_cache_set_get(self):
        c = CacheStore(default_ttl=60)
        c.set("k", "v")
        self.assertEqual(c.get("k"), "v")
        self.assertIsNone(c.get("nonexistent"))

if __name__ == "__main__":
    unittest.main()
