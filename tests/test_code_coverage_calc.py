import unittest
from activity_lab.code_coverage_calc import calculate_coverage

class TestCodeCoverageCalc(unittest.TestCase):
    def test_coverage(self):
        self.assertEqual(calculate_coverage(100, 95), 95.0)
        self.assertEqual(calculate_coverage(0, 0), 0.0)

if __name__ == "__main__":
    unittest.main()
