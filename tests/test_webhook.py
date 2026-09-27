import unittest
from activity_lab.webhook import route_webhook_event

class TestWebhook(unittest.TestCase):
    def test_routing(self):
        msg = route_webhook_event("pull_request", {"action": "opened", "number": 42})
        self.assertEqual(msg, "PR #42 opened")

if __name__ == "__main__":
    unittest.main()
