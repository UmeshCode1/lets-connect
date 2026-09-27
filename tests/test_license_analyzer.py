import unittest
from activity_lab.license_analyzer import identify_license

class TestLicenseAnalyzer(unittest.TestCase):
    def test_identify(self):
        self.assertEqual(identify_license("mit"), "MIT License")
        self.assertEqual(identify_license("unknown"), "Custom / Proprietary")

if __name__ == "__main__":
    unittest.main()
