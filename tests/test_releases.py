import unittest
from activity_lab.releases import format_release_notes

class TestReleases(unittest.TestCase):
    def test_release_notes_format(self):
        notes = format_release_notes("v1.0.0", "Major Release", ["New UI", "Better performance"])
        self.assertIn("## Major Release (v1.0.0)", notes)
        self.assertIn("- New UI", notes)

if __name__ == "__main__":
    unittest.main()
