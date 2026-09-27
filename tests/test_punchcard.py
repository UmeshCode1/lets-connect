import unittest
from datetime import datetime
from activity_lab.punchcard import build_punchcard

class TestPunchcard(unittest.TestCase):
    def test_punchcard_matrix(self):
        times = [datetime(2026, 9, 28, 14, 0), datetime(2026, 9, 28, 14, 30)]
        matrix = build_punchcard(times)
        self.assertEqual(matrix[0][14], 2)
        self.assertEqual(matrix[0][10], 0)

if __name__ == "__main__":
    unittest.main()
