import unittest
from activity_lab.ci_matrix import build_test_matrix

class TestCiMatrix(unittest.TestCase):
    def test_matrix(self):
        mat = build_test_matrix(["3.10", "3.11"], ["ubuntu-latest"])
        self.assertEqual(len(mat["strategy"]["matrix"]["python-version"]), 2)

if __name__ == "__main__":
    unittest.main()
