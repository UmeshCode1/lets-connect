import unittest
import json
from activity_lab.audit_log import create_audit_entry

class TestAuditLog(unittest.TestCase):
    def test_entry(self):
        line = create_audit_entry("merge_pr", "UmeshCode1", {"pr": 48})
        obj = json.loads(line)
        self.assertEqual(obj["action"], "merge_pr")
        self.assertEqual(obj["actor"], "UmeshCode1")

if __name__ == "__main__":
    unittest.main()
