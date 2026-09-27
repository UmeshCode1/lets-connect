import unittest
from activity_lab.security_policy import generate_security_policy

class TestSecurityPolicy(unittest.TestCase):
    def test_policy(self):
        pol = generate_security_policy("lets-connect", "security@example.com")
        self.assertIn("# Security Policy", pol)
        self.assertIn("security@example.com", pol)

if __name__ == "__main__":
    unittest.main()
