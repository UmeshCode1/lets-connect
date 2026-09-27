import unittest
from activity_lab.tag_generator import format_release_tag

class TestTagGenerator(unittest.TestCase):
    def test_tag_creation(self):
        self.assertEqual(format_release_tag(1, 2, 3), "v1.2.3")
        self.assertEqual(format_release_tag(2, 0, 0, "rc.1"), "v2.0.0-rc.1")

if __name__ == "__main__":
    unittest.main()
