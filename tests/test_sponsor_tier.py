import unittest
from activity_lab.sponsor_tier import generate_funding_yml

class TestSponsorTier(unittest.TestCase):
    def test_funding_generation(self):
        cfg = {"github": ["UmeshCode1"]}
        yml = generate_funding_yml(cfg)
        self.assertIn("github: [UmeshCode1]", yml)

if __name__ == "__main__":
    unittest.main()
