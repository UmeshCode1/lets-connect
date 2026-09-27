import unittest
from activity_lab.activity_feed import serialize_feed

class TestActivityFeed(unittest.TestCase):
    def test_feed(self):
        data = serialize_feed([{"id": "1", "content_text": "Commit merged"}])
        self.assertIn("Activity Lab Feed", data)

if __name__ == "__main__":
    unittest.main()
